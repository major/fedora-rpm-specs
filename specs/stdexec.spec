# Stolen from eigen spec
# The (empty) main package is arch, to have the package built and tests run
# on all arches, but the actual result package is the -devel subpackge.
# Debuginfo packages are disabled to prevent rpmbuild from generating an empty
# debuginfo package for the empty main package.
%global debug_package %{nil}

Name:           stdexec
Release:        4%{?dist}
Summary:        A reference implementation of C++26 std::execution
# stdexec: Apache-2.0 WITH LLVM-exception AND MIT
# rapids-cmake: Apache-2.0
# cpm-cmake: MIT
# Catch2: BSL-1.0
# icm: MIT
# relacy: BSD-3-Clause
License:        Apache-2.0 WITH LLVM-exception AND MIT
SourceLicense:  Apache-2.0 WITH LLVM-exception AND MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
%global         forgeurl0 https://github.com/NVIDIA/stdexec
%global         commit0 34fa94719f97f49a553811423fa1200172f22a0e
%global         forgeurl1 https://github.com/rapidsai/rapids-cmake
%global         version1 24.02.00
%global         forgeurl2 https://github.com/cpm-cmake/CPM.cmake
%global         version2 0.38.5
%global         forgeurl3 https://github.com/catchorg/Catch2
%global         version3 3.14.0
%global         forgeurl4 https://github.com/iboB/icm
%global         version4 1.5.0
%global         forgeurl5 https://github.com/dvyukov/relacy
%global         commit5 2c87447b56b90cbccb5129c93a4e82eda5e7868e
%forgemeta -a
Version:        0.11.0~git20261016.%{sub %{commit0} 1 8}
URL:            %{forgeurl0}
Source0:        %{forgesource0}
Source1:        %{forgesource1}
Source2:        %{forgesource2}
Source3:        %{forgesource3}
Source4:        %{forgesource4}
Source5:        %{forgesource5}
Provides:       bundled(rapids-cmake) = %{version1}
Provides:       bundled(cpm-cmake) = %{version2}
Provides:       bundled(Catch2) = %{version3}
Provides:       bundled(icm) = %{version4}
Provides:       bundled(relacy) = 0~git260906.%{sub %{commit5} 1 8}

# merged upstream, exclude one failing test on ppcle64
Patch0:         https://patch-diff.githubusercontent.com/raw/NVIDIA/stdexec/pull/2356.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.28
BuildRequires:  git

%global stdexec_desc \
std::execution, the standard C++ framework for asynchronous and parallel \
programming. A reference implementation of std::execution, the C++26 model \
for asynchronous and parallel programming.

%description
%{stdexec_desc}

%package devel
Summary:        Development package for %{name} reference package
BuildArch:      noarch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       %{name}-static = %{version}-%{release}
%description devel
%{stdexec_desc}

This package contains the development files of %{name}.

%prep
%setup -q %{forgesetupargs0} -b 1 -b 2 -b 3 -b 4 -b 5
%patch -P0 -p1

# in rapids_cpm_download(): CPM.cmake needs to be known as CPM_<Version>.cmake
%__ln_s	%{_builddir}/%{topdir2}/cmake/CPM.cmake %{_builddir}/%{topdir2}/cmake/CPM_%{version2}.cmake

%__patch -d %{_builddir}/%{topdir4} -p1 <%{_builddir}/%{topdir0}/cmake/cpm/patches/icm/regex-build-error.diff

%conf
%cmake \
  -DSTDEXEC_BUILD_TESTS=ON \
  -DFETCHCONTENT_SOURCE_DIR_RAPIDS-CMAKE=%{_builddir}/%{topdir1} \
  -DCPM_SOURCE_CACHE=%{_builddir}/%{topdir2} \
  -DFETCHCONTENT_SOURCE_DIR_CATCH2=%{_builddir}/%{topdir3} \
  -DFETCHCONTENT_SOURCE_DIR_ICM=%{_builddir}/%{topdir4} \
  -DFETCHCONTENT_SOURCE_DIR_RELACY=%{_builddir}/%{topdir5}
  %{nil}

%build
%cmake_build

%install
%cmake_install
mkdir %{buildroot}/%{_datadir}
mv %{buildroot}/{%{_libdir},%{_datadir}}/cmake

%check
%ctest

%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/stdexec
%{_includedir}/exec
%{_includedir}/stdexec_version_config.hpp
%{_datadir}/cmake/stdexec

%changelog
* Thu Oct 29 2026 Christoph Junghans <junghans@votca.org> - 0.11.0~git20261016.34fa9471-4
- Initial commit (bug #2558317)
