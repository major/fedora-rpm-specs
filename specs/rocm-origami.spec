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
%global rocm_release 7.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname origami

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
%if 0%{?suse_version}
%global origami_name liborigami1%{pkg_suffix}
%else
%global origami_name rocm-origami%{pkg_suffix}
%endif

Name:       rocm-origami%{pkg_suffix}
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    Analytical GEMM Solution Selection

License:    MIT
URL:        https://github.com/ROCm/rocm-libraries
Source0:    %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
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
BuildRequires: rocm-cmake%{pkg_suffix}
BuildRequires: rocm-comgr%{pkg_suffix}-devel
BuildRequires: rocm-compilersupport%{pkg_suffix}-macros
BuildRequires: rocm-hip%{pkg_suffix}-devel
BuildRequires: rocm-runtime%{pkg_suffix}-devel

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

%if 0%{?suse_version}
%package -n %{origami_name}
Summary:        Shared libraries for %{name}

%description -n %{origami_name}
%{summary}

%ldconfig_scriptlets -n %{origami_name}
%endif

%package devel
Summary: Libraries and headers for %{name}
Requires: %{origami_name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p3 -n %{upstreamname}

# Use system rocm-cmake, no downloading
sed -i -e 's@if(NOT ROCM_FOUND)@if(FALSE)@' cmake/dependencies.cmake

%build
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/origami/LICENSE.md

%files -n %{origami_name}
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/liborigami.so.1{,.*}

%files devel
%{pkg_prefix}/include/origami/
%{pkg_prefix}/%{pkg_libdir}/cmake/origami/
%{pkg_prefix}/%{pkg_libdir}/liborigami.so

%changelog
* Fri Feb 20 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-2
- Fix TW build

* Wed Jan 28 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 25 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-3
- Add --with compat

* Sat Dec 13 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-2
- Support SUSE

* Thu Nov 27 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Sun Nov 2 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Initial package
