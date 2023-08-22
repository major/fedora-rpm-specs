%global repo dde-calendar
%global __provides_exclude_from ^%{_prefix}/lib/dde-.*\\.so$

Name:           deepin-calendar
Version:        5.10.0
Release:        %autorelease
Summary:        Calendar for Deepin Desktop Environment
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

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
BuildRequires:  pkgconfig(libical)
BuildRequires:  gmock-devel
BuildRequires:  systemd-rpm-macros
Requires:       hicolor-icon-theme
Requires:       deepin-daemon%{?_isa}
Recommends:     deepin-manual

%description
Calendar for Deepin Desktop Environment.

%prep
%autosetup -p1 -n %{repo}-%{version}

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
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
%{_prefix}/lib/deepin-aiassistant
%{_prefix}/lib/deepin-daemon/%{repo}-service
%{_datadir}/deepin-manual/
%{_userunitdir}/com.dde.calendarserver.calendar.*

%changelog
%autochangelog
