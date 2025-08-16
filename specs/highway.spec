%global common_description %{expand:
Highway is a C++ library for SIMD (Single Instruction, Multiple Data), i.e.
applying the same operation to 'lanes'.}

%global toolchain clang

Name:           highway
Version:        1.2.0
Release:        %autorelease
Summary:        Efficient and performance-portable SIMD

License:        Apache-2.0
URL:            https://github.com/google/highway
Source:         %url/archive/%{version}/%{name}-%{version}.tar.gz
# [PATCH] Made fixes to generic_ops-inl.h BitShuffle impl on big-endian
Patch:          %url/commit/3ce50ffa85577140bdf088d8ee7830b76ac2501c.patch
# [PATCH] Disable RVV runtime dispatch. Fixes #2227
#
# Public Clang <= 18 still appears to require compiler flags for RVV.
# GCC 13 also has an #error and 14 is missing mulh/mulhu.
#
# Also split HWY_HAVE_RUNTIME_DISPATCH into multiple macros to enable
# overriding parts of the logic.
Patch:          %url/commit/c95cc0237d2f7a0f5ca5dc3fb4b5961b2b1dcdfc.patch
# Fix FTBFS related to GCC15 on ppc64le
Patch:          https://github.com/google/highway/commit/dcc0ca1cd4245ecff9e5ba50818e47d5e2ccf699.patch

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  gtest-devel
BuildRequires:  libatomic

%description
%common_description

%package        devel
Summary:        Development files for Highway
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{common_description}

Development files for Highway.

%package        doc
Summary:        Documentation for Highway
BuildArch:      noarch

%description doc
%{common_description}

Documentation for Highway.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
    -DHWY_SYSTEM_GTEST:BOOL=ON \
    -DHWY_CMAKE_RVV:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libhwy.so.1
%{_libdir}/libhwy.so.%{version}
%{_libdir}/libhwy_contrib.so.1
%{_libdir}/libhwy_contrib.so.%{version}
%{_libdir}/libhwy_test.so.1
%{_libdir}/libhwy_test.so.%{version}

%files devel
%license LICENSE
%{_includedir}/hwy/
%{_libdir}/cmake/hwy/
%{_libdir}/libhwy.so
%{_libdir}/libhwy_contrib.so
%{_libdir}/libhwy_test.so
%{_libdir}/pkgconfig/libhwy.pc
%{_libdir}/pkgconfig/libhwy-contrib.pc
%{_libdir}/pkgconfig/libhwy-test.pc

%files doc
%license LICENSE
%doc g3doc hwy/examples

%changelog
%autochangelog
