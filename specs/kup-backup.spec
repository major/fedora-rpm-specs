# kup already exists in the Fedora namespace, so we used a different name
%global projectname kup

Name:           kup-backup
Version:        6.7.90
Release:        1%{?dist}
Summary:        Backup scheduler for the Plasma desktop

# CC0-1.0 is used but only in a couple upstream-related CI files, which we aren't using.
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://apps.kde.org/%{projectname}/
Source0:        http://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{projectname}-%{version}.tar.xz
Source1:        http://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{projectname}-%{version}.tar.xz.sig

# Base
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)

# KF6
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Crash)

# Plasma
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)

# Others
BuildRequires:  pkgconfig(libgit2)

# Runtime Reqs
Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.kcmutils)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kquickcontrolsaddons)
Requires:       qt6qml(org.kde.plasma.components)
Requires:       qt6qml(org.kde.plasma.core)
Requires:       qt6qml(org.kde.plasma.extras)
Requires:       qt6qml(org.kde.plasma.plasma5support)
Requires:       qt6qml(org.kde.plasma.plasmoid)
Requires:       qt6qml(QtQuick)
Requires:       qt6qml(QtQuick.Layouts)

%description
%{summary}.

%prep
%autosetup -n %{projectname}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{projectname}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_kup.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kup-daemon.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kup.appdata.xml

%files -f %{projectname}.lang
%doc README.md MAINTAINER
%license LICENSES/*
%{_sysconfdir}/xdg/autostart/kup-daemon.desktop
%{_kf6_bindir}/kup-*
%{_kf6_qtplugindir}/kf6/kfileitemaction/kupfileitemaction.so
%{_kf6_qtplugindir}/kf6/kio/kio_bup.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kup.so
%{_kf6_datadir}/applications/kcm_kup.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/kup.svg
%{_kf6_datadir}/knotifications6/kupdaemon.notifyrc
%{_kf6_metainfodir}/org.kde.kup.appdata.xml
%{_kf6_datadir}/qlogging-categories6/kup.categories
%{_kf6_datadir}/applications/kup-daemon.desktop
%{_kf6_qtplugindir}/plasma/applets/org.kde.kupapplet.so



%changelog
* Sat Sep 12 2026 Steve Cossette <farchord@gmail.com> - 6.7.90-1
- 6.7.90

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0^git20260214.094327.92115c2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Feb 16 2026 Steve Cossette <farchord@gmail.com> - 0.10.0^git20260214.094327.92115c2-1
- Initial commit
