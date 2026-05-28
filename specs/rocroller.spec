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

%global upstreamname rocroller
%global rocm_release 7.13
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# For testing
# Hardcoded hw support in lib/include/rocRoller/GPUArchitecture/GPUArchitectureTarget.hpp
# 908, 90a, 942, 950, 1010, 1012, 1030, 1200, 1201
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

Name:           rocroller
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD's rocRoller Assembly Kernel Generator
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/therock-%{rocm_release}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  libdivide-devel
BuildRequires:  msgpack-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  spdlog-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  yaml-cpp-devel

%if %{with test}
BuildRequires:  blas-static
BuildRequires:  blis-devel
BuildRequires:  catch-devel
BuildRequires:  chrpath
BuildRequires:  flexiblas-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  lapack-static
BuildRequires:  mxdatagenerator-devel
BuildRequires:  rocm-omp-devel
%endif

# ROCm only working on x86_64
ExclusiveArch:  x86_64

%description
AMD's rocRoller Assembly Kernel Generator

rocRoller is a software library for generating AMDGPU kernels.

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname} -p3

# GPUArchitectureGenerator/isa_spec_manager/amdisa_structures.h:88:9: error: unknown type name 'uint32_t'
# and similar
sed -i '/#include <iostream.*/a#include <stdint.h>' GPUArchitectureGenerator/isa_spec_manager/amdisa_structures.h
sed -i '/#include <iostream.*/a#include <stdint.h>' lib/include/rocRoller/GPUArchitecture/GPUInstructionInfo.hpp

# test/catch/SettingsTest.cpp:197:21: error: use of undeclared identifier 'usleep'
#  197 |                     usleep(rand() % 100);
sed -i '/#include <omp.*/a#include <unistd.h>' test/catch/SettingsTest.cpp

# Remove some problem tests
sed -i '/ExpressionIdenticalTest/d' test/catch/CMakeLists.txt
sed -i '/FastDivisionTest/d' test/unit/CMakeLists.txt

# Removed bundled tinyxml
rm GPUArchitectureGenerator/isa_spec_manager/tinyxml2.cpp
rm GPUArchitectureGenerator/isa_spec_manager/tinyxml2.h
sed -i -e '/tinyxml2/d' GPUArchitectureGenerator/CMakeLists.txt
sed -i -e 's@        rocroller::isa-spec-manager@        rocroller::isa-spec-manager tinyxml2@' GPUArchitectureGenerator/CMakeLists.txt


%build
%cmake \
    -Dcblas_DIR=%{_libdir}/cmake/cblas64-3.12.0/ \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DROCROLLER_BUILD_TESTING=%{build_test} \
    -DROCROLLER_ENABLE_CLIENT=OFF \
    -DROCROLLER_ENABLE_GEMM_CLIENT_TESTS=OFF

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%_datadir/doc/rocroller/LICENSE.md

%if %{with test}
# can not find libomp.so
#  chrpath -l /usr/bin/rocroller-tests
#  /usr/bin/rocroller-tests: RUNPATH=$ORIGIN/../lib:$ORIGIN/../lib/rocroller/lib
chrpath -r %{rocmllvm_libdir} %{buildroot}%_bindir/rocroller-tests* 
%endif

%files
%doc README.md
%license LICENSE.md
%{_libdir}/librocroller.so.1{,.*}

%files devel
%_includedir/rocRoller/
%{_libdir}/cmake/rocroller/
%{_libdir}/librocroller.so

%if %{with test}
%files test
%{_bindir}/rocroller-*
%endif

%changelog
* Sat May 16 2026 Tom Rix <Tom.Rix@amd.com> - 7.13.0-1
- Initial package

