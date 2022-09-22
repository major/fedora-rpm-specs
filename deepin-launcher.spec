%global repo dde-launcher
%global sname deepin-launcher

Name:           %{sname}
Version:        5.5.19.1
Release:        %autorelease
Summary:        Deepin desktop-environment - Launcher module
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-launcher
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

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
%if 0%{?fedora}
Requires:       deepin-daemon
%else
Requires:       dde-daemon
%endif
Requires:       startdde
Requires:       hicolor-icon-theme
Requires:       %{_bindir}/dbus-send

%description
%{summary}.

%prep
%autosetup -p1 -n %{repo}-%{version}

%build
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
%if 0%{?fedora}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITHOUT_UNINSTALL_APP=1
%cmake_build
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITHOUT_UNINSTALL_APP=1 .
%make_build
%endif

%install
%if 0%{?fedora}
%cmake_install
%else
%make_install INSTALL_ROOT=%{buildroot}
%endif

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
