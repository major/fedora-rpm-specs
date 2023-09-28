%global		gitdate 20230916.160754
%global 	cmakever 5.240.0
%global 	commit0 7ff692a014cc1c5d8b415c05a17a62a5741c3276
%global 	shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global 	framework kguiaddons

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtGui

License:	BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel

BuildRequires:  kf6-rpm-macros
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtwayland-devel

BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
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
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6GuiAddons.so.*
%{_kf6_datadir}/applications/*-handler.desktop

%files devel
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_libdir}/cmake/KF6GuiAddons/
%{_kf6_archdatadir}/mkspecs/modules/qt_KGuiAddons.pri


%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230916.160754.7ff692a-1
- Initial release
