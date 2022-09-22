%global vc_commit 984bb27baacce6ee5c716c2e64845f2a1928025b
%global vc_shortcommit %(c=%{vc_commit}; echo ${c:0:7})
%global toolchain clang
%global optflags %{optflags} -Wno-everything -Qunused-arguments

%ifarch i686
%global optflags %(echo %{optflags} | sed 's/-flto / /')
%global _lto_cflags %{nil}
%endif

Name: intel-igc
Version: 1.0.12149
Release: 2%{?dist}
Summary: Intel Graphics Compiler for OpenCL

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/igc-%{version}/igc-%{version}.tar.gz
Source1: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics-%{vc_shortcommit}.tar.gz

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires: cmake
BuildRequires: make
BuildRequires: git
BuildRequires: ninja-build
BuildRequires: llvm-devel
BuildRequires: lld-devel
BuildRequires: clang
BuildRequires: flex
BuildRequires: bison
BuildRequires: python3
BuildRequires: zlib-devel
BuildRequires: intel-opencl-clang-devel
BuildRequires: libunwind-devel
BuildRequires: spirv-llvm-translator-devel
BuildRequires: spirv-llvm-translator-tools
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

%setup -q -n intel-graphics-compiler-igc-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DIGC_OPTION__LLVM_PREFERRED_VERSION='%(rpm -q --qf '%%{version}' llvm-devel | cut -d. -f1 | sed "s/$/.0.0/")' \
    -DVC_INTRINSICS_SRC="%{_builddir}/vc-intrinsics-%{vc_commit}" \
%ifarch x86_64
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
%endif
%ifarch i686
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux32' \
%endif
    -DIGC_OPTION__LINK_KHRONOS_SPIRV_TRANSLATOR=ON \
    -DIGC_OPTION__USE_KHRONOS_SPIRV_TRANSLATOR_IN_VC=ON \
    -DIGC_OPTION__USE_KHRONOS_SPIRV_TRANSLATOR_IN_SC=OFF \
    -DIGC_OPTION__SPIRV_TRANSLATOR_MODE=Prebuilds \
    -DIGC_OPTION__CLANG_MODE=Prebuilds \
    -DIGC_OPTION__LLD_MODE=Prebuilds \
    -DIGC_OPTION__LLVM_MODE=Prebuilds \
    -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
    -DIGC_OPTION__USE_PREINSTALLED_SPRIV_HEADERS=ON \
    -DIGC_OPTION__VC_INTRINSICS_MODE=Source \
    -DINSTALL_GENX_IR=ON \
    -Wno-dev \
    -G Ninja

%cmake_build

%install
%cmake_install

%files
%{_bindir}/iga{32,64}
%{_bindir}/GenX_IR

%files libs
%license LICENSE.md
%license %{_libdir}/igc/NOTICES.txt
%{_libdir}/libiga{32,64}.so.1{,.*}
%{_libdir}/libigc.so.1{,.*}
%{_libdir}/libigdfcl.so.1{,.*}

%files devel
%{_libdir}/libiga{32,64}.so
%{_libdir}/libigc.so
%{_libdir}/libigdfcl.so
%{_includedir}/igc
%{_includedir}/iga
%{_includedir}/visa
%{_libdir}/pkgconfig/igc-opencl.pc

%changelog
* Mon Sep 19 2022 Pete Walter <pwalter@fedoraproject.org> - 1.0.12149-2
- Rebuild for llvm 15

* Thu Sep 08 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.12149-1
- intel-igc-1.0.12149

* Tue Aug 30 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.12037.1-1
- intel-igc-1.0.12037.1

* Tue Aug 09 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.12037.1-1
- intel-igc-1.0.11702.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11485-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.11485-1
- intel-igc-1.0.11485

* Sun May 29 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.11279-1
- intel-igc-1.0.11279
- add LLVM 13 and 14 patches

* Thu Mar 31 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.10778-1
- intel-igc-1.0.10778

* Sat Mar 19 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.10409-1
- intel-igc-1.0.10409
- use system spirv

* Thu Feb 24 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.10395-1
- intel-igc-1.0.10395

* Thu Feb 24 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.10395-1
- intel-igc-1.0.10395

* Fri Feb 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.10200-1
- intel-igc-1.0.10200

* Mon Dec 27 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.9933-1
- Initial package
