%bcond ctest 1
# Build with libpfm for hardware performance counter support?
%bcond libpfm 1

Name:           google-benchmark
Version:        1.10.0
%global so_version 1
Release:        %autorelease

License:        Apache-2.0
Summary:        A microbenchmark support library
URL:            https://github.com/google/benchmark
Source:         %{url}/archive/v%{version}/benchmark-%{version}.tar.gz

# Use the full version as the SOVERSION
# https://github.com/google/benchmark/pull/2342
#
# A candidate fix for:
#
# [BUG] ABI break in 1.10.0 without SONAME version bump
# https://github.com/google/benchmark/issues/2340
Patch:          %{url}/pull/2342.patch

BuildSystem:    cmake

BuildOption(conf): -DCMAKE_BUILD_TYPE=Release
BuildOption(conf): -DGIT_VERSION='%{version}'
BuildOption(conf): -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF
# Do not enable BENCHMARK_ENABLE_ASSEMBLY_TESTS, since it is for a very
# specific OS and compiler:
# https://github.com/google/benchmark/issues/1326#issuecomment-1015221235
BuildOption(conf): -DBENCHMARK_ENABLE_ASSEMBLY_TESTS:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_DOXYGEN:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_INSTALL:BOOL=ON
BuildOption(conf): -DBENCHMARK_INSTALL_DOCS:BOOL=OFF
BuildOption(conf): -DBENCHMARK_INSTALL_TOOLS:BOOL=OFF
BuildOption(conf): -DBENCHMARK_USE_BUNDLED_GTEST:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_LIBPFM:BOOL=%{with libfpm}
BuildOption(conf): -DBENCHMARK_ENABLE_GTEST_TESTS:BOOL=%{with ctest}
BuildOption(conf): -DBENCHMARK_ENABLE_TESTING:BOOL=%{with ctest}

BuildRequires:  gcc
BuildRequires:  gcc-c++

%if %{with libpfm}
BuildRequires:  libpfm-devel
%endif

%if %{with ctest}
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
# Required for locale_impermeablity_test so the en_US.UTF-8 locale is valid.
BuildRequires:  glibc-langpack-en
%endif

%description
A library to support the benchmarking of functions, similar to unit-tests.


%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with libpfm}
Requires:       libpfm-devel%{?_isa}
%endif
# Removed for Fedora 43; we can drop the Obsoletes after Fedora 45.
Obsoletes:      %{name}-doc < 1.9.4-9

%description devel
%{summary}.


%prep -a
sed --in-place \
    --expression='/get_git_version/d' \
    --expression='/-Werror/d' \
    CMakeLists.txt


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
