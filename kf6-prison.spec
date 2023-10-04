%global		gitdate 20230925.220236
%global		cmakever 5.240.0
%global		commit0 d99e5a221b737edd6f923388e97f06d34b283577
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework prison 

Name:		kf6-%{framework}
Summary:	KDE Frameworks 6 Tier 1 barcode library
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
License:	BSD-3-Clause AND CC0-1.0 AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	cmake(ZXing)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(libqrencode)

Requires:	kf6-filesystem

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

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
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Prison.so.5*
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6PrisonScanner.so.5*
%{_kf6_libdir}/libKF6PrisonScanner.so.6
%{_kf6_qmldir}/org/kde/prison/

%files devel
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so
%{_kf6_libdir}/cmake/KF6Prison/
%{_kf6_archdatadir}/mkspecs/modules/qt_Prison.pri

%changelog
* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.220236.d99e5a2-1
- Initial release
