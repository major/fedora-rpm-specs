# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
%undefine _include_frame_pointers

# Pin to a specific llvm version
%global llvm_ver 21

Name: pocl
Version: 7.1
Release: %autorelease

# The entire code is under MIT
# include/utlist.h which is under BSD-1-Clause (unbundled)
# lib/kernel/vecmath which is under GPL-3.0-or-later OR LGPL-3.0-or-later
License: MIT AND BSD-1-Clause AND (GPL-3.0-or-later OR LGPL-3.0-or-later)
Summary: Portable Computing Language - an OpenCL implementation
URL: https://github.com/%{name}/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

# PoCL always targets clang/LLVM, but should be built with the same
# system compiler used to build LLVM, thus we build with GCC.
# See: https://portablecl.org/docs/html/install.html#compiler-support
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: clang(major) = %{llvm_ver}
BuildRequires: clang-devel(major) = %{llvm_ver}
BuildRequires: compiler-rt(major) = %{llvm_ver}
BuildRequires: llvm-devel(major) = %{llvm_ver}
# required for SPIR-V support
# TODO: add a major provide to spirv-llvm-translator
BuildRequires: spirv-llvm-translator-devel >= %{llvm_ver}, spirv-llvm-translator-devel < %[%{llvm_ver} + 1]

# basic deps
BuildRequires: glew-devel
BuildRequires: hwloc-devel
BuildRequires: libedit-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(OpenCL)
BuildRequires: uthash-devel
BuildRequires: zlib-devel

# build system deps
BuildRequires: cmake
BuildRequires: libtool
BuildRequires: ninja-build

# TODO: Unbundle the STC headers
# It's unclear if this should be STC, stclib, libstc or libSTC?
Provides: bundled(STC)

# https://bugzilla.redhat.com/show_bug.cgi?id=1082364
Requires: libstdc++-devel%{?_isa}
# Runtime dependency, because libm.so is required for kernels
Requires: glibc-devel%{?_isa}

%description
PoCL is a portable open source (MIT-licensed) implementation of the OpenCL
standard. In addition to being an easily portable/layered multi-device
open-source OpenCL implementation, a major goal of this project is improving
interoperability of diversity of OpenCL-capable devices by integrating them to
a single centrally orchestrated platform. Also one of the key goals is to
enhance performance portability of OpenCL programs across device types
utilizing runtime and compiler techniques.

PoCL uses Clang as an OpenCL C frontend and LLVM for kernel compiler
implementation, and as a portability layer. Thus, if your desired target has an
LLVM backend, it should be able to get OpenCL support easily by using PoCL.

%package devel
Summary: Portable Computing Language development files
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: clang(major) = %{llvm_ver}
Requires: ocl-icd-devel%{?_isa}
Requires: opencl-filesystem
Requires: uthash-devel

%description devel
Portable Computing Language development files.

%prep
%autosetup -p1

# Unbundle uthash
rm include/uthash.h
rm include/utlist.h

# TODO: Unbundle the STC headers
# Copy the STC license
cp thirdparty/STC/LICENSE STC-LICENSE


%build
# We build PoCL as an OpenCL ICD
# We build the tests but not the examples
# We build poclcc to allow pre-compilation of OpenCL kernel binaries
# We pass the distro flags when complining OpenCL kernels
# We build all the drivers in OpenCL Conformance mode, which disables all
#    experimental and incomplete extensions.
# Device Drivers we build:
# - CPU driver (the default for PoCL)
#    - with OpenMP support
#    - on i686/x86_64/ppc64le, use the generic CPU option for Linux distros
#       - this builds in support for different levels of optional instructions
#    - on aarch64 and riscv64, just target the most generic CPU possible
#       - ideally, upstream will add "distro" support eventually
#    - without FP16 support (not compatible with conformance)
#    - without vectorizing builtins (not compatible with conformance)
#    - without predefined kernels from onnxruntime, OpenCV, etc (not conformant)
# Device Drivers we don't build:
# - CPU driver using TBB (seems feasible - TODO make a PR for the TBB driver)
# - AMD HSA (deprecated, CPU only)
# - NVIDIA CUDA (for the usual reasons)
# - Fixed-Function Accelerators/alamif (no demand from users)
# - Proxy (not compatible with PoCL as an OpenCL ICD)
# - Vulkan (incomplete and not maintained)
# - Level Zero (feasible - see https://src.fedoraproject.org/rpms/pocl/pull-request/28 )
# - Remote (seems feasible - TODO make a PR for the Remote driver)
%global __cc_clang clang-%{llvm_ver}
%global __cxx_clang clang++-%{llvm_ver}
%global __cpp_clang clang-cpp-%{llvm_ver}
%cmake -G Ninja \
    -DENABLE_ICD:BOOL=ON \
    -DPOCL_ICD_ABSOLUTE_PATH:BOOL=OFF \
    -DPOCL_INSTALL_ICD_VENDORDIR=%{_sysconfdir}/OpenCL/vendors \
    -DENABLE_TESTS:BOOL=ON \
    -DENABLE_EXAMPLES:BOOL=OFF \
    -DENABLE_POCLCC:BOOL=ON \
    -DEXTRA_KERNEL_CXX_FLAGS="%{optflags}" \
    -DENABLE_CONFORMANCE:BOOL=ON \
    -DENABLE_HOST_CPU_DEVICES:BOOL=ON \
    -DENABLE_HOST_CPU_DEVICES_OPENMP:BOOL=ON \
%ifarch %{ix86} x86_64 ppc64le
    -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch aarch64
    -DLLC_HOST_CPU="cortex-a53" \
%endif
%ifarch riscv64
    -DLLC_HOST_CPU="generic-rv64" \
%endif
    -DWITH_LLVM_CONFIG="llvm-config-%{llvm_ver}"
%cmake_build

%install
%cmake_install

%check
# Upstream supports running tests only on x86_64, but test everything anyway
# PoCL doesn't support s390x, see rhbz#2396306. The tests fail badly (endian issues?) but removing a main arch from a package is a pain.
%ifnarch s390x
# Run all tests except those expected to fail on the CPU driver
%ctest -LE 'cpu_fail'
%endif

%files
%doc README.md doc/sphinx/source/*.rst
# TODO: Unbundle the STC headers
%license COPYING STC-LICENSE
%{_sysconfdir}/OpenCL/vendors/%{name}.icd
%{_libdir}/lib%{name}.so.2*
%{_datadir}/%{name}/
%{_libdir}/%{name}/

%files devel
%{_bindir}/poclcc
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
