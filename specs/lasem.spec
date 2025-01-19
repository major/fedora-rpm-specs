%global apiver 0.6

Name:           lasem
Version:        0.6.0
Release:        2%{?dist}
Summary:        A library for rendering SVG and Mathml, implementing a DOM like API

License:        LGPL-2.1-or-later
URL:            https://lasemproject.github.io/lasem/
Source0:        https://github.com/LasemProject/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# dropped as in 0.6.0 the different translatable strings have changed
# will attempt to contact the translator
#Patch0:      000-add-ka.patch

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  meson
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gi-docgen
Requires:       lyx-fonts
Provides:       bundled(itex2mml) = 1.6.1

%description
Lasem is a library for rendering SVG and Mathml, implementing a DOM like API.
It's based on GObject and use Pango and Cairo for the rendering.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        render
Summary:        Simple MathML converter
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    render
Simple application, which is able to convert a Mathml, a latex math or a SVG
file to either a PNG, PDF or SVG image.


%prep
%autosetup


%build
%meson -Ddocumentation=enabled

%meson_build


%install
%meson_install
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.la' -delete -print

#docs are installed using %%doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%find_lang %{name}-%{apiver}

%ldconfig_scriptlets


%check
# disabled until failure can be resolved upstream
#%%meson_test


%files -f %{name}-%{apiver}.lang
%doc NEWS.md README.md
%license COPYING itex2mml/COPYING.itex2MML
%{_libdir}/girepository-1.0/Lasem-%{apiver}.typelib
%{_libdir}/lib%{name}-%{apiver}.so.*

%files devel
%{_includedir}/%{name}-%{apiver}
%{_libdir}/lib%{name}-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_datadir}/gir-1.0/Lasem-%{apiver}.gir
%{_docdir}/%{name}-%{apiver}

%files render
%{_bindir}/%{name}-render-%{apiver}
%{_mandir}/man1/%{name}-render-%{apiver}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.6.0-1
- Update to v0.6.0
- Fix project and source URL
- Change license to LGPL-2.1-or-later
- Adapt for building with Meson
- Add lyx-fonts dependency
- Drop patch for Georgian

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.3-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Temuri Doghonadze <temuri.doghonadze@gmail.com> - 0.4.3-21
- Add Georgian translation

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-9
- Removed ldconfig scriptlets as per
  https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 27 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-4
- Added itex2mml information

* Fri Jul 08 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-3
- Incorporated further review feedback

* Thu Jul 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-2
- Incorporated some of the review feedback

* Tue Jun 21 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-1
- Initial RPM release
