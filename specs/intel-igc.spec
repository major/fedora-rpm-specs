%global vc_commit 27f7c4f34738f5eaf7a045b77edf8d9e034443d8
%global vc_shortcommit %(c=%{vc_commit}; echo ${c:0:7})

%if 0%{?rhel}
# RHEL build here
%global use_system_headers 0
%global clang_commit 07e7c931d8bdb38549a907cf04fd06a278f7cdce
%global clang_shortcommit %(c=%{clang_commit}; echo ${c:0:7})
%global translator_commit b84990a370e46748f7196af1d8f5a39f5834802d
%global translator_shortcommit %(c=%{translator_commit}; echo ${c:0:7})
%global spirv_headers_commit b8a32968473ce852a809b9de5f04f02a5a9dfa78
%global spirv_headers_shortcommit %(c=%{spirv_headers_commit}; echo ${c:0:7})
%global spirv_tools_commit 28a883ba4c67f58a9540fb0651c647bb02883622
%global spirv_tools_shortcommit %(c=%{spirv_tools_commit}; echo ${c:0:7})
%global llvm_ver 16.0.6
%global llvm_compat 16
# Disable LTO; LLVM/clang under LTO has produced miscompiled binaries here.
%define _lto_cflags %{nil}
# Disable dwz: this fails anyways, due to static linking, sometimes fails builds
# when builders do not have enough RAM
%define _find_debuginfo_dwz_opts %{nil}
%else
# Fedora build here
%global use_system_headers 1
%global llvm_compat 15
%endif

# Keep this override here, otherwise LTO disable will not take affect in RHEL
%global optflags %{optflags} -w

# This patch level is reused in cflags
%global igc_patch 3

Name: intel-igc
Version: 2.36.%{igc_patch}
Release: %autorelease
Summary: Intel Graphics Compiler for OpenCL

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/v%{version}/v%{version}.tar.gz
Source1: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics-%{vc_shortcommit}.tar.gz
%if ! 0%{?use_system_headers}
Source2: https://github.com/intel/opencl-clang/archive/%{clang_commit}/intel-opencl-clang-%{clang_shortcommit}.tar.gz
Source3: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{translator_commit}/spirv-llvm-translator-%{translator_shortcommit}.tar.gz
Source4: https://github.com/KhronosGroup/SPIRV-Headers/archive/%{spirv_headers_commit}/spirv-headers-%{spirv_headers_shortcommit}.tar.gz
Source5: https://github.com/KhronosGroup/SPIRV-Tools/archive/%{spirv_tools_commit}/spirv-tools-%{spirv_tools_shortcommit}.tar.gz
Source6: https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{llvm_ver}.tar.gz
%endif

Patch0: 0001-Fix-segfault-when-running-analysis-passes-after-SCCP.patch
Patch1: 0002-Fix-incomplete-type-llvm-Triple-in-MemCpyOptimizer-w.patch

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires: cmake
BuildRequires: make
BuildRequires: git
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: flex
BuildRequires: bison
BuildRequires: python3
BuildRequires: python3-mako
BuildRequires: python3-pyyaml
BuildRequires: zlib-devel
BuildRequires: libffi-devel
BuildRequires: libunwind-devel
#This pkg is needed with system headers or without
BuildRequires: spirv-tools-devel
%if 0%{?use_system_headers}
BuildRequires: llvm%{?llvm_compat}-devel
BuildRequires: lld%{?llvm_compat}-devel
BuildRequires: clang%{?llvm_compat}
BuildRequires: clang-tools-extra
BuildRequires: spirv-headers-devel
BuildRequires: intel-opencl-clang-devel
BuildRequires: spirv-llvm15.0-translator-devel
BuildRequires: spirv-llvm15.0-translator-tools
%else
BuildRequires: chrpath
%endif

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

# Unfortunately, it isn't trivially posible to build with prebuilt vc-intrinsics
Provides: bundled(intel-vc-intrinsics)
# For RHEL builds, we bundle quite a few things
%if ! 0%{?use_system_headers}
Provides: bundled(llvm)
Provides: bundled(opencl-clang)
Provides: bundled(spirv-llvm-translator)
Provides: bundled(spirv-headers)
Provides: bundled(spirv-tools)
%endif

%description
The Intel Graphics Compiler for OpenCL is an LLVM based compiler for OpenCL targeting Intel Gen graphics hardware architecture.

%package       devel
Summary:       Intel Graphics Compiler Frontend - Devel Files
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description   devel
Devel files for Intel Graphics Compiler for OpenCL.

%package       libs
Summary:       Intel Graphics Compiler Frontend - Library Files
Requires:      %{name} = %{version}-%{release}

%description   libs
Library files for Intel Graphics Compiler for OpenCL.

%prep
tar -xf %{SOURCE1}

%autosetup -n intel-graphics-compiler-%{version} -p1 -S git

#This setup is needed for the bundled libraries build in RHEL
%if ! 0%{?use_system_headers}
# LLVM monorepo tarball
mkdir -p %{_builddir}/llvm-project
tar -xf %{SOURCE6} -C %{_builddir}/llvm-project --strip-components=1

# opencl-clang and SPIRV-LLVM-Translator extract directly into LLVM's projects/
rm -rf %{_builddir}/llvm-project/llvm/projects/opencl-clang \
       %{_builddir}/llvm-project/llvm/projects/llvm-spirv
mkdir -p %{_builddir}/llvm-project/llvm/projects/opencl-clang \
         %{_builddir}/llvm-project/llvm/projects/llvm-spirv
