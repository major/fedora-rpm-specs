Name:     libirc
Version:  0.2.1
Release:  %{autorelease}
Summary:  IRC client library for C
License:  GPL-3.0-only
URL:      https://github.com/n0la/libirc
Source0:  %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/n0la/libirc/commit/602c11bcd652d723eb511effbdf256bcf6202182
Patch:    compatible-with-cmake-3.5.patch
# https://github.com/n0la/libirc/commit/900b1e238b34604ff3a623a65b500e36aced3cd9
Patch:    compatible-with-cmake-4.0.patch
# https://github.com/n0la/libirc/commit/09777ef345ed6338e8585ebcd294fdcea69fd97f
Patch:    tests-include-stdint.h.patch

BuildRequires: cmake
BuildRequires: pkgconf
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: libcmocka-devel
BuildRequires: gnutls-devel

ExcludeArch:   i686

%description
%{summary}.

%package devel
Summary:   Development headers for the libirc library
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers for the libric library.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%doc README.md
%{_libdir}/libirc.so.0
%{_libdir}/libirc.so.%{version}

%files devel
%{_includedir}/irc
%{_datadir}/pkgconfig/libirc.pc
%{_libdir}/libirc.so

%changelog
%autochangelog

