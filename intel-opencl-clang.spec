%global toolchain clang

%global commit c78c1f884ffe8b40e1681a90ebde1a919c08ddb1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: intel-opencl-clang
Version: 15.0.0
Release: 2%{?dist}
Summary: Library to compile OpenCL C kernels to SPIR-V modules

License: NCSA
URL:     https://github.com/intel/opencl-clang
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExcludeArch: armv7hl

BuildRequires: cmake
BuildRequires: make
BuildRequires: llvm-devel
BuildRequires: clang-devel
BuildRequires: spirv-llvm-translator-devel
BuildRequires: zlib-devel

%description
opencl-clang is a thin wrapper library around clang. The library has OpenCL-oriented API and
is capable to compile OpenCL C kernels to SPIR-V modules.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%prep
%setup -q -n opencl-clang-%{commit}

%build
%cmake -DPREFERRED_LLVM_VERSION='%(rpm -q --qf '%%{version}' llvm-devel | cut -d. -f1 | sed "s/$/.0.0/")'
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libopencl-clang.so.*

%files devel
%{_libdir}/libopencl-clang.so
%{_includedir}/cclang/common_clang.h

%changelog
* Mon Sep 26 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 15.0.0-2
- Rebuild for spirv-llvm-translator against llvm 15

* Fri Sep 16 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 15.0.0-1
- Update to llvm 15

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 14.0.0-2
- Bump to a later commit with bunch of fixes

* Thu Mar 31 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 14.0.0-1
- Update to llvm 14

* Mon Dec 06 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 13.0.0-1
- Initial package
