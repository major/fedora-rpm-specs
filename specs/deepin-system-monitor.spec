Name:           deepin-system-monitor
Version:        6.5.37
Release:        %autorelease
Summary:        A more user-friendly system monitor
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  libicu-devel

BuildRequires:  cmake(PolkitQt6-1)

BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(dde-dock)

BuildRequires:  deepin-gettext-tools

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
#Requires:       deepin-qt6integration
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1

sed -i 's|lib/|${CMAKE_INSTALL_LIBDIR}/|' deepin-system-monitor-plugin/CMakeLists.txt

%build
export CXXFLAGS="%{optflags} -Wno-error=incompatible-pointer-types"
%cmake -GNinja -DUSE_DEEPIN_WAYLAND=ON
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/deepin-system-monitor
%{_bindir}/deepin-system-monitor-server
%{_bindir}/deepin-system-monitor-plugin-popup
%{_prefix}/lib/deepin-daemon/deepin-system-monitor-system-server
%{_libdir}/dde-dock/plugins/libdeepin-system-monitor-plugin.so
%{_libdir}/deepin-service-manager/libdeepin-system-monitor-daemon.so
%{_datadir}/applications/deepin-system-monitor.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/org.deepin.SystemMonitorSystemServer.service
%{_datadir}/dbus-1/system.d/org.deepin.SystemMonitorSystemServer.conf
%{_unitdir}/deepin-system-monitor-system-server.service
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.system-monitor.json
%{_datadir}/deepin-service-manager/other/deepin-system-monitor-system-server.json
%{_datadir}/deepin-system-monitor/
%{_datadir}/deepin-system-monitor-plugin-popup/
%{_datadir}/deepin-system-monitor-plugin/
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.system-monitor.gschema.xml
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/deepin-manual/manual-assets/application/deepin-system-monitor/
%{_datadir}/deepin-service-manager/user/deepin-system-monitor-daemon.json
%{_datadir}/dsg/configs/org.deepin.system-monitor/*.json
%{_datadir}/dde-dock/icons/dcc-setting/dcc-system-monitor.dci

%changelog
%autochangelog
