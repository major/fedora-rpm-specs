Name:          saga
Version:       7.6.1
Release:       16%{?dist}
Summary:       Geographic information system with an API for processing geodata

# libsaga_api is licensed under the terms of LGPLv2. So is one single
# module and some of the code to create documentation.
# The rest of the code is GPLv2, GPLv2+ or compatible (ISC, MIT/X11)
License:       GPLv2 and LGPLv2
URL:           http://www.saga-gis.org
#Source0:       https://sourceforge.net/projects/saga-gis/files/SAGA%%20-%%207/SAGA%%20-%%20%%{version}/saga-%%{version}.tar.gz
# Mailing list discussion on non-free components
# https://sourceforge.net/p/saga-gis/mailman/message/28391147/
Source0:       %{name}_%{version}-fedora.tar.gz

# Script to generate free tarball
# See comments inside
Source2:       %{name}_tarball.sh

# Use system-wide e00compr
# http://sourceforge.net/p/saga-gis/bugs/137/
Patch1:        saga_e00compr.patch

# Use system-wide polyclipping
# http://sourceforge.net/p/saga-gis/bugs/135/
Patch2:        saga_polyclipping.patch

# Fix qhull include
Patch3:        saga_qhull.patch

BuildRequires: make
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: e00compr-devel
BuildRequires: gdal-devel
BuildRequires: hdf5-devel
BuildRequires: libdxflib-devel
BuildRequires: libpq-devel
BuildRequires: jasper-devel
BuildRequires: libharu-devel
BuildRequires: libsvm-devel
BuildRequires: libtiff-devel
BuildRequires: polyclipping-devel
BuildRequires: proj-devel
BuildRequires: qhull-devel
BuildRequires: swig
BuildRequires: unixODBC-devel
#BuildRequires: vigra-devel
BuildRequires: wxGTK3-devel


%description
SAGA is a geographic information system (GIS) with a special API
for geographic data processing. This API makes it easy to implement
new algorithms. The SAGA API supports grid data, vector data, and tables. 


%package devel
Summary:        SAGA development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes the headers and development libraries for SAGA.


%prep
%autosetup -p1 -n %{name}-%{version}-fedora
# Convert to UNIX line-breaks
sed -i 's/\r//' AUTHORS

gzip -c ChangeLog > ChangeLog.gz

# Make sure no bundled libraries are used: e00compr, polyclipping and triangle (qhull)
rm -r src/tools/io/io_esri_e00/e00compr
rm -r src/saga_core/saga_api/clipper.{c,h}pp
rm -r src/tools/grid/grid_gridding/nn/triangle.*
rm -r src/tools/imagery/imagery_svm/svm/
rm -r src/tools/io/io_shapes_dxf/dxflib


%build
autoreconf -fi

# Build without non-free components
%configure \
    --with-system-svm \
    --disable-static \
    --disable-python \
    --disable-libfire \
    --disable-triangle

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|^LTCC="gcc"|LTCC="gcc -Wl,--as-needed"|' \
    -e 's|^CC="g++"|CC="g++ -Wl,--as-needed"|' \
    -i libtool

%make_build


%install
%make_install

# Drop libtool archives
find %{buildroot} -name '*.la' -delete

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.saga-gis.saga-gui.appdata.xml


%ldconfig_scriptlets


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}_cmd
%{_bindir}/%{name}_gui
%{_libdir}/%{name}/
%{_datadir}/%{name}/
# No soname versioning is yet in place and the interfaces are not stable
%{_libdir}/lib%{name}_api-%{version}.so
%{_libdir}/lib%{name}_gdi-%{version}.so
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.saga-gis.saga-gui.appdata.xml
%{_mandir}/man1/%{name}_*1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}_api.so
%{_libdir}/lib%{name}_gdi.so


%changelog
* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 7.6.1-16
- Rebuild for libsvm 3.3

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 7.6.1-14
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 7.6.1-13
- Rebuild for proj-9.0.0

* Mon Feb 07 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 7.6.1-12
- Rebuild with e00compr as a shared library

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 7.6.1-10
- Rebuild (gdal)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 7.6.1-8
- Rebuild (gdal)

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 7.6.1-7
- Rebuild (proj)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 7.6.1-6
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 13:11:53 CET 2020 Sandro Mani <manisandro@gmail.com> - 7.6.1-4
- Rebuild (proj, gdal)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 7.6.1-2
- Rebuild (gdal)

* Wed Mar 04 2020 Sandro Mani <manisandro@gmail.com> - 7.6.1-1
- Update to 7.6.1

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 2.2.7-18
- Rebuild (gdal)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.2.7-15
- rebuilt (proj)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.7-13
- Subpackage python2-saga has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Volker Fröhlich <volker27@gmx.at> - 2.2.7-10
- Remove Group keyword

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.7-9
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.7-8
- Python 2 binary package renamed to python2-saga
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 volker27@gmx.at - 2.2.7-5
- Rebuild for libhpdf

* Sat Mar 04 2017 Volker Froehlich <volker27@gmx.at> - 2.2.7-4
- Rebuild for gtk3

