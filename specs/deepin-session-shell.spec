Name:           deepin-session-shell
Version:        6.0.52
Release:        %autorelease
Summary:        Deepin Desktop Environment - session-shell module
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-session-shell-snipe
Source0:        %{url}/archive/%{version}/dde-session-shell-snipe-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(GTest)

BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(liblightdm-qt6-3)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libcrypto)

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
%autosetup -p1 -C

sed -i 's|/usr/lib|%{_libdir}|' CMakeLists.txt

%build
%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}%{_bindir}/deepin-greeter

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/deepin/greeters.d/00-xrandr
%{_sysconfdir}/deepin/greeters.d/10-cursor-theme
%{_sysconfdir}/deepin/greeters.d/lightdm-deepin-greeter
%dir %{_sysconfdir}/lightdm/deepin
%{_sysconfdir}/lightdm/deepin/qt-theme.ini
%{_sysconfdir}/pam.d/dde-lock
%{_sysconfdir}/pam.d/deepin-lightdm-autologin
%{_bindir}/dde-lock
%{_bindir}/deepin-greeter
%{_bindir}/lightdm-deepin-greeter
%{_libdir}/security/pam_inhibit_autologin.so
%{_datadir}/applications/dde-lock.desktop
%{_datadir}/dbus-1/services/org.deepin.dde.LockFront1.service
%{_datadir}/dbus-1/services/org.deepin.dde.ShutdownFront1.service
%{_datadir}/dde-session-shell/
%{_datadir}/deepin-authentication/privileges/lightdm-deepin-greeter.conf
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.session-shell.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.session-shell.json
%{_datadir}/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/
%{_datadir}/dsg/configs/org.deepin.dde.lock/
%{_datadir}/dsg/configs/org.deepin.dde.session-shell/
%{_datadir}/lightdm/lightdm.conf.d/50-deepin.conf
%{_datadir}/xgreeters/lightdm-deepin-greeter.desktop

%files devel
%{_includedir}/dde-session-shell/
%{_libdir}/cmake/DdeSessionShell/

%changelog
%autochangelog
