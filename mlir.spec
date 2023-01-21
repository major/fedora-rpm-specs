%global maj_ver 15
%global min_ver 0
#global rc_ver 3
%global patch_ver 7
%global mlir_version %{maj_ver}.%{min_ver}.%{patch_ver}
%global mlir_srcdir llvm-project-%{mlir_version}%{?rc_ver:rc%{rc_ver}}.src

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

Name: mlir
Version: %{mlir_version}%{?rc_ver:~rc%{rc_ver}}
Release: 2%{?dist}
Summary: Multi-Level Intermediate Representation Overview

License: Apache-2.0 WITH LLVM-exception
URL: http://mlir.llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{mlir_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{mlir_srcdir}.tar.xz.sig
Source2: release-keys.asc

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-test = %{version}
BuildRequires: python3-lit

# For origin certification
BuildRequires: gnupg2

%description
The MLIR project is a novel approach to building reusable and extensible
compiler infrastructure. MLIR aims to address software fragmentation,
improve compilation for heterogeneous hardware, significantly reduce
the cost of building domain specific compilers, and aid in connecting
existing compilers together.

%package static
Summary: MLIR static files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
MLIR static files.

%package devel
Summary: MLIR development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-static%{?_isa} = %{version}-%{release}

%description devel
MLIR development files.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{mlir_srcdir}/%{name} -p2
# remove all but keep mlir
find ../* -maxdepth 0 ! -name '%{name}' -exec rm -rf {} +


%build
%cmake  -GNinja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_RPATH=ON \
        -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
        -DLLVM_BUILD_LLVM_DYLIB=ON \
        -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/llvm/ \
        -DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
        -DLLVM_BUILD_TOOLS:BOOL=ON \
        -DLLVM_BUILD_UTILS:BOOL=ON \
        -DMLIR_INCLUDE_DOCS:BOOL=ON \
        -DMLIR_INCLUDE_TESTS:BOOL=ON \
        -DMLIR_INCLUDE_INTEGRATION_TESTS:BOOL=OFF \
        -DBUILD_SHARED_LIBS=OFF \
        -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \
        -DMLIR_BUILD_MLIR_C_DYLIB=ON \
%if 0%{?__isa_bits} == 64
        -DLLVM_LIBDIR_SUFFIX=64
%else
        -DLLVM_LIBDIR_SUFFIX=
%endif
# build process .exe tools normally use rpath or static linkage
export LD_LIBRARY_PATH=%{_builddir}/%{mlir_srcdir}/%{name}/%{_build}/%{_lib}
%cmake_build


%install
%cmake_install

%check
# Remove tablegen tests, as they rely on includes from llvm/.
rm -rf test/mlir-tblgen

%ifarch %{ix86}
# TODO: Test currently fails on i686.
rm test/IR/file-metadata-resources.mlir

# TODO: There's two issues here (see https://github.com/llvm/llvm-project/issues/58357):
# 1. The async dialect hardcodes a 64-bit assumption.
# 2. The cpu runner tests call mlir-opt without awareness of the host index size.
# For this reason, skip mlir-cpu-runner tests on 32-bit.
rm -rf test/mlir-cpu-runner
%endif

# Test execution normally relies on RPATH, so set LD_LIBRARY_PATH instead.
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%cmake_build --target check-mlir

%files
%license LICENSE.TXT
%{_libdir}/libMLIR*.so.%{maj_ver}*
%{_libdir}/libmlir_async_runtime.so.%{maj_ver}*
%{_libdir}/libmlir_c_runner_utils.so.%{maj_ver}*
%{_libdir}/libmlir_runner_utils.so.%{maj_ver}*

%files static
%{_libdir}/libMLIR*.a

%files devel
%{_bindir}/mlir-cpu-runner
%{_bindir}/mlir-linalg-ods-yaml-gen
%{_bindir}/mlir-lsp-server
%{_bindir}/mlir-opt
%{_bindir}/mlir-pdll-lsp-server
%{_bindir}/mlir-reduce
%{_bindir}/mlir-tblgen
%{_bindir}/mlir-translate
%{_bindir}/tblgen-lsp-server
%{_libdir}/libMLIR*.so
%{_libdir}/libmlir_async_runtime.so
%{_libdir}/libmlir_c_runner_utils.so
%{_libdir}/libmlir_runner_utils.so
%{_includedir}/mlir
%{_includedir}/mlir-c
%{_libdir}/cmake/mlir

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.6-3
- Omit frame pointers when building

* Thu Dec 22 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-2
- rhbz#2127916: Add mlir tools to mlir-devel

* Mon Dec 05 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Thu Sep 15 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-4
- Rebuild

* Wed Sep 14 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Run tests during the build

* Mon Sep 12 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Add explicit requires from mlir-devel to mlir

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Mon Feb 07 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-2
- Reenable build on armv7hl

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Tue Feb 01 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc3-1
- Update to LLVM 13.0.1rc3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Wed Jan 12 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Wed Oct 06 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-2
- Rebuild for llvm soname bump

* Fri Oct 01 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Wed Sep 22 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc3-1
- 13.0.0-rc3 Release

* Tue Aug 10 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-3
- Add -static requires back to -devel package

* Tue Aug 10 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-2
- Add back the -static sub-package

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Thu Jul 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc3-1
- 12.0.1-rc3 Release

* Wed Jun 02 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-1
- 12.0.1-rc1 Release

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.7.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.6.rc4
- New upstream release candidate

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 12.0.0-0.5.rc3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.4.rc3
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- llvm 12.0.0-rc2 release

* Thu Feb 18 2021 sguelton@redhat.com - 12.0.0-0.1.rc1
- llvm 12.0.0-rc1 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Serge Guelton - 11.1.0-0.2.rc2
- llvm 11.1.0-rc2 release

* Thu Jan 14 2021 Serge Guelton - 11.1.0-0.1.rc1
- 11.1.0-rc1 release

* Wed Jan 06 2021 Serge Guelton - 11.0.1-3
- LLVM 11.0.1 final

* Tue Dec 22 2020 sguelton@redhat.com - 11.0.1-2.rc2
- llvm 11.0.1-rc2

* Tue Dec 01 2020 sguelton@redhat.com - 11.0.1-1.rc1
- llvm 11.0.1-rc1

* Thu Oct 15 2020 sguelton@redhat.com - 11.0.0-1
- Fix NVR

* Mon Oct 12 2020 sguelton@redhat.com - 11.0.0-0.6
- llvm 11.0.0 - final release

* Thu Oct 08 2020 sguelton@redhat.com - 11.0.0-0.5.rc6
- 11.0.0-rc6

* Fri Oct 02 2020 sguelton@redhat.com - 11.0.0-0.4.rc5
- 11.0.0-rc5 Release

* Sun Sep 27 2020 sguelton@redhat.com - 11.0.0-0.3.rc3
- Fix NVR

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.1.rc3
- 11.0.0-rc3 Release

* Wed Sep 02 2020 sguelton@redhat.com - 11.0.0-0.2.rc2
- Package mlir-tblgen

* Wed Aug 12 2020 Cristian Balint <cristian.balint@gmail.com> - 11.0.0-0.1.rc1
- Initial version.

