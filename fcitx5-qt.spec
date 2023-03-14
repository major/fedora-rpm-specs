%global __provides_exclude_from ^%{_libdir}/(fcitx5|qt5)/.*\\.so$

%ifarch s390x
# Don't build fcitx5-qt6 for s390x
%global build_qt6 0
%else
%global build_qt6 1
%endif

Name:           fcitx5-qt
Version:        5.0.17
Release:        %autorelease
Summary:        Qt library and IM module for fcitx5
# Fcitx5Qt{4,5}DBusAddons Library and Input context plugin are released under BSD.
License:        LGPLv2+ and BSD
URL:            https://github.com/fcitx/fcitx5-qt
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui) 
BuildRequires:  gettext
BuildRequires:  qt5-qtbase-private-devel
%if %{build_qt6}
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  qt6-qtbase-private-devel
%endif
# This needs to be rebuilt on every minor Qt5 version bump



Requires:       %{name}-module%{?_isa} = %{version}-%{release}
Requires:       %{name}-libfcitx5qtdbus%{?_isa} = %{version}-%{release}
Requires:       %{name}-libfcitx5qt5widgets%{?_isa} = %{version}-%{release}
Requires:       ((fcitx5-qt6%{?_isa} = %{version}-%{release}) if qt6-qtbase)

%description
Qt library and IM module for fcitx5.

%package module
Summary:        Provides seperately modules for fcitx5-qt

%description module
This package provides im-modules that can be installed seperately
from fcitx5-qt.

%package libfcitx5qtdbus
Summary:        Provides libFcitx5Qt5DBusAddons for fcitx5

%description libfcitx5qtdbus
This package provides libFcitx5Qt5DBusAddons for fcitx5.

%package libfcitx5qt5widgets
Summary:        Provide libFcitx5Qt5WidgetsAddons for fcitx5

%description libfcitx5qt5widgets
This package provides libFcitx5Qt5WidgetsAddons for fcitx5.

%if %{build_qt6}
%package -n fcitx5-qt6
Summary:        Qt 6 support for fcitx5
# This needs to be rebuilt on every minor Qt6 version bump
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description -n fcitx5-qt6
Qt6 library and IM module for fcitx5.
%endif

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel
Requires:       cmake-filesystem%{?_isa}

%description devel
Development files for %{name}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -GNinja -DENABLE_QT4=False \
%if %{build_qt6}
    -DENABLE_QT6=True
%else
    -DENABLE_QT6=False
%endif
%cmake_build 

%install
%cmake_install

%find_lang %{name}


%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libexecdir}/fcitx5-qt5-gui-wrapper
%{_libdir}/fcitx5/qt5/
%{_datadir}/applications/org.fcitx.fcitx5-qt5-gui-wrapper.desktop
%if %{build_qt6}
%files -n fcitx5-qt6
%{_qt6_plugindir}/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%{_libdir}/libFcitx5Qt6DBusAddons.so.1
%{_libdir}/libFcitx5Qt6DBusAddons.so.*.*
%endif

%files devel
%{_includedir}/Fcitx5Qt5/
%{_libdir}/cmake/Fcitx5Qt5*
%{_libdir}/libFcitx5Qt5DBusAddons.so
%{_libdir}/libFcitx5Qt5WidgetsAddons.so
%if %{build_qt6}
%{_libdir}/libFcitx5Qt6DBusAddons.so
%{_libdir}/cmake/Fcitx5Qt6*
%{_includedir}/Fcitx5Qt6/
%endif


%files module 
%{_qt5_plugindir}/platforminputcontexts/libfcitx5platforminputcontextplugin.so

%files libfcitx5qt5widgets
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.*.*

%files libfcitx5qtdbus
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libFcitx5Qt5DBusAddons.so.1
%{_libdir}/libFcitx5Qt5DBusAddons.so.*.*

%changelog
%autochangelog
