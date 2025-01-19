%global upstreamname MIOpen
%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm

# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' )

# $gpu will be evaluated in the loops below             
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# For testing
# hardcoded use of gtest and dirs is not suitable for mock building
# Testsuite is not in great shape, fails instead of skips ck tests
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# Change this to the gpu family you are testing on
%bcond_with check
%global gpu_test default
%if %{with test}
%if %{with check}
# Do not build everything to do the test on one thing
%global rocm_gpu_list %{gpu_test}
%endif
%endif

# Needs to match rocblas
%bcond_without tensile

Name:           miopen
Version:        %{rocm_version}
Release:        3%{?dist}
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

# So we do not thrash memory
Patch2:         0001-add-link-and-compile-pools-for-miopen.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  gcc-c++
BuildRequires:  fplus-devel
BuildRequires:  frugally-deep-devel
BuildRequires:  half-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  hipblas-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocrand-devel
BuildRequires:  roctracer-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  zlib-devel

%if 0%{?suse_version}
BuildRequires:  libbz2-devel
BuildRequires:  libboost_filesystem-devel
%else
BuildRequires:  pkgconfig(bzip2)
%endif

%if %{with test}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

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

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

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

%if %{without tensile}
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/include/miopen/handle.hpp
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/solver/mha/mha_common.hpp
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/gemm_v2.cpp
%endif

# Our use of modules confuse install locations
# The db is not installed relative to the lib dir.
# Hardcode its location
sed -i -e 's@GetLibPath().parent_path() / "share/miopen/db"@"/usr/share/miopen/db"@' src/db_path.cpp.in

# Unsupported compiler flags
sed -i -e 's@opts.push_back("-fno-offload-uniform-block");@//opts.push_back("-fno-offload-uniform-block");@' src/comgr.cpp

# Paths to clang
sed -i -e 's@llvm/bin/clang@bin/clang@' src/hip/hip_build_utils.cpp

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
    %cmake -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	   -DCMAKE_CXX_COMPILER=hipcc \
	   -DCMAKE_C_COMPILER=hipcc \
	   -DROCM_SYMLINK_LIBS=OFF \
	   -DHIP_PLATFORM=amd \
	   -DAMDGPU_TARGETS=$ROCM_GPUS \
	   -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
	   -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
           -DBUILD_TESTING=%{build_test} \
           -DCMAKE_BUILD_TYPE=%{build_type} \
	   -DCMAKE_SKIP_RPATH=ON \
           -DBoost_USE_STATIC_LIBS=OFF \
           -DMIOPEN_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
           -DMIOPEN_PARALLEL_LINK_JOBS=$LINK_JOBS \
           -DMIOPEN_BACKEND=HIP \
           -DMIOPEN_BUILD_DRIVER=OFF \
	   -DMIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK=OFF \
	   -DMIOPEN_ENABLE_AI_KERNEL_TUNING=OFF \
	   -DMIOPEN_TEST_ALL=%{build_test} \
	   -DMIOPEN_USE_HIPBLASLT=OFF \
           -DMIOPEN_USE_MLIR=OFF \
           -DMIOPEN_USE_COMPOSABLEKERNEL=OFF

    %cmake_build

%if %{with test}
    %cmake_build -t tests
%endif

    module purge
done

%if %{with test}
%if %{with check}
%check
gpu=%{gpu_test}
module load rocm/$gpu
%cmake_build -t test
module purge
%endif
%endif

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done
echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}           -name 'install_*'    | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
find %{buildroot}           -name 'test_*'       | sed -f br.sed >  %{name}.test

if [ -f %{buildroot}%{_prefix}/share/doc/miopen-hip/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/miopen-hip/LICENSE.txt
fi

%files -f %{name}.files
%license LICENSE.txt

%files devel -f %{name}.devel
%dir %_datadir/%{name}
%dir %_datadir/%{name}/db
%dir %_includedir/%{name}
%dir %_libdir/cmake/%{name}
%doc README.md
%_datadir/%{name}/*
%_includedir/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- build requires gcc-c++

* Mon Dec 23 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Wed Dec 11 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Mon Dec 2 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-5
- Build on TW
- Use manual release and changelog


