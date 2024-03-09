%global qt_module qtquick3dphysics

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif
	
%global examples 1

Summary: Qt6 - Quick3D Physics Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.6.2
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io

%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_6_PRIVATE_API)(64bit)
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtshadertools-devel
BuildRequires: qt6-qtquick3d-devel

%description
The Qt 6 Quick3D Physics library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
Requires: qt6-qtquick3d-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif


%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

%build

%cmake_qt6 \
  -DQT_BUILD_EXAMPLES=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Quick3DPhysics.so.*
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.so.*
%{_qt6_qmldir}//QtQuick3D/

%files devel
%{_qt6_bindir}/cooker

%dir %{_qt6_headerdir}/QtQuick3DPhysics
%{_qt6_headerdir}/QtQuick3DPhysics/*
%dir %{_qt6_headerdir}/QtQuick3DPhysicsHelpers
%{_qt6_headerdir}/QtQuick3DPhysicsHelpers/*
%{_qt6_libdir}/libQt6BundledPhysX.a
%{_qt6_libdir}/libQt6Quick3DPhysics.so
%{_qt6_libdir}/libQt6Quick3DPhysics.prl
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.so
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.prl
%{_qt6_libdir}/cmake/Qt6/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtQuick3DPhysicsTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6BundledPhysX
%{_qt6_libdir}/cmake/Qt6BundledPhysX/*
%{_qt6_libdir}/cmake/Qt6Qml/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DPhysics
%{_qt6_libdir}/cmake/Qt6Quick3DPhysics/*
%dir %{_qt6_libdir}/cmake/Qt6Quick3DPhysicsHelpers
%{_qt6_libdir}/cmake/Qt6Quick3DPhysicsHelpers/*
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc


%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Fri Feb 23 2024 Marie Loise Nolden <loise@kde.org> - 6.6.2-1
- 6.6.2

* Fri Dec 08 2023 Marie Loise Nolden <loise@kde.org> - 6.6.1-1
- 6.6.1

* Thu May 25 2023 Marie Loise Nolden <loise@kde.org> - 6.5.1-1
- 6.5.1

* Tue Apr 4 2023 Marie Loise Nolden <loise@kde.org> - 6.5.0-1
- 6.5.0

* Tue Feb 21 2023 Marie Loise Nolden <loise@kde.org> - 6.4.2-1
- 6.4.2
