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

%bcond_with gitcommit
%if %{with gitcommit}
# 7.0.x is broken, ck was never updated in rocm-libraries
# https://github.com/ROCm/rocm-libraries/issues/2263
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif

%global upstreamname composablekernel
%global rocm_release 7.1
%global rocm_patch 1
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
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' )

# This package takes a very long time to build, build only the most useful.
# ck is needed for hipTensor but hipTensor only supports gfx908,gfx90a,gfx942,gfx950
%global ck_gpu_list "gfx11-generic;gfx12-generic"


%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# may run out of memory for both compile and link
# Calculate a good -j number below
%global _smp_mflags %{nil}

# export an llvm compilation database
# Useful for input for other llvm tools
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif

%bcond_without ck_contraction
%if %{with ck_contraction}
%global build_ck_contraction ON
%else
%global build_ck_contraction OFF
%endif

%bcond_without ck_conv
%if %{with ck_conv}
%global build_ck_conv ON
%else
%global build_ck_conv OFF
%endif

%bcond_without ck_gemm
%if %{with ck_gemm}
%global build_ck_gemm ON
%else
%global build_ck_gemm OFF
%endif

%bcond_without ck_mha
%if %{with ck_mha}
%global build_ck_mha ON
%else
%global build_ck_mha OFF
%endif

%bcond_without ck_other
%if %{with ck_other}
%global build_ck_other ON
%else
%global build_ck_other OFF
%endif

%bcond_without ck_reduction
%if %{with ck_reduction}
%global build_ck_reduction ON
%else
%global build_ck_reduction OFF
%endif

# Testing depends on having GPU hw, build only for these gpus to speed up tests
# Need to use --enable-network with mock
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# Reduce link pressure
%global _rocm_lto_cflags %{nil}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"         xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           composable_kernel%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        3%{?dist}
%endif
Summary:        Performance Portable Programming Model for Machine Learning Tensor Operators
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries

%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif

Patch1:         0001-composable_kernel-per-dir-build.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
Composable Kernel (CK) library aims to provide a programming
model for writing performance critical kernels for machine
learning workloads across multiple architectures including
GPUs, CPUs, etc, through general purpose kernel languages,
like HIP C++.

CK utilizes two concepts to achieve performance portability
and code maintainability:

- A tile-based programming model
- Algorithm complexity reduction for complex ML operators,
  using innovative technique we call "Tensor Coordinate
  Transformation".

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{without library}
Provides:       %{name}-static = %{version}-%{release}
%endif

%description devel
%{summary}

%package test
Summary: Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}

%prep
%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/composablekernel
%patch -P1 -p1
%else
%autosetup -p1 -n %{upstreamname}
%endif

# do not error on warnings
sed -i -e 's@add_compile_options(-Werror)@#add_compile_options(-Werror)@' CMakeLists.txt
sed -i -e '/-Werror/d' cmake/EnableCompilerWarnings.cmake
# No extra warnings
sed -i -e 's@add_compile_options(-Weverything)@#add_compile_options(-Weverything)@' CMakeLists.txt
sed -i -e '/-Wextra/d' cmake/EnableCompilerWarnings.cmake
sed -i -e '/-Wunused/d' cmake/EnableCompilerWarnings.cmake
sed -i -e '/-Weverything/d' cmake/EnableCompilerWarnings.cmake
sed -i -e 's@-Wno-unknown-warning-option@-Wno-unknown-warning-option -Wno-unused-parameter@' cmake/EnableCompilerWarnings.cmake

# Do not time the kernel loading
# https://github.com/ROCm/composable_kernel/issues/1780
sed -i -e 's@CK_TIME_KERNEL 1@CK_TIME_KERNEL 0@' include/ck/ck.hpp

# No way easy way to turn off examples building
# https://github.com/ROCm/composable_kernel/issues/1781
sed -i -e 's@add_subdirectory(example)@#add_subdirectory(example)@' CMakeLists.txt
# No profiler
sed -i -e 's@add_subdirectory(profiler)@#add_subdirectory(profiler)@' CMakeLists.txt

# Does not honor BUILD_SHARED
# https://github.com/ROCm/composable_kernel/issues/1782
sed -i -e 's@STATIC@SHARED@' library/src/utility/CMakeLists.txt library/src/tensor_operation_instance/gpu/CMakeLists.txt
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION \"%{version}\"@' library/src/utility/CMakeLists.txt library/src/tensor_operation_instance/gpu/CMakeLists.txt

