%global neo_major 25
%global neo_minor 35
%global neo_build 35096
%global neo_hotfix 9

%if 0%{?rhel}
%global use_system_headers  0
%else
%global use_system_headers  1
%endif

Name: intel-compute-runtime
Version: %{neo_major}.%{neo_minor}.%{neo_build}.%{neo_hotfix}
Release: %autorelease
Summary: Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL

#LTO is controlled in compute-runtime itself, but temp disable it here
%global _lto_cflags %{nil}

License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

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
The Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL
Driver is an open-source project supporting computations for Intel graphics
hardware architectures using oneAPI Level Zero and Open Computing Language
(OpenCL) APIs.

%package -n    intel-ocloc
Summary:       Tool for managing Intel Compute GPU device binary format

%description -n intel-ocloc
ocloc is a tool for managing Intel Compute GPU device binary format (a format
used by Intel Compute GPU runtime). It can be used for generation (as part of
'compile' command) as well as manipulation (decoding/modifying - as part of
'disasm'/'asm' commands) of such binary files.

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
Runtime library providing the ability to use Intel GPUs with the oneAPI Level
Zero programming interface. Level Zero is the primary low-level interface for
language and runtime libraries. Level Zero offers fine-grain control over
accelerators capabilities, delivering a simplified and low-latency interface to
hardware, and efficiently exposing hardware capabilities to applications.

%package -n    intel-level-zero-devel
Summary:       oneAPI L0 support implementation for Intel GPUs - Devel Files
Requires:      intel-level-zero%{?_isa} = %{version}-%{release}

%description -n intel-level-zero-devel
Devel files for developing against intel-level-zero

%prep
%autosetup -p1 -n compute-runtime-%{version}

# remove sse2neon completely as we're building just for x86(_64)
rm -rv third_party/sse2neon

%build
# mitigations are handled by the kernel, unnecessary for the GPU/userspace
# disabling mitigations adds up to 20% performance improvement
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DNEO_OCL_VERSION_MAJOR=%{neo_major} \
    -DNEO_OCL_VERSION_MINOR=%{neo_minor} \
    -DNEO_VERSION_BUILD=%{neo_build} \
    -DNEO_VERSION_HOTFIX=%{neo_hotfix} \
    -DSKIP_UNIT_TESTS=1 \
%if 0%{?use_system_headers}
    -DKHRONOS_GL_HEADERS_DIR="/usr/include/GL/" \
    -DKHRONOS_HEADERS_DIR="/usr/include/CL/" \
    -DNEO_DRM_HEADERS_DIR="/usr/src/kernels/`rpm -q --queryformat '%{Version}-%{Release}.%{Arch}\n' kernel-devel | tail -n1`/include/uapi/drm/" \
    -DNEO_I915_HEADERS_DIR="/usr/src/kernels/`rpm -q --queryformat '%{Version}-%{Release}.%{Arch}\n' kernel-devel | tail -n1`/include/uapi/drm/" \
    -DNEO_XE_HEADERS_DIR="/usr/src/kernels/`rpm -q --queryformat '%{Version}-%{Release}.%{Arch}\n' kernel-devel | tail -n1`/include/uapi/drm/" \
%endif
    -DNEO_ENABLE_I915_PRELIM_DETECTION=TRUE \
    -DNEO_ENABLE_XE_PRELIM_DETECTION=TRUE \
    -DNEO_DISABLE_MITIGATIONS=TRUE \
    -G Ninja

%cmake_build

%install
%cmake_install

# Compute-runtime only creates a specific /usr/bin/ocloc-version binary, due to
# the possibility of mutiple versions installed on the system. i.e. legacy pkg
%post -n intel-ocloc
update-alternatives --install /usr/bin/ocloc ocloc /usr/bin/ocloc-%{neo_major}.%{neo_minor}.1 %{neo_major}%{neo_minor}%{neo_build}

%preun -n intel-ocloc
if [ $1 == "0" ]; then
    # uninstall
    update-alternatives --remove ocloc /usr/bin/ocloc-%{neo_major}.%{neo_minor}.1
fi


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
%{_bindir}/ocloc-*
%{_libdir}/libocloc.so

%files -n intel-ocloc-devel
%{_includedir}/ocloc_api.h

%doc

%changelog
%autochangelog
