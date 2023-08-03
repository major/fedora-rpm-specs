%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global gomodulesmode GO111MODULE=on

Name: gvisor-tap-vsock
Epoch: 6
Version: 0.7.0
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
Release: %autorelease
ExclusiveArch: %{golang_arches_future}
Summary: Go replacement for libslirp and VPNKit
URL: https://github.com/containers/%{name}
# All SourceN files fetched from upstream
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: golang
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make
Obsoletes: podman-gvproxy < 5:4.7.0-1
Provides: podman-gvproxy = %{epoch}:%{version}-%{release}

%description
A replacement for libslirp and VPNKit, written in pure Go.
It is based on the network stack of gVisor. Compared to libslirp,
gvisor-tap-vsock brings a configurable DNS server and
dynamic port forwarding.

%prep
%autosetup -Sgit -n %{name}-%{version}

%build
%set_build_flags
export CGO_CFLAGS=$CFLAGS

# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif

# reset LDFLAGS for plugins and gvisor binaries
LDFLAGS=''

# build gvisor-tap-vsock binaries
%gobuild -o bin/gvproxy ./cmd/gvproxy
%gobuild -o bin/gvforwarder ./cmd/vm

%install
# install gvproxy
install -dp %{buildroot}%{_libexecdir}/podman
install -p -m0755 bin/gvproxy %{buildroot}%{_libexecdir}/podman
install -p -m0755 bin/gvforwarder %{buildroot}%{_libexecdir}/podman

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/gvproxy
%{_libexecdir}/podman/gvforwarder

%changelog
%autochangelog
