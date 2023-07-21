Name: belr
Version: 5.2.45
Release: 2%{?dist}
Summary: Language recognition library
License: GPL-3.0-or-later AND GPL-2.0-or-later

URL: https://gitlab.linphone.org/BC/public/belr/

Source: https://gitlab.linphone.org/BC/public/belr/-/archive/%{version}/%{name}-%{version}.tar.bz2

# Patches.
Patch00: 0001_belr_set_current_version.patch
Patch01: 0002_belr_actually_give_pkgconfig_file_an_install_location.patch

BuildRequires: cmake >= 3.2
BuildRequires: gcc-c++
BuildRequires: systemd-devel
BuildRequires: pkgconfig(bctoolbox)

%description
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

%package devel
Summary: Headers and libraries for the belr library
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-tools%{?_isa} = %{version}-%{release}

%description devel
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

This package contains header files and development libraries needed
to develop applications using the belr library.

%package tools
Summary: Tools and utilities for the belr library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description tools
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

This package contains tools and utilities needed to develop applications
using the belr library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_libdir}/libbelr.so.1*

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/belr/
%{_libdir}/libbelr.so
%{_libdir}/cmake/belr/
%{_datadir}/belr/
%{_datadir}/belr-tester/
%{_libdir}/pkgconfig/belr.pc

%files tools
%{_bindir}/belr-compiler
%{_bindir}/belr-parse
%{_bindir}/belr_tester

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 02 2023 Phil Wyett <philip.wyett@kathenas.org> - 5.2.45-1
- Initial package.
