Name:           paho-c
Version:        1.3.14
Release:        %autorelease
Summary:        MQTT C Client
License:        BSD-3-Clause AND EPL-2.0
URL:            https://eclipse.org/paho/clients/c/
Source0:        https://github.com/eclipse/paho.mqtt.c/archive/v%{version}/paho.mqtt.c-%{version}.tar.gz
Source1:        unused.abignore

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  graphviz
BuildRequires:  doxygen
BuildRequires:  openssl-devel

%description
The Paho MQTT C Client is a fully fledged MQTT client written in C.

%package        devel
Summary:        MQTT C Client development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files and samples for the the Paho MQTT C Client.

%package        doc
Summary:        MQTT C Client development kit documentation
BuildArch:      noarch

%description    doc
Development documentation files for the the Paho MQTT C Client.

%prep
%autosetup -n paho.mqtt.c-%{version}

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DPAHO_WITH_SSL=ON \
    -DPAHO_BUILD_DOCUMENTATION=ON \
    -DPAHO_BUILD_SAMPLES=ON \
    -DPAHO_ENABLE_CPACK=OFF \
%cmake_build

%install
%cmake_install
install -pDm755 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/abi/paho-c.abignore

# Move the man pages to the correct directory
mkdir -p %{buildroot}%{_mandir}/man3
mv -fv %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTAsync/man/man3/* %{buildroot}%{_mandir}/man3/
mv -fv %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTClient/man/man3/* %{buildroot}%{_mandir}/man3/
rm -rvf %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTAsync/man %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTClient/man

%files
%license LICENSE edl-v10 epl-v20
%{_bindir}/paho*
%{_libdir}/libpaho-mqtt*.so.1*
%{_datadir}/%{name}/abi/paho-c.abignore

%files devel
%{_bindir}/MQTT*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/eclipse-paho-mqtt-c/
%{_mandir}/man3/*

%files doc
%license LICENSE edl-v10 epl-v20
%{_defaultdocdir}/*

%changelog
%autochangelog
