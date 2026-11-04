Name: lmdbxx
Version: 1.0.3
Release: %autorelease

License: LicenseRef-Fedora-Public-Domain
Summary: C++ wrapper for the LMDB embedded B+ tree database library
URL: https://github.com/hoytech/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# make pkgconfig install path noarch and fix meson warning
Patch0: %{name}-meson.patch
BuildArch: noarch

BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconfig(lmdb)

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Requires: lmdb-devel
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
%meson -Dtests=true

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files devel
%doc README.md FUNCTIONS.rst AUTHORS CREDITS VERSION
%license UNLICENSE
%{_includedir}/lmdb++.h
%{_datadir}/pkgconfig/lmdb++.pc

%changelog
%autochangelog
