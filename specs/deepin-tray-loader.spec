%global forgeurl https://github.com/linuxdeepin/dde-tray-loader
Version:        2.0.16
%global tag %{version}
%forgemeta

%global repo dde-tray-loader

Name:           deepin-tray-loader
Release:        %autorelease
Summary:        A set of tray plugins for Deepin
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND CC-BY-4.0 AND CC0-1.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)

BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  wayland-devel

%description
The dde-tray-loader project provides a set of tray plugins that integrated into
task bar and the tool loader which can load the plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%forgeautosetup -p1
sed -i '/LIBRARY DESTINATION/s|lib/dde-dock|${CMAKE_INSTALL_LIBDIR}/dde-dock|' \
    $(find ./plugins -name '*CMakeLists.txt')

%build
%cmake -GNinja \
    -DVERSION=%{version} \
    -DDTL_BUILD_WITH_QT6=ON \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*
%dir %{_sysconfdir}/dde-dock
%dir %{_sysconfdir}/dde-dock/indicator
%{_sysconfdir}/dde-dock/indicator/keybord_layout.json
%{_libexecdir}/trayplugin-loader
%dir %{_libdir}/dde-dock
%dir %{_libdir}/dde-dock/plugins
%{_libdir}/dde-dock/plugins/*.so
%dir %{_libdir}/dde-dock/plugins/system-trays
%{_libdir}/dde-dock/plugins/system-trays/*.so
%{_libdir}/libdde-trayplugin-interface.so.1*
%{_qt6_plugindir}/wayland-shell-integration/libplugin-shell.so
%{_datadir}/dde-dock/
%{_datadir}/dock-wirelesscasting-plugin/
%{_datadir}/trayplugin-loader/
%{_datadir}/dsg/configs/org.deepin.dde.dock/
%{_datadir}/dsg/configs/org.deepin.dde.tray-loader/

%files devel
%{_includedir}/dde-dock/
%dir %{_includedir}/dde-tray-loader
%dir %{_includedir}/dde-tray-loader/protocol
%{_includedir}/dde-tray-loader/protocol/plugin-manager-v1.xml
%{_libdir}/libdde-trayplugin-interface.so
%{_libdir}/cmake/DdeDock/
%{_libdir}/cmake/DdeTrayLoader/
%{_libdir}/pkgconfig/dde-dock.pc
%{_libdir}/pkgconfig/dde-tray-loader.pc

%changelog
%autochangelog
