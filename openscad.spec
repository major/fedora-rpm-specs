Name:           openscad
Version:        2021.01
%global upversion %{version}
Release:        13%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:        GPLv2 with exceptions and CC0
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

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  Xvfb
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
License:        LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
URL:            https://www.github.com/openscad/MCAD
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

### LICENSES:

##  LGPLv2+:
#   2Dshapes.scad
#   3d_triangle.scad
#   fonts.scad
#   gridbeam.scad
#   hardware.scad
#   libtriangles.scad
#   multiply.scad
#   shapes.scad
#   screw.scad

##  LGPLv2:
#   gears.scad
#   involute_gears.scad
#   servos.scad
#   transformations.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPLv3+:
#   teardrop.scad

##  GPLv3 or LGPLv2:
#   motors.scad
#   nuts_and_bolts.scad


##  GPLv3+ or LGPLv2:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA or LGPLv2+:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   utilities.scad

##  CC-BY-SA or LGPLv2:
#   units.scad

##  CC-BY:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

## BSD
#   boxes.scad

## MIT
#   constants.scad
#   curves.scad
#   math.scad

## Public Domain
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
ctest %{?_smp_mflags} || : # let the tests fail, as they probably won't work in Koji
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
* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2021.01-13
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Miro Hrončok <mhroncok@redhat.com> - 2021.01-10
- Enable PDF export
- Fixes: rhbz#2101338

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2021.01-9
- Rebuilt for Boost 1.78

* Tue Apr 05 2022 Lumír Balhar <lbalhar@redhat.com> - 2021.01-8
- Security fixes for CVE-2022-0496 and CVE-2022-0497
- Fixes: rhbz#2050696 rhbz#2050700

* Fri Feb 11 2022 Tom Callaway <spot@fedoraproject.org> - 2021.01-7
- apply upstream fix for build issue with overloaded join()
- fix build against new CGAL 5.4

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2021.01-6
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 2021.01-4
- Rebuilt for Boost 1.76

