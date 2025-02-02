#TODO: Run test suite (see debian/rules)

Name:           qgis
Version:        3.40.3
Release:        2%{?dist}
Summary:        A user friendly Open Source Geographic Information System

# http://issues.qgis.org/issues/3789
#               QGIS license         the bundled JS code (see %%{name}-%%{version}-vendor-licenses.txt)
License:        GPL-2.0-or-later AND MIT AND ISC AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND MIT AND (MIT OR CC0-1.0) AND Unlicense AND (MIT OR Apache-2.0) AND CC0-1.0 AND (MIT AND CC-BY-3.0) AND Python-2.0.1 AND CC-BY-4.0 AND (BSD-3-Clause OR GPL-2.0-only) AND (WTFPL OR MIT) AND (MIT AND BSD-3-Clause) AND CC-BY-3.0 AND MPL-2.0
URL:            http://www.qgis.org

Source0:        http://qgis.org/downloads/%{name}-%{version}.tar.bz2
# ./prepare_vendor.sh
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        %{name}-%{version}-vendor-licenses.txt
# Sample configuration files for QGIS server
Source3:        %{name}-server-httpd.conf
Source4:        %{name}-server-README.fedora
# MIME definitions
# Based on debian/qgis.xml but excluding already defined or proprietary types
#TODO: Path; Still necessary?
Source5:        %{name}-mime.xml

# Fix QGIS Server prefix calculation
Patch0:         %{name}-serverprefix.patch
# Pass --offline to yarn, plus replace deprecated md4 with sha256 in webpack sources
Patch1:         %{name}-yarn-offline.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  draco-devel
BuildRequires:  exiv2-devel
BuildRequires:  expat-devel
BuildRequires:  fcgi-devel
BuildRequires:  flex bison
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  grass-devel
BuildRequires:  gsl-devel
BuildRequires:  laszip-devel
BuildRequires:  libspatialite-devel
BuildRequires:  libdxfrw-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  ninja-build
BuildRequires:  netcdf-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
# PDAL detection relies on pdal executable
BuildRequires:  PDAL
BuildRequires:  PDAL-devel
BuildRequires:  poly2tri-devel
BuildRequires:  postgresql-devel
BuildRequires:  proj-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  python3-devel
BuildRequires:  python3-qscintilla-qt5
BuildRequires:  python3-qscintilla-qt5-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  %{py3_dist sip} >= 5.3
BuildRequires:  %{py3_dist PyQt-builder} >= 1
BuildRequires:  qca-qt5-devel
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  qwt-qt5-devel
BuildRequires:  spatialindex-devel
BuildRequires:  sqlite-devel
BuildRequires:  libzstd-devel
BuildRequires:  yarnpkg

# Enable for tests
#BuildRequires:  xorg-x11-server-Xvfb

Requires:       gpsbabel
# As found in BZ#1396818
#TODO: Not picked up by build system? Relevant?
Requires:       qca-qt5-ossl

# We don't want to provide private Python extension libs
%global __provides_exclude_from ^(%{python3_sitearch}|%{_libdir}/%{name}/plugins)/.*\.so(\.%{version})?$


%description
Geographic Information System (GIS) manages, analyzes, and displays
databases of geographic information. QGIS supports shape file
viewing and editing, spatial data storage with PostgreSQL/PostGIS, projection
on-the-fly, map composition, and a number of other features via a plugin
interface. QGIS also supports display of various geo-referenced raster and
Digital Elevation Model (DEM) formats including GeoTIFF, Arc/Info ASCII Grid,
and USGS ASCII DEM.


%package devel
Summary:        Development Libraries for the QGIS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development packages for QGIS including the C header files.


%package grass
Summary:        GRASS Support Libraries for QGIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       grass%{?_isa}

%description grass
GRASS plugin for QGIS required to interface with the GRASS system.


%package -n python3-qgis
%{?python_provide:%python_provide python3-qgis}
Summary:        Python integration and plug-ins for QGIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gdal
Requires:       python3-httplib2
Requires:       python3-jinja2
Requires:       python3-matplotlib
Requires:       python3-OWSLib
Requires:       python3-psycopg2
Requires:       python3-pygments
Requires:       python3-PyYAML
Requires:       python3-qscintilla-qt5
Requires:       python3-qt5-webkit
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Supplements:    %{name}%{?_isa} = %{version}-%{release}

%description -n python3-qgis
Python integration and plug-ins for QGIS.


%package server
Summary:        FCGI-based OGC web map server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mod_fcgid

%description server
This FastCGI OGC web map server implements OGC WMS 1.3.0 and 1.1.1.
The services are prepared as regular projects in QGIS. They're rendered using
the QGIS libraries. The server also supports SLD (Styled Layer Descriptor)
for styling. Sample configurations for Httpd and Lighttpd are included.

Please refer to %{name}-server-README.fedora for details!


%prep
%autosetup -p1 -a1

# %%{name}-%%{version}-vendor-licenses.txt
cp -a %{SOURCE2} .

# Readme file for QGIS server configuration and Lighttpd example
install -pm0644 %{SOURCE4} .

gzip ChangeLog

sed -i 's/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19"/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19 || 20 || 22"/' $(find "$PWD/.package-cache" | grep 'node_modules/@achrinza/node-ipc/package.json')
sed -i 's/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19"/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19 || 20 || 22"/' $(find "$PWD/.package-cache" | grep 'node_modules/@achrinza/node-ipc/.yarn-metadata.json')

