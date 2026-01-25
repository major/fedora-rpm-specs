%global pypi_name torch

# Where the src comes from
%global forgeurl https://github.com/pytorch/pytorch

# So pre releases can be tried
%bcond_with gitcommit
%if %{with gitcommit}
# v2.9.0-rc9
%global commit0 0fabc3ba44823f257e70ce397d989c8de5e362c1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20251008
%global pypi_version 2.9.0
%global flatbuffers_version 24.12.23
%global miniz_version 3.0.2
%global pybind11_version 2.13.6
%global rc_tag -rc9
%else
%global pypi_version 2.9.1
%global flatbuffers_version 24.12.23
%global miniz_version 3.0.2
%global pybind11_version 2.13.6
%endif

# For -test subpackage
# suitable only for local testing
# Install and do something like
#   export LD_LIBRARY_PATH=/usr/lib64/python3.12/site-packages/torch/lib
#   /usr/lib64/python3.12/site-packages/torch/bin/test_api, test_lazy
%bcond_with test

%ifarch x86_64
%bcond_without rocm
%endif

# For testing distributed+rccl etc.
%bcond_with gloo
%bcond_without mpi
%bcond_without tensorpipe

# Disable dwz with rocm because memory can be exhausted
%if %{with rocm}
%define _find_debuginfo_dwz_opts %{nil}
%endif

# These came in 2.4 and not yet in Fedora
%bcond_with opentelemetry
%bcond_with httplib
%bcond_with kineto

# In fedora, not in rhel/epel or requires a newer version
%if 0%{?fedora}
%bcond_without eigen3
%bcond_without onnx
%bcond_without protobuf
%bcond_without setuptools
%else
%bcond_with eigen3
%bcond_with onnx
%bcond_with protobuf
%bcond_with setuptools
%endif

# 1/23/26
# nothing provides (python3.14dist(mpmath) < 1.4~~ with python3.14dist(mpmath) >= 1.1) needed by python3-sympy-1.14.0-10.fc44.noarch from fedora
%bcond_with sympy

Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        %autorelease
Summary:        PyTorch AI/ML framework
# See license.txt for license details
License:        BSD-3-Clause AND BSD-2-Clause AND 0BSD AND Apache-2.0 AND MIT AND BSL-1.0 AND GPL-3.0-or-later AND Zlib

URL:            https://pytorch.org/
%if %{with gitcommit}
Source0:        %{forgeurl}/archive/%{commit0}/pytorch-%{shortcommit0}.tar.gz
Source1000:     pyproject.toml
%else
Source0:        %{forgeurl}/releases/download/v%{version}/pytorch-v%{version}.tar.gz
%endif
Source1:        https://github.com/google/flatbuffers/archive/refs/tags/v%{flatbuffers_version}.tar.gz
Source2:        https://github.com/pybind/pybind11/archive/refs/tags/v%{pybind11_version}.tar.gz

# Developement on tensorpipe has stopped, repo made read only July 1, 2023, this is the last commit
%global tp_commit 52791a2fd214b2a9dc5759d36725909c1daa7f2e
%global tp_scommit %(c=%{tp_commit}; echo ${c:0:7})
Source20:       https://github.com/pytorch/tensorpipe/archive/%{tp_commit}/tensorpipe-%{tp_scommit}.tar.gz
# The old libuv tensorpipe uses
Source21:       https://github.com/libuv/libuv/archive/refs/tags/v1.41.0.tar.gz
# Developement afaik on libnop has stopped, this is the last commit
%global nop_commit 910b55815be16109f04f4180e9adee14fb4ce281
%global nop_scommit %(c=%{nop_commit}; echo ${c:0:7})
Source22:       https://github.com/google/libnop/archive/%{nop_commit}/libnop-%{nop_scommit}.tar.gz

%if %{without opentelemetry}
%global ot_ver 1.14.2
Source60:       https://github.com/open-telemetry/opentelemetry-cpp/archive/refs/tags/v%{ot_ver}.tar.gz
%endif

