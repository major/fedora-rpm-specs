%global _lto_cflags %{nil}
# https://github.com/pytorch/FBGEMM/blob/main/CMakeLists.txt#L55
%global soversion 1.4.0
%global desc %{expand: \
FBGEMM (Facebook GEneral Matrix Multiplication) is a low-precision, high
performance matrix-matrix multiplications and convolution library for
server-side inference.

The library provides efficient low-precision general matrix multiplication for
small batch sizes and support for accuracy-loss minimizing techniques such as
row-wise quantization and outlier-aware quantization. FBGEMM also exploits
fusion opportunities in order to overcome the unique challenges of matrix
multiplication at lower precision with bandwidth-bound operations.}

Name:		fbgemm
Version:	1.6.0
Release:	%autorelease
Summary:	Facebook General Matrix-Matrix Multiplication

License:	BSD-3-Clause
URL:		https://github.com/pytorch/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		fbgemm-fedora.patch

ExclusiveArch:	x86_64

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	asmjit-devel
BuildRequires:	cpuinfo-devel
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libomp-devel

%description
%{desc}

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{desc}

%prep
%autosetup -p1 -n FBGEMM-%{version}

rm -rf external
# library version
sed -i '$a set_target_properties(fbgemm PROPERTIES SOVERSION 1 VERSION %{soversion})' CMakeLists.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_CXX_FLAGS="%{optflags} -mno-avx512f" \
	-DCMAKE_C_FLAGS="%{optflags} -mno-avx512f" \
	-DFBGEMM_LIBRARY_TYPE=shared \
	-DFBGEMM_BUILD_BENCHMARKS=OFF \
	-DFBGEMM_BUILD_TESTS=ON \
	-DFBGEMM_BUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libfbgemm.so.%{soversion}
%{_libdir}/libfbgemm.so.1

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/libfbgemm.so

%changelog
%autochangelog
