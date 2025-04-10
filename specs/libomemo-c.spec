%global forgeurl https://github.com/dino/libomemo-c
Version:        0.5.1
%forgemeta

Name:           libomemo-c
Release:        %autorelease
Summary:        Fork of libsignal-protocol-c adding support for OMEMO XEP-0384 0.5.0+

# The library is under GPL-3.0-only license, except the CMakeModules/FindCheck.cmake file is BSD-3-Clause
License:        GPL-3.0-only AND BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  protobuf-c-devel
# testing dependencies
BuildRequires:  check-devel
BuildRequires:  openssl-devel

%description
This is a fork of libsignal-protocol-c, an implementation of Signal's ratcheting
forward secrecy protocol that works in synchronous and asynchronous messaging.
The fork adds support for OMEMO as defined in XEP-0384 versions 0.3.0 and later.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DBUILD_TESTING=ON \
    -DLIB_INSTALL_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libomemo-c.so.0*

%files devel
%dir %{_includedir}/omemo
%{_includedir}/omemo/*.h
%{_libdir}/libomemo-c.so
%{_libdir}/pkgconfig/libomemo-c.pc

%changelog
%autochangelog
