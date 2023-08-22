%global repo dde-launcher
%global sname deepin-launcher

Name:           %{sname}
Version:        5.6.1
Release:        %autorelease
Summary:        Deepin desktop-environment - Launcher module
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-launcher
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# applied in upstream git0612c1181f232eb1c7be05a40c9c951a51cd0f2a
Patch0:         0001-fix-window-mode-show-slowly.patch
Patch1:         https://github.com/linuxdeepin/dde-launcher/pull/369.patch

BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  dtkwidget-devel
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  gtest-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make

Requires:       deepin-menu
Requires:       deepin-daemon
Requires:       startdde
Requires:       hicolor-icon-theme
Requires:       %{_bindir}/dbus-send

%description
%{summary}.

%prep
%autosetup -p1 -n %{repo}-%{version}

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITHOUT_UNINSTALL_APP=1
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/%{repo}
%{_bindir}/%{repo}-wapper
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/scalable/apps/%{sname}.svg
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/dsg/

%changelog
%autochangelog
