%if "%{_vendor}" == "debbuild"
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -tags=" ${BUILDTAGS:-}" -a -v -x %{?**};
%endif

%if 0%{?fedora}
%global with_debug 1
%else
%global with_debug 0
%endif

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project containernetworking
%global repo plugins
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag_strip 1.1.1

Name: %{project}-%{repo}
Version: 1.1.1
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0+
Release: 0%{?dist}
%else
Release: %autorelease
License: ASL 2.0 and BSD and MIT
%endif
Summary: Libraries for writing CNI plugin
URL: %{git0}
Source0: %{git0}/archive/v%{built_tag_strip}.tar.gz
BuildRequires: golang >= 1.16.6
%if "%{_vendor}" == "debbuild"
BuildRequires: libsystemd-dev
%else
BuildRequires: systemd-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: go-rpm-macros
%endif
%endif
BuildRequires: go-md2man
Requires: systemd

Obsoletes: %{project}-cni < 0.7.1-2
Provides: %{project}-cni = %{version}-%{release}
Provides: kubernetes-cni
Provides: container-network-stack = 1
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.4.17
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.8.20
Provides: bundled(golang(github.com/alexflint/go_filemutex)) = v1.1.0
Provides: bundled(golang(github.com/buger/jsonparser)) = v1.1.1
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.1
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.0.1
Provides: bundled(golang(github.com/coreos/go_iptables)) = v0.6.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/d2g/dhcp4)) = v0.0.0_20170904100407_a1d1b6c41b1c
Provides: bundled(golang(github.com/d2g/dhcp4client)) = v1.0.0
Provides: bundled(golang(github.com/d2g/dhcp4server)) = v0.0.0_20181031114812_7d4a0a7f59a5
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.4.9
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.0.4
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20200121045136_8c9f03a8e57e
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/networkplumbing/go_nft)) = v0.2.0
Provides: bundled(golang(github.com/nxadm/tail)) = v1.4.8
Provides: bundled(golang(github.com/onsi/ginkgo)) = v1.16.4
Provides: bundled(golang(github.com/onsi/gomega)) = v1.15.0
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/safchain/ethtool)) = v0.0.0_20210803160452_9aa261dae9b1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.1.1_0.20210330154013_f5de75959ad5
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20210104183010_2eb08e3e575f

%description
The CNI (Container Network Interface) project consists of a specification
and libraries for writing plugins to configure network interfaces in Linux
containers, along with a number of supported plugins. CNI concerns itself
only with network connectivity of containers and removing allocated resources
when the container is deleted.

%prep
%autosetup -p1 -n %{repo}-%{built_tag_strip}
rm -rf plugins/main/windows

# Use correct paths in cni-dhcp unitfiles
sed -i 's/\/opt\/cni\/bin/\%{_prefix}\/libexec\/cni/' plugins/ipam/dhcp/systemd/cni-dhcp.service

%build
export ORG_PATH="%{provider}.%{provider_tld}/%{project}"
export REPO_PATH="$ORG_PATH/%{repo}"

if [ ! -h gopath/src/${REPO_PATH} ]; then
        mkdir -p gopath/src/${ORG_PATH}
        ln -s ../../../.. gopath/src/${REPO_PATH} || exit 255
fi

export GOPATH=$(pwd)/gopath
mkdir -p $(pwd)/bin

echo "Building plugins"
export PLUGINS="plugins/meta/* plugins/main/* plugins/ipam/* plugins/sample"
for d in $PLUGINS; do
        if [ -d "$d" ]; then
                plugin="$(basename "$d")"
                echo "  $plugin"
                %gobuild -o "${PWD}/bin/$plugin" "$@" "$REPO_PATH"/$d
        fi
done

%install
install -d -p %{buildroot}%{_libexecdir}/cni/
install -p -m 0755 bin/* %{buildroot}/%{_libexecdir}/cni

install -dp %{buildroot}%{_unitdir}
install -p plugins/ipam/dhcp/systemd/cni-dhcp.service %{buildroot}%{_unitdir}
install -p plugins/ipam/dhcp/systemd/cni-dhcp.socket %{buildroot}%{_unitdir}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc *.md
%dir %{_libexecdir}/cni
%{_libexecdir}/cni/*
%{_unitdir}/cni-dhcp.service
%{_unitdir}/cni-dhcp.socket

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
