%global vc_commit 9d255266e1df8f1dc5d11e1fbb03213acfaa4fc7
%global vc_shortcommit %(c=%{vc_commit}; echo ${c:0:7})

%global optflags %{optflags} -w

# not compatible with newer clang versions
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 8
%global llvm_compat 15
%endif

Name: intel-igc
Version: 2.7.8
Release: %autorelease
Summary: Intel Graphics Compiler for OpenCL

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/v%{version}/v%{version}.tar.gz
Source1: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics-%{vc_shortcommit}.tar.gz

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires: cmake
BuildRequires: make
BuildRequires: git
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: llvm%{?llvm_compat}-devel
BuildRequires: lld%{?llvm_compat}-devel
BuildRequires: clang%{?llvm_compat}
BuildRequires: flex
BuildRequires: bison
BuildRequires: python3
BuildRequires: python3-mako
BuildRequires: python3-pyyaml
BuildRequires: zlib-devel
BuildRequires: intel-opencl-clang-devel
BuildRequires: libunwind-devel
%if %{?llvm_compat} == 15
BuildRequires: spirv-llvm15.0-translator-devel
BuildRequires: spirv-llvm15.0-translator-tools
%else
BuildRequires: spirv-llvm-translator%{?llvm_compat}-devel
BuildRequires: spirv-llvm-translator%{?llvm_compat}-tools
%endif
BuildRequires: spirv-headers-devel
BuildRequires: spirv-tools-devel

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

# Unfortunately, it isn't trivially posible to build with prebuilt vc-intrinsics
Provides: bundled(intel-vc-intrinsics)

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

%autosetup -n intel-graphics-compiler-%{version} -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DIGC_OPTION__LLVM_PREFERRED_VERSION='%(rpm -q --qf '%%{version}' llvm%{?llvm_compat}-devel | cut -d. -f1 | sed "s/$/.0.0/")' \
    -DVC_INTRINSICS_SRC="%{_builddir}/vc-intrinsics-%{vc_commit}" \
%ifarch x86_64
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
%endif
%ifarch i686
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux32' \
%endif
    -DIGC_OPTION__LINK_KHRONOS_SPIRV_TRANSLATOR=ON \
    -DIGC_BUILD__VC_ENABLED=ON \
    -DIGC_OPTION__SPIRV_TRANSLATOR_MODE=Prebuilds \
    -DIGC_OPTION__CLANG_MODE=Prebuilds \
    -DIGC_OPTION__LLD_MODE=Prebuilds \
    -DIGC_OPTION__LLVM_MODE=Prebuilds \
    -DLLVM_ROOT=%{_libdir}/llvm%{?llvm_compat}/ \
    -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
    -DIGC_OPTION__USE_PREINSTALLED_SPIRV_HEADERS=ON \
    -DIGC_OPTION__VC_INTRINSICS_MODE=Source \
    -DINSTALL_GENX_IR=ON \
    -Wno-dev \
    -G Ninja

%cmake_build

%install
%cmake_install

%files
%{_bindir}/iga{32,64}

%files libs
%license LICENSE.md
%license %{_libdir}/igc2/NOTICES.txt
%dir %{_libdir}/igc2/
%{_libdir}/libiga{32,64}.so.2.*
%{_libdir}/libigc.so.2.*+*
%{_libdir}/libigdfcl.so.2.*

%files devel
%{_libdir}/libiga{32,64}.so.2
%{_libdir}/libigc.so.2
%{_libdir}/libigdfcl.so.2
%{_includedir}/igc
%{_includedir}/iga
%{_includedir}/visa
%{_libdir}/pkgconfig/igc-opencl.pc

%changelog
%autochangelog
