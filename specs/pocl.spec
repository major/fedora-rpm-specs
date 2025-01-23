# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
%undefine _include_frame_pointers

# Use Clang for building this project
%global toolchain clang

# Sometimes releases require legacy versions of LLVM
%if 0%{?fedora} && 0%{?fedora} >= 41
%global llvm_legacy 1
%else
%global llvm_legacy 0
%endif
%global llvm_legacy_ver 18

Name: pocl
Version: 6.0
Release: %autorelease

# The entire code is under MIT
# include/utlist.h which is under BSD-1-Clause (unbundled)
# lib/kernel/vecmath which is under GPL-3.0-or-later OR LGPL-3.0-or-later
License: MIT AND BSD-1-Clause AND (GPL-3.0-or-later OR LGPL-3.0-or-later)
Summary: Portable Computing Language - an OpenCL implementation
URL: https://github.com/%{name}/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Add missing includes for modern libstdc++ versions
Patch100: %{name}-6.0-add-missing-includes.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

%if %{llvm_legacy}
BuildRequires: clang%{llvm_legacy_ver}
BuildRequires: clang%{llvm_legacy_ver}-devel
BuildRequires: compiler-rt%{llvm_legacy_ver}
BuildRequires: llvm%{llvm_legacy_ver}-devel
%else
BuildRequires: clang
BuildRequires: clang-devel
BuildRequires: compiler-rt
BuildRequires: llvm-devel
%endif

BuildRequires: cmake
BuildRequires: glew-devel
BuildRequires: hwloc-devel
BuildRequires: libedit-devel
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGL-devel
BuildRequires: ninja-build
BuildRequires: ocl-icd-devel
BuildRequires: uthash-devel
BuildRequires: zlib-devel

# https://bugzilla.redhat.com/show_bug.cgi?id=1082364
Requires: libstdc++-devel%{?_isa}
# Runtime dependency, because libm.so is required for kernels
Requires: glibc-devel%{?_isa}

%description
Pocl's goal is to become an efficient open source (MIT-licensed) implementation
of the OpenCL 1.2 (and soon OpenCL 2.0) standard.

In addition to producing an easily portable open-source OpenCL implementation,
another major goal of this project is improving performance portability of
OpenCL programs with compiler optimizations, reducing the need for
target-dependent manual optimizations.

At the core of pocl is the kernel compiler that consists of a set of LLVM
passes used to statically transform kernels into work-group functions with
multiple work-items, even in the presence of work-group barriers. These
functions are suitable for parallelization in multiple ways (SIMD, VLIW,
superscalar,...).

%package devel
Summary: Portable Computing Language development files
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{llvm_legacy}
Requires: clang%{llvm_legacy_ver}
%else
Requires: clang%{?_isa}
%endif
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
%if %{llvm_legacy}
export CC="clang-%{llvm_legacy_ver}"
export CXX="clang++-%{llvm_legacy_ver}"
%endif
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_ICD:BOOL=ON \
    -DENABLE_CUDA:BOOL=OFF \
    -DENABLE_TESTS:BOOL=OFF \
    -DENABLE_EXAMPLES:BOOL=OFF \
    -DPOCL_INSTALL_ICD_VENDORDIR=%{_sysconfdir}/OpenCL/vendors \
    -DEXTRA_KERNEL_CXX_FLAGS="%{optflags}" \
%ifarch x86_64
    -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch aarch64
    -DLLC_HOST_CPU="cortex-a53" \
%endif
%ifarch riscv64
    -DLLC_HOST_CPU="generic-rv64" \
%endif
%if %{llvm_legacy}
    -DWITH_LLVM_CONFIG="llvm-config-%{llvm_legacy_ver}" \
%endif
    -DPOCL_ICD_ABSOLUTE_PATH:BOOL=OFF \
    -DENABLE_POCL_BUILDING:BOOL=ON
%cmake_build

%install
%cmake_install

%check
# Upstream support running tests only on x86_64
%ifarch x86_64
%ctest
%endif

%files
%doc README.md doc/sphinx/source/*.rst
%license LICENSE
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
