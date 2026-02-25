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

%global upstreamname mxdatagenerator
%global rocm_release 7.11
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# there is no debug package, this just headers
%global debug_package %{nil}

Name:           mxdatagenerator
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD's floating point data generator
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/therock-%{rocm_release}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-filesystem

# Only a header
BuildArch: noarch
# But, ROCm only working on x86_64
ExclusiveArch:  x86_64

%description
AMD's floating point data generator

This library supports data generation for different floating point
formats, as well as conversion instructions between lower precision
floating points and single precision floating point.

Formats Supported

    F32 (E8M23)
    FP16 (E5M2)
    BF16 (E8M7)
    OCP MX-FP8 (E4M3)
    OCP MX-BF8 (E5M2)
    OCP MX-FP6 (E2M3)
    OCP MX-BF6 (E3M2)
    OCP MX-FP4 (E2M1)

%package devel
Summary:  AMD's floating point data generator
Provides: mxdatagenertor-static = %{version}-%{release}

%description devel
AMD's floating point data generator

This library supports data generation for different floating point
formats, as well as conversion instructions between lower precision
floating points and single precision floating point.

Formats Supported

    F32 (E8M23)
    FP16 (E5M2)
    BF16 (E8M7)
    OCP MX-FP8 (E4M3)
    OCP MX-BF8 (E5M2)
    OCP MX-FP6 (E2M3)
    OCP MX-BF6 (E3M2)
    OCP MX-FP4 (E2M1)

%prep
%autosetup -n %{upstreamname} -p1

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR=share

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%_datadir/doc/mxDataGenerator/LICENSE.md

%files devel
%doc README.md
%license LICENSE.md
%_includedir/*.hpp
%_datadir/cmake/mxDataGenerator/

%changelog
* Sun Feb 15 2026 Tom Rix <Tom.Rix@amd.com> - 7.11.0-1
- Initial package
