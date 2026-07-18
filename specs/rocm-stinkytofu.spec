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

%global upstreamname stinkytofu
%global rocm_release 7.13
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Name:           rocm-stinkytofu
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        A LLVM-inspired pass-based IR optimizer for AMD GPU assembly kernels
License:        MIT AND BSD-3-Clause
# https://github.com/ROCm/rocm-libraries/issues/7864
# Request the upstream have a top level license file.
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/therock-%{rocm_release}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

%global nanobind_version 2.9.2
%global nanobind_giturl https://github.com/wjakob/nanobind
Source1:        %{nanobind_giturl}/archive/v%{nanobind_version}/nanobind-%{nanobind_version}.tar.gz
%global robinmap_version 1.3.0
%global robinmap_giturl https://github.com/Tessil/robin-map
Source2:        %{robinmap_giturl}/archive/v%{robinmap_version}/robin-map-%{robinmap_version}.tar.gz


Patch1:         0001-stinkytofu-use-nanobind-tarball.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel

# BSD-3-Clause
Provides:       bundled(nanobind) = %{nanobind_version}
Provides:       bundled(robin-map) = %{robinmap_version}

# ROCm only working on x86_64
ExclusiveArch:  x86_64

%description
StinkyTofu is an LLVM-inspired pass-based IR optimizer for
AMD GPU assembly kernels. It is used by hipBLASLt/TensileLite
to schedule and optimize generated GPU code for gfx1250.

Features
* Two-level IR: High-level Logical IR (architecture-agnostic)
  and low-level Asm IR (architecture-specific)
* Pass pipeline: DAG scheduling, wait count insertion, dead
  code elimination, redundant move elimination, peephole optimization
* TableGen-based instruction definitions: New architectures
  require only .def files, no C++ changes
* FileCheck-style testing: LLVM-style lit tests with stinkytofu-check
* Python bindings: Full IR construction and optimization accessible
  from Python

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%package -n python3-stinkytofu
Summary:        python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-stinkytofu
%{summary}

%prep
%autosetup -n %{upstreamname} -p3

# Use bundled nanobind
tar xf %{SOURCE1}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE2}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind

# src/serialization/asm/PatternParser.cpp:794:13: error: unknown type name 'uint32_t'
sed -i -e '/#include <sstream>.*/a#include <stdint.h>' src/serialization/asm/PatternParser.cpp
sed -i -e '/#include <vector>.*/a#include <stdint.h>' include/stinkytofu/serialization/logical/IRSerializer.hpp
# src/transforms/asm/dag/ReadyQueue.hpp:49:31: error: use of undeclared identifier 'UINT_MAX'
sed -i -e '/#include <queue>.*/a#include <limits.h>' src/transforms/asm/dag/ReadyQueue.hpp
sed -i -e '/#include <string_view>.*/a#include <limits.h>' src/serialization/asm/IRParser.cpp
# Install to lib64 not lib
sed -i -e 's@LIBRARY DESTINATION lib@LIBRARY DESTINATION lib64@' CMakeLists.txt
sed -i -e 's@ARCHIVE DESTINATION lib@ARCHIVE DESTINATION lib64@' CMakeLists.txt
sed -i -e 's@DESTINATION lib/cmake/stinkytofu@DESTINATION lib64/cmake/stinkytofu@' CMakeLists.txt
sed -i -e 's@DESTINATION lib@DESTINATION lib64@' tools/intrinsic-compiler/CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DSTINKYTOFU_BUILD_PYTHON=ON \
    -DSTINKYTOFU_BUILD_TESTS=OFF

%cmake_build

%install
%cmake_install

# Move python bindings to a system location
mkdir -p %{buildroot}/%{python3_sitearch}/
mv %{buildroot}/usr/lib/python%{python3_version}/dist-packages/stinkytofu %{buildroot}/%{python3_sitearch}/

%files
%doc README.md
%_bindir/stinkytofu-opt
%_bindir/stinkytofu-check
%_bindir/intrinsic-compiler
%_libdir/libstinkytofu.so.0{,.*}
%_libdir/intrinsics.st.bc

%files devel
%_includedir/stinkytofu/
%_libdir/cmake/stinkytofu/
%_libdir/libstinkytofu.so

%files -n python3-stinkytofu
%{python3_sitearch}/stinkytofu/

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jun 13 2026 Tom Rix <Tom.Rix@amd.com> - 7.13.0-2
- Enable python bindings

* Thu May 28 2026 Tom Rix <Tom.Rix@amd.com> - 7.13.0-1
- Initial package

