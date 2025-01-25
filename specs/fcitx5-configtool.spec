%global translation_domain kcm_fcitx5
	
# as of 2024-01, required dependencies 
# for building QT6 are not available 
# in Fedora 39 
#  - cmake(Plasma)
#  - cmake(KF6Svg)
#  - cmake(KF6KCMUtils)
%if 0%{?fedora} >= 40
%global use_qt6 1
%else
%global use_qt6 0
%endif

%if %{use_qt6}
%define qt_major_ver 6
%else
%define qt_major_ver 5
%endif

Name:           fcitx5-configtool
Version:        5.1.8
Release:        %autorelease
Summary:        Configuration tools used by fcitx5
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-configtool
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gettext-devel
BuildRequires:  kf%{qt_major_ver}-kwidgetsaddons-devel
BuildRequires:  kf%{qt_major_ver}-kirigami2-devel
BuildRequires:  kf%{qt_major_ver}-kdeclarative-devel
BuildRequires:  kf%{qt_major_ver}-kpackage-devel
BuildRequires:  kf%{qt_major_ver}-ki18n-devel
BuildRequires:  kf%{qt_major_ver}-kcoreaddons-devel
BuildRequires:  kf%{qt_major_ver}-kitemviews-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  cmake(KF%{qt_major_ver}IconThemes)
BuildRequires:  cmake(Qt%{qt_major_ver}QuickControls2)
BuildRequires:  cmake(Qt%{qt_major_ver}Svg)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  /usr/bin/appstream-util
%if %{use_qt6}
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6KCMUtils)
%else
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(KF5Plasma)
%endif

# to display scalable icons
Requires:       qt%{qt_major_ver}-qtsvg
# explicit requires on fcitx5-qt{5,6}-gui-wrapper
Requires:       fcitx5-qt-qt%{qt_major_ver}gui

%description
Configuration tools used by fcitx5.

%package -n kcm-fcitx5
Summary:        Config tools to be used on KDE based environment.
Requires:       kf%{qt_major_ver}-filesystem
Requires:       kf%{qt_major_ver}-kcmutils
Requires:       kf%{qt_major_ver}-plasma
Suggests:       %{name}%{?_isa} = %{version}-%{release}

%description -n kcm-fcitx5
Config tools to be used on KDE based environment. Can be installed seperately.

%package -n fcitx5-migrator
Summary:        Migration tools for fcitx5
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n fcitx5-migrator
Migration tools for fcitx5, containing fcitx5-migrator

%package -n fcitx5-migrator-devel
Summary:        Devel files for fcitx5-migrator
Requires:       fcitx5-migrator%{?_isa} = %{version}-%{release}

%description -n fcitx5-migrator-devel
Development files for fcitx5-migrator

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

#fix typos
sed -i 's/Catogories/Categories/g' src/configtool/org.fcitx.fcitx5-config-qt.desktop.in
sed -i 's/Catogories/Categories/g' src/migrator/app/org.fcitx.fcitx5-migrator.desktop.in

%build
%if %{use_qt6}
  %cmake_kf6 -GNinja -DUSE_QT6=On
%else
  %cmake_kf5 -GNinja -DUSE_QT6=Off
%endif
%cmake_build 

%install
%cmake_install
# kservices5/*.desktop desktop file dont't need to use desktop-file-install
# only for applications/*.desktop
for desktop_file_name in kbd-layout-viewer5 org.fcitx.fcitx5-config-qt org.fcitx.fcitx5-migrator
do
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/${desktop_file_name}.desktop
done
%find_lang %{name}
%find_lang %{translation_domain}


%files -f %{name}.lang 
%license LICENSES/GPL-2.0-or-later.txt
%doc README
%{_bindir}/fcitx5-config-qt
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_bindir}/kbd-layout-viewer5
%{_datadir}/applications/kbd-layout-viewer5.desktop

%files -n kcm-fcitx5 -f %{translation_domain}.lang 
%license LICENSES/GPL-2.0-or-later.txt
%if %{use_qt6}
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_fcitx5.so
%else
%{_datadir}/kpackage/kcms/%{translation_domain}
%{_kf5_qtplugindir}/plasma/kcms/systemsettings/kcm_fcitx5.so
%endif
%{_datadir}/applications/kcm_fcitx5.desktop
%{_bindir}/fcitx5-plasma-theme-generator

%files -n fcitx5-migrator
%{_bindir}/fcitx5-migrator
%{_libdir}/libFcitx5Migrator.so.5*
%{_libdir}/libFcitx5Migrator.so.1
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop

%files -n fcitx5-migrator-devel
%{_libdir}/libFcitx5Migrator.so

%changelog
%autochangelog
