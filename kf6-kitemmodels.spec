%global		gitdate 20230914.113622
%global		cmakever 5.240.0
%global		commit0 4c5c66325d03f6ecfabf3ad6f474310f33193282
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework kitemmodels

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with item models

License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Qml)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with item models.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
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
%{_kf6_libdir}/libKF6ItemModels.so.*
%{_kf6_qmldir}/org/kde/kitemmodels/

%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/KItemModels/
%{_kf6_libdir}/libKF6ItemModels.so
%{_kf6_libdir}/cmake/KF6ItemModels/
%{_kf6_archdatadir}/mkspecs/modules/qt_KItemModels.pri


%changelog
* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230914.113622.4c5c663-1
- Initial Release
