%global		gitdate 20230922.150947
%global		cmakever 5.240.0
%global		commit0 770e361d9b6521191e4464944e49b41b21ccdf2e
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		date 20230922
%global		framework kwayland

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 library that wraps Client and Server Wayland libraries

License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT-CMU AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	appstream
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtbase-static
BuildRequires:	qt6-qtbase-private-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel

BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Qt6WaylandClient)

Requires:	kf6-filesystem

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{commit0}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6WaylandClient.so.5*
%{_kf6_libdir}/libKF6WaylandClient.so.6

%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/KWayland/
%{_kf6_libdir}/cmake/KF6Wayland/
%{_kf6_libdir}/libKF6WaylandClient.so
%{_kf6_libdir}/pkgconfig/KF6WaylandClient.pc
%{_kf6_archdatadir}/mkspecs/modules/qt_KWaylandClient.pri

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230922.150947.770e361-1
- Initial release
