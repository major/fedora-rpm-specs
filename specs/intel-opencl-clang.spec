%global commit b953eceebb0abc6ea954a14545420e3f97540a77
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global llvm_ver 22

# f44 ships LLVM 22 as the main package; f45+ provide llvm22 compat
%if 0%{?fedora} >= 45
%global llvm_compat %{llvm_ver}
%global llvm_bindir %{_libdir}/llvm%{llvm_ver}/bin
%global llvm_cmake  %{_libdir}/llvm%{llvm_ver}/%{_lib}/cmake
%else
%global llvm_bindir %{_bindir}
%global llvm_cmake  %{_libdir}/cmake
%endif

Name: intel-opencl-clang
Version: 22.1.4
Release: %autorelease
Summary: Library to compile OpenCL C kernels to SPIR-V modules

License: NCSA
URL:     https://github.com/intel/opencl-clang
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: cmake
BuildRequires: clang%{?llvm_compat}-devel
BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ninja-build
BuildRequires: libffi-devel
BuildRequires: llvm%{?llvm_compat}
BuildRequires: llvm%{?llvm_compat}-devel
BuildRequires: llvm%{?llvm_compat}-static
BuildRequires: spirv-llvm-translator%{?llvm_compat}-devel
BuildRequires: spirv-headers-devel
BuildRequires: spirv-tools-devel
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
# compat clang keeps its resource dir in /usr/lib/clang/<major>, not under LLVM_LIBRARY_DIR
sed -i -E 's|message\(FATAL_ERROR "\[OPENCL-CLANG\] Couldn.t find prebuilt LLVM include directory\."\)|set(OPENCL_HEADERS_DIR "%{_prefix}/lib/clang/%{llvm_ver}/include/")|' cl_headers/CMakeLists.txt
grep -q 'OPENCL_HEADERS_DIR "/usr/lib/clang' cl_headers/CMakeLists.txt

%build
export PATH=%{llvm_bindir}:$PATH
LLVM_FULL_VER=$(llvm-config --version | sed 's/~.*//;s/git//')
LLVM_MAJOR=$(echo "$LLVM_FULL_VER" | cut -d. -f1)
if [ "$LLVM_MAJOR" != "%{llvm_ver}" ]; then
    echo "Expected LLVM %{llvm_ver}, got $LLVM_FULL_VER" >&2
    exit 1
fi

%cmake \
    -DUSE_PREBUILT_LLVM=ON \
    -DPREFERRED_LLVM_VERSION=$LLVM_FULL_VER \
    -DLLVM_DIR=%{llvm_cmake}/llvm \
    -DLLVMSPIRV_INCLUDED_IN_LLVM=OFF \
    -DSPIRV_TRANSLATOR_DIR=/usr
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libopencl-clang.so.*

%files devel
%{_libdir}/libopencl-clang.so
%{_includedir}/cclang/opencl_clang.h
%{_includedir}/cclang/opencl-c.h
%{_includedir}/cclang/opencl-c-base.h
%{_includedir}/cclang/module.modulemap

%changelog
%autochangelog
