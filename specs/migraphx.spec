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
%global upstreamname AMDMIGraphX
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global bundled_llvm_version 21.0.0

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"         xz level 7 using %%{getncpus} threads
%global _source_payload         w7T0.xzdio
%global _binary_payload         w7T0.xzdio

# The llvm build has its LLVM_PARALLEL_COMPILE|LINK_JOBS switches
%global _smp_mflags %{nil}

%global gpu_list %{rocm_gpu_list_default}

%bcond_with check
%if %{with check}
%global build_test ON
%else
%global build_test OFF
%endif

Name:           migraphx
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD's graph optimization engine
License:        MIT AND (Apache-2.0 WITH LLVM-exception OR NCSA)

# LICENSE : MIT
# AMDMIGraphX, the main project
#
# LICENSE.rocMLIR.TXT : Apache-2.0 WITH LLVM-exception OR NCSA
# 
# LICENSE.llvm-project.TXT : Apache-2.0 WITH LLVM-exception OR NCSA
# rocMLIR/external/llvm-project/*
#
# external/mlir-hal/CMakesLists.txt comes from
# Merge: 11d3f3f571aa 743bfaa4540c
# Author: SJW <swaters@amd.com>
# Date:   Tue Jun 20 18:59:07 2023 +0000
#
#    Add 'external/mlir-hal/' from commit '743bfaa4540cd124a260643b308f0dac3fceedd9'
#
# This is commit in the same rocMLIR project, so this is confusing, open this ticket
# suggesting a move from external/mlir-hal to mlir-hal
# https://github.com/ROCm/rocMLIR/issues/2026
#
# From fedora-review licensecheck.txt, the misc files
# Not used in the build was check by looking for object files in the build dir similar to
# $ find . -name '*.o' | grep -i blake
# 
# *No copyright* Apache License 2.0 and/or Creative Commons CC0 1.0
# -----------------------------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/BLAKE3/LICENSE
# blake3 is not used in the build
#
# *No copyright* Creative Commons Attribution 3.0
# -----------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/docs/CodeOfConduct.rst
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/docs/ReportingGuide.rst
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/docs/ResponseGuide.rst
# documents are not shipped
#
# *No copyright* Creative Commons CC0 1.0
# ---------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/include/llvm-c/blake3.h
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/BLAKE3/blake3.c
# blake3 is not used in the build
#
# *No copyright* GNU General Public License, Version 3
# ----------------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/docs/GoldPlugin.rst
# documents are not shipped
#
# *No copyright* Public domain
# ----------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/rpmalloc/README.md
# Not used in the build
#
# *No copyright* RealNetworks Public Source License
# -------------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/clang/docs/RealtimeSanitizer.rst
# documents are not shipped, no sanitizers used in build
# 
# Apache License 2.0 and/or Unicode License Agreement - Data Files and Software (2015)
# ------------------------------------------------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/include/llvm/Support/ConvertUTF.h
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/ConvertUTF.cpp
# Not used in the build
#
# Apache License 2.0 and/or Unicode License Agreement - Data Files and Software (2016) [generated file]
# -----------------------------------------------------------------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/UnicodeNameToCodepointGenerated.cpp
# Not used in the build
#
# BSD 2-Clause License
# --------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/include/llvm/Support/xxhash.h
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/xxhash.cpp
# Not used in the build 
#
# BSD 3-Clause License
# --------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/docs/re_format.7
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/COPYRIGHT.regex
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/reg*.c
# Not used in the build
#
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/openmp/runtime/src/thirdparty/ittnotify/LICENSE.txt
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/third-party/unittest/googlemock/LICENSE.txt
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/third-party/unittest/googlemock/*
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/third-party/unittest/googletest/LICENSE.TXT
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/third-party/unittest/googletest/*
# Test infra not shipped
#
# GNU General Public License
# --------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/docs/WritingAnLLVMPass.rst
# Document not shipped
#
# GNU General Public License v2.0 or later [generated file]
# ---------------------------------------------------------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/cmake/config.guess
# Script not shipped
#
# ISC License
# -----------
# migraphx-7.0.1-build/AMDMIGraphX-rocm-7.0.1/rocMLIR-rocm-7.0.1/external/llvm-project/llvm/lib/Support/regstrlcpy.c
# Not used in build

URL:            https://github.com/ROCm/AMDMIGraphX
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Source1:        https://github.com/ROCm/rocMLIR/archive/rocm-%{version}.tar.gz#/rocMLIR-%{version}.tar.gz
# Need to manually patch Source1
# https://github.com/ROCm/rocMLIR/pull/1953
# Source100:      0001-rocmlir-add-job-pools.patch

# https://github.com/ROCm/AMDMIGraphX/issues/4368
Patch1:         0001-migraphx-check-if-use_hipblaslt-before-call-gfx_defa.patch

# ROCm only works on x86_64
ExclusiveArch:  x86_64

BuildRequires:  ccache
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  miopen-devel
BuildRequires:  msgpack-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  protobuf-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-clang
BuildRequires:  rocm-cmake
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

# rocMLIR bundles a fork of rocm-llvm which itself is a fork of the upstream llvm
Provides:       bundled(llvm) = %bundled_llvm_version
Provides:       bundled(clang) = %bundled_llvm_version

%description
AMD MIGraphX is AMD's graph inference engine, which
accelerates machine learning model inference.

%package devel
Summary:        The development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
tar xf %{SOURCE1}
cd rocMLIR-rocm-%{version}
# patch -p1 < %{SOURCE100}
cp -p LICENSE.TXT ../LICENSE.rocMLIR.TXT
cp -p external/llvm-project/LICENSE.TXT ../LICENSE.llvm-project.TXT

# rm llvm-project bits we do not need
# llvm build is internal to rocMLIR, so we can not remove as much as we would like
rm -rf external/llvm-project/{amd,bolt,clang-tools-extra,clang/test,compiler-rt,flang,flang-rt,libclc,libcxx,lldb,llvm-libgcc,polly}

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
BUILD_MEM=2
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=32
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`

%global _vpath_srcdir rocMLIR-rocm-%{version}
%global _vpath_builddir build-rocmlir
# so we can find install
p=$PWD

%cmake -G Ninja \
       -DBUILD_FAT_LIBROCKCOMPILER=ON \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
       -DCMAKE_INSTALL_PREFIX=$PWD/install \
       -DROCMLIR_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
       -DROCMLIR_PARALLEL_LINK_JOBS=$LINK_JOBS

%cmake_build
%cmake_build -t install

%global _vpath_srcdir $PWD
%global _vpath_builddir build-migraphx
%cmake -G Ninja \
       -DBoost_USE_STATIC_LIBS=OFF \
       -DBUILD_TESTING=%{build_test} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_PREFIX_PATH=${p}/install/lib64/cmake \
       -DGPU_TARGETS=%{gpu_list} \
       -DMIGRAPHX_ENABLE_PYTHON=OFF \
       -DMIGRAPHX_USE_COMPOSABLEKERNEL=OFF \
       -DMIGRAPHX_USE_HIPBLASLT=OFF \
       -DMIOPEN_BACKEND=HIP 

%cmake_build -j $COMPILE_JOBS

%install
%global _vpath_builddir build-migraphx
%cmake_install

# Remove rpaths like
# chrpath -l libmigraphx_gpu.so.2012000.0
# libmigraphx_gpu.so.2012000.0: RUNPATH=$ORIGIN/../lib:$ORIGIN/../../
chrpath -d %{buildroot}%{_libdir}/libmigraphx*.so.*

rm -f %{buildroot}%{_prefix}/share/doc/migraphx/LICENSE


%if %{with check}
%check
%global _vpath_builddir build-migraphx
%ctest
%endif

%files
%license LICENSE LICENSE.rocMLIR.TXT LICENSE.llvm-project.TXT 
%{_bindir}/migraphx-driver
%{_bindir}/migraphx-hiprtc-driver
%{_libdir}/libmigraphx*.so.*

%files devel
%{_includedir}/migraphx/
%{_libdir}/libmigraphx*.so
%{_libdir}/cmake/migraphx/

%changelog
* Fri Nov 28 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Sat Nov 22 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Remove dir tags

* Sat Nov 8 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sat Oct 4 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1
- Add fedora copyright
- change --with test to --with check

* Sat Aug 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Initial package
