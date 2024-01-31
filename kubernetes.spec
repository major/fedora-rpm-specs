%global with_debug   0

%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global provider                github
%global provider_tld            com
%global project                 kubernetes
%global repo                    kubernetes
# https://github.com/kubernetes/kubernetes

%global provider_prefix         %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path             kubernetes.io/

# **** release metadata ****
%global commit                  bc401b91f2782410b3fb3f9acf43a995c4de90d2
%global shortcommit             %(c=%{commit}; echo ${c:0:7})
# release major.minor version (k8s_minver); patch version (k8s_patchver)
%global k8s_name                kubernetes
%global k8s_minver              1.29
%global k8s_patchver            1
# golang 'built with' version
%global golangver               1.21.6

# last release version of these rpms prior to F40 restructure
# should not change once restructure goes into rawhide
%global switchver              1.28.4-1

# Needed otherwise "version_ldflags=$(kube::version_ldflags)" doesn't work
%global _buildshell  /bin/bash
%global _checkshell  /bin/bash

##############################################
Name:           %{k8s_name}
Version:        %{k8s_minver}.%{k8s_patchver}
Release:        %autorelease
Summary:        Open Source Production-Grade Container Scheduling And Management Platform
License:        ASL 2.0
URL:            https://%{import_path}
ExclusiveArch:  x86_64 aarch64 ppc64le s390x %{arm}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

Source101:      kube-proxy.service
Source102:      kube-apiserver.service
Source103:      kube-scheduler.service
Source104:      kube-controller-manager.service
Source105:      kubelet.service
Source106:      environ-apiserver
Source107:      environ-config
Source108:      environ-controller-manager
Source109:      environ-kubelet
Source110:      environ-kubelet.kubeconfig
Source111:      environ-proxy
Source112:      environ-scheduler
Source113:      kubernetes-accounting.conf
Source114:      kubeadm.conf
Source115:      kubernetes.conf
Source116:      %{name}.sysusers

Patch3:         build-with-debug-info.patch

##############################################
# main package components - installs kubelet, kubeadm and necessary
# configuration files. Recommends kubernetes-client.

# build requirements for kubelet, kubeadm
BuildRequires: golang >= %{golangver}
BuildRequires: make
BuildRequires: go-md2man
BuildRequires: systemd
BuildRequires: rsync

# needed per fedora documentation - may drop as /run not used
# and kube user no longer needed
BuildRequires: systemd-rpm-macros
%{?sysusers_requires_compat}

# additonal kubelet requirements
Requires:   (containerd or cri-o)
Recommends: cri-o = %{version}-%{release}
Requires:   conntrack-tools

Requires(pre): shadow-utils
Requires:      socat
Recommends:    kubernetes-client = %{version}-%{release}

# additional kubeadm requirements
Requires: containernetworking-plugins
Requires: cri-tools

# require same version for kubernetes-client if installed
Conflicts: kubernetes-client < %{version}-%{release}
Conflicts: kubernetes-client > %{version}-%{release}

# provides and obsoletes kubernetes-node and kubernetes-kubeadm
Provides: kubernetes-kubeadm = %{version}-%{release}
Obsoletes: kubernetes-kubeadm <= %{switchver}
Provides: kubernetes-node = %{version}-%{release}
Obsoletes: kubernetes-node <= %{switchver}

%description
%{summary}
Installs kubeadm and kubelet, the two basic components needed to
bootstrap, and run a cluster. The kubernetes-client sub-package,
containing kubectl, is recommended but not strictly required.
The kubernetes-client sub-package should be installed on
control plane machines.

##############################################
%package client
Summary: Kubernetes client tools

BuildRequires: golang >= %{golangver}
BuildRequires: make

Conflicts: kubernetes < %{version}-%{release}
Conflicts: kubernetes > %{version}-%{release}

%description client
Installs kubectl, the Kubernetes command line client.

##############################################
%package legacy-systemd
Summary: Legacy systemd services for control plane and/or node

BuildRequires: golang >= %{golangver}
BuildRequires: systemd
BuildRequires: rsync
BuildRequires: make
BuildRequires: go-md2man

Requires(pre): shadow-utils
Requires: kubernetes = %{version}-%{release}

# obsoletes kubernetes-master in part
Provides: kubernetes-master = %{version}-%{release}
Obsoletes: kubernetes-master <= %{switchver}

%description legacy-systemd
Legacy systemd services needed for manual installation of Kubernetes
on control plane or node machines. Not needed for most modern clusters.
If kubeadm is used to bootstrap Kubernetes then this rpm is not
needed as kubeadm will install these services as static pods in
the cluster on nodes as needed. If these services are used, enable
 all services on each control plane. Enable kube-proxy on all nodes.

##############################################
##############################################
%prep
%setup -q -n %{repo}-%{commit}

