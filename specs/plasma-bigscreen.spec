%global commit a1b44a8d9c27a527a0004cdd59db8c18f6cee3ba
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20260218.085444

Name:          plasma-bigscreen
Version:       6.5.80^%{gitdate}.%{shortcommit}
Release:       1%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later and CC-BY-SA-4.0
Summary:       A big launcher giving you access to any installed apps and skills
Url:           https://invent.kde.org/plasma/plasma-bigscreen

# Not currently in the plasma releases. Getting from gitlab tags.
# Source0:       http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source0:       https://invent.kde.org/plasma/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

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
BuildRequires: cmake(KF6BluezQt)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Screen)

BuildRequires: cmake(Plasma)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(PlasmaWaylandProtocols)

BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(SDL3)
BuildRequires: pkgconfig(libcec)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6WebEngineCore)

Requires:   %{name}-wayland = %{version}-%{release}
Requires:   qt6qml(org.kde.plasma.private.nanoshell)


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
%find_lang plasma-bigscreen --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_mediacenter_{audiodevice,bigscreen_settings,kdeconnect,wifi}.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/plasma-bigscreen-swap-session.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.{inputhandler,uvcviewer}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f plasma-bigscreen.lang
%license LICENSES/*
%{_kf6_bindir}/plasma-bigscreen-{common-env,envmanager,settings,swap-session,uvcviewer,wayland,webapp,inputhandler}
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mediacenter_*.so
%{_kf6_qmldir}/org/kde//bigscreen/
%{_kf6_metainfodir}/org.kde.plasma.bigscreen.metainfo.xml
%{_kf6_datadir}/plasma/look-and-feel/org.kde.plasma.bigscreen/
%{_kf6_datadir}/plasma/plasmoids/org.kde.bigscreen.homescreen/
%{_kf6_datadir}/plasma/shells/org.kde.plasma.bigscreen/
%{_kf6_datadir}/sounds/plasma-bigscreen/
%{_kf6_datadir}/dbus-1/interfaces/org.kde.biglauncher.xml
%{_kf6_qtplugindir}/plasma/applets/org.kde.bigscreen.homescreen.so
%{_kf6_qtplugindir}/kf6/kded/kded_plasma_bigscreen_start.so
%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.inputhandler.desktop
%{_kf6_datadir}/applications/kcm_mediacenter_*.desktop
%{_kf6_datadir}/applications/plasma-bigscreen-swap-session.desktop
%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.uvcviewer.desktop

%files wayland
%{_kf6_bindir}/plasma-bigscreen-wayland
%{_kf6_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop


%changelog
* Thu Feb 19 2026 Steve Cossette <farchord@gmail.com> - 6.5.80^20260218.085444.a1b44a8-1
- Updated to latest git snapshot

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.80~20251021.093642.6a767b3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Oct 29 2025 Steve Cossette <farchord@gmail.com> - 6.4.80~20251021.093642.6a767b3-2
- Bump for rebuild for plasma 6.5 + PackageKit-Qt

* Sun Oct 26 2025 Steve Cossette <farchord@gmail.com> - 6.4.80~20251021.093642.6a767b3-1
- Updated to latest git snapshot

* Thu Oct 23 2025 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-8
- Rebuild for plasma-activities change

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

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
