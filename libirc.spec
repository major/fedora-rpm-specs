Name:     libirc
Version:  0.2.1
Release:  %{autorelease}
Summary:  IRC client library for C
License:  GPL-3.0-only
URL:      https://github.com/n0la/libirc
Source0:  %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconf
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: libcmocka-devel
BuildRequires: gnutls-devel

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

