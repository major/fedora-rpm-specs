Name:           google-benchmark
Version:        1.9.5
%global so_version 1
Release:        %autorelease

License:        Apache-2.0
Summary:        A microbenchmark support library
URL:            https://github.com/google/benchmark
Source:         %{url}/archive/v%{version}/benchmark-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
# Required for locale_impermeablity_test so the en_US.UTF-8 locale is valid.
BuildRequires:  glibc-langpack-en

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
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_VERSION='%{version}' \
    -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF \
    -DBENCHMARK_ENABLE_DOXYGEN:BOOL=OFF \
    -DBENCHMARK_ENABLE_GTEST_TESTS:BOOL=ON \
    -DBENCHMARK_ENABLE_ASSEMBLY_TESTS:BOOL=OFF \
    -DBENCHMARK_ENABLE_INSTALL:BOOL=ON \
    -DBENCHMARK_ENABLE_TESTING:BOOL=ON \
    -DBENCHMARK_INSTALL_DOCS:BOOL=OFF \
    -DBENCHMARK_INSTALL_TOOLS:BOOL=OFF \
    -DBENCHMARK_USE_BUNDLED_GTEST:BOOL=OFF


%build
%cmake_build


%check
%ctest


%install
%cmake_install


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
