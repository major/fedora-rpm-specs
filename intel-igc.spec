%global vc_commit 77f069b71fa9042bc4b2f68d06942a43c8ecec73
%global vc_shortcommit %(c=%{vc_commit}; echo ${c:0:7})

%global optflags %{optflags} -w

# not compatible with newer clang versions
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 8
%global llvm_compat 15
%endif

Name: intel-igc
Version: 1.0.15313.1
Release: 2%{?dist}
Summary: Intel Graphics Compiler for OpenCL

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/igc-%{version}/igc-%{version}.tar.gz
Source1: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics-%{vc_shortcommit}.tar.gz
Patch01: 0001-Guard-getValue-dump-with-DEBUG_VERBOSE_ON.patch

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

%autosetup -n intel-graphics-compiler-igc-%{version} -p1

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
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15313.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 06 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.15313.1-1
- intel-igc-1.0.15313.1 (fixes RHBZ#2183055)
- Switch to llvm 17 compat package

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13700.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.13700.7-1
- intel-igc-1.0.13700.7 (fixes RHBZ#2177378 )

* Mon Mar 06 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.13463.1-1
- intel-igc-1.0.13463.1 (fixes RHBZ#2175129 )

* Fri Feb 17 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.13230.4-1
- intel-igc-1.0.13230.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12812.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.12812.4-1
- intel-igc-1.0.12812.4
- LLVM 15 Support (fixes RHBZ#2127746 )

* Mon Sep 19 2022 Pete Walter <pwalter@fedoraproject.org> - 1.0.12149-2
- Rebuild for llvm 15

* Fri Sep 16 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.12149.1-1
- intel-igc-1.0.12149.1

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
