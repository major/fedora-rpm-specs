%global commit 58242977b4092cf5eb94a10dd144691c12c87001
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# not compatible with newer clang versions
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 8
%global llvm_compat 15
%endif

Name: intel-opencl-clang
Version: 15.0.1
Release: %autorelease
Summary: Library to compile OpenCL C kernels to SPIR-V modules

License: NCSA
URL:     https://github.com/intel/opencl-clang
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: cmake
BuildRequires: clang%{?llvm_compat}
BuildRequires: gcc gcc-c++
BuildRequires: libffi-devel
BuildRequires: make
BuildRequires: llvm%{?llvm_compat}-devel
BuildRequires: clang%{?llvm_compat}-devel
%if %{?llvm_compat} == 15
BuildRequires: spirv-llvm15.0-translator-devel
%else
BuildRequires: spirv-llvm-translator%{?llvm_compat}-devel
%endif
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
%autosetup -n opencl-clang-%{commit} -p1
sed -i 's/$<TARGET_FILE:clang>/$<TARGET_FILE:clang%{?llvm_compat}>/' cl_headers/CMakeLists.txt

%build
%cmake \
    -DPREFERRED_LLVM_VERSION='%(rpm -q --qf '%%{version}' llvm%{?llvm_compat}-devel | cut -d. -f1 | sed "s/$/.0.0/")' \
    -DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake/llvm/
%cmake_build

%install
%cmake_install

# This is ugly, but a combined behavior of LLVM_DIR=*/lib/* and LLVM_LIBDIR_SUFFIX=64 is borked
%ifnarch i686
mkdir -p %{buildroot}%{_libdir}/
cp %{buildroot}/usr/lib/libopencl-clang.so.* %{buildroot}%{_libdir}/
cp %{buildroot}/usr/lib/libopencl-clang.so %{buildroot}%{_libdir}/
rm %{buildroot}/usr/lib/libopencl-clang.so.*
rm %{buildroot}/usr/lib/libopencl-clang.so
%endif

%files
%license LICENSE
%{_libdir}/libopencl-clang.so.*

%files devel
%{_libdir}/libopencl-clang.so
%{_includedir}/cclang/common_clang.h
%{_includedir}/cclang/opencl-c.h
%{_includedir}/cclang/opencl-c-base.h
%{_includedir}/cclang/module.modulemap

%changelog
%autochangelog