%if %{without httplib}
%global hl_commit 3b6597bba913d51161383657829b7e644e59c006
%global hl_scommit %(c=%{hl_commit}; echo ${c:0:7})
Source70:       https://github.com/yhirose/cpp-httplib/archive/%{hl_commit}/cpp-httplib-%{hl_scommit}.tar.gz
%endif

%if %{without kineto}
%global ki_commit 5e7501833f1021ce6f618572d3baf657b6319658
%global ki_scommit %(c=%{ki_commit}; echo ${c:0:7})
Source80:       https://github.com/pytorch/kineto/archive/%{ki_commit}/kineto-%{ki_scommit}.tar.gz
%endif

%global ox_ver 1.18.0
Source90:       https://github.com/onnx/onnx/archive/refs/tags/v%{ox_ver}.tar.gz

%global pb_ver 3.19.6
Source100:      https://github.com/protocolbuffers/protobuf/archive/refs/tags/v%{pb_ver}.tar.gz

# A problem on RHEL 10
# + /usr/bin/python3 setup.py build '--executable=/usr/bin/python3 -sP'
# Traceback (most recent call last):
#  File "/root/rpmbuild/BUILD/pytorch-v2.9.1/setup.py", line 288, in <module>
#    import setuptools.command.bdist_wheel
# ModuleNotFoundError: No module named 'setuptools.command.bdist_wheel'
# This support came in 70.1.0, RHEL 10.2 has 69.0.3
# Use ELN version
%global st_ver 80.9.0
Source110:      https://github.com/pypa/setuptools/archive/refs/tags/v%{st_ver}.tar.gz

%global pt_arches x86_64 aarch64
ExclusiveArch:  %pt_arches
%global toolchain gcc
%global _lto_cflags %nil

BuildRequires:  cmake
BuildRequires:  cpuinfo-devel
%if %{with eigen3}
BuildRequires:  eigen3-devel
%endif
BuildRequires:  flexiblas-devel
BuildRequires:  fmt-devel
BuildRequires:  foxi-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran

%if %{with gloo}
BuildRequires:  gloo-devel
%endif
BuildRequires:  json-devel

BuildRequires:  libomp-devel
BuildRequires:  moodycamel-concurrentqueue-devel
BuildRequires:  numactl-devel
%if %{with onnx}
BuildRequires:  onnx-devel
%endif
%if %{with mpi}
BuildRequires:  openmpi-devel
%endif
%if %{with protobuf}
BuildRequires:  protobuf-devel
%endif
BuildRequires:  sleef-devel
BuildRequires:  valgrind-devel
BuildRequires:  pocketfft-devel
BuildRequires:  pthreadpool-devel

BuildRequires:  FP16-devel
BuildRequires:  fxdiv-devel
BuildRequires:  psimd-devel
BuildRequires:  xnnpack-devel = 0.0^git20240814.312eb7e

BuildRequires:  python3-devel
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml)
%if %{with setuptools}
BuildRequires:  python3dist(setuptools)
%endif
%if %{with sympy}
BuildRequires:  python3dist(sympy)
%endif
BuildRequires:  python3dist(typing-extensions)

# Packages missing for RHEL/EPEL
%if 0%{?fedora}
BuildRequires:  python3-pybind11
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(sphinx)
# New for 2.9 / EPEL 10.2
BuildRequires:  ninja-build
%endif

%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  hipsparselt-devel
BuildRequires:  hipsolver-devel
BuildRequires:  magma-devel
BuildRequires:  miopen-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocfft-devel
BuildRequires:  rccl-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocsolver-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  rocthrust-devel
BuildRequires:  roctracer-devel

Requires:       amdsmi

%endif

%if %{with test}
BuildRequires:  google-benchmark-devel
%endif

Requires:       python3dist(dill)
Requires:       python3dist(yaml)

Obsoletes:      caffe  = 1.0^git20200212.9b89154

%description
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# For convience
Provides:       pytorch

