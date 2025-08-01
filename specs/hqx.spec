%global summ() High quality upscaling %1 for pixel-art

Name: hqx
Summary: %{summ program}
License: LGPL-2.1-or-later

Version: 1.2
Release: 12%{?dist}

URL: https://github.com/grom358/hqx
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

# Adds a basic man page for the program.
# Submitted upstream: https://github.com/grom358/hqx/pull/4
Patch0: %{name}--add-man-page.patch

# Code specific to big-endian architectures has some undefined variables.
# Submitted upstream: https://github.com/grom358/hqx/pull/3
Patch1: %{name}--undefined-variables.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

BuildRequires: DevIL-devel

# Should be picked up automatically, but let's be explicit
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
Command-line program providing an implementation of hqx,
one of the pixel art scaling algorithms developed by Maxim Stepin.


%package -n lib%{name}
Summary: %{summ library}

%description -n lib%{name}
Library providing an implementation of hqx, one of the pixel art
scaling algorithms developed by Maxim Stepin.


%package -n lib%{name}-devel
Summary: Development files for lib%{name}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package provides development files required to build applications
using lib%{name}.


%prep
%autosetup -p1


%build
autoreconf -vi
%configure --disable-static

# The Makefile, as generated by configure, overrides CFLAGS
sed -e '/^CFLAGS = -O3$/d' -i Makefile
%make_build


%install
%make_install

# Don't want this
rm %{buildroot}%{_libdir}/lib%{name}.la


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n lib%{name}
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.1*

%files -n lib%{name}-devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2-6
- Migrate License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2-2
- Re-write patches (and submit upstream)
- Disable building static libs instead of deleting them after the build
- Rename hqx-libs subpckage to libhqx

* Sun Nov 21 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2-1
- Initial packaging
