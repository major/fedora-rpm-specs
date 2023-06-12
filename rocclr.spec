# ROCclr loads comgr at run time by soversion, so this needs to be checked when
# updating this package as it's used for the comgr requires for opencl and hip:
%global comgr_maj_api_ver 2
# See the file "rocclr/device/comgrctx.cpp" for reference:
# https://github.com/ROCm-Developer-Tools/ROCclr/blob/develop/device/comgrctx.cpp#L62

%global rocm_release 5.5
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocclr
Version:        %{rocm_version}
Release:        8%{?dist}
Summary:        ROCm Compute Language Runtime
Url:            https://github.com/ROCm-Developer-Tools/clr
License:        MIT
Source0:        https://github.com/ROCm-Developer-Tools/ROCclr/archive/refs/tags/rocm-%{version}.tar.gz#/ROCclr-%{version}.tar.gz
# TODO: it would be nice to separate this into its own package:
Source1:        https://github.com/ROCm-Developer-Tools/HIP/archive/refs/tags/rocm-%{version}.tar.gz#/HIP-%{version}.tar.gz
# ROCm 5.7 will merge these sources with rocclr, for now they are separate:
Source2:        https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/archive/refs/tags/rocm-%{version}.tar.gz#/ROCm-OpenCL-Runtime-%{version}.tar.gz
Source3:        https://github.com/ROCm-Developer-Tools/hipamd/archive/refs/tags/rocm-%{version}.tar.gz#/hipamd-%{version}.tar.gz

# Patches to allow building ocl and hip at once:
Patch0:         https://github.com/ROCm-Developer-Tools/clr/commit/1bc186323fb83c6d2124a273d2d5a5c05de52bbe.patch
Patch1:         https://github.com/ROCm-Developer-Tools/clr/commit/d9ceb6a3a38581f72b0eb443b736a23a30bc82ec.patch
# Newer GCC fixes:
Patch2:         https://github.com/ROCm-Developer-Tools/clr/commit/158e79358c811c31adebd6e421e884c7f98b968c.patch
Patch3:         https://github.com/ROCm-Developer-Tools/clr/commit/70bdb7a5970d0c518c4ed494ea8cbb129ed3c598.patch

# Revert patch: this causes some issues with upstream LLVM 16 (RHBZ#2207599)
#https://github.com/ROCm-Developer-Tools/ROCclr/commit/041c00465b7adcee78085dc42253d42d1bb1f250
Patch4:         0001-Revert-SWDEV-325538-Enable-code-object-v5-by-default.patch

# HIPCC fixes for Fedora:
# https://github.com/ROCm-Developer-Tools/HIPCC/pull/83
Patch100:       0001-Improve-HIP_CLANG_INCLUDE-detection.patch
Patch101:       0002-Improve-HIP_CLANG_PATH-detection.patch

# Fix FHS compliance issue (currently working on an upstream-able patch):
Patch5:         0001-Install-.hipVersion-into-datadir.patch

# Moves FindHIP cmake to datadir, to fit better with hip-devel being noarch:
Patch6:         0002-Move-FindHIP-to-datadir.patch

# Upstream patches to let clang use the default hip device lib path:
Patch7:         https://github.com/ROCm-Developer-Tools/clr/commit/cbb393719633f5ade47efbe8d2946e5f649c1f22.patch
Patch102:       https://github.com/ROCm-Developer-Tools/HIP/commit/e18cbe64c173f6f9abf1b56f78cdd9bc7d4716d2.patch
Patch103:       https://github.com/ROCm-Developer-Tools/HIP/commit/802e3f439726b0c119f58de5dde8770cda75b2b0.patch

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  llvm-devel
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

# Only the following architectures are supported, since the kernel support only
# exists for x86_64, aarch64, and ppc64le:
ExclusiveArch:  x86_64 aarch64 ppc64le
# 32bit userspace is excluded as it likely doesn't work and is not very useful

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
Requires:       hip = %{version}-%{release}

%description -n rocm-hip
ROCm HIP implementation specifically for AMD platforms.

%package -n rocm-hip-devel
Summary:        ROCm HIP development package
Requires:       rocm-hip%{?_isa} = %{version}-%{release}
Requires:       hip-devel = %{version}-%{release}

%description -n rocm-hip-devel
ROCm HIP development package.

%package -n hip
Summary:        C++ Runtime API and Kernel Language
BuildArch:      noarch
# hipcc requirements:
Requires:       rocminfo >= %{rocm_release}
# 16.2 has an important fix for hipcc to work out of the box:
Requires:       rocm-device-libs >= 16.2
Requires:       clang

%description -n hip
HIP is a C++ Runtime API and Kernel Language that allows developers to create
portable applications for AMD and NVIDIA GPUs from the same source code.

%package -n hip-devel
Summary:        HIP API development package
BuildArch:      noarch
Requires:       hip = %{version}-%{release}

%description -n hip-devel
HIP API development package.

%package -n hip-doc
Summary:        HIP API documentation package
BuildArch:      noarch

%description -n hip-doc
This package contains documentation for the hip package

%prep
%autosetup -N -c -T -a 1 -n clr-rocm-%{version}
# TODO: use this for ROCm 5.7 or newer:
#autosetup -p1 -m 0 -M 99 -a 1 -n clr-rocm-{version}

