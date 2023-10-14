%global gitdate 20231011.024143
%global cmakever 5.240.0
%global commit0 b56185bbd6739b1975b680e44198965ce2647553
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework ksvg

Name:    kf6-ksvg
Summary: Components for handling SVGs
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules >= %{cmakever}

BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Svg)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6ColorScheme)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{framework}-%{commit0}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_kf6_libdir}/libKF6Svg.so.*
%{_kf6_libdir}/qt6/qml/org/kde/ksvg
%{_kf6_datadir}/qlogging-categories6/ksvg.categories

%files devel
%{_kf6_includedir}/KSvg
%{_kf6_libdir}/cmake/KF6Svg
%{_kf6_libdir}/libKF6Svg.so

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024143.b56185b-1
- Initial release
