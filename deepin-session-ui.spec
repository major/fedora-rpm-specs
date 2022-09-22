%global repo dde-session-ui
%global __provides_exclude_from ^%{_libdir}/dde-dock/.*\\.so$

Name:           deepin-session-ui
Version:        5.5.23
Release:        %autorelease
Summary:        Deepin desktop-environment - Session UI module
License:        GPLv3
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# fix crash at start of dde-osd
Patch0:         0001-Don-t-try-to-get-app-setting-if-appName-is-empty.patch

BuildRequires:  gcc-c++
BuildRequires:  deepin-gettext-tools
BuildRequires:  pkgconfig(dtkwidget) >= 5.1
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  dtkcore-devel >= 5.1
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gio-qt-devel
BuildRequires:  gtest-devel
%if 0%{?fedora}
Requires:       deepin-daemon
Requires:       deepin-session-shell
%else
Requires:       dde-daemon
%endif
Requires:       startdde

Provides:       deepin-notifications = %{version}-%{release}
Obsoletes:      deepin-notifications <= 3.3.4

%description
This project include those sub-project:

- dde-shutdown: User interface of shutdown.
- dde-lock: User interface of lock screen.
- dde-lockservice: The back-end service of locking screen.
- lightdm-deepin-greeter: The user interface when you login in.
- dde-switchtogreeter: The tools to switch the user to login in.
- dde-lowpower: The user interface of reminding low power.
- dde-osd: User interface of on-screen display.
- dde-hotzone: User interface of setting hot zone.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i 's:lib/deepin-daemon:libexec/deepin-daemon:' \
    dde-osd/files/com.deepin.dde.Notification.service \
    dde-osd/files/com.deepin.dde.freedesktop.Notification.service \
    dde-osd/files/com.deepin.dde.osd.service \
    dde-warning-dialog/com.deepin.dde.WarningDialog.service \
    dde-welcome/com.deepin.dde.welcome.service \
    CMakeLists.txt
sed -i 's|lib/dde-dock|%{_lib}/dde-dock|' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/dde-*
%{_bindir}/dmemory-warning-dialog
%{_libexecdir}/deepin-daemon/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/dbus-1/services/*.service
%{_libdir}/dde-dock/plugins/libnotifications.so
%{_prefix}/share/glib-2.0/schemas/com.deepin.dde.dock.module.notifications.gschema.xml

%changelog
%autochangelog
