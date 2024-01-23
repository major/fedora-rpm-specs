# Control wayland by default
%if (0%{?rhel} && 0%{?rhel} < 9)
%bcond_with wayland_default
%else
%bcond_without wayland_default
%endif

Name:          plasma-bigscreen
Version:       5.27.9
Release:       2%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later and CC-BY-SA-4.0
Summary:       A big launcher giving you access to any installed apps and skills
Url:           https://invent.kde.org/plasma/plasma-bigscreen

%global        stable %stable_kf5
Source0:       http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5ActivitiesStats)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(libkworkspace)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Multimedia)


# Require Xorg/Wayland sessions appropriately
%if ! %{with wayland_default}
Recommends: %{name}-wayland = %{version}-%{release}
Requires:   %{name}-x11 = %{version}-%{release}
%else
Requires:   %{name}-wayland = %{version}-%{release}
Recommends: %{name}-x11 = %{version}-%{release}
%endif


%package  wayland
Summary:   Wayland support for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Requires:  plasma-workspace-wayland >= %{version}


%description wayland
%{summary}


%package  x11
BuildArch: noarch
Summary:   X11 support for %{name}
Requires:  %{name} = %{version}-%{release}
Requires:  plasma-workspace-x11 >= %{version}


%description x11
%{summary}



%description
%{summary}


%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
chmod +x %{buildroot}%{_kf5_bindir}/mycroft-skill-launcher.py

%find_lang plasma-bigscreen --with-man --with-qt --all-name


%files -f plasma-bigscreen.lang
%license LICENSES/*
%{_kf5_bindir}/mycroft-skill-launcher.py
%{_kf5_qtplugindir}/kcms/kcm_mediacenter_*.so
%{_kf5_qtplugindir}/plasma/applets/plasma_containment_biglauncherhomescreen.so
%{_kf5_qmldir}/org/kde/mycroft/bigscreen/
%{_kf5_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/*.qml
%{_kf5_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/
%{_kf5_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/
%{_kf5_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/
%{_kf5_datadir}/kpackage/kcms/kcm_mediacenter_wifi/
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.mycroft.bigscreen.homescreen.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.mycroft.bigscreen.desktop
%{_kf5_datadir}/kservices5/plasma-lookandfeel-org.kde.plasma.mycroft.bigscreen.desktop
%{_kf5_metainfodir}/org.kde.mycroft.bigscreen.homescreen.appdata.xml
%{_kf5_metainfodir}/org.kde.plasma.mycroft.bigscreen.appdata.xml
%{_kf5_metainfodir}/org.kde.plasma.mycroft.bigscreen.metainfo.xml
%{_kf5_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/
%{_kf5_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/
%{_kf5_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/
%{_kf5_datadir}/sounds/plasma-bigscreen/


%files wayland
%{_kf5_bindir}/plasma-bigscreen-wayland
%{_kf5_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop


%files x11
%{_kf5_bindir}/plasma-bigscreen-x11
%{_kf5_datadir}/xsessions/plasma-bigscreen-x11.desktop


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.9-1
- 5.27.9

* Sun Oct 15 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.8-1
- Update to 5.27.8

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-4
- Fixes on the spec file

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-3
- Add plasma-workspace requirements.

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-2
- Create wayland/x11 subpackages

* Wed Mar 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- Update to 5.27.2

* Sun Jan 22 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- Initial Package
