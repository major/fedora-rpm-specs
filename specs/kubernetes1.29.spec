# Do not edit this spec file. (Re-)Generate using newrelease

%global with_debug   0

%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global service_name            kubernetes
# https://github.com/kubernetes/kubernetes

# **** release metadata ****
# populated by envsubst in newrelease
%global k8s_name                kubernetes1.29
%global k8s_ver                 1.29.12
# major:minor version substring
%global k8s_minver              1.29
%global k8s_nextver             1.30
%global k8s_tag                 v1.29.12
# golang 'built with' version
%global golangver               1.22.9

# k8builddir is the default kubernetes build dir - current _output
# setting this macro should simplify the build/install process
%global k8builddir             _output

# last release version of kubernetes rpms prior to adoption of
# revised package organization (kubernetes-systemd rpm created and
# kubernetes-node rpm essentially renamed to kubernetes.
# Used to help set up Obsoletes correctly. Can be removed sometime
# after Kubernetes 1.29 is retired.
%global switchver              1.29.0

# Needed otherwise "version_ldflags=$(kube::version_ldflags)" doesn't work
%global _buildshell  /bin/bash
%global _checkshell  /bin/bash

# https://github.com/kubernetes/kubernetes
%global goipath         k8s.io/kubernetes
%global forgeurl        https://github.com/kubernetes/kubernetes
Version:                %{k8s_ver}
%global tag             %{k8s_tag}

%gometa -f

%global common_description %{expand:
Production-Grade Container Scheduling and Management.}

Name:           %{k8s_name}
# add base so that release is always higher than unversioned release
Release:        %autorelease -b 2
Summary:        Open Source Production-Grade Container Scheduling And Management Platform
License:        Apache-2.0
# Kubernetes built with components that are covered by one or more
# of the following licenses:
#              Apache-2.0, BSD-2-Clause, BSD-3-Clause,
#              BSD-3-Clause-HP, BSD-4-Clause, CC-BY-SA-4.0,
#              ISC, MIT

URL:            %{gourl}
Source0:        %{gosource}

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
Source114:      10-kubeadm.conf
# Source115:      kubernetes.conf
# Source116:      % {service_name}.sysusers
Source117:      kubelet.env

##############################################
# main package components - installs kubelet and necessary
# configuration files. Recommends kubernetes-client and
# kubernetes-kubeadm.
#
# Build requires for all packages
BuildRequires:  golang-github-cpuguy83-md2man
BuildRequires:  golang >= %{golangver}
BuildRequires:  go-rpm-macros
# BuildRequires:  go-vendor-tools
BuildRequires:  make
BuildRequires:  go-md2man
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  rsync

# additonal kubelet requirements
Requires:       conntrack-tools
Requires:       iptables >= 1.4.21
Requires:       iproute
Requires:       iproute-tc
Requires:       util-linux
Requires:       ethtool
Requires:       conntrack

# used to be Requires containerd or cri-0; other choices now available
Recommends:     (containerd or cri-o)
Conflicts:      cri-o < %{k8s_minver}
Conflicts:      cri-o >= %{k8s_nextver}
Recommends:     %{name}-client = %{version}-%{release}
Recommends:     %{name}-kubeadm = %{version}-%{release}

# require same version for kubernetes-kubeadm if installed
Conflicts:      %{name}-kubeadm < %{version}-%{release}
Conflicts:      %{name}-kubeadm > %{version}-%{release}

# require same version for kubernetes-client if installed
Conflicts:      %{name}-client < %{version}-%{release}
Conflicts:      %{name}-client > %{version}-%{release}

# provides and obsoletes kubernetes-node and kubernetes-kubeadm
Provides:       kubernetes-node = %{version}-%{release}
Obsoletes:      kubernetes-node < %{switchver}

# catch conflict with any other versioned kubernetes
Provides:       kubernetes
Conflicts:      kubernetes

%description
%{common_description}
Installs kubelet, the kubernetes agent on each machine in a
cluster. The kubernetes-client sub-package,
containing kubectl, is recommended but not strictly required.
The kubernetes-client sub-package should be installed on
control plane machines.

##############################################
%package  kubeadm
Summary:  Kubernetes tool for standing up clusters
Requires:       %{name} = %{version}-%{release}

Requires:       containernetworking-plugins
Recommends:     cri-tools
Conflicts:      cri-tools < %{k8s_minver}
Conflicts:      cri-tools >= %{k8s_nextver}

# require same version for kubernetes
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name} > %{version}-%{release}

# catch conflict with any other versioned kubernetes-kubeadm
Provides:       kubernetes-kubeadm
Conflicts:      kubernetes-kubeadm

%description kubeadm
%{common_description}
Installs kubeadm, a Kubernetes tool for standing up clusters. Not mandatory.
If used, install on each machine in the cluster. Used to initialize
each node, and to join new machines to an existing cluster.

##############################################
%package client
Summary: Kubernetes client tools

# require same version for kubernetes
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name} > %{version}-%{release}

# catch conflict with any other versioned kubernetes-client
Provides:       kubernetes-client
Conflicts:      kubernetes-client

