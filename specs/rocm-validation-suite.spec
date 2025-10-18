%global upstreamname ROCmValidationSuite
%global rocm_release 7.0
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fcf-protection//' -e 's/-fcf-protection//' -e 's/-ffat-lto-objects//' -e 's/-flto=thin//' -e 's/-mtls-dialect=gnu2//')

%global _lto_cflags %{nil}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Name:           rocm-validation-suite
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        ROCm Validation Suite (rvs)

Url:            https://github.com/ROCm/ROCmValidationSuite
License:        MIT AND NCSA
# Only a few files are NCSA
# mem.so/README.md
# babel.so/include/rvs_memkernel.h
# mem.so/include/rvs_memkernel.h
# mem.so/include/rvs_memtest.h
# mem.so/src/rvs_memtest.cpp
# A comment from the README.md
#  This is a fork of the original, yet long-time unmaintained project at https://sourceforge.net/projects/cudagpumemtest/
# From inspection of cuda-memtest.tar.gz ver 1.1 the original copyright was kept
#
# Should be MIT
# https://github.com/ROCm/ROCmValidationSuite/issues/986
# cmake_modules/utils.cmake

Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# From CMakeMXDataGeneratorDownload.cmake
%global mxdata_commit 12c016dc694139317feb2e23c59028fde70beaf4
%global mxdata_scommit %(c=%{mxdata_commit}; echo ${c:0:7})
# MIT
Source1:        https://github.com/ROCm/mxDataGenerator/archive/%{mxdata_commit}/mxDataGenerator-%{mxdata_scommit}.tar.gz
# https://github.com/ROCm/ROCmValidationSuite/issues/1023
Patch1:         0001-rocm-validation-suite-do-not-download-mxDataGenerato.patch

BuildRequires:  amdsmi-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hipblas-common-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hiprand-devel
BuildRequires:  ninja-build
BuildRequires:  pciutils-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-omp-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  yaml-cpp-devel

ExclusiveArch: x86_64

%description
The ROCm Validation Suite (RVS) is a system validation and
diagnostics tool for monitoring, stress testing, detecting
and troubleshooting issues that affects the functionality
and performance of AMD GPU(s) operating in a
high-performance/AI/ML computing environment. RVS is enabled
using the ROCm software stack on a compatible software and
hardware platform.

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1

# mxDataGenerator
tar xf %{SOURCE1}
mv mxDataGenerator-* mxDataGenerator
cp -p mxDataGenerator/LICENSE.md mxDataGenerator/LICENSE.mxDataGenerator.md

# disable rpath
# Fixes these related issues on build
# ERROR   0010: file '/opt/rocm/usr/lib64/librvslib.so.0.0.0' contains an empty runpath in [:/..]
sed -i -e 's@set(CMAKE_SHARED_LINKER_FLAGS_INIT@#set(CMAKE_SHARED_LINKER_FLAGS_INIT@' CMakeLists.txt
sed -i -e 's@set(CMAKE_EXE_LINKER_FLAGS_INIT@#set(CMAKE_EXE_LINKER_FLAGS_INIT@' CMakeLists.txt

# fix opt/rocm things
sed -i -e 's@set(ROCM_PATH "/opt/rocm"@set(ROCM_PATH "/usr"@' CMakeLists.txt
sed -i -e 's@set(CMAKE_INSTALL_PREFIX "/opt/rocm"@#set(CMAKE_INSTALL_PREFIX "/opt/rocm"@' CMakeLists.txt

# lib64 vs lib
# https://github.com/ROCm/ROCmValidationSuite/issues/985
sed -i -e 's@HSA_PATH}/lib@HSA_PATH}/lib64@' CMakeLists.txt
sed -i -e 's@ROCBLAS_INC_DIR}/../lib@ROCBLAS_INC_DIR}/../lib64@' CMakeLists.txt
sed -i -e 's@HIPBLASLT_INC_DIR}/../lib@HIPBLASLT_INC_DIR}/../lib64@' CMakeLists.txt
sed -i -e 's@hiprand_INCLUDE_DIR}/../lib@hiprand_INCLUDE_DIR}/../lib64@' CMakeLists.txt
sed -i -e 's@rocrand_INCLUDE_DIR}/../lib@rocrand_INCLUDE_DIR}/../lib64@' CMakeLists.txt
# and with the dlopen
sed -i -e 's@../lib/rvs/@../lib64/rvs/@' rvs/src/rvsmodule.cpp

# rvs_lib_path
sed -i -e 's@DRVS_LIB_PATH="${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/rvs"@DRVS_LIB_PATH="/usr/lib64/rvs"@' CMakeLists.txt

