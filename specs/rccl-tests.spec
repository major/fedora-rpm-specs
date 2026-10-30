#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

%global upstreamname rccl-tests

%bcond_with preview
%if %{with preview}
%global rocm_release 10.1
%else
%global rocm_release 10.1
%endif

%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-flto=thin//' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%global gpu_list %{rocm_gpu_list_rccl}
%global _gpu_list gfx1100

Name:           rccl-tests%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        RCCL tests

License:        BSD-3-Clause AND MIT
# The main license.txt is BSD-3-Clause
# rccl-tests is derrived from nccl-tests
# https://github.com/NVIDIA/nccl-tests/blob/master/LICENSE.txt
#
# The MIT license covers the rccl specific parst like
# src/rccl_compat.h
# test/*.py
#
# The unknown files come from nccl-tests such as
# Makefile
# src/*.cu
# Have this header
# /*************************************************************************
# * Copyright (c) 2016-2022, NVIDIA CORPORATION. All rights reserved.
# * Modifications Copyright (c) 2019-2022 Advanced Micro Devices, Inc. All rights reserved.
# *
# * See LICENSE.txt for license information
# ************************************************************************/

URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  hipify%{pkg_suffix}
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  rccl%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
These tests check both the performance and the correctness of RCCL
operations. They can be compiled against RCCL.

%prep
%autosetup -p3 -n %{upstreamname}

%build
%cmake \
    -DGPU_TARGETS=%{gpu_list} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DEXPLICIT_ROCM_VERSION=%{rocm_version}

%cmake_build

%install
%cmake_install

# ERROR   0001: file '/usr/bin/all_reduce_bias_perf' contains a standard runpath '/usr/lib' in [/usr/lib:/opt/rocm/lib]
chrpath -d %{buildroot}%{pkg_prefix}/bin/*

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rccl-tests/LICENSE.txt

%files
%doc README.md
%license LICENSE.txt
%{pkg_prefix}/bin/*_perf

%changelog
* Thu Oct 29 2026 Tom Rix <Tom.Rix@amd.com> - 10.1-1
- Update to 10.1

* Tue Oct 13 2026 Tom Rix <Tom.Rix@amd.com> - git20260116.a52452e-4
- Rebuild for 10.1

* Thu Sep 24 2026 Tom Rix <Tom.Rix@amd.com> - git20260116.a52452e-3
- Rebuild for 10.0

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - git20260116.a52452e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sun Jan 25 2026 Tom Rix <Tom.Rix@amd.com> - git20260116.a52452e-1
- Update source

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - git20251211.5272cd1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Dec 27 2025 Tom Rix <Tom.Rix@amd.com> - git20251211.5272cd1-1
- Add --with compat
- Update source

* Wed Oct 22 2025 Tom Rix <Tom.Rix@amd.com> - git20251018.33cc4df-1
- Initial package