%build
%cmake \
      %{_cmake_skip_rpath} \
      -D QGIS_LIB_SUBDIR=%{_lib} \
      -D QGIS_MANUAL_SUBDIR=/share/man \
      -D QGIS_CGIBIN_SUBDIR=%{_libexecdir}/%{name} \
      -D WITH_BINDINGS:BOOL=TRUE \
      -D WITH_GRASS8:BOOL=TRUE \
      -D GRASS_PREFIX8=`pkg-config --variable=prefix grass` \
      -D WITH_CUSTOM_WIDGETS:BOOL=TRUE \
      -D BINDINGS_GLOBAL_INSTALL:BOOL=TRUE \
      -D ENABLE_TESTS:BOOL=FALSE \
      -D WITH_EPT:BOOL=TRUE \
      -D WITH_PDAL:BOOL=TRUE \
      -D WITH_QSPATIALITE:BOOL=TRUE \
      -D WITH_QWTPOLAR:BOOL=TRUE \
      -D WITH_INTERNAL_QWTPOLAR:BOOL=FALSE \
      -D WITH_SERVER:BOOL=TRUE \
      -D WITH_3D:BOOL=TRUE \
      -D WITH_QSPATIALITE:BOOL=TRUE \
      -D WITH_SERVER_LANDINGPAGE_WEBAPP=ON \
      -G Ninja
export YARN_CACHE_FOLDER="$PWD/.package-cache"
%cmake_build


%install
%cmake_install

# Install desktop file without connecting proprietary file types
desktop-file-edit \
    --remove-mime-type="application/x-raster-ecw" \
    --remove-mime-type="application/x-raster-mrsid" \
    %{buildroot}%{_datadir}/applications/org.qgis.qgis.desktop

# Install MIME type definitions
install -d %{buildroot}%{_datadir}/mime/packages
install -pm0644 %{SOURCE5} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

install -pd %{buildroot}%{_datadir}/pixmaps
install -pm0644 images/icons/%{name}-icon-512x512.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pm0644 images/icons/%{name}_icon.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -pm0644 images/icons/%{name}-mime-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}-mime.png

# Install basic QGIS Mapserver configuration for Apache
install -pd %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/qgis-server.conf

# Remove install instructions
rm -f %{buildroot}%{_datadir}/%{name}/doc/INSTALL*

# Drop static library
rm -f %{buildroot}%{_prefix}/lib/liboauth2authmethod_static.a

%find_lang %{name} --with-qt


%check
# All tests basically run fine, but one fails using mock, while a different one fails when building with rpmbuild alone
#export LD_LIBRARY_PATH=%%{buildroot}%%{_libdir}
#xvfb-run -a -n 1 -s "-screen 0 1280x1024x24 -dpi 96" make Experimental
#rm -f %%{_bindir}%%{name}_bench


