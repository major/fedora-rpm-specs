%bcond libpfm   1

Name:           google-benchmark
Version:        1.9.5
%global so_version 1
Release:        %autorelease

License:        Apache-2.0
Summary:        A microbenchmark support library
URL:            https://github.com/google/benchmark
Source:         %{url}/archive/v%{version}/benchmark-%{version}.tar.gz

# In PerfCountersTest.MultiThreaded, serialize worker threads
# https://github.com/google/benchmark/pull/2175
#
# Fixes:
#
# [BUG] Flaky failure of PerfCountersTest.MultiThreaded
# https://github.com/google/benchmark/issues/2173
Patch:          0001-In-PerfCountersTest.MultiThreaded-serialize-worker-t.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
# Required for locale_impermeablity_test so the en_US.UTF-8 locale is valid.
BuildRequires:  glibc-langpack-en
%if %{with libpfm}
BuildRequires:  libpfm-devel
%endif

%description
A library to support the benchmarking of functions, similar to unit-tests.


%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# Removed for Fedora 43; we can drop the Obsoletes after Fedora 45.
Obsoletes:      %{name}-doc < 1.9.4-9

%description devel
%{summary}.


%prep
%autosetup -n benchmark-%{version} -p1
sed -e '/get_git_version/d' -e '/-Werror/d' -i CMakeLists.txt


%conf
# Do not enable BENCHMARK_ENABLE_ASSEMBLY_TESTS, since it is for a very
# specific OS and compiler:
# https://github.com/google/benchmark/issues/1326#issuecomment-1015221235
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_VERSION='%{version}' \
    -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF \
    -DBENCHMARK_ENABLE_DOXYGEN:BOOL=OFF \
    -DBENCHMARK_ENABLE_GTEST_TESTS:BOOL=ON \
    -DBENCHMARK_ENABLE_ASSEMBLY_TESTS:BOOL=OFF \
%if %{with libpfm}
    -DBENCHMARK_ENABLE_LIBPFM:BOOL=ON \
%endif
    -DBENCHMARK_ENABLE_INSTALL:BOOL=ON \
    -DBENCHMARK_ENABLE_TESTING:BOOL=ON \
    -DBENCHMARK_INSTALL_DOCS:BOOL=OFF \
    -DBENCHMARK_INSTALL_TOOLS:BOOL=OFF \
    -DBENCHMARK_USE_BUNDLED_GTEST:BOOL=OFF


%build
%cmake_build


%install
%cmake_install


%check
%ifarch s390x
# [BUG] Multiple PerfCountersTest failures with counter.num_counters() zero on
# some s390x systems
# https://github.com/google/benchmark/issues/2174
#
# Five of the nine tests in perf_counters_gtest fail with:
#
#   Expected equality of these values:
#     counter.num_counters()
#       Which is: 0
#     1
#
# Tests in perf_counters_test also fail for similar reasons:
#
#   […]/test/output_test.h:146: GetAs: Check `sv != nullptr && !sv->empty()'
#   failed.
#
# It’s likely that these are a “correct failures,” in that the library is
# compiled with libpfm support (so performance counters are supported in
# general) but even basic performance counters are not necessarily supported on
# more recent s390x hardware versions (i.e., probably z14 and later).
#
# We don’t bother attempting to run the four tests that do succeed in
# perf_counters_gtest; it’s much more straightforward to just skip these two
# executables at the ctest level entirely, and little is lost by doing so.
%ctest --exclude-regex '^perf_counters_g?test$'
%else
%ctest
%endif


%files
%license AUTHORS
%license CONTRIBUTORS
%license LICENSE

%doc README.md

%{_libdir}/libbenchmark*.so.%{so_version}{,.*}


%files devel
%{_libdir}/libbenchmark*.so
%{_includedir}/benchmark/
%{_libdir}/cmake/benchmark/
%{_libdir}/pkgconfig/benchmark*.pc


%changelog
%autochangelog
