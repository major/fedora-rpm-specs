%global pypi_name torch

# Where the src comes from
%global forgeurl https://github.com/pytorch/pytorch

# So pre releases can be tried
%bcond_without gitcommit
%if %{with gitcommit}
# git tag v2.3.0-rc2
%global commit0 6a89a753b1556fe8558582c452fdba083f6ec01a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240313
%else
%global commit0 975d4284250170602db60adfda5eb1664a3b8acc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240307
%endif
%global pypi_version 2.3.0

# For -test subpackage
# suitable only for local testing
# Install and do something like
#   export LD_LIBRARY_PATH=/usr/lib64/python3.12/site-packages/torch/lib
#   /usr/lib64/python3.12/site-packages/torch/bin/test_api, test_lazy
%bcond_with test

%ifarch x86_64
%if 0%{?fedora}
%bcond_without rocm
%else
%bcond_with rocm
%endif
%endif
# hipblaslt is in development
%bcond_with hipblaslt
# Which families gpu build for
%global rocm_gpu_list gfx8 gfx9 gfx10 gfx11
%global rocm_default_gpu default
%bcond_without rocm_loop

# For testing caffe2
%if 0%{?fedora}
%bcond_without caffe2
%else
%bcond_with caffe2
%endif

# For testing distributed
%bcond_with distributed

# For testing openvs
%bcond_with opencv

# For testing cuda
%ifarch x86_64
%bcond_with cuda
%endif

Name:           python-%{pypi_name}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        PyTorch AI/ML framework
# See license.txt for license details
License:        BSD-3-Clause AND BSD-2-Clause AND 0BSD AND Apache-2.0 AND MIT AND BSL-1.0 AND GPL-3.0-or-later AND Zlib

URL:            https://pytorch.org/
%if %{with gitcommit}
Source0:        %{forgeurl}/archive/%{commit0}/pytorch-%{shortcommit0}.tar.gz
Source100:        pyproject.toml
%else
Source0:        %{forgeurl}/archive/%{commit0}/pytorch-%{shortcommit0}.tar.gz
Source100:        pyproject.toml
%endif
Source1:        https://github.com/google/flatbuffers/archive/refs/tags/v23.3.3.tar.gz
Source2:        https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz

%if %{with cuda}
%global cuf_ver 1.1.2
Source10:       https://github.com/NVIDIA/cudnn-frontend/archive/refs/tags/v%{cuf_ver}.tar.gz
%global cul_ver 3.4.1
Source11:       https://github.com/NVIDIA/cutlass/archive/refs/tags/v%{cul_ver}.tar.gz
%endif

Patch0:        0001-no-third_party-foxi.patch
Patch1:        0001-no-third_party-fmt.patch
Patch2:        0001-no-third_party-FXdiv.patch
Patch3:        0001-Stub-in-kineto-ActivityType.patch
Patch5:        0001-disable-submodule-search.patch

%if %{with caffe2}
Patch6:        0001-reenable-foxi-linking.patch
%endif

# ROCm patches
# https://github.com/pytorch/pytorch/pull/120551
Patch100:      0001-Optionally-use-hipblaslt.patch
Patch101:      0001-cuda-hip-signatures.patch
Patch102:      0001-silence-an-assert.patch
Patch103:      0001-can-not-use-with-c-files.patch
Patch104:      0001-use-any-hip.patch
Patch105:      0001-disable-use-of-aotriton.patch

ExclusiveArch:  x86_64 aarch64
%global toolchain gcc
%global _lto_cflags %nil

BuildRequires:  cmake
BuildRequires:  cpuinfo-devel
BuildRequires:  eigen3-devel
BuildRequires:  fmt-devel
BuildRequires:  foxi-devel
BuildRequires:  FP16-devel
BuildRequires:  fxdiv-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
%if %{with distributed}
BuildRequires:  gloo-devel
%endif
BuildRequires:  ninja-build
BuildRequires:  onnx-devel
BuildRequires:  libomp-devel
BuildRequires:  openblas-devel
BuildRequires:  pocketfft-devel
BuildRequires:  protobuf-devel
BuildRequires:  pthreadpool-devel
BuildRequires:  psimd-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pyyaml
BuildRequires:  python3-typing-extensions
BuildRequires:  sleef-devel
BuildRequires:  valgrind-devel
BuildRequires:  xnnpack-devel = 0.0^git20240229.fcbf55a

BuildRequires:  python3-devel
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(sphinx)

%if 0%{?fedora}
BuildRequires:  python3-pybind11
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(sympy)
%endif

%if %{with rocm}
BuildRequires:  hipblas-devel
%if %{with hipblaslt}
BuildRequires:  hipblaslt-devel
%endif
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  hipsolver-devel
BuildRequires:  miopen-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocfft-devel
%if %{with distributed}
BuildRequires:  rccl-devel
%endif
BuildRequires:  rocprim-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocthrust-devel
BuildRequires:  roctracer-devel

Requires:       rocm-rpm-macros-modules
%endif

%if %{with opencv}
BuildRequires:  opencv-devel
%endif


