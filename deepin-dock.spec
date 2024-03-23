%global sname deepin-dock
%global repo dde-dock
%global __provides_exclude_from ^%{_prefix}/lib/dde-.*\\.so$

%global start_logo start-here
Name:           %{sname}
Version:        5.5.81
Release:        %autorelease
Summary:        The dock of Deepin Desktop Environment
# migrated to SPDX
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  dtkwidget-devel >= 5.1
BuildRequires:  dtkgui-devel >= 5.2.2.16
BuildRequires:  dtkcore-devel >= 5.1
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  qt5-linguist
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  deepin-control-center-devel >= 5.5.77
Requires:       dbusmenu-qt5
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make
Requires:       deepin-network-core
Requires:       deepin-qt-dbus-factory
Requires:       xcb-util-wm
Requires:       xcb-util-image

%description
Deepin desktop-environment - Dock module.

%package devel
Summary:        Development package for %{sname}

%description devel
Header files and libraries for %{sname}.

%prep
%autosetup -p1 -n %{repo}-%{version}

%if 0%{?fedora}
# set icon to Fedora logo
sed -i 's|deepin-launcher|%{start_logo}|' frame/item/launcheritem.cpp
%endif

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} # needed to install configfile
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_sysconfdir}/%{repo}/
%{_bindir}/%{repo}
%dir %{_prefix}/lib/%{repo}/
%dir %{_prefix}/lib/%{repo}/plugins
%{_prefix}/lib/%{repo}/plugins/libdatetime.so
%{_prefix}/lib/%{repo}/plugins/libmultitasking.so
%{_prefix}/lib/%{repo}/plugins/liboverlay-warning.so
%{_prefix}/lib/%{repo}/plugins/libshow-desktop.so
%{_prefix}/lib/%{repo}/plugins/libshutdown.so
%{_prefix}/lib/%{repo}/plugins/libtrash.so
%{_prefix}/lib/%{repo}/plugins/libtray.so
%{_prefix}/lib/%{repo}/plugins/libonboard.so
%{_prefix}/lib/%{repo}/plugins/system-trays/
%{_datadir}/%{repo}/
%{_datadir}/dcc-dock-plugin/
%{_datarootdir}/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml
%{_datarootdir}/polkit-1/actions/com.deepin.dde.dock.overlay.policy
%{_prefix}/lib/dde-control-center/modules/
%{_datadir}/dsg/

%files devel
%license LICENSE
%doc plugins/plugin-guide
%{_includedir}/%{repo}/
%{_libdir}/pkgconfig/%{repo}.pc
%{_libdir}/cmake/DdeDock/DdeDockConfig.cmake

%changelog
%autochangelog
