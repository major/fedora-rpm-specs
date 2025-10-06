# rocm toolchain uses the hipcc wrapper of clang
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' -e 's/-flto=thin//' )
# lto problems
# ld.lld: error: CMakeFiles/magma.dir/control/libmagma.so.2.9.0.lto.constants.cpp.o:(.rodata.magma_diag_const+0x4): relocation R_X86_64_PC32 out of range: 5412144436 is not in [-2147483648, 2147483647]; r
%global _lto_cflags %nil

# Need to have a GPU in the build machine to test.
# To speed up testing, only gfx1201 is built
%bcond_with test
%if %{with test}
%global gpu_list gfx1201
%else
%global gpu_list %{rocm_gpu_list_default}
%endif

Name:           magma
Version:        2.9.0
Release:        %autorelease
Summary:        Matrix Algebra on GPU and Multi-core Architectures
Url:            https://icl.utk.edu/magma/
License:        BSD-3-Clause AND MIT
# From the license check
# The main license is BSD-3-Clause
#   COPYRIGHT
# Then ICS, with file copied from OPEN BSD
#   control/strlcpy.cpp
# Then MIT, with a file copied from hipify
# hipify is used but not delivered
#   tools/hipify-perl
# Reported GPL but not used, other similar files for cuda
#   results/v1.5.0/cuda7.0-k40c/setup.txt

Source0:        https://github.com/icl-utk-edu/%{name}/archive/v%{version}.tar.gz

# For versioning the *.so's
# https://bitbucket.org/icl/magma/issues/77/versioning-so
Patch0:         0001-Prepare-magma-cmake-for-fedora.patch

# https://github.com/jeffdaily/magma/commit/1b966b72402e3f37ebd462f3d7e019e669e510ff
Patch1:         0001-magma-ROCm-7-changes.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  flexiblas-devel
BuildRequires:  hipblas-devel
BuildRequires:  hipsparse-devel
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

# MIT
# Just the hipify-perl file is taken and it is very old
# This is older than any release of https://github.com/ROCm/HIPIFY.git
# So setting to earliest release -1
Provides:       bundled(hipify) = 3.4.0

# ROCm is only on x86_64:
ExclusiveArch:  x86_64

%description
Matrix Algebra on GPU and Multi-core Architectures (MAGMA) is a collection
of next-generation linear algebra libraries for heterogeneous computing.
The MAGMA package supports interfaces for current linear algebra packages
and standards (e.g., LAPACK and BLAS) to enable computational scientists
to easily port any linear algebra–reliant software component to
heterogeneous computing systems. MAGMA enables applications to fully
exploit the power of current hybrid systems of many-core CPUs and
multi-GPUs/coprocessors to deliver the fastest possible time to accurate
solutions within given energy constraints.

MAGMA features LAPACK-compliant routines for multi-core CPUs enhanced with
NVIDIA or AMD GPUs. MAGMA 2.7.2 now includes more than 400 routines that
cover one-sided dense matrix factorizations and solvers, two-sided
factorizations, and eigen/singular-value problem solvers, as well as a
subset of highly optimized BLAS for GPUs. A MagmaDNN package has been
added and further enhanced to provide high-performance data analytics,
including functionalities for machine learning applications that use MAGMA
as their computational back end. The MAGMA Sparse and MAGMA Batched
packages have been included since MAGMA 1.6.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1

%if %{with test}
# Just the test gpu gfx1201
sed -i -e 's@1032 1033@1201@' Makefile
# Remove some tests,
sed -i -e '/testing_zgenerate.cpp/d' testing/Makefile.src
%else
# Add some more gfx's
# https://bitbucket.org/icl/magma/issues/76/a-few-new-rocm-gpus
sed -i -e 's@1032 1033@950 1032 1033 1100 1101 1102 1103 1150 1151 1152 1153 1200 1201@' Makefile
# Disable building tests
sed -i -e 's@include_directories( testing )@#include_directories( testing )@' CMakeLists.txt
sed -i -e 's@foreach( filename ${testing_all} )@foreach( filename ${no_testing_all} )@' CMakeLists.txt
sed -i -e 's@add_custom_target( testing DEPENDS ${testing} )@#add_custom_target( testing DEPENDS ${testing} )@' CMakeLists.txt
sed -i -e 's@foreach( TEST ${sparse_testing_all} )@foreach( TEST ${no_sparse_testing_all} )@' CMakeLists.txt
sed -i -e 's@add_custom_target( sparse-testing DEPENDS ${sparse-testing} )@#add_custom_target( sparse-testing DEPENDS ${sparse-testing} )@' CMakeLists.txt
%endif

# Change the bin,lib install locations
sed -i -e 's@DESTINATION lib@DESTINATION ${CMAKE_INSTALL_LIBDIR}@' CMakeLists.txt
sed -i -e 's@DESTINATION bin@DESTINATION ${CMAKE_INSTALL_BINDIR}@' CMakeLists.txt