%description client
%{common_description}
Installs kubectl, the Kubernetes command line client used to
interact with a Kubernetes cluster.

##############################################
%package systemd
Summary: Systemd services for control plane and/or node

# require same version for kubernetes
Requires: %{name} = %{version}-%{release}

# obsoletes kubernetes-master in part
Provides:       kubernetes-master = %{version}-%{release}
Provides:       kubernetes-legacy-systemd = %{version}-%{release}
Obsoletes:      kubernetes-master < %{switchver}

# catch conflict with any other versioned kubernetes-systemd
Provides:       kubernetes-systemd
Conflicts:      kubernetes-systemd

%description systemd
%{common_description}
Systemd services needed for manual installation of Kubernetes
on control plane or node machines. If kubeadm is used to bootstrap
a Kubernetes cluster then this rpm is not needed as kubeadm will install
these services as static pods in the cluster on nodes as needed.
If these systemd services are used, enable all services except
kube-proxy on each control plane. Enable kube-proxy on all machines
nodes that runs kubelet, including control plane machines with
kubelet.

##############################################
##############################################
%prep
%goprep -k
%setup -q -T -D %{forgesetupargs}

# mkdir -p src/k8s.io/kubernetes
# mv $(ls | grep -v "^src$") src/k8s.io/kubernetes/.

# mv command above skips all dot files. Move .generated_files and all
#.go* files
# mv .generated_files src/k8s.io/kubernetes/.
# mv .go* src/k8s.io/kubernetes/.

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

# see kube::golang::setup_env in ./hack/lib/golang.sh
# set these values to create common environment for
# gobuild macro and generate_docs in ./hack/update_generate_docs.sh
# export KUBE_GOPATH=% {gobuilddir}
# export KUBE_OUTPUT_SUBPATH=_build
# export GOCACHE=% {gobuilddir}/cache/build
# export GOMODCACHE=% {gobuilddir}/cache/mod

source hack/lib/init.sh
kube::golang::setup_env

export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_VERSION=v%{version}
export KUBE_EXTRA_GOPATH=$(pwd)/Godeps/_workspace

# go internal linker does not provide build ids; use
# KUBE_CGO_OVERRIDES to force external linker; consistent
# with Fedora go standards
export KUBE_CGO_OVERRIDES="kube-proxy kubeadm kube-apiserver kube-controller-manager kubelet kube-scheduler kubectl"

# Use settings from gobuild macro to populate GOFLAGS and
# GOLDFLAGS - see Makefile (%make_build help) for more information
export GOFLAGS="-buildmode=pie -compiler=gc -tags=rpm_crashtraceback${BUILDTAGS:+,}${BUILDTAGS:-}"

export GOLDFLAGS="%{?currentgoldflags} -B 0x$(echo '%{name}-%{version}-%{release}-${SOURCE_DATE_EPOCH:-}' | sha1sum | cut -d ' ' -f1) -compressdwarf=false -linkmode=external -extldflags '%{build_ldflags} %{?__golang_extldflags}'"

# Build each binary separately to generate a unique build-id.
# Otherwise: Duplicate build-ids /builddir/build/BUILDROOT/
# .../usr/bin/kube-apiserver and /builddir/build/BUILDROOT/.../usr/bin/kubeadm
%make_build WHAT="cmd/kube-proxy"
%make_build WHAT="cmd/kube-apiserver"
%make_build WHAT="cmd/kube-controller-manager"
%make_build WHAT="cmd/kubelet"
%make_build WHAT="cmd/kubeadm"
%make_build WHAT="cmd/kube-scheduler"
%make_build WHAT="cmd/kubectl"

# As of kubernetes 1.30 alpha.0 doc generation
# now handled by generate_docs function in
# update-generated-docs.sh. Including building doc
# generation binaries
# Gen docs
%make_build WHAT="cmd/gendocs"
%make_build WHAT="cmd/genkubedocs"
%make_build WHAT="cmd/genman"
%make_build WHAT="cmd/genyaml"
kube::util::gen-docs .
# source hack/update-generated-docs.sh

###############

%install

install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kube-proxy
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kube-apiserver
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kube-controller-manager
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kubelet
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kubeadm
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kube-scheduler
install -p -m 755 -t %{buildroot}%{_bindir} %{k8builddir}/bin/kubectl

echo "+++ INSTALLING kubelet service config"
install -d -m 0755 %{buildroot}/%{_unitdir}/kubelet.service.d
install -p -m 0644 -t %{buildroot}/%{_unitdir}/kubelet.service.d %{SOURCE114}

echo "+++ INSTALLING shell completion"
install -dm 0755 %{buildroot}/%{bash_completions_dir}
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}/%{bash_completions_dir}/kubectl
install -dm 0755 %{buildroot}/%{fish_completions_dir}
%{buildroot}%{_bindir}/kubectl completion fish > %{buildroot}/%{fish_completions_dir}/kubectl.fish
install -dm 0755 %{buildroot}/%{zsh_completions_dir}
%{buildroot}%{_bindir}/kubectl completion zsh > %{buildroot}/%{zsh_completions_dir}/_kubectl

