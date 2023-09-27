%global		gitdate 20230906.190341
%global		cmakever 5.240.0
%global		commit0 34bbef032a99336826a1341c69f988fe7ec11287
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework kquickcharts

Name:		kf6-%{framework}
Summary:	A QtQuick module providing high-performance charts
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}

License:	BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	make
BuildRequires:	pkgconfig(xkbcommon)

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{commit0} -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_qmldir}/org/kde/quickcharts/

%files devel
%{_kf6_libdir}/cmake/KF6QuickCharts/

%changelog
* Mon Sep 25 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230906.190341.34bbef0-1
- Initial release
