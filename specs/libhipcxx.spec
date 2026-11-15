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
# LIABILITY, WHETHER IN AN ACTION OF ANY KIND, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE PERFORMANCE OF THIS SOFTWARE.
#

%global upstreamname libhipcxx

%bcond_with preview
%if %{with preview}
%global rocm_release 10.1
%else
%global rocm_release 10.1
%endif

%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# there is no debug package, this is headers only
%global debug_package %{nil}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           libhipcxx
%if %{with preview}
Release:        0%{?dist}
%else
Release:        1%{?dist}
%endif
Version:        %{rocm_version}
Summary:        C++ Standard Library for HIP (host and device)
License:        Apache-2.0 WITH LLVM-exception AND MIT
# Apache-2.0 with LLVM-exceptions
# The main license is Apache-2.0 with LLVM-exceptions
# This project was derrived from libcudacxx
# https://github.com/NVIDIA/libcudacxx/blob/main/LICENSE.TXT
# See LICENSE.TXT and NOTICE.txt
#
# Apache-2.0 WITH LLVM-exception AND MIT
# Many changes to the original libcudacxx code
#
# MIT
# AMD changes to the libcudacxx source and a few misc files are MIT
# CMakeLists.txt
# README.rst
# cmake/DownloadProject.cmake
# cmake/FindROCMCmake.cmake
# cmake/libhipcxx*
# cmake/test/
# codegen/CMakeLists.txt
# docs/.sphinx/_toc.yml.in
# docs/build.sh
# docs/conf.py
# docs/libcudacxx/extended_api/functional/proclaim_return_type.rst
# docs/overview.md
# docs/requirements.txt
# examples/hip/
# include/amd/amd_utils.h
# include/cuda/std/detail/libcxx/include/support/hip/chrono_hip_extension.h
# lib/cmake/libhipcxx/
URL:            https://github.com/ROCm/libhipcxx
Source0:        %{url}/archive/refs/tags/therock-%{rocm_release}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# ROCm only working on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros

%description
The header-only development files for libhip++: C++ Standard Library
features usable in both host and device HIP code.

%package devel
Summary:        C++ Standard Library for HIP (host and device)
Provides:       %{name}-static = %{version}-%{release}

# the devel subpackage is only headers and cmake infra
BuildArch: noarch

%description devel
The header-only development files for libhip++: C++ Standard Library
features useable in both host and device HIP code.

%prep
%autosetup -p1 -n %{upstreamname}-therock-%{rocm_release}

# simplify the source for the license check
rm -rf test utils cmake/config.guess ci example
# some hidden dirs and files
rm -rf .*

%build
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DLIBCUDACXX_ENABLE_LIBCUDACXX_TESTS=OFF \
    -Dlibhipcxx_ENABLE_CMAKE_TESTS=OFF \
    -Dlibhipcxx_ENABLE_CODEGEN=OFF

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{_datadir}/doc/libhipcxx/LICENSE.TXT

%files devel
%doc README.rst
%license LICENSE.TXT
%license NOTICE.txt
%{_includedir}/libhipcxx/
%{_datadir}/cmake/libhipcxx/

%changelog
* Sun Nov 08 2026 Tom Rix <Tom.Rix@amd.com> - 10.1.0-1
-Initial package
