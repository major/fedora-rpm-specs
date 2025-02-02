Name: libzim
Version: 9.2.3
Release: %autorelease

License: GPL-2.0-only AND Apache-2.0 AND BSD-3-Clause
Summary: Reference implementation of the ZIM specification

URL: https://github.com/openzim/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/openzim/libzim/pull/936
Patch100: %{name}-9.2.3-icu76-build-fix.patch

BuildRequires: gtest-devel
BuildRequires: libicu-devel
BuildRequires: libzstd-devel
BuildRequires: xapian-core-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build

Provides: zimlib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: zimlib < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The ZIM library is the reference implementation for the ZIM file
format. It's a solution to read and write ZIM files on many systems
and architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/%{name}.so.9*

%files devel
%{_includedir}/zim
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
