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
%global commit0 5272cd16efeeb5012f17e5541a39af9de6aa9eae
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20251211

%global rocm_release 7.1
%global rocm_patch 0
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
Version:        git%{date0}.%{shortcommit0}
Release:        2%{?dist}
Summary:        RCCL tests

Url:            https://github.com/ROCm/rccl-tests
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

Source0:        %{url}/archive/%{commit0}/rccl-tests-%{shortcommit0}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  hipify%{pkg_suffix}
BuildRequires:  gcc-c++
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
%setup -q -n rccl-tests-%{commit0}

%build
%cmake \
    -DGPU_TARGETS=%{gpu_list} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
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
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - git20251211.5272cd1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Dec 27 2025 Tom Rix <Tom.Rix@amd.com> - git20251211.5272cd1-1
- Add --with compat
- Update source

* Wed Oct 22 2025 Tom Rix <Tom.Rix@amd.com> - git20251018.33cc4df-1
- Initial package
