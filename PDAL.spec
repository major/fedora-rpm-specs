%global __cmake_in_source_build 1

# BZ 1996330
%ifarch ppc64le
%global _lto_cflags %nil
%endif

Summary:	Point Data Abstraction Library
Name:		PDAL
# NOTE: Re-verifiy test exclusions in %%check when updating
Version:	2.4.3
Release:	2%{?dist}
# The code is licensed BSD except for:
# - filters/private/csf/* and plugins/i3s/lepcc/* are ASL 2.0
# - vendor/arbiter/*, plugins/nitf/io/nitflib.h and plugins/oci/io/OciWrapper.* are Expat/MIT
# - plugins/e57/libE57Format/{src,include}/* is Boost
License:	BSD-3-Clause AND Apache-2.0 AND MIT AND BSL-1.0
URL:		https://www.pdal.io
Source:		https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}-src.tar.gz
# commented out due to size (320 MB larger)
#Source1:	http://download.osgeo.org/proj/vdatum/%%{name}-vdatums.zip
# originals
#Source1:   http://download.osgeo.org/proj/vdatum/egm08_25/egm08_25.gtx
#Source2:   http://download.osgeo.org/proj/vdatum/egm08_25/egm08_25.txt
#Source3:   http://download.osgeo.org/proj/vdatum/egm96_15/egm96_15.gtx
#Source4:   http://download.osgeo.org/proj/vdatum/egm96_15/WW15MGH.TXT
#Source5:   http://download.osgeo.org/proj/vdatum/vertcon/README.TXT
#Source6:   http://download.osgeo.org/proj/vdatum/vertcon/vertconc.gtx
#Source7:   http://download.osgeo.org/proj/vdatum/vertcon/vertcone.gtx
#Source8:   http://download.osgeo.org/proj/vdatum/vertcon/vertconw.gtx
#Source9:   http://download.osgeo.org/proj/vdatum/usa_geoid1999.zip
#Source10:  http://download.osgeo.org/proj/vdatum/usa_geoid2003.zip
#Source11:  http://download.osgeo.org/proj/vdatum/usa_geoid2009.zip
#Source12:  http://download.osgeo.org/proj/vdatum/usa_geoid2012.zip
#Source13:  http://download.osgeo.org/proj/vdatum/usa_geoid2012b.zip

# Unbundle some bundled libraries
Patch0:		PDAL_unbundle.patch

# Use correct libdir for PDAL_DRIVER_PATH when running tests
Patch1:		PDAL_tests.patch

# fix build with sphinxcontrib-bibtex 2.0 (RHBZ #1921498)
Patch2:		PDAL_sphinxconf.patch

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	eigen3-devel
BuildRequires:	gcc-c++
BuildRequires:	gdal
BuildRequires:	gdal-devel
BuildRequires:	geos-devel
BuildRequires:	gtest-devel
BuildRequires:	hdf5-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libgeotiff-devel
BuildRequires:	libpq-devel
BuildRequires:	libxml2-devel
BuildRequires:	libzstd-devel
BuildRequires:  make
BuildRequires:	netcdf-cxx-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-server
BuildRequires:	proj-devel
%if 0%{?fedora}
# yet missing for EPEL8 BZ#1808766
BuildRequires:	python3-breathe
%endif
BuildRequires:	python3-devel
BuildRequires:	python3-numpy
BuildRequires:	python3-sphinx
%if 0%{?fedora}
# yet missing for EPEL8
BuildRequires:	python3-sphinxcontrib-bibtex
BuildRequires:  python3-sphinxcontrib-spelling
%endif
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	qhull-devel
BuildRequires:	sqlite-devel
BuildRequires:	zlib-devel

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	bash-completion

# https://github.com/connormanning/arbiter bundled in vendor/arbiter
Provides:	bundled(arbiter)
# https://github.com/mkazhdan/PoissonRecon bundled in vendor/kazhdan
Provides:	bundled(PoissonRecon)
# https://github.com/jlblancoc/nanoflann bundled in vendor/nanoflann
Provides:	bundled(nanoflann)
# https://github.com/nlohmann/json bundled in vendor/nlohmann
Provides:	bundled(nlohmann)

