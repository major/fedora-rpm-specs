%global forgeurl https://github.com/KDE/choqok/
%global commit de3801bb52f4d4ee3ad3cbaa7f8704d0013881f3

Name:    choqok
Version: 1.7.0
Summary: KDE Micro-Blogging Client
License: GPL-3.0-only

%{forgemeta}

Release: %autorelease
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: %{name}.rpmlintrc

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: cmake(Qca-qt5)
BuildRequires: qt5-qtnetworkauth-devel
BuildRequires: kf5-purpose-devel
BuildRequires: extra-cmake-modules

# optional features
BuildRequires: cmake(TelepathyQt5)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5WebKit)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
A Free/Open Source micro-blogging client for K Desktop Environment.
The name comes from an ancient Persian word, which means Sparrow!
Choqok currently supports:
Twitter, Friendica, Mastodon social, Pump.io network, GNU social
and Open Collaboration Services.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep
%{forgesetup}
%autosetup -p1 -n %{archivename}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.choqok.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.choqok.desktop

%files -f %{name}.lang
%doc README AUTHORS changelog
%{_kf5_bindir}/choqok
%{_kf5_qtplugindir}/choqok_*.so
%{_kf5_qtplugindir}/kcm_choqok_*.so
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/applications/org.kde.choqok.desktop
%{_kf5_metainfodir}/org.kde.choqok.appdata.xml
%{_datadir}/dbus-1/services/org.kde.choqok.service
%{_kf5_datadir}/config.kcfg/*.kcfg
%{_kf5_datadir}/kservices5/choqok_*.desktop
%{_kf5_datadir}/choqok/
%{_kf5_datadir}/knotifications5/choqok.notifyrc
%{_kf5_datadir}/kxmlgui5/*choqok*/
%{_kf5_datadir}/qlogging-categories5/choqok.categories
%{_kf5_plugindir}/parts/konqchoqokplugin.so
%{_kf5_plugindir}/purpose/choqokplugin.so
%{_kf5_datadir}/kservices5/ServiceMenus/choqok_*.desktop
%{_kf5_datadir}/kservices5/konqchoqok.desktop
%{_kf5_datadir}/kservicetypes5/choqok*.desktop

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libchoqok.so.*
%{_kf5_libdir}/libgnusocialapihelper.so.*
%{_kf5_libdir}/libtwitterapihelper.so.*

%files devel
%{_includedir}/choqok/
%{_kf5_libdir}/libchoqok.so
%{_kf5_datadir}/cmake/modules/FindChoqok.cmake
%{_kf5_libdir}/libgnusocialapihelper.so
%{_kf5_libdir}/libtwitterapihelper.so

%changelog
%autochangelog