%if 0%{?with_debug}
%patch3 -p1
%endif

# src/k8s.io/kubernetes/pkg/util/certificates
# Patch the code to remove eliptic.P224 support
# For whatever reason:
# https://groups.google.com/forum/#!topic/Golang-nuts/Oq4rouLEvrU
for dir in vendor/github.com/google/certificate-transparency/go/x509 pkg/util/certificates; do
  if [ -d "${dir}" ]; then
    pushd ${dir}
    sed -i "/^[^=]*$/ s/oidNamedCurveP224/oidNamedCurveP256/g" *.go
    sed -i "/^[^=]*$/ s/elliptic\.P224/elliptic.P256/g" *.go
    popd
  fi
done

mkdir -p src/k8s.io/kubernetes
mv $(ls | grep -v "^src$") src/k8s.io/kubernetes/.

# mv command above skips all dot files. Move .generated_files and all
#.go* files
mv .generated_files src/k8s.io/kubernetes/.
mv .go* src/k8s.io/kubernetes/.

###############

%build

# As of K8S 1.26.3/1.25.8/1.24.12 upstream now builds with an explicit
# version of go and will try to fetch that version if not present.
# FORCE_HOTS_GO=y overrides that specification by using the host's
# version of go. This spec file continues to use build requires to
# require as a minimum the 'built with' go version from upstream.
#
# Packagers need to ensure that the go version on the build host contains
# any security patches and other critical fixes that are part of the
# "built with" version. Go maintainers typically release patch updates
# for both supported versions of Go that contain the same security
# updates.
export FORCE_HOST_GO=y

pushd src/k8s.io/kubernetes/
source hack/lib/init.sh
kube::golang::setup_env

export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_COMMIT=%{commit}
export KUBE_GIT_VERSION=v{version}
export KUBE_EXTRA_GOPATH=$(pwd)/Godeps/_workspace

# Build each binary separately to generate a unique build-id.
# Otherwise: Duplicate build-ids /builddir/build/BUILDROOT/.../usr/bin/kube-apiserver and /builddir/build/BUILDROOT/.../usr/bin/kubeadm
make WHAT="cmd/kube-proxy"
make WHAT="cmd/kube-apiserver"
make WHAT="cmd/kube-controller-manager"
make WHAT="cmd/kubelet"
make WHAT="cmd/kubeadm"
make WHAT="cmd/kube-scheduler"
make WHAT="cmd/kubectl"

# Gen docs
make WHAT="cmd/gendocs"
make WHAT="cmd/genkubedocs"
make WHAT="cmd/genman"
make WHAT="cmd/genyaml"
kube::util::gen-docs .

###############

%install
pushd src/k8s.io/kubernetes/
source hack/lib/init.sh
kube::golang::setup_env

%ifarch ppc64le
output_path="_output/local/go/bin"
%else
output_path="${KUBE_OUTPUT_BINPATH}/$(kube::golang::host_platform)"
%endif

echo "+++ INSTALLING binaries"
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-proxy
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-apiserver
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-controller-manager
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubelet
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubeadm
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-scheduler
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubectl

echo "+++ INSTALLING kubelet service config"
install -d -m 0755 %{buildroot}/%{_sysconfdir}/systemd/system/kubelet.service.d
install -p -m 0644 -t %{buildroot}/%{_sysconfdir}/systemd/system/kubelet.service.d %{SOURCE114}

echo "+++ INSTALLING shell completion"
install -dm 0755 %{buildroot}/%{bash_completions_dir}
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}/%{bash_completions_dir}/kubectl
install -dm 0755 %{buildroot}/%{fish_completions_dir}
%{buildroot}%{_bindir}/kubectl completion fish > %{buildroot}/%{fish_completions_dir}/kubectl.fish
install -dm 0755 %{buildroot}/%{zsh_completions_dir}
%{buildroot}%{_bindir}/kubectl completion zsh > %{buildroot}/%{zsh_completions_dir}/_kubectl

echo "+++ INSTALLING config files"
%define remove_environ_prefix() %(echo -n %1|sed 's/.*environ-//g')
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/manifests
install -m 644 -T %{SOURCE106} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE106}}
install -m 644 -T %{SOURCE107} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE107}}
install -m 644 -T %{SOURCE108} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE108}}
install -m 644 -T %{SOURCE109} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE109}}
install -m 644 -T %{SOURCE110} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE110}}
install -m 644 -T %{SOURCE111} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE111}}
install -m 644 -T %{SOURCE112} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE112}}

# place systemd/tmpfiles.d/kubernetes.conf to /usr/lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -p -m 0644 -t %{buildroot}/%{_tmpfilesdir} %{SOURCE115}

