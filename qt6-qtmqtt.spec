%global qt_module qtmqtt

Name:           qt6-%{qt_module}
Version:        6.6.2
Release:        2%{?dist}
Summary:        Qt6 - Mqtt module

License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://github.com/qt/qtmqtt/
Source0:        https://github.com/qt/qtmqtt/archive/refs/tags/v%{version}/%{qt_module}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
MQTT is a machine-to-machine (M2M) protocol utilizing the publish-and-subscribe
paradigm, and provides a channel with minimal communication overhead.
The Qt MQTT module provides a standard compliant implementation of the MQTT 
protocol specification. It enables applications to act as telemetry displays 
and devices to publish telemetry data.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}

%prep
%autosetup -n %{qt_module}-%{version}

%build
%cmake_qt6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Mqtt.so.6*

%files devel
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMqttTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Mqtt/*.cmake
%{_qt6_libdir}/libQt6Mqtt.prl
%{_qt6_libdir}/libQt6Mqtt.so
%{_qt6_libdir}/pkgconfig/Qt6Mqtt.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_headerdir}/QtMqtt/*
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%dir %{_qt6_libdir}/cmake/Qt6Mqtt/
%dir %{_qt6_headerdir}/QtMqtt

%files examples
%{_qt6_examplesdir}

%changelog
* Thu Feb 22 2024 Dana Elfassy <delfassy@redhat.com> - 6.6.2-2
- Bump version

* Thu Feb 08 2024 Dana Elfassy <delfassy@redhat.com>
- QtMqtt initial release
