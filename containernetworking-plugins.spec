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
%license LICENSE vendor/modules.txt
%doc *.md
%dir %{_libexecdir}/cni
%{_libexecdir}/cni/*
%{_unitdir}/cni-dhcp.service
%{_unitdir}/cni-dhcp.socket

%changelog
%autochangelog
