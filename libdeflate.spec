Name:          libdeflate
Version:       1.20
Release:       %autorelease
Summary:       Fast implementation of DEFLATE, gzip, and zlib

# SPDX
License:       MIT
URL:           https://github.com/ebiggers/libdeflate
Source:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake

# For tests
BuildRequires: zlib-devel

%description
libdeflate is a library for fast, whole-buffer DEFLATE-based compression and
decompression, supporting DEFLATE, gzip, and zlib.

%package devel
Summary:       Development files for libdeflate
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libdeflate.

%package utils
Summary:       Binaries from libdeflate
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description utils
Binaries from libdeflate.

%prep
%autosetup

%build
%cmake \
    -DLIBDEFLATE_BUILD_STATIC_LIB:BOOL=OFF \
    -DLIBDEFLATE_BUILD_SHARED_LIB:BOOL=ON \
    -DLIBDEFLATE_COMPRESSION_SUPPORT:BOOL=ON \
    -DLIBDEFLATE_DECOMPRESSION_SUPPORT:BOOL=ON \
    -DLIBDEFLATE_ZLIB_SUPPORT:BOOL=ON \
    -DLIBDEFLATE_GZIP_SUPPORT:BOOL=ON \
    -DLIBDEFLATE_FREESTANDING:BOOL=OFF \
    -DLIBDEFLATE_BUILD_GZIP:BOOL=ON \
    -DLIBDEFLATE_BUILD_TESTS:BOOL=ON \
    -DLIBDEFLATE_USE_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%doc NEWS.md README.md
%license COPYING
%{_libdir}/libdeflate.so.0

%check
%ctest

%files devel
%{_includedir}/libdeflate.h
%{_libdir}/libdeflate.so
%{_libdir}/pkgconfig/libdeflate.pc
%{_libdir}/cmake/libdeflate/

%files utils
%{_bindir}/libdeflate-gzip
%{_bindir}/libdeflate-gunzip

%changelog
%autochangelog
