Name:           kweather 
Version:        23.01.0
Release:        1%{?dist}
License:        GPLv2+
Summary:        Convergent KDE weather application
Url:            https://invent.kde.org/plasma-mobile/kweather
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KWeatherCore)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5QuickCharts)

Requires:       kf5-kirigami2
Requires:       kf5-kirigami2-addons
Requires:       hicolor-icon-theme

%description
Weather application for Plasma Mobile

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
chmod -x %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%find_lang %{name}

%check
appstreamcli validate --no-net %{buildroot}%{_kf5_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_metainfodir}/org.kde.plasma.%{name}_1x4.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf5_datadir}/dbus-1/services/org.kde.%{name}.service
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.%{name}_1x4.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x4/contents/ui/LocationSelector.qml
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x4/contents/ui/WeatherContainer.qml
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x4/contents/ui/main.qml
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x4/metadata.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x4/metadata.json
%{_kf5_qtplugindir}/plasma/applets/plasma_applet_%{name}_1x4.so

%changelog
* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Rebuild against kweathercore 0.7

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Tue Sep 20 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.06-3
- Rebuild for kweathercore 0.6

* Tue Sep 20 2022 Justin Zobel <justin@1707.io> - 22.06-2
- Rebuild

* Fri Aug 26 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-2
- Lang packs added.

* Sat Jul 17 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- 21.06 

* Sat May 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
