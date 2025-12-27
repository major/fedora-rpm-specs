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
%global upstreamname ROCdbgapi

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

Name:       rocdbgapi%{pkg_suffix}
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    AMD Debugger API

License:    MIT
URL:        https://github.com/ROCm/%{upstreamname}
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

ExclusiveArch: x86_64

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: rocm-comgr%{pkg_suffix}-devel
BuildRequires: rocm-runtime%{pkg_suffix}-devel

%description
The AMD Debugger API is a library that provides all the support necessary
for a debugger and other tools to perform low level control of the
execution and inspection of execution state of AMD's commercially
available GPU architectures.

%package devel
Summary: Libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-dbgapi/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-dbgapi-asan/LICENSE.txt

%files
%doc README.md
%license LICENSE.txt
%{pkg_prefix}/%{pkg_libdir}/librocm-dbgapi.so.0{,.*}

%files devel
%{pkg_prefix}/share/pkgconfig/amd-dbgapi.pc
%{pkg_prefix}/include/amd-dbgapi/
%{pkg_prefix}/%{pkg_libdir}/librocm-dbgapi.so
%{pkg_prefix}/%{pkg_libdir}/cmake/amd-dbgapi/

%changelog
* Tue Dec 23 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Add --with compat

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Initial package
