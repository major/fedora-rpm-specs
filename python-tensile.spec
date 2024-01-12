%global upstreamname Tensile

%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# This doesn't work quite yet:
# Also depends on local gpu hw
%bcond_with check

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

Name:           python-tensile
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

Url:            https://github.com/ROCmSoftwarePlatform/Tensile
License:        MIT
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  python3-devel

%if %{with check}
# Some of these might not be needed
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
%endif

# Straight python, but only usable for ROCm which is only on x86_64
BuildArch:      noarch
ExclusiveArch:  x86_64

%description
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%package -n python3-tensile
Summary:        %{summary}
Requires:       cmake-filesystem

%description -n python3-tensile
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

#Fix a few things:
chmod 755 Tensile/Configs/miopen/convert_cfg.py
%py3_shebang_fix Tensile/Configs/miopen/convert_cfg.py
%py3_shebang_fix Tensile/Tests/create_tests.py

# I'm assuming we don't need these:
rm -r %{upstreamname}/Configs/miopen/archives

# hack where TensileGetPath is located
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g' Tensile/cmake/TensileConfig.cmake

# Use /usr instead of /opt/rocm for prefix
sed -i -e 's@opt/rocm@usr@g' Tensile/Common.py
sed -i -e 's@opt/rocm@usr@g' Tensile/Tests/yaml_only/test_config.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{upstreamname}

mkdir -p %{buildroot}%{_datadir}/cmake/Tensile
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/Tensile/
rm -rf %{buildroot}%{_prefix}/cmake

# Do not distribute broken bins
rm %{buildroot}%{_bindir}/tensile*

%check
%if %{with check}
%tox
%endif

%files -n python3-tensile -f %{pyproject_files}
%doc README.md
%license LICENSE.md
%{_bindir}/%{upstreamname}*
%{_datadir}/cmake/Tensile
%exclude %{python3_sitelib}/%{upstreamname}/Tests

%changelog
%autochangelog
