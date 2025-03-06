
%global commit 781d0790ea4dc6238eabe44fc39e49b6b27fbcbe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-llvm-translator
Version:        20.1.0
Release:        %autorelease
Summary:        LLVM to SPIRV Translator

License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
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
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm to spirv translator tool
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
       -DLLVM_DIR="/usr/lib64/cmake/llvm/" \
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
%{_includedir}/LLVMSPIRVLib/*
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
%autochangelog
