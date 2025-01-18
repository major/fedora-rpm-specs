Name:		intel-qpl
Version:	1.7.0
Release:	%autorelease
Summary:	Intel Query Processing Library

License:	MIT
URL:		https://github.com/intel/qpl
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		qpl-fedora.patch
Patch1:		qpl-werror.patch

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc-c++
BuildRequires:	gtest-devel
BuildRequires:	libuuid-devel
BuildRequires:	libtsan
BuildRequires:	nasm

ExclusiveArch:	x86_64

%description
The Intel Query Processing Library (Intel QPL) is an open-source library to 
provide high-performance query processing operations on Intel CPUs. Intel QPL
is aimed to support capabilities of the new Intel In-Memory Analytics 
Accelerator (Intel IAA) available on Next Generation Intel Xeon Scalable 
processors, codenamed Sapphire Rapids processor, such as very high throughput
compression and decompression combined with primitive analytic functions, as 
well as to provide highly-optimized SW fallback on other Intel CPUs.
Intel QPL primarily targets applications such as big-data and in-memory 
analytic databases.
	
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	accel-config-libs

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -p1 -n qpl-%{version}
# Continue to use Gtest 1.14.0 instead of 1.15.2
sed -i -e 's|GTEST_INTERNAL_ATTRIBUTE_MAYBE_UNUSED|GTEST_ATTRIBUTE_UNUSED_|g' tools/tests/common/test_cases.hpp

%build
%cmake \
		-DCMAKE_BUILD_TYPE=RelWithDebInfo \
		-DDYNAMIC_LOADING_LIBACCEL_CONFIG=ON \
		-DQPL_LIBRARY_TYPE=SHARED \
		-DSANITIZE_THREADS=ON \
		-DQPL_BUILD_TESTS=ON \
		-DQPL_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%check
%__cmake_builddir/tools/tests/functional/tests --dataset=tools/testdata/ --gtest_filter=ta_unit*

%files
%license LICENSE
%doc README.md
%{_libdir}/libqpl.so.1
%{_libdir}/libqpl.so.%{version}

%files devel
%{_includedir}/qpl
%{_datadir}/QPL
%{_libdir}/libqpl.so
%{_libdir}/cmake/QPL
%{_libdir}/pkgconfig/qpl.pc

%changelog
%autochangelog
