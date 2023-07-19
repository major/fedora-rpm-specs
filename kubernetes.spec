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
%global commit                  25b4e43193bcda6c7328a6d147b1fb73a33f1598
%global shortcommit              %(c=%{commit}; echo ${c:0:7})

# Needed otherwise "version_ldflags=$(kube::version_ldflags)" doesn't work
%global _buildshell  /bin/bash
%global _checkshell  /bin/bash

##############################################
Name:           kubernetes
Version:        1.27.3
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

# It obsoletes cadvisor but needs its source code (literally integrated)
Obsoletes:      cadvisor

# kubernetes is decomposed into master and node subpackages
# require both of them for updates
Requires: kubernetes-master = %{version}-%{release}
Requires: kubernetes-node = %{version}-%{release}

%description
%{summary}

##############################################
%package master
Summary: Kubernetes services for control plane host

BuildRequires: golang >= 1.20.5
BuildRequires: systemd
BuildRequires: rsync
BuildRequires: go-md2man
#BuildRequires: go-bindata

Requires(pre): shadow-utils
Requires: kubernetes-client = %{version}-%{release}

# if node is installed with node, version and release must be the same
Conflicts: kubernetes-node < %{version}-%{release}
Conflicts: kubernetes-node > %{version}-%{release}

%description master
Kubernetes services for control plane host

##############################################
%package node
Summary: Kubernetes services for worker node host

Requires: (containerd or cri-o)
Suggests: containerd
Requires: conntrack-tools

BuildRequires: golang >= 1.20.5
BuildRequires: systemd
BuildRequires: rsync
BuildRequires: go-md2man
#BuildRequires: go-bindata

Requires(pre): shadow-utils
Requires:      socat
Requires:      kubernetes-client = %{version}-%{release}

# if master is installed with node, version and release must be the same
Conflicts: kubernetes-master < %{version}-%{release}
Conflicts: kubernetes-master > %{version}-%{release}

%description node
Kubernetes services for worker node host

##############################################
%package  kubeadm
Summary:  Kubernetes tool for standing up clusters
Requires: kubernetes-node = %{version}-%{release}

Requires: containernetworking-plugins
Requires: cri-tools

%description kubeadm
Kubernetes tool for standing up clusters

##############################################
%package client
Summary: Kubernetes client tools

BuildRequires: golang >= 1.20.5
#BuildRequires: go-bindata
BuildRequires: make

%description client
Kubernetes client tools like kubectl

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

# With K*S 1.26.3/1.25.8/1.24.12 upstream now builds with an explicit
# version of go and will try to fetch that version if not present.
# FORCE_HOTS_GO=y overrides that specification by using the host's
# version of go. This spec file continues to use built requires to
# require as a minimum the 'built with' go version from upstream.
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
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}%{_datadir}/bash-completion/completions/kubectl
install -d -m 0755 %{buildroot}%{_datadir}/zsh-completion/completions/
%{buildroot}%{_bindir}/kubectl completion zsh > %{buildroot}%{_datadir}/zsh-completion/completions/kubectl
install -d -m 0755 %{buildroot}%{_datadir}/fish-completion/completions/
%{buildroot}%{_bindir}/kubectl completion fish > %{buildroot}%{_datadir}/fish-completion/completions/kubectl

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
install -D -m644 -vp %{SOURCE116}       %{buildroot}%{_sysusersdir}/%{name}.conf

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
# empty as it depends on master and node

##############################################
%files master
%license LICENSE
%doc *.md
%{_mandir}/man1/kube-apiserver.1*
%{_mandir}/man1/kube-controller-manager.1*
%{_mandir}/man1/kube-scheduler.1*
%attr(754, -, kube) %caps(cap_net_bind_service=ep) %{_bindir}/kube-apiserver
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler
%{_unitdir}/kube-apiserver.service
%{_unitdir}/kube-controller-manager.service
%{_unitdir}/kube-scheduler.service
%{_sysusersdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/apiserver
%config(noreplace) %{_sysconfdir}/%{name}/scheduler
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/controller-manager
%{_tmpfilesdir}/kubernetes.conf
%verify(not size mtime md5) %attr(755, kube,kube) %dir /run/%{name}

##############################################
%files node
%license LICENSE
%doc *.md
%{_mandir}/man1/kubelet.1*
%{_mandir}/man1/kube-proxy.1*
%{_bindir}/kubelet
%{_bindir}/kube-proxy
%{_unitdir}/kube-proxy.service
%{_unitdir}/kubelet.service
%{_sysusersdir}/%{name}.conf
%dir %{_sharedstatedir}/kubelet
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/manifests
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/kubelet.kubeconfig
%config(noreplace) %{_sysconfdir}/systemd/system.conf.d/kubernetes-accounting.conf
%{_tmpfilesdir}/kubernetes.conf
%verify(not size mtime md5) %attr(755, kube,kube) %dir /run/%{name}

##############################################
%files kubeadm
%license LICENSE
%doc *.md
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
%{_datadir}/bash-completion/completions/kubectl
%{_datadir}/zsh-completion/completions/kubectl
%{_datadir}/fish-completion/completions/kubectl

##############################################

%pre master
%sysusers_create_compat %{SOURCE116}

%post master
%systemd_post kube-apiserver kube-scheduler kube-controller-manager

%preun master
%systemd_preun kube-apiserver kube-scheduler kube-controller-manager

%postun master
%systemd_postun kube-apiserver kube-scheduler kube-controller-manager


%pre node
%sysusers_create_compat %{SOURCE116}

%post node
%systemd_post kubelet kube-proxy
# If accounting is not currently enabled systemd reexec
if [[ `systemctl show kubelet | grep -q -e CPUAccounting=no -e MemoryAccounting=no; echo $?` -eq 0 ]]; then
  systemctl daemon-reexec
fi

%preun node
%systemd_preun kubelet kube-proxy

%postun node
%systemd_postun kubelet kube-proxy

############################################
%changelog
%autochangelog
