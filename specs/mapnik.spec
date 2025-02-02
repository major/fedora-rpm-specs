%global testcommit fd9ab4313a9ca59a3d8dce7ede6a117b2f5475da
%global visualcommit 309738759f39c19db3f08382b270fc8c1d1dd043

Name:      mapnik
Version:   4.0.5
Release:   %autorelease
Summary:   Free Toolkit for developing mapping applications
License:   LGPL-2.1-only
URL:       http://mapnik.org/
Source0:   https://github.com/mapnik/mapnik/releases/download/v%{version}/mapnik-v%{version}.tar.bz2
Source1:   https://github.com/mapnik/test-data/archive/%{testcommit}/test-data-%{testcommit}.tar.gz
Source2:   https://github.com/mapnik/test-data-visual/archive/%{visualcommit}/test-data-visual-%{visualcommit}.tar.gz
Source3:   mapnik-data.license
Source4:   viewer.desktop
# Build against the system version of sparsehash
Patch:     mapnik-system-sparsehash.patch
# Build against the system version of catch
Patch:     mapnik-system-catch.patch
# Allow some minor differences in the visual tests
Patch:     mapnik-visual-compare.patch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch: ppc ppc64 s390 s390x

Requires: dejavu-serif-fonts dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-lgc-serif-fonts dejavu-lgc-sans-fonts dejavu-lgc-sans-mono-fonts
Requires: proj

BuildRequires: libpq-devel pkgconfig
BuildRequires: gdal-devel proj-devel
BuildRequires: cmake make desktop-file-utils gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: libxml2-devel boost-devel libicu-devel
BuildRequires: libtiff-devel libjpeg-devel libpng-devel libwebp-devel
BuildRequires: cairo-devel freetype-devel harfbuzz-devel
BuildRequires: sqlite-devel
BuildRequires: sparsehash-devel
BuildRequires: geometry-hpp-devel geometry-hpp-static
BuildRequires: polylabel-devel polylabel-static
BuildRequires: protozero-devel protozero-static
BuildRequires: mapbox-variant-devel mapbox-variant-static
BuildRequires: catch2-devel
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
Requires: geometry-hpp-devel
Requires: polylabel-devel
Requires: protozero-devel
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
License:  GPL-2.0-or-later
Summary:  Utilities distributed with the Mapnik spatial visualization library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Miscellaneous utilities distributed with the Mapnik spatial visualization
library.


%package demo
Summary:  Demo utility and some sample data distributed with mapnik
License:  GPL-2.0-or-later AND LicenseRef-GeoGratis
Requires: %{name}-devel = %{version}-%{release}
Requires: python3-%{name}

%description demo
Demo application and sample vector datas distributed with the Mapnik
spatial visualization library.


%prep
%setup -q -n mapnik-v%{version} -a 1 -a 2
%autopatch -p 1
cp -p %{SOURCE3} demo/data
rm -rf test/data test/data-visual
mv test-data-%{testcommit} test/data
mv test-data-visual-%{visualcommit} test/data-visual
find . -name '._*' -delete
iconv -f iso8859-1 -t utf-8 demo/data/COPYRIGHT.txt > COPYRIGHT.conv && mv -f COPYRIGHT.conv demo/data/COPYRIGHT.txt
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' demo/simple-renderer/render.py
sed -i -e 's|+init=||' test/data/*_maps/*.xml
sed -i -e 's|+init=||' test/data-visual/styles/*.xml
rm -rf deps/mapnik/sparsehash deps/mapbox/geometry deps/mapbox/polylabel deps/mapbox/protozero deps/mapbox/variant


%build
%cmake \
  -DUSE_EXTERNAL_MAPBOX_GEOMETRY=ON \
  -DUSE_EXTERNAL_MAPBOX_POLYLABEL=ON \
  -DUSE_EXTERNAL_MAPBOX_PROTOZERO=ON \
  -DUSE_EXTERNAL_MAPBOX_VARIANT=ON \
  -DFONTS_INSTALL_DIR=share/fonts
%cmake_build


%install
%cmake_install
rm -rf %{buildroot}/%{_bindir}/viewer.ini %{buildroot}/%{_datadir}/fonts
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}


%check
PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
createdb template_postgis
psql -c "CREATE EXTENSION postgis" template_postgis
%ctest
pushd redhat-linux-build/out
%ifarch aarch64 ppc64le
rm test/data-visual/styles/line-pattern-issue-2726.xml
%endif
./mapnik-test-visual -j %{_smp_build_ncpus} --output-dir ./visual-test-result
popd


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
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/lib%{name}*.pc


%files static
%{_libdir}/lib%{name}*.a


%files utils
%{_bindir}/geometry_to_wkb
%{_bindir}/mapnik-index
%{_bindir}/mapnik-render
%{_bindir}/mapnik-viewer
%{_bindir}/pgsql2sqlite
%{_bindir}/shapeindex
%{_bindir}/svg2png
%{_datadir}/applications/viewer.desktop


%files demo
%doc demo/c++
%doc demo/data
%doc demo/simple-renderer
%license demo/data/mapnik-data.license


%changelog
%autochangelog
