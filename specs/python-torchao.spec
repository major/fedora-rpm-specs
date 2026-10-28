%global pypi_name torchao
# Broken due to pytorch issues
%global with_tests 0

Name:          python-%{pypi_name}
Version:       0.18.0
Release:       2%{?dist}
Summary:       PyTorch native quantization and sparsity for training and inference
License:       BSD-3-Clause
URL:           https://pytorch.org/ao
Source0:       https://github.com/pytorch/ao/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

# pytorch built arches
ExclusiveArch: aarch64 x86_64
BuildArch: noarch
BuildRequires: gcc gcc-c++
BuildRequires: python3-cmake
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-torch
# For check
%if 0%{?with_tests}
BuildRequires: python3-pytest
%endif

%global _description %{expand:
PyTorch native quantization and sparsity for training and inference.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n ao-%{version}
# works around the git submodule checkout
mkdir -p torchao/experimental/third-party/cutlass

%generate_buildrequires
export USE_CPP=0
export USE_CUDA=0
%ifarch aarch64
export TORCHAO_BUILD_CPU_AARCH64=1
export TORCHAO_BUILD_KLEIDIAI=0
# Newer aarch64 cores
export TORCHAO_ENABLE_ARM_NEON_DOT=0
export TORCHAO_ENABLE_ARM_I8MM=0
%endif
%if 0%{?with_tests}
%pyproject_buildrequires -r
%else
%pyproject_buildrequires
%endif

%build
export USE_CUDA=0
export USE_CPP=0
%ifarch aarch64
export TORCHAO_BUILD_CPU_AARCH64=1
export TORCHAO_BUILD_KLEIDIAI=0
# Newer aarch64 cores
export TORCHAO_ENABLE_ARM_NEON_DOT=0
export TORCHAO_ENABLE_ARM_I8MM=0
%endif
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%if 0%{?with_tests}
%check
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitelib}/test/

%changelog
* Fri Oct 23 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18.0-2
- Minor spec updates

* Wed Sep 23 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18.0-1
- Initial package
