%global common_description %{expand:
Highway is a C++ library for SIMD (Single Instruction, Multiple Data), i.e.
applying the same operation to 'lanes'.}

%global toolchain clang

%if 0%{?rhel}
%bcond gtest 0
%bcond contrib 0
%else
%bcond gtest 1
%bcond contrib 1
%endif

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
%if %{with gtest}
BuildRequires:  gtest-devel
%endif
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
%cmake %{!?with_gtest:-DHWY_ENABLE_TESTS:BOOL=OFF} \
       %{?with_gtest:-DHWY_SYSTEM_GTEST:BOOL=ON} \
       %{!?with_contrib:-DHWY_ENABLE_CONTRIB:BOOL=OFF} \
       -DHWY_CMAKE_RVV:BOOL=OFF
%cmake_build

%install
%cmake_install

%if %{without gtest}
rm -vf %{buildroot}%{_libdir}/libhwy_test.so.*
rm -vrf %{buildroot}%{_includedir}/hwy/tests
rm -vf %{buildroot}%{_libdir}/libhwy_test.so
rm -vf %{buildroot}%{_libdir}/pkgconfig/libhwy-test.pc
%endif

%if %{without contrib}
rm -vf %{buildroot}%{_libdir}/libhwy_contrib.so.*
rm -vrf %{buildroot}%{_includedir}/hwy/contrib
rm -vf %{buildroot}%{_libdir}/libhwy_contrib.so
rm -vf %{buildroot}%{_libdir}/pkgconfig/libhwy-contrib.pc
%endif

%check
%ctest

%files
%license LICENSE
%{_libdir}/libhwy.so.1
%{_libdir}/libhwy.so.%{version}
%if %{with contrib}
%{_libdir}/libhwy_contrib.so.1
%{_libdir}/libhwy_contrib.so.%{version}
%endif
%if %{with gtest}
%{_libdir}/libhwy_test.so.1
%{_libdir}/libhwy_test.so.%{version}
%endif

%files devel
%license LICENSE
%{_includedir}/hwy/
%{_libdir}/cmake/hwy/
%{_libdir}/libhwy.so
%if %{with contrib}
%{_libdir}/libhwy_contrib.so
%{_libdir}/pkgconfig/libhwy-contrib.pc
%endif
%if %{with gtest}
%{_libdir}/libhwy_test.so
%{_libdir}/pkgconfig/libhwy-test.pc
%endif
%{_libdir}/pkgconfig/libhwy.pc

%files doc
%license LICENSE
%doc g3doc hwy/examples

%changelog
%autochangelog
