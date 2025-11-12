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
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname origami

Name:       rocm-origami
Version:    %{rocm_version}
Release:    1%{?dist}
Summary:    Analytical GEMM Solution Selection

License:    MIT
URL:        https://github.com/ROCm/rocm-libraries
Source0:    %{upstreamname}-rocm-%{version}.tar.gz
# Use fetch.sh to extract origami from rocm-libraries
# There is no upstream origami project, it is part of the new ROCm
# monorepo rocm-libraries.  This monorepo is expected to replace the upstream
# locations its libraries. At this time there is only a single tarball
# This PR starts the process to address that
# https://github.com/ROCm/rocm-libraries/pull/2494
Source1:    fetch.sh
# License file is not in the 7.1.0 tag, but is here
Source2:    https://github.com/ROCm/rocm-libraries/tree/develop/shared/origami/LICENSE.md

#
# Workaround this hipblaslt build issue
# CMake Error at /usr/lib64/cmake/origami/origami-config.cmake:11 (message):
#   origami::origami target is missing
#
# hipblaslt from rocm-libraries does not use cmake to find origami
# https://github.com/ROCm/rocm-libraries/issues/2422
# So they would not have run into this issue.
Patch1:     0001-rocm-origami-remove-scope-for-variables.patch

ExclusiveArch: x86_64

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: rocm-cmake
BuildRequires: rocm-comgr-devel
BuildRequires: rocm-hip-devel
BuildRequires: rocm-runtime-devel

%description
The name "origami" still evokes the elegance of transforming
a flat (2-D) sheet into intricate higher dimensional
structures. In this context, however, Origami has evolved
into a tool set for **GEMM solution selection and
optimization**. Inspired by the art of paper folding, the
library now enables users to explore a range of tiling and
mapping configurations and to make informed decisions on
data and computation mapping for high-performance GEMM
operations.

%package devel
Summary: Libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p3 -n %{upstreamname}-rocm-%{version}

# The license file
cp %{SOURCE2} .

# Use system rocm-cmake, no downloading
sed -i -e 's@if(NOT ROCM_FOUND)@if(FALSE)@' cmake/dependencies.cmake

%build
%cmake
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/origami/LICENSE.md

%files
%doc README.md
%license LICENSE.md
%{_libdir}/liborigami.so.0{,.*}

%files devel
%dir %{_includedir}/origami
%dir %{_libdir}/cmake/origami
%{_includedir}/origami/*.hpp
%{_libdir}/cmake/origami/*.cmake
%{_libdir}/liborigami.so

%changelog
* Sun Nov 2 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Initial package