# Apache-2.0
Provides:       bundled(flatbuffers) = %{flatbuffers_version}
# MIT
Provides:       bundled(miniz) = %{miniz_version}
Provides:       bundled(pybind11) = %{pybind11_version}

%if %{with tensorpipe}
# BSD-3-Clause
Provides:       bundled(tensorpipe)
# Apache-2.0
Provides:       bundled(libnop)
# MIT AND CC-BY-4.0 AND ISC AND BSD-2-Clause
Provides:       bundled(libuv) = 1.41.0
%endif

%description -n python3-%{pypi_name}
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

%if %{with test}
%package -n python3-%{pypi_name}-test
Summary:        Tests for %{name}
Requires:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}

%description -n python3-%{pypi_name}-test
%{summary}
%endif


%prep

%if %{with gitcommit}
%autosetup -p1 -n pytorch-%{commit0}
# Overwrite with a git checkout of the pyproject.toml
cp %{SOURCE1000} .

%else
%autosetup -p1 -n pytorch-v%{version}

# GitHub release tarballs identify the version as an alpha, so replace that
echo "%{pypi_version}" > version.txt

%endif

%if %{without setuptools}
mkdir -p extra-python
cd extra-python
tar xf %{SOURCE110}
mv setuptools-* setuptools
cd ..
%endif

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

tar xf %{SOURCE1}
rm -rf third_party/flatbuffers/*
cp -r flatbuffers-%{flatbuffers_version}/* third_party/flatbuffers/

tar xf %{SOURCE2}
rm -rf third_party/pybind11/*
cp -r pybind11-%{pybind11_version}/* third_party/pybind11/

%if %{with tensorpipe}
tar xf %{SOURCE20}
rm -rf third_party/tensorpipe/*
cp -r tensorpipe-*/* third_party/tensorpipe/
tar xf %{SOURCE21}
rm -rf third_party/tensorpipe/third_party/libuv/*
cp -r libuv-*/* third_party/tensorpipe/third_party/libuv/
tar xf %{SOURCE22}
rm -rf third_party/tensorpipe/third_party/libnop/*
cp -r libnop-*/* third_party/tensorpipe/third_party/libnop/

# gcc 15 include cstdint
sed -i '/#include <tensorpipe.*/a#include <cstdint>' third_party/tensorpipe/tensorpipe/common/allocator.h
sed -i '/#include <tensorpipe.*/a#include <cstdint>' third_party/tensorpipe/tensorpipe/common/memory.h
%endif

%if %{without opentelemtry}
tar xf %{SOURCE60}
rm -rf third_party/opentelemetry-cpp/*
cp -r opentelemetry-cpp-*/* third_party/opentelemetry-cpp/
%endif

%if %{without httplib}
tar xf %{SOURCE70}
rm -rf third_party/cpp-httplib/*
cp -r cpp-httplib-*/* third_party/cpp-httplib/
%endif

%if %{without kineto}
tar xf %{SOURCE80}
rm -rf third_party/kineto/*
cp -r kineto-*/* third_party/kineto/
%endif

%if %{without onnx}
tar xf %{SOURCE90}
rm -rf third_party/onnx/*
cp -r onnx-*/* third_party/onnx/
%endif

%if %{without protobuf}
tar xf %{SOURCE100}
rm -rf third_party/protobuf/*
cp -r protobuf-*/* third_party/protobuf/
%endif

# Adjust for the hipblaslt's we build
sed -i -e 's@"gfx1100", "gfx1101", "gfx1200", "gfx1201", "gfx908",@"gfx1100", "gfx1101", "gfx1200", "gfx1201", "gfx1151",@' aten/src/ATen/native/cuda/Blas.cpp

%if 0%{?rhel}
# In RHEL but too old
sed -i -e '/typing-extensions/d' setup.py
# Need to pip these
sed -i -e '/sympy/d' setup.py
sed -i -e '/fsspec/d' setup.py
%else
# for 2.5.0
sed -i -e 's@sympy==1.13.1@sympy>=1.13.1@' setup.py
%endif

