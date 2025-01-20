# ROCclr loads comgr at run time by soversion, so this needs to be checked when
# updating this package as it's used for the comgr requires for opencl and hip:
%global comgr_maj_api_ver 2
# See the file "rocclr/device/comgrctx.cpp" for reference:
# https://github.com/ROCm-Developer-Tools/ROCclr/blob/develop/device/comgrctx.cpp#L62

%global rocm_major 6
%global rocm_minor 3
%global rocm_patch 1
%global rocm_release %{rocm_major}.%{rocm_minor}
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain clang

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%if 0%{?fedora}
%bcond_without cppheaderparser
%else
%bcond_with cppheaderparser
%endif
%if %{with cppheaderparser}
%global build_prof_api ON
%else
%global build_prof_api OFF
%endif

%if 0%{?rhel} && 0%{?rhel} < 10
# No ocl-icd-devel in cs9
%bcond_with ocl
%else
%bcond_without ocl
%endif
%if %{with ocl}
%global build_ocl ON
%else
%global build_ocl OFF
%endif

%bcond_with docs

Name:           rocclr
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        ROCm Compute Language Runtime
Url:            https://github.com/ROCm-Developer-Tools/clr
License:        MIT
Source0:        https://github.com/ROCm-Developer-Tools/clr/archive/refs/tags/rocm-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# TODO: it would be nice to separate this into its own package:
Source1:        https://github.com/ROCm-Developer-Tools/HIP/archive/refs/tags/rocm-%{version}.tar.gz#/HIP-%{version}.tar.gz

# Revert patch: this causes some issues with upstream LLVM 16 (RHBZ#2207599)
#https://github.com/ROCm-Developer-Tools/ROCclr/commit/041c00465b7adcee78085dc42253d42d1bb1f250
# Patch4:         0001-Revert-SWDEV-325538-Enable-code-object-v5-by-default.patch

# a fix for building blender
Patch8:         0001-add-long-variants-for-__ffsll.patch

# https://github.com/ROCm/clr/pull/69
Patch9:         0001-Check-p2p_agents_list_-before-deleting.patch

#https://github.com/ROCm/clr/pull/97
patch10:        https://github.com/ROCm/clr/pull/97/commits/909fa3dcb644f7ca422ed1a980a54ac426d831b1.patch

# https://github.com/ROCm/clr/issues/99
# patch11:        0001-handle-v1-of-compressed-fatbins.patch

BuildRequires:  cmake
%if %{with docs}
BuildRequires:  doxygen
%endif
%if 0%{?fedora}
BuildRequires:  fdupes
BuildRequires:  perl-generators
%endif
BuildRequires:  gcc-c++
BuildRequires:  hipcc
BuildRequires:  libffi-devel
BuildRequires:  perl
%if 0%{?suse_version}
BuildRequires:  pkgconfig(gl)
%elif 0%{?rhel} && 0%{?rhel} < 10
BuildRequires:  libglvnd-devel
%else
BuildRequires:  pkgconfig(opengl)
%endif
%if %{with ocl}
BuildRequires:  pkgconfig(ocl-icd)
%endif
BuildRequires:  pkgconfig(numa)
%if %{with cppheaderparser}
BuildRequires:  python3-cppheaderparser
%endif
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-runtime-devel >= %{rocm_release}
BuildRequires:  zlib-devel

# ROCclr relies on some x86 intrinsics
# 32bit userspace is excluded as it likely doesn't work and is not very useful
# Also depends on rocm-runtime which doesn't build non x86
ExclusiveArch:  x86_64

%if %{with ocl}
# rocclr bundles OpenCL 2.2 headers
# Some work is needed to unbundle this, as it fails to compile with latest
Provides:       bundled(opencl-headers) = 2.2
%endif

%description
ROCm Compute Language Runtime

%if %{with ocl}
%package -n rocm-opencl
Summary:        ROCm OpenCL platform and device tool
Requires:       comgr(major) = %{comgr_maj_api_ver}
%if 0%{?rhel} || 0%{?fedora}
Requires:       ocl-icd%{?_isa}
Requires:       opencl-filesystem
%endif

%description -n rocm-opencl
ROCm OpenCL language runtime.
Supports offline and in-process/in-memory compilation.

%package -n rocm-opencl-devel
Summary:        ROCm OpenCL development package
Requires:       rocm-opencl%{?_isa} = %{version}-%{release}
Requires:       ocl-icd-devel%{?_isa}

%description -n rocm-opencl-devel
The AMD ROCm OpenCL development package.

%package -n rocm-clinfo
Summary:        ROCm OpenCL platform and device tool

%description -n rocm-clinfo
A simple ROCm OpenCL application that enumerates all possible platform and
device information.
%endif

%package -n rocm-hip
Summary:        ROCm HIP platform and device tool
Requires:       comgr(major) = %{comgr_maj_api_ver}
Requires:       hipcc

%description -n rocm-hip
HIP is a C++ Runtime API and Kernel Language that allows developers to create
portable applications for AMD and NVIDIA GPUs from the same source code.

%package -n rocm-hip-devel
Summary:        ROCm HIP development package
Requires:       rocm-hip%{?_isa} = %{version}-%{release}
Requires:       rocm-comgr-devel
Requires:       rocm-runtime-devel >= %{rocm_release}
Provides:       hip-devel = %{version}-%{release}
Obsoletes:      hip-devel < 6.0.0

%description -n rocm-hip-devel
ROCm HIP development package.

%if %{with docs}
%package -n hip-doc
Summary:        HIP API documentation package
BuildArch:      noarch

%description -n hip-doc
This package contains documentation for the hip package
%endif

%prep
%autosetup -N -a 1 -n clr-rocm-%{version}