%files -f %{name}.lang
%license COPYING %{name}-%{version}-vendor-licenses.txt
%doc BUGS NEWS.md README.md Exception_to_GPL_for_Qt.txt ChangeLog.gz
# QGIS shows the following files in the GUI, including the license text
%doc %{_datadir}/%{name}/doc/
%dir %{_datadir}/%{name}/i18n/
%{_libdir}/lib%{name}_native.so.*
%{_libdir}/lib%{name}_app.so.*
%{_libdir}/lib%{name}_analysis.so.*
%{_libdir}/lib%{name}_core.so.*
%{_libdir}/lib%{name}_gui.so.*
%{_libdir}/lib%{name}_3d.so.*
%{_libdir}/%{name}/
%{_qt5_plugindir}/sqldrivers/libqsqlspatialite.so
%{_bindir}/%{name}
%{_bindir}/%{name}_process
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}/
%{_datadir}/mime/packages/qgis.xml
%{_metainfodir}/*.appdata.xml
%{_datadir}/pixmaps/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}/images/
%{_datadir}/%{name}/resources/
%{_datadir}/%{name}/svg/
%exclude %{_libdir}/libqgisgrass*.so.*
%exclude %{_libdir}/%{name}/plugins/libplugin_grass8.so
%exclude %{_libdir}/%{name}/plugins/libprovider_grass8.so
%exclude %{_libdir}/%{name}/plugins/libprovider_grassraster8.so
%exclude %{_libdir}/%{name}/server/
%exclude %{_libdir}/%{name}/grass/
%exclude %{_datadir}/%{name}/resources/server/

%files devel
%{_datadir}/%{name}/FindQGIS.cmake
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*.so
%{?_qt5_plugindir}/designer/libqgis_customwidgets.so*

%files grass
%{_libdir}/lib%{name}grass*.so.*
%{_libdir}/%{name}/plugins/libplugin_grass8.so
%{_libdir}/%{name}/plugins/libprovider_grass8.so
%{_libdir}/%{name}/plugins/libprovider_grassraster8.so
%{_libdir}/%{name}/grass/
%{_datadir}/%{name}/grass/

%files -n python3-qgis
%{_libdir}/libqgispython.so.*
%{_datadir}/%{name}/python/
%{python3_sitearch}/%{name}/
%{python3_sitearch}/PyQt5/uic/widget-plugins/
%exclude %{python3_sitearch}/%{name}/server/
%exclude %{python3_sitearch}/%{name}/_server.so

%files server
%doc %{name}-server-README.fedora
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}-server.conf
%{_bindir}/qgis_mapserver
%{_libdir}/%{name}/server/
%{_libdir}/lib%{name}_server.so.*
%{_libexecdir}/%{name}/
%{python3_sitearch}/%{name}/server/
%{python3_sitearch}/%{name}/_server.so
%{_datadir}/%{name}/resources/server/


%changelog
* Fri Jan 31 2025 Sandro Mani <manisandro@gmail.com> - 3.40.3-2
- Rebuild for dropped python-qt5-webkit

* Tue Jan 21 2025 Sandro Mani <manisandro@gmail.com> - 3.40.3-1
- Update to 3.40.3

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 21 2024 Sandro Mani <manisandro@gmail.com> - 3.40.2-1
- Update to 3.40.2

* Fri Nov 22 2024 Sandro Mani <manisandro@gmail.com> - 3.40.1-1
- Update to 3.40.1

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 3.40.0-3
- Rebuild (GDAL)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 3.40.0-2
- Rebuild for hdf5 1.14.5

* Fri Oct 25 2024 Sandro Mani <manisandro@gmail.com> - 3.40.0-1
- Update to 3.40.0

* Sat Sep 14 2024 Sandro Mani <manisandro@gmail.com> - 3.38.3-1
- Update to 3.38.3

* Mon Sep 09 2024 Sandro Mani <manisandro@gmail.com> - 3.38.2-2
- Rebuild (PDAL)

* Sat Aug 17 2024 Sandro Mani <manisandro@gmail.com> - 3.38.2-1
- Update to 3.38.2

* Tue Jul 30 2024 Sandro Mani <manisandro@gmail.com> - 3.38.1-2
- Rebuild (grass)

* Sat Jul 20 2024 Sandro Mani <manisandro@gmail.com> - 3.38.1-1
- Update to 3.38.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Robert-André Mauchin <zebob.m@gmail.com> - 3.38.0-2
- Rebuild for exiv2 0.28.2

* Sat Jun 22 2024 Sandro Mani <manisandro@gmail.com> - 3.38.0-1
- Update to 3.38.0

* Sun Jun 16 2024 Robert-André Mauchin <zebob.m@gmail.com> - 3.36.3-3
- Rebuilt for exiv2 0.28.2

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.36.3-2
- Rebuilt for Python 3.13

* Sat May 18 2024 Sandro Mani <manisandro@gmail.com> - 3.36.3-1
- Update to 3.36.3

* Tue May 14 2024 Sandro Mani <manisandro@gmail.com> - 3.36.2-2
- Rebuild (gdal)

* Sat Apr 20 2024 Sandro Mani <manisandro@gmail.com> - 3.36.2-1
- Update to 3.36.2

* Fri Mar 22 2024 Sandro Mani <manisandro@gmail.com> - 3.36.1-1
- Update to 3.36.1

* Tue Mar 19 2024 Sandro Mani <manisandro@gmail.com> - 3.36.0-2
- Rebuild (PDAL)

* Fri Feb 23 2024 Sandro Mani <manisandro@gmail.com> - 3.36.0-1
- Update to 3.36.0

* Tue Jan 23 2024 Sandro Mani <manisandro@gmail.com> - 3.34.3-2
- Rebuild (libdraco)

* Sun Jan 21 2024 Sandro Mani <manisandro@gmail.com> - 3.34.3-1
- Update to 3.34.3

* Sat Dec 23 2023 Sandro Mani <manisandro@gmail.com> - 3.34.2-1
- Update to 3.34.2

* Sun Nov 26 2023 Sandro Mani <manisandro@gmail.com> - 3.34.1-1
- Update to 3.34.1

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 3.34.0-4
- Rebuild (gdal)

* Fri Nov 03 2023 Sandro Mani <manisandro@gmail.com> - 3.34.0-3
- Add supplements qgis to python3-qgis subpackage

* Sat Oct 28 2023 Sandro Mani <manisandro@gmail.com> - 3.34.0-2
- Rebuild (grass)

* Fri Oct 27 2023 Sandro Mani <manisandro@gmail.com> - 3.34.0-1
- Update to 3.34.0

* Sun Oct 15 2023 Sandro Mani <manisandro@gmail.com> - 3.32.3-2
- Rebuild (PDAL)

* Mon Sep 18 2023 Sandro Mani <manisandro@gmail.com> - 3.32.3-1
- Update to 3.32.3

* Sat Aug 19 2023 Sandro Mani <manisandro@gmail.com> - 3.32.2-1
- Update to 3.32.2

* Tue Aug 15 2023 Sandro Mani <manisandro@gmail.com> - 3.32.1-2
- Rebuild (libspatialite)

* Tue Jul 25 2023 Sandro Mani <manisandro@gmail.com> - 3.32.1-1
- Update to 3.32.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Sandro Mani <manisandro@gmail.com> - 3.32.0-1
- Update to 3.32.0

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.30.3-2
- Rebuilt for Python 3.12

* Fri May 26 2023 Sandro Mani <manisandro@gmail.com> - 3.30.3-1
- Update to 3.30.3

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 3.30.2-2
- Rebuild (gdal)

* Sun Apr 30 2023 Sandro Mani <manisandro@gmail.com> - 3.30.2-1
- Update to 3.30.2

* Fri Mar 31 2023 Sandro Mani <manisandro@gmail.com> - 3.30.1-1
- Update to 3.30.1

* Sat Mar 04 2023 Sandro Mani <manisandro@gmail.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jan 27 2023 Sandro Mani <manisandro@gmail.com> - 3.28.3-1
- Update to 3.28.3

* Sun Jan 22 2023 Sandro Mani <manisandro@gmail.com> - 3.28.2-4
- Rebuild (PDAL)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 3.28.2-2
- Rebuild (qwt)

* Fri Dec 16 2022 Sandro Mani <manisandro@gmail.com> - 3.28.2-1
- Update to 3.28.2

* Fri Nov 18 2022 Sandro Mani <manisandro@gmail.com> - 3.28.1-1
- Update to 3.28.1

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 3.28.0-2
- Rebuild (gdal)

* Tue Oct 25 2022 Sandro Mani <manisandro@gmail.com> - 3.28.0-1
- Update to 3.28.0

* Sat Sep 10 2022 Sandro Mani <manisandro@gmail.com> - 3.26.3-1
- Update to 3.26.3

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.26.2-2
- Rebuild for gsl-2.7.1

* Sat Aug 13 2022 Sandro Mani <manisandro@gmail.com> - 3.26.2-1
- Update to 3.26.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Sandro Mani <manisandro@gmail.com> - 3.26.1-1
- Update to 3.26.1

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 3.26.0-4
- Rebuild (qt5)

* Mon Jul 04 2022 Sandro Mani <manisandro@gmail.com> - 3.26.0-3
- Rebuild (grass)

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 3.26.0-2
- Rebuilt for Python 3.11

* Fri Jun 17 2022 Sandro Mani <manisandro@gmail.com> - 3.26.0-1
- Update to 3.26.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.24.3-4
- Rebuilt for Python 3.11

* Sun Jun 05 2022 Sandro Mani <manisandro@gmail.com> - 3.24.3-3
- Rebuild (grass)

* Mon May 23 2022 Sandro Mani <manisandro@gmail.com> - 3.24.3-2
- Fix python3-gdal requires

* Sun May 22 2022 Sandro Mani <manisandro@gmail.com> - 3.24.3-1
- Update to 3.24.3
- Enable PDAL support

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 3.24.2-3
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 3.24.2-2
- Rebuild (qt5)

* Sat Apr 16 2022 Sandro Mani <manisandro@gmail.com> - 3.24.2-1
- Update to 3.24.2

* Mon Mar 21 2022 Sandro Mani <manisandro@gmail.com> - 3.24.1-1
- Update to 3.24.1

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 3.24.0-3
- Rebuild for proj-9.0.0

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 3.24.0-2
- Rebuild (qt5)

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 3.24.0-1
- Update to 3.24.0

* Wed Feb 09 2022 Sandro Mani <manisandro@gmail.com> - 3.22.3-6
- Drop common image raster formats from qgis-mime.xml

* Mon Feb 07 2022 Sandro Mani <manisandro@gmail.com> - 3.22.3-5
- Workaround linking against libgrass_imagery.8.0.so

* Wed Feb 02 2022 Sandro Mani <manisandro@gmail.com> - 3.22.3-4
- Update qgis-grass8.patch

* Sun Jan 30 2022 Sandro Mani <manisandro@gmail.com> - 3.22.3-3
- Rebuild (grass)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Sandro Mani <manisandro@gmail.com> - 3.22.3-1
- Update to 3.22.3

* Wed Jan 12 2022 Sandro Mani <manisandro@gmail.com> - 3.22.2-3
- Update qgis-mime.xml

* Wed Jan 05 2022 Sandro Mani <manisandro@gmail.com> - 3.22.2-2
- Disable landingpage

* Fri Dec 17 2021 Sandro Mani <manisandro@gmail.com> - 3.22.2-1
- Update to 3.22.2

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 3.22.1-2
- Rebuild for hdf5 1.12.1

* Sat Nov 20 2021 Sandro Mani <manisandro@gmail.com> - 3.22.1-1
- Update to 3.22.1

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 3.22.0-7
- Rebuild (gdal)

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 3.22.0-6
- Rebuilt for protobuf 3.19.0

* Wed Nov 03 2021 Sandro Mani <manisandro@gmail.com> - 3.22.0-5
- Backport fix for GIL deadlock

* Mon Oct 25 2021 Sandro Mani <manisandro@gmail.com> - 3.22.0-4
- Move grass provider plugins to grass subpackage

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 3.22.0-2
- Rebuilt for protobuf 3.18.1

* Sat Oct 23 2021 Sandro Mani <manisandro@gmail.com> - 3.22.0-1
- Update to 3.22.0

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 3.20.3-2
- Rebuild (geos)

* Mon Sep 13 2021 Sandro Mani <manisandro@gmail.com> - 3.20.3-1
- Update to 3.20.3

* Mon Aug 16 2021 Orion Poplawski <orion@nwra.com> - 3.20.2-2
- Rebuild for netcdf 4.8.0 (again)

* Sat Aug 14 2021 Sandro Mani <manisandro@gmail.com> - 3.20.2-1
- Update to 3.20.2

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 3.20.1-3
- Rebuild for netcdf 4.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Sandro Mani <manisandro@gmail.com> - 3.20.1-1
- Update to 3.20.1

* Tue Jul 20 2021 Sandro Mani <manisandro@gmail.com> - 3.20.0-1
- Update to 3.20.0

* Sat Jul 10 2021 Scott Talbert <swt@techie.net> - 3.18.3-5
- Revert back to building with sip 4 due to no sip 6 support

* Tue Jun 08 2021 Scott Talbert <swt@techie.net> - 3.18.3-4
- Update to build with sip5+

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.18.3-3
- Rebuilt for Python 3.10

* Fri May 21 2021 Sandro Mani <manisandro@gmail.com> - 3.18.3-2
- Rebuild (gdal)

* Sun May 16 2021 Sandro Mani <manisandro@gmail.com> - 3.18.3-1
- Update to 3.18.3

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 3.18.2-2
- Rebuild (gdal)

* Sat Apr 17 2021 Sandro Mani <manisandro@gmail.com> - 3.18.2-1
- Update to 3.18.2

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 3.18.1-2
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Mar 24 2021 sandro Mani <manisandro@gmail.com> - 3.18.1-1
- Update to 3.18.1

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 3.18.0-2
- Rebuild (proj)

* Fri Feb 19 2021 Sandro Mani <manisandro@gmail.com> - 3.18.0-1
- Update to 3.18.0

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 3.16.3-5
- Rebuild (geos)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 3.16.3-4
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 12:49:18 CET 2021 Adrian Reber <adrian@lisas.de> - 3.16.3-2
- Rebuilt for protobuf 3.14

* Fri Jan 15 2021 Sandro Mani <manisandro@gmail.com> - 3.16.3-1
- Update to 3.16.3

* Wed Jan 13 14:42:26 CET 2021 Adrian Reber <adrian@lisas.de> - 3.16.2-2
- Rebuilt for protobuf 3.14

* Mon Dec 21 2020 Sandro Mani <manisandro@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Mon Nov 23 07:54:37 CET 2020 Jan Grulich <jgrulich@redhat.com> - 3.16.1-2
- rebuild (qt5)

* Fri Nov 20 2020 Sandro Mani <manisandro@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Wed Nov 11 13:08:14 CET 2020 Sandro Mani <manisandro@gmail.com> - 3.16.0-2
- Rebuild (proj, gdal)

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Nov 03 2020 Sandro Mani <manisandro@gmail.com> - 3.14.16-2
- Fix QGIS Server prefix calculation

* Sun Oct 18 2020 Orion Poplawski <orion@nwra.com> - 3.14.16-1
- Update to 3.14.16

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 3.12.1-7
- rebuild (qt5)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.12.1-4
- Rebuilt for Python 3.9

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.12.1-3
- Rebuild (gdal)

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.12.1-2
- rebuild (qt5)
- drop BR: qt5-devel

* Sat Mar 21 2020 Volker Froehlich <volker27@gmx.at> - 3.12.1-1
- New upstream release
- Don't require python3-qscintilla anymore (BZ #1815712)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.12.0-2
- Rebuild (gdal)

* Sat Feb 22 2020 Volker Froehlich <volker27@gmx.at> - 3.12.0-1
- New upstream release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Volker Froehlich <volker27@gmx.at> - 3.10.2-1
- New upstream release
- Add Hant translation again

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 3.10.1-2
- rebuild (qt5)

* Sat Dec 07 2019 Volker Froehlich <volker27@gmx.at> - 3.10.1-1
- New upstream release
- Remove Hant translation from files list (is no more)

* Thu Nov 14 2019 Volker Froehlich <volker27@gmx.at> - 3.10.0-1
- New upstream release 3.10

* Wed Oct 30 2019 Volker Froehlich <volker27@gmx.at> - 3.8.3-2
- sip-devel -> python3-sip-devel
- qscintilla-devel -> is no more

* Tue Oct 22 2019 Volker Froehlich <volker27@gmx.at> - 3.8.3-1
- Rebuild for spatialindex soname bump

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 3.8.2-6
- rebuild (qt5)

* Mon Sep 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.8.2-5
- use (namespaced) python3-pyqt5-sip-api

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.2-4
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.8.2-3
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.2-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Volker Fröhlich <volker27@gmx.at> - 3.8.2-1
- New upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Volker Fröhlich <volker27@gmx.at> - 3.8.1-1
- New upstream release

* Fri Jun 21 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.3-5
- Require python3-qscintilla-qt5 in python3 sub-package, BZ#1722653

* Fri Jun 07 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.3-4
- Add BR python3-qt5-webkit, BZ#1712275

* Wed Jun 05 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.3-3
- Require python3-sip-api instead of sip-api, BZ#1714490

* Wed May 22 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.3-2
- Remove the dependency on PyQt5-webkit, BZ#1712275

* Sat May 18 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.3-1
- New upstream release
- Add qt5-qtbase-private-devel for QtSql/private/qsqlcachedresult_p.h

* Fri Mar 22 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.2-1
- New upstream release

* Fri Mar 22 2019 Volker Fröhlich <volker27@gmx.at> - 3.6.1-1
- New upstream release

* Sat Feb 16 2019 Björn Esser <besser82@fedoraproject.org> - 3.4.4-3
- rebuilt (qscintilla)

* Tue Feb 12 2019 Björn Esser <besser82@fedoraproject.org> - 3.4.4-2
- rebuilt (qscintilla)

* Thu Jan 31 2019 Volker Fröhlich <volker27@gmx.at> - 3.4.4-1
- New upstream release

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 2.18.25-1
- Update to 2.18.25
- Fix broken provides

* Sat Nov 03 2018 Sandro Mani <manisandro@gmail.com> - 2.18.20-3
- Fix broken requires
- Fix build with namespaced SIP
- Fix grass detection
- Fix grass script shebangs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Volker Fröhlich <volker27@gmx.at> - 2.18.20-1
- New upstream release
- Rebuild for Grass to solve BZ#1577583

* Sat Mar 03 2018 Volker Fröhlich <volker27@gmx.at> - 2.18.16-4
- Rebuild for Grass

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Volker Fröhlich <volker27@gmx.at> - 2.18.16-2
- Remove Group keyword

* Sat Jan 20 2018 Volker Froehlich <volker27@gmx.at> - 2.18.16-1
- New upstream release

* Sat Dec 09 2017 Volker Froehlich <volker27@gmx.at> - 2.18.15-1
- New upstream release

* Tue Nov 07 2017 Volker Froehlich <volker27@gmx.at> - 2.18.14-1
- New upstream release

* Tue Aug 22 2017 Volker Froehlich <volker27@gmx.at> - 2.18.12-1
- New upstream release
- Add patch to solve SIP-4.19-related build failure

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.18.11-4
- Python 2 binary package renamed to python2-qgis
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Volker Froehlich <volker27@gmx.at> - 2.18.11-1
- New upstream release

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.18.10-7
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Jul 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.18.10-6
- rebuild (sip)

* Mon Jul 03 2017 Sandro Mani <manisandro@gmail.com> - 2.18.10-5
- Bump release for NVR parity with F26

* Thu Jun 29 2017 Sandro Mani <manisandro@gmail.com> - 2.18.10-4
- Drop unnecessary qgis-2.18.10-sip.patch

* Wed Jun 28 2017 Volker Froehlich <volker27@gmx.at> - 2.18.10-3
- Add patch to fix sip issues

* Mon Jun 26 2017 Sandro Mani <manisandro@gmail.com> - 2.18.10-2
- Disable parallel build for now to avoid build failures

* Sat Jun 24 2017 Volker Froehlich <volker27@gmx.at> - 2.18.10-1
- New upstream release

* Wed May 31 2017 Volker Froehlich <volker27@gmx.at> - 2.18.9-1
- New upstream release

* Fri May 19 2017 Volker Froehlich <volker27@gmx.at> - 2.18.8-1
- New upstream release

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 23 2017 Volker Froehlich <volker27@gmx.at> - 2.18.7-1
- New upstream release

* Fri Apr 07 2017 Volker Froehlich <volker27@gmx.at> - 2.18.6-1
- New upstream release

* Sat Mar 25 2017 Volker Froehlich <volker27@gmx.at> - 2.18.5-1
- New upstream release

* Wed Mar 01 2017 Sandro Mani <manisandro@gmail.com> - 2.18.4-2
- Add patch to fix FTBFS

* Fri Feb 24 2017 Volker Froehlich <volker27@gmx.at> - 2.18.4-1
- New upstream release

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.18.2-5
- rebuild (qscintilla)

* Tue Feb 14 2017 Volker Froehlich <volker27@gmx.at> - 2.18.2-4
- Apply build patch for SIP 4.19 (#16071)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Rex Dieter <rdieter@math.unl.edu> - 2.18.2-2
- rebuild (sip), disable PyQwt support (f26+, for now)

* Fri Dec 16 2016 Volker Froehlich <volker27@gmx.at> - 2.18.2-1
- New upstream release

* Sat Nov 26 2016 Volker Froehlich <volker27@gmx.at> - 2.18.1-1
- New upstream release

* Sun Nov 20 2016 Volker Froehlich <volker27@gmx.at> - 2.18.0-2
- Add qca-ossl to Requires, as of BZ#1396818

* Fri Oct 21 2016 Volker Froehlich <volker27@gmx.at> - 2.18.0-1
- New upstream release

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 2.16.3-1
- Update to 2.16.3
- Add patch to fix qreal usage on arm

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 2.16.2-1
- Update to 2.16.2 (bug #1378240)
- Add patch to fix build on 64-bit machines
- Drop unused cmake options
- Move %%grass_version macro to grass-devel, make it an install requirement

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.14.3-6
- rebuilt for matplotlib-2.0.0

* Thu Aug 11 2016 Volker Froehlich <volker27@gmx.at> - 2.14.3-5
- Replace dependency on PyQt4 with PyQt4-webkit, since webkit
  is in a sub-package now (BZ #1360485)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 07 2016 Volker Froehlich <volker27@gmx.at> - 2.14.3-3
- Version bump to be newer than F24

* Mon Jun 06 2016 Volker Froehlich <volker27@gmx.at> - 2.14.3-2
- Move grass version to BR. This will avoid building with a
  different version than intended. The sub-package dependencies
  is taken care of by soname versions.

* Mon May 23 2016 Volker Froehlich <volker27@gmx.at> - 2.14.3-1
- New upstream release

* Wed Apr 20 2016 Volker Froehlich <volker27@gmx.at> - 2.14.1-2
- Change BR of qca to qca2 to make things easier in EPEL
- Rebuild for BZ #1327360
- Make the requires on grass match an exact version again

* Sun Mar 27 2016 Volker Froehlich <volker27@gmx.at> - 2.14.1-1
- New upstream release
- Resolve the false sub-package dependency of python on server

* Fri Mar 25 2016 Devrim Gündüz <devrim@gunduz.org> - 2.14.0-5
- Depend exclusively against GRASS => 7.0.3

* Thu Mar 17 2016 Devrim Gündüz <devrim@gunduz.org> - 2.14.0-4
- Rebuild for GRASS 7.0.3

* Wed Mar 16 2016 Volker Froehlich <volker27@gmx.at> - 2.14.0-3
- Build with Grass 7
- Remove Requires-filtering, hiding the dependency on libgsl

* Wed Mar  9 2016 Volker Froehlich <volker27@gmx.at> - 2.14.0-2
- Add patch for upstream issue #14402 (MSSQL)

* Sat Feb 27 2016 Volker Froehlich <volker27@gmx.at> - 2.14.0-1
- New upstream release
- Add PyYAML as BR and disable the use of the bundled version
- Be more explicit about the supported version of grass
- Install proper icons (BZ #1166977)
- Break the dependency of the base package on the python sub-package
- Add a new locale not found by find_lang

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Volker Froehlich <volker27@gmx.at> - 2.12.3-1
- New upstream release

* Sat Dec 19 2015 Volker Froehlich <volker27@gmx.at> - 2.12.2-1
- New upstream release

* Fri Nov 27 2015 Volker Froehlich <volker27@gmx.at> - 2.12.1-1
- New upstream release

* Mon Oct 26 2015 Volker Froehlich <volker27@gmx.at> - 2.12.0-2
- Fix ARM build

* Sat Oct 24 2015 Volker Froehlich <volker27@gmx.at> - 2.12.0-1
- New upstream release
- Add qca BR

* Sun Jul 26 2015 Volker Froehlich <volker27@gmx.at> - 2.10.1-3
- Correct conditionals for spatialite support on PPC and Fedora
  (Thanks to Rafael Fonseca)

* Sun Jul 26 2015 Volker Froehlich <volker27@gmx.at> - 2.10.1-2
- Rebuild for GDAL 2.0

* Tue Jul 21 2015 Volker Fröhlich <volker27@gmx.at> - 2.10.1-1
- New upstream release

* Wed Jul  8 2015 Volker Fröhlich <volker27@gmx.at> - 2.10.0-1
- New upstream release
- Drop obsolete Grass CMake patch
- Add ARM build fix; Thanks again, Sandro Mani!
- Truncate the changelog a bit

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Volker Fröhlich <volker27@gmx.at> - 2.8.2-1
- New upstream release

* Mon Apr 20 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-4
- rebuild (qscintilla)

* Wed Mar 11 2015 Devrim GÜNDÜZ <devrim@gunduz.org> - 2.8.1-3
- Rebuild for Proj 4.9.1

* Mon Mar  9 2015 Volker Fröhlich <volker27@gmx.at> - 2.8.1-2
- Add upstream patch to fix the build on ARM

* Sun Mar  8 2015 Volker Fröhlich <volker27@gmx.at> - 2.8.1-1
- New upstream release, remove included patch change
- Rename mapserver sub-package to server
- Add a new locale not found by find_lang
- Partly solve the icon file naming issue (BZ#1166977)

* Thu Feb 19 2015 Dave Johansen <davejohansen@gmail.com> 2.6.1-2
- Rebuild for gcc 5.0 C++ ABI change

* Fri Jan  2 2015 Dave Johansen <davejohansen@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Sun Nov  2 2014 Volker Fröhlich <volker27@gmx.at> - 2.6.0-2
- Fix the build on ARMv7hl, thanks to Sandro Mani!
- Updated the removing of executable permissions from source code files
- Add qscintilla-python-devel as BR
- Don't build the dxf converter plug-in
- Remove the Python directory definitions that were necessary on EL5

* Sun Nov  2 2014 Volker Fröhlich <volker27@gmx.at> - 2.6.0-1
- New upstream release, drop obsolete patch, update the sip patch

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-6
- update mime scriptlet

* Sun Aug 10 2014 Devrim GÜNDÜZ <devrim@gunduz.org> - 2.4.0-5
- Rebuild against new grass

* Sat Aug  9 2014 Volker Fröhlich <volker27@gmx.at> - 2.4.0-4
- Rebuild for grass 6.4.4

* Mon Jul 28 2014 Volker Fröhlich <volker27@gmx.at> - 2.4.0-3
- Restore ARM build (Thanks to Sandro Mani for the patch!)

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.0-2
- rebuild (libspatialite)

* Sat Jun 28 2014 Volker Fröhlich <volker27@gmx.at> - 2.4.0-1
- New upstream release, drop obsolete patches, update remaining
- Remove references to "Quantum"
- Add CODING and BUGS file
- Add necessary direct Python module dependencies

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.0-3
- ARM build fix

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-2
- rebuild (sip)

* Sat Feb 22 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.0-1
- New upstream release
- Fix the issue of the license text not being shown in the GUI
- Drop EL5 support leftovers
- Remove private provides
- Remove unnecessary explicit paths for GDAL
- Simplify conditionals
- Remove custom plugin directory setting
- Delete bundled Pyspatialite
- Compress changelog file
- Simplify documentation labeling

* Fri Feb 07 2014 Volker Fröhlich <volker27@gmx.at> - 2.0.1-8
- Rebuild for minor ABI breakage in spatialindex 1.8.1

* Wed Dec 25 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.1-7
- Python sub-package must require psycopg2 for the Processing plug-in
  (BZ #1043683)

* Fri Nov 08 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.1-6
- Rebuild for new qwt and qwtpolar

* Sat Oct 19 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.1-5
- Patch QGIS #8507 -- QGIS trunk failed to compile with sip 4.15
- Patch QGIS #8601 -- sip: QgsFieldValidator::fixup has versioned and
  unversioned overloads

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-4
- rebuild (sip)

* Tue Oct  1 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.1-3
- Fix Grass version to make breakage more visible

* Fri Sep 27 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.1-2
- Remove import path for httplib2 module to use the system version
- Use upstream desktop files

* Wed Sep 25 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.1-1
- New upstream release
- Exclude ARM for now, due to build issues

* Sat Sep 14 2013 Volker Fröhlich <volker27@gmx.at> - 1.8.0-17
- Rebuild for grass 6.4.3

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-16
- Rebuild for gdal 1.10.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-14
- rebuild (sip)

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.8.0-13
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-11
- Rebuild for spatialindex soname bump

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> - 1.8.0-10
- Rebuild for libspatialite soname bump

* Thu Nov  8 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-9
- Build with system version of qextserialport
- Update config file to fit httpd 2.4 (BZ#871471)

* Wed Oct 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-8
- rebuild (sip)

* Thu Aug  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-7
- Append ppc to ppc64 conditionals

* Wed Jul 18 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-6
- Add patch for QGIS bug #5809

* Sat Jul  7 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-5
- Rebuilt too quick

* Sat Jul  7 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-4
- One more rebuild, due to a broken GDAL

* Fri Jul  6 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-3
- Rebuild for Spatialite 3

* Thu Jul  5 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-2
- Correct locale if clause
- Apply patch for older versions of SIP

* Fri Jun 29 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-1
- New upstream release
- Correct provides-filtering as of https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Usage
- Drop obsolete spatialindex patch
- FSF addresses are now correct
- Explicitly set PYSPATIALITE to false
- Don't ship the 4 MB changelog
- Use wildcard for soname versions

* Tue Apr 10 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.4-4
- Been to quick with rebuilding, proper spatialindex build wasn't used yet

* Mon Apr  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.4-3
- Apply patch for Spatialindex 1.7's include dir
- Rebuild for Spatialindex 1.7.1

* Fri Mar 23 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.4-2
- Rebuild for GRASS 6.4.2

* Sun Feb 19 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.4-1
- Update for new release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.3-1
- Update for new release
- Is also the rebuild for BZ#761147
- Arch-specifically require the base package

* Tue Nov 15 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.2-1
- Updated for new release
- No more themes directory
- Remove dispensable geo-referencing patch

* Sun Oct 16 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.1-2
- Findlang doesn't recognize sr@latin in Fedora 14 and older
- Build with system-wide spatialindex
- Remove if structures intended for EPEL package
  Due to the rapid development in QGIS and the libraries it uses,
  QGIS will not go to EPEL now; ELGIS provides rebuilds with more
  current versions: http://elgis.argeo.org/

* Sat Sep 24 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.1-1
- Update for new release
- Drop one patch that made it into the release
- Correct permissions for two cpp files
- Change spelling for changelog file
- Findlang seems to find sr@latin now, so don't explicitly list it
- Build with Qwtpolar
- Remove grass as BR
- Add GRASS_PREFIX again
  Cmake uses the first entry in FindGRASS.cmake,
  which is not fine for 64 bit systems

* Sun Jul 24 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.0-5
- Extend histogram patch, see BZ 725161

* Wed Jul 06 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.0-4
- Remove icon path macros, that don't work in EPEL
- Avoid creating unnecessary directories there
- Be explicit about the shared lib names in the files section
- Put libqgispython.so.1.7.0 in Python sub-package
- Correct FSF address

* Wed Jul 06 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.0-3
- Withdraw immature Lighty configuration
- Update README and provide a better sample configuration,
  that utilizes mod_rewrite

* Sun Jun 26 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.0-2
- Add histogram patch
- Add scriplets to refresh icon cache
- Mention Fedora specific readme file in QGIS mapserver description
- Update the aforementioned file and the Apache configuration
  with rewrite rules

* Sun Jun 26 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.0-1
- Update for 1.7
- License is now GPLv3+ (Sqlanyconnect)
- Add mapserver sub-package and require mod_fcgi
- Use upstreams current description text
- Drop now needless iconv
- Rename new Serbian translations
- Install MIME type definitions and icons
- Add Readme file and sample configuration for Mapserver
- Add patch to avoid segfault when geo-referencing
- Add conditional for Spatialite and PPC64
- Add conditional for GRASS and EPEL
- Delete bundled libspatialite before building
- Removed glob from /usr/bin/qgis in files section
