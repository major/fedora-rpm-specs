Name:           vakzination
Version:        22.09
Release:        1%{?dist}
License:        Apache2.0 and BSD and CC-PDDC and CC0-1.0 and FSFAP and GPLv2+
Summary:        Vakzination manages your health certificates like vaccination, test, and recovery certificates.
Url:            https://invent.kde.org/plasma-mobile/vakzination
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/vakzination-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5Prison)
BuildRequires: cmake(KHealthCertificate)
BuildRequires: cmake(KPimItinerary)
BuildRequires: cmake(KPimPkPass)

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_kf5_datadir}/applications/ %{buildroot}/%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang

%license LICENSES/*

%{_kf5_bindir}/%{name}

%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%{_kf5_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
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
