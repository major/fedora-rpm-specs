
%global commit 2e025e413c8b80875bbb89ce2e87e10ae3e99e60
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global vc_date 20240131
%global vc_rev .%{vc_date}git%(c=%{commit}; echo ${c:0:7})
%global upstream_name spirv-llvm-translator

%global llvm_compat 11

Name:           spirv-llvm-translator%{?llvm_compat}
Version:        %{?llvm_compat}
Release:        1%{?vc_rev}%{?dist}
Summary:        LLVM %{?llvm_compat} to SPIRV Translator

License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/%{commit}/%{upstream_name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm%{?llvm_compat}
BuildRequires:  llvm%{?llvm_compat}-devel
BuildRequires:  llvm%{?llvm_compat}-static
BuildRequires:  spirv-headers-devel

%description
Khronos LLVM %{?llvm_compat} to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM %{?llvm_compat} to SPIRV Translator
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts:      spirv-llvm-translator-devel

%description devel
This package contains libraries and header files for
developing against %{upstream_name}

%package tools
Summary: Standalone LLVM %{?llvm_compat} to spirv translator tool
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts:      spirv-llvm-translator-tools

%description tools
This package contains the standalone LLVM %{?llvm_compat} to spirv tool.

%prep
%autosetup -n SPIRV-LLVM-Translator-%{commit}

%build
%cmake -GNinja \
%if 0%{?llvm_compat}
       -DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake/llvm \
%else
       -DLLVM_DIR=%%{_libdir}/cmake/llvm
%endif
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="%{_includedir}/spirv/unified1/" \
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
%{_libdir}/libLLVMSPIRVLib.so.%{?llvm_compat}

%files tools
%{_bindir}/llvm-spirv

%files devel
%{_includedir}/LLVMSPIRVLib/
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
* Thu Feb 08 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 11-1.20240131git2e025e4
- New package based on spirv-llvm8.0-translator
