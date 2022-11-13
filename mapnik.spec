Name:      mapnik
Version:   3.1.0
Release:   20%{?dist}
Summary:   Free Toolkit for developing mapping applications
License:   LGPL-2.1-or-later
URL:       http://mapnik.org/
Source0:   https://github.com/mapnik/mapnik/releases/download/v%{version}/mapnik-v%{version}.tar.bz2
Source1:   https://github.com/mapnik/test-data/archive/v%{version}/test-data-v%{version}.tar.gz
Source2:   https://github.com/mapnik/test-data-visual/archive/v%{version}/test-data-visual-v%{version}.tar.gz
Source3:   mapnik-data.license
Source4:   viewer.desktop
# Allow the viewer to be built against uninstalled libraries
Patch0:    mapnik-build-viewer.patch
# Build against the system version of sparsehash
Patch1:    mapnik-system-sparsehash.patch
# Allow some minor differences in the visual tests
Patch2:    mapnik-visual-compare.patch
# Patch out attempt to set rpath
Patch3:    mapnik-rpath.patch
# https://github.com/mapnik/mapnik/pull/4202
Patch4:    mapnik-proj.patch
# https://github.com/mapnik/mapnik/pull/4159
Patch5:    mapnik-scons4.patch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch: ppc ppc64 s390 s390x

Requires: dejavu-serif-fonts dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-lgc-serif-fonts dejavu-lgc-sans-fonts dejavu-lgc-sans-mono-fonts
Requires: proj

BuildRequires: libpq-devel pkgconfig
BuildRequires: gdal-devel proj-devel
BuildRequires: scons make desktop-file-utils gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: libxml2-devel boost-devel libicu-devel
BuildRequires: libtiff-devel libjpeg-devel libpng-devel libwebp-devel
BuildRequires: cairo-devel freetype-devel harfbuzz-devel
BuildRequires: sqlite-devel
BuildRequires: sparsehash-devel
BuildRequires: mapbox-variant-devel mapbox-variant-static
BuildRequires: dejavu-sans-fonts
BuildRequires: postgresql-test-rpm-macros postgis

# Bundled version has many local patches and upstream is essentially dead
Provides: bundled(agg) = 2.4

# Bundles a couple of files from the unreleased "toolbox" extension
# of the boost GIL library. Attempts are being made to establish the
# status of these files (https://svn.boost.org/trac/boost/ticket/11819)
# in the hope of unbundling them
Provides: bundled(boost)

%global __provides_exclude_from ^%{_libdir}/%{name}/input/.*$

%description
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org 


%package devel
Summary: Mapnik is a Free toolkit for developing mapping applications
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: proj-devel libxml2-devel
Requires: boost-devel libicu-devel
Requires: libtiff-devel libjpeg-devel libpng-devel libwebp-devel
Requires: cairo-devel freetype-devel harfbuzz-devel
Requires: sparsehash-devel
Requires: mapbox-variant-devel

%description devel
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org


%package static
Summary: Static libraries for the Mapnik spatial visualization library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
Static libraries for the Mapnik spatial visualization library.


%package utils
License:  GPLv2+
Summary:  Utilities distributed with the Mapnik spatial visualization library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Miscellaneous utilities distributed with the Mapnik spatial visualization
library.


%package demo
Summary:  Demo utility and some sample data distributed with mapnik
License:  GPLv2+ and GeoGratis
Requires: %{name}-devel = %{version}-%{release}
Requires: python3-%{name}

%description demo
Demo application and sample vector datas distributed with the Mapnik
spatial visualization library.