echo "+++ INSTALLING sysusers.d"
install -D -m 0644 -vp %{SOURCE116}       %{buildroot}%{_sysusersdir}/%{name}.conf

# enable CPU and Memory accounting
install -d -m 0755 %{buildroot}/%{_sysconfdir}/systemd/system.conf.d
install -p -m 0644 -t %{buildroot}/%{_sysconfdir}/systemd/system.conf.d %{SOURCE113}

echo "+++ INSTALLING service files"
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE101}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE102}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE103}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE104}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE105}

echo "+++ INSTALLING manpages"
install -d %{buildroot}%{_mandir}/man1
# from k8s tarball copied docs/man/man1/*.1
install -p -m 644 docs/man/man1/*.1 %{buildroot}%{_mandir}/man1

# install the place the kubelet defaults to put volumes and default folder structure
install -d %{buildroot}%{_sharedstatedir}/kubelet

mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/
popd

mv src/k8s.io/kubernetes/CHANGELOG/CHANGELOG-*.md .
mv src/k8s.io/kubernetes/*.md .
mv src/k8s.io/kubernetes/LICENSE .
# CHANGELOG.md is symlink to CHANGELOG/README.md and not actual
# change log. no need to include generated rpms
rm CHANGELOG.md

%check
if [ 1 != 1 ]; then
echo "******Testing the commands*****"
hack/test-cmd.sh
echo "******Benchmarking kube********"
hack/benchmark-go.sh

# In Fedora 20 and RHEL7 the go cover tools isn't available correctly
echo "******Testing the go code******"
hack/test-go.sh
echo "******Testing integration******"
hack/test-integration.sh --use_go_build
fi

##############################################
%files
%license LICENSE
%doc *.md

# kubelet
%{_mandir}/man1/kubelet.1*
%{_bindir}/kubelet
%{_unitdir}/kubelet.service
%{_sysusersdir}/%{name}.conf
%dir %{_sharedstatedir}/kubelet
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/manifests
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/kubelet
# % config(noreplace) % {_sysconfdir}/% {name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/kubelet.kubeconfig
%config(noreplace) %{_sysconfdir}/systemd/system.conf.d/kubernetes-accounting.conf
%{_tmpfilesdir}/kubernetes.conf
%verify(not size mtime md5) %attr(755, kube,kube) %dir /run/%{name}

# kubeadm
%{_mandir}/man1/kubeadm.1*
%{_mandir}/man1/kubeadm-*
%{_bindir}/kubeadm
%dir %{_sysconfdir}/systemd/system/kubelet.service.d
%config(noreplace) %{_sysconfdir}/systemd/system/kubelet.service.d/kubeadm.conf

##############################################
%files client
%license LICENSE
%doc *.md
%{_mandir}/man1/kubectl.1*
%{_mandir}/man1/kubectl-*
%{_bindir}/kubectl
%{bash_completions_dir}/kubectl
%{fish_completions_dir}/kubectl.fish
%{zsh_completions_dir}/_kubectl

##############################################

%files legacy-systemd
%license LICENSE
%doc *.md
%{_mandir}/man1/kube-apiserver.1*
%{_mandir}/man1/kube-controller-manager.1*
%{_mandir}/man1/kube-scheduler.1*
%{_mandir}/man1/kube-proxy.1*
%attr(754, -, kube) %caps(cap_net_bind_service=ep) %{_bindir}/kube-apiserver
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler
%{_bindir}/kube-proxy
%{_unitdir}/kube-proxy.service
%{_unitdir}/kube-apiserver.service
%{_unitdir}/kube-controller-manager.service
%{_unitdir}/kube-scheduler.service
%{_sysusersdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/apiserver
%config(noreplace) %{_sysconfdir}/%{name}/scheduler
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/controller-manager
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%{_tmpfilesdir}/kubernetes.conf
%verify(not size mtime md5) %attr(755, kube,kube) %dir /run/%{name}

##############################################

%pre legacy-systemd
%sysusers_create_compat %{SOURCE116}

%post legacy-systemd
%systemd_post kube-apiserver kube-scheduler kube-controller-manager kube-proxy

%preun legacy-systemd
%systemd_preun kube-apiserver kube-scheduler kube-controller-manager kube-proxy

%postun legacy-systemd
%systemd_postun kube-apiserver kube-scheduler kube-controller-manager kube-proxy


%pre
%sysusers_create_compat %{SOURCE116}

%post
%systemd_post kubelet
# If accounting is not currently enabled systemd reexec
if [[ `systemctl show kubelet | grep -q -e CPUAccounting=no -e MemoryAccounting=no; echo $?` -eq 0 ]]; then
  systemctl daemon-reexec
fi

%preun
%systemd_preun kubelet

%postun
%systemd_postun kubelet

############################################
%changelog
%autochangelog
