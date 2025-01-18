Name:           exodusii
Version:        6.09
Release:        26%{?dist}
Summary:        Library to store and retrieve transient finite element data
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Url:            http://sourceforge.net/projects/exodusii/
#last version of the orinal source, got merge into https://github.com/gsjaardema/seacas
# but has different API
Source0:        http://distfiles.gentoo.org/distfiles/exodus-%{version}.tar.gz
Source1:        http://prod.sandia.gov/techlib/access-control.cgi/1992/922137.pdf
Source2:        http://gsjaardema.github.io/seacas/exodusII.pdf
Patch1:         sovers.diff

BuildRequires:  tcsh
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  netcdf-devel

%description
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for pre-processing (problem definition), post-processing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

%package devel
Summary:    Development headers and libraries for exodusII
Requires:   %{name}%{_isa} = %{version}-%{release}
Requires:   netcdf-devel

%description devel
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for pre-processing (problem definition), post-processing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

This package contains development headers and libraries for exodusII.

%package doc
Summary:    PDF documentation for exodusII
BuildArch:  noarch

%description doc
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for pre-processing (problem definition), post-processing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

This package contains pdf documentation for exodusII.

%prep
%setup -n exodus-%{version} -q
%patch -P 1 -p1
#avoid over-linking
#zlib is actually not a direct dep of exodus, but hdf5
sed -i '/FATAL_ERROR.*ZLib/s/^/#/' exodus/CMakeLists.txt

%build
cd exodus
export LDFLAGS="%{__global_ldflags} -Wl,--as-needed"
%{cmake} -DBUILD_SHARED=ON -DHDF5HL_LIBRARY="" -DHDF5_LIBRARY="" -DCMAKE_DISABLE_FIND_PACKAGE_ZLIB=ON -DZLIB_LIBRARY="" -DPYTHON=FALSE
%cmake_build

%install
cd exodus
%cmake_install
[[ %{_lib} = lib ]] || mv %{buildroot}/%{_prefix}/{lib,%{_lib}}
pushd %{buildroot}/%{_prefix}/%{_lib}
ln -s libexodus-*.so "%buildroot/%_libdir/libexodus.so"
ln -s libexoIIv2for-*.so "%buildroot/%_libdir/libexoIIv2for.so"
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -p %{S:1} %{S:2} %{buildroot}/%{_docdir}/%{name}

%check
cd exodus
%cmake_build --target check f_check

%ldconfig_scriptlets

%files devel
%{_includedir}/*
%{_libdir}/libexodus.so
%{_libdir}/libexoIIv2for.so

%files
%license exodus/COPYRIGHT
%{_libdir}/libexodus-*.so
%{_libdir}/libexoIIv2for-*.so

%files doc
%{_docdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 6.09-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 6.09-17
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 6.09-16
- Rebuild for netcdf 4.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Christoph Junghans <junghans@votca.org> - 6.09-13
- Fix out-of-source build on F33 (bug #1863520)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for netcdf 4.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Christoph Junghans <junghans@votca.org> - 6.09-1
- version bump to 6.09
- devel: fix deps

* Mon Oct 03 2016 Christoph Junghans <junghans@votca.org> - 6.02-5
- added __global_ldflags to LDFLAGS

* Mon Sep 26 2016 Christoph Junghans <junghans@votca.org> - 6.02-4
- Fixed another overlinking issue by --as-needed

* Fri Sep 09 2016 Christoph Junghans <junghans@votca.org> - 6.02-3
- Fixed testsuite
- Avoid over-linking
- Minor changes from review (bug #1336552)

* Sat Sep 03 2016 Christoph Junghans <junghans@votca.org> - 6.02-2
- Minor changes from review (bug #1336552)
- Added doc package

* Thu Sep 01 2016 Christoph Junghans <junghans@votca.org> - 6.02-1
- First release.
