
%global commit a44863e231a8f1b1dfcde3c1f3c86c010fa5c4c5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global vc_date 20211223
%global vc_rev .%{vc_date}git%(c=%{commit}; echo ${c:0:7})
%global upstream_name spirv-llvm-translator

Name:           spirv-llvm8.0-translator
Version:        8
Release:        7%{?vc_rev}%{?dist}
Summary:        LLVM 8.0 to SPIRV Translator

License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/%{commit}/%{upstream_name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm8.0
BuildRequires:  llvm8.0-devel
BuildRequires:  llvm8.0-static
BuildRequires:  spirv-headers-devel

%description
Khronos LLVM 8.0 to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM 8.0 to SPIRV Translator
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts:      spirv-llvm-translator-devel

%description devel
This package contains libraries and header files for
developing against %{upstream_name}

%package tools
Summary: Standalone llvm 8.0 to spirv translator tool
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts:      spirv-llvm-translator-tools

%description tools
This package contains the standalone llvm 8.0 to spirv tool.

%prep
%autosetup -n SPIRV-LLVM-Translator-%{commit}

%build
%cmake -GNinja \
       -DLLVM_DIR=%{_libdir}/llvm8.0/lib/cmake/llvm \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/1.2/" \
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64 \
%else
       -DLLVM_LIBDIR_SUFFIX= \
%endif

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE.TXT
%{_libdir}/libLLVMSPIRVLib.so.8

%files tools
%{_bindir}/llvm-spirv

%files devel
%{_includedir}/LLVMSPIRVLib/
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-7.20211223gita44863e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-6.20211223gita44863e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-5.20211223gita44863e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-4.20211223gita44863e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 8-3.20211223gita44863e
- Remove double include of LLVMSPIRVLib

* Wed Jan 26 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 8-2.20211223gita44863e
- Drop redundant dir macro
- List libLLVMSPIRVLib.so.8 explictly without glob

* Mon Dec 27 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 8-1.20211223gita44863e
- New package based on spirv-llvm-translator