* Tue Feb 21 2017 Volker Froehlich <volker27@gmx.at> - 2.2.7-3
- Temporarily remove vigra support, due to build failure

* Tue Jan 31 2017 Volker Froehlich <volker27@gmx.at> - 2.2.7-2
- Rebuild for libproj

* Fri Oct 14 2016 Volker Froehlich <volker27@gmx.at> - 2.2.7-1
- New upstream release
- Add new icons to file list
- Add svm patch from Ubuntugis
- Remove references to g2clib

* Thu Oct 13 2016 Volker Froehlich <volker27@gmx.at> - 2.2.4-4
- Rebuild for polyclipping 6.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.2.4-2
- Rebuild for qhull-2015.2-1.
- Reflect qhull_a.h's location having changed.

* Sat Mar 12 2016 Volker Froehlich <volker27@gmx.at> - 2.2.4-1
- New upstream release
- Use the new build options to get rid of triangle, libfire and grib2c

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Volker Froehlich <volker27@gmx.at> - 2.2.2-1
- New upstream release

* Fri Sep 25 2015 Volker Froehlich <volker27@gmx.at> - 2.2.1-1
- New upstream release

* Sun Jul 26 2015 Volker Froehlich <volker27@gmx.at> - 2.2.0-2
- Rebuild for GDAL 2.0

* Sat Jul  4 2015 Volker Froehlich <volker27@gmx.at> - 2.2.0-1
- New upstream version

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.4-3
- Fix up removing bundled source

* Sat Mar 14 2015 Volker Froehlich <volker27@gmx.at> - 2.1.4-2
- Rebuild for Proj 4.1.9

* Fri Nov 14 2014 Volker Fröhlich <volker27@gmx.at> - 2.1.4-1
- New upstream release
- Update dxflib patch

* Fri Oct 31 2014 Volker Fröhlich <volker27@gmx.at> - 2.1.3-1
- New upstream release
- Remove ChangeLog, as it is not updated, ship README instead
- Add and validate appdata file
- Remove format patch (solved upstream)

* Wed Oct 22 2014 Volker Froehlich <volker27@gmx.at> - 2.1.2-5
- Rebuild for polyclipping 6.2.0

* Tue Oct 14 2014 Volker Fröhlich <volker27@gmx.at> - 2.1.2-4
- Adapt package to new file layout in wxGTK3 3.0.1-3 (F22)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Volker Fröhlich <volker27@gmx.at> - 2.1.2-1
- New upstream release

* Thu Feb 13 2014 Volker Fröhlich <volker27@gmx.at> - 2.1.1-1
- New upstream release
- Compress changelog file
- Adjust to using wxGTK3, thus drop propgrid dependency as it is included
- Drop outdated build options
- Adapt to polyclipping 6.1 API
- Add BR for postgresql-devel
- Drop custom desktop file and use png icon
- Remove odbc headers from devel package, as discussed with Volker Wichmann
- Add complementary requires-filtering

* Sat Jan 18 2014 Volker Fröhlich <volker27@gmx.at> - 2.0.8-14
- Use safe printing format, solve BZ #1037315 and upstream bug #163
- Add patch for vigra 1.10.0 (upstream bug #173)

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 2.0.8-13
- Rebuild for gdal 1.10.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.8-11
- Rebuild for polyclipping 5.1.6

* Mon Mar  4 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.8-10
- Rebuild for polyclipping 5.1.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.8-8
- Rebuild for polyclipping

* Wed Dec 26 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.8-7
- Rebuild for polyclipping

* Fri Nov 23 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.8-6
- Rebuild for polyclipping

* Fri Oct 19 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.8-5
- Correct isa macros
- No later versions of GPL and LGPL are allowed
- Break down licenses
- Solve the rpath issue differently
- Rename patches and change numbering

* Tue Oct  9 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.8-4
- Remove draft patch breaking the build

* Sun Oct  7 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.8-3
- Replace provides-filtering with a suitable method
- Replace dos2unix invocation with sed

* Thu Apr 12 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.8-2
- Build with system-wide wxpropgrid and polyclipping
- Correct Exec entry in the desktop file
- Update patch for e00compr

* Thu Nov 24 2011 Volker Fröhlich <volker27@gmx.at> - 2.0.8-1
- Updated for new version
- Drop obsolete patches gcc46 and python-parallel
- Correct tarball script
- Update and correct linking in g2clib patch

* Sun Oct 30 2011 Volker Fröhlich <volker27@gmx.at> - 2.0.7-3
- Delete dxflib from tarball
- Split patches for dxflib and e00compr
- Use bundled wxpropgrid for the time being
- Use system-wide e00compr

* Fri Oct 07 2011 Volker Fröhlich <volker27@gmx.at> - 2.0.7-2
- Correct g2clib patch to actually use g2clib
- Only link to libraries actually used
- Fix configure.in to really search for lodbc
- Require g2clib-static instead of -devel

* Fri Sep 09 2011 Volker Fröhlich <volker27@gmx.at> - 2.0.7-1
- Initital package
