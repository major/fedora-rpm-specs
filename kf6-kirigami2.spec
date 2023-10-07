%global		gitdate 20230927.203844
%global		cmakever 5.240.0
%global		commit0 684c010ecb891c156ac16b74913eca8a8a00e022
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework kirigami

Name:		kf6-%{framework}2
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	2%{?dist}
Summary:	QtQuick plugins to build user interfaces based on the KDE UX guidelines
License:	BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-linguist
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtbase-private-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qtsvg-devel
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	qt6-qtbase-private-devel
BuildRequires:	pkgconfig(xkbcommon)

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1
# Some licenses are missing from the main LICENSES folder but are in the template folder, copying them over.
cp %{_builddir}/%{framework}-%{commit0}/templates/kirigami6/LICENSES/* %{_builddir}/%{framework}-%{commit0}/LICENSES/

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 libkirigami6_qt

%files -f libkirigami6_qt.lang
%doc README.md
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Kirigami2.so.5*
%{_kf6_libdir}/libKF6Kirigami2.so.6
%{_kf6_qmldir}/org/kde/kirigami
%{_datadir}/qlogging-categories6/kirigami.categories

%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_archdatadir}/mkspecs/modules/qt_Kirigami2.pri
%{_kf6_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_kf6_includedir}/Kirigami2/
%{_kf6_libdir}/cmake/KF6Kirigami2/
%{_kf6_libdir}/libKF6Kirigami2.so


%changelog
* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230927.203844.684c010-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230927.203844.684c010-1
- Initial Release
