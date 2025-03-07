# Version 2.2.0 was “released” 2020-07-31 based on the version history in
# loguru.hpp, but the tag was never pushed to GitHub. We package a post-release
# snapshot with many bugfixes, CMake support, and Unlicense added as an
# alternative to the original public-domain dedication.
%global commit 4adaa185883e3c04da25913579c451d3c32cfac1
%global snapdate 20230406

# Tests want to use -fsanitize=address
# Lists copied from gcc.spec
# Current as of 15.0.1 (line 68).
# Note that asan and ubsan are available on all Fedora primary architectures;
# tsan is missing on i686 only.
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 riscv64
%global arch_has_asan 1
%endif
%bcond asan 0%{?arch_has_asan:1}

Name:           loguru
Version:        2.2.0^%{snapdate}git%{sub %{commit} 1 7}
%global so_version 2
Release:        %autorelease
Summary:        A lightweight C++ logging library

License:        LicenseRef-Fedora-Public-Domain OR Unlicense
URL:            https://github.com/emilk/loguru
Source:         %{url}/archive/%{commit}/loguru-%{commit}.tar.gz

# Fix invalid regex in lnav_format_loguru_cpp.json
# https://github.com/emilk/loguru/pull/250
Patch:          %{url}/pull/250.patch

# Update all cmake_minimum_required to 3.12; support CMake 4.0
# https://github.com/emilk/loguru/pull/257
Patch:          %{url}/pull/257.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Faster than the "UNIX Makefiles" backend for cmake, with no disadvantages
BuildRequires:  ninja-build

# For tests:
%if %{with asan}
BuildRequires:  libasan
%endif

# Automatically install format support when lnav is also installed
Requires:       (loguru-lnav = %{version}-%{release} if lnav)

%description
A lightweight and flexible C++ logging library.


%package devel
Summary:        Development files for loguru

Requires:       loguru%{?_isa} = %{version}-%{release}

%description devel
The loguru-devel package contains libraries and header files for developing
applications that use loguru.


%package lnav
Summary:        Configuration for lnav (Log File Navigator) to support loguru

BuildArch:      noarch

%description lnav
The loguru-lnav package contains configuration for lnav (Log File Navigator) to
support logs produced by loguru.


%package doc
Summary:        Documentation and examples for loguru

BuildArch:      noarch

%description doc
The loguru-doc package contains documentation and examples for developing
applications that use loguru. It does not bring in dependencies for compiling
and running the examples.


%prep
%autosetup -n loguru-%{commit} -p1

# Too strict for downstream packaging
sed -r -i 's/;?-Werror\b//' CMakeLists.txt test/CMakeLists.txt

%if %{without asan}
sed -r -i 's/-fsanitize=address\b//' test/CMakeLists.txt
%endif


%conf
# Building examples and tests from the top-level project is not yet supported.
#
# In docs/index.html, LOGURU_STACKTRACES=1 is documented as the default where
# supported.
#
# Setting LOGURU_WITH_STREAMS adds C++ iostream support to the shared library
# ABI without changing the C ABI; C++ in loguru.hpp is still guarded by whether
# or not LOGURU_WITH_STREAMS is defined before including loguru.hpp.
%cmake \
  -DLOGURU_INSTALL:BOOL=ON \
  -DLOGURU_BUILD_EXAMPLES:BOOL=OFF \
  -DLOGURU_BUILD_TESTS:BOOL=OFF \
  -DLOGURU_STACKTRACES:BOOL=ON \
  -DLOGURU_WITH_STREAMS:BOOL=ON \
  -GNinja

pushd test
%cmake -GNinja
popd


%build
%cmake_build

pushd test
%cmake_build
popd


%install
%cmake_install

# https://docs.lnav.org/en/latest/formats.html#installing-formats
install -D -p -m 0644 lnav_format_loguru_cpp.json \
    '%{buildroot}%{_sysconfdir}/lnav/formats/loguru_cpp.json'

# By default, the upstream CMake build system installs headers to the
# %%{_includedir}/loguru/ directory; however, documentation (such as README.md)
# implies that "#include <loguru.hpp>" (rather than "#include
# <loguru/loguru.hpp>") should suffice. Since there is only a single API
# header, we can support both usages by adding a symbolic link.
ln -s loguru/loguru.hpp '%{buildroot}%{_includedir}/loguru.hpp'


%check
pushd test
%ctest
popd


%files
%license LICENSE
%doc README.md
%{_libdir}/libloguru.so.%{so_version}{,.*}


%files devel
%dir %{_includedir}/loguru/
%{_includedir}/loguru/loguru.hpp
# Symbolic link
%{_includedir}/loguru.hpp

%{_libdir}/libloguru.so

%{_libdir}/cmake/loguru/
%{_libdir}/pkgconfig/loguru.pc


%files lnav
%license LICENSE
# We must co-own these directories. This subpackage could be installed without
# lnav, and lnav does not create and own them anyway.
%dir %{_sysconfdir}/lnav
%dir %{_sysconfdir}/lnav/formats
%config(noreplace) %{_sysconfdir}/lnav/formats/loguru_cpp.json


%files doc
%license LICENSE
# Basic hand-written HTML documentation
%doc docs/
%doc glog_example/
%doc loguru_cmake_example/
%doc loguru_example/


%changelog
%autochangelog