%description
PDAL is a BSD licensed library for translating and manipulating point cloud
data of various formats. It is a library that is analogous to the GDAL raster
library. PDAL is focused on reading, writing, and translating point cloud
data from the ever-growing constellation of data formats. While PDAL is not
explicitly limited to working with LiDAR data formats, its wide format
coverage is in that domain.

PDAL is related to Point Cloud Library (PCL) in the sense that both work with
point data, but PDAL’s niche is data translation and processing pipelines, and
PCL’s is more in the algorithmic exploitation domain. There is cross over of
both niches, however, and PDAL provides a user the ability to exploit data
using PCL’s techniques.

%package devel
Summary:	PDAL development header files and libraries
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The pdal-devel package contains the header files and libraries needed to
compile C or C++ applications which will directly interact with PDAL.

%package libs
Summary:	The shared libraries required for PDAL

%description libs
The pdal-libs package provides the essential shared libraries for any
PDAL client program or interface. You will need to install this package
to use PDAL

# commented out due to size
#%%package vdatums
#Summary:	Vertical datum and geoid files for PDAL
#Requires:	%%{name} = %%{version}-%%{release}
#
#%%description vdatums
#This package contains vertical datum and geoid files for PDAL.

%package doc
Summary:	Documentation for PDAL
BuildArch:	noarch

%description doc
This package contains documentation for PDAL.

# We don't want to provide private PDAL extension libs (to be verified)
%global __provides_exclude_from ^%{_libdir}/libpdal_plugin.*\.so.*$


%prep
%autosetup -p1 -n %{name}-%{version}-src

# Remove some bundled libraries
rm -rf vendor/{eigen,gtest,pdalboost}


%build
%cmake	-D PDAL_LIB_INSTALL_DIR:PATH=%{_lib} \
	-D CMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	-D CMAKE_VERBOSE_MAKEFILE=ON  \
	-D GEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \
	-D BUILD_PGPOINTCLOUD_TESTS:BOOL=OFF \
	-D WITH_COMPLETION=ON \
	-D WITH_LAZPERF=ON \
	-D WITH_TESTS=ON \
	-D PDAL_HAVE_LIBGEOTIFF=ON \
	-D PDAL_HAVE_LIBXML2=ON \
	-D POSTGRESQL_INCLUDE_DIR=%{_includedir}/pgsql \
	-D POSTGRESQL_LIBRARIES=%{_libdir}/libpq.so .

%cmake_build

# Build documentation
%if 0%{?fedora}
# dependencies yet missing for EPEL8 BZ#1808766
(
cd doc
sphinx-build -b html . build/html
)
%endif

%install
%cmake_install

# commented out due to size
## unpack vertical datums
#mkdir -p %%{buildroot}%%{_datadir}/proj
#mkdir vdatum
#pushd vdatum
#unzip -o %%{SOURCE1}
#mv *.gtx  %%{buildroot}%%{_datadir}/proj/
#popd
#rm -rf vdatum


%check
## test the compiled code (see doc/project/testing.rst)
# we skip tests for selected architectures which need upstream fixes
%ifarch armv7hl aarch64 ppc64le s390x
(cd %{_vpath_builddir} && ctest --output-on-failure || true)
%else
## we skip the PG test (BUILD_PGPOINTCLOUD_TESTS:BOOL=OFF):
# PGUSER=pdal PGPASSWORD=password PGHOST=localhost PGPORT=5432 ctest -V

# Use plain ctest as opposed to %%ctest, which runs tests in parallel, and appears to trigger
# a race condition when running pdal_filters_overlay_test, leading to
# "Unable to open stream for '/builddir/build/BUILD/PDAL-2.2.0-src/test/data/../temp/temp.laz' with error 'No such file or directory'".
%ifarch i686
# https://github.com/PDAL/PDAL/issues/3469
# https://github.com/PDAL/PDAL/issues/3501
%ctest || :
%else
# https://github.com/PDAL/PDAL/issues/3501
%ctest || :
%endif
%endif

