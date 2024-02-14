# Memory requirements are insane otherwise
%define _lto_cflags %{nil}

%global commit cc4f5b62a39543e78df13008c5ab3f8256e01a5f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global vc_date 20240131
%global vc_rev .%{vc_date}git%(c=%{commit}; echo ${c:0:7})

# The package will have to be adjusted if we ever stop needing compat, but I don't expect that
%global llvm_compat 11

Name: intel-cm-compiler
Version: 1.0.144
Release: 7%{?vc_rev}%{?dist}
Summary: Intel C for Metal compiler

License: MIT
URL: https://github.com/intel/cm-compiler
Source0: %{url}/archive/%{commit}/cm-compiler-%{shortcommit}.tar.gz
Patch01: 0001-Include-LLVMSPIRVLib.h-from-subdir-link-to-LLVMGenXI.patch

# This is Intel-only compiler
ExclusiveArch:  i686 x86_64

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: intel-llvm-vc-intrinsics%{?llvm_compat}-devel
BuildRequires: spirv-llvm-translator%{?llvm_compat}-devel
BuildRequires: llvm%{?llvm_compat}-devel
BuildRequires: llvm%{?llvm_compat}-static
BuildRequires: zlib-devel

# For pathfix.py
BuildRequires: python3-devel

# The compiler itself just requires everything...
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description
The Intel C for Metal compiler is a open source compiler that implements C for Metal programming language.
C for Metal is a new GPU kernel programming language for Intel HD Graphics.

%package libs
Summary: Libraries for %{summary}

%description libs
This package contains libraries applications built by %{summary}

%package devel
Summary: Development files for %{summary}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{summary}

%prep
%autosetup -p1 -n cm-compiler-%{commit}

cd clang/
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn \
    tools/clang-format/*.py \
    tools/clang-format/git-clang-format \
    utils/hmaptool/hmaptool \
    tools/scan-view/bin/scan-view

%build
cd clang/
%cmake \
    -DLLVM_CMAKE_PATH=%{_libdir}/llvm%{?llvm_compat} \
    -DLLVMGenXIntrinsics_DIR="/usr/include/llvm/GenXIntrinsics/" \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_INCLUDE_TESTS=OFF \
%if 0%{?__isa_bits} == 64
    -DLLVM_LIBDIR_SUFFIX=64 \
%else
    -DLLVM_LIBDIR_SUFFIX= \
%endif
    -G Ninja

%cmake_build

%install
cd clang/
%cmake_install

# Clean up
find %{buildroot}/usr/bin ! -name 'cmc' -type f -delete
find %{buildroot}/usr/bin ! -name 'cmc' -type l -delete
find %{buildroot}%{_libdir} ! -name 'libclangFEWrapper.so.%{?llvm_compat}' -type f -delete
find %{buildroot}%{_libdir} ! -name 'libclangFEWrapper.so' -type l -delete
rm -rf %{buildroot}/usr/include/clang
rm -rf %{buildroot}%{_libdir}/clang
rm -rf %{buildroot}%{_libdir}/cmake
rm -rf %{buildroot}/usr/include/clang
rm -rf %{buildroot}/usr/include/clang-c
rm -rf %{buildroot}/usr/share/clang
rm -rf %{buildroot}/usr/share/scan-view
rm -rf %{buildroot}/usr/share/scan-build
rm -f %{buildroot}/usr/libexec/c++-analyzer
rm -f %{buildroot}/usr/libexec/ccc-analyzer
rm -f %{buildroot}/usr/share/man/man1/scan-build.1

%files
%license clang/LICENSE.TXT
%{_bindir}/cmc

%files libs
%license clang/LICENSE.TXT
%{_libdir}/libclangFEWrapper.so.%{?llvm_compat}

%files devel
%{_includedir}/cm
%{_includedir}/opencl-c-common.h
%{_libdir}/libclangFEWrapper.so

%changelog
* Mon Feb 12 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.144-7.20240131gitcc4f5b6
- cm-compiler rebase to LLVM 11

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.144-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.144-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.144-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.144-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.144-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.144-1
- cm-compiler-1.0.144

* Thu Jan 27 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.119-2
- Address some packaging issues for packaging guidelines compliance

* Mon Dec 27 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.119-1
- Initial package
