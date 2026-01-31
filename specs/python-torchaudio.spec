%global pypi_name torchaudio

%bcond_with gitcommit
%if %{with gitcommit}
# The release/2.3.0
%global commit0 17a70815259222570feb071034acd7bae2adc019
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240318
%global pypi_version 2.3.0
%else
%global pypi_version 2.9.0
%endif

%global desc %{expand: \
The aim of torchaudio is to apply PyTorch to the audio domain. By supporting
PyTorch, torchaudio follows the same philosophy of providing strong GPU
acceleration, having a focus on trainable features through the autograd
system, and having consistent style (tensor names and dimension names).
Therefore, it is primarily a machine learning library and not a general
signal processing library. The benefits of PyTorch can be seen in torchaudio
through having all the computations be through PyTorch operations which
makes it easy to use and feel like a natural extension. }

%ifarch x86_64
%if 0%{?fedora}
%bcond_without rocm
%else
%bcond_with rocm
%endif
%endif

# torch toolchain
%global toolchain gcc

Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        %autorelease
Summary:        Audio signal processing, powered by PyTorch

License:        BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND MIT
URL:            https://github.com/pytorch/audio
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/audio-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/audio-v%{version}.tar.gz
%endif

# Limit to these because that is what torch is on
# failing to build 1/29/26
# ExclusiveArch:  aarch64 x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ffmpeg-free
BuildRequires:  ffmpeg-free-devel
BuildRequires:  ninja-build
BuildRequires:  protobuf-devel
BuildRequires:  sox-devel

%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  hipsparselt-devel
BuildRequires:  hipsolver-devel
BuildRequires:  miopen-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocprim-static
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocm-smi-devel
BuildRequires:  rocsolver-devel
BuildRequires:  rocthrust-devel
BuildRequires:  roctracer-devel
%endif

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(torch)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        Audio signal processing, powered by PyTorch

%description -n python3-%{pypi_name}
%{desc}

%prep
%if %{with gitcommit}
%autosetup -p1 -n audio-%{commit0}
%else
%autosetup -p1 -n audio-%{version}
%endif

rm -rf third_party/*

%generate_buildrequires
%pyproject_buildrequires

%build
# Building uses python3_sitearch/torch/utils/cpp_extension.py
# cpp_extension.py does a general linking with all the pytorch libs which
# leads warnings being reported by rpmlint.
#
# pyproject_wheel tries to use pypi's cmake, revert back to py3_build

export BUILD_SOX=OFF
export USE_FFMPEG=OFF
%if %{with rocm}
export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode

export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%pyproject_wheel

%else

%pyproject_wheel

%endif

%install

%if %{with rocm}

export USE_ROCM=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode

export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%pyproject_install
%pyproject_save_files %{pypi_name}

%else
%pyproject_install
%pyproject_save_files %{pypi_name}

%endif

# exec permission
for f in `find %{buildroot} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done

%files -n python3-%{pypi_name}  -f %{pyproject_files}
%license LICENSE
%doc README.md 

%changelog
%autochangelog
