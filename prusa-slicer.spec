# Currently all of the test suite requires the old Perl infrastructure to run.
# When building flatpak, tests have to be disabled by default due to some missing dependencies.
%if 0%{?flatpak}
%bcond_with perltests
%else
%bcond_without perltests
%endif

Name:           prusa-slicer
Version:        2.4.2
Release:        2%{?dist}
Summary:        3D printing slicer optimized for Prusa printers

# The main PrusaSlicer code and resources are AGPLv3, with small parts as
# Boost.  but it includes some bundled libraries under varying licenses which
# are statically linked into the main executable.  The full list would be:
# "AGPLv3 and CC-BY and GPLv2+ and (Copyright only or BSD) and Boost and
# MPLv2.0 and MIT and Unlicense and zlib and Qhull" (with Unlicense removed in
# F31) but the AGPLv3 dominates in the final executable.
# Technically the appdata.xml file is 0BSD but it seems quite pointless to list
# that here.
License:        AGPLv3
URL:            https://github.com/prusa3d/PrusaSlicer/
Source0:        https://github.com/prusa3d/PrusaSlicer/archive/version_%version.tar.gz
Source2:        %name.appdata.xml

Patch1:         prusa-slicer-no-cereal-lib.patch

# Beware!
# Patches >= 340 are only applied on Fedora 34+
# Patches >= 350 are only applied on Fedora 35+
# ...

# OpenEXR 3 fixes
Patch351:       https://github.com/archlinux/svntogit-community/blob/1dea61c0b5/trunk/prusa-slicer-openexr3.patch

# Highly-parallel uild can run out of memory on PPC64le
%ifarch ppc64le
%global _smp_ncpus_max 8
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cereal-devel
BuildRequires:  CGAL-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-devel
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glew-devel
BuildRequires:  gtest-devel
BuildRequires:  ilmbase-devel
BuildRequires:  ImageMagick
BuildRequires:  libgudev
# Upstream miniz is no longer compatible, gotta use the fork.
# BuildRequires:  miniz-devel
BuildRequires:  NLopt-devel
BuildRequires:  openvdb
BuildRequires:  openvdb-devel
BuildRequires:  systemd-devel
BuildRequires:  tbb-devel
BuildRequires:  wxGTK-devel

# Things we wish we could unbundle
#BuildRequires:  admesh-devel >= 0.98.1
#BuildRequires:  polyclipping-devel >= 6.2.0
#BuildRequires:  boost-nowide-devel
#BuildRequires:  qhull-devel

# For the %%_udevrulesdir macro
BuildRequires:  systemd

