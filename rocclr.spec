# ROCclr loads comgr at run time by soversion, so this needs to be checked when
# updating this package as it's used for the comgr requires for opencl and hip:
%global comgr_maj_api_ver 2
# See the file "rocclr/device/comgrctx.cpp" for reference:
# https://github.com/ROCm-Developer-Tools/ROCclr/blob/develop/device/comgrctx.cpp#L62

%global llvm_maj_ver 17
%bcond_without compat_build

%global rocm_major 6
%global rocm_minor 0
%global rocm_patch 2
%global rocm_release %{rocm_major}.%{rocm_minor}
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocclr
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Compute Language Runtime
Url:            https://github.com/ROCm-Developer-Tools/clr
License:        MIT
Source0:        https://github.com/ROCm-Developer-Tools/clr/archive/refs/tags/rocm-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# TODO: it would be nice to separate this into its own package:
Source1:        https://github.com/ROCm-Developer-Tools/HIP/archive/refs/tags/rocm-%{version}.tar.gz#/HIP-%{version}.tar.gz
# TODO drop in 6.1 when HIPCC is merged into rocm-compilersupport
# Note: All the related bits to this is wrapped in 'TODO HIPCC' below
Source2:        https://github.com/ROCm-Developer-Tools/HIPCC/archive/refs/tags/rocm-%{version}.tar.gz#/HIPCC-%{version}.tar.gz

# Revert patch: this causes some issues with upstream LLVM 16 (RHBZ#2207599)
#https://github.com/ROCm-Developer-Tools/ROCclr/commit/041c00465b7adcee78085dc42253d42d1bb1f250
Patch4:         0001-Revert-SWDEV-325538-Enable-code-object-v5-by-default.patch

# a fix for building blender
Patch8:         0001-add-long-variants-for-__ffsll.patch

# https://github.com/ROCm/clr/pull/69
Patch9:         0001-Check-p2p_agents_list_-before-deleting.patch

BuildRequires:  cmake
%if %{with compat_build}
BuildRequires:  clang%{llvm_maj_ver}-devel
BuildRequires:  llvm%{llvm_maj_ver}-devel
%else
BuildRequires:  clang-devel
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  python3-cppheaderparser
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocminfo >= %{rocm_release}
BuildRequires:  rocm-runtime-devel >= %{rocm_release}
BuildRequires:  zlib-devel

# ROCclr relise on some x86 intrinsics
# 32bit userspace is excluded as it likely doesn't work and is not very useful
ExclusiveArch:  x86_64

# rocclr bundles OpenCL 2.2 headers
# Some work is needed to unbundle this, as it fails to compile with latest
Provides:       bundled(opencl-headers) = 2.2

%description
ROCm Compute Language Runtime

%package -n rocm-opencl
Summary:        ROCm OpenCL platform and device tool
Requires:       comgr(major) = %{comgr_maj_api_ver}
Requires:       ocl-icd%{?_isa}
Requires:       opencl-filesystem

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

%package -n rocm-hip
Summary:        ROCm HIP platform and device tool
Requires:       comgr(major) = %{comgr_maj_api_ver}
Requires:       hipcc = %{version}-%{release}

%description -n rocm-hip
HIP is a C++ Runtime API and Kernel Language that allows developers to create
portable applications for AMD and NVIDIA GPUs from the same source code.

%package -n rocm-hip-devel
Summary:        ROCm HIP development package
Requires:       rocm-hip%{?_isa} = %{version}-%{release}
Requires:       rocm-comgr-devel
Requires:       rocm-runtime-devel >= %{rocm_release}
Provides:       hip-devel = %{version}-%{release}

%description -n rocm-hip-devel
ROCm HIP development package.

#TODO HIPCC
%package -n hipcc
Summary:        HIP compiler driver
BuildArch:      noarch
# hipcc requirements:
Requires:       rocminfo >= %{rocm_release}
# 16.2 has an important fix for hipcc to work out of the box:
Requires:       rocm-device-libs >= 16.2
%if %{with compat_build}
Requires:       clang%{llvm_maj_ver}
Requires:       clang%{llvm_maj_ver}-devel
Requires:       compiler-rt%{llvm_maj_ver}
Requires:       lld%{llvm_maj_ver}
Requires:       llvm%{llvm_maj_ver}-devel
%else
Requires:       clang
Requires:       clang-devel
Requires:       compiler-rt
Requires:       lld
Requires:       llvm-devel
%endif
# Renamed hip to hipcc to prepare for hipcc package split
Provides:       hip = %{version}-%{release}
Obsoletes:      hip < 5.6.0

%description -n hipcc
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.
#END TODO HIPCC

%package -n hip-doc
Summary:        HIP API documentation package
BuildArch:      noarch

%description -n hip-doc
This package contains documentation for the hip package

%prep
%autosetup -N -a 1 -n clr-rocm-%{version}

# ROCclr patches
%autopatch -p1 -M 99

# Enable experimental pre vega platforms
sed -i 's/\(ROC_ENABLE_PRE_VEGA.*\)false/\1true/' rocclr/utils/flags.hpp

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

