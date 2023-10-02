%global		gitdate 20230829.232959
%global		cmakever 5.240.0
%global		commit0 124d7db2dfefe70b4fa90fc1a9b255ec1a166ee0
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework kdnssd

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module for DNS-SD services (Zeroconf)
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	avahi-devel
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	nss-mdns
Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 integration module for DNS-SD services (Zeroconf)

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
%find_lang_kf6 kdnssd6_qt

%files -f kdnssd6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6DNSSD.so.*

%files devel
%{_kf6_includedir}/KDNSSD/
%{_kf6_libdir}/libKF6DNSSD.so
%{_kf6_libdir}/cmake/KF6DNSSD/
%{_kf6_archdatadir}/mkspecs/modules/qt_KDNSSD.pri


%changelog
* Mon Sep 25 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232959.124d7db-1
- Initial Release
