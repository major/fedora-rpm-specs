#debuginfo not supported with Go
%global debug_package %{nil}
# modifying the Go binaries breaks the DWARF debugging
%global __os_install_post %{_rpmconfigdir}/brp-compress

%global gopath      %{_datadir}/gocode
%global import_path github.com/openshift/origin
%global registry_import_path github.com/openshift/image-registry
%global webconsole_import_path github.com/openshift/origin-web-console-server
%global servicecat_import_path github.com/openshift/service-catalog
%global clustercap_import_path github.com/openshift/cluster-capacity

# docker_version is the version of docker requires by packages
%global docker_version 1.13
# openvswitch_version is the version of openvswitch requires by packages
%global openvswitch_version 2.6.1
# this is the version we obsolete up to. The packaging changed for Origin
# 1.0.6 and OSE 3.1 such that 'openshift' package names were no longer used.
%global package_refactor_version 3.0.2.900
%global golang_version 1.10
# %%commit and %%os_git_vars are intended to be set by tito custom builders provided
# in the .tito/lib directory. The values in this spec file will not be kept up to date.
%{!?commit:
%global commit 20c5b86c88657888e4906ed7942b85515c650f96
}
%global kube_commit b3b92b285f38984ad0b5b4d4ba6b150ac119dd2a
%global etcd_commit 135cf9b40738d17886f499b40bc176fc892ba5e9
%global registry_commit bffddbaeee29b7d32fe4cccc62f0049644c21705
%global webconsole_commit ea422803d27e20a8a78eeaa2d9c5619ac979f834
%global servicecat_commit 2e6be86d6e11c14aaca5c62e291879c9c694f425
%global clustercap_commit 22be164a90dc8d2705ce05638e6ce61839596dfc

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global kube_shortcommit %(c=%{kube_commit}; echo ${c:0:7})
%global etcd_shortcommit %(c=%{etcd_commit}; echo ${c:0:7})
%global registry_shortcommit %(c=%{registry_commit}; echo ${c:0:7})
%global webconsole_shortcommit %(c=%{webconsole_commit}; echo ${c:0:7})
%global servicecat_shortcommit %(c=%{servicecat_commit}; echo ${c:0:7})
%global clustercap_shortcommit %(c=%{clustercap_commit}; echo ${c:0:7})

# os_git_vars needed to run hack scripts during rpm builds
# place to look for the kube, catalog and etcd commit hashes are the lock files in the origin tree, seems that origin build scripts are ignorant about what origin is bundling...
%{!?os_git_vars:
%global os_git_vars OS_GIT_COMMIT=%{shortcommit} OS_GIT_VERSION=v3.11.0+%{shortcommit} OS_GIT_MAJOR=3 OS_GIT_MINOR=11+ OS_GIT_PATCH=0 OS_GIT_TREE_STATE=clean KUBE_GIT_VERSION=v1.10.0+%{kube_shortcommit} KUBE_GIT_MAJOR=1 KUBE_GIT_MINOR=10+ KUBE_GIT_COMMIT=%{kube_shortcommit} ETCD_GIT_COMMIT=%{etcd_shortcommit} ETCD_GIT_VERSION=v3.2.16-0-%{etcd_shortcommit} OS_GIT_CATALOG_VERSION=v0.1.9}

%if 0%{?fedora} || 0%{?epel}
%global need_redistributable_set 0
%else
# Due to library availability, redistributable builds only work on x86_64
%ifarch x86_64
%global need_redistributable_set 1
%else
%global need_redistributable_set 0
%endif
%endif
%{!?make_redistributable: %global make_redistributable %{need_redistributable_set}}

%if "%{dist}" == ".el7aos"
%global package_name atomic-openshift
%global product_name Atomic OpenShift
%else
%global package_name origin
%global product_name Origin
%endif

Name:           %{package_name}
# Version is not kept up to date and is intended to be set by tito custom
# builders provided in the .tito/lib directory of this project
Version:        3.11.2
Release:        8%{?dist}
Summary:        OpenShift Open Source Container Management by Red Hat
License:        ASL 2.0
URL:            https://%{import_path}

