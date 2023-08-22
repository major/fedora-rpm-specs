Name:           deepin-system-monitor
Version:        6.0.3
Release:        %autorelease
Summary:        A more user-friendly system monitor
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         deepin-system-monitor-procps-ng-4.patch
Patch1:         deepin-system-monitor-c99.patch
Patch2:         https://github.com/linuxdeepin/deepin-system-monitor/commit/94c5e9d15fc5bffdff002e5a65068dc93041f6d9.patch
Patch3:         https://raw.githubusercontent.com/archlinux/svntogit-community/packages/deepin-system-monitor/trunk/a159e571.patch
Source1:        %{name}-appdata.xml

BuildRequires:  cmake
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(dtkwm) >= 2.0
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(KF5WaylandClient)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  qt5-linguist
BuildRequires:  libpcap-devel
BuildRequires:  libcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  libicu-devel
BuildRequires:  deepin-dock-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  deepin-gettext-tools
BuildRequires:  libnl3-devel
BuildRequires:  systemd-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
Requires:       hicolor-icon-theme
Requires:       deepin-qt5integration%{?_isa}
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1
sed -i 's:/usr/lib/x86_64-linux-gnu/qt5/bin/:%{_qt5_bindir}/:' \
    deepin-system-monitor-daemon/translations/translate_generation.sh \
    deepin-system-monitor-plugin/translations/translate_generation.sh

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DUSE_DEEPIN_WAYLAND=OFF
%cmake_build

%install
%cmake_install
install -Dm644 %SOURCE1 %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/autostart/%{name}-daemon.desktop
# caps sync with debian/postinst
%caps(cap_net_raw,cap_dac_read_search,cap_sys_ptrace+ep) %{_bindir}/%{name}
%{_bindir}/%{name}-daemon
%{_bindir}/%{name}-plugin-popup
%{_prefix}/lib/dde-dock/plugins/lib%{name}-plugin.so
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{name}/
%{_datadir}/%{name}-daemon/
%{_datadir}/%{name}-plugin-popup/
%{_datadir}/%{name}-plugin/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/polkit-1/actions/com.deepin.*.policy
%{_datadir}/deepin-manual/

%changelog
%autochangelog
