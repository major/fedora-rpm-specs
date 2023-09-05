
%global commit 322fca5d9c59bfdb80562a52ace51cdbe2a60e92
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-llvm-translator16
Version:        16.0.0
Release:        1%{?dist}
Summary:        LLVM to SPIRV Translator

License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm16-devel
BuildRequires:  llvm16-static
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  zlib-devel

%description
Khronos LLVM to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM to SPIRV Translator
Conflicts: spirv-llvm-translator-devel
Conflicts: spirv-llvm8.0-translator-devel
Conflicts: spirv-llvm15.0-translator-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm to spirv translator tool
Conflicts: spirv-llvm-translator-tools
Conflicts: spirv-llvm8.0-translator-tools
Conflicts: spirv-llvm15.0-translator-tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains the standalone llvm to spirv tool.

%prep
%autosetup -n SPIRV-LLVM-Translator-%{commit} -p1

%build
%cmake -GNinja \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_DIR=%{_libdir}/llvm16/lib/cmake/llvm \
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64 \
%else
       -DLLVM_LIBDIR_SUFFIX= \
%endif
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/"

%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_libdir}/libLLVMSPIRVLib.so.*

%files tools
%{_bindir}/llvm-spirv

%files devel
%dir %{_includedir}/LLVMSPIRVLib/
%{_includedir}/LLVMSPIRVLib/
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
* Mon Sep 04 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 16.0.0-1
- Initial compat package from spirv-llvm-translator
