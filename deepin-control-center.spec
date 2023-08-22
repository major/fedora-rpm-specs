%global repo dde-control-center

%if 0%{?fedora}
%global dde_prefix deepin
Name:           deepin-control-center
%else
%global dde_prefix dde
Name:           %{repo}
%endif
Version:        5.5.158
Release:        %autorelease
Summary:        New control center for Linux Deepin
# migrated to SPDX
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

Patch0:         https://raw.githubusercontent.com/archlinux/svntogit-community/60ac39ad6f703cb47cbbb24cc4c882609bad25b7/trunk/deepin-control-center-systeminfo-deepin-icon.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  %{dde_prefix}-dock-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkgui-devel
BuildRequires:  dtkcore-devel
BuildRequires:  %{dde_prefix}-qt-dbus-factory-devel
BuildRequires:  deepin-pw-check-devel
#BuildRequires:  deepin-pw-check-devel >= 5.1.16
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(geoip)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  libpwquality-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(KF5WaylandClient)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  qt5-qtbase-private-devel
# for libQt5XkbCommonSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xext)
BuildRequires:  kf5-networkmanager-qt-devel
BuildRequires:  udisks2-qt5-devel
BuildRequires:  gtest-devel
BuildRequires:  qt5-linguist
BuildRequires:  cmake
BuildRequires:  make
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
Requires:       %{dde_prefix}-account-faces
Requires:       %{dde_prefix}-api
Requires:       %{dde_prefix}-daemon
Requires:       %{dde_prefix}-qt5integration
Requires:       startdde
Requires:       %{dde_prefix}-network-core

%description
New control center for Linux Deepin.

%package lib
Summary:        Shared library for %{name}

%description lib
This package provides shared library %{name}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
# sync with Arch
rm src/frame/window/icons/icons/dcc_nav_systeminfo_{42,84}px.svg

%patch -P 0 -p1

# needed for properly installing the main library
sed -i '/TARGETS/s|lib|%{_lib}|' src/frame/CMakeLists.txt

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DDISABLE_ACTIVATOR=YES \
       -DDISABLE_AUTHENTICATION=YES \
       -DDISABLE_DEVELOPER_MODE=YES \
       -DDISABLE_RECOVERY=YES \
       -DDISABLE_SYS_UPDATE=YES \
       -DDCC_DISABLE_GRUB=YES \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir}  # needed for properly installing cmake file
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop

%files
%doc README.md
%{_bindir}/%{repo}-wapper
%{_bindir}/%{repo}
%{_prefix}/lib/dde-grand-search-daemon/
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/polkit-1/actions/com.deepin.*.policy
%{_datadir}/%{repo}/
%{_datadir}/dict/MainEnglishDictionary_ProbWL.txt
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/dsg/

%files lib
%license LICENSE
%{_libdir}/libdccwidgets.so

%files devel
%{_includedir}/%{repo}
%{_libdir}/cmake/DdeControlCenter/
%{_datadir}/dman/

%changelog
%autochangelog
