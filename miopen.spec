%global upstreamname MIOpen
%global rocm_release 6.0
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm

# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' )

# $gpu will be evaluated in the loops below             
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

# For testing
# hardcoded use of gtest and dirs is not suitable for mock building
# Testsuite is not in great shape, fails instead of skips ck tests
%bcond_with test
# Change this to the gpu family you are testing on
%global gpu_test gfx9
%if %{with test}
# Do not build everything to do the test on one thing
%global rocm_gpu_list %{gpu_test}
%endif



Name:           miopen
Version:        %{rocm_version}
Release:        %autorelease
Summary:        AMD's Machine Intelligence Library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND BSD-2-Clause AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
# The base license is MIT with a couple of exceptions
# BSD-2-Clause
#   driver/mloSoftmaxHost.hpp
#   src/include/miopen/mlo_internal.hpp
# Apache-2.0
#   src/include/miopen/kernel_cache.hpp
#   src/kernel_cache.cpp
# Public Domain
#   src/md5.cpp

Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# https://github.com/ROCm/MIOpen/issues/2670
# https://github.com/ROCm/MIOpen/issues/2734
# patch from AMD
Patch1:         0001-fix-issue-2734-rel-6.0-commit.patch
# So we do not thrash memory
Patch2:         0001-add-link-and-compile-pools-for-miopen.patch
# Our use of modules confuse install locations
Patch3:         0001-Find-db-location-on-fedora.patch

BuildRequires:  pkgconfig(bzip2)
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  compiler-rt
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  fplus-devel
BuildRequires:  frugally-deep-devel
BuildRequires:  half-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  roctracer-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  zlib-devel

Requires:       rocm-rpm-macros-modules

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
AMD's library for high performance machine learning primitives.

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Readme has executable bit
chmod 644 README.md

# clang-tidy is brittle and not needed for rebuilding from a tarball
sed -i -e 's@clang-tidy@true@' cmake/ClangTidy.cmake

# workaround error on finding lbunzip2
sed -i -e 's@lbunzip2 bunzip2@bunzip2@' CMakeLists.txt

# https://github.com/ROCm/MIOpen/issues/2672
sed -i -e 's@find_path(HALF_INCLUDE_DIR half/half.hpp)@#find_path(HALF_INCLUDE_DIR half/half.hpp)@' CMakeLists.txt
# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done

# Tries to download its own googletest
# No good knob to turn it off so hack the cmake
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt
sed -i -e 's@add_subdirectory(speedtests)@#add_subdirectory(speedtests)@' CMakeLists.txt
%endif

%build

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=4
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

for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    %cmake %rocm_cmake_options \
%if %{with test}
          -DBUILD_TESTING=ON \
%else
          -DBUILD_TESTING=OFF \
%endif
          -DCMAKE_BUILD_TYPE=RelWithDebInfo \
          -DBoost_USE_STATIC_LIBS=OFF \
          -DMIOPEN_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
          -DMIOPEN_PARALLEL_LINK_JOBS=$LINK_JOBS \
          -DMIOPEN_BACKEND=HIP \
          -DMIOPEN_BUILD_DRIVER=OFF \
          -DMIOPEN_USE_MLIR=OFF \
          -DMIOPEN_USE_COMPOSABLEKERNEL=OFF

    %cmake_build
    module purge
done

%install

for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

%if %{with test}
%check
gpu=%{gpu_test}
module load rocm/$gpu
%cmake_build -t tests
%cmake_build -t test
module purge
%endif

%files 
%license LICENSE.txt
%exclude %{_docdir}/%{name}-hip/LICENSE.txt
%exclude %_bindir/install_precompiled_kernels.sh
%exclude %_libdir/rocm/gfx*/bin/install_precompiled_kernels.sh
%if %{with test}
%exclude %_bindir/test_perf.py
%exclude %_libdir/rocm/gfx*/bin/test_perf.py
%endif
%_libdir/libMIOpen.so.*
%_libdir/rocm/gfx*/lib/libMIOpen.so.*

%files devel
%dir %_libdir/cmake/%{name}
%dir %_libdir/rocm/gfx*/lib/cmake/%{name}

%doc README.md
%_datadir/%{name}/
%_includedir/%{name}/
%_libdir/libMIOpen.so
%_libdir/rocm/gfx*/lib/libMIOpen.so
%_libdir/cmake/%{name}/*
%_libdir/rocm/gfx*/lib/cmake/%{name}/*

%changelog
%autochangelog