# If go_arches not defined fall through to implicit golang archs
%if 0%{?go_arches:1}
ExclusiveArch:  %{go_arches}
%else
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
%endif

ExcludeArch: ppc64

%global sversion %{version}

Source0:        https://%{import_path}/archive/%{commit}/%{name}-%{sversion}.tar.gz
# Docker registry has been move to separate repository at https://github.com/openshift/image-registry along with other "integral" parts of openshift origin
Source1:        https://%{registry_import_path}/archive/%{registry_commit}/registry-v%{sversion}.tar.gz
Source2:        https://%{webconsole_import_path}/archive/%{webconsole_commit}/webconsole-v%{sversion}.tar.gz
Source3:        https://%{servicecat_import_path}/archive/%{servicecat_commit}/servicecat-v%{sversion}.tar.gz
Source4:        https://%{clustercap_import_path}/archive/%{clustercap_commit}/clustercap-v%{sversion}.tar.gz

# Patch to enable armv7hl and i386
#
# armv7hl parts submitted upstream:
#   https://github.com/openshift/origin/pull/15686
#
# Upstream had this explcitly disabled for i386 but had client builds enabled.
# Will follow up with upstream to find out if they want to leave this as is.
Patch0:         origin-3.6.0-build.patch

BuildRequires: make
BuildRequires:  systemd
BuildRequires:  bsdtar
BuildRequires:  golang >= %{golang_version}
BuildRequires:  krb5-devel
BuildRequires:  rsync
Requires:       %{name}-clients = %{version}-%{release}
Requires:       iptables
Obsoletes:      openshift < %{package_refactor_version}

#
# The following Bundled Provides entries are populated automatically by the
# OpenShift Origin tito custom builder found here:
#   https://github.com/openshift/origin/blob/master/.tito/lib/origin/builder/
#
# Can also be generated with the following:
#   $ python -c 'import json; print "\n".join(["Provides: bundled(golang({})) = {}".format(dep[u"ImportPath"], dep[u"Rev"]) for dep in json.load(open("Godeps/Godeps.json", "r"))[u"Deps"]])'
#
# These are defined as per:
# https://fedoraproject.org/wiki/Packaging:Guidelines#Bundling_and_Duplication_of_system_libraries
# TODO add actual bundled list including recursive vendored deps, not just what origin BS can generate...
Provides: bundled(golang(github.com/coreos/etcd/etcdserver)) = 121edf0467052d55876a817b89875fb39a99bf78
Provides: bundled(golang(k8s.io/kubernetes/pkg/api)) = d4cacc043ac762235e16cb7361d527cb4189393c
Provides: bundled(golang(github.com/openshift/image-registry)) = 0d49798e519cb36d27c97392e92a9bf41ef90b66
Provides: bundled(golang(github.com/openshift/origin-web-console-server)) = 515b8e4fbaed78cb2dcad3f4d12b0e5493cb9bce
Provides: bundled(golang(github.com/openshift/service-catalog)) = c0f3fe8b3d0127d1be39a6dfa56baf96153ad762
Provides: bundled(golang(github.com/openshift/cluster-capacity)) = d8c344e0feb22cc9078081243b492b38a411e4cb

%description
OpenShift Origin is a distribution of Kubernetes optimized for enterprise application
development and deployment. OpenShift Origin adds developer and operational centric
tools on top of Kubernetes to enable rapid application development, easy
deployment and scaling, and long-term lifecycle maintenance for small and large
teams and applications. It provides a secure and multi-tenant configuration for
Kubernetes allowing you to safely host many different applications and workloads
on a unified cluster.

%package hypershift
Summary:        %{product_name} server commands

%description hypershift
%{summary}

%package hyperkube
Summary:        %{product_name} Kubernetes server commands
Conflicts:  kubernetes-node, kubernetes-master, kubernetes-client

%description hyperkube
%{summary}

%package master
Summary:        %{product_name} Master
Requires:       %{name} = %{version}-%{release}
Obsoletes:      openshift-master < %{package_refactor_version}

%description master
%{summary}

%package tests
Summary: %{product_name} Test Suite

%description tests
%{summary}

%package node
Summary:        %{product_name} Node
Requires:       %{name}-hyperkube = %{version}-%{release}
Requires:       util-linux
Requires:       socat
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Obsoletes:      openshift-node < %{package_refactor_version}
Obsoletes:      tuned-profiles-%{name}-node < 3.6.1
Provides:       tuned-profiles-%{name}-node = %{version}-%{release}

%description node
%{summary}

%package clients
Summary:        %{product_name} Client binaries for Linux
Obsoletes:      openshift-clients < %{package_refactor_version}
Conflicts:      kubernetes-client
Recommends:     bash-completion

%description clients
%{summary}

%if 0%{?make_redistributable}
%package clients-redistributable
Summary:        %{product_name} Client binaries for Linux, Mac OSX, and Windows
Obsoletes:      openshift-clients-redistributable < %{package_refactor_version}

%description clients-redistributable
%{summary}
%endif

%package dockerregistry
Summary:        Docker Registry v2 for %{product_name}
Requires:       %{name} = %{version}-%{release}

%description dockerregistry
%{summary}

%package pod
Summary:        %{product_name} Pod

%description pod
%{summary}

%package sdn-ovs
Summary:          %{product_name} SDN Plugin for Open vSwitch
Requires:         openvswitch >= %{openvswitch_version}
# selinux-policy is required because openvswitch doesn't yet take a dependency on selinux-policy but changes the files
Requires:         selinux-policy
Requires:         %{name}-node = %{version}-%{release}
Requires:         bridge-utils
Requires:         ethtool
Requires:         procps-ng
Requires:         iproute
Requires:         conntrack-tools
Obsoletes:        openshift-sdn-ovs < %{package_refactor_version}

%description sdn-ovs
%{summary}

%package service-catalog
Summary:        %{product_name} Service Catalog
Requires:       %{name} = %{version}-%{release}

%description service-catalog
%{summary}

%package template-service-broker
Summary: Template Service Broker
%description template-service-broker
%{summary}

%package cluster-capacity
Summary:        %{product_name} Cluster Capacity Analysis Tool
Requires:       %{name} = %{version}-%{release}

%description cluster-capacity
%{summary}

%package excluder
Summary:   Exclude openshift packages from updates
BuildArch: noarch

%description excluder
Many times admins do not want openshift updated when doing
normal system updates.

%{name}-excluder exclude - No openshift packages can be updated
%{name}-excluder unexclude - Openshift packages can be updated

%package docker-excluder
Summary:   Exclude docker packages from updates
BuildArch: noarch

%description docker-excluder
Certain versions of OpenShift will not work with newer versions
of docker.  Exclude those versions of docker.

%{name}-docker-excluder exclude - No major docker updates
%{name}-docker-excluder unexclude - docker packages can be updated

%package web-console
Summary: Web Console for the OpenShift Application Platform

%description web-console
OpenShift is a distribution of Kubernetes optimized for enterprise application
development and deployment. This is the web console server for OpenShift.


%prep
%setup -q -n %{name}-%{commit}
gzip -dc %{SOURCE1} | tar -xof -
gzip -dc %{SOURCE2} | tar -xof -
gzip -dc %{SOURCE3} | tar -xof -
gzip -dc %{SOURCE4} | tar -xof -

%patch0 -p1 -b .bsfix

