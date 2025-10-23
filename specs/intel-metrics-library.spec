%global upstream_name metrics-library

Name: intel-metrics-library
Version: 1.0.200
Release: %autorelease
Summary: Shared library for Intel Metrics Library for Metrics Discovery API
License: MIT
ExclusiveArch: x86_64
URL: https://github.com/intel/metrics-library
Source0: %{url}/archive/%{upstream_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: libdrm-devel

%description
Intel Metrics Library for Metrics Discovery API is a user-mode driver helper
library that provides access to GPU performance counters.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name} = %{version}-%{release}

%description     devel
Intel Metrics Library for Metrics Discovery API is a user-mode driver helper
library that provides access to GPU performance counters.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{upstream_name}-%{upstream_name}-%{version}

%build
%cmake \
   -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%files
%config(noreplace)
%{_libdir}/libigdml.so.%{version}
%{_libdir}/libigdml.so.1
%license LICENSE.md
%doc README.md

%files devel
%config(noreplace)
%{_libdir}/libigdml.so
%{_libdir}/libigdml64.so
%{_includedir}/metrics_library_api_1_0.h
%{_libdir}/pkgconfig/libigdml.pc

%changelog
%autochangelog
