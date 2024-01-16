Name:           paho-cpp
Version:        1.3.2
Release:        %autorelease
Summary:        Eclipse Paho MQTT C++ Client Library

License:        EPL-2.0
URL:            https://github.com/eclipse/paho.mqtt.cpp
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  graphviz
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  paho-c-devel

%description
Eclipse Paho MQTT C++ client library for memory-managed operating systems such
as Linux, MacOS, and Windows.

%package            devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description        devel
The %{name}-devel package contains development files for %{name}.

%package            doc
Summary:            Documentation for %{name}
BuildArch:          noarch

%description        doc
This %{name}-doc package contains documentation for %{name}.

%prep
%autosetup -p1 -n paho.mqtt.cpp-%{version}

sed -i 's|lib/cmake|%{_lib}/cmake|g' cmake/CMakeLists.txt

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPAHO_WITH_SSL=ON \
    -DPAHO_BUILD_SAMPLES=OFF \
    -DPAHO_BUILD_DOCUMENTATION=ON \

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/samples/
cp -a src/samples/*.cpp %{buildroot}%{_docdir}/%{name}/samples/
mv %{buildroot}%{_docdir}/html %{buildroot}%{_docdir}/%{name}/html

%files
%license edl-v10 epl-v20
%{_libdir}/libpaho-mqttpp3.so.1*

%files devel
%{_includedir}/mqtt/
%{_libdir}/libpaho-mqttpp3.so
%{_libdir}/cmake/PahoMqttCpp/

%files doc
%license edl-v10 epl-v20
%doc README.md
%{_docdir}/%{name}

%changelog
%autochangelog