# A new dependency
# Connected to USE_FLASH_ATTENTION, since this is off, do not need it
sed -i -e '/aotriton.cmake/d' cmake/Dependencies.cmake
# Compress hip
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc --offload-compress@' cmake/Dependencies.cmake
# Silence noisy warning
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-pass-failed@' cmake/Dependencies.cmake
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-unused-command-line-argument@' cmake/Dependencies.cmake
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-unused-result@' cmake/Dependencies.cmake
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-deprecated-declarations@' cmake/Dependencies.cmake
# Use parallel jobs
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -parallel-jobs=4@' cmake/Dependencies.cmake
# Need to link with librocm_smi64
sed -i -e 's@hiprtc::hiprtc@hiprtc::hiprtc rocm_smi64@' cmake/Dependencies.cmake

# No third_party fmt, use system
sed -i -e 's@fmt::fmt-header-only@fmt@' CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' aten/src/ATen/CMakeLists.txt
sed -i -e 's@list(APPEND ATen_HIP_INCLUDE $<TARGET_PROPERTY:fmt,INTERFACE_INCLUDE_DIRECTORIES>)@@' aten/src/ATen/CMakeLists.txt

sed -i -e 's@fmt::fmt-header-only@fmt@' third_party/kineto/libkineto/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' c10/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' torch/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' cmake/Dependencies.cmake
sed -i -e 's@fmt::fmt-header-only@fmt@' caffe2/CMakeLists.txt

sed -i -e 's@add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@#add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@' cmake/Dependencies.cmake
sed -i -e 's@set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@#set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@' cmake/Dependencies.cmake
sed -i -e 's@list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)@#list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)@' cmake/Dependencies.cmake

# No third_party FXdiv
sed -i -e 's@if(NOT TARGET fxdiv)@if(MSVC AND USE_XNNPACK)@' caffe2/CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@#TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@' caffe2/CMakeLists.txt

# https://github.com/pytorch/pytorch/issues/149803
# Tries to checkout nccl
sed -i -e 's@    checkout_nccl()@    True@' tools/build_pytorch_libs.py

# Disable the use of check_submodule's in the setup.py, we are a tarball, not a git repo
sed -i -e 's@check_submodules()$@#check_submodules()@' setup.py

# Release comes fully loaded with third party src
# Remove what we can
#
# For 2.1 this is all but miniz-2.1.0
# Instead of building as a library, caffe2 reaches into
# the third_party dir to compile the file.
# mimiz is licensed MIT
# https://github.com/richgel999/miniz/blob/master/LICENSE
mv third_party/miniz-%{miniz_version} .
#
# setup.py depends on this script
mv third_party/build_bundled.py .

# Need the just untarred flatbuffers/flatbuffers.h
mv third_party/flatbuffers .

mv third_party/pybind11 .

%if %{with tensorpipe}
mv third_party/tensorpipe .
%endif

%if %{without opentelemetry}
mv third_party/opentelemetry-cpp .
%endif

%if %{without httplib}
mv third_party/cpp-httplib .
%endif

%if %{without kineto}
mv third_party/kineto .
%endif

%if %{without onnx}
mv third_party/onnx .
%endif

%if %{without protobuf}
mv third_party/protobuf .
%endif

%if %{with test}
mv third_party/googletest .
%endif

