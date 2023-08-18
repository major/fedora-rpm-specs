%global repo dde-network-core
%global __provides_exclude_from ^%{_prefix}/lib/dde-.*\\.so$

Name:           deepin-network-core
Version:        1.0.63
Release:        %autorelease
Summary:        DDE network library and plugins

# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# don't ignore linker flags specified by system
Patch0:         https://github.com/linuxdeepin/dde-network-core/pull/54.patch
# soname versioning
Patch1:         add-soname.patch

BuildRequires:  gcc-c++
BuildRequires:  dtkwidget-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  kf5-networkmanager-qt-devel
BuildRequires:  cmake
BuildRequires:  deepin-control-center-devel
BuildRequires:  gtest-devel
BuildRequires:  qt5-linguist
BuildRequires:  deepin-dock-devel
BuildRequires:  deepin-session-shell-devel
BuildRequires:  pkgconfig(Qt5Svg)
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
# provides %%{_var}/lib/polkit-1/localauthority/10-vendor.d
Requires:       polkit-pkla-compat

%description
This package provides %{summary}.

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
%autosetup -p1 -n %{repo}-%{version}

%build
%cmake
%cmake_build


%install
%cmake_install


%files
%{_bindir}/dde-network-dialog
%{_prefix}/lib/dde-control-center/
%{_prefix}/lib/dde-dock/
%{_prefix}/lib/dde-session-shell/
%{_datadir}/dcc-network-plugin/
%{_datadir}/dde-network-dialog/
%{_datadir}/dock-network-plugin/
%{_datadir}/dss-network-plugin/
%{_datadir}/dsg/
%{_var}/lib/polkit-1/localauthority/10-vendor.d/*

%files lib
%{_libdir}/libdde-network-core.so.1*

%files devel
%{_includedir}/libddenetworkcore/
%{_libdir}/libdde-network-core.so
%{_libdir}/pkgconfig/%{repo}.pc

%changelog
%autochangelog
