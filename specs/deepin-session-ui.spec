%global repo dde-session-ui
%global __provides_exclude_from ^%{_libdir}/dde-.*\\.so$

Name:           deepin-session-ui
Version:        6.0.22
Release:        %autorelease
Summary:        Deepin desktop-environment - Session UI module
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-session-ui
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
# for translation, lrelease-qt5
BuildRequires:  qt5-linguist

BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(DtkTools)
BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(DtkGui)

BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel

BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libdeepin_pw_check)
BuildRequires:  libxcrypt-devel
BuildRequires:  libXext-devel

Requires:       deepin-daemon
Requires:       deepin-session-shell
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

sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
%find_lang dde-session-ui --with-qt --all-name
rm %{buildroot}%{_datadir}/dde-session-ui/translations/dde-session-ui.qm

%files -f dde-session-ui.lang
%doc README.md
%license LICENSE
%{_bindir}/dde-*
%{_datadir}/icons/hicolor/scalable/devices/computer.svg
%{_datadir}/dbus-1/services/*.service
%{_prefix}/lib/dde-control-center/reset-password-dialog
%dir %{_prefix}/lib/deepin-daemon/
%{_prefix}/lib/deepin-daemon/dde-*
%{_prefix}/lib/deepin-daemon/dnetwork-secret-dialog

%changelog
%autochangelog
