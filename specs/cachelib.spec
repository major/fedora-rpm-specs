%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

%bcond_without build_tests
# tests not discoverable by ctest yet
%bcond_with check

%global forgeurl https://github.com/facebook/CacheLib
%global tag 2025.02.03.00
%global date %(echo %{tag} | sed -e 's|.00$||' | sed -e 's|\\.||g')
# disable forge macro snapinfo generation
# https://pagure.io/fedora-infra/rpmautospec/issue/240
%global distprefix %{nil}
%forgemeta

# see cachelib/allocator/CacheVersion.h's kCachelibVersion
%global major_ver 17

Name:           cachelib
Version:        %{major_ver}^%{date}
Release:        %autorelease
Summary:        Pluggable caching engine for scale high performance cache services

License:        Apache-2.0
URL:            %forgeurl
Source:         %{url}/archive/v%{tag}/%{name}-%{tag}.tar.gz
# DeviceTest needs common/FdpNvme.cpp. Disable for now
Patch:          %{name}-fix-DeviceTest-FDP.diff
# incomplete dependencies, will sort out later
Patch:          %{name}-disable-binary_trace_gen.diff
# needed on EL8; its gtest does not come with cmake files
Patch100:       %{name}-find-gtest.patch
# Workaround for gcc issue (still needed on epel9 x86_64)
# https://bugzilla.redhat.com/show_bug.cgi?id=2108665
Patch200:         %{name}-workaround-gcc-epel9-x86_64-bz2108665.patch

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  fbthrift-devel = %{tag}
BuildRequires:  fizz-devel = %{tag}
BuildRequires:  folly-devel = %{tag}
BuildRequires:  mvfst-devel = %{tag}
%if %{with build_tests}
BuildRequires:  gmock-devel
%endif
# this is actually needed, because of
# cachelib/navy/admission_policy/DynamicRandomAP.h
BuildRequires:  gtest-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libzstd-devel
BuildRequires:  numactl-devel
BuildRequires:  wangle-devel
BuildRequires:  zlib-devel
BuildRequires:  tsl-sparse-map-devel
# BuildRequires:  libatomic


%global _description %{expand:
CacheLib is a C++ library providing in-process high performance caching
mechanism. CacheLib provides a thread safe API to build high throughput, low
overhead caching services, with built-in ability to leverage DRAM and SSD
caching transparently.}

%description %{_description}

%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake

%description devel %{_description}

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n CacheLib-%{tag} -N
%autopatch -p1 -M 99
%if 0%{?el8}
%autopatch -p1 -m 100 -M 199
%endif
%ifarch x86_64
%if 0%{?el9}
%autopatch -p1 -m 200 -M 209
%endif
%endif


%build
pushd %{name}
%cmake \
%if %{with build_tests}
  -DBUILD_TESTS:BOOL=ON \
%else
  -DBUILD_TESTS:BOOL=OFF \
%endif
  -DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=FALSE \
  -DCMAKE_INSTALL_DIR:PATH=%{_libdir}/cmake/%{name} \
  -DCONFIGS_INSTALL_DIR:STRING=%{_datadir}/%{name}/test_configs \
  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/%{name} \
  -DCACHELIB_MAJOR_VERSION:STRING=%{major_ver} \
  -DPACKAGE_VERSION:STRING=%{major_ver}.%{date}
%cmake_build


%install
pushd %{name}
%cmake_install
%if %{with build_tests}
# TODO: prevent tests being installed
rm -rf %{buildroot}%{_prefix}/tests
%endif


%if %{with check}
%check
pushd %{name}
%ctest
%endif


%files
%license LICENSE
%doc BENCHMARKS.md CHANGELOG.md README.md examples
%{_bindir}/cachebench
%{_datadir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/cmake/%{name}


%changelog
%autochangelog
