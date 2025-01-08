Name:           blosc2
Version:        2.15.2
Release:        %autorelease
Summary:        High performance compressor optimized for binary data

License:        BSD-3-Clause
URL:            https://www.blosc.org/
Source:         https://github.com/Blosc/c-blosc2/archive/v%{version}/c-blosc2-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build
BuildRequires:  lz4-devel
BuildRequires:  zlib-devel
BuildRequires:  zlib-ng-devel
BuildRequires:  libzstd-devel
BuildRequires:  xxhash-devel

%description
Blosc is a high performance compressor optimized for binary data
(i.e. floating-point numbers, integers, and booleans, although it can handle
string data too). It has been designed to transmit data to the processor cache
faster than the traditional, non-compressed, direct memory fetch approach via a
memcpy() OS call. Blosc main goal is not just to reduce the size of large
datasets on-disk or in-memory, but also to accelerate memory-bound computations.

C-Blosc2 is the new major version of C-Blosc, and is backward compatible with
both the C-Blosc1 API and its in-memory format. However, the reverse thing is
generally not true for the format; buffers generated with C-Blosc2 are not
format-compatible with C-Blosc1.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n c-blosc2-%{version} -p1

# https://github.com/Blosc/c-blosc2/issues/489
rm plugins/codecs/ndlz/xxhash.?
sed -r -i '/xxhash.c/d' plugins/codecs/ndlz/CMakeLists.txt

# let's do this to make it clear that we're not using those
rm -r internal-complibs/* internal-complibs

%build
OPTIONS=(
        -GNinja
        -DBUILD_STATIC:BOOL=OFF
        -DBUILD_FUZZERS:BOOL=OFF
        -DPREFER_EXTERNAL_LZ4:BOOL=ON
        -DPREFER_EXTERNAL_ZLIB:BOOL=ON
        -DPREFER_EXTERNAL_ZSTD:BOOL=ON
        -DDEACTIVATE_AVX2:BOOL=ON

        # We need to pass the distro build flags here, otherwise they are ignored.
        # Silence warnings about stupid programming errors.
        -DCMAKE_C_FLAGS:STRING="$CFLAGS -Wno-unused-variable"
        )

%cmake "${OPTIONS[@]}"
%cmake_build

%install
%cmake_install

# Record the actual library SONAME in the build log
objdump -p %{buildroot}%{_libdir}/libblosc2.so.4 | grep SONAME

%check
# Tests fail on s390x: https://github.com/Blosc/c-blosc2/issues/467
%ifarch s390x
%global ignore_result || :
%endif

# Tests fail with -j12: https://github.com/Blosc/c-blosc2/issues/432
%ctest -j1 %{?ignore_result}

%files
# API versioning hard. With CMake even harder.
%{_libdir}/libblosc2.so.4
%{_libdir}/libblosc2.so.%{version}
%license LICENSE.txt
%doc ROADMAP.rst
%doc ANNOUNCE.*
%doc THANKS.*
%doc RELEASE_NOTES.*
%doc README*
%doc FAQ.*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/b2nd.h
%{_includedir}/blosc2.h
%{_includedir}/blosc2/*.h
%{_libdir}/libblosc2.so
%{_libdir}/pkgconfig/blosc2.pc
%{_libdir}/cmake/Blosc2

%changelog
%autochangelog