# Version *.so
sed -i -e 's@magma_VERSION@"%{version}"@g' CMakeLists.txt

# python to python3, need env to find local bits like magmasubs.py
sed -i -e 's@env python@env python3@' tools/checklist_run_tests.py
sed -i -e 's@env python@env python3@' tools/check-style.py
sed -i -e 's@env python@env python3@' tools/parse-magma.py

# Remove some files we do not need to similify licenses
# GPL, results for cuda
rm -rf results/*
# ICS, Copy of strlcpy - just use strlcpy
sed -i -e '/strlcpy/d' control/Makefile.src
sed -i -e '/strlcpy/d' include/magma_auxiliary.h
sed -i -e 's@magma_strlcpy@strlcpy@' control/trace.cpp
rm control/strlcpy.cpp

# Policy CMP0037 may not be set to OLD behavior because this version of CMake
sed -i -e 's@cmake_policy( SET CMP0037 OLD)@#cmake_policy( SET CMP0037 OLD)@' CMakeLists.txt

%build

export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
# To fix relocation overflow on link
export HIPCC_COMPILE_FLAGS_APPEND=--offload-compress

echo "BACKEND = hip"                          > make.inc
echo "FORT = false"                          >> make.inc
%if %{with test}
echo "GPU_TARGET = gfx1201" >> make.inc
%else
echo "GPU_TARGET = gfx900;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack+;gfx90a:xnack-;gfx942;gfx950;gfx1010;gfx1012;gfx1030;gfx1031;gfx1035;gfx1100;gfx1101;gfx1102;gfx1103;gfx1150;gfx1151;gfx1152;gfx1153;gfx1200;gfx1201" >> make.inc
%endif

make generate

%cmake -G Ninja \
       -DBLA_VENDOR=FlexiBLAS \
       -DCMAKE_CXX_COMPILER=hipcc \
       -DAMDGPU_TARGETS=%{gpu_list} \
       -DCMAKE_INSTALL_LIBDIR=%_libdir \
       -DMAGMA_ENABLE_HIP=ON \
       -DUSE_FORTRAN=OFF

%cmake_build

%install
%cmake_install

%if %{with test}
%check
# Results should be something like
# % MAGMA 2.9.0 svn 32-bit magma_int_t, 64-bit pointer.
# % HIP runtime 70051831, driver 70051831. MAGMA not compiled with OpenMP. 
# % device 0: AMD Radeon Graphics, 2420.0 MHz clock, 16304.0 MiB memory, gcn arch gfx1201
# % Sat Oct  4 08:05:46 2025
# % Usage: redhat-linux-build/testing/testing_sgemm [options] [-h|--help]
#
# % If running lapack (option --lapack), MAGMA and HIPBLAS error are both computed
# % relative to CPU BLAS result. Else, MAGMA error is computed relative to HIPBLAS result.
#
# % transA = No transpose, transB = No transpose
# %   M     N     K   MAGMA Gflop/s (ms)  HIPBLAS Gflop/s (ms)   CPU Gflop/s (ms)  MAGMA error  HIPBLAS error
# %========================================================================================================
# 1088  1088  1088   1778.70 (   1.45)     146.15 (  17.63)     ---   (  ---  )    1.25e-08        ---    ok
# 2112  2112  2112   10940.92 (   1.72)    10784.16 (   1.75)     ---   (  ---  )    1.19e-08        ---    ok
# 3136  3136  3136   10919.38 (   5.65)    11215.23 (   5.50)     ---   (  ---  )    1.34e-08        ---    ok
# 4160  4160  4160   11144.04 (  12.92)    12124.94 (  11.87)     ---   (  ---  )    1.13e-08        ---    ok
# 5184  5184  5184   12999.31 (  21.43)    14869.66 (  18.74)     ---   (  ---  )    1.29e-08        ---    ok
# 6208  6208  6208   13411.76 (  35.68)    14849.32 (  32.22)     ---   (  ---  )    1.07e-08        ---    ok
# 7232  7232  7232   13335.70 (  56.73)    14755.09 (  51.27)     ---   (  ---  )    8.81e-09        ---    ok
# 8256  8256  8256   13441.97 (  83.73)    14693.99 (  76.59)     ---   (  ---  )    8.36e-09        ---    ok
# 9280  9280  9280   13347.32 ( 119.75)    14706.62 ( 108.68)     ---   (  ---  )    1.13e-08        ---    ok
# 10304 10304 10304   13291.48 ( 164.62)    14655.85 ( 149.29)     ---   (  ---  )    1.04e-08        ---    ok
%{_vpath_builddir}/testing/testing_sgemm
%endif

%files
%license COPYRIGHT
%{_libdir}/libmagma.so.2{,.*}
%{_libdir}/libmagma_sparse.so.2{,.*}

%files devel
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libmagma.so
%{_libdir}/libmagma_sparse.so

%changelog
%autochangelog