tar -xf %{SOURCE2} -C %{_builddir}/llvm-project/llvm/projects/opencl-clang --strip-components=1
tar -xf %{SOURCE3} -C %{_builddir}/llvm-project/llvm/projects/llvm-spirv  --strip-components=1

# SPIRV-Headers and SPIRV-Tools live standalone (referenced by IGC cmake flags)
mkdir -p %{_builddir}/SPIRV-Headers %{_builddir}/SPIRV-Tools
tar -xf %{SOURCE4} -C %{_builddir}/SPIRV-Headers --strip-components=1
tar -xf %{SOURCE5} -C %{_builddir}/SPIRV-Tools   --strip-components=1
# IGC cmake copies .git into the LLVM staging dir and uses git am to apply
# opencl-clang patches to clang and llvm. Keep at clang/ and llvm/docs/
# adjust the directories if needed, when patches change.
git config --global user.email "build@localhost"
git config --global user.name "build"
git -C %{_builddir}/llvm-project init -q
git -C %{_builddir}/llvm-project add -f clang/ llvm/docs
git -C %{_builddir}/llvm-project commit -q -m "llvmorg-%{llvm_ver}"
%endif

%build
# TODO: Please submit an issue to upstream (rhbz#2380657)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DIGC_API_PATCH_VERSION=%{igc_patch} \
%ifarch x86_64
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
%endif
%ifarch i686
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux32' \
%endif
    -DIGC_BUILD__VC_ENABLED=ON \
    -DIGC_OPTION__VC_INTRINSICS_MODE=Source \
    -DVC_INTRINSICS_SRC="%{_builddir}/vc-intrinsics-%{vc_commit}" \
%if 0%{?use_system_headers}
    -DIGC_OPTION__LLVM_PREFERRED_VERSION='%(rpm -q --qf '%%{version}' llvm%{?llvm_compat}-devel | cut -d. -f1 | sed "s/$/.0.0/")' \
    -DIGC_OPTION__LLD_MODE=Prebuilds \
    -DIGC_OPTION__LLVM_MODE=Prebuilds \
    -DLLVM_ROOT=%{_libdir}/llvm%{?llvm_compat}/ \
    -DIGC_OPTION__LINK_KHRONOS_SPIRV_TRANSLATOR=ON \
    -DIGC_OPTION__SPIRV_TRANSLATOR_MODE=Prebuilds \
    -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
    -DIGC_OPTION__USE_PREINSTALLED_SPIRV_HEADERS=ON \
    -DIGC_OPTION__CLANG_MODE=Prebuilds \
    -DIGC_OPTION__API_ENABLE_OPAQUE_POINTERS=OFF \
    -DIGC_OPTION__ENABLE_BF16_BIF=OFF \
    -DINSTALL_GENX_IR=ON \
%else
    -DIGC_OPTION__LLVM_MODE=Source \
    -DIGC_OPTION__LLVM_PREFERRED_VERSION=%{llvm_ver} \
    -DIGC_OPTION__SPIRV_TOOLS_MODE=Source \
    -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="%{_builddir}/SPIRV-Headers" \
    -DIGC_OPTION__API_ENABLE_OPAQUE_POINTERS=ON \
%endif
    -Wno-dev \
    -G Ninja

%cmake_build

%install
%cmake_install
%if ! 0%{?use_system_headers}
# Remove bundled standalone tools/plugins not shipped as part of intel-igc.
# These are statically-linked-against-LLVM binaries built as a side-effect
# of LLVM source mode, each ~500MB. Without these, libs subpkg drops dramatically.
rm -fv %{buildroot}%{_bindir}/GenX_IR
rm -fv %{buildroot}%{_bindir}/clang-%{llvm_compat}
rm -fv %{buildroot}%{_bindir}/lld
rm -fv %{buildroot}%{_prefix}/lib/NewPMPlugin.so
rm -fv %{buildroot}%{_prefix}/lib/debug%{_prefix}/lib/NewPMPlugin.so*
# Change permissions otherwise opencl install will fail
chmod +x %{buildroot}%{_libdir}/libopencl-clang.so.%{llvm_compat}
# Strip rpath from libclang.so.16 since its empty anyways and fails build
chrpath -d %{buildroot}%{_libdir}/libopencl-clang.so.%{llvm_compat}
# Removes additional non-essential symbols beyond what find-debuginfo.sh strips.
# These files end up being huge. This cuts the debuginfo libs pkg in half
strip --strip-unneeded %{buildroot}%{_libdir}/libopencl-clang.so.%{llvm_compat} %{buildroot}%{_libdir}/libigdfcl.so.*
%endif

%files
%{_bindir}/iga{32,64}

%files libs
%license LICENSE.md
%license %{_libdir}/igc2/NOTICES.txt
%dir %{_libdir}/igc2/
%{_libdir}/libiga{32,64}.so.2.*
%{_libdir}/libigc.so.2.*+*
%{_libdir}/libigdfcl.so.2.*
%if ! 0%{?use_system_headers}
%{_libdir}/libopencl-clang.so.%{llvm_compat}
%{_includedir}/opencl-c.h
%{_includedir}/opencl-c-base.h
%endif

%files devel
%{_libdir}/libiga{32,64}.so.2
%{_libdir}/libiga{32,64}.so
%{_libdir}/libigc.so.2
%{_libdir}/libigc.so
%{_libdir}/libigdfcl.so.2
%{_libdir}/libigdfcl.so
%{_includedir}/igc
%{_includedir}/iga
%{_includedir}/visa
%{_libdir}/pkgconfig/igc-opencl.pc

%changelog
%autochangelog
