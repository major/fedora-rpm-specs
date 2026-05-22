Name:		intel-qpl
Version:	1.9.0
Release:	%autorelease
Summary:	Intel Query Processing Library

License:	MIT
URL:		https://github.com/intel/qpl
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		qpl-accel.patch
Patch1:		qpl-werror.patch
Patch2:		qpl-tests.patch
Patch3:		qpl-intel-cet.patch

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

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	accel-config-libs

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package	tests
Summary:	Test applications that use %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	gtest

%description tests
The %{name}-tests package contains test datasets, functional
and cross-test applications that use and test %{name}.

%prep
%autosetup -p1 -n qpl-%{version}
# Continue to use gtest 1.14.0 instead of 1.15.2
sed -i -e 's|GTEST_INTERNAL_ATTRIBUTE_MAYBE_UNUSED|GTEST_ATTRIBUTE_UNUSED_|g' tools/tests/common/test_cases.hpp

%build
%cmake \
		-DCMAKE_BUILD_TYPE=RelWithDebInfo \
		-DDYNAMIC_LOADING_LIBACCEL_CONFIG=ON \
		-DQPL_LIBRARY_TYPE=SHARED \
		-DQPL_BUILD_TESTS=ON \
		-DQPL_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%check
# Change to "--gtest_filter=ta_unit*" for a longer and more comprehensive unit test (software path)
%__cmake_builddir/tools/tests/functional/qpl-func-tests --dataset=tools/testdata/ --gtest_filter=ta_c_api_async_multiple_jobs_submit.*:ta_c_api_integrity_control.*:ta_c_api_crc64.*

%files
%license LICENSE
%doc README.md
%{_libdir}/libqpl.so.1
%{_libdir}/libqpl.so.%{version}

%files devel
%{_includedir}/qpl
%{_datadir}/intel-qpl/configs
%{_datadir}/intel-qpl/scripts
%{_libdir}/libqpl.so
%{_libdir}/cmake/QPL
%{_libdir}/pkgconfig/qpl.pc

%files tests
%doc doc/source/documentation/get_started_docs/testing.rst
%{_datadir}/intel-qpl/testdata
%{_bindir}/qpl-func-tests
%{_bindir}/qpl-cross-tests

%changelog
%autochangelog
