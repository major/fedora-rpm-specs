%global		gitdate 20230829.232751
%global		cmakever 5.240.0
%global		commit0 29055998c8ea3538113cbacf2f0d4e6d101e1225
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework kcalendarcore

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 KCalendarCore Library
License:	BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	bison
BuildRequires:	libical-devel
BuildRequires:	qt6-qtbase-devel
BuildRequires:	pkgconfig(xkbcommon)

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = :%{version}-%{release}
Requires:	libical-devel
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
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*kcalendarcore.*
%{_kf6_libdir}/libKF6CalendarCore.so.*

%files devel
%{_kf6_includedir}/KCalendarCore/
%{_kf6_libdir}/libKF6CalendarCore.so
%{_kf6_libdir}/cmake/KF6CalendarCore/
%{_kf6_libdir}/pkgconfig/KF6CalendarCore.pc
%{_kf6_archdatadir}/mkspecs/modules/qt_KCalendarCore.pri

%changelog
* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232751.2905599-1
- Initial release
