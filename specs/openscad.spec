Name:           openscad
Version:        2021.01
%global upversion %{version}
Release:        %autorelease
Summary:        The Programmers Solid 3D CAD Modeller
# OpenSCAD is GPL-2.0-only WITH CGAL-linking-exception
# Appdata file is CC0-1.0
# Examples are CC0-1.0
License:        GPL-2.0-only WITH CGAL-linking-exception AND CC0-1.0
URL:            http://www.%{name}.org/
Source0:        http://files.%{name}.org/%{name}-%{upversion}.src.tar.gz
Patch0:         %{name}-polyclipping.patch

# CGAL 5.3 fixes from https://github.com/openscad/openscad/pull/3844
Patch1:         %{name}-cgal5.3.patch

# Upstream backports:
%global github  https://github.com/openscad/openscad

# https://github.com/openscad/openscad/commit/9b79576c1ee9d57d0f4a5de5c1365bb87c548f36
Patch2:         %{name}-2021.01-fix-overloaded-join.patch
# https://github.com/openscad/openscad/commit/71f2831c0484c3f35cbf44e1d1dc2c857384100b
Patch3:         %{name}-2021.01-cgal-build-fix.patch
# https://github.com/openscad/openscad/commit/770e3234cbfe66edbc0333f796b46d36a74aa652
Patch4:         CVE-2022-0496.patch
# https://github.com/openscad/openscad/commit/84addf3c1efbd51d8ff424b7da276400bbfa1a4b
Patch5:         CVE-2022-0497.patch
# https://github.com/openscad/openscad/commit/254904624763e4dd2d04ca5706af303a1f0a1777
Patch6:         %{name}-2021.01-cgal6-cpp17.patch
# https://github.com/openscad/openscad/commit/cc51ea0a0dd14075df0f9af09ed4e20cce7fcb4c
Patch7:         %{name}-boost1.90.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  bison >= 2.4
BuildRequires:  boost-devel >= 1.35
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  flex >= 2.5.35
BuildRequires:  freetype-devel >= 2.4
BuildRequires:  fontconfig-devel >= 2.10
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  harfbuzz-devel >= 0.9.19
BuildRequires:  libspnav-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  polyclipping-devel >= 6.1.3
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtgamepad-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  pkgconfig(libzip)
BuildRequires:  xwfb-run
# Both weston and mutter appear to work. We pick mutter explicitly, here and in
# the xwfb-run invocation, to accommodate different defaults in Fedora and EL.
BuildRequires:  mutter
Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationserif)
Requires:       hicolor-icon-theme
Recommends:     %{name}-MCAD = %{version}-%{release}

%bcond_without 3mf
%if %{with 3mf}
BuildRequires:  lib3mf-devel
%endif

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.


###############################################
%package        MCAD
Summary:        OpenSCAD Parametric CAD Library
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-3.0-or-later AND (GPL-3.0-only OR LGPL-2.1-only) AND (GPL-3.0-or-later OR LGPL-2.1-or-later) AND (CC-BY-SA-3.0 OR LGPL-2.0-or-later) AND CC-BY-3.0 AND BSD-2-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://www.github.com/openscad/MCAD
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

### LICENSES:

##  LGPL-2.0-or-later:
#   multiply.scad

##  LGPL-2.1-or-later:
#   2Dshapes.scad
#   3d_triangle.scad
#   gridbeam.scad
#   libtriangles.scad
#   shapes.scad
#   screw.scad
#   transformations.scad

##  LGPL-2.1-only:
#   fonts.scad
#   gears.scad
#   hardware.scad
#   involute_gears.scad
#   servos.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPL-3.0-or-later:
#   teardrop.scad

##  GPL-3.0-only OR LGPL-2.1-only:
#   motors.scad
#   nuts_and_bolts.scad


##  GPL-3.0-or-later OR LGPL-2.1-or-later:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA-3.0 OR LGPL-2.0-or-later:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   units.scad
#   utilities.scad

##  CC-BY-3.0:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

##  BSD-2-Clause:
#   boxes.scad

##  MIT:
#   constants.scad
#   curves.scad
#   math.scad

##  LicenseRef-Fedora-Public-Domain:
#   lego_compatibility.scad
#   trochoids.scad

###############################################

%prep
%autosetup -n %{name}-%{upversion} -p1 -S git

# Unbundle polyclipping
rm src/ext/polyclipping -rf

# Remove unwanted things from MCAD, such as nonworking Python tests
pushd libraries/MCAD
for FILE in *.py; do
  rm -r $FILE
done
mv bitmap/README bitmap-README
popd

# Tests cmake check for MCAD by probing libraries/MCAD/__init__.py
# But we've just removed it
sed -i 's@MCAD/__init__.py@MCAD/gears.scad@' tests/CMakeLists.txt

%build
%{qmake_qt5} PREFIX=%{_prefix} VERSION=%{upversion} CONFIG-=debug
%make_build

# tests
cd tests
cmake -DPYTHON_EXECUTABLE:STRING=%{python3} .
%make_build
cd -

%install
make install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
%find_lang %{name}

for FILE in .gitignore lgpl-2.1.txt README.markdown TODO bitmap-README; do
  rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/$FILE
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
xwfb-run -c mutter -- ctest %{?_smp_mflags} || : # let the tests fail, as they probably won't work in Koji
cd -

%files -f %{name}.lang
%license COPYING
%doc README.md RELEASE_NOTES.md
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/color-schemes/
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/libraries
%{_datadir}/%{name}/templates/
%{_mandir}/man1/*

%files MCAD
%license libraries/MCAD/lgpl-2.1.txt
%doc libraries/MCAD/README.markdown
%doc libraries/MCAD/TODO
%doc libraries/MCAD/bitmap-README
%dir %{_datadir}/%{name}/libraries/MCAD
%dir %{_datadir}/%{name}/libraries/MCAD/bitmap
%{_datadir}/%{name}/libraries/MCAD/*.scad
%{_datadir}/%{name}/libraries/MCAD/bitmap/*.scad

%changelog
%autochangelog
