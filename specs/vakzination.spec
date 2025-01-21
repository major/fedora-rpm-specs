%global commit0 851a9fb0178003bb931d637356ee82c4ecfc4bc4
%global date 20241228
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           vakzination
Version:        23.01.0^git%{date}.%{shortcommit0}
Release:        2%{?dist}

License:        CC-PDDC AND Apache-2.0 AND LGPL-2.0-or-later AND CC0-1.0 AND BSD-3-Clause AND GPL-2.0-or-later AND FSFAP
Summary:        Vakzination manages your health certificates like vaccination, test, and recovery certificates.
Url:            https://invent.kde.org/plasma-mobile/vakzination
Source:         https://invent.kde.org/pim/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.gz

ExclusiveArch:  %{java_arches}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KHealthCertificate)
BuildRequires: cmake(KPim6Itinerary)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_kf6_datadir}/applications/ %{buildroot}/%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang

%license LICENSES/*

%{_kf6_bindir}/%{name}

%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0^git20241228.851a9fb-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 11 2025 Alessandro Astone <ales.astone@gmail.com> - 23.01.0^git20241228.851a9fb-1
- Use git snapshot for porting to Qt6

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 14 2023 Justin Zobel <justin.zobel@gmail.com> - 23.01.0-6
- Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 08 2023 Justin Zobel <justin.zobel@gmail.com> - 23.01.0-3
- rebuilt

* Thu May 04 2023 Justin Zobel <justin@1707.io> - 23.01.0-2
- Rebuild

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Fri Aug 26 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Mon Feb 21 2022 Justin Zobel <justin@1707.io> - 22.02
- Verison bump to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
