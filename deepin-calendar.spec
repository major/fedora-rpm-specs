%global repo dde-calendar

Name:           deepin-calendar
Version:        5.9.1
Release:        %autorelease
Summary:        Calendar for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# fix build for ARM architectures
Patch0:         0001-needed-cstdint-for-uint32_t.patch

BuildRequires:  cmake
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  gmock-devel
BuildRequires:  systemd-rpm-macros
Requires:       hicolor-icon-theme
Requires:       deepin-daemon%{?_isa}
Recommends:     deepin-manual

%description
Calendar for Deepin Desktop Environment.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i "s:/usr/lib:%{_libdir}:" schedule-plugin/CMakeLists.txt
sed -i "s:lib/deepin-daemon/:libexec/deepin-daemon/:" \
    calendar-service/assets/data/com.deepin.dataserver.Calendar.service \
    calendar-service/assets/dde-calendar-service.desktop \
    calendar-service/CMakeLists.txt

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
install -m 644 -D calendar-client/assets/dde-calendar/calendar/common/dde-calendar.svg \
    ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps/%{repo}.svg

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/autostart/%{repo}-service.desktop
%{_bindir}/%{repo}
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/com.deepin.Calendar.service
%{_datadir}/dbus-1/services/com.deepin.dataserver.Calendar.service
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{repo}.svg
%{_libdir}/deepin-aiassistant
%{_libexecdir}/deepin-daemon/%{repo}-service
%{_datadir}/deepin-manual/
%{_userunitdir}/com.dde.calendarserver.calendar.*

%changelog
%autochangelog
