# The bench subpackage requires matplotlib.  Disable it on new EPEL releases
# until matplotlib is available.
%bcond bench %[%{undefined rhel} || 0%{?rhel} < 11]

Summary: High performance compressor optimized for binary data
Name: blosc
Version: 1.21.6
Release: %autorelease
License: BSD-3-Clause
Source: https://github.com/Blosc/c-blosc/archive/v%{version}/blosc-%{version}.tar.gz
Patch:  blosc-gcc11.patch
Patch:  blosc-gcc23.patch

URL:  https://github.com/Blosc/c-blosc
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: lz4-devel
BuildRequires: snappy-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel

%description
Blosc is a compression library designed to transmit data to the processor
cache faster than the traditional non-compressed memory fetch.
Compression ratios are not very high, but the decompression is very fast.
Blosc is meant not only to reduce the size of large datasets on-disk or
in-memory, but also to accelerate memory-bound computations.

%package devel
Summary: Header files and libraries for Blosc development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The blosc-devel package contains the header files and libraries needed
to develop programs that use the blosc meta-compressor.

%if %{with bench}
%package bench
Summary: Benchmark for the Blosc compressor
Requires: %{name} = %{version}-%{release}
# This isn't actually a build-time dependency, but we'll mark it as such to
# make sure the dependency is present in EPEL to avoid it later becoming a
# missing run-time dependency and having an uninstallable subpackage.
BuildRequires: python3-matplotlib
Requires: python3-matplotlib

%description bench
The blosc-bench package contains a benchmark suite which evaluates
the performance of Blosc, and compares it with memcpy.
%endif

%prep
%autosetup -n c-%{name}-%{version} -p1
rm -r internal-complibs/lz4* internal-complibs/zstd*

# Fix rpath issue
sed -i '1i  set\(CMAKE_SKIP_RPATH true\)' bench/CMakeLists.txt

# Fix cmake detection of pthreads
sed -i '1i  set\(CMAKE_POSITION_INDEPENDENT_CODE TRUE\)' CMakeLists.txt

# https://github.com/Blosc/c-blosc/issues/190
sed -i 's|lib/pkgconfig|%{_lib}/pkgconfig|' CMakeLists.txt

# Add python shebang and permission
sed -i '1i  #!/usr/bin/python3' bench/plot-speeds.py

%build
# Use the proper library path and SSE2 instruction on 64bits systems
%cmake \
    -DBUILD_STATIC:BOOL=OFF \
    -DPREFER_EXTERNAL_LZ4:BOOL=ON \
    -DTEST_INCLUDE_BENCH_SUITE:BOOL=OFF \
    -DDEACTIVATE_SNAPPY:BOOL=OFF \
    -DPREFER_EXTERNAL_ZLIB:BOOL=ON \
    -DPREFER_EXTERNAL_ZSTD:BOOL=ON

%cmake_build

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%install
%cmake_install

%if %{with bench}
install -p bench/plot-speeds.py* -Dt %{buildroot}/%{_pkgdocdir}/bench/
install -pm 0644 bench/*.c %{buildroot}/%{_pkgdocdir}/bench

install -p %{_vpath_builddir}/bench/bench -D %{buildroot}/%{_bindir}/%{name}-bench
install -p bench/plot-speeds.py %{buildroot}/%{_bindir}/%{name}-plot-times
%endif

%files
%exclude %{_pkgdocdir}/bench/
%license LICENSES/*
%doc README.md ANNOUNCE.rst RELEASE_NOTES.rst README*.rst
%{_libdir}/libblosc.so.1*

%files devel
%{_libdir}/libblosc.so
%{_libdir}/pkgconfig/blosc.pc
%{_includedir}/blosc.h
%{_includedir}/blosc-export.h

%if %{with bench}
%files bench
%{_pkgdocdir}/bench
%{_bindir}/%{name}-bench
%{_bindir}/%{name}-plot-times
%endif


%changelog
%autochangelog
