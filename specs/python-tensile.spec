%if 0%{?suse_version}
%{?!python_module:%define python_module() python3-%{**}}
%else
%global python_files -n python3-tensile-devel
%define python_sitelib %python3_sitelib
%define python_subpackages %nil
%define python_alternative %nil
%endif

%global upstreamname Tensile

%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%if 0%{?suse_version}
Name:           python-tensile-devel
%else
Name:           python-tensile
%endif
Version:        %{rocm_version}
Release:        10%{?dist}
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

URL:            https://github.com/ROCmSoftwarePlatform/Tensile
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

Patch1:         0001-Adding-gfx1151-to-6.2-2026.patch
Patch2:         0002-More-gfx1151.patch
Patch3:         0003-Add-gfx1103.patch
Patch4:         0004-Add-gfx1035.patch
Patch5:         0005-Add-gfx1152.patch
Patch6:         0006-Add-gfx1150.patch
Patch7:         0001-Handle-a-missing-joblib.patch
Patch8:         0001-serialize-reading-logic-files.patch

%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif

%if 0%{?suse_version}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
Requires:       hipcc
Requires:       rocminfo
%if %{suse_version} >= 1699
Requires:       %{python_module joblib}
%endif
Requires:       %{python_module msgpack}
Requires:       %{python_module PyYAML}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%endif

# Straight python, but only usable for ROCm which is only on x86_64
BuildArch:      noarch
ExclusiveArch:  x86_64
%python_subpackages

%description
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%if 0%{?fedora} || 0%{?rhel}
# There are headers and code as part of the code generation.
# This make rpm checkers unhappy
%package -n python3-tensile-devel
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

Requires:       cmake-filesystem
Requires:       hipcc
Requires:       rocminfo
%if 0%{?fedora}
Requires:       python3dist(joblib)
Requires:       python3dist(msgpack)
%endif
Requires:       python3dist(pyyaml)

%description -n python3-tensile-devel
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.
%endif

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

# Reduce requirements
sed -i -e '/joblib/d' requirements.*
sed -i -e '/rich/d' requirements.*
sed -i -e '/msgpack/d' requirements.*

%build
%py3_build
%{?python_build: %python_build}

%install
%py3_install
%{?python_install: %python_install}

mkdir -p %{buildroot}%{_datadir}/cmake/Tensile
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/Tensile/
rm -rf %{buildroot}%{_prefix}/cmake

# Do not distribute broken bins
rm %{buildroot}%{_bindir}/tensile*

# Do not distribute tests
rm -rf %{buildroot}%{python3_sitelib}/%{upstreamname}/Tests

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

# rm hard links and replace
rm %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/*.cmake
mv %{buildroot}%{_datadir}/cmake/Tensile/*.cmake %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/

%if 0%{?suse_version}
%python_clone -a %{buildroot}%{_bindir}/Tensile
%python_clone -a %{buildroot}%{_bindir}/TensileBenchmarkCluster
%python_clone -a %{buildroot}%{_bindir}/TensileCreateLibrary
%python_clone -a %{buildroot}%{_bindir}/TensileGetPath
%python_clone -a %{buildroot}%{_bindir}/TensileRetuneLibrary

%post
%python_install_alternative Tensile
%python_install_alternative TensileBenchmarkCluster
%python_install_alternative TensileCreateLibrary
%python_install_alternative TensileGetPath
%python_install_alternative TensileRetuneLibrary

%postun
%python_uninstall_alternative Tensile
%python_uninstall_alternative TensileBenchmarkCluster
%python_uninstall_alternative TensileCreateLibrary
%python_uninstall_alternative TensileGetPath
%python_uninstall_alternative TensileRetuneLibrary
%endif


%files %{python_files}
%dir %{python_sitelib}/%{upstreamname}
%dir %{python_sitelib}/%{upstreamname}*.egg-info
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/Tensile
%python_alternative %{_bindir}/TensileBenchmarkCluster
%python_alternative %{_bindir}/TensileCreateLibrary
%python_alternative %{_bindir}/TensileGetPath
%python_alternative %{_bindir}/TensileRetuneLibrary
%{python_sitelib}/%{upstreamname}/*
%{python_sitelib}/%{upstreamname}*.egg-info/*

%changelog
* Thu Feb 27 2025 Tom Rix <Tom.Rix@amd.com> 6.3.0-10
- Fix RHEL

* Wed Feb 26 2025 Tom Rix <Tom.Rix@amd.com> 6.3.0-9
- Handle missing joblib

* Thu Feb 20 2025 Tom Rix <Tom.Rix@amd.com> 6.3.0-8
- Remove python-rich suse requires

* Wed Feb 19 2025 Tom Rix <Tom.Rix@amd.com> 6.3.0-7
- Fix cmake links in TW

* Tue Feb 18 2025 Christian Goll <cgoll@suse.com> 6.3.0-6
- Fix TW

* Fri Feb 14 2025 Tom Rix <Tom.Rix@amd.com> 6.3.0-5
- Fix SLE 15.6

* Sat Feb 8 2025 Tom Rix <Tom.Rix@amd.com> 6.3.0-4
- Remove check
- Reduce files
- Cleanup URL

* Thu Jan 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- Add gfx1150

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- Add gfx1152

* Fri Dec 6 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3.0


