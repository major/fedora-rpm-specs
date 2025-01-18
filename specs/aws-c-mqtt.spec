%global _description %{expand:
C99 implementation of the MQTT 3.1.1 and MQTT 5 specifications}

Name:           aws-c-mqtt
Version:        0.11.0
Release:        2%{?dist}
Summary:        C99 implementation of the MQTT 3.1.1 and MQTT 5 specifications.

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-mqtt-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-io-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  aws-c-compression-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Dependencies like aws-c-common don't support and build on s390x
# Upstream issue: https://github.com/awslabs/aws-c-common/issues/1111
# Fedora bugzilla ticket to be created after package review
ExcludeArch: s390x

%description %{_description}


%package libs
Summary:        %{summary}

%description libs %{_description}


%package devel
Summary:        %{summary}
Requires:       openssl-devel
Requires:       aws-c-io-devel
Requires:       aws-c-http-devel
Requires:       aws-c-compression-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE NOTICE
%doc README.md
%{_bindir}/elastipubsub
%{_bindir}/elastipubsub5
%{_bindir}/mqtt5canary
%{_bindir}/elastishadow


%files libs
%{_libdir}/libaws-c-mqtt.so.1{,.*}


%files devel
%{_libdir}/libaws-c-mqtt.so
%dir %{_includedir}/aws/mqtt
%dir %{_includedir}/aws/mqtt/v5
%dir %{_includedir}/aws/mqtt/private
%{_includedir}/aws/mqtt/*.h
%{_includedir}/aws/mqtt/v5/*.h
%{_includedir}/aws/mqtt/private/mqtt_client_test_helper.h
%{_includedir}/aws/mqtt/request-response/request_response_client.h
%dir %{_libdir}/cmake/aws-c-mqtt
%dir %{_libdir}/cmake/aws-c-mqtt/shared
%{_libdir}/cmake/aws-c-mqtt/aws-c-mqtt-config.cmake
%{_libdir}/cmake/aws-c-mqtt/shared/aws-c-mqtt-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-mqtt/shared/aws-c-mqtt-targets.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Packit <hello@packit.dev> - 0.11.0-1
- Update to version 0.11.0
- Resolves: rhbz#2317409

* Thu Sep 26 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.10.6-1
- update to 0.10.6

* Mon Aug 12 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.10.4-1
- update to 0.10.4

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.7.8-3
- Prepare for package review

* Tue Jan 25 2022 Kyle Knapp <kyleknap@amazon.com> - 0.7.8-2
- Add patch to make missing API accessible when a shared library

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.7.8-1
- Initial package development
