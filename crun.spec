%global krun_opts %{nil}

%if 0%{?fedora} >= 37
%ifarch aarch64 || x86_64
%global krun_support enabled
%global krun_opts --with-libkrun
%endif
%endif

# wasmedge built only for aarch64 and x86_64
%ifarch aarch64 || x86_64
%global wasm_support enabled
%global wasm_opts --with-wasmedge
%endif

%global built_tag 1.8.3
%global gen_version %(b=%{built_tag}; echo ${b/-/"~"})

Summary: OCI runtime written in C
Name: crun
Version: %{gen_version}
URL: https://github.com/containers/%{name}
# Fetched from upstream
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
License: GPL-2.0-only
Release: %autorelease
ExclusiveArch: %{golang_arches_future}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: go-md2man
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libgcrypt-devel
%if "%{krun_support}" == "enabled"
BuildRequires: libkrun-devel
%endif
%if "%{wasm_support}" == "enabled"
BuildRequires: wasmedge-devel
%endif
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: protobuf-c-devel
%ifnarch %ix86
BuildRequires: criu-devel >= 3.17.1-2
%endif
Recommends: criu >= 3.17.1
Recommends: criu-libs
Provides: oci-runtime

%description
%{name} is a runtime for running OCI containers

%prep
%autosetup -Sgit %{name}-%{built_tag}

%build
./autogen.sh
%configure --disable-silent-rules %{krun_opts} %{wasm_opts}
%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib*
%if "%{krun_support}" == "enabled"
ln -s ../bin/%{name} %{buildroot}%{_bindir}/krun
%endif

%if "%{wasm_support}" == "enabled"
ln -s ../bin/%{name} %{buildroot}%{_bindir}/%{name}-wasm
%endif

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%if "%{krun_support}" == "enabled"
%package krun
Summary: OCI Runtime providing Virtualization-based process isolation capabilities.
Provides: krun
Requires: %{name} = %{version}-%{release}
Requires: libkrun

%description krun
%{name}-krun OCI Runtime providing Virtualization-based process isolation capabilities.

%files krun
%{_bindir}/krun
%endif

%if "%{wasm_support}" == "enabled"
%package wasm
Summary: wasm support for %{name}
Requires: wasm-library
Recommends: wasmedge
Requires: %{name} = %{version}-%{release}

%description wasm
%{name}-wasm provides %{name} built with wasm support

%files wasm
%{_bindir}/%{name}-wasm
%endif

%changelog
%autochangelog