%build
echo "GOLANG DEBUG OUTPUT"
go version
export TRAVIS=true
export GO111MODULE=off
export GOPROXY=direct
export GOSUMDB=off
%if 0%{make_redistributable}
# Create Binaries for all supported arches
%{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
%{os_git_vars} hack/build-go.sh vendor/github.com/onsi/ginkgo/ginkgo
pushd image-registry-%{registry_commit}
%{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
pushd origin-web-console-server-%{webconsole_commit}
%{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
pushd service-catalog-%{servicecat_commit}
%{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
pushd cluster-capacity-%{clustercap_commit}
%{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
%else
# Create Binaries only for building arch
%ifarch x86_64
  BUILD_PLATFORM="linux/amd64"
%endif
%ifarch %{ix86}
  BUILD_PLATFORM="linux/386"
%endif
%ifarch ppc64le
  BUILD_PLATFORM="linux/ppc64le"
%endif
%ifarch aarch64
  BUILD_PLATFORM="linux/arm64"
%endif
%ifarch %{arm}
  BUILD_PLATFORM="linux/arm"
%endif
%ifarch s390x
  BUILD_PLATFORM="linux/s390x"
%endif
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
pushd image-registry-%{registry_commit}
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
pushd origin-web-console-server-%{webconsole_commit}
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
pushd service-catalog-%{servicecat_commit}
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
pushd cluster-capacity-%{clustercap_commit}
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %{os_git_vars} OS_BUILD_RELEASE_ARCHIVES=n make build-cross
popd
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %{os_git_vars} hack/build-go.sh vendor/github.com/onsi/ginkgo/ginkgo
%endif

# Create extended.test
%{os_git_vars} hack/build-go.sh test/extended/extended.test

# Create/Update man pages
%{os_git_vars} hack/generate-docs.sh

%install

PLATFORM="$(go env GOHOSTOS)/$(go env GOHOSTARCH)"
install -d %{buildroot}%{_bindir}

# Install linux components
for bin in oc oadm openshift hypershift hyperkube template-service-broker openshift-node-config
do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 _output/local/bin/${PLATFORM}/${bin} %{buildroot}%{_bindir}/${bin}
done

echo "+++ INSTALLING dockerregistry"
install -p -m 755 image-registry-%{registry_commit}/_output/local/bin/${PLATFORM}/dockerregistry %{buildroot}%{_bindir}/dockerregistry

echo "+++ INSTALLING web-console"
install -p -m 755 origin-web-console-server-%{webconsole_commit}/_output/local/bin/${PLATFORM}/origin-web-console %{buildroot}%{_bindir}/origin-web-console

# Install tests
install -d %{buildroot}%{_libexecdir}/%{name}
install -p -m 755 _output/local/bin/${PLATFORM}/extended.test %{buildroot}%{_libexecdir}/%{name}/
install -p -m 755 _output/local/bin/${PLATFORM}/ginkgo %{buildroot}%{_libexecdir}/%{name}/

%if 0%{?make_redistributable}
# Install client executable for windows and mac
install -d %{buildroot}%{_datadir}/%{name}/{linux,macosx,windows}
install -p -m 755 _output/local/bin/linux/amd64/oc %{buildroot}%{_datadir}/%{name}/linux/oc
install -p -m 755 _output/local/bin/linux/amd64/kubectl %{buildroot}%{_datadir}/%{name}/linux/kubectl
install -p -m 755 _output/local/bin/darwin/amd64/oc %{buildroot}/%{_datadir}/%{name}/macosx/oc
install -p -m 755 _output/local/bin/darwin/amd64/kubectl %{buildroot}/%{_datadir}/%{name}/macosx/kubectl
install -p -m 755 _output/local/bin/windows/amd64/oc.exe %{buildroot}/%{_datadir}/%{name}/windows/oc.exe
install -p -m 755 _output/local/bin/windows/amd64/kubectl.exe %{buildroot}/%{_datadir}/%{name}/windows/kubectl.exe
# Install oadm client executable
install -p -m 755 _output/local/bin/linux/amd64/oadm %{buildroot}%{_datadir}/%{name}/linux/oadm
install -p -m 755 _output/local/bin/darwin/amd64/oadm %{buildroot}/%{_datadir}/%{name}/macosx/oadm
install -p -m 755 _output/local/bin/windows/amd64/oadm.exe %{buildroot}/%{_datadir}/%{name}/windows/oadm.exe
%endif
# Install cluster capacity
install -p -m 755 cluster-capacity-%{clustercap_commit}/_output/local/bin/${PLATFORM}/hypercc %{buildroot}%{_bindir}/
ln -s hypercc %{buildroot}%{_bindir}/cluster-capacity

# Install service-catalog
install -p -m 755 service-catalog-%{servicecat_commit}/_output/local/bin/${PLATFORM}/service-catalog %{buildroot}%{_bindir}/

# Install pod
install -p -m 755 _output/local/bin/${PLATFORM}/pod %{buildroot}%{_bindir}/

install -d -m 0755 %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig

for cmd in \
    openshift-deploy \
    openshift-docker-build \
    openshift-sti-build \
    openshift-git-clone \
    openshift-manage-dockerfile \
    openshift-extract-image-content \
    openshift-f5-router \
    openshift-recycle \
    openshift-router \
    kubectl
do
    ln -s oc %{buildroot}%{_bindir}/$cmd
done

install -d -m 0755 %{buildroot}%{_sysconfdir}/origin/{master,node}
install -d -m 0755 %{buildroot}%{_sysconfdir}/kubernetes/manifests

# stub filed required to ensure config is not reverted during upgrades
install -m 0644 contrib/systemd/origin-node.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}-node

# Install man1 man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 docs/man/man1/* %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_sharedstatedir}/origin

# Install sdn scripts
install -d -m 0755 %{buildroot}%{_sysconfdir}/cni/net.d
install -d -m 0755 %{buildroot}/opt/cni/bin
install -p -m 0755 _output/local/bin/${PLATFORM}/sdn-cni-plugin %{buildroot}/opt/cni/bin/openshift-sdn
install -p -m 0755 _output/local/bin/${PLATFORM}/host-local %{buildroot}/opt/cni/bin
install -p -m 0755 _output/local/bin/${PLATFORM}/loopback %{buildroot}/opt/cni/bin

install -d -m 0755 %{buildroot}%{_unitdir}/%{name}-node.service.d

# Install bash completions
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d/
for bin in oc openshift
do
  echo "+++ INSTALLING BASH COMPLETIONS FOR ${bin} "
  %{buildroot}%{_bindir}/${bin} completion bash > %{buildroot}%{_sysconfdir}/bash_completion.d/${bin}
  chmod 644 %{buildroot}%{_sysconfdir}/bash_completion.d/${bin}
done

# Install origin-accounting
install -d -m 755 %{buildroot}%{_sysconfdir}/systemd/system.conf.d/
install -p -m 644 contrib/systemd/origin-accounting.conf %{buildroot}%{_sysconfdir}/systemd/system.conf.d/

# Excluder variables
mkdir -p $RPM_BUILD_ROOT/usr/sbin
%if 0%{?fedora}
  OS_CONF_FILE="/etc/dnf.conf"
%else
  OS_CONF_FILE="/etc/yum.conf"
%endif

# Install openshift-excluder script
sed "s|@@CONF_FILE-VARIABLE@@|${OS_CONF_FILE}|" contrib/excluder/excluder-template > $RPM_BUILD_ROOT/usr/sbin/%{name}-excluder
sed -i "s|@@PACKAGE_LIST-VARIABLE@@|%{name} %{name}-clients %{name}-clients-redistributable %{name}-master %{name}-node %{name}-pod %{name}-recycle %{name}-hyperkube %{name}-tests|" $RPM_BUILD_ROOT/usr/sbin/%{name}-excluder
chmod 0744 $RPM_BUILD_ROOT/usr/sbin/%{name}-excluder

# Install docker-excluder script
sed "s|@@CONF_FILE-VARIABLE@@|${OS_CONF_FILE}|" contrib/excluder/excluder-template > $RPM_BUILD_ROOT/usr/sbin/%{name}-docker-excluder
sed -i "s|@@PACKAGE_LIST-VARIABLE@@|docker*1.14* docker*1.15* docker*1.16* docker*1.17* docker*1.18* docker*1.19* docker*1.20*|" $RPM_BUILD_ROOT/usr/sbin/%{name}-docker-excluder
chmod 0744 $RPM_BUILD_ROOT/usr/sbin/%{name}-docker-excluder

# Give the excluders a consistent timestamp between multi-arch builds
touch --reference=%{SOURCE0} $RPM_BUILD_ROOT/usr/sbin/%{name}-excluder
touch --reference=%{SOURCE0} $RPM_BUILD_ROOT/usr/sbin/%{name}-docker-excluder

%files
%doc README.md
%license LICENSE
%{_bindir}/openshift
%{_sharedstatedir}/origin
%{_sysconfdir}/bash_completion.d/openshift
%defattr(-,root,root,0700)
%dir %config(noreplace) %{_sysconfdir}/origin
%ghost %dir %config(noreplace) %{_sysconfdir}/origin
%ghost %config(noreplace) %{_sysconfdir}/origin/.config_managed
%{_mandir}/man1/openshift*

%files tests
%license LICENSE
%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/extended.test

%files hypershift
%{_bindir}/hypershift
%defattr(-,root,root,0700)

%files hyperkube
%{_bindir}/hyperkube
%defattr(-,root,root,0700)

%files master
%license LICENSE
%defattr(-,root,root,0700)
%config(noreplace) %{_sysconfdir}/origin/master

%files node
%license LICENSE
%{_bindir}/openshift-node-config
%{_sysconfdir}/systemd/system.conf.d/origin-accounting.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-node
%defattr(-,root,root,0700)
%config(noreplace) %{_sysconfdir}/origin/node
%dir %{_sysconfdir}/kubernetes/manifests

%preun node
%systemd_preun %{name}-node.service

%postun node
%systemd_postun %{name}-node.service

%files sdn-ovs
%license LICENSE
%dir %{_sysconfdir}/cni/net.d
%dir /opt/cni/bin
/opt/cni/bin/*

%files service-catalog
%license LICENSE
%{_bindir}/service-catalog

%files clients
%license LICENSE
%{_bindir}/oc
%{_bindir}/kubectl
%{_bindir}/oadm
%{_bindir}/openshift-deploy
%{_bindir}/openshift-docker-build
%{_bindir}/openshift-sti-build
%{_bindir}/openshift-git-clone
%{_bindir}/openshift-extract-image-content
%{_bindir}/openshift-manage-dockerfile
%{_bindir}/openshift-f5-router
%{_bindir}/openshift-recycle
%{_bindir}/openshift-router
%{_sysconfdir}/bash_completion.d/oc
%{_mandir}/man1/oc*

%if 0%{?make_redistributable}
%files clients-redistributable
%dir %{_datadir}/%{name}/linux/
%dir %{_datadir}/%{name}/macosx/
%dir %{_datadir}/%{name}/windows/
%{_datadir}/%{name}/linux/oc
%{_datadir}/%{name}/linux/kubectl
%{_datadir}/%{name}/macosx/oc
%{_datadir}/%{name}/macosx/kubectl
%{_datadir}/%{name}/windows/oc.exe
%{_datadir}/%{name}/windows/kubectl.exe
%{_datadir}/%{name}/linux/oadm
%{_datadir}/%{name}/macosx/oadm
%{_datadir}/%{name}/windows/oadm.exe
%endif

%files dockerregistry
%license LICENSE
%{_bindir}/dockerregistry

%files pod
%license LICENSE
%{_bindir}/pod

%files excluder
%license LICENSE
/usr/sbin/%{name}-excluder

%pretrans excluder
# we always want to clear this out using the last
#   versions script.  Otherwise excludes might get left in
if [ -s /usr/sbin/%{name}-excluder ] ; then
  /usr/sbin/%{name}-excluder unexclude
fi

%posttrans excluder
# we always want to run this after an install or update
/usr/sbin/%{name}-excluder exclude

%preun excluder
# If we are the last one, clean things up
if [ "$1" -eq 0 ] ; then
  /usr/sbin/%{name}-excluder unexclude
fi

%files docker-excluder
%license LICENSE
/usr/sbin/%{name}-docker-excluder

%files cluster-capacity
%license LICENSE
%{_bindir}/hypercc
%{_bindir}/cluster-capacity

%files template-service-broker
%{_bindir}/template-service-broker

%files web-console
%license LICENSE
%{_bindir}/origin-web-console


%pretrans docker-excluder
# we always want to clear this out using the last
#   versions script.  Otherwise excludes might get left in
if [ -s /usr/sbin/%{name}-docker-excluder ] ; then
  /usr/sbin/%{name}-docker-excluder unexclude
fi

%posttrans docker-excluder
# we always want to run this after an install or update
/usr/sbin/%{name}-docker-excluder exclude

%preun docker-excluder
# If we are the last one, clean things up
if [ "$1" -eq 0 ] ; then
  /usr/sbin/%{name}-docker-excluder unexclude
fi

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 3.11.2-7
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.11.2-6
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jakub Čajka <jcajka@fedoraproject.org> - 3.11.2-1
- Rebase to upstream 20c5b86c88657888e4906ed7942b85515c650f96, let's call it 3.11.2
- Fix for CVE-2020-8551, CVE-2020-8552, CVE-2020-8555, CVE-2020-8945
- Resolves: BZ#1816406, BZ#1816396, BZ#1842692, BZ#1802905

* Fri May 01 2020 Petr Pisar <ppisar@redhat.com> - 3.11.1-6
- Soften a dependency on bash-completion (bug #1493993)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 02 2019 Jakub Čajka <jcajka@fedoraproject.org> - 3.11.1-4
- Fix build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.11.1-1
- Rebase to upstream 8de5c3442e56dbe05403990ce0821746673fd588, let's call it 3.11.1
- Fix for CVE-2018-1002105
- Resolves: BZ#1656650

* Wed Nov 07 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.11.0-2
- fix OS_GIT_VERSION value
- Resolves: BZ#1646995

* Fri Oct 19 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.11.0-1
- Rebase to 3.11.0 proper
- Addopt upstream sub-package layout
- Add conflicts with kube

* Wed Sep 26 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.11.0-0.alpha1.0
- Rebase to 3.11.alpha1
- Resolves: BZ#1608505

* Wed Aug 29 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.10.0-2
- Add openshift-node-config binary in to the node sub-package
- Related: BZ#1598406

* Mon Aug 06 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.10.0-1
- Rebase to 3.10
- Resolves: BZ#1598406

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.9.0-3
- incorporate changes from the upstream spec file
- move to hyperkube
- add alternatives for hyperkube

* Wed May 30 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.9.0-2
- Add web-console sub-package

* Fri Mar 23 2018 Jakub Čajka <jcajka@fedoraproject.org> - 3.9.0-1
- Rebase to 3.9.0
- Obsolete tuned-profiles-origin-node

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.0-3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Adam Miller <maxamillion@fedoraproject.org> - 3.6.0-1
- Update to latest upstream
- Switch to new upstream versioning scheme (jump from 1.5 -> 3.6)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.5.1-3
- fix OS_CONF_FILE excluder path

* Wed Jul 05 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.5.1-2
- Exclude ppc64 since docker doesn't exist for that architecture

* Mon Jun 26 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.5.1-1
- Update to latest upstream - 1.5.1

* Tue Apr 25 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.5.0-1
- Update to latest upstream - 1.5.0

* Thu Feb 16 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.4.1-1
- Update to latest upstream - 1.4.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.4.0-1
- Update to latest upstream - 1.4.0

* Tue Oct 25 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.3.1-1
- Update to latest upstream - 1.3.1

* Fri Sep 16 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.3.0-1
- Update to latest upstream - 1.3.0
- Rebase spec file on upstream spec

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2.git.0.2e62fab
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Jun 17 2016 Adam Miller <maxamillion@fedoraproject.org- 1.2.0-1.git.0.2e62fab
- build on i686, %%{arm}, aarch64

* Thu Apr 21 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.6-2.git.0.ef1caba
- build on i686, %%{arm}, aarch64

* Tue Apr 19 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1.6-1.git.0.ef1caba
- Update to latest upstream release

* Wed Mar 23 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1.4-1.git.0.3941102
- Update to latest upstream release

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2.git.0.cffae05
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 17 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1.3-1.git.0.cffae05
- Update to latest upstream release

* Tue Feb 09 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1.1-1.git.0.86b5e46
- Update to latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.git.0.ac7a99a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.1-4.git.0.ac7a99a
- Add iproute and procpc-ng Requires for sdn-ovs
- set .config_managed to %%ghost and %%config(noreplace)
- Fix dir ownership for redistributable clients
- Remove no longer needed basename reference

* Wed Dec 09 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.1-3.git.0.ac7a99a
- Fix dir listing for kube_plugin_path

* Wed Dec 09 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.1-2.git.0.ac7a99a
- Fix dir listing for sdn

* Wed Dec 09 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.1-1.git.0.ac7a99a
- Remove no longer needed defattr
- Remove Obsoletes for package never in Fedora
- Remove upstream specific conditionals for el7aos dist tag

* Wed Dec 02 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.git.0.ac7a99a
- First submission to Fedora