%if %{with test}
BuildRequires:  google-benchmark-devel
%endif

# Apache-2.0
Provides:       bundled(flatbuffers) = 22.3.3
# MIT
Provides:       bundled(miniz) = 2.1.0
Provides:       bundled(pybind11) = 2.11.1


%description
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

%if %{with rocm}
%package -n python3-%{pypi_name}-rocm-gfx8
Summary:        %{name} for ROCm gfx8

%description -n python3-%{pypi_name}-rocm-gfx8
%{summary}

%package -n python3-%{pypi_name}-rocm-gfx9
Summary:        %{name} for ROCm gfx9

%description -n python3-%{pypi_name}-rocm-gfx9
%{summary}

%package -n python3-%{pypi_name}-rocm-gfx10
Summary:        %{name} for ROCm gfx10

%description -n python3-%{pypi_name}-rocm-gfx10
%{summary}

%package -n python3-%{pypi_name}-rocm-gfx11
Summary:        %{name} for ROCm gfx11

%description -n python3-%{pypi_name}-rocm-gfx11
%{summary}

%endif

%if %{with test}
%package -n python3-%{pypi_name}-test
Summary:        Tests for %{name}
Requires:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}

%description -n python3-%{pypi_name}-test
%{summary}
%endif


%prep

%autosetup -p1 -n pytorch-%{commit0}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Overwrite with a git checkout of the pyproject.toml
cp %{SOURCE100} .

