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
%global commit0 33cc4df1e4631d98a7a9ff1b1e0221f77ec81470
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20251018

%global rocm_release 7.0
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-flto=thin//' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Name:           rccl-tests
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
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
BuildRequires:  hipify
BuildRequires:  gcc-c++
BuildRequires:  rccl-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
These tests check both the performance and the correctness of RCCL
operations. They can be compiled against RCCL.

%prep
%setup -q -n rccl-tests-%{commit0}

%build
%cmake \
    -DGPU_TARGETS=%{rocm_gpu_list_rccl} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DEXPLICIT_ROCM_VERSION=%{rocm_version}

%cmake_build

%install
%cmake_install

# ERROR   0001: file '/usr/bin/all_reduce_bias_perf' contains a standard runpath '/usr/lib' in [/usr/lib:/opt/rocm/lib]
chrpath -d %{buildroot}%{_bindir}/*

rm -f %{buildroot}%{_prefix}/share/doc/rccl-tests/LICENSE.txt

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*_perf

%changelog
* Wed Oct 22 2025 Tom Rix <Tom.Rix@amd.com> - git20251018.33cc4df-1
- Initial package