# Remove everything
rm -rf third_party/*
# Put stuff back
mv build_bundled.py third_party
mv miniz-%{miniz_version} third_party
mv flatbuffers third_party
mv pybind11 third_party

%if %{with tensorpipe}
mv tensorpipe third_party
%endif

%if %{without opentelemetry}
mv opentelemetry-cpp third_party
%endif

%if %{without httplib}
mv cpp-httplib third_party
%endif

%if %{without kineto}
mv kineto third_party
%endif

%if %{without onnx}
mv onnx third_party
%endif

%if %{without protobuf}
mv protobuf third_party
%endif

%if %{with test}
mv googletest third_party
%endif

#
# Fake out pocketfft, and system header will be used
mkdir third_party/pocketfft
cp /usr/include/pocketfft_hdronly.h third_party/pocketfft/

#
# Use the system valgrind headers
mkdir third_party/valgrind-headers
cp %{_includedir}/valgrind/* third_party/valgrind-headers

# Fix installing to /usr/lib64
sed -i -e 's@DESTINATION ${PYTHON_LIB_REL_PATH}@DESTINATION ${CMAKE_INSTALL_PREFIX}/${PYTHON_LIB_REL_PATH}@' caffe2/CMakeLists.txt

# reenable foxi linking
sed -i -e 's@list(APPEND Caffe2_DEPENDENCY_LIBS foxi_loader)@#list(APPEND Caffe2_DEPENDENCY_LIBS foxi_loader)@' cmake/Dependencies.cmake

# cmake version changed
sed -i -e 's@cmake_minimum_required(VERSION 3.4)@cmake_minimum_required(VERSION 3.5)@' third_party/tensorpipe/third_party/libuv/CMakeLists.txt
sed -i -e 's@cmake_minimum_required(VERSION 3.4)@cmake_minimum_required(VERSION 3.5)@' libuv*/CMakeLists.txt
%if %{without opentelemtry}
sed -i -e 's@cmake_minimum_required(VERSION 3.1)@cmake_minimum_required(VERSION 3.5)@' third_party/opentelemetry-cpp/CMakeLists.txt
%endif

%if %{with rocm}
# hipify
./tools/amd_build/build_amd.py
# Fedora installs to /usr/include, not /usr/include/rocm-core
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/hip/tunable/TunableGemm.h
# https://github.com/pytorch/pytorch/issues/149805
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' cmake/public/LoadHIP.cmake
# Fedora installs to /usr/include, not /usr/include/rocm-core
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/hip/tunable/Tunable.cpp
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/cuda/tunable/Tunable.cpp
# use any hip, correct CMAKE_MODULE_PATH
sed -i -e 's@lib/cmake/hip@lib64/cmake/hip@' cmake/public/LoadHIP.cmake
sed -i -e 's@HIP 1.0@HIP MODULE@'            cmake/public/LoadHIP.cmake
# silence an assert
# sed -i -e '/qvalue = std::clamp(qvalue, qmin, qmax);/d' aten/src/ATen/native/cuda/IndexKernel.cu

%endif

# moodycamel include path needs adjusting to use the system's
sed -i -e 's@${PROJECT_SOURCE_DIR}/third_party/concurrentqueue@/usr/include/concurrentqueue@' cmake/Dependencies.cmake

%build

# Export the arches
# echo "%%pytorch_arches %pt_arches"   > macros.pytorch

#
# Control the number of jobs
#
# The build can fail if too many threads exceed the physical memory
# Run at least one thread, more if CPU & memory resources are available.
#
%ifarch x86_64
# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
%else
# cpuinfo format varies on other arches, fall back to nproc
COMPILE_JOBS=`nproc`
%endif
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
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
export MAX_JOBS=$COMPILE_JOBS

# For debugging setup.py
# export SETUPTOOLS_SCM_DEBUG=1

# For verbose cmake output
# export VERBOSE=ON
# For verbose linking
# export CMAKE_SHARED_LINKER_FLAGS=-Wl,--verbose

# Manually set this hardening flag
export CMAKE_EXE_LINKER_FLAGS=-pie

%if %{with protobuf}
export BUILD_CUSTOM_PROTOBUF=OFF
%endif

