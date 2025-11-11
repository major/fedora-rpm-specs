%global forgeurl https://github.com/actor-framework/actor-framework
Version:        1.1.0
%global tag %{version}
%forgemeta

Name:           actor-framework
Release:        %autorelease
Summary:        An Open Source Implementation of the Actor Model in C++

# https://github.com/actor-framework/actor-framework/issues/1410#issuecomment-1547459576
License:        BSD-3-Clause
URL:            https://github.com/actor-framework/actor-framework
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  doxygen
# optional dependencies for building examples
BuildRequires:  libcurl-devel
BuildRequires:  protobuf-devel
BuildRequires:  qt6-qtbase-devel

%description
CAF (the C++ Actor Framework) is an open source implementation of the actor
model for C++ featuring lightweight & fast actor implementations, pattern
matching for messages, network transparent messaging, and more.

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for %{name}.

%package        examples
Summary:        Example files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
This package contains example files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCAF_ENABLE_CURL_EXAMPLES=ON \
    -DCAF_ENABLE_PROTOBUF_EXAMPLES=ON \
    -DCAF_ENABLE_QT6_EXAMPLES=ON \
    -DCAF_ENABLE_RUNTIME_CHECKS=ON \
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libcaf_*.so.1*

%files devel
%{_includedir}/caf/
%{_libdir}/libcaf_*.so
%{_libdir}/cmake/CAF/

%files examples
%dir %{_datadir}/caf
%{_datadir}/caf/examples/

%changelog
%autochangelog
