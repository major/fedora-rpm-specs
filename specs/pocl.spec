# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
%undefine _include_frame_pointers

# Pin to a specific llvm version
%global llvm_ver 20

Name: pocl
Version: 7.0
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

BuildRequires: glew-devel
BuildRequires: hwloc-devel
BuildRequires: libedit-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGL-devel
BuildRequires: ocl-icd-devel
BuildRequires: uthash-devel
BuildRequires: zlib-devel

BuildRequires: cmake
BuildRequires: libtool
BuildRequires: ninja-build

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
find . -depth -name utlist.h -print -delete

%build
%global __cc_clang clang-%{llvm_ver}
%global __cxx_clang clang++-%{llvm_ver}
%global __cpp_clang clang-cpp-%{llvm_ver}
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_ICD:BOOL=ON \
    -DENABLE_CUDA:BOOL=OFF \
    -DENABLE_TESTS:BOOL=ON \
    -DENABLE_EXAMPLES:BOOL=OFF \
    -DPOCL_INSTALL_ICD_VENDORDIR=%{_sysconfdir}/OpenCL/vendors \
    -DEXTRA_KERNEL_CXX_FLAGS="%{optflags}" \
%ifarch %{ix86} %{x86_64} ppc64le
    -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch %{arm64}
    -DLLC_HOST_CPU="cortex-a53" \
%endif
%ifarch riscv64
    -DLLC_HOST_CPU="generic-rv64" \
%endif
    -DWITH_LLVM_CONFIG="llvm-config-%{llvm_ver}" \
    -DPOCL_ICD_ABSOLUTE_PATH:BOOL=OFF \
    -DENABLE_POCL_BUILDING:BOOL=ON
%cmake_build

%install
%cmake_install

%check
# Upstream supports running tests only on x86_64, but test everything anyway
%ifarch %{arm64} ppc64le s390x
# on non-x86, the fp16 tests fail since it isn't supported (technically it's unfinished on x86 too)
%global pocl_arched_test_excludes |^kernel/test_halfs_loopvec$|^kernel/test_halfs_cbs$|^kernel/test_printf_vectors_halfn_loopvec$|^kernel/test_printf_vectors_halfn_cbs$
%else
%global pocl_arched_test_excludes %{nil}
%endif
# PoCL doesn't support s390x, see rhbz#2396306. The tests fail badly (endian issues?) but removing a main arch from a package is a pain.
%ifnarch s390x
%ctest -E '^regression/test_rematerialized_alloca_load_with_outside_pr_users$|^workgroup/conditional_barrier_dynamic$%{pocl_arched_test_excludes}'
%endif

%files
%doc README.md doc/sphinx/source/*.rst
%license COPYING
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
