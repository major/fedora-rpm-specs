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
%global upstreamname rocshmem

%global rocm_release 7.12
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-flto=thin//' -e 's/-mtls-dialect=gnu2//')

Name:       rocshmem
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    ROCm OpenSHMEM runtime

License:    MIT AND (GPL-2.0-only OR BSD-2-Clause) AND (GPL-2.0-only OR Linux-OpenIB)
# The main license is MIT
# There are a couple of other licenses for these files
# GPL-2.0-only OR BSD-2-Clause
#  src/gda/bnxt/bnxt_re_dv.h
#  src/gda/bnxt/bnxt_re_hsi.h
# GPL-2.0-only OR Linux-OpenIB - licensecheck gets this wrong
#  src/gda/ibv_core.hpp
#  src/gda/ionic/ionic_dv.h
#  src/gda/ionic/ionic_fw.h
#  src/gda/mlx5/mlx5dv.h

URL:        https://github.com/ROCm/rocm-systems
Source0:    %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

Patch1:     0001-rocshmem-so-version.patch

ExclusiveArch: x86_64

BuildRequires: chrpath
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: rocm-cmake
BuildRequires: rocm-comgr-devel
BuildRequires: rocm-compilersupport-macros
BuildRequires: rocm-core-devel
BuildRequires: rocm-hip-devel
BuildRequires: rocm-runtime-devel
BuildRequires: rocm-rpm-macros

%description
The ROCm OpenSHMEM (rocSHMEM) runtime is part of an AMD and AMD Research
initiative to provide GPU-centric networking through an OpenSHMEM-like
interface. This intra-kernel networking library simplifies application code
complexity and enables more fine-grained communication/computation overlap
than traditional host-driven networking. rocSHMEM uses a single symmetric
heap that is allocated on GPU memories.

There are currently three backends for rocSHMEM; IPC, Reverse Offload (RO),
and GDA. The backends primarily differ in their implementations of
intra-kernel networking.

The IPC backend implements communication primitives using load/store
operations issued from the GPU.

The Reverse Offload (RO) backend has the GPU runtime forward rocSHMEM
networking operations to the host-side runtime, which calls into a
traditional MPI or OpenSHMEM implementation. This forwarding of requests is
transparent to the programmer, who only sees the GPU-side interface.

The GPU Direct Async (GDA) backend allows for rocSHMEM to issue communication
operations to the NIC directly from the device-side code, without involving a
CPU proxy. within the GPU. During initialization we prepare network resources
for each NIC vendor using the vendor-appropriate Direct Verbs APIs. When
calling the device-side rocSHMEM API, the device threads are used to
construct Work Queue Entries (WQEs) and post the communication to the send
queues of the NIC directly. Completion Queues (CQs) are polled from the
device-side code as well.

The RO and GDA backend is provided as-is with limited support from AMD or AMD
Research.

%package devel
Summary: Libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p3 -n %{upstreamname}

# install location of rocm_version
sed -i -e 's@rocm-core/@@' src/tools/rocshmem_info.cpp

%build
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DEXPLICIT_ROCM_VERSION=%{rocm_version} \

%cmake_build

%install
%cmake_install

# ERROR   0002: file '/usr/bin/rocshmem_info' contains an invalid runpath '
chrpath -d %{buildroot}%{_bindir}/rocshmem_info

# Extra license
rm -f %{buildroot}%{_prefix}/share/doc/rocshmem/LICENSE.md

%files
%doc README.md
%license LICENSE.md
%{_bindir}/rocshmem_info
%{_libdir}/librocshmem.so.1{,.*}

%files devel
%{_includedir}/rocshmem/
%{_libdir}/cmake/rocshmem/
%{_libdir}/librocshmem.so

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Mar 30 2026 Tom Rix <Tom.Rix@amd.com> - 7.12.0-1
- Initial package
