%global commit bd13aee2455c1d137bee45f7d2aedea8dd30115c
%global snapdate 20220717
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           freeopcua
Version:        0
Release:        %autorelease -s %{snapdate}.%{shortcommit}
Summary:        Open Source C++ OPC-UA Server and Client Library

License:        LGPL-3.0-or-later
URL:            http://freeopcua.github.io/
Source0:        https://github.com/FreeOpcUa/freeopcua/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Do not override build flags, we want to use the Fedora flags
Patch0:         freeopcua.build-flags.patch
# https://github.com/FreeOpcUa/freeopcua/pull/354
Patch1:         freeopcua.catch-exception-in-destructor.patch
# Upstream has not reacted to a request to add a SOVERSION:
# https://github.com/FreeOpcUa/freeopcua/issues/337
# This patch sets the SOVERSION to 0.1.
Patch2:         freeopcua.set-soversion.patch
# FMT-9 formatter change
Patch3:         freeopcua-fmt9-formatter.patch
# FMT-10 fmt::format change
Patch4:         freeopcua-fmt10-fmt-format.patch
# https://github.com/FreeOpcUa/freeopcua/pull/398
Patch5:         freeopcua-gcc14-headers.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
BuildRequires:  spdlog-devel

%description
A LGPL C++ library to develop server and client OPC-UA applications.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
# The dependencies are not picked up automatically
Requires:   mbedtls-devel
Requires:   spdlog-devel

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Remove bundled spdlog
rm -rf include/opc/spdlog


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{?_lib}
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc README.md
%{_libdir}/libopc*.so.0.1


%files devel
%{_includedir}/opc
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*
%{_libdir}/libopc*.so



%changelog
%autochangelog
