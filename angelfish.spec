Name:           angelfish
Version:        23.03.90
Release:        1%{?dist}
Summary:        Plasma Mobile minimal web browser

License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/plasma-mobile/%{name}
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz


%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
 
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Feedback)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)

Requires:       hicolor-icon-theme
Requires:       kf5-kirigami2%{_isa} 
Requires:       qt5-qtfeedback%{_isa} 
Requires:       qt5-qtwayland%{_isa} 

%description
Web browser for mobile devices with Plasma integration

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/{MIT,GPL-2.0-or-later,LGPL-2.0-only,LGPL-2.0-or-later}.txt
%doc README.md

%{_kf5_bindir}/%{name}
%{_kf5_bindir}/%{name}-webapp

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/config.kcfg/%{name}settings.kcfg
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf5_datadir}/knotifications5/%{name}.notifyrc

%{_kf5_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jan Grulich <jgrulich@redhat.com> - 22.04-3
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 22.04-2
- Rebuild (qt5)

* Wed May 04 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Wed Mar 30 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-3
- Rebuild (qt5)

* Mon Mar 14 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-2
- Rebuild for Qt5WebEngine

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Fri Jan 21 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-2
- Ignore ppc64le and s390x 

* Tue Jan 11 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Version bump 21.12 and cosmetic fixes 

* Fri Nov 05 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-1
- initial version angelfish
