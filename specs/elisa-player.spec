%global base_name elisa

Name:       elisa-player
Version:    24.12.2
Release:    %autorelease
Summary:    Elisa music player

# Main program LGPLv3+
# Background image CC-BY-SA
# Automatically converted from old format: LGPLv3+ and CC-BY-SA - review is highly recommended.
License:    LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:        https://community.kde.org/Elisa

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/elisa-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

Requires:       hicolor-icon-theme
Requires:       dbus-common
# QML module dependencies
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qt5compat%{?_isa}


%description
Elisa is a simple music player aiming to provide a nice experience for its
users.

%prep
%autosetup -n elisa-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang elisa --all-name --with-kde --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.elisa.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.elisa.appdata.xml

%files -f elisa.lang
%license COPYING
%{_kf6_bindir}/elisa
%{_kf6_datadir}/applications/org.kde.elisa.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.elisa.service
%{_kf6_datadir}/icons/hicolor/*/apps/elisa*
%{_kf6_datadir}/qlogging-categories6/elisa.categories
%{_kf6_metainfodir}/org.kde.elisa.appdata.xml
%{_kf6_libdir}/elisa/

%changelog
%autochangelog
