Name:      libxcvt
Version:   0.1.2
Release:   5%{?dist}
Summary:   VESA CVT standard timing modelines generator

URL:       https://gitlab.freedesktop.org/xorg/lib/libxcvt/
Source0:   https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz

License:   MIT AND HPND-sell-variant

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package devel
Summary: Development package
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n cvt
Summary: Command line tool to calculate VESA CVT mode lines
Conflicts: xorg-x11-server-Xorg < 1.21

%description -n cvt
A standalone version of the command line tool cvt copied from the Xorg
implementation and is meant to be a direct replacement to the version
provided by the Xorg server.

%prep
%autosetup -S git_am -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING
%{_libdir}/libxcvt.so.*

%files devel
%{_libdir}/pkgconfig/libxcvt.pc
%dir %{_includedir}/libxcvt
%{_includedir}/libxcvt/*.h
%{_libdir}/libxcvt.so

%files -n cvt
%{_bindir}/cvt
%{_mandir}/man1/cvt.1*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Olivier Fourdan <ofourdan@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Olivier Fourdan <ofourdan@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Thu Jul 8 2021 Olivier Fourdan <ofourdan@redhat.com> - 0.1.0-1
- Initial import (#1980342)
