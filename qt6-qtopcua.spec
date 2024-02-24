%global qt_module qtopcua

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

%global examples 1

Summary: Qt6 - OPC UA component
Name:    qt6-%{qt_module}
Version: 6.6.2
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

## upstreamable patches

BuildRequires: cmake
BuildRequires: gcc-c++	
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_6_PRIVATE_API)(64bit)
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: openssl-devel
BuildRequires: mbedtls-devel
#BuildRequires: open62541-devel

%description
Qt OPC UA (API) provides classes and functions to access the OPC UA protocol

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
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
%{_qt6_libdir}/libQt6OpcUa.so.*
%{_qt6_plugindir}/opcua/libopen62541_backend.so
%{_qt6_libdir}/libQt6DeclarativeOpcua.so.*
%{_qt6_qmldir}/QtOpcUa/*

%files devel
%{_qt6_headerdir}/QtOpcUa/
%{_qt6_headerdir}/QtDeclarativeOpcua/
%{_qt6_libdir}/libQt6OpcUa.so
%{_qt6_libdir}/libQt6OpcUa.prl
%{_qt6_libdir}/libQt6DeclarativeOpcua.so
%{_qt6_libdir}/libQt6DeclarativeOpcua.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtOpcUaTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6OpcUa/
%{_qt6_libdir}/cmake/Qt6OpcUa/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6DeclarativeOpcua/
%{_qt6_libdir}/cmake/Qt6DeclarativeOpcua/*.cmake
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Sat Feb 17 2024 Marie Loise Nolden <loise@kde.org> - 6.6.2-1
-  6.6.2

* Fri Dec 08 2023 Marie Loise Nolden <loise@kde.org> - 6.6.1-1
- 6.6.1

* Thu May 25 2023 Marie Loise Nolden <loise@kde.org> - 6.5.1-1
- 6.5.1

* Tue Apr 4 2023 Marie Loise Nolden <loise@kde.org> - 6.5.0-1
- 6.5.0

* Thu Dec 08 2022 Marie Loise Nolden <loise@kde.org> - 6.4.1-1
- 6.4.1

* Fri Aug 05 2022 Marie Loise Nolden <loise@kde.org> - 6.3.1-1
- 6.3.1
