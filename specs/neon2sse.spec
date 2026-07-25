%global debug_package %{nil}
%global gitdate 20260428
%global commit ed59be8546632d5126ff69c87122ae5de20ffe4f
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name:		neon2sse
Version:	0.0^%{gitdate}git%{shortcommit}
Release:	%autorelease
Summary:	Library intended to simplify ARM->IA32 porting

License:	BSD-2-Clause
URL:		https://github.com/intel/ARM_NEON_2_x86_SSE
Source0:	%{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# test code for vector addition
Source1:	test.c

BuildArch:	noarch
ExclusiveArch:	x86_64

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc-c++

%description
The platform independent header allowing to compile any C/C++ code containing
ARM NEON intrinsic functions for x86 target systems using SIMD up to SSE4
intrinsic functions.

The NEON_2_SSE.h file is intended to simplify ARM->IA32 porting

%package devel
Summary:	Development files for %{name}
Provides:	%{name}-static = %{version}-%{release}

%description devel
The platform independent header allowing to compile any C/C++ code containing
ARM NEON intrinsic functions for x86 target systems using SIMD up to SSE4
intrinsic functions.

The NEON_2_SSE.h file is intended to simplify ARM->IA32 porting

%prep
%autosetup -n ARM_NEON_2_x86_SSE-%{commit}

cp %{SOURCE1} .

# fix path
sed -i 's/lib\/cmake/%{_lib}\/cmake/g' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
$CC -o test test.c -I%{buildroot}%{_includedir}
./test

%files devel
%license LICENSE
%doc ReadMe.md
%{_includedir}/NEON_2_SSE.h
%{_libdir}/cmake/NEON_2_SSE/

%changelog
%autochangelog
