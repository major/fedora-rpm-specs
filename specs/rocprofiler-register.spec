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
%global upstreamname rocprofiler-register
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

%global glog_version 0.7.1

%bcond_with check
%if %{with check}
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

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           rocprofiler-register%{pkg_suffix}
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        A rocprofiler helper library
License:        MIT AND BSD-3-Clause

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Url:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Source1:        https://github.com/google/glog/archive/refs/tags/v%{glog_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  git

# BSD-3-Clause
# rocprofile needs a newer glog
# glog looks like a dead project, notifiy the upstream they should move off of it.
# https://github.com/ROCm/rocprofiler-sdk/issues/87
Provides:       bundled(glog) = %{glog_version}

%description
The rocprofiler-register library is a helper library that coordinates
the modification of the intercept API table(s) of the HSA/HIP/ROCTx
runtime libraries by the ROCprofiler (v2) library. The purpose of this
library is to provide a consistent and automated mechanism of enabling
performance analysis in the ROCm runtimes which does not rely on
environment variables or unique methods for each runtime library.

When a runtime is initialized (either explicitly and lazily) and the
intercept API table is constructed, it passes this API table to
rocprofiler-register. Rocprofiler-register scans the symbols in the
address space and if it detects there is at least one visible symbol
named rocprofiler_configure (which is a function provided by tools),
it passes the intercept API table to the rocprofiler library (dlopening
the rocprofiler library if it is not already loaded). The rocprofiler
library then does an extensive scan for all the instances of the
rocprofiler_configure symbols and invokes each of them. The
rocprofiler_configure function (again, provided by a tool) returns
effectively tells rocprofiler which behaviors it wants to be notified
about, features it wants to use (e.g. API tracing, kernel dispatch
timing), etc.

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# When using the system fmt, need to change this link
sed -i 's@fmt::fmt@fmt@' source/lib/rocprofiler-register/CMakeLists.txt

# Do not hardcode install lib
sed -i 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# Do not use git to fetch glog, use cached source
cd external
rm -rf glog
tar xf %{SOURCE1}
mv glog-* glog
# Need to remove the fetch
sed -i -e '/rocprofiler_register_checkout_git_submodule/,+6d' CMakeLists.txt
cd -

# Copy glog's license file
cp -p external/glog/COPYING COPYING.glog

%build
%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DROCPROFILER_REGISTER_BUILD_TESTS=%{build_test} \
    -DROCPROFILER_REGISTER_BUILD_FMT=OFF

%cmake_build

%install
%cmake_install

# Do not install the test source etc
rm -rf %{buildroot}%{pkg_prefix}/share/rocprofiler-register
rm -rf %{buildroot}%{pkg_prefix}/share/modulefiles
rm -rf %{buildroot}%{pkg_prefix}/share/doc/rocprofiler-register/LICENSE.md

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE.md COPYING.glog
%{pkg_prefix}/%{pkg_libdir}/librocprofiler-register.so.0{,.*}

%files devel
%doc README.md
%{pkg_prefix}/include/rocprofiler-register/
%{pkg_prefix}/%{pkg_libdir}/librocprofiler-register.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocprofiler-register/

%changelog
* Tue Dec 23 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Add --with compat

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Fri Oct 10 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Fri Sep 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 21 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Initial package