# disable use of CPACK_PACKAGING_INSTALL_PREFIX
# https://github.com/ROCm/ROCmValidationSuite/issues/984
sed -i -e 's@DESTINATION ${CPACK_PACKAGING_INSTALL_PREFIX}/@DESTINATION @g' CMakeLists.txt
sed -i -e 's@INSTALL_DESTINATION ${CPACK_PACKAGING_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/cmake/rvs@INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/rvs@' CMakeLists.txt
sed -i -e 's@${CPACK_PACKAGING_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/cmake/rvs@${CMAKE_INSTALL_LIBDIR}/cmake/rvs@' CMakeLists.txt
find -type f -name CMakeLists.txt -print0 | xargs -0 sed -i -e 's@DESTINATION ${CPACK_PACKAGING_INSTALL_PREFIX}/@DESTINATION @g'

# Hardcoded gpus
# https://github.com/ROCm/ROCmValidationSuite/issues/983
# Need to remove 940,941
sed -i -e 's@--offload-arch=gfx940 --offload-arch=gfx941@@' CMakeLists.txt
# Need to remove 803
sed -i -e 's@--offload-arch=gfx803@@' CMakeLists.txt
# Need to add 1035,1103,1150,1151,1152
sed -i -e 's@--offload-arch=gfx1030@--offload-arch=gfx1030 --offload-arch=gfx1035 --offload-arch=gfx1103 --offload-arch=gfx1150 --offload-arch=gfx1151 --offload-arch=gfx1152@' CMakeLists.txt

# disable git usage on tarballs
sed -i -e 's@GIT NAMES git@GIT NAMES git-not-going-to-find-me@' cmake_modules/utils.cmake

# fix link of librvslib
sed -i -e '/add_library/a target_link_libraries(${RVS_TARGET} -lrocm_smi64 -lhipblaslt -lhiprand -lrocrand -lrocblas -lyaml-cpp -lpci -lamd_smi -lamdhip64 -lhsa-runtime64 -lomp)' rvslib/CMakeLists.txt

# for finding omp.h
sed -i -e 's@${YAML_CPP_INCLUDE_DIR}@${YAML_CPP_INCLUDE_DIR} "/usr/lib64/rocm/llvm/include" @' rvs/CMakeLists.txt
sed -i -e 's@${YAML_CPP_INCLUDE_DIR}@${YAML_CPP_INCLUDE_DIR} "/usr/lib64/rocm/llvm/include" @' rvslib/CMakeLists.txt

# No devel package
%build
%cmake -G Ninja \
       -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DCMAKE_BUILD_TYPE=%{build_type} \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DHIP_PLATFORM=amd \
       -DMXDATAGENERATOR_INC_DIR=${PWD}/mxDataGenerator/lib/include \
       -DRVS_BUILD_TESTS=FALSE

%cmake_build

%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocm-validation-suite/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocm-validation-suite/LICENSE
fi

# No devel package, remove devel like things
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/cmake
rm %{buildroot}%{_libdir}/librvslib.so{,.0}

# The libdir/rvs/*.so are dlopened, the version and symlinks are not needed
L="libbabel libgm libgpup libgst libiet libmem libpbqt libpeqt libperf libpebb libpesm librcqt libsmqt libtst"
for l in $L; do
    rm %{buildroot}%{_libdir}/rvs/$l.so{,.0}
    mv %{buildroot}%{_libdir}/rvs/$l.so.0.0.0 %{buildroot}%{_libdir}/rvs/$l.so
done

# rocm-validation-suite.x86_64: W: hidden-file-or-dir /usr/share/rocm-validation-suite/conf/.rvsmodules.config
# Is needed, this command
# rm %%{buildroot}%%{_datadir}/rocm-validation-suite/conf/.rvsmodules.config
# Produces this runtime error
# RVS-ERROR [CLI] file does not exist: /usr/bin/.rvsmodules.config

# Clean up dupes
# causes this problem
# rocm-validation-suite.x86_64: W: cross-directory-hard-link /usr/share/rocm-validation-suite/conf/MI300X/gst_single.conf /usr/share/rocm-validation-suite/conf/MI300X-HF/gst_single.conf
%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE mxDataGenerator/LICENSE.mxDataGenerator.md
%doc README.md
%dir %{_datadir}/rocm-validation-suite
%dir %{_libdir}/rvs
%{_bindir}/rvs
%{_datadir}/rocm-validation-suite/*
%{_libdir}/librvslib.so.0.0.0
%{_libdir}/rvs/libbabel.so
%{_libdir}/rvs/libgm.so
%{_libdir}/rvs/libgpup.so
%{_libdir}/rvs/libgst.so
%{_libdir}/rvs/libiet.so
%{_libdir}/rvs/libmem.so
%{_libdir}/rvs/libpbqt.so
%{_libdir}/rvs/libpeqt.so
%{_libdir}/rvs/libperf.so
%{_libdir}/rvs/libpebb.so
%{_libdir}/rvs/libpesm.so
%{_libdir}/rvs/librcqt.so
%{_libdir}/rvs/libsmqt.so
%{_libdir}/rvs/libtst.so

%changelog
* Thu Oct 16 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-2
- link rvslib with libomp

* Sat Oct 11 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Sat Sep 27 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-2
- build requires amdsmi-devel
- import mxdatagenertor

* Mon Sep 22 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Wed Sep 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-2
- Simplify cpack install change

* Sat Jul 26 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-1
- Initial package
