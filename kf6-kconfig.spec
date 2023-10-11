%global		gitdate 20230925.220329
%global		cmakever 5.240.0
%global		commit0 8ff33136df67fddc9dd5bd979acf81592bfe4f98
%global		framework kconfig

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{commit0}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with advanced configuration system
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{commit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	pkgconfig(xkbcommon)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with advanced configuration system made of two
parts: KConfigCore and KConfigGui.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig(Qt6Xml)
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6 \
  %if 0%{?flatpak}
  %{?docs:-DBUILD_QCH:BOOL=OFF} \
  %else
  %{?docs:-DBUILD_QCH:BOOL=ON} \
  %endif
%cmake_build

%install
%cmake_install
%find_lang_kf6 kconfig6_qt

%files -f kconfig6_qt.lang
%doc DESIGN README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/kreadconfig6
%{_kf6_bindir}/kwriteconfig6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6ConfigCore.so.6*
%{_kf6_libdir}/libKF6ConfigCore.so.5*
%{_kf6_libdir}/libKF6ConfigQml.so.6*
%{_kf6_libdir}/libKF6ConfigQml.so.5*
%{_kf6_libdir}/libKF6ConfigGui.so.6*
%{_kf6_libdir}/libKF6ConfigGui.so.5*
%{_kf6_libexecdir}/kconf_update
%{_kf6_libexecdir}/kconfig_compiler_kf6
%{_kf6_libdir}/qt6/qml/org/kde/config/libkconfigqmlplugin.so
%{_kf6_libdir}/qt6/qml/org/kde/config/qmldir
%{_kf6_libdir}/qt6/qml/org/kde/config/kconfigqmlplugin.qmltypes
%{_kf6_libdir}/qt6/qml/org/kde/config/kde-qmlmodule.version

%files devel
%{_kf6_archdatadir}/mkspecs/modules/qt_KConfigCore.pri
%{_kf6_archdatadir}/mkspecs/modules/qt_KConfigGui.pri
%{_kf6_includedir}/KConfig/
%{_kf6_includedir}/KConfigCore/
%{_kf6_includedir}/KConfigGui/
%{_kf6_includedir}/KConfigQml/
%{_kf6_libdir}/cmake/KF6Config/
%{_kf6_libdir}/libKF6ConfigCore.so
%{_kf6_libdir}/libKF6ConfigGui.so
%{_kf6_libdir}/libKF6ConfigQml.so

%changelog
* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.220329.8ff33136df67fddc9dd5bd979acf81592bfe4f98-1
- Initial Package
