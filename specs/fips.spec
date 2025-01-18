Name:           fips
Version:        3.4.0
Release:        20%{?dist}
Summary:        OpenGL-based FITS image viewer
License:        LGPL-3.0-or-later
Url:            https://github.com/matwey/fips3
Source:         https://github.com/matwey/fips3/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel >= 5.6
Requires:       hicolor-icon-theme

%description
FIPS is a cross-platform FITS viewer with responsive user interface. Unlike
other FITS viewers FIPS uses GPU hardware via OpenGL to provide usual
functionality such as zooming, panning and level adjustments. OpenGL 2.1 and
later is supported.

FIPS supports all 2D image formats (except for floating point formats on OpenGL
2.1). FITS image extension has basic limited support.
FITS image extension has basic limited support.

%prep
%setup -q -n fips3-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/space.fips.Fips.desktop

%check
%ctest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/space.fips.Fips.desktop
%{_datadir}/metainfo/space.fips.Fips.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/space.fips.Fips.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4.0-18
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Matwey V. Kornilov <matwey.kornilov@gmail.com> - 3.4.0-9
- Use %cmake_build/%cmake_install macroes to fix f33 build

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Matwey V. Kornilov <matwey.kornilov@gmail.com> - 3.4.0-7
- Require qt5-qtbase-devel instead of qt5-devel (fc32+)

* Sun May 03 2020 Matwey V. Kornilov <matwey.kornilov@gmail.com> - 3.4.0-6
- Version 3.4.0 (RHBZ#1830571)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Matwey V. Kornilov <matwey.kornilov@gmail.com> - 3.3.1-4
- Update package description

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Matwey V. Kornilov <matwey.kornilov@gmail.com> - 3.3.1-1
- Version 3.3.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep  6 2018 Matwey V. Kornilov <matwey.kornilov@gmail.com> - 3.3.0-1
- Initial build
