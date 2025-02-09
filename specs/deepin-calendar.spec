%global repo dde-calendar
%global __provides_exclude_from ^%{_libdir}/deepin-aiassistant/.*\\.so$

Name:           deepin-calendar
Version:        6.5.1
Release:        %autorelease
Summary:        Calendar for Deepin Desktop Environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  pkgconfig(libical)

BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
Calendar for Deepin Desktop Environment.

%prep
%autosetup -p1 -n %{repo}-%{version}

sed -i 's|lib/deepin-aiassistant/|${CMAKE_INSTALL_LIBDIR}/deepin-aiassistant/|' schedule-plugin/CMakeLists.txt

%build
%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install
install -pDm644 calendar-client/assets/dde-calendar/calendar/common/dde-calendar.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/dde-calendar.svg

%find_lang dde-calendar-service --with-qt --all-name
%find_lang dde-calendar --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f dde-calendar-service.lang -f dde-calendar.lang
%doc README.md
%license LICENSE
%{_bindir}/dde-calendar
%{_sysconfdir}/xdg/autostart/dde-calendar-service.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/dde-calendar.desktop
%{_datadir}/icons/hicolor/scalable/apps/dde-calendar.svg
%{_libdir}/deepin-aiassistant/serivce-plugins/libuosschedulex-plugin.so
%{_datadir}/deepin-manual/
%{_userunitdir}/com.dde.calendarserver.calendar.timer
%{_userunitdir}/*.service
%{_libexecdir}/deepin-daemon/dde-calendar-service
%dir %{_datadir}/dde-calendar
%dir %{_datadir}/dde-calendar/data
%{_datadir}/dde-calendar/data/huangli.db
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.calendar.json
%{_datadir}/metainfo/org.deepin.calendar.metainfo.xml

%changelog
%autochangelog
