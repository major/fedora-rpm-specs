Name:		x86-simd-sort
Version:	4.0
Release:	%autorelease
Summary:	C++ template library for high performance SIMD based sorting algorithms

License:	BSD-3-Clause
URL:		https://github.com/intel/x86-simd-sort
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# C++ header file library for x86 processors.
ExclusiveArch:	x86_64

BuildRequires:	gcc-c++
BuildRequires:	gtest-devel
BuildRequires:	meson

%description
C++ template library for high performance SIMD based sorting routines for 
16-bit, 32-bit and 64-bit data types. The sorting routines are accelerated
using AVX-512/AVX2 when available. The library auto picks the best version
depending on the processor it is run on.
	
%package devel
Summary: Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

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

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libx86simdsortcpp.so.0

%files devel
%{_includedir}/x86simdsort.h
%{_libdir}/libx86simdsortcpp.so
%{_libdir}/pkgconfig/x86simdsortcpp.pc

%changelog
%autochangelog
