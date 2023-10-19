%global		gitdate 20231003.213655
%global		cmakever 5.240.0
%global		commit0 0aa4d0723d61a1c811ad68de8356783f4c8ad4be
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework kwindowsystem

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module with classes for windows management
License:	CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtbase-private-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	fdupes

Requires:	kf6-filesystem

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

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
%find_lang_kf6 kwindowsystem6_qt
%fdupes %{buildroot}%{_kf6_includedir}

%files -f kwindowsystem6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6WindowSystem.so.*
%dir %{_kf6_plugindir}/kwindowsystem/
%{_kf6_plugindir}/kwindowsystem/KF6WindowSystemX11Plugin.so
%{_kf6_qmldir}/org/kde/kwindowsystem

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_libdir}/cmake/KF6WindowSystem/

%changelog
* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.213655.0aa4d07-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20231003.213655.0aa4d07-2
- Rebuild for Qt Private API

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.213655.0aa4d07-1
- Fix for build on s390x arch

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230905.004205.b59a819-1
- Initial Release
