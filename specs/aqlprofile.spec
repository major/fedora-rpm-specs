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

%global upstreamname aqlprofile
%global rocm_release 7.0
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

# Testing is broken
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Summary:        Architected Queuing Language Profiling Library
Name:           aqlprofile
License:        MIT
Version:        %{rocm_version}
Release:        1%{?dist}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Url:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-runtime-devel

%description
AQLprofile is an open source library that enables advanced GPU
profiling and tracing on AMD platforms. It works in conjunction
with rocprofiler-sdk to support profiling methods such as
performance counters (PMC) and SQ thread trace (SQTT).
AQLprofile provides the foundational mechanisms for constructing
AQL packets and managing profiling operations across multiple
AMD GPU architecture families.

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Do not hardcode CMAKE_BUILD_TYPE
# https://github.com/ROCm/aqlprofile/issues/12
sed -i -e 's@CMAKE_BUILD_TYPE@DO_NO_HARDCODE_CMAKE_BUILD_TYPE@' cmake_modules/env.cmake

%build
%cmake \
  -DCMAKE_BUILD_TYPE=%{build_type} \
  -DAQLPROFILE_BUILD_TESTS=%{build_test} \
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libhsa-amd-aqlprofile64.so.1{,.*}

%files devel
%doc README.md
%dir %{_includedir}/aqlprofile-sdk
%{_includedir}/aqlprofile-sdk/*.h
%{_libdir}/libhsa-amd-aqlprofile64.so

%changelog
* Fri Sep 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 28 2025 Tom Rix <Tom.Rix@amd.com> - 0.0^git20250526.eebb229-3
- Add Fedora copyright

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0^git20250526.eebb229-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 1 2025 Tom Rix <Tom.Rix@amd.com> - 0.0^git20250526.eebb229-1
- Initial package