pushd HIP-rocm-%{version}

#TODO HIPCC
gzip -dc %{SOURCE2} | tar --strip-components=1 -xof -

# HIP patches
%autopatch -p1 -m 100

#TODO HIPCC
# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' bin/hipcc.pl
# Drop some unnecessary includes:
sed -i '/^# Add paths to common HIP includes:/,/^$HIPCFLAGS/d' bin/hipcc.pl
#END TODO HIPCC

# HIPCC to use the compat version of clang
%if %{with compat_build}
sed -i 's| or -e "$HIP_PATH/bin/clang"||' bin/hipvars.pm
sed -i 's|llvm/bin|lib64/llvm%{llvm_maj_ver}/bin|' bin/hipvars.pm
sed -i 's|-e "$HIP_ROCCLR_HOME/bin/clang" or ||' bin/hipvars.pm
%endif

# Disable doxygen timestamps:
sed -i 's/^\(HTML_TIMESTAMP.*\)YES/\1NO/' docs/doxygen-input/doxy.cfg

popd

%build

%if %{with compat_build}
export PATH=%{_libdir}/llvm%{llvm_maj_ver}/bin:$PATH
%endif

# PCH appears to be broken for aarch64, just disable for now
%cmake \
%ifarch aarch64
    -D__HIP_ENABLE_PCH=OFF \
%endif
    -DCMAKE_SHARED_LINKER_FLAGS=-Wl,-z,noexecstack \
    -DHIP_COMMON_DIR=$(realpath HIP-rocm-%{version}) \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DHIPCC_BIN_DIR=$(realpath HIP-rocm-%{version})/bin \
    -DHIP_PLATFORM=amd \
    -DROCM_PATH=%{_prefix} \
    -DBUILD_ICD=OFF \
    -DCLR_BUILD_HIP=ON \
    -DCLR_BUILD_OCL=ON \
    -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

# Install OpenCL ICD configuration:
install -D -m 644 opencl/config/amdocl64.icd \
    %{buildroot}%{_sysconfdir}/OpenCL/vendors/amdocl64.icd

# Avoid file conflicts with opencl-headers package:
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/CL %{buildroot}%{_includedir}/%{name}/CL

# Avoid file conflicts with clinfo package:
mv %{buildroot}%{_bindir}/clinfo %{buildroot}%{_bindir}/rocm-clinfo

#TODO HIPCC
# Fix perl module files installation:
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{_bindir}/hip*.pm %{buildroot}%{perl_vendorlib}
# Eventually upstream plans to deprecate Perl usage, see HIPCC README:
# https://github.com/ROCm-Developer-Tools/HIPCC/blob/develop/README.md
#END TODO HIPCC

# Clean up file dupes
%fdupes %{buildroot}/%{_docdir}/hip

# TODO send upstream a patch, libhip should be installed with cmake's 'TARGETS'
chmod 755 %{buildroot}%{_libdir}/lib*.so*

%files -n rocm-opencl
%license opencl/LICENSE.txt
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl64.icd
%{_libdir}/libamdocl64.so.%{rocm_major}{,.*}
%{_libdir}/libcltrace.so.%{rocm_major}{,.*}
#Duplicated files:
%exclude %{_docdir}/opencl*/LICENSE*

%files -n rocm-opencl-devel
%{_libdir}/libamdocl64.so
%{_libdir}/libcltrace.so
%{_includedir}/%{name}

%files -n rocm-clinfo
%license opencl/LICENSE.txt
%{_bindir}/rocm-clinfo

%files -n rocm-hip
%doc hipamd/README.md
%license hipamd/LICENSE.txt
%{_libdir}/libamdhip64.so.%{rocm_major}{,.*}
%{_libdir}/libhiprtc.so.%{rocm_major}{,.*}
%{_libdir}/libhiprtc-builtins.so.%{rocm_major}{,.*}
%{_datadir}/hip
#Duplicated files:
%exclude %{_docdir}/hip*/LICENSE*

%files -n rocm-hip-devel
%{_bindir}/roc-*
%{_libdir}/libamdhip64.so
%{_libdir}/libhiprtc.so
%{_libdir}/libhiprtc-builtins.so
%{_libdir}/cmake/hip*
%{_bindir}/hipdemangleatp
%{_bindir}/hipcc_cmake_linker_helper
%{_includedir}/hip
%{_includedir}/hip_prof_str.h
# Unnecessary file and is not FHS compliant:
%exclude %{_libdir}/.hipInfo

#TODO HIPCC
%doc HIP-rocm-%{version}/README.md
%license HIP-rocm-%{version}/LICENSE.txt
%files -n hipcc
%{_bindir}/hipcc{,.pl}
%{_bindir}/hipconfig{,.pl}
%{perl_vendorlib}/hip*.pm
# Don't include windows files
%exclude %{_bindir}/*.bat
#END TODO HIPCC

%files -n hip-doc
%license HIP-rocm-%{version}/LICENSE.txt
%{_docdir}/hip

%changelog
%autochangelog
