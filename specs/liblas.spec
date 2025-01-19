%global commit 96d4dc9d6abc93c683ee97cfd14a984148390320
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           liblas
Version:        1.8.2
Release:        0.21%{?shortcommit:.git%shortcommit}%{?dist}
Summary:        Library for reading and writing the very common LAS LiDAR format

# Automatically converted from old format: BSD and Boost - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND BSL-1.0
URL:            https://www.liblas.org
%if 0%{?commit:1}
Source0:        https://github.com/libLAS/libLAS/archive/%{commit}/libLAS-%{shortcommit}.tar.gz
%else
Source0:        https://download.osgeo.org/%{name}/libLAS-%{version}.tar.bz2
%endif

# Fix build against recent gdal3+
# https://github.com/libLAS/libLAS/issues/164
# From https://github.com/OSGeo/gdal/blob/master/gdal/MIGRATION_GUIDE.TXT:
#  removal of OSRFixup() and OSRFixupOrdering(): no longer needed since objects constructed are always valid
Patch1:         liblas_gdal3.patch

# Fix incorrect libgeotiff pkgconfig require resulting in broken dependencies
# Fix incorrect includedir and libdir paths
Patch2:         liblas_pkgconfig.patch

# Fix FTBFS with boost 1.73
Patch3:         liblas_boost173.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel >= 1.53
BuildRequires:  cmake
BuildRequires:  gdal-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  laszip-devel
BuildRequires:  libgeotiff-devel
BuildRequires:  zlib-devel
# FIXME? 
#  The imported target "ZLIB::zlibstatic" references the file
#     "/usr/lib/libz.a"
#  but this file does not exist.
BuildRequires:  zlib-ng-compat-static

%description
libLAS is a C/C++ library for reading and writing the very common LAS LiDAR
format. The ASPRS LAS format is a sequential binary format used to store
data from LiDAR sensors and by LiDAR processing software for data
interchange and archival.

%package devel
Summary:	libLAS development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

Requires:	boost-devel >= 1.53
Requires:	gdal-devel
Requires:	laszip-devel
Requires:	libgeotiff-devel

%description devel
libLAS deveolpment files.

%package tools
Summary:	libLAS utility applications
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
libLAS utility applications.


%prep
%if 0%{?commit:1}
%autosetup -p1 -n libLAS-%{commit}
%else
%autosetup -p1 -n libLAS-%{version}
%endif


%build
%cmake \
        -DCMAKE_SKIP_RPATH:BOOL=ON \
        -DLIBLAS_LIB_SUBDIR:PATH="%{_lib}" \
        -DWITH_GDAL:BOOL=ON \
        -DWITH_LASZIP:BOOL=ON \
        -DWITH_TESTS:BOOL=ON
%cmake_build


%install
%cmake_install


%files
%exclude %{_datadir}/%{name}/
%{_libdir}/*.so.3
%{_libdir}/*.so.2.*

%files devel
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/libLAS/
%{_libdir}/pkgconfig/liblas.pc
%{_libdir}/*.so

%files tools
%doc AUTHORS README.txt
%{_bindir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.21.git96d4dc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.20.git96d4dc9
- Rebuild (GDAL)

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.19.git96d4dc9
- Rebuild (GDAL)

* Fri Nov 08 2024 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.18.git96d4dc9
- Rebuild (gdal)

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.2-0.17.git96d4dc9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.16.git96d4dc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 14 2024 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.15.git96d4dc9
- Update to git 96d4dc9

* Mon May 13 2024 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.14.gitf1da555
- Rebuild (gdal)

* Wed Apr 03 2024 Orion Poplawski <orion@nwra.com> - 1.8.2-0.13.gitf1da555
- Add patch to fix cmake dependencies

* Mon Mar 04 2024 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.12.gitf1da555
- Update to git f1da555, fixes CVE-2024-27507

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.11.gitded4637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.10.gitded4637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.8.2-0.9.gitded4637
- Rebuilt for Boost 1.83

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.8.gitded4637
- Rebuild (gdal)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.7.gitded4637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.6.gitded4637
- Rebuild (gdal)

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.8.2-0.5.gitded4637
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.4.gitded4637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.3.gitded4637
- Rebuild (gdal)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-0.2.gitded4637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 1.8.2-0.1.gitded4637
- Update to git ded4637

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.8.1-21.gitd76a061
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.8.1-20.gitd76a061
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-19.gitd76a061
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 1.8.1-18.gitd76a061
- Rebuild (gdal)

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.8.1-17.gitd76a061
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-16.gitd76a061
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 1.8.1-15.gitd76a061
- Rebuild (gdal)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-14.gitd76a061
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.8.1-13.gitd76a061
- Rebuilt for Boost 1.75

* Fri Nov  6 22:01:04 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-12.gitd76a061
- Rebuild (proj, gdal)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11.gitd76a061
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-10.gitd76a061
- Fix liblas_pkgconfig.patch

* Mon Jun 08 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-9.gitd76a061
- Rebuild (boost)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-8.gitd76a061
- Rebuild (gdal)

* Wed May 06 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-7.gitd76a061
- Add liblas_pkgconfig.patch

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-6.gitd76a061
- Add patches for CVE-2018-20539, CVE-2018-20537, CVE-2018-20536, CVE-2018-20540

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-5.gitd76a061
- Update to latest git

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-4
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-24
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-21
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-18
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-17
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-15
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-14
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-13
- Rebuilt for linker errors in boost (#1331983)

* Tue Mar 15 2016 Thomas Kreuzer <thomas.kreuzer@uni-vechta.de> - 1.8.0-12
- Put licence file into correct place.

* Thu Mar 10 2016 Thomas Kreuzer <thomas.kreuzer@uni-vechta.de> - 1.8.0-11
- Fix bug #1311953

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Mon Jul 27 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.0-6
- Rebuilt for libgdal

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.8.0-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Devrim GUNDUZ <devrim@gunduz.org> 1.8.0-3
- Various updates, per Fedora review from Rex:
 - Update license
 - omit INSTALL from %%doc
 - Own directories in -devel subpackage
 - omit deprecated Group: tags and %%clean section
 - Use better macros for make and cmake
 - use %%%{?_isa} macro in subpkg dependencies
 - have %%build section envoke 'make'
 - Update %%install section
 - Improve cmake build parameters, also fix rpath
 - move liblaszip.so symlink to -devel subpkg
 - move liblas-config to -devel subpackage
 - Split -devel and -libs subpackages

* Fri Apr 17 2015 Devrim GUNDUZ <devrim@gunduz.org> 1.8.0-2
- Various updates:
  * Split -devel and -libs subpackages
  * Use %%license macro
  * Use %%make_install macro
  * Get rid of BuildRoot definition
  * No need to cleanup buildroot during %%install
  * Remove %%defattr
  * Run ldconfig
  * Fix version numbers in spec file
  * BR laszip-devel, and require laszip, per recent laszip changes.

* Tue Jan 13 2015 Devrim GUNDUZ <devrim@gunduz.org> 1.8.0-1
- Initial packaging