# Extract/patch sources manually (this won't be required in ROCm 5.7 or later):
mkdir -p rocclr opencl hipamd
gzip -dc %{SOURCE0} | tar -C rocclr --strip-components=1 -xof -
gzip -dc %{SOURCE2} | tar -C opencl --strip-components=1 -xof -
gzip -dc %{SOURCE3} | tar -C hipamd --strip-components=1 -xof -
%autopatch -p1 -m 0 -M 99

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

# Fix libhip permissions:
# upstream has a fix but it's not published yet and history has diverged anyway
sed -i 's/FILES\(.*lib.*\.so\)/PROGRAMS\1/' hipamd/packaging/CMakeLists.txt

# HIP patches
pushd HIP-rocm-%{version}
%autopatch -p1 -m 100

# Fix script permissions:
chmod 755 bin/hipcc.pl
# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' bin/hipcc.pl
# Fix incorrect lib location in hipcc.pl (Fedora uses lib64):
# TODO: propose upstream fix
sed -i '/^# Add paths to common HIP includes:/,/^$HIPCFLAGS/d' bin/hipcc.pl

# Disable doxygen timestamps:
sed -i 's/^\(HTML_TIMESTAMP.*\)YES/\1NO/' docs/doxygen-input/doxy.cfg

popd

%build
# PCH appears to be broken for aarch64, just disable for now
%cmake \
%ifarch aarch64
    -D__HIP_ENABLE_PCH=OFF \
%endif
    -DCMAKE_SHARED_LINKER_FLAGS=-Wl,-z,noexecstack \
    -DHIP_COMMON_DIR=$(realpath HIP-rocm-%{version}) \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
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

# Fix perl module files installation:
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{_bindir}/hip*.pm %{buildroot}%{perl_vendorlib}
# Eventually upstream plans to deprecate Perl usage, see HIPCC README:
# https://github.com/ROCm-Developer-Tools/HIPCC/blob/develop/README.md

# Clean up file dupes
%fdupes %{buildroot}/%{_docdir}/hip
# Note: fdupes doesn't work correctly with the following, so it's done manually
for i in %{buildroot}/%{_libdir}/cmake/hip{rtc,-lang}/*-config-version.cmake; do
    if cmp -s $i %{buildroot}/%{_libdir}/cmake/hip/hip-config-version.cmake
    then
        ln -fs ../hip/hip-config-version.cmake $i
    fi
done
if cmp -s %{buildroot}/%{_includedir}/hip/amd_detail/hip_prof_str.h \
    %{buildroot}/%{_includedir}/hip_prof_str.h; then
    ln -fs hip/amd_detail/hip_prof_str.h %{buildroot}/%{_includedir}
fi

%files -n rocm-opencl
%license opencl/LICENSE.txt
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl64.icd
%{_libdir}/libamdocl64.so.5{,.*}
%{_libdir}/libcltrace.so.5{,.*}
#Duplicated files:
%exclude %{_docdir}/*/LICENSE*

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
%{_libdir}/libamdhip64.so.5{,.*}
%{_libdir}/libhiprtc.so.5{,.*}
%{_libdir}/libhiprtc-builtins.so.5{,.*}

%files -n rocm-hip-devel
%{_bindir}/roc-*
%{_libdir}/libamdhip64.so
%{_libdir}/libhiprtc.so
%{_libdir}/libhiprtc-builtins.so
%{_libdir}/cmake/hip*
# Unnecessary file and is not FHS compliant:
%exclude %{_libdir}/.hipInfo

%files -n hip
%doc HIP-rocm-%{version}/README.md
%license HIP-rocm-%{version}/LICENSE.txt
%{_bindir}/hipcc{,.pl}
%{_bindir}/hipconfig{,.pl}
%{perl_vendorlib}/hip*.pm
%{_datadir}/hip
# Upstream is moving code samples to another git tree in 5.7, so exclude this:
%exclude %{_datadir}/hip/samples

%files -n hip-devel
%{_bindir}/hipdemangleatp
%{_bindir}/hipcc_cmake_linker_helper
%{_includedir}/hip
%{_includedir}/hip_prof_str.h
%{_datadir}/cmake/hip

%files -n hip-doc
%license HIP-rocm-%{version}/LICENSE.txt
%{_docdir}/hip

%changelog
* Sat Jun 10 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-8
- Fix hip-lang-config.cmake bug (upstream patch)

* Fri Jun 09 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-7
- Fix hip-config.cmake bug (upstream patch)

* Fri Jun 02 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-6
- Fix rocminfo requires for hip

* Tue May 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-5
- Move some sed patching to patch files, sent some to upstream
- Add hipconfig patch for incorrect HIP_CLANG_INCLUDE detection
- Using rocm-device-libs 16.2 simplifies hipcc patching
- Minor clean up

* Tue May 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-4
- Move libamdhip64.so to rocm-hip to workaround blender issue

* Tue May 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-3
- Add "hip" runtime package; hipcc/hipconfig is required for blender at runtime

* Tue May 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-2
- Add missing perl-generators for generating requires
- Fix some issues with hipcc.pl
- Add fix build for aarch64

* Sun May 28 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-1
- Update to 5.5.1
- Workaround RHBZ#2207599
- Add noexecstack linker option
- Add doxygen docs

* Tue May 16 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.0-1
- Initial package
