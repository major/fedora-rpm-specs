%global repo dde-control-center

%if 0%{?fedora}
%global dde_prefix deepin
Name:           deepin-control-center
%else
%global dde_prefix dde
Name:           %{repo}
%endif
Version:        5.5.77
Release:        %autorelease
Summary:        New control center for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

Patch0:      https://raw.githubusercontent.com/archlinux/svntogit-community/60ac39ad6f703cb47cbbb24cc4c882609bad25b7/trunk/deepin-control-center-systeminfo-deepin-icon.patch

Patch1:      https://patch-diff.githubusercontent.com/raw/linuxdeepin/dde-control-center/pull/407.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  %{dde_prefix}-dock-devel
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkgui-devel
BuildRequires:  dtkcore-devel
BuildRequires:  %{dde_prefix}-qt-dbus-factory-devel
BuildRequires:  deepin-pw-check-devel
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
Requires:       %{dde_prefix}-account-faces
Requires:       %{dde_prefix}-api
Requires:       %{dde_prefix}-daemon
Requires:       %{dde_prefix}-qt5integration
Requires:       %{dde_prefix}-network-utils
Requires:       startdde

%description
New control center for Linux Deepin.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
# sync with Arch
rm src/frame/window/icons/icons/dcc_nav_systeminfo_{42,84}px.svg

%patch0 -p1
%patch1 -p1

sed -i -E '/add_compile_definitions/d; 's:lib/:%{_lib}/: CMakeLists.txt

sed -i '/%{repo}/ s|/usr/lib|%{_libdir}|' src/frame/modules/update/updatework.cpp \
                                          src/frame/window/mainwindow.cpp \
                                          com.deepin.controlcenter.develop.policy \
                                          README.md

sed -i '/TARGETS/s|lib|%{_lib}|' src/frame/CMakeLists.txt

# sync with Arch
# remove after they obey -DDISABLE_SYS_UPDATE properly
sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DDCC_DISABLE_GRUB=YES \
       -DDISABLE_SYS_UPDATE=YES -DDISABLE_RECOVERY=YES \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install
# place holder plugins dir
mkdir -p %{buildroot}%{_libdir}/%{repo}/plugins

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{repo}-wapper
%{_bindir}/%{repo}
%{_libdir}/%{repo}
%{_libdir}/libdccwidgets.so
%{_libdir}/dde-grand-search-daemon/
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/polkit-1/actions/com.deepin.*.policy
%{_datadir}/%{repo}/
%{_datadir}/dict/MainEnglishDictionary_ProbWL.txt
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/dsg/

%files devel
%{_includedir}/%{repo}
%{_libdir}/cmake/DdeControlCenter/

%changelog
%autochangelog
