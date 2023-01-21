%global commit 753ad5002af5a5e467b3a0194a2b0e9a3243059e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global vc_date 20211222
%global vc_rev .%{vc_date}git%(c=%{commit}; echo ${c:0:7})
%global upstream_name vc-intrinsics
%global debug_package %{nil}

Name: intel-llvm8.0-vc-intrinsics
Version: 0
Release: 3%{?vc_rev}%{?dist}
Summary: New intrinsics on top of core LLVM IR instructions

License: MIT
URL: https://github.com/intel/%{upstream_name}
Source0: %{url}/archive/%{commit}/%{upstream_name}-%{shortcommit}.tar.gz

# LICENSE is not included in sources
Source1: LICENSE.md

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++

BuildRequires: make
BuildRequires: llvm8.0-devel
BuildRequires: llvm8.0-static

%description
VC Intrinsics project contains a set of new intrinsics on top of core LLVM IR instructions
that represent SIMD semantics of a program targeting GPU.

%package devel
Summary: Development files for LLVM VC Intrinsics
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{upstream_name}

%prep
%setup -q -n %{upstream_name}-%{commit}
cp %{SOURCE1} .

%build
#%%cmake -DLLVM_DIR=%%{_libdir}/cmake/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake -DLLVM_DIR=%{_libdir}/llvm8.0/lib/cmake -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%{_libdir}/libLLVMGenXIntrinsics.a

%files devel
%{_libdir}/cmake/LLVMGenXIntrinsics/*
%{_includedir}/llvm/GenXIntrinsics/*

%doc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20211222git753ad50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20211222git753ad50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Dec 27 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 0-1.20211222git753ad50
- Initial package
