# The tests work but they rely on strict timing, which makes them flaky when
# run in koji, so keep them disabled for now
%bcond_with tests

# last tagged release is from 2016 despite ongoing development
%global commit 0d2e06ad501ec6e464b329b1bb3dc971049cf9db
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250124

Name:           wdt
Version:        1.32.1910230^%{?date}git%{?shortcommit}
Release:        %autorelease
Summary:        Warp speed Data Transfer

License:        BSD-3-Clause
URL:            https://www.facebook.com/WdtOpenSource
Source0:        https://github.com/facebook/wdt/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{date}git%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  boost-devel
BuildRequires:  double-conversion-devel
BuildRequires:  folly-devel
BuildRequires:  gflags-devel
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  jemalloc-devel
BuildRequires:  openssl-devel
%if %{with tests}
BuildRequires:  bash
BuildRequires:  python3
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# for wcp
Requires:       bash

%global _description %{expand:
Warp speed Data Transfer is aiming to transfer data between two systems
as fast as possible.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 1.32.1910230^20210809git57bbd43-1

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{_description}

The %{name}-libs package contains libraries for %{name}.


%prep
%setup -c -q
# wdt needs to be build from a base directory called wdt
# https://github.com/facebook/wdt/issues/213
ln -s %{name}-%{commit} %{name}
# Disable hardcoded CXX FLAGS
sed -i -e 's/set(CMAKE_CXX_FLAGS.*//' %{name}/CMakeLists.txt


%build
pushd %{name}
%cmake \
  -DCMAKE_CXX_FLAGS="%{optflags}" \
  -DCMAKE_SKIP_RPATH=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DWDT_USE_SYSTEM_FOLLY=ON \
%if %{with tests}
  -DBUILD_TESTING=ON
%else
  -DBUILD_TESTING=OFF
%endif
%cmake_build
popd


%install
pushd %{name}
%cmake_install
# move installed shared libraries in the right place if needed
%if "%{_lib}" == "lib64"
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif
popd


%if %{with tests}
%check
pushd %{_shared_builddir}
# tests are linked against a bunch of shared libraries
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}"
%ctest
popd
%endif


%files
%doc wdt/README.md
%license wdt/LICENSE
%{_bindir}/wdt
%{_bindir}/wcp

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files libs
%{_libdir}/*.so.1*


%changelog
%autochangelog
