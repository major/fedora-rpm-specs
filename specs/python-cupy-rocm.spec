%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

Name:           python-cupy-rocm
Version:        14.1.1
Release:        %autorelease
Summary:        NumPy & SciPy for GPU

License:        MIT AND BSD-3-Clause AND Apache-2.0 AND BSL-1.0 AND BSD-2-Clause
# LICENSE : MIT
# Is the main license for the project
#
# docs/source/license.rst
# Is a attribution breakdown of where parts of the cupy project came from
#   NumPy - BSD-3-Clause
#   SciPy - BSD-3-Clause
#     cupyx/scipy/*
#   cuSignal - MIT
#     cupyx/signal/*
#
# LICENSE.thrust : Apache-2.0 AND BSL-1.0 AND BSD-2-Clause
# Covers these files
# cupy/_core/include/cupy/complex/*
#
# LICENSE.jitify : BSD-3-Clause
# Covers this file
# cupy/_core/include/cupy/_jitify/jitify.hpp
#
# LICENSE.random : BSD-3-Clause AND MIT
# covers this file cupy/random/_kernels.py
#
# LICENSE.ndimage : MIT
# covers cupyx/scipy/ndimage/cuda/*.h
#
# Misc file not covered by the LICENSE.* files
# cupyx/scipy/special/_digamma.py BSL-1.0
#

URL:            https://cupy.dev/
Source0:        %{pypi_source cupy}
# Upstream for both of these license files
# https://github.com/cupy/cupy/issues/9387
#
# Files in _core/include/cupy/complex come from thrust
# Here is its location in the devel project where thrust is a submodule
# https://github.com/NVIDIA/cccl/blob/3a388b7b01512d48474b98389a3e776c8d8f817a/thrust/LICENSE
Source1:        LICENSE.thrust
# The license listed from
# cupy/random/_kernels.py
# Here is its location in the devel project
# https://github.com/cupy/cupy/blob/main/cupy/random/LICENSE
Source2:        LICENSE.random

# Only x86_64 works right now:
ExclusiveArch:  x86_64

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(fastrlock)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

BuildRequires:  hipblas-devel
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  hipsolver-devel
BuildRequires:  rccl-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocsolver-devel
BuildRequires:  rocsparse-devel
BuildRequires:  roctracer-devel
BuildRequires:  rocthrust-devel

# cupy/_core/include/cupy/_jitify/jitify.hpp
Provides:       bundled(jitify) = 0.9
# cupy/_core/include/cupy/_dlpack/dlpack.h
Provides:       bundled(dlpack) = 1.0
# cupy/_core/include/cupy/complex/*
Provides:       bundled(thrust) = 3.1.2
# cupy/_core/include/cupy/xsf/*
Provides:       bundled(xsf) = 0.1.5
# cupy/_core/include/cupy/xsf/third_party/kokkos/mdspan.hpp
Provides:       bundled(mdspan) = 4.0
# cupyx/scipy/ndimage/cuda/pba_kernels_*.h
Provides:       bundled(pba)

%global _description %{expand:
CuPy is a NumPy/SciPy-compatible array library for GPU-accelerated
computing with Python. CuPy acts as a drop-in replacement to run
existing NumPy/SciPy code on AMD ROCm platforms.}

%description %_description

%package -n     python3-cupy-rocm
Summary:        %{summary}

# cupy builds hip/rocm on the fly
# so the build requires is also the requires
Requires:       hipblas-devel
Requires:       hipcub-devel
Requires:       hipfft-devel
Requires:       hiprand-devel
Requires:       hipsparse-devel
Requires:       hipsolver-devel
Requires:       rccl-devel
Requires:       rocblas-devel
Requires:       rocrand-devel
Requires:       rocfft-devel
Requires:       rocm-comgr-devel
Requires:       rocm-hip-devel
Requires:       rocm-runtime-devel
Requires:       rocsolver-devel
Requires:       rocsparse-devel
Requires:       roctracer-devel
Requires:       rocthrust-devel

%description -n python3-cupy-rocm %_description

%prep
%autosetup -p1 -n cupy-%{version}

# Do not be specific on cython version
sed -i -e 's@Cython>=3.1,<3.2@Cython@' pyproject.toml

