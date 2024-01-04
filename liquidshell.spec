Name:           liquidshell
Version:        1.9.0
Release:        %autorelease
Summary:        Basic desktop shell using QtWidgets

License:        GPL-3.0-or-later
URL:            https://apps.kde.org/liquidshell/
Source0:        https://download.kde.org/stable/liquidshell/liquidshell-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5ThemeSupport)
# provide libQt5ThemeSupport.a
BuildRequires:  qt5-qtbase-static

BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5NewStuff)

BuildRequires:  cmake(packagekitqt5)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       kf5-knotifications

%description
liquidshell is an alternative to plasmashell. It does not use QtQuick but
instead relies on QtWidgets, therefore no hardware graphics acceleration is
needed.

Main Features:

* Wallpaper per virtual desktop
* No animations, no CPU hogging, low Memory footprint
* Instant startup
* No use of activities
* QtWidgets based, therefore follows widget style from systemsettings
* Icons are used from your globally defined icon theme from systemsettings
* Colors are used from your globally defined color theme from systemsettings
* Can additionally be styled with css by passing the commandline option
-stylesheet filename.css (see included example stylesheet.css)
* uses existing KDE dialogs for most configurations, e.g. StartMenu, Virtual
Desktops, Bluetooth, Network
* One bottom DesktopPanel
* Desktop Applets

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml

%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/liquidshell
%{_bindir}/start_liquidshell
%{_datadir}/applications/org.kde.liquidshell.desktop
%{_datadir}/icons/hicolor/48x48/apps/liquidshell.png
%{_datadir}/knotifications5/liquidshell.notifyrc
%{_metainfodir}/org.kde.liquidshell.appdata.xml
%{_datadir}/xsessions/liquidshell-session.desktop

%changelog
%autochangelog