# ROCclr patches
%autopatch -p1

# Disable RPATH
# https://github.com/ROCm-Developer-Tools/hipamd/issues/22
sed -i '/INSTALL_RPATH/d' \
    opencl/tools/clinfo/CMakeLists.txt hipamd/CMakeLists.txt

# Upstream doesn't want OpenCL sonames because they don't guarantee API/ABI.
# For Fedora, SOVERSION can be major.minor (i.e. rocm_release) as rocm patch
# releases are very unlikely to break anything:
echo "set_target_properties(amdocl PROPERTIES VERSION %{version} SOVERSION %rocm_release)" \
    >> opencl/amdocl/CMakeLists.txt
echo "libamdocl64.so.%{rocm_release}" > opencl/config/amdocl64.icd
echo "set_target_properties(cltrace PROPERTIES VERSION %{version} SOVERSION %rocm_release)" \
    >> opencl/tools/cltrace/CMakeLists.txt

# Clean up unused bundled code
# Only keep opencl2.2 headers as are they needed for now:
ls -d opencl/khronos/* | grep -v headers | xargs rm -r
ls -d opencl/khronos/headers/* | grep -v opencl2.2 | xargs rm -r
# Unused opencl 2.2 test code:
rm -r opencl/khronos/headers/opencl2.2/tests/

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' hipamd/src/CMakeLists.txt

# Stop cmake from trying to install HIPCC again:
sed -i "/install(PROGRAMS.*{[Hh][Ii][Pp][Cc]/d" hipamd/CMakeLists.txt

# Disable doxygen timestamps:
sed -i 's/^\(HTML_TIMESTAMP.*\)YES/\1NO/' \
    HIP-rocm-%{version}/docs/doxygen-input/doxy.cfg

%build

p=$PWD

%cmake \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DHIP_COMMON_DIR=$p/HIP-rocm-%{version} \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DHIPCC_BIN_DIR=%{_bindir} \
    -DHIP_PLATFORM=amd \
    -DROCM_PATH=%{_prefix} \
    -DBUILD_ICD=OFF \
    -DCLR_BUILD_HIP=ON \
    -DCLR_BUILD_OCL=%{build_ocl} \
    -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DHIP_ENABLE_ROCPROFILER_REGISTER=OFF \
    -DUSE_PROF_API=%{build_prof_api} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_BUILD_TYPE=%{build_type}
%cmake_build

%install
%cmake_install

%if %{with ocl}
# Install OpenCL ICD configuration:
install -D -m 644 opencl/config/amdocl64.icd \
    %{buildroot}%{_sysconfdir}/OpenCL/vendors/amdocl64.icd

# Avoid file conflicts with opencl-headers package:
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/CL %{buildroot}%{_includedir}/%{name}/CL

# Avoid file conflicts with clinfo package:
mv %{buildroot}%{_bindir}/clinfo %{buildroot}%{_bindir}/rocm-clinfo
%endif

# Clean up file dupes
%if 0%{?fedora}
%fdupes %{buildroot}/%{_docdir}/hip
%endif

# TODO send upstream a patch, libhip should be installed with cmake's 'TARGETS'
chmod 755 %{buildroot}%{_libdir}/lib*.so*

# Unnecessary file and is not FHS compliant:
rm %{buildroot}%{_libdir}/.hipInfo

# Windows files:
rm %{buildroot}%{_bindir}/*.bat

if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocclr/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocclr*/LICENSE.txt
fi
if [ -f %{buildroot}%{_prefix}/share/doc/opencl/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/opencl*/LICENSE.txt
fi
if [ -f %{buildroot}%{_prefix}/share/doc/hip-asan/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/hip-asan/LICENSE.txt
fi
if [ -f %{buildroot}%{_prefix}/share/doc/hip/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/hip/LICENSE.txt
fi


%if %{with ocl}
%files -n rocm-opencl
%if 0%{?suse_version}
%dir %{_sysconfdir}/OpenCL/
%dir %{_sysconfdir}/OpenCL/vendors
%endif
%license opencl/LICENSE.txt
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl64.icd
%{_libdir}/libamdocl64.so.%{rocm_major}{,.*}
%{_libdir}/libcltrace.so.%{rocm_major}{,.*}

%files -n rocm-opencl-devel
%{_libdir}/libamdocl64.so
%{_libdir}/libcltrace.so
%{_includedir}/%{name}

%files -n rocm-clinfo
%license opencl/LICENSE.txt
%{_bindir}/rocm-clinfo
%endif

%files -n rocm-hip
%license hipamd/LICENSE.txt
%{_libdir}/libamdhip64.so.%{rocm_major}{,.*}
%{_libdir}/libhiprtc.so.%{rocm_major}{,.*}
%{_libdir}/libhiprtc-builtins.so.%{rocm_major}{,.*}
%{_datadir}/hip

%files -n rocm-hip-devel
%{_bindir}/roc-*
%{_libdir}/libamdhip64.so
%{_libdir}/libhiprtc.so
%{_libdir}/libhiprtc-builtins.so
%{_libdir}/cmake/hip*
%{_bindir}/hipdemangleatp
%{_bindir}/hipcc_cmake_linker_helper
%{_includedir}/hip
%if %{with cppheaderparser}
%{_includedir}/hip_prof_str.h
%endif

%if %{with docs}
%files -n hip-doc
%license HIP-rocm-%{version}/LICENSE.txt
%{_docdir}/hip
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Jeremy Newton <alexjnewt@hotmail.com> - 6.3.1-2
- We dropped the hip-devel package in 6.0 and forgot to obsolete it
- Fixes RHBZ#2327258

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Sun Dec 8 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Tue Sep 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.0-1
- A placeholder for rhel 9