* Mon Aug 02 2021 Miro Hrončok <mhroncok@redhat.com> - 2021.01-3
- Rebuilt with CGAL 5.3
- Fixes: rhbz#1987777

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Miro Hrončok <mhroncok@redhat.com> - 2021.01-1
- Update to 2021.01
- Enable 3mf support
- Fixes: rhbz#1904759

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2019.05-13
- Rebuilt for Boost 1.75

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 2019.05-11
- Rebuilt and patched for Boost 1.73.0 (#1841257)

* Tue Apr 21 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.05-10
- Fix broken build dependency on removed qt5-devel metapackage

* Sat Mar 28 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.05-9
- Rebuilt to fix a crash on startup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2019.05-7
- Rebuild for mpfr 4

* Wed Oct 02 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.05-6
- Rebuilt for CGAL becoming header only
- Add a patch to the QMake configuration, for CGAL 5.0

* Sun Sep 22 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for double-conversion 3.1.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.05-3
- Fix crash with empty imported STL/PNG (#1717625)
- Don't build in debug mode (it impacts performance)

* Thu May 23 2019 Ivan Mironov <mironov.ivan@gmail.com> - 2019.05-2
- Switch to Qt5 (this enables OctoPrint support)
- Add dependency on Qt Gamepad (enables gamepad support)

* Mon May 20 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2019.05-1
- Update to 2019.05.
- New build dependency double-conversion.

* Thu Feb 28 2019 Tom Callaway <spot@fedoraproject.org> - 2019.01~RC2-1
- 2019.01-RC2

* Sun Feb 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 2015.03.3-22
- rebuild (qscintilla)

* Tue Feb 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 2015.03.3-21
- rebuild (qscintilla)
- use %%make_build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2015.03.3-19
- Rebuilt for Boost 1.69

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2015.03.3-18
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 21 2018 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-16
- Fix SIGABRT (#1563897)

* Thu Apr 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-15
- Make sure what's shipped with MCAD, don't bring in python2 dependency
- Run the tests with python2 explicitly

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2015.03.3-13
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2015.03.3-10
- Rebuilt for Boost 1.64

* Sun Jun 04 2017 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-9
- Rebuilt for new CGAL

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2015.03.3-7
- rebuild (qscintilla)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 2015.03.3-5
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-4
- Rebuilt for new libGLEW.so.2.0

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 2015.03.3-3
- Rebuild for eigen3-3.3.1

* Wed Sep 21 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-2
- Rebuilt for new CGAL 4.9

* Sun Sep 18 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-1
- New upstream version 2015.03-3
- Recommends MCAD from the main package

* Sun Sep 18 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-9
- Rebuilt for new polyclipping (#1159525)

* Thu Sep 15 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-8
- Rebuilt for new opencsg version 1.4.1

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 2015.03.2-7
- Rebuilt for linker errors in boost (#1331983)

* Sun Apr 10 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-6
- Rebuilt with new gcc, fix FTBFS (#1305220)

* Wed Feb 03 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-5
- Rebuilt for Boost 1.60 (again?)

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 2015.03.2-4
- use %%qmake_qt4 macro

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 2015.03.2-3
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 2015.03.2-2
- Rebuild for glew 1.13

* Thu Nov 19 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-1
- New upstream version 2015.03-2

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2015.03.1-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2015.03.1-3
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03.1-1
- New upstream version 2015.03-1

* Mon Apr 20 2015 Rex Dieter <rdieter@fedoraproject.org> 2015.03-2
- rebuild (qscintilla), BR: qt4-devel

* Tue Mar 17 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03-1
- New stable version 2015.03§

* Wed Feb 25 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.02-0.2.RC3
- Rebuilt for new CGAL

* Sun Feb 22 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.02-0.1.RC3
- New RC version of 2015.02
- Build MCAD as a subpackage
- Unbundle polyclipping

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2014.03-7
- Rebuild for boost 1.57.0

* Tue Sep 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-6
- Rebuilt for OpenCSG 1.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2014.03-3
- rebuild for boost 1.55.0

* Thu May 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-2
- Rebuilt for opencsg 1.3.3

* Sun Mar 09 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-1
- New version

* Fri Dec 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-8
- Enable Xvfb tests
- Add AppData from upstream git

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2013.06-7
- rebuilt for GLEW 1.10

* Sun Nov 17 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-6
- Rebuilt for new glew

* Fri Sep 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-5
- Require Python for tests

* Fri Sep 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-4
- Patch to solve upstream bug #482

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 2013.06-2
- Rebuild for boost 1.54.0

* Wed Jun 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-1
- New upstream release
- Moved removing MCAD to %%install

* Sat Feb 23 2013 Kevin Fenzi <kevin@scrye.com> - 2013.01.17-6
- Rebuild for broken deps in rawhide

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2013.01.17-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2013.01.17-4
- Rebuild for Boost-1.53.0

* Sun Feb 03 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-3
- Added fix for issue 267

* Tue Jan 22 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-2
- Using  source tarball
- Reffer to the shorter version in the app
- Run tests
- Added patch so test will compile
* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-1
- New stable release 2013.01
- Updated to respect GitHub rule

* Tue Jan 08 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.08-1
- New version

* Sun Jan 06 2013 Miro Hrončok <miro@hroncok.cz> - 2013.01.05-1
- New version

* Thu Dec 06 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-5
- Separated MCAD

* Mon Dec 03 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-4
- Removed useless gziping

* Sun Dec 02 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-3
- Added manpage

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-2
- Commented macros in comments
- Fully versioned dependency of the main package
- added desktop-file-validate

* Wed Oct 31 2012 Miro Hrončok <miro@hroncok.cz> 2012.10.31-1
- New version
- Solved 2 MLCAD files license issues
- Using full date version

* Mon Oct 08 2012 Miro Hrončok <miro@hroncok.cz> 2012.10-1
- New version.

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 2012.08-1
- New package.