export BUILD_NVFUSER=OFF
export BUILD_SHARED_LIBS=ON
export BUILD_TEST=OFF
export CMAKE_BUILD_TYPE=RelWithDebInfo
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_DISTRIBUTED=OFF
export USE_CUDA=OFF
export USE_FAKELOWP=OFF
export USE_FBGEMM=OFF
export USE_FLASH_ATTENTION=OFF
export USE_GLOO=OFF
export USE_ITT=OFF
export USE_KINETO=OFF
export USE_KLEIDIAI=OFF
export USE_LITE_INTERPRETER_PROFILER=OFF
export USE_LITE_PROTO=OFF
export USE_MAGMA=OFF
export USE_MEM_EFF_ATTENTION=OFF
export USE_MKLDNN=OFF
export USE_MPI=OFF
export USE_NCCL=OFF
export USE_NNPACK=OFF
export USE_NUMPY=ON
export USE_OPENMP=ON
export USE_PYTORCH_QNNPACK=OFF
export USE_ROCM=OFF
export USE_SYSTEM_SLEEF=ON
%if %{with eigen3}
export USE_SYSTEM_EIGEN_INSTALL=ON
%endif
%if %{with onnx}
export USE_SYSTEM_ONNX=ON
%endif
export USE_SYSTEM_PYBIND11=OFF
export USE_SYSTEM_LIBS=OFF
export USE_SYSTEM_NCCL=OFF
export USE_TENSORPIPE=OFF
export USE_XNNPACK=OFF
export USE_XPU=OFF
export USE_SYSTEM_PTHREADPOOL=ON
export USE_SYSTEM_CPUINFO=ON
export USE_SYSTEM_FP16=ON
export USE_SYSTEM_FXDIV=ON
export USE_SYSTEM_PSIMD=ON
export USE_SYSTEM_XNNPACK=OFF

export USE_DISTRIBUTED=ON
%if %{with tensorpipe}
export USE_TENSORPIPE=ON
export TP_BUILD_LIBUV=OFF
%endif

%if %{with gloo}
export USE_GLOO=ON
export USE_SYSTEM_GLOO=ON
%endif
%if %{with mpi}
export USE_MPI=ON
%endif

%if %{with test}
export BUILD_TEST=ON
%endif

%if %{with rocm}

export USE_ROCM=ON
export USE_ROCM_CK_SDPA=OFF
export USE_ROCM_CK_GEMM=OFF
export USE_FBGEMM_GENAI=OFF

export USE_MAGMA=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`

# pytorch uses clang, not hipcc
export HIP_CLANG_PATH=%{rocmllvm_bindir}
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}

%endif

%if %{without setuptools}
cd extra-python
EXTRA_PYTHON=$PWD
cd setuptools
python3 setup.py install --root $EXTRA_PYTHON
cd ../..
export PYTHONPATH=${EXTRA_PYTHON}%{python3_sitelib}:$PYTHONPATH
%endif

%if 0%{?fedora}
%pyproject_wheel
%else
%py3_build
%endif


%install

%if %{with rocm}
export USE_ROCM=ON
export USE_ROCM_CK=OFF
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`

# pytorch uses clang, not hipcc
export HIP_CLANG_PATH=%{rocmllvm_bindir}
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%endif

%if 0%{?fedora}
%pyproject_install
%pyproject_save_files '*torch*'
%else
# In 2.9+ the 'setup.py install' command is gone
# + /usr/bin/python3 setup.py install -O1 --skip-build --root /builddir/build/BUILDROOT/python-torch-2.9.1-1.el10.x86_64 --prefix /usr
# WARNING: Redirecting 'python setup.py install' to 'pip install . -v --no-build-isolation', for more inf
# So we can no longer use py3_install
# The replacement from pytorch does not map arguements
# cobble together a new install based on pyproject_install

PYTHONPATH=$PWD/extra-python/%{python3_sitelib}:$PYTHONPATH \
 TMPDIR="$PWD/build" \
 %{__python3} -m pip install --root %{buildroot} --prefix %{_prefix} --no-deps --disable-pip-version-check --progress-bar off --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --no-build-isolation .

%endif

%check
# Not working yet
# pyproject_check_import torch

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md 
%{_bindir}/torchrun
%if 0%{?rhel}
%{_bindir}/torchfrtrace
%endif
%{python3_sitearch}/%{pypi_name}*
%{python3_sitearch}/functorch

%changelog
%autochangelog

