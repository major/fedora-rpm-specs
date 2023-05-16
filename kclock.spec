%global klockd_name org.kde.kclockd
%global orig_name org.kde.kclock

Name:           kclock
Version:        23.04.1
Release:        1%{?dist}
License:        GPLv2+ and LGPLv2.1+ and CC-BY and GPLv3+
Summary:        Clock app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/kclock
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream
 
BuildRequires:  libsodium-devel
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Concurrent)

BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Plasma)

 
Requires:       kf5-kirigami2
Requires:       hicolor-icon-theme
Requires:       kf5-kirigami2-addons-dateandtime


%description
A convergent clock application for Plasma.


%package plasma-applet
Summary: Plasma5 applet for kclock
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plasma-applet
%{summary}.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf5
%cmake_build

%install
%cmake_install
sed -i 's/GPL-2+/GPL-2.0-or-later/g' %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%find_lang %{name} --all-name


%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf5_bindir}/%{name}
%{_kf5_bindir}/%{name}d
%{_kf5_datadir}/applications/%{orig_name}.desktop
%{_kf5_metainfodir}/%{orig_name}.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_sysconfdir}/xdg/autostart/%{klockd_name}-autostart.desktop
%{_datadir}/dbus-1/services/org.kde.%{name}d.service
%{_kf5_datadir}/knotifications5/%{name}d.notifyrc
%{_kf5_datadir}/dbus-1/interfaces/*.xml

%files plasma-applet
%{_kf5_metainfodir}/org.kde.plasma.%{name}_1x2.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/%{name}_plasmoid_1x2.svg
%{_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x2/
%{_qt5_plugindir}/plasma/applets/plasma_applet_%{name}_1x2.so

%changelog
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

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- version update : 21.06

* Sun Jun 06 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
- BR: appstream added

* Sat May 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