# Rename license files so they can be referenced in files
# BSD-3-Clause
mv cupy/_core/include/cupy/_jitify/LICENSE LICENSE.jitify
# Apache-2.0
mv cupy/_core/include/cupy/_dlpack/LICENSE LICENSE.dlpack
# MIT
mv cupyx/scipy/ndimage/cuda/LICENSE        LICENSE.ndimage
# Apache-2.0 AND BSL-1.0 AND BSD-2-Clause
cp -p %{SOURCE1}                           LICENSE.thrust
# BSD-3-Clause AND MIT
cp -p %{SOURCE2}                           LICENSE.random

# cccl has this license clause
# 3. LIMITATIONS. Your license to use the SOFTWARE is restricted as follows:
# a.    The SOFTWARE is licensed for you to develop applications only for use in systems with NVIDIA GPUs.
# so remove cccl
rm -rf cupy/_core/include/cupy/_cccl/*
# cuda-* also not needed
rm -rf cupy/_core/include/cupy/_cuda/*

# remove tests to simplify licenses
rm -rf tests

# Use hipcc
sed -i -e "s@backend = 'hiprtc' if backend == 'nvrtc' else 'hipcc'@backend = 'hipcc'@" cupy/cuda/compiler.py

%generate_buildrequires

# rpmbuild complains, no rpaths in the install
export CUPY_INSTALL_NO_RPATH=1
# do not use cuda
export CUPY_USE_CUDA_PYTHON=0
# do not use the cuda stub headers to build
export CUPY_INSTALL_USE_STUB=0
# use the hip/rocm runtime
export CUPY_INSTALL_USE_HIP=1
# some help finding rocm, it's not in /opt/rocm
export ROCM_HOME=/usr
# HCC_AMDGPU_TARGET has a ',' seperator, not a ';' seperator, do the switch
export HCC_AMDGPU_TARGET=`echo %{rocm_gpu_list_default} | tr ';' ',' `
export CXX=/usr/lib64/rocm/llvm/bin/amdclang++
export CC=/usr/lib64/rocm/llvm/bin/amdclang

%pyproject_buildrequires

%build

# rpmbuild complains, no rpaths in the install
export CUPY_INSTALL_NO_RPATH=1
# do not use cuda
export CUPY_USE_CUDA_PYTHON=0
# do not use the cuda stub headers to build
export CUPY_INSTALL_USE_STUB=0
# use the hip/rocm runtime
export CUPY_INSTALL_USE_HIP=1
# some help finding rocm, it's not in /opt/rocm
export ROCM_HOME=/usr
# HCC_AMDGPU_TARGET has a ',' seperator, not a ';' seperator, do the switch
export HCC_AMDGPU_TARGET=`echo %{rocm_gpu_list_default} | tr ';' ',' `
export CXX=/usr/lib64/rocm/llvm/bin/amdclang++
export CC=/usr/lib64/rocm/llvm/bin/amdclang

# Speed up the build by using -parallel-jobs option for building hip
# There are ~20 gpu targets
# Most builders will have between 4 and 32 cores
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
export HIPCC_COMPILE_FLAGS_APPEND="-parallel-jobs=${HIP_JOBS} --offload-compress"

%pyproject_wheel

%install

%pyproject_install

# Clean up dupes
%fdupes %{buildroot}%{_prefix}

# python3-cupy.x86_64: E: non-executable-script
#  /usr/lib64/python3.14/site-packages/cupyx/tools/install_library.py 644 /usr/bin/env python
# The purpose of this script is..
#  This script will also be used as a standalone script when building wheels.
# Import check complains, just remove the script line
sed -i '1d' %{buildroot}%{python3_sitearch}/cupyx/tools/install_library.py
# similar for _generate_wheel_metadata.py
sed -i '1d' %{buildroot}%{python3_sitearch}/cupyx/tools/_generate_wheel_metadata.py

%pyproject_save_files 'cupy*'

%check
%pyproject_check_import

%files -n python3-cupy-rocm -f %{pyproject_files}
%license LICENSE.jitify LICENSE.dlpack LICENSE.ndimage
%license docs/source/license.rst
# python3-cupy.x86_64: E: zero-length /usr/lib64/python3.14/site-packages/cupy/_util.pyi
%exclude %{python3_sitearch}/cupy/_util.pyi


%changelog
%autochangelog
