%global intname benchmark
%global lbname lib%{intname}

Name: google-benchmark
Version: 1.9.2
Release: %autorelease

License: Apache-2.0
Summary: A microbenchmark support library
URL: https://github.com/google/%{intname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gmock-devel
BuildRequires: gtest-devel

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{intname}-%{version} -p1
sed -e '/get_git_version/d' -e '/-Werror/d' -i CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_VERSION=%{version} \
    -DBENCHMARK_ENABLE_DOXYGEN:BOOL=ON \
    -DBENCHMARK_ENABLE_TESTING:BOOL=ON \
    -DBENCHMARK_USE_BUNDLED_GTEST:BOOL=OFF \
    -DBENCHMARK_ENABLE_GTEST_TESTS:BOOL=ON \
    -DBENCHMARK_ENABLE_INSTALL:BOOL=ON \
    -DBENCHMARK_INSTALL_DOCS:BOOL=ON \
    -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc CONTRIBUTING.md README.md
%license AUTHORS CONTRIBUTORS LICENSE
%{_libdir}/%{lbname}*.so.1*

%files devel
%{_libdir}/%{lbname}*.so
%{_includedir}/%{intname}/
%{_libdir}/cmake/%{intname}/
%{_libdir}/pkgconfig/%{intname}*.pc

%files doc
%{_docdir}/%{intname}/

%changelog
%autochangelog
