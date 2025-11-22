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
%if 0%{?suse_version}
%global rocsolver_name librocsolver0
%else
%global rocsolver_name rocsolver
%endif

%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif

%global upstreamname rocSOLVER
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif

%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# may run out of memory for both compile and link
# Calculate a good -j number below
%global _smp_mflags %{nil}

# Fortran is only used in testing
%global build_fflags %{nil}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use ninja if it is available
%if 0%{?fedora} || 0%{?suse_version}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

# export an llvm compilation database
# Useful for input for other llvm tools
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif

Name:           rocsolver
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        3%{?dist}
%endif
Summary:        Next generation LAPACK implementation for ROCm platform

# License check reports BSD 2-Clause
# But reviewing LICENSE.md, this is only for AMD
# Later in the file are BSD 3-Clause for LAPACK and MAGMA
License:        BSD-3-Clause AND BSD-2-Clause

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
Url:            https://github.com/ROCm/rocSOLVER
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
%endif

# https://github.com/ROCm/rocSOLVER/pull/652
Patch0:         0001-rocsolver-ninja-job-pools.patch
# Patch1:         0001-rocsolver-offload-compress.patch
# https://github.com/ROCm/rocSOLVER/pull/962
Patch2:         0001-rocsolver-parallel-jobs.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
# RFE to replace fmt:: with std::
# https://github.com/ROCm/rocSOLVER/issues/929
BuildRequires:  fmt-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocprim-static
BuildRequires:  rocsparse-devel

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}

%if 0%{?suse_version}
BuildRequires:  gcc-fortran
BuildRequires:  gtest
BuildRequires:  blas-devel-static
BuildRequires:  lapack-devel-static

# Problem on Tumbleweed 
# CMake Error at /usr/lib64/cmake/lapack-3.12.0/lapack-targets.cmake:98 (message):
#  The imported target "blas" references the file
#
#     "/usr/lib64/libblas.so.3.12.0"

%else
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  blas-static
BuildRequires:  lapack-static
%endif

%endif

%if %{with ninja}
%if 0%{?fedora}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

Provides:       rocsolver = %{version}-%{release}

%description
rocSOLVER is a work-in-progress implementation of a subset
of LAPACK functionality on the ROCm platform.

%if 0%{?suse_version}
%package -n %{rocsolver_name}
Summary:        Shared libraries for %{name}

%description -n %{rocsolver_name}
%{summary}

%ldconfig_scriptlets -n %{rocsolver_name}
%endif

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{rocsolver_name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocsolver
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

# As of 6.4, there are 2 long running hip jobs
# There are ~20 gpu targets
# Most builders will have between 4 and 32 cores
# Default to 2 cpu's per hip job
# Increase to half of the systems maximum
# Real cores, No hyperthreading
HIP_JOBS=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${HIP_JOBS}x = x ]; then
    HIP_JOBS=1
fi
# Try again..
if [ ${HIP_JOBS} = 1 ]; then
    HIP_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${HIP_JOBS}x = x ]; then
        HIP_JOBS=4
    fi
fi
HIP_JOBS=`eval "expr ${HIP_JOBS} / 2"`

# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=32
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
HIP_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$HIP_JOBS_MEM" -lt "$HIP_JOBS" ]; then
    HIP_JOBS=$HIP_JOBS_MEM
fi

sed -i -e "s@-parallel-jobs=4@-parallel-jobs=${HIP_JOBS}@" library/src/CMakeLists.txt

%build
%if %{with gitcommit}
cd projects/rocsolver
%endif

cat /proc/cpuinfo
cat /proc/meminfo
lscpu

# Real cores, No hyperthreading
COMPILE_JOBS=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
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
BUILD_MEM=8
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
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

%cmake %{cmake_generator} \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_C_COMPILER=hipcc \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DROCSOLVER_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DROCSOLVER_PARALLEL_LINK_JOBS=${LINK_JOBS} \
    -DBUILD_PARALLEL_HIP_JOBS=ON

%if %{with ninja}
%cmake_build
%else
%cmake_build -j ${JOBS}
%endif

%install
%if %{with gitcommit}
cd projects/rocsolver
%endif
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocsolver/LICENSE.md

%files  -n %{rocsolver_name}
%if %{with gitcommit}
%license projects/rocsolver/LICENSE.md
%doc projects/rocsolver/README.md
%else
%license LICENSE.md
%doc README.md
%endif

%{_libdir}/librocsolver.so.0{,.*}

%files devel
%{_includedir}/rocsolver/
%{_libdir}/librocsolver.so
%{_libdir}/cmake/rocsolver/

%if %{with test}
%files test
%{_datadir}/rocsolver/
%{_bindir}/rocsolver*
%endif

%changelog
* Thu Nov 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Remove dir tags

* Tue Nov 11 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Better handling of shared library on opensuse

* Thu Oct 30 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sat Oct 11 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Sat Sep 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-5
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-4
- Simplify removal of files

* Wed Aug 6 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-3
- Default build type RelWithDebInfo

* Wed Jul 30 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-2
- Remove -mtls-dialect cflag

* Tue Jul 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.2-1
- Update to 6.4.2
- Rebase patch1
- Fix some tabs to spaces in the specfile for consistent formatting

* Thu Jun 12 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Add hip jobs
- Remove suse if check for ldconfig
- Add export compilation database option

* Tue May 13 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Cleanup module build

* Fri Apr 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Thu Apr 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-7
- Reenable ninja

* Sun Apr 6 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-6
- Document RFE to remove fmt dependency

* Thu Feb 13 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-5
- Remove multibuild
- Fix SLE 15.6

* Tue Jan 21 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- multithread compress

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed
