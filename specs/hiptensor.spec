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
%global upstreamname hiptensor

%global pkg_library_name %{upstreamname}
%global pkg_library_version 0

%bcond_with preview
%if %{with preview}
%global rocm_release 10.1
%else
%global rocm_release 10.1
%endif

%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global skip_install_rpath ON

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

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

Name:           hiptensor
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        ROCm tensor primitives library
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries

Source0:        %{url}/releases/download/therock-%{rocm_release}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  composable_kernel-devel
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-filesystem
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros

Requires:       rocm-filesystem

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
The hipTensor package contains AMD's C++ library for accelerating
tensor primitives using GPU matrix cores on AMD's latest discrete
GPUs. It provides high-level kernels for contraction, per element,
and reduction operations.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{upstreamname}

%build
%cmake \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_RPATH=%{_libdir} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DGPU_TARGETS=gfx11-generic \
    -DHIPTENSOR_BUILD_SAMPLES=OFF \
    -DHIPTENSOR_BUILD_TESTS=OFF \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{_datadir}/doc/hiptensor/LICENSE

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}

%files devel
%{_includedir}/hiptensor/
%{_libdir}/lib%{pkg_library_name}.so
%{_libdir}/cmake/hiptensor/

%changelog
* Mon Nov 09 2026 Tom Rix <Tom.Rix@amd.com> - 10.1.0-1
- Initial package
