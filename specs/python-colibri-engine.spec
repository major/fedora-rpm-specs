Name:           python-colibri-engine
Version:        2.0.0
Release:        %autorelease
Summary:        Run frontier MoE models on hardware you already own

# The main license is Apache-2.0
#
# MIT comes from the THIRD_PARTY_NOTICES.md
#
# Portions of `backend_cuda_dsv4.cu`, including the DeepSeek-V4 GPU router
# selection algorithm, are adapted from `ds4_cuda.cu` in the ds4 project:
# https://github.com/antirez/ds4
#
# - DeepGEMM (MIT, Copyright (c) 2025 DeepSeek), from the community sm120 port
#  https://github.com/bvolpato/DeepGEMM branch `sm120-full` @
#  39fb4447a062b418fd08ce17cd308adb28559417, with
#  `c/patches-deepgemm-sm120-msvc.patch` applied at fetch time. License text:
#  `c/third_party/deepgemm/LICENSE` after the fetch.
#
# BSD-3-Clause is reported in the THIRD_PARTY_NOTICES.md
# 
# - NVIDIA CUTLASS / CuTe (BSD-3-Clause), the `third-party/cutlass` submodule of
#  that commit @ f3fde58372d33e9a5650ba7b80fc48b3b49d40c8. License text:
#  `c/third_party/deepgemm/third-party/cutlass/LICENSE.txt` after the fetch.
#
# But the source is not use in the release
#
# Other Apache-2.0 from the THIRD_PARTY_NOTICES.md
#
# Swiftlet qpack installers (`c/tools/qpack_*install*.py`)
#
# Swiftlet (https://github.com/leonickson1/Swiftlet) is licensed under Apache
# License 2.0. This repository's `LICENSE` contains the applicable Apache 2.0
# text.
License:        Apache-2.0 AND MIT

URL:            https://github.com/JustVugg/colibri
Source0:        %{url}/archive/v%{version}/v%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hipcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  rocm-filesystem
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocwmma-devel

%description
%{summary}.

%package -n     python3-colibri-engine
Summary:        Run frontier MoE models on hardware you already own

%description -n python3-colibri-engine
%{summary}.

%prep
%autosetup -p1 -n colibri-%{version}
# Add -g for debuginfo
sed -i -e 's@-O3@-O3 -g@' c/Makefile
# change install location of the real coli
sed -i -e 's@engine_dir = os.path.join(os.path.dirname(here), "c")@engine_dir = "%{_libexecdir}/colibri/c"@' colibri/cli.py

# remove uneeded files to make license check easier
rm c/tools/jev-sdk/package-lock.json
rm -rf web/

%generate_buildrequires
# orcale needs python3-transformers
%pyproject_buildrequires -x convert,bench

%build
# rocwmma can not run all gpus, here is list ..
GPUS="gfx908,gfx90a,gfx942,gfx950,gfx1100,gfx1101,gfx1102,gfx1151,gfx1150,gfx1200,gfx1201"
%make_build HIP=1 ROCM_HOME=/usr HIP_ARCH=${GPUS}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files colibri

mkdir -p %{buildroot}%{_libexecdir}/colibri/c
install c/coli %{buildroot}%{_libexecdir}/colibri/c/
scripts="doctor family_registry image_engine openai_server resource_plan \
         v4_dsml v41_dsml version"
for s in $scripts; do
    install c/${s}.py %{buildroot}%{_libexecdir}/colibri/c/
done
install c/colibri %{buildroot}%{_libexecdir}/colibri/c/
# ERROR   0001: file '/usr/libexec/colibri/c/colibri' contains a standard runpath '/usr/lib' in [/usr/lib]
chrpath -d %{buildroot}%{_libexecdir}/colibri/c/colibri

%check
%pyproject_check_import

%files -n python3-colibri-engine -f %{pyproject_files}
%doc README.it.md  README.md  README.zh-CN.md  README.zh-TW.md GPU_BACKENDS.md
%license LICENSE THIRD_PARTY_NOTICES.md
%{_bindir}/coli
%{_libexecdir}/colibri/

%changelog
%autochangelog
