%global qt_module qtmqtt

%global examples 1

Name:           qt6-%{qt_module}
Version:        6.8.2
Release:        1%{?dist}
Summary:        Qt6 - Mqtt module

License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://github.com/qt/qtmqtt/
Source0:        https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}/%{qt_module}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_6_PRIVATE_API)(64bit)
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
%cmake_qt6 \
        -DQT_BUILD_EXAMPLES=%{?examples:ON}%{!?examples:OFF} \
        -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx
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
* Fri Jan 31 2025 Jan Grulich <jgrulich@redhat.com> - 6.8.2-1
- 6.8.2

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

* Thu Feb 22 2024 Dana Elfassy <delfassy@redhat.com> - 6.6.2-2
- Bump version

* Thu Feb 08 2024 Dana Elfassy <delfassy@redhat.com>
- QtMqtt initial release
