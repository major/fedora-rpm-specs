%global repo dde-session-shell-snipe

Name:           deepin-session-shell
Version:        6.0.21
Release:        %autorelease
Summary:        Deepin Desktop Environment - session-shell module
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-session-shell-snipe
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# Use registered OnlyShowIn value
Patch0:         https://github.com/linuxdeepin/dde-session-shell-snipe/pull/376.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Network)
# BuildRequires:  cmake(Qt5WebEngineWidgets)
# lrelease-qt5
BuildRequires:  qt5-linguist

BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(DtkCMake)
BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(DtkTools)
BuildRequires:  cmake(GTest)

BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(liblightdm-qt5-3)
BuildRequires:  pam-devel
BuildRequires:  openssl-devel
BuildRequires:  deepin-pw-check-devel

BuildRequires:  desktop-file-utils

# provides needed directories
Requires:       dbus-common
Requires:       %{_bindir}/qdbus-qt5
# used by /etc/deepin/greeters.d/00-xrandr
Requires:       %{_bindir}/xrandr
# used by /etc/deepin/greeters.d/10-cursor-theme
Requires:       %{_bindir}/xrdb
Requires:       lightdm

Provides:       lightdm-deepin-greeter%{?_isa} = %{version}-%{release}
Provides:       lightdm-greeter%{?_isa} = %{version}-%{release}

%description
DDE session shell provides two applications: dde-lock and lightdm-deepin-greeter.
dde-lock provides screen lock function, and lightdm-deepin-greeter provides
login function.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}

sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/usr/lib/x86_64-linux-gnu|%{_libdir}|' \
    files/wayland/deepin-greeter-wayland \
    files/wayland/lightdm-deepin-greeter-wayland

%build
%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install
%find_lang dde-session-shell --with-qt
rm %{buildroot}%{_datadir}/dde-session-shell/translations/dde-session-shell.qm
chmod +x %{buildroot}%{_bindir}/deepin-greeter

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f dde-session-shell.lang
%doc README.md
%license LICENSE
%{_bindir}/dde-lock
%{_bindir}/lightdm-deepin-greeter
%{_bindir}/deepin-greeter
%dir %{_prefix}/lib/dde-session-shell
%dir %{_prefix}/lib/dde-session-shell/modules
%{_prefix}/lib/dde-session-shell/modules/libvirtualkeyboard.so
%dir %{_datadir}/dde-session-shell
%{_datadir}/dde-session-shell/dde-session-shell.conf
%{_datadir}/deepin-authentication/
%{_datadir}/applications/dde-lock.desktop
%{_datadir}/xgreeters/lightdm-deepin-greeter.desktop
%{_datadir}/dbus-1/services/org.deepin.dde.*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/*.json
%{_datadir}/dsg/configs/org.deepin.dde.lock/*.json
%{_sysconfdir}/pam.d/dde-lock
%{_sysconfdir}/deepin/greeters.d/00-xrandr
%{_sysconfdir}/deepin/greeters.d/10-cursor-theme
%{_sysconfdir}/deepin/greeters.d/lightdm-deepin-greeter
%{_sysconfdir}/lightdm/deepin/qt-theme.ini

%files devel
%{_includedir}/dde-session-shell/
%{_libdir}/cmake/DdeSessionShell/

%changelog
%autochangelog
