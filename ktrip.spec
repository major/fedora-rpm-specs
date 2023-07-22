Name:           ktrip
Version:        23.04.3
Release:        2%{?dist}
License:        GPLv2+
Summary:        Public transport navigation, allows you to find journeys between specified locations, departures for a specific station and shows real-time delay and disruption information.
Url:            https://apps.kde.org/ktrip/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/ktrip-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kirigami2-addons-dateandtime
BuildRequires: kf5-rpm-macros
BuildRequires: kpublictransport-devel
BuildRequires: libappstream-glib
BuildRequires: qqc2-desktop-style
BuildRequires: reuse

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickControls2)

BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5ItemModels)

BuildRequires: pkgconfig(zlib)

# QML module dependencies
Requires:      kf5-ki18n%{?_isa}
Requires:      kf5-kirigami2%{?_isa}
Requires:      kf5-kirigami2-addons%{?_isa}
Requires:      kpublictransport%{?_isa}
Requires:      qt5-qtquickcontrols2%{?_isa}

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_kf5_bindir}/%{name}

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*

%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 27 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Sun Feb 27 2022 Justin Zobel <justin@1707.io> - 22.02-1
- Verison bump to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
