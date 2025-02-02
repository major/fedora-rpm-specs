Name: libkiwix
Version: 14.0.0
Release: %autorelease

License: GPL-3.0-or-later
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Fixed build against libicu 76
# Similar to https://github.com/openzim/libzim/pull/936
Patch100: %{name}-14.0.0-icu76-build-fix.patch

BuildRequires: gtest-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libzim-devel
BuildRequires: mustache-devel
BuildRequires: ninja-build
BuildRequires: pugixml-devel
BuildRequires: zlib-devel

BuildRequires: aria2
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson

Provides: kiwix-lib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: kiwix-lib < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The Kiwix library provides the Kiwix software core. It contains
the code shared by all Kiwix ports.

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
%{_bindir}/kiwix-compile-*
%{_libdir}/%{name}.so.14*
%{_mandir}/man1/kiwix*.1*

%files devel
%{_includedir}/kiwix
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
