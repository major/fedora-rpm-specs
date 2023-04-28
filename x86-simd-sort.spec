%global debug_package %{nil}

Name:		x86-simd-sort
Version:	1.0
Release:	%autorelease
Summary:	C++ header file library for high performance SIMD based sorting algorithms

License:	BSD-3-Clause
URL:		https://github.com/intel/x86-simd-sort
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		meson-build.patch
# https://github.com/intel/x86-simd-sort/commit/1735e86cda95a469357a19ab8984ad8530372e75
Patch1:		1735e86cda95a469357a19ab8984ad8530372e75.patch

# C++ header file library for x86 processors.
ExclusiveArch:	x86_64

BuildRequires:	gcc-c++
BuildRequires:	gtest-devel
BuildRequires:	meson

%description
C++ header file library for SIMD based 16-bit, 32-bit and 64-bit data type
sorting on x86 processors. Source header files are available in src directory.
We currently only have AVX-512 based implementation of quicksort. This 
repository also includes a test suite which can be built and run to test the 
sorting algorithms for correctness. It also has benchmarking code to compare 
its performance relative to std::sort.
	
%package devel
Summary: Development files for %{name}
BuildArch:	noarch
Provides:	%{name}-static = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test -v

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/*.h
%{_includedir}/*.hpp
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
