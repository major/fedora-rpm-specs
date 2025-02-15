%global neo_major 25
%global neo_minor 05
%global neo_build 32567.12

Name: intel-compute-runtime
Version: %{neo_major}.%{neo_minor}.%{neo_build}
Release: %autorelease
Summary: Compute API support for Intel graphics

%if 0%{?rhel}
%global patch_new_headers  0
%else
%global patch_new_headers  1
%endif

%global _lto_cflags %{nil}
%global optflags %{optflags} -Wno-error=maybe-uninitialized

License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

# Support opencl-headers-2024.10.24
%if 0%{?patch_new_headers}
Patch01: 0001-CL-Headers-2024.10.24.patch
%endif

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: intel-gmmlib-devel
BuildRequires: libva-devel
BuildRequires: libdrm-devel
BuildRequires: kernel-devel
BuildRequires: intel-igc-devel
BuildRequires: ninja-build
BuildRequires: libglvnd-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers
BuildRequires: oneapi-level-zero-devel

# This doesn't get added automatically, so specify it explicitly
Requires: intel-igc

# Let compute-runtime be a meta package for intel-ocloc, intel-opencl and intel-level-zero
Requires: intel-ocloc = %{version}-%{release}
Requires: intel-opencl = %{version}-%{release}
Requires: intel-level-zero = %{version}-%{release}

# prelim/drm
Provides: bundled(drm-uapi-helper)

%description
The Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL Driver is an open source project
providing compute API support (Level Zero, OpenCL) for Intel graphics hardware architectures (HD Graphics, Xe).

%package -n    intel-ocloc
Summary:       Tool for managing Intel Compute GPU device binary format

%description -n intel-ocloc
ocloc is a tool for managing Intel Compute GPU device binary format (a format used by Intel Compute GPU runtime).
It can be used for generation (as part of 'compile' command) as well as
manipulation (decoding/modifying - as part of 'disasm'/'asm' commands) of such binary files.

%package -n    intel-ocloc-devel
Summary:       Tool for managing Intel Compute GPU device binary format - Devel Files
Requires:      intel-ocloc%{?_isa} = %{version}-%{release}

%description -n intel-ocloc-devel
Devel files (headers and libraries) for developing against
intel-ocloc (a tool for managing Intel Compute GPU device binary format).

%package -n    intel-opencl
Summary:       OpenCL support implementation for Intel GPUs
Requires:      intel-igc-libs%{?_isa}
Requires:      intel-gmmlib%{?_isa}

%description -n intel-opencl
Implementation for the Intel GPUs of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package -n    intel-level-zero
Summary:       oneAPI L0 support implementation for Intel GPUs
Requires:      intel-igc-libs%{?_isa}
Requires:      intel-gmmlib%{?_isa}
# In some references, the package is named intel-level-zero-gpu, so provide that for convenience too
Provides:      intel-level-zero-gpu%{?_isa}

%description -n intel-level-zero
Implementation for the Intel GPUs of the oneAPI L0 specification -  which provides direct-to-metal
interfaces to offload accelerator devices. Its programming interface can be tailored to any device
needs and can be adapted to support broader set of languages features such as function pointers,
virtual functions, unified memory, and I/O capabilities..

%package -n    intel-level-zero-devel
Summary:       oneAPI L0 support implementation for Intel GPUs - Devel Files
Requires:      intel-level-zero%{?_isa} = %{version}-%{release}

%description -n intel-level-zero-devel
Devel files for developing against intel-level-zero (oneAPI L0 support implementation for Intel GPUs).

%prep
%autosetup -p1 -n compute-runtime-%{version}

# remove sse2neon completely as we're building just for x86(_64)
rm -rv third_party/sse2neon

# bundled CL headers are leaking into the build
%if 0%{?patch_new_headers}
rm -rv third_party/opencl_headers/CL
ln -s /usr/include/CL/ third_party/opencl_headers/CL
%endif

%build
# -DNEO_DISABLE_LD_GOLD=1 for https://bugzilla.redhat.com/show_bug.cgi?id=2043178 and https://bugzilla.redhat.com/show_bug.cgi?id=2043758
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DNEO_OCL_VERSION_MAJOR=%{neo_major} \
    -DNEO_OCL_VERSION_MINOR=%{neo_minor} \
    -DNEO_VERSION_BUILD=%{neo_build} \
    -DSKIP_UNIT_TESTS=1 \
    -DNEO_DISABLE_LD_GOLD=1 \
    -DKHRONOS_GL_HEADERS_DIR="/usr/include/GL/" \
%if 0%{?patch_new_headers}
    -DKHRONOS_HEADERS_DIR="/usr/include/CL/" \
%endif
    -DNEO_DRM_HEADERS_DIR="/usr/src/kernels/`rpm -q --queryformat '%{Version}-%{Release}.%{Arch}\n' kernel-devel | tail -n1`/include/uapi/drm/" \
    -DNEO_I915_HEADERS_DIR="/usr/src/kernels/`rpm -q --queryformat '%{Version}-%{Release}.%{Arch}\n' kernel-devel | tail -n1`/include/uapi/drm/" \
    -DNEO_XE_HEADERS_DIR="/usr/src/kernels/`rpm -q --queryformat '%{Version}-%{Release}.%{Arch}\n' kernel-devel | tail -n1`/include/uapi/drm/" \
    -DCL_TARGET_OPENCL_VERSION=300 \
    -G Ninja

%cmake_build

%install
%cmake_install
# Symlink to provide ocloc
pushd %{buildroot}%{_bindir}
ln -s ocloc-* ocloc
popd

%files

%files -n intel-opencl
%license LICENSE.md
%dir %{_libdir}/intel-opencl/
%{_libdir}/intel-opencl/libigdrcl.so
%{_sysconfdir}/OpenCL/vendors/intel.icd

%files -n intel-level-zero
%license LICENSE.md
%{_libdir}/libze_intel_gpu.so.*

%files -n intel-level-zero-devel
%{_includedir}/level_zero/*.h
%{_includedir}/level_zero/driver_experimental/*.h

%files -n intel-ocloc
%license LICENSE.md
%{_bindir}/ocloc
%{_bindir}/ocloc-*
%{_libdir}/libocloc.so

%files -n intel-ocloc-devel
%{_includedir}/ocloc_api.h

%doc

%changelog
%autochangelog
