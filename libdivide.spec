# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           libdivide
Version:        5.0
Release:        %autorelease
Summary:        Optimized integer division

License:        Zlib OR BSL-1.0
URL:            https://libdivide.com/
Source0:        https://github.com/ridiculousfish/libdivide/archive/%{version}/libdivide-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%global _description %{expand:
This package contains a header-only C/C++ library for optimizing integer
division. Integer division is one of the slowest instructions on most CPUs,
e.g. on current x64 CPUs a 64-bit integer division has a latency of up to 90
clock cycles whereas a multiplication has a latency of only 3 clock cycles.
libdivide allows you to replace expensive integer divsion instructions by a
sequence of shift, add and multiply instructions that will calculate the
integer division much faster.

On current CPUs you can get a speedup of up to 10x for 64-bit integer division
and a speedup of up to to 5x for 32-bit integer division when using libdivide.
libdivide also supports SSE2, AVX2 and AVX512 vector division which provides an
even larger speedup.}

%description %_description


%package        devel
Summary:        Development files for libdivide

# Header-only library
Provides:       libdivide-static = %{version}-%{release}

%description    devel %_description


%prep
%autosetup

# Disable -Werror
sed -i 's/;-Werror//;/-Werror/d' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%doc doc

%{_includedir}/libdivide.h
%{_libdir}/cmake/libdivide/


%changelog
%autochangelog