echo "+++ INSTALLING config files"
%define remove_environ_prefix() %(echo -n %1|sed 's/.*environ-//g')
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{service_name}
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{service_name}/manifests
install -m 644 -T %{SOURCE106} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE106}}
install -m 644 -T %{SOURCE107} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE107}}
install -m 644 -T %{SOURCE108} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE108}}
install -m 644 -T %{SOURCE109} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE109}}
install -m 644 -T %{SOURCE110} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE110}}
install -m 644 -T %{SOURCE111} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE111}}
install -m 644 -T %{SOURCE112} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE112}}

# place systemd/tmpfiles.d/kubernetes.conf to /usr/lib/tmpfiles.d/kubernetes.conf
# install -d -m 0755 % {buildroot}% {_tmpfilesdir}
# install -p -m 0644 -t % {buildroot}/% {_tmpfilesdir} % {SOURCE115}

# echo "+++ INSTALLING sysusers.d"
# install -D -m 0644 -vp % {SOURCE116}       % {buildroot}% {_sysusersdir}/% {service_name}.conf

# enable CPU and Memory accounting
# see https://github.com/ingvagabund/articles/blob/master/cpu-and-memory-accounting-for-systemd.md for more information
install -d -m 0755 %{buildroot}%{_sysconfdir}/systemd/system.conf.d
install -p -m 0644 -t %{buildroot}%{_sysconfdir}/systemd/system.conf.d %{SOURCE113}

# kubelet extra args can be set in this file
# originally set in kubeadm defined service file for kubelet
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 0644 -T %{SOURCE117} %{buildroot}%{_sysconfdir}/sysconfig/kubelet

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

# mkdir -p % {buildroot}/run
# install -d -m 0755 % {buildroot}/run/% {service_name}/

mv CHANGELOG/CHANGELOG-*.md .
# mv src/k8s.io/kubernetes/*.md .
# mv src/k8s.io/kubernetes/LICENSE .
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
# %%license LICENSE vendor/modules.txt
%doc *.md

# kubelet
%{_mandir}/man1/kubelet.1*
%{_bindir}/kubelet
%{_unitdir}/kubelet.service
# % {_sysusersdir}/% {service_name}.conf
%dir %{_sharedstatedir}/kubelet
%dir %{_sysconfdir}/%{service_name}
%dir %{_sysconfdir}/%{service_name}/manifests
%config(noreplace) %{_sysconfdir}/%{service_name}/config
%config(noreplace) %{_sysconfdir}/%{service_name}/kubelet
%config(noreplace) %{_sysconfdir}/%{service_name}/kubelet.kubeconfig
%config(noreplace) %{_sysconfdir}/systemd/system.conf.d/kubernetes-accounting.conf
%config(noreplace) %{_sysconfdir}/sysconfig/kubelet
# % {_tmpfilesdir}/kubernetes.conf

##############################################
%files kubeadm
%license LICENSE
# %%license LICENSE vendor/modules.txt
%doc *.md
%{_mandir}/man1/kubeadm.1*
%{_mandir}/man1/kubeadm-*
%{_bindir}/kubeadm
%dir %{_unitdir}/kubelet.service.d
%{_unitdir}/kubelet.service.d/10-kubeadm.conf

##############################################
%files client
%license LICENSE
# %%license LICENSE vendor/modules.txt
%doc *.md
%{_mandir}/man1/kubectl.1*
%{_mandir}/man1/kubectl-*
%{_bindir}/kubectl
%{bash_completions_dir}/kubectl
%{fish_completions_dir}/kubectl.fish
%{zsh_completions_dir}/_kubectl

##############################################
%files systemd
%license LICENSE
# %%license LICENSE vendor/modules.txt
%doc *.md
%{_mandir}/man1/kube-apiserver.1*
%{_mandir}/man1/kube-controller-manager.1*
%{_mandir}/man1/kube-scheduler.1*
%{_mandir}/man1/kube-proxy.1*
%{_bindir}/kube-apiserver
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler
%{_bindir}/kube-proxy
%{_unitdir}/kube-proxy.service
%{_unitdir}/kube-apiserver.service
%{_unitdir}/kube-controller-manager.service
%{_unitdir}/kube-scheduler.service
# % {_sysusersdir}/% {service_name}.conf
%dir %{_sysconfdir}/%{service_name}
%config(noreplace) %{_sysconfdir}/%{service_name}/apiserver
%config(noreplace) %{_sysconfdir}/%{service_name}/scheduler
%config(noreplace) %{_sysconfdir}/%{service_name}/config
%config(noreplace) %{_sysconfdir}/%{service_name}/controller-manager
%config(noreplace) %{_sysconfdir}/%{service_name}/proxy
# % {_tmpfilesdir}/kubernetes.conf

##############################################

%post systemd
%systemd_post kube-apiserver kube-scheduler kube-controller-manager kube-proxy

%preun systemd
%systemd_preun kube-apiserver kube-scheduler kube-controller-manager kube-proxy

%postun systemd
%systemd_postun kube-apiserver kube-scheduler kube-controller-manager kube-proxy

# % pre
# % sysusers_create_compat % {SOURCE116}

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