%files
%{_bindir}/pdal
%{_datadir}/bash-completion/completions/pdal

%files libs
%license LICENSE.txt
%license vendor/arbiter/LICENSE
%license plugins/e57/libE57Format/LICENSE.md
%{_libdir}/libpdal_base.so.14*
%{_libdir}/libpdal_plugin_kernel_fauxplugin.so.14*
%{_libdir}/libpdal_plugin_reader_pgpointcloud.so.14*
%{_libdir}/libpdal_plugin_writer_pgpointcloud.so.14*
%{_libdir}/libpdal_util.so.14*

%files devel
%{_bindir}/pdal-config
%{_includedir}/pdal/
# drop unversioned symbolic links (BZ#1841616)
%exclude %{_libdir}/libpdal_plugin_kernel_fauxplugin.so
%exclude %{_libdir}/libpdal_plugin_reader_pgpointcloud.so
%exclude %{_libdir}/libpdal_plugin_writer_pgpointcloud.so
%{_libdir}/libpdal_base.so
%{_libdir}/libpdal_util.so
%{_libdir}/libpdalcpp.so
%{_libdir}/cmake/PDAL/
%{_libdir}/pkgconfig/*.pc

# commented out due to size
#%%files vdatums
#%%attr(0644,root,root) %%{_datadir}/proj/*.gtx

%files doc
%if 0%{?fedora}
%doc doc/build/html
%endif
%license LICENSE.txt

%changelog
* Wed Nov 09 2022 Markus Neteler <neteler@mundialis.de> 2.4.3-2
- SPDX license tag update

* Sat Aug 06 2022 Sandro Mani <manisandro@gmail.com> - 2.4.3-1
- Update to 2.4.3

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Sandro Mani <manisandro@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 2.4.0-2
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Mon Mar 28 2022 Markus Neteler <neteler@mundialis.de> 2.4.0-1
- new upstream version
- removed laszip requirement as lasperf is now used
- deactivated unbundling of some bundled libraries, see https://github.com/PDAL/PDAL/issues/3719
- fix https://github.com/PDAL/PDAL/pull/3720
- ppc64le: workaround for BZ #1996330

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 2.3.0-5
- Rebuild for hdf5 1.12.1

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 2.3.0-4
- Rebuild (gdal)

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 2.3.0-3
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Markus Neteler <neteler@mundialis.de> 2.3.0-1
- new upstream version
- removed broken tests patch

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 2.2.0-8
- Rebuild (gdal)

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-7
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.2.0-6
- rebuild for libpq ABI fix rhbz#1908268

* Thu Jan 28 2021 Markus Neteler <neteler@mundialis.de> 2.2.0-6
- fix build with sphinxcontrib-bibtex 2.0 (RHBZ #1921498)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-4
- Rebuilt for Boost 1.75

* Fri Nov  6 22:41:05 CET 2020 Sandro Mani <manisandro@gmail.com> - 2.2.0-3
- Rebuild (proj, gdal)

* Sat Oct 24 2020 Markus Neteler <neteler@mundialis.de> 2.2.0-2
- add laszip-devel requirement to PDAL-devel (fixes BZ #1891154)
- activated bash completion

* Sat Oct 17 2020 Markus Neteler <neteler@mundialis.de> 2.2.0-1
- new upstream version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Markus Neteler <neteler@mundialis.de> 2.1.0-8
- enable EPEL8 compilation by dropping sphinx docs for now

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 2.1.0-7
- Rebuilt for Boost 1.73

* Sat May 30 2020 Markus Neteler <neteler@mundialis.de> 2.1.0-6
- drop unversioned symbolic links of libpdal_plugin_* in PDAL-devel (BZ#1841616)

* Wed May 27 2020 Sandro Mani <manisandro@gmail.com> 2.1.0-5
- license statements updates

* Sat May 23 2020 Sandro Mani <manisandro@gmail.com> 2.1.0-4
- major cleanup, see BZ#1838686

* Fri May 22 2020 Markus Neteler <neteler@mundialis.de> 2.1.0-3
- commented out vertical datums due to size for initial Fedora upload
- cleanup upon review by Sandro Mani, BZ#1838686

* Thu May 14 2020 Markus Neteler <neteler@mundialis.de> 2.1.0-2
- fix qhull package name for EPEL 8

* Wed Apr 01 2020 Markus Neteler <neteler@mundialis.de> 2.1.0-1
- New 2.1.0 upstream release

* Wed Sep 18 2019 Markus Neteler <neteler@mundialis.de> 2.0.1-2
- removed unused points2grid dependency

* Mon Sep 16 2019 Markus Neteler <neteler@mundialis.de> 2.0.1-1
- New 2.0.1 upstream release
- PCL support dropped as per release notes
- added BuildRequires gcc-c++ as per RHBZ #1551327 (removing gcc and gcc-c++ from default buildroot)
- further dependency cleanup

* Mon Apr 01 2019 Markus Neteler <neteler@mundialis.de> 1.8.0-2
- fix for "nothing provides pkgconfig(geos) needed by PDAL-devel..."

* Wed Nov 07 2018 Markus Neteler <neteler@mundialis.de> 1.8.0-1
- New 1.8.0 upstream release

* Mon May 14 2018 Markus Neteler <neteler@mundialis.de> 1.7.2-2
- New 1.7.2 upstream release
- hexer no longer required

* Thu May 10 2018 Markus Neteler <neteler@mundialis.de> 1.7.2-1
- New 1.7.2RC2 upstream release
- enforce python3
- set -DBUILD_PLUGIN_PYTHON:BOOL=FALSE to avoid numpy detection error

* Fri Apr 20 2018 Markus Neteler <neteler@mundialis.de> 1.7.0-1
- New 1.7.0 upstream release
- patch for https://github.com/PDAL/PDAL/issues/1899
- patch using https://github.com/PDAL/PDAL/pull/1900

* Thu Dec 14 2017 Markus Neteler <neteler@mundialis.de> 1.6.0-3
- fix pkgconfig (must be in -devel)

* Sat Oct 28 2017 Markus Neteler <neteler@mundialis.de> 1.6.0
- New 1.6.0 upstream release

* Tue Oct 24 2017 Markus Neteler <neteler@mundialis.de> 1.5.0
- New 1.5.0 upstream release
- vertical datums added

* Sun Jan  8 2017 Markus Neteler <neteler@osgeo.org> 1.4.0
- New upstream release
- configure tweaks

* Sat Jun 20 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.9-4
- Change build type from Debug to Release

* Mon Apr 20 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.9-3
- Various updates:
 - Build with hexer support
 - Own directories in devel subpackage
 - omit deprecated Group: tags and %%clean section
 - Use better macros for make and cmake
 - use %%{?_isa} macro in subpkg dependencies
 - have %%build section envoke 'make'
 - Update %%install section
 - Improve cmake build parameters
 - Use %%license macro
 - Add %%doc
 - Get rid of BuildRoot definition
 - No need to cleanup buildroot during %%install
 - Remove %%defattr
 - Run ldconfig
 - Add PostgreSQL and PointCloud support
 - Add Python and PCL plugins
 - Build with GEOS and OPENNI2 support
 - Update BR and Requires
 - Add -libs subpackage, and move related files there

* Fri Apr 10 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.9-2
- Add -devel subpackage, and move related files there.

* Fri Apr 10 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.9-1
- Update to 0.9.9

* Tue Mar 10 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.8-3
- Add support for more stuff.

* Sun Mar 8 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.8-2
- Rebuild with new GDAL and the new build points2grid.

* Tue Jan 13 2015 Devrim GUNDUZ <devrim@gunduz.org> 0.9.8-1
- Initial packaging

