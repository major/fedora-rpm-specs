%global upstreamname Tensile

%global rocm_release 6.3
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
Release:        3%{?dist}
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

Url:            https://github.com/ROCmSoftwarePlatform/Tensile
License:        MIT
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

Patch1:         0001-Adding-gfx1151-to-6.2-2026.patch
Patch2:         0002-More-gfx1151.patch
Patch3:         0003-Add-gfx1103.patch
Patch4:         0004-Add-gfx1035.patch
Patch5:         0005-Add-gfx1152.patch
Patch6:         0006-Add-gfx1150.patch

#Patch0:         0001-enable-gfx1103-for-Tensile.patch
# In 6.1, work around  this error
# Tensile::FATAL: Cached asm caps differ from derived asm caps for (9, 0, 10)
# Patch1:         0001-tensile-workaround-cache-problem.patch

BuildRequires:  fdupes
BuildRequires:  python3-devel
%if 0%{?suse_version}
# TW
BuildRequires:  python311-setuptools
%else
BuildRequires:  python3dist(setuptools)
%endif

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

# There are headers and code as part of the code generation.
# This make rpm checkers unhappy
%package -n python3-tensile-devel
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs
%if 0%{?fedora}
Requires:       cmake-filesystem
%endif
Requires:       hipcc
Requires:       rocminfo
%if 0%{?suse_version}
# TW
Requires:       python311-joblib
Requires:       python311-msgpack
Requires:       python311-PyYAML
%else
Requires:       python3dist(joblib)
Requires:       python3dist(msgpack)
Requires:       python3dist(pyyaml)
%endif
Provides:       python3-tensile

%description -n python3-tensile-devel
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.


%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

#Fix a few things:
chmod 755 Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Tests/create_tests.py
sed -i -e 's@bin/env python3@bin/python3@' Tensile/bin/Tensile
sed -i -e 's@bin/env python3@bin/python3@' Tensile/bin/TensileCreateLibrary

# I'm assuming we don't need these:
rm -r %{upstreamname}/Configs/miopen/archives

# hack where TensileGetPath is located
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g' Tensile/cmake/TensileConfig.cmake

# Use /usr instead of /opt/rocm for prefix
sed -i -e 's@opt/rocm@usr@g' Tensile/Common.py
sed -i -e 's@opt/rocm@usr@g' Tensile/Tests/yaml_only/test_config.py

# Ignora asm cap
sed -i -e 's@globalParameters["IgnoreAsmCapCache"] = False@globalParameters["IgnoreAsmCapCache"] = True@' Tensile/Common.py
sed -i -e 's@arguments["IgnoreAsmCapCache"] = args.IgnoreAsmCapCache@arguments["IgnoreAsmCapCache"] = True@' Tensile/TensileCreateLibrary.py
sed -i -e 's@if not ignoreCacheCheck and derivedAsmCaps@if False and derivedAsmCaps@' Tensile/Common.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/cmake/Tensile
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/Tensile/
rm -rf %{buildroot}%{_prefix}/cmake

# Do not distribute broken bins
rm %{buildroot}%{_bindir}/tensile*

# Do not distribute tests
rm -rf %{buildroot}%{python3_sitelib}/%{upstreamname}/Tests

#Clean up dupes:
%fdupes %{buildroot}%{_prefix}

# rm hard links and replace
rm %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/*.cmake
cp %{buildroot}%{_datadir}/cmake/Tensile/*.cmake %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/

%check
%if %{with check}
%tox
%endif

%files -n python3-tensile-devel
%if 0%{?suse_version}
# Should not have to do this
%dir %{_datadir}/cmake
%endif
%dir %{_datadir}/cmake/Tensile
%dir %{python3_sitelib}/%{upstreamname}
%dir %{python3_sitelib}/%{upstreamname}/__pycache__
%dir %{python3_sitelib}/%{upstreamname}/bin
%dir %{python3_sitelib}/%{upstreamname}/cmake
%dir %{python3_sitelib}/%{upstreamname}/Components
%dir %{python3_sitelib}/%{upstreamname}/Configs
%dir %{python3_sitelib}/%{upstreamname}/CustomKernels
%dir %{python3_sitelib}/%{upstreamname}/Source
%dir %{python3_sitelib}/%{upstreamname}/TensileCreateLib
%dir %{python3_sitelib}/%{upstreamname}/Perf
%dir %{python3_sitelib}/%{upstreamname}/Utilities
%dir %{python3_sitelib}/%{upstreamname}*.egg-info
%doc README.md
%license LICENSE.md
%{_bindir}/%{upstreamname}*
%{_datadir}/cmake/Tensile/*.cmake
%{python3_sitelib}/%{upstreamname}/*.py
%{python3_sitelib}/%{upstreamname}/__pycache__/*
%{python3_sitelib}/%{upstreamname}/bin/*
%{python3_sitelib}/%{upstreamname}/cmake/*
%{python3_sitelib}/%{upstreamname}/Components/*
%{python3_sitelib}/%{upstreamname}/Configs/*
%{python3_sitelib}/%{upstreamname}/CustomKernels/*
%{python3_sitelib}/%{upstreamname}/Perf/*
%{python3_sitelib}/%{upstreamname}/Source/*
%{python3_sitelib}/%{upstreamname}/TensileCreateLib/*
%{python3_sitelib}/%{upstreamname}/Utilities/*
%{python3_sitelib}/%{upstreamname}*.egg-info/*

%changelog
* Thu Jan 16 2026 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- Add gfx1150

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- Add gfx1152

* Fri Dec 6 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3.0


