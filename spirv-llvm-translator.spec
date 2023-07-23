
%global commit 8703d43bd14d000fc630c2d3918d918819d23741
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-llvm-translator
Version:        16.0.0
Release:        4%{?dist}
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
%{_includedir}/LLVMSPIRVLib/
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Dave Airlie <airlied@redhat.com> - 16.0.0-3
- Bump to newer release branch

* Wed Apr 19 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 16.0.0-2
- Rebase downstream patch Fix-standalone-builds-with-LLVM_LINK_LLVM_DYLIB-ON to the version that got merged upstream
- Rebase to a later commit while at it

* Mon Feb 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 15.0.0-2
- Bump to a later llvm 15 branch commit including backported fixes
- Add spirv-tools dep

* Fri Sep 16 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 15.0.0-1
- update to llvm 15

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 22 2022 Dave Airlie <airlied@redhat.com> - 14.0.0-1
- Update to llvm 14

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-2
- Rebuild for LLVM 13.0.0-final

* Tue Oct 26 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 13.0.0-1
- update to llvm 13

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Dave Airlie <airlied@redhat.com> - 12.0.0-1
- update for llvm 12

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 11.1.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Feb 15 2021 Dave Airlie <airlied@redhat.com> - 11.1.0-1
- Update to llvm 11.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Dave Airlie <airlied@redhat.com> - 11.0.0-0.1
- Initial package of git snapshot for 11.0.0

