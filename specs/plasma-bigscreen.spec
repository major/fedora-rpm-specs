%global commit 046d404e34aa04f4deddddd40e8bdf40dfa43d05
%global shortcommit 046d404
%global gitdate 20240204.214319

Name:          plasma-bigscreen
Version:       5.27.80~%{gitdate}.%{shortcommit}
Release:       6%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later and CC-BY-SA-4.0
Summary:       A big launcher giving you access to any installed apps and skills
Url:           https://invent.kde.org/plasma/plasma-bigscreen

# Not currently in the plasma releases. Getting from gitlab tags.
# Source0:       http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source0:       https://invent.kde.org/plasma/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Svg)

BuildRequires: cmake(Plasma)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)

BuildRequires: cmake(LibKWorkspace)

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Multimedia)


Requires:   %{name}-wayland = %{version}-%{release}


%package  wayland
Summary:   Wayland support for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Requires:  plasma-workspace-wayland >= %{version}
# Transition users upgrading from F39 and before to the wayland session
Obsoletes: %{name}-x11 < %{version}-%{release}
Conflicts: %{name}-x11 < %{version}-%{release}

%description wayland
%{summary}



%description
%{summary}


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
chmod +x %{buildroot}%{_kf6_bindir}/mycroft-skill-launcher.py
# F40: Remove the X11 Launcher
rm -v %{buildroot}%{_kf6_bindir}/plasma-bigscreen-x11
rm -v %{buildroot}%{_kf6_datadir}/xsessions/plasma-bigscreen-x11.desktop
%find_lang plasma-bigscreen --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_mediacenter_{audiodevice,bigscreen_settings,kdeconnect,wifi}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f plasma-bigscreen.lang
%license LICENSES/*
%{_kf6_bindir}/mycroft-skill-launcher.py
%{_kf6_qtplugindir}/kcms/kcm_mediacenter_*.so
%{_kf6_qmldir}/org/kde/mycroft/bigscreen/
%{_kf6_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/*.qml
%{_kf6_metainfodir}/org.kde.plasma.mycroft.bigscreen.appdata.xml
%{_kf6_metainfodir}/org.kde.plasma.mycroft.bigscreen.metainfo.xml
%{_kf6_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/
%{_kf6_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/
%{_kf6_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/
%{_kf6_datadir}/sounds/plasma-bigscreen/
%{_kf6_qtplugindir}/plasma/applets/org.kde.mycroft.bigscreen.homescreen.so
%{_kf6_datadir}/applications/kcm_mediacenter_*.desktop

%files wayland
%{_kf6_bindir}/plasma-bigscreen-wayland
%{_kf6_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~20240204.214319.046d404-4
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~20240204.214319.046d404-3
- Rebuild (qt6)

* Mon Mar 18 2024 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-2
- Building to accomodate new depend library sonames

* Mon Feb 05 2024 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-1
- Updated to Qt6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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
