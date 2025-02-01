
%global commit 72538254527d23f48cef863c5ce3c3d804f94b8b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-llvm15.0-translator
Version:        15.0.0
Release:        %autorelease
Summary:        LLVM 15 to SPIRV Translator

License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{commit}/spirv-llvm-translator-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm15-devel
BuildRequires:  llvm15-static
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel

%description
Khronos LLVM 15 to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM 15 to SPIRV Translator
Conflicts: spirv-llvm-translator-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm 15 to spirv translator tool
Conflicts: spirv-llvm-translator-tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains the standalone llvm to spirv tool.

%prep
%autosetup -n SPIRV-LLVM-Translator-%{commit} -p1

%build
%cmake -GNinja \
       -DLLVM_DIR=%{_libdir}/llvm15/lib/cmake/llvm \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/" \
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64
%else
       -DLLVM_LIBDIR_SUFFIX=
%endif

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
%autochangelog