%if %{with perltests}
# All of the old Perl dependencies needed to run the test suite
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(ExtUtils::Typemaps::Basic)
BuildRequires:  perl(ExtUtils::XSpp)
BuildRequires:  perl(ExtUtils::XSpp::Cmd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(Module::Build::WithXSpp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Wx)
%endif

Requires:       hicolor-icon-theme

# === Bundled libraries ===
# Many are described here:
# https://github.com/prusa3d/PrusaSlicer/blob/master/doc/Dependencies.md

# Note that the developers have performed the worst sort of bundling: they are
# often using random portions of other projects, without keeping documentation
# or license files, and adding their own build system.  It can be very
# difficult to tell what versions have been bundled or even where they came
# from.

# Upstream has custom patches, reluctant to send to upstream
# License: GPLv2+
# Upstream: http://github.com/admesh/admesh/
Provides: bundled(admesh-libs) = 0.98.1

# This is a header-only library, not packaged in Fedora
# License: Copyright only or BSD
# Upstream: http://antigrain.com
Provides: bundled(agg) = 2.4

# Patched to fix a bug in some Prusa hardware
# License: GPLv2+
# Upstream: http://www.nongnu.org/avrdude
Provides: bundled(avrdude) = 6.3

# This could be unbundled, but the Fedora package is broken....
# This is a version from 2017, seemingly the last commit available.
# Fedora bug: https://bugzilla.redhat.com/show_bug.cgi?id=1712550
# License: Boost
# Upstream: https://github.com/artyom-beilis/nowide
Provides: bundled(boost-nowide)

# Not packaged in Fedora, but could be.
# License: MIT
# Upstream: https://github.com/ocornut/imgui
Provides: bundled(imgui) = 1.66

# Some old code extracted from mesa libGLU that was last changed upstream in
# 2010 and last substantially changed before things were imported to git.
# The files are in src/glu-libtess.
# License: MIT
Provides: bundled(mesa-libGLU)

# PrusaResearch added functions to the upstream miniz. Yay.
# See https://github.com/prusa3d/PrusaSlicer/issues/7080
# License: MIT
Provides: bundled(miniz) = 2.1.0prusa

# A header-only library, developed by one of the authors of PrusaSlicer.
# Packaged in Fedora, but have not yet attempted unbundling.
# None of the source files carry licensing information, but a file LICENSE.txt
# exists and contains the AGPL text.
# License: AGPLv3
# Upstream: https://github.com/tamasmeszaros/libnest2d
Provides: bundled(libnest2d) = 0.3.2

# A tiny header-only library, not packaged in Fedora (but could be, though
# there is little point).  The filees appear to include commits up to and
# including one made on 2018-12-14 (c1f6e20) but nothing after.
# License: zlib
# Upstream: https://github.com/memononen/nanosvg
Provides: bundled(nanosvg)

# Two files from an old version of the Clipper/polyclipping library are used,
# but have been modified to add dependencies on other pieces of PrusaSlicer and
# to other bundled libraries.  The library is packaged in Fedora but that
# version is not usable.  (The bundled files are in src/clipper.)
# License: Boost
# Upstream: https://sourceforge.net/projects/polyclipping
Provides: bundled(polyclipping) = 6.2.9

# A tiny library, not packaged in Fedora (but could be).  Supposedly this is a
# candidate for removal but is still required for compilation.
# License: MIT
# Upstream: https://github.com/ivanfratric/polypartition
Provides: bundled(polypartition)

# It looks like we could unbundle this, but the Fedora package is old and
# doesn't appear to be suitable.  There is one change from upstream: in
# lib
# this, the compilation will fail as the slicer code expects floats while qhull
# uses doubles.
# License: Qhull
# Upstream: http://www.qhull.org
Provides: bundled(qhull) = 2016.01

# Is intended to be embedded (or installed into a source tree using clib).
# Could technically be packaged in Fedora but isn't currently.
# License: MIT
# Upstream: https://github.com/h2non/semver.c
Provides: bundled(semver) = 1.0.0

# Not packaged in Fedora; this is different from the existing "shiny" package.
# Upstream seems dead or idle as well.  To top it all off, the files have been
# reorganized from the upstream version.  Could technically be packaged, but
# PrusaSlicer would probably need patches to use it.
# License: MIT
# Upstream: https://sourceforge.net/projects/shinyprofiler/
Provides: bundled(shinyprofiler) = 2.6~rc1

# In case someone tries to install the upstream name
Provides: PrusaSlicer = %version-%release

# The package was renamed after version 2
Obsoletes: slic3r-prusa3d < 1.41.3-2
Provides: slic3r-prusa3d = %version-%release

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

# i686 arm build fails with lto
%ifarch %ix86 %arm
%define _lto_cflags %{nil}
%endif

%description
PrusaSlicer takes 3D models (STL, OBJ, AMF) and converts them into G-code
instructions for FFF printers or PNG layers for mSLA 3D printers. It's
compatible with any modern printer based on the RepRap toolchain, including all
those based on the Marlin, Prusa, Sprinter and Repetier firmware. It also works
with Mach3, LinuxCNC and Machinekit controllers.

PrusaSlicer is based on Slic3r by Alessandro Ranelucci and the RepRap
community.


%prep
%autosetup -S git -n PrusaSlicer-version_%version -N
# Apply patches, but only apply 340+ on Fedora 34, 350+ on Fedora 35, etc...
%autopatch -M %[%{?fedora} * 10 + 9]

commit () { git commit -q -a -m "$1" --author "%{__scm_author}"; }

# Fix the "UNKNOWN" in the displayed version string
sed -i 's/UNKNOWN/Fedora/' version.inc
commit "Fix version string"

# Copy out specific license files so we can reference them later.
license () { mv src/$1/$2 $2-$1; git add $2-$1; echo %%license $2-$1 >> license-files; }
license agg copying
license avrdude COPYING
license imgui LICENSE.txt
license libnest2d LICENSE.txt
license qhull COPYING.txt
commit "Move license files"

# Delete a stray font file
rm -rf resources/fonts
commit "Remove stray font file"

# Unbundle libraries
unbundle () {
    rm -rf src/$1
    sed -i "/add_subdirectory($1)/d" src/CMakeLists.txt
    commit "Unbundle $1"
}

unbundle eigen
unbundle expat
unbundle glew

# These tests were fixed but the fixes were undone upsteam with commit ac6969c
# https://github.com/prusa3d/PrusaSlicer/issues/2288
# Just remove them for now
rm -f t/combineinfill.t t/custom_gcode.t t/fill.t t/multi.t t/retraction.t t/skirt_brim.t
commit "Remove xfail tests."

# compiling test_voronoi.cpp seems to hang...
# Fixed with binutils-2.38-6.fc37 (bug 2059646)
%if 0%{?fedora} < 37
sed -i tests/libslic3r/CMakeLists.txt -e '\@test_voronoi.cpp@d'
commit "Disable voronoi test"
%endif


%build
# -DSLIC3R_PCH=0 - Disable precompiled headers, which break cmake for some reason
# -DSLIC3R_FHS=1 - Enable FHS layout instead of installing things into the resources directory
# -DSLIC3R_WX_STABLE=1 - Allow use of wxGTK version 3.0 instead of 3.1.
%cmake -DSLIC3R_PCH=0 -DSLIC3R_FHS=1 -DSLIC3R_WX_STABLE=1 -DSLIC3R_GTK=3 \
    -DSLIC3R_BUILD_TESTS=1 -DCMAKE_BUILD_TYPE=Release \
%if %{with perltests}
    -DSLIC3R_PERL_XS=1
%endif

%cmake_build
# To avoid "iCCP: Not recognized known sRGB profile that has been edited"
pushd resources/icons
find . -type f -name "*.png" -exec convert {} -strip {} \;
popd


%install
%cmake_install

# Since the binary segfaults under Wayland, we have to wrap it.
mv %buildroot%_bindir/prusa-slicer %buildroot%_bindir/prusa-slicer.wrapped
cat >> %buildroot%_bindir/prusa-slicer <<'END'
#!/bin/bash
export GDK_BACKEND=x11
exec %_bindir/prusa-slicer.wrapped "$@"
END
chmod 755 %buildroot%_bindir/prusa-slicer

mkdir -p %buildroot%_datadir/appdata
install -m 644 %SOURCE2 %buildroot%_datadir/appdata/%name.appdata.xml

# For now, delete the Perl module that gets installed.  It only exists because
# we want the test suite to run.  It could be placed into a subpackage, but
# nothing needs it currently and it would conflict with the other slic3r
# package.
#
# The %%perl_vendorarch and %%perl_vendorlib can be undefined,
# which would cause deleting of the whole buildroot.
%{?perl_vendorarch:rm -rf %buildroot/%perl_vendorarch}
%{?perl_vendorlib:rm -rf %buildroot/%perl_vendorlib}

# Upstream installs the translation source files when they probably shouldn't
ls -lR %buildroot%_datadir/PrusaSlicer/localization
rm %buildroot%_datadir/PrusaSlicer/localization/{PrusaSlicer.pot,list.txt}
find %buildroot%_datadir/PrusaSlicer/localization/ -name \*.po -delete

# Handle locale files.  The find_lang macro doesn't work because it doesn't
# understand the directory structure.  This copies part of the funtionality of
# find-lang.sh by:
#   * Getting a listing of all files
#   * removing the buildroot prefix
#   * inserting the proper 'lang' tag
#   * removing everything that doesn't have a lang tag
#   * A list of lang-specific directories is also added
# The resulting file is included in the files list, where we must be careful to
# exclude that directory.
find %buildroot%_datadir/PrusaSlicer/localization -type f -o -type l | sed '
    s:'"%buildroot"'::
    s:\(.*/PrusaSlicer/localization/\)\([^/_]\+\)\(.*\.mo$\):%%lang(\2) \1\2\3:
    s:^\([^%].*\)::
    s:%lang(C) ::
    /^$/d
' > lang-files

find %buildroot%_datadir/PrusaSlicer/localization -type d | sed '
    s:'"%buildroot"'::
    s:\(.*\):%dir \1:
' >> lang-files

%if 0%{?flatpak}
# Remove udev rules that aren't needed for flatpak builds
rm -f %buildroot%_prefix/lib/udev/rules.d/90-3dconnexion.rules
%endif

%check
desktop-file-validate %buildroot%_datadir/applications/PrusaGcodeviewer.desktop

# Some tests are Perl but there is a framework for other tests even though
# currently the only thing that uses them is one of the bundled libraries.
# There's no reason not to run as much as we can.
%cmake_build -- test ARGS=-V


%files -f license-files -f lang-files
%license LICENSE
%doc README.md
%_bindir/%name
%_bindir/prusa-gcodeviewer
%_bindir/%name.wrapped
%_datadir/icons/hicolor/*/apps/PrusaSlicer*.png
%_datadir/applications/PrusaGcodeviewer.desktop
%_datadir/applications/PrusaSlicer.desktop
%_datadir/appdata/%name.appdata.xml
%dir %_datadir/PrusaSlicer
%_datadir/PrusaSlicer/{icons,models,profiles,shaders,shapes,udev,applications,data}/
%if !0%{?flatpak}
%_udevrulesdir/90-3dconnexion.rules
%endif

%changelog
* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.4.2-2
- Rebuild with wxWidgets 3.2

* Fri Jul 22 2022 Jan Staněk <jstanek@redhat.com> - 2.4.2-1
- Update to 2.4.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-5
- Rebuilt for openvdb 9.1
- Fixes: rhbz#2098784

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.4.0-4
- Rebuilt for Boost 1.78

* Thu Mar 17 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.0-3
- Remove the previous voronoi workaround for fixed binutils

* Wed Mar  2 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.0-2
- %%ix86 %%arm: kill LTO for now
- kill test_voronoi.cpp, compilation (as) hangs (bug 2059646)

* Mon Feb 14 2022 Tom Callaway <spot@fedoraproject.org> - 2.4.0-1
- update to 2.4.0

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2.3.3-5
- Rebuild for glew 2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Miro Hrončok <mhroncok@redhat.com> - 2.3.3-3
- Disable GLIBCXX_ASSERTIONS
- Fixes rhbz#2023345

* Sun Nov 28 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.3-2
- Rebuild for OpenVDB 9.

* Mon Nov 08 2021 Dennis Gilmore <dennis@ausil.us> - 2.3.3-1
- update to 2.3.3
- remove upstreamed gcc patch

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 2.3.1-5
- Rebuilt for Boost 1.76

* Mon Aug 02 2021 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-4
- Rebuilt for OpenEXR 3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-2
- Rebuilt for openvdb 8.1
- Fixes rhbz#1972120

* Sat May 15 2021 Dennis Gilmore <dennis@ausil.us> - 2.3.1-1
- update to 2.3.1
- include upstream patch fixing build with gcc 11

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-12
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-10
- Rebuilt for Boost 1.75

* Thu Jan 14 2021 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-9
- Trim perl build dependencies

* Mon Jan 04 2021 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-8
- Rebuilt for openvdb 8.0
- Fixes: rhbz#1912499

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-7
- Rebuild for OpenEXR 2.5.3.

* Wed Aug 26 2020 Jan Beran <jaberan@redhat.com> - 2.2.0-6
- Add fixes for the flatpak build:
  disable perltests by default when building flatpak
  don't remove Perl modules when building without perltests

* Mon Aug 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Rebuilt for openvdb 7.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt and fix for Boost 1.73.0 (#1842011)

* Tue Mar 31 2020 Alexander Jacocks <alexander@redhat.com> - 2.2.0-1
- Update to 2.2.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.1-1
- Update to 2.1.1.

* Mon Sep 23 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0-2
- Fix the s390x build and re-enable it.

* Fri Sep 13 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0-1
- Update to 2.1.0.

* Fri Sep 06 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0~rc0-2
- Temporarily disable build on s390x because of a new bug in the code upstream:
  https://github.com/prusa3d/PrusaSlicer/issues/2879

* Wed Sep 04 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0~rc0-1
- Update to rc0.
- Drop tests which are known to fail.

* Tue Aug 13 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0~alpha1-1
- Update to the current alpha.
- Drop several upstreamed patches.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.0.0-3
- Wrap the executable to set GDK_BACKEND=x11 to avoid segfault on Wayland.

* Wed Jun 05 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.0.0-2
- Update with review feedback
- Add in three patches suggested by upstream
- Try to enable building on aarch64 and s390x

* Mon May 20 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.0.0-1
- Update to 2.0.0 final release.

* Fri Feb 15 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.41.3-1
- Update to 1.41.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.41.0-3
- Rebuilt and patched for Boost 1.69

* Sun Dec 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.41.0-2
- Set GDK_BACKEND=x11 to prevent crashes on Wayland (#1661324)

* Mon Oct  1 2018 Tom Callaway <spot@fedoraproject.org> - 1.41.0-1
- update to 1.41.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.8-11
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.8-10
- Add missing BR perl(ExtUtils::CBuilder)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.33.8-8
- Remove obsolete scriptlets
- Rebuilt for new boost

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.33.8-5
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.33.8-4
- Rebuilt for Boost 1.64

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.8-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 22 2017 Miro Hrončok <mhroncok@redhat.com> - 1.33.8-1
- Update to 1.33.8
- Mention it's a fork in the description and appdata file
- Require hicolor-icon-theme
- Exclude big endian arches

* Sat Dec 17 2016 Miro Hrončok <mhroncok@redhat.com> - 1.31.6-1
- Update to 1.31.6
- Bundle admesh
- Recommend Thread::Queue for faster slicing
- Unbundle glew

* Fri Nov 11 2016 Miro Hrončok <mhroncok@redhat.com> - 1.31.4-1
- New package adapted from the slic3r package
