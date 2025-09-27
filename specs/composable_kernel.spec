%global upstreamname composable_kernel
%global rocm_release 7.0
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' )

# This package takes a very long time to build.
# For the review using only the test gpu, gfx1100
%global gpu_list "gfx1100"

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

Name:           composable_kernel
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        Performance Portable Programming Model for Machine Learning Tensor Operators
Url:            https://github.com/ROCm
License:        MIT

Source0:        %{url}/%{upstreamname}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel

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
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

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
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

%cmake \
    -DBUILD_TESTING=%{build_test} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_CXX_FLAGS="-fuse-ld=bfd" \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_HIP_ARCHITECTURES=%gpu_list \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DGPU_TARGETS=%gpu_list \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build -j ${JOBS}

%install
%cmake_install

# Clean up dupes
%fdupes %{buildroot}%{_prefix}

if [ -f %{buildroot}%{_prefix}/share/doc/composablekernel/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/composablekernel/LICENSE
fi

%files
%license LICENSE
%{_libdir}/libdevice_*.so.*
%{_libdir}/libutility.so.*

%files devel
%dir %{_includedir}/ck
%dir %{_includedir}/ck_tile
%dir %{_libdir}/cmake/%{name}
%doc README.md
%{_includedir}/ck/*
%{_includedir}/ck_tile/*
%{_libdir}/cmake/%{name}/*
%{_libdir}/libdevice_*.so
%{_libdir}/libutility.so

%if %{with test}
%files test
%{_bindir}/test*
%endif

%changelog
* Wed Sep 24 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Jul 31 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-1
- Update to 6.4.2

* Fri Jun 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.1-1
- Update to 6.4.1

* Wed Apr 30 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Initial Package