%prep
%setup -q -n mapnik-v%{version} -a 1 -a 2
%autopatch -p1
rm -rf test/data test/data-visual
mv test-data-%{version} test/data
mv test-data-visual-%{version} test/data-visual
iconv -f iso8859-1 -t utf-8 demo/data/COPYRIGHT.txt > COPYRIGHT.conv && mv -f COPYRIGHT.conv demo/data/COPYRIGHT.txt
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' demo/python/rundemo.py
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' demo/simple-renderer/render.py
sed -i -e 's|+init=||' test/data/*_maps/*.xml
sed -i -e 's|+init=||' test/data-visual/styles/*.xml
rm -rf deps/mapnik/sparsehash deps/mapbox/variant


%build

# start with default compiler flags
local_optflags="%{optflags}"

# configure mapnik
PROJ_LIB=%{_datadir}/proj \
GDAL_DATA=$(gdal-config --datadir) \
scons configure FAST=True \
                DESTDIR=%{buildroot} \
                PREFIX=%{_prefix} \
                FULL_LIB_PATH=False \
                SYSTEM_FONTS=%{_datadir}/fonts \
                LIBDIR_SCHEMA=%{_lib} \
                CUSTOM_CFLAGS="${local_optflags}" \
                CUSTOM_CXXFLAGS="${local_optflags}" \
                OPTIMIZATION=2 \
                SVG2PNG=True \
                DEMO=False \
                XMLPARSER=libxml2 \
                INPUT_PLUGINS=csv,gdal,geojson,ogr,pgraster,postgis,raster,shape,sqlite,topojson

# build mapnik
scons

# build mapnik viewer app
pushd demo/viewer
  %qmake_qt5 viewer.pro
  %make_build
popd


%install

# install mapnik
scons install

# get rid of fonts use external instead
rm -rf %{buildroot}%{_libdir}/%{name}/fonts

# install more utils
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 demo/viewer/viewer %{buildroot}%{_bindir}/
install -p -m 644 %{SOURCE3} demo/data/

# install pkgconfig file
cat > %{name}.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -lmapnik
Cflags: -I\${includedir}/%{name}
EOF

mkdir -p %{buildroot}%{_datadir}/pkgconfig
install -p -m 644 %{name}.pc %{buildroot}%{_datadir}/pkgconfig

# install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}


%check

# create and start a postgres instance
PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
createdb template_postgis
psql -c "CREATE EXTENSION postgis" template_postgis

# run tests
LANG="C.UTF-8" make test


%files
%doc AUTHORS.md CHANGELOG.md README.md
%license COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/input
%{_libdir}/%{name}/input/*.input
%{_libdir}/lib%{name}*.so.*


%files devel
%doc docs/
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/lib%{name}*.so
%{_datadir}/pkgconfig/%{name}.pc
%{_bindir}/mapnik-config


%files static
%{_libdir}/lib%{name}*.a


%files utils
%{_bindir}/mapnik-index
%{_bindir}/mapnik-render
%{_bindir}/shapeindex
%{_bindir}/svg2png
%{_bindir}/viewer
%{_datadir}/applications/viewer.desktop


%files demo
%doc demo/c++
%doc demo/data
%doc demo/python
%doc demo/simple-renderer
%license demo/data/mapnik-data.license


%changelog
* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.1.0-20
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 3.1.0-18
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.1.0-17
- Rebuilt for Boost 1.78

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 3.1.0-16
- Rebuild for proj-9.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 3.1.0-14
- Rebuild (gdal)

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-13
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 3.1.0-11
- Rebuild for ICU 69

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 3.1.0-10
- Rebuild (gdal)

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-9
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Mar 24 2021 Tom Hughes <tom@compton.nu> - 3.1.0-8
- Update proj API patch with latest upstream changes

* Thu Mar 18 2021 Tom Hughes <tom@compton.nu> - 3.1.0-7
- Update proj API patch with latest upstream changes

* Tue Mar  9 2021 Tom Hughes <tom@compton.nu> - 3.1.0-6
- Update proj API patch with latest upstream changes

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 3.1.0-5
- Rebuild (proj)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 3.1.0-4
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-2
- Rebuilt for Boost 1.75

* Fri Jan  8 2021 Tom Hughes <tom@compton.nu> - 3.1.0-1
- Update to 3.1.0 upstream release

* Tue Jan  5 2021 Tom Hughes <tom@compton.nu> - 3.0.24-1
- Update to 3.0.24 upstream release

* Fri Nov  6 22:44:58 CET 2020 Sandro Mani <manisandro@gmail.com> - 3.0.23-7
- Rebuild (proj, gdal)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Tom Hughes <tom@compton.nu> - 3.0.23-5
- Add patch for boost 1.73 support

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.0.23-4
- Rebuild (gdal)

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 3.0.23-3
- Rebuild for ICU 67

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.0.23-2
- Rebuild (gdal)

* Mon Mar  2 2020 Tom Hughes <tom@compton.nu> - 3.0.23-1
- Update to 3.0.23 upstream release

* Fri Jan 31 2020 Tom Hughes <tom@compton.nu> - 3.0.22-8
- Enable use of legacy proj API
- Drop proj-epsg requires

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Tom Hughes <tom@compton.nu> - 3.0.22-5
- Workaround build breaking change in scons 3.0.5

* Tue Feb  5 2019 Tom Hughes <tom@compton.nu> - 3.0.22-4
- Rebuilt for proj 5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.0.22-2
- Rebuilt for Boost 1.69

* Tue Jan 22 2019 Tom Hughes <tom@compton.nu> - 3.0.22-1
- Update to 3.0.22 upstream release

* Tue Nov  6 2018 Tom Hughes <tom@compton.nu> - 3.0.21-2
- Replace en_US.UTF-8 with C.UTF-8

* Mon Oct  8 2018 Tom Hughes <tom@compton.nu> - 3.0.21-1
- Update to 3.0.21 upstream release

* Mon Aug 27 2018 Tom Hughes <tom@compton.nu> - 3.0.20-6
- Rebuild for GDAL 2.3
- Use new postgres test macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.0.20-4
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.0.20-3
- Rebuild for ICU 61.1

* Sun Apr 15 2018 Tom Hughes <tom@compton.nu> - 3.0.20-1
- Update to 3.0.20 upstream release

* Tue Mar  6 2018 Tom Hughes <tom@compton.nu> - 3.0.19-1
- Update to 3.0.19 upstream release

* Mon Feb 26 2018 Tom Hughes <tom@compton.nu> - 3.0.18-5
- Re-enable tree-vrp optimisation

* Tue Feb 13 2018 Tom Hughes <tom@compton.nu> - 3.0.18-4
- Define PROJ_LIB and GDAL_DATA
- Disable tree-vrp optimisation

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Tom Hughes <tom@compton.nu> - 3.0.18-2
- Drop ldconfig scriptlets

* Sat Jan 27 2018 Tom Hughes <tom@compton.nu> - 3.0.18-1
- Update to 3.0.18 upstream release

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.0.17-3
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.0.17-2
- Rebuild for ICU 60.1

* Thu Nov 30 2017 Tom Hughes <tom@compton.nu> - 3.0.17-1
- Update to 3.0.17 upstream release

* Mon Nov 20 2017 Tom Hughes <tom@compton.nu> - 3.0.16-2
- Drop libagg require from pkgconfig file

* Mon Nov 20 2017 Tom Hughes <tom@compton.nu> - 3.0.16-1
- Update to 3.0.16 upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.0.15-2
- Rebuilt for Boost 1.64

* Fri Jun 16 2017 Tom Hughes <tom@compton.nu> - 3.0.15-1
- Update to 3.0.15 upstream release

* Wed Jun 14 2017 Tom Hughes <tom@compton.nu> - 3.0.14-1
- Update to 3.0.14 upstream release

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May  4 2017 Tom Hughes <tom@compton.nu> - 3.0.13-5
- Require mapbox-variant-devel

* Thu May  4 2017 Tom Hughes <tom@compton.nu> - 3.0.13-4
- Rebuild for ARM ABI fix
- Unbundle mapbox-variant

* Sat Apr  8 2017 Tom Hughes <tom@compton.nu> - 3.0.13-3
- Revert to default compiler flags on armv7hl

* Wed Feb 15 2017 Tom Hughes <tom@compton.nu> - 3.0.13-2
- Disable problematic optimisation on armv7hl

* Tue Feb 14 2017 Tom Hughes <tom@compton.nu> - 3.0.13-1
- Update to 3.0.13 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 3.0.12-5
- Rebuild (libwebp)

* Wed Jan 25 2017 Tom Hughes <tom@compton.nu> - 3.0.12-4
- Rebuild for proj 4.9.3

* Thu Nov 17 2016 Tom Hughes <tom@compton.nu> - 3.0.12-3
- Add patch for postgis 2.3 support

* Tue Nov 15 2016 Tom Hughes <tom@compton.nu> - 3.0.12-2
- Exclude big endian architectures as mapnik does not support them
- Reduce debugging on 32 bit mips platforms to save memory

* Thu Sep  8 2016 Tom Hughes <tom@compton.nu> - 3.0.12-1
- Update to 3.0.12 upstream release

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 3.0.10-4
- Rebuilt for linker errors in boost (#1331983)

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.0.10-3
- rebuild for ICU 57.1

* Thu Apr  7 2016 Tom Hughes <tom@compton.nu> - 3.0.10-2
- Add patch for regression round-tripping empty strings
- Require libxml2-devel from mapnik-devel

* Wed Mar  2 2016 Tom Hughes <tom@compton.nu> - 3.0.10-1
- Add upstream patch to reduce compile time memory usage
- Re-enable debugging on x86 and arm

* Sat Feb 27 2016 Tom Hughes <tom@compton.nu> - 3.0.10-1
- Update to 3.0.10 upstream release

* Sat Feb 13 2016 Tom Hughes <tom@compton.nu> - 3.0.9-13
- Build with -ffloat-store on x86

* Tue Feb  2 2016 Tom Hughes <tom@compton.nu> - 3.0.9-12
- Disable debugging on x86 and arm to stop koji running out of memory

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.0.9-12
- Use %%qmake_qt4 macro to ensure proper build flags

* Sat Jan 30 2016 Tom Hughes <tom@compton.nu> - 3.0.9-11
- Rebuild with correct compiler flags

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 3.0.9-10
- Rebuild for gcc 6

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 3.0.9-9
- Remove %%defattr and fix various rpmlint issues

* Fri Jan 22 2016 Tom Hughes <tom@compton.nu> - 3.0.9-8
- Rebuild for boost 1.60.0

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.0.9-7
- Rebuilt for libwebp soname bump

* Fri Dec 11 2015 Tom Hughes <tom@compton.nu> - 3.0.9-6
- Remove version from python-mapnik dependency

* Thu Dec 10 2015 Tom Hughes <tom@compton.nu> - 3.0.9-5
- Don't do parallel builds as it uses too much memory on ARM builders
- Correct mapnik-python require

* Sun Dec  6 2015 Tom Hughes <tom@compton.nu> - 3.0.9-4
- Allow minor image differences

* Mon Nov 30 2015 Tom Hughes <tom@compton.nu> - 3.0.9-3
- Build with libxml2 as the XML parser so entities work

* Fri Nov 27 2015 Tom Hughes <tom@compton.nu> - 3.0.9-2
- Provide a postgres instance for the tests

* Fri Nov 27 2015 Tom Hughes <tom@compton.nu> - 3.0.9-1
- Update to 3.0.9 upstream release

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 3.0.8-4
- Update various dependencies

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 3.0.8-3
- Add patch to fix infinite loop in shapeindex

* Sun Nov 22 2015 Tom Hughes <tom@compton.nu> - 3.0.8-2
- Install bundled agg headers
- Package static libraries in a subpackage
- Disable all visual tests on non x86_64 machines

* Sun Nov 22 2015 Tom Hughes <tom@compton.nu> - 3.0.8-1
- Update to 3.0.8 upstream release
- Drop mapnik-python subpackage
- Enable geojson, pgraster and topojson input plugins
- Disable osm plugin

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.2.1-0.11.20150127git0639d54
- rebuild for ICU 56.1

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.2.1-0.10.20150127git0639d54
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.9.20150127git0639d54
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Mon Jul 27 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.8.20150127git0639d54
- Rebuild for boost 1.58.0

* Mon Jul 27 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.7.20150127git0639d54
- Rebuild for gdal 2.0.0

* Fri Jul 24 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.6.20150127git0639d54
- Rebuild for boost 1.58.0

* Sat Jul 18 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.5.20150127git0639d54
- Rebuild for boost 1.58.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.4.20150127git0639d54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.3.20150127git0639d54
- Rebuild for C++ ABI change

* Thu Mar 12 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.2.20150127git0639d54
- Rebuild for libproj soname change

* Tue Jan 27 2015 Tom Hughes <tom@compton.nu> - 2.2.1-0.1.20150127git0639d54
- Update to 2.2.1 prerelease snapshot for boost 1.57 support

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 2.2.0-14
- Rebuild for boost 1.57.0

* Wed Oct 22 2014 Tom Hughes <tom@compton.nu> - 2.2.0-13
- Rebuild for polyclipping 6.2.0

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.2.0-12
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.2.0-9
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2.2.0-8
- rebuild for boost 1.55.0

* Fri Mar  7 2014 Tom Hughes <tom@compton.nu> - 2.2.0-7
- Rebuild for polyclipping 6.1.3a

* Thu Feb 13 2014 Tom Hughes <tom@compton.nu> - 2.2.0-6
- Rebuild for icu 52.1

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-5
- Rebuild for gdal 1.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 2.2.0-3
- Rebuild for boost 1.54.0

* Thu Jun 27 2013 Tom Hughes <tom@compton.nu> - 2.2.0-2
- Get the tests running properly
- Enable osm input plugin
- Compile with correct optimisation flags

* Wed Jun  5 2013 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Sun May 19 2013 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release
- BuildRequire libcurl-devel for the osm plugin
- Filter out provides from the plugins

* Fri May 17 2013 Tom Hughes <tom@compton.nu> - 2.0.0-14
- Rebuild for libpng 1.6.2

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.0-13
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.0.0-12
- Rebuild for Boost-1.53.0

* Sun Feb 03 2013 Kevin Fenzi <kevin@scrye.com> - 2.0.0-11
- Rebuild for broken deps in rawhide

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.0.0-10
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 02 2013 Dan Horák <dan[at]danny.cz> - 2.0.0-9
- fix build on big-endian arches and additional 64-bit arches

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.0.0-8
- rebuild against new libjpeg

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 2.0.0-7
- Rebuild for new boost

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Caolán McNamara <caolanm@redhat.com> - 2.0.0-5
- Rebuild for new icu soname bump

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.0-2
- Add proj-devel to devel package requires
- Drop ancient fedora 11 conditionals

* Tue Nov 22 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0.0-1
- Update to upstream 2.0.0
- Namespace is "mapnik2".
- Add some new binaries to main package and python subpackage
- Add Requires for proj-epsg (#689201) so that tile rendering
  for OSM works out of the box
- Drop old patches

* Tue Nov 22 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.7.1-12
- Rebuild for new boost.

* Mon Oct 17 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.7.1-11
- Rebuild for new icu soname bump

* Thu Jul 21 2011 Kevin Fenzi <kevin@scrye.com> - 0.7.1-10
- Rebuilt for boost 1.47.0 soname bump

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 0.7.1-9
- Rebuilt for boost 1.46.1 soname bump

* Wed Feb  9 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.7.1-8
- Backport and modify upstream changeset to build against newer boost (1.46)
- Also modify demo/viewer patch accordingly

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 28 2010 Bill Nottingham <notting@redhat.com> - 0.7.1-6
- Rebuilt for boost 1.44, again

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 0.7.1-5
- Rebuilt for boost 1.44

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul  3 2010 Christopher Brown <snecklifter@gmail.com> - 0.7.1-3
- Update to 0.7.1

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.7.0-3
- rebuild for icu 4.4

* Sat Feb 20 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.7.0-2
- Add patch to fix implicit linking fixes FTBFS #564720
  (http://fedoraproject.org/wiki/Features/ChangeInImplicitDSOLinking)

* Sun Jan 24 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.7.0-1
- Update to 0.7.0
- Rebase mapnik-build-viewer patch against 0.7.0
- aggdepends patch no longer seems necessary

* Sat Jan 16 2010 Stepan Kasal <skasal@redhat.com> - 0.6.1-5
- rebuild against new boost

* Sun Nov 29 2009 Christopher Brown <snecklifter@gmail.com> - 0.6.1-4
- Add gcc-c++ BuildRequires and bump to build again

* Sat Sep 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.1-3
- fix mapnik to properly link to libagg (caolanm)
- fix pkgconfig file (caolanm)

* Fri Aug  7 2009 Christopher Brown <snecker[AT]fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Add mapnik-build-viewer.patch
- Drop use-system-fonts.patch as scons provides this
- Drop mapnik-0.5.2-gcc44.patch as the code is now good for gcc44

* Sat Jun 20 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.5.2-0.13.svn780
- Require individual dejavu font packages

* Tue Mar 24 2009 Alex Lancaster <alexlan[AT] fedoraproject org> - 0.5.2-0.12.svn780
- Add patch for compiling against GCC 4.4
- Fix file list for Python
- Fix font Requires: dejavu-fonts-compat and macro

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-0.11.svn780
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 03 2009 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.10.svn780
- fix > fc11 fonts requirement
- new CVS

* Sun Dec 07 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.9.svn738
- fix fonts for F11

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.2-0.8.svn738
- Rebuild for Python 2.6

* Thu Oct 09 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.7.svn738
- require desktop-utils in koji

* Wed Oct 08 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.6.svn738
- fix self dependency build for viewer

* Wed Oct 08 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.5.svn738
- enable viewer application for mapnik's xml templates
- exclude viewer from demo than

* Wed Sep 24 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.4.svn738
- use relative path in a demo file
- enable mapnik.pc

* Fri Sep 12 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.3.svn738
- enable libicu wrap

* Fri Sep 12 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.2.svn738
- fix koji build
- disable smp build with upstream scons

* Thu Sep 11 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.2-0.1.svn738
- new cvs snapshot, x86_64 should work for now
- new cairo dep added

* Mon Aug 25 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.1-4
- License of demo is GPLv2+ GeoGratis

* Fri Jul 25 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.1-3
- fix perms in -demo
- fix demo folder ownership

* Wed Jul 23 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.1-2
- new demo subpackage
- demo and python subpackages have GPLv2+ license
- fix dependency for python ogc server
- *.input plugins will stay in _libdir instead
- fix linkage over plugins

* Sun Jul 06 2008 Balint Cristian <rezso@rdsor.ro> - 0.5.1-1
- the license of mapnik is LGPLv2+
- release is now 0.5.1 from upstream stable
- fix explicit library dependency requirement
- fix library dependency for -devel requirement
- fix library dependency for -python requirement
- fix to use fedora specific compile flag
- fix to use external agg-devel library as shared
- make sure get rid of internal tinyxml and agg chunks
- use libxml2 by default instead of tinyxml
- use macros everywhere in specfile
- use external fedora dejavu fonts insted, get rid of local one
- place tool binaries in _bindir
- add check section and run testsuite, they should pass
- add one python tool
- build and add doxygen docs
- fix multilib issue
- fix UTF-8 and some spurious permission
- include local copied web license of some demo data
- rpmlint should print zarro bugs
