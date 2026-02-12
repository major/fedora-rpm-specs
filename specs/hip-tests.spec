#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%global upstreamname hip-tests
%global rocm_release 7.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' -e 's/flto=thin//' )

# What gpu's we are testing
%global gpu_list "--offload-arch=gfx1100 --offload-arch=gfx1101 --offload-arch=gfx1102 --offload-arch=gfx1151 --offload-arch=gfx1200 --offload-arch=gfx1201"
%global _gpu_list "--offload-arch=gfx1100"

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond_with check

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Some lto issues
# ld.lld: error: undefined hidden symbol: __hip_gpubin_handle_8e42c98bcbd90dcf
# >>> referenced by memoryCommon.cc
# >>>               /tmp/InlineVarTest.lto.memoryCommon-13d8cd.o:(__hip_module_ctor)
# Also had to step on the cxx flags in the cmake step.
%global _lto_cflags %{nil}

Name:       hip-tests%{pkg_suffix}
Version:    %{rocm_version}
Release:    1%{?dist}
Summary:    HIP tests

License:    MIT AND BSL-1.0 AND Apache-2.0
# The MIT License is the main license
# The Boost Software License 1.0 is for the bundled catch2
# Apache 2.0 covers these files
#  catch/unit/math/math_special_values.hh
#  catch/unit/memory/hipSVMCommon.h
#  catch/unit/memory/hipSVMTestByteGranularity.cpp
#  catch/unit/memory/hipSVMTestFineGrainMemoryConsistency.cpp
#  catch/unit/memory/hipSVMTestFineGrainSyncBuffers.cpp
#  catch/unit/memory/hipSVMTestSharedAddressSpaceFineGrain.cp

URL:        https://github.com/ROCm/rocm-systems
Source0:    %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch1:     0001-hip-tests-build-on-fedora.patch
Patch2:     0001-hip-tests-link-with-libamd64.patch
Patch3:     0001-hip-tests-disable-spv.patch

ExclusiveArch:  x86_64

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  pkgconfig(opengl)
%if 0%{?fedora}
BuildRequires:  picojson-devel
%endif
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

# Boost Software License 1.0
# https://github.com/catchorg/Catch2/blob/v2.13.4/LICENSE.txt
Provides:       bundled(catch2) = 2.13.4

%if %{with check}
BuildRequires:  rocminfo
%endif

Requires:       cmake
Requires:       rocminfo

%description
This repository provides unit tests for HIP implementation.

%prep
%autosetup -n %{upstreamname} -p1

# Change path to clang-cpp
sed -i -e 's@${ROCM_PATH}/llvm/bin/clang-cpp@%{rocmllvm_bindir}/clang-cpp@' catch/CMakeLists.txt

# Change install to libexec
sed -i -e 's@INSTALL_DIR ${CMAKE_INSTALL_DATADIR}/hip@INSTALL_DIR libexec/hip-tests@' catch/packaging/CMakeLists.txt

# Some tests need to include stdlib.h to find malloc/free
sed -i '/hip\/hip_runtime/a#include <stdlib.h>' catch/unit/deviceLib/kerDevAlloc*.cc
sed -i '/hip\/hip_runtime/a#include <stdlib.h>' catch/unit/deviceLib/kerDevFree*.cc

# Need some help finding lamdhip64
sed -i -e 's@-lamdhip64@-L %{pkg_prefix}/%{pkg_libdir} -lamdhip64@' catch/unit/compiler/CMakeLists.txt

%if 0%{?fedora}
# Remove local copy of picojson, use the system version
rm -rf catch/external/picojson
%endif

# Rename the catch2 license so we can pick it up
mv catch/external/Catch2/LICENSE.txt catch/external/Catch2/LICENSE.catch2.txt

%build
cd catch

# hip is built with hipcc, append the location of the runtime headers
export HIPCC_COMPILE_FLAGS_APPEND="-I %{pkg_prefix}/include"

%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-O2 -I %{pkg_prefix}/include" \
    -DCMAKE_EXE_LINKER_FLAGS="-L %{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib \
    -DHIP_PLATFORM=amd \
    -DOFFLOAD_ARCH_STR=%{gpu_list} \
    -DROCM_PATH=%{pkg_prefix}

%cmake_build -t build_tests

# Need to be run locally with rpmbuild on a system with one of the GPU's
# in the gpu_offload_list.
#
%if %{with check}
%check
cd catch
%ctest --output-on-failure
%endif

%install
cd catch
%cmake_install

# rpmlint will have several issues with
# hip-tests.x86_64: W: unused-direct-shlib-dependency /usr/libexec/hip-tests/catch_tests/libLazyLoad.so /lib64/libgcc_s.so.1
# hip-tests.x86_64: W: unstripped-binary-or-object /usr/libexec/hip-tests/catch_tests/libLazyLoad.so
# libLazyLoad.so is only used by a dlopen as part of a unit test
# From unit/dynamicLoading/complex_loading_behavior.cc
# static bool launch_dynamically_loaded_kernel() {
#  bool testResult = true;
#  int ret = 1;
#
#  void* handle = dlopen("./libLazyLoad.so", RTLD_LAZY);

# Remove devel things
rm -rf %{buildroot}%%{pkg_prefix}/libexec/hip-tests/catch_tests/headers
rm -rf %{buildroot}%%{pkg_prefix}/libexec/hip-tests/catch_tests/saxpy.h

# Clean up dupes:
%fdupes %{buildroot}%{pkg_prefix}

%files
%doc README.md
%license LICENSE.md
%license catch/external/Catch2/LICENSE.catch2.txt
%{pkg_prefix}/libexec/hip-tests/

%changelog
* Mon Jan 26 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Dec 23 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-2
- Add --with compat

* Wed Nov 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Fri Oct 10 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Thu Sep 18 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.0-1
- Update to 7.0.0

* Mon Sep 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-2
- Build on RHEL
- Add Fedora license

* Mon Sep 8 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Initial package