tar xf %{SOURCE1}
cp -r flatbuffers-23.3.3/* third_party/flatbuffers/

tar xf %{SOURCE2}
cp -r pybind11-2.11.1/* third_party/pybind11/

%if %{with cuda}
tar xf %{SOURCE10}
cp -r cudnn-frontend-%{cuf_ver}/* third_party/cudnn_frontend/
tar xf %{SOURCE11}
cp -r cutlass-%{cul_ver}/* third_party/cutlass/
%endif

%if %{with opencv}
# Reduce requirements, *FOUND is not set 
sed -i -e 's/USE_OPENCV AND OpenCV_FOUND AND USE_FFMPEG AND FFMPEG_FOUND/USE_OPENCV AND USE_FFMPEG/' caffe2/video/CMakeLists.txt
sed -i -e 's/USE_OPENCV AND OpenCV_FOUND/USE_OPENCV/' caffe2/image/CMakeLists.txt
sed -i -e 's/STATUS/FATAL/' caffe2/image/CMakeLists.txt
%endif

%if 0%{?rhel}
# In RHEL but too old
sed -i -e '/typing-extensions/d' setup.py
# Need to pip these
sed -i -e '/sympy/d' setup.py
sed -i -e '/fsspec/d' setup.py
%endif

# A new dependency
# Connected to USE_FLASH_ATTENTION, since this is off, do not need it
sed -i -e '/aotriton.cmake/d' cmake/Dependencies.cmake

# Release comes fully loaded with third party src
# Remove what we can
#
# For 2.1 this is all but miniz-2.1.0
# Instead of building as a library, caffe2 reaches into
# the third_party dir to compile the file.
# mimiz is licensed MIT
# https://github.com/richgel999/miniz/blob/master/LICENSE
mv third_party/miniz-2.1.0 .
#
# setup.py depends on this script
mv third_party/build_bundled.py .

# Need the just untarred flatbuffers/flatbuffers.h
mv third_party/flatbuffers .

mv third_party/pybind11 .

%if %{with cuda}
mv third_party/cudnn_frontend .
mv third_party/cutlass .
%endif

%if %{with test}
mv third_party/googletest .
%endif

# Remove everything
rm -rf third_party/*
# Put stuff back
mv build_bundled.py third_party
mv miniz-2.1.0 third_party
mv flatbuffers third_party
mv pybind11 third_party

%if %{with cuda}
mv cudnn_frontend third_party
mv cutlass third_party
%endif

%if %{with test}
mv googletest third_party
%endif

#
# Fake out pocketfft, and system header will be used
mkdir third_party/pocketfft
#
# Use the system valgrind headers
mkdir third_party/valgrind-headers
cp %{_includedir}/valgrind/* third_party/valgrind-headers

# Remove unneeded OpenCL files that confuse the lincense scanner
rm caffe2/contrib/opencl/OpenCL/cl.hpp
rm caffe2/mobile/contrib/libopencl-stub/include/CL/*.h
rm caffe2/mobile/contrib/libopencl-stub/include/CL/*.hpp

%if %{with rocm}
# hipify
./tools/amd_build/build_amd.py
# Fedora installs to /usr/include, not /usr/include/rocm-core
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/hip/tunable/TunableGemm.h
%endif

%if %{with cuda}
# build complains about not being able to build -pie without -fPIC
sed -i -e 's@string(APPEND CMAKE_CUDA_FLAGS " -D_GLIBCXX_USE_CXX11_ABI=${GLIBCXX_USE_CXX11_ABI}")@string(APPEND CMAKE_CUDA_FLAGS " -fPIC -D_GLIBCXX_USE_CXX11_ABI=${GLIBCXX_USE_CXX11_ABI}")@' CMakeLists.txt
%endif

%build

#
# Control the number of jobs
#
# The build can fail if too many threads exceed the physical memory
# So count core and and memory and increase the build memory util the build succeeds
#
# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
%if %{with cuda}
BUILD_MEM=4
%else
BUILD_MEM=2
%endif
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

export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_NVFUSER=OFF
export BUILD_SHARED_LIBS=ON
export BUILD_TEST=OFF
export CMAKE_BUILD_TYPE=RelWithDebInfo
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_DISTRIBUTED=OFF
export USE_CUDA=OFF
export USE_FBGEMM=OFF
export USE_FLASH_ATTENTION=OFF
export USE_GOLD_LINKER=OFF
export USE_ITT=OFF
export USE_KINETO=OFF
export USE_LITE_INTERPRETER_PROFILER=OFF
export USE_LITE_PROTO=OFF
export USE_MKLDNN=OFF
export USE_NCCL=OFF
export USE_NNPACK=OFF
export USE_NUMPY=ON
export USE_OPENMP=ON
export USE_PYTORCH_QNNPACK=OFF
export USE_QNNPACK=OFF
export USE_ROCM=OFF
export USE_SYSTEM_CPUINFO=ON
export USE_SYSTEM_SLEEF=ON
export USE_SYSTEM_EIGEN_INSTALL=ON
export USE_SYSTEM_FP16=ON
export USE_SYSTEM_PTHREADPOOL=ON
export USE_SYSTEM_PSIMD=ON
export USE_SYSTEM_FXDIV=ON
export USE_SYSTEM_ONNX=ON
export USE_SYSTEM_XNNPACK=ON
export USE_SYSTEM_PYBIND11=OFF
export USE_SYSTEM_LIBS=OFF
export USE_TENSORPIPE=OFF
export USE_XNNPACK=ON

%if %{with caffe2}
export BUILD_CAFFE2=ON
%endif

%if %{with cuda}
%if %{without rocm}
export CUDACXX=/usr/local/cuda/bin/nvcc
export CPLUS_INCLUDE_PATH=/usr/local/cuda/include
export USE_CUDA=ON
%endif
%endif

%if %{with distributed}
export USE_DISTRIBUTED=ON
%endif

%if %{with opencv}
export USE_OPENCV=ON
%endif

%if %{with test}
export BUILD_TEST=ON
%endif

# Why we are using py3_ vs pyproject_
#
# current pyproject problem with mock
# + /usr/bin/python3 -Bs /usr/lib/rpm/redhat/pyproject_wheel.py /builddir/build/BUILD/pytorch-v2.1.0/pyproject-wheeldir
# /usr/bin/python3: No module named pip
# Adding pip to build requires does not fix
#
# See BZ 2244862


%if %{with rocm}

export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode

gpu=%{rocm_default_gpu}
module load rocm/$gpu
export PYTORCH_ROCM_ARCH=$ROCM_GPUS
%py3_build
mv build build-${gpu}
module purge

%if %{with rocm_loop}
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    export PYTORCH_ROCM_ARCH=$ROCM_GPUS
    %py3_build
    mv build build-${gpu}
    module purge
done
%endif

%else

%py3_build

%endif

%install

%if %{with rocm}

export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode

gpu=%{rocm_default_gpu}
module load rocm/$gpu
export PYTORCH_ROCM_ARCH=$ROCM_GPUS
mv build-${gpu} build
%py3_install
mv build build-${gpu}
module purge

%if %{with rocm_loop}
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    export PYTORCH_ROCM_ARCH=$ROCM_GPUS
    mv build-${gpu} build
    # need to customize the install location, so replace py3_install
    %{__python3} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} --prefix /usr/lib64/rocm/${gpu} %{?*}
    rm -rfv %{buildroot}/usr/lib/rocm/${gpu}/bin/__pycache__
    mv build build-${gpu}
    module purge
done
%endif

%else
%py3_install

%endif

# Do not remote the empty files


%files -n python3-%{pypi_name} 
%license LICENSE
%doc README.md 
%{_bindir}/convert-caffe2-to-onnx
%{_bindir}/convert-onnx-to-caffe2
%{_bindir}/torchrun
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-*.egg-info
%{python3_sitearch}/functorch
%{python3_sitearch}/torchgen
%if %{with caffe2}
%{python3_sitearch}/caffe2
%endif

%if %{with rocm}
%files -n python3-%{pypi_name}-rocm-gfx8
%{_libdir}/rocm/gfx8/bin/*
%{_libdir}/rocm/gfx8/lib64/*

%files -n python3-%{pypi_name}-rocm-gfx9
%{_libdir}/rocm/gfx9/bin/*
%{_libdir}/rocm/gfx9/lib64/*

%files -n python3-%{pypi_name}-rocm-gfx10
%{_libdir}/rocm/gfx10/bin/*
%{_libdir}/rocm/gfx10/lib64/*

%files -n python3-%{pypi_name}-rocm-gfx11
%{_libdir}/rocm/gfx11/bin/*
%{_libdir}/rocm/gfx11/lib64/*
%endif

%changelog
%autochangelog

