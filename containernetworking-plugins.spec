%global with_debug 1

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

%global built_tag v1.4.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: %{project}-%{repo}
Version: 1.4.0
Release: %autorelease
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and MPL-2.0
Summary: Libraries for writing CNI plugin
URL: %{git0}
# Tarball fetched from upstream
Source0: %{url}/archive/%{built_tag}.tar.gz
ExclusiveArch: %{golang_arches}
BuildRequires: golang >= 1.21.0
BuildRequires: systemd-devel
BuildRequires: go-rpm-macros
BuildRequires: go-md2man
Requires: systemd
Obsoletes: %{project}-cni < 0.7.1-2
Provides: %{project}-cni = %{version}-%{release}
Provides: kubernetes-cni
Provides: container-network-stack = 1
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/alexflint/go_filemutex)) = v1.2.0
Provides: bundled(golang(github.com/buger/jsonparser)) = v1.1.1
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.1.0
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.2
Provides: bundled(golang(github.com/coreos/go_iptables)) = v0.6.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.5.0
Provides: bundled(golang(github.com/d2g/dhcp4client)) = v1.0.0
Provides: bundled(golang(github.com/d2g/dhcp4server)) = v0.0.0_20181031114812_7d4a0a7f59a5
Provides: bundled(golang(github.com/d2g/dhcp4)) = v0.0.0_20170904100407_a1d1b6c41b1c
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/go_logr/logr)) = v1.2.4
Provides: bundled(golang(github.com/google/go_cmp)) = v0.5.9
Provides: bundled(golang(github.com/google/pprof)) = v0.0.0_20230323073829_e72429f035bd
Provides: bundled(golang(github.com/go_task/slim_sprig)) = v0.0.0_20230315185526_52ccab3ef572
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.0
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.9
Provides: bundled(golang(github.com/networkplumbing/go_nft)) = v0.3.0
Provides: bundled(golang(github.com/onsi/ginkgo/v2)) = v2.9.2
Provides: bundled(golang(github.com/onsi/gomega)) = v1.27.6
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.11.0
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/safchain/ethtool)) = v0.3.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.2.1_beta.2
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.4

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
%autochangelog

