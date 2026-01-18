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
%global upstreamname TransferBench

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Not all hw is supported
%global gpu_list "gfx906;gfx908;gfx90a;gfx942;gfx950;gfx1030;gfx1100;gfx1101;gfx1102;gfx1150;gfx1151;gfx1200;gfx1201"

Name:       rocm-transferbench
Version:    %{rocm_version}
Release:    1%{?dist}
Summary:    Benchmark copies between AMD GPUs

License:    MIT
URL:        https://github.com/ROCm/%{upstreamname}
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

ExclusiveArch: x86_64

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(numa)
BuildRequires: rocm-cmake
BuildRequires: rocm-comgr-devel
BuildRequires: rocm-compilersupport-macros
BuildRequires: rocm-hip-devel
BuildRequires: rocm-runtime-devel
BuildRequires: rocm-rpm-macros

%description
TransferBench is a benchmark for simultaneous copies between
user-specified CPU and GPU devices.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake \
    -DGPU_TARGETS=%{gpu_list} \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=${bt} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
    -DROCM_PATH=/usr \

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/transferbench/LICENSE.md

%files
%license LICENSE.md
%{_bindir}/TransferBench

%changelog
* Thu Nov 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Initial package