%build
%if %{with gitcommit}
cd projects/composablekernel
%endif

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Try again..
if [ ${COMPILE_JOBS} = 1 ]; then
    COMPILE_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${COMPILE_JOBS}x = x ]; then
        COMPILE_JOBS=4
    fi
fi

# Take into account memmory usage per core, do not thrash real memory
# conv 4
BUILD_MEM=6
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi

LINK_MEM=12
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`

# hipTensors needs contraction,other,reduction

%cmake -G Ninja \
    -DBUILD_TESTING=%{build_test} \
    -DCK_BUILD_DEVICE_CONV=%{build_ck_conv} \
    -DCK_BUILD_DEVICE_CONTRACTION=%{build_ck_contraction} \
    -DCK_BUILD_DEVICE_GEMM=%{build_ck_gemm} \
    -DCK_BUILD_DEVICE_MHA=%{build_ck_mha} \
    -DCK_BUILD_DEVICE_OTHER=%{build_ck_other} \
    -DCK_BUILD_DEVICE_REDUCTION=%{build_ck_reduction} \
    -DCK_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DCK_PARALLEL_LINK_JOBS=${LINK_JOBS} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-fuse-ld=bfd" \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_HIP_ARCHITECTURES=%ck_gpu_list \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_HIP_COMPILER_ROCM_ROOT=%{pkg_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DENABLE_CLANG_CPP_CHECKS=OFF \
    -DGPU_ARCHS=%ck_gpu_list \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build

%install
%if %{with gitcommit}
cd projects/composablekernel
%endif

%cmake_install

%if %{without cklibs}
cp -p -r include/ck_tile %{buildroot}%{pkg_prefix}/include
%endif

# Clean up dupes
%fdupes %{buildroot}%{pkg_prefix}

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/composablekernel/LICENSE

%files
%if %{with gitcommit}
%doc projects/composablekernel/README.md
%license projects/composablekernel/LICENSE
%else
%doc README.md
%license LICENSE
%endif

%{pkg_prefix}/%{pkg_libdir}/libutility.so.*
%if %{with ck_conv} || %{with ck_gemm}
%{pkg_prefix}/%{pkg_libdir}/libdevice_conv_operations.so.*
%endif
%if %{with ck_gemm} || %{with ck_conv} || %{with ck_mha} || %{with ck_reduction} || %{with ck_contraction}
%{pkg_prefix}/%{pkg_libdir}/libdevice_gemm_operations.so.*
%endif
%if %{with ck_other}
%{pkg_prefix}/%{pkg_libdir}/libdevice_other_operations.so.*
%endif
%if %{with ck_reduction}
%{pkg_prefix}/%{pkg_libdir}/libdevice_reduction_operations.so.*
%endif
%if %{with ck_contraction}
%{pkg_prefix}/%{pkg_libdir}/libdevice_contraction_operations.so.*
%endif

%files devel
%{pkg_prefix}/include/ck/
%{pkg_prefix}/include/ck_tile/
%{pkg_prefix}/%{pkg_libdir}/cmake/composable_kernel/
%{pkg_prefix}/%{pkg_libdir}/libutility.so
%if %{with ck_conv} || %{with ck_gemm}
%{pkg_prefix}/%{pkg_libdir}/libdevice_conv_operations.so
%endif
%if %{with ck_gemm} || %{with ck_mha} || %{with ck_conv} || %{with ck_reduction} || %{with ck_contraction}
%{pkg_prefix}/%{pkg_libdir}/libdevice_gemm_operations.so
%endif
%if %{with ck_other}
%{pkg_prefix}/%{pkg_libdir}/libdevice_other_operations.so
%endif
%if %{with ck_reduction}
%{pkg_prefix}/%{pkg_libdir}/libdevice_reduction_operations.so
%endif
%if %{with ck_contraction}
%{pkg_prefix}/%{pkg_libdir}/libdevice_contraction_operations.so
%endif

%if %{with test}
%files test
%{pkg_prefix}/bin/test*
%endif

%changelog
* Sat Dec 27 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-3
- Add --with compat
- Fix build with ck_gemm

* Sun Nov 30 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-2
- Fix missing contraction libs

* Fri Nov 28 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Tue Nov 18 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Rework to use generic targets
- Selectively disable parts of build

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Thu Sep 25 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-2
- Add with cklibs option to disable lib builds

* Wed Sep 24 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Jul 31 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-1
- Update to 6.4.2

* Fri Jun 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.1-1
- Update to 6.4.1

* Wed Apr 30 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Initial Package
