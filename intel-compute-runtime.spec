%global neo_major 22
%global neo_minor 43
%global neo_build 24558

Name: intel-compute-runtime
Version: %{neo_major}.%{neo_minor}.%{neo_build}
Release: 1%{?dist}
Summary: Compute API support for Intel graphics

%global _lto_cflags %{nil}
%global optflags %{optflags} -Wno-error=odr -Wno-error=implicit-fallthrough= -Wno-error=mismatched-new-delete

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
BuildRequires: intel-igc-devel
BuildRequires: ninja-build
BuildRequires: libglvnd-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers
# level-zero to be added later on

# This doesn't get added automatically, so specify it explicitly
Requires: intel-igc

# Let compute-runtime be a meta package for intel-ocloc and intel-opencl
Requires: intel-ocloc = %{version}-%{release}
Requires: intel-opencl = %{version}-%{release}

# prelim/drm
Provides: bundled(drm-uapi-helper)

# drm.h and others
Provides: bundled(libdrm-devel)

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

%prep
%autosetup -p1 -n compute-runtime-%{version}

# remove sse2neon completely as we're building just for x86(_64)
rm -rv third_party/sse2neon

# Replace bundled drm.h and i915_drm.h with files provided by libdrm-devel
# Uncomment once upstream gets the missing definitions
#find %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/ ! -name 'intel_hwconfig_types.h' ! -name 'i915_drm_prelim.h' -type f -delete
#cp /usr/include/libdrm/drm_fourcc.h %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/drm/
#cp /usr/include/libdrm/drm.h %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/drm/
#cp /usr/include/libdrm/drm_mode.h %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/drm/
#cp /usr/include/libdrm/i915_drm.h %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/drm/
#cp -r %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/drm %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/prelim/
#cp -r %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/drm %%{_builddir}/compute-runtime-%%{version}/third_party/uapi/dg1/

%build
# -DNEO_DISABLE_LD_GOLD=1 for https://bugzilla.redhat.com/show_bug.cgi?id=2043178 and https://bugzilla.redhat.com/show_bug.cgi?id=2043758
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DNEO_OCL_VERSION_MAJOR=%{neo_major} \
    -DNEO_OCL_VERSION_MINOR=%{neo_minor} \
    -DNEO_VERSION_BUILD=%{neo_build} \
    -DSUPPORT_DG1=ON \
    -DSKIP_UNIT_TESTS=1 \
    -DNEO_DISABLE_LD_GOLD=1 \
    -DKHRONOS_GL_HEADERS_DIR="/usr/include/GL/" \
    -DKHRONOS_HEADERS_DIR="/usr/include/CL/" \
    -DCL_TARGET_OPENCL_VERSION=300 \
    -G Ninja

%cmake_build

%install
%cmake_install

%files

%files -n intel-opencl
%license LICENSE.md
%{_libdir}/intel-opencl/libigdrcl.so
# Uncomment once we get level-zero
#%%{_libdir}/libze_intel_gpu.so*
%{_sysconfdir}/OpenCL/vendors/intel.icd

%files -n intel-ocloc
%license LICENSE.md
%{_bindir}/ocloc
%{_libdir}/libocloc.so

%files -n intel-ocloc-devel
%{_includedir}/ocloc_api.h

%doc

%changelog
* Tue Nov 29 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.43.24558-1
- intel-compute-runtime-22.43.24558 (fixes RHBZ#2135350 )

* Tue Aug 30 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.34.24023-1
- intel-compute-runtime-22.34.24023

* Wed Aug 17 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.32.23937-1
- intel-compute-runtime-22.32.23937

* Wed Aug 10 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.31.23852-1
- intel-compute-runtime-22.31.23852

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.26.23599-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.26.23599-1
- intel-compute-runtime-22.26.23599

* Sun May 29 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.21.23269-1
- intel-compute-runtime-22.21.23269

* Mon Mar 21 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.11.22682-1
- intel-compute-runtime-22.11.22682

* Sat Mar 19 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.10.22597-1
- intel-compute-runtime-22.10.22597
- disable lto and share libs

* Thu Mar 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.08.22549-1
- intel-compute-runtime-22.08.22549

* Fri Feb 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.07.22465-1
- intel-compute-runtime-22.07.22465

* Mon Dec 27 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 22.04.22286-1
- Initial package
