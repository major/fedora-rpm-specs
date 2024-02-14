%global commit 1ba2c43bb8b6536287d020c598c5e2f035392d9a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global vc_date 20240206
%global vc_rev .%{vc_date}git%(c=%{commit}; echo ${c:0:7})
%global upstream_name vc-intrinsics
%global debug_package %{nil}

%global llvm_compat 11

Name: intel-llvm-vc-intrinsics%{?llvm_compat}
Version: 0.17.0
Release: 1%{?vc_rev}%{?dist}
Summary: New intrinsics on top of core LLVM %{?llvm_compat} IR instructions

License: MIT
URL: https://github.com/intel/%{upstream_name}
Source0: %{url}/archive/%{commit}/%{upstream_name}-%{shortcommit}.tar.gz

# LICENSE is not included in sources
Source1: LICENSE.md

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: llvm%{?llvm_compat}-devel
BuildRequires: llvm%{?llvm_compat}-static

%description
VC Intrinsics project contains a set of new intrinsics on top of core LLVM %{?llvm_compat} IR instructions
that represent SIMD semantics of a program targeting GPU.

%package devel
Summary: Development files for LLVM %{?llvm_compat} VC Intrinsics

%description devel
This package contains libraries and header files for
developing against %{upstream_name} built against LLVM %{?llvm_compat}.

%prep
%autosetup -p1 -n %{upstream_name}-%{commit}
cp %{SOURCE1} .

%build
%if 0%{?llvm_compat}
%cmake -DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%else
%cmake -DLLVM_DIR=%%{_libdir}/cmake/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%endif
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%{_libdir}/libLLVMGenXIntrinsics.a
%{_libdir}/cmake/VCIntrinsics*/*
%{_libdir}/cmake/LLVMGenXIntrinsics/*
%{_includedir}/llvm/GenXIntrinsics/*

%doc

%changelog
* Thu Feb 08 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.17.0-1.20240206git1ba2c43
- Initial package based on intel-llvm8.0-vc-intrinsics
