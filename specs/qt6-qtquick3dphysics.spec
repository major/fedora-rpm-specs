%global qt_module qtquick3dphysics

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif
	
%global examples 1

Summary: Qt6 - Quick3D Physics Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.8.1
Release: 3%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io

%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

ExclusiveArch: aarch64 i686 x86_64

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
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.1-2
- Move Software Bill of Materials from -devel

* Thu Nov 28 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.1-1
- 6.8.1

* Fri Oct 11 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.0-1
- 6.8.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.2-1
- 6.7.2

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.1-1
- 6.7.1

* Tue Apr 02 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.0-1
- 6.7.0

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
