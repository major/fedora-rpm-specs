# Currently all of the test suite requires the old Perl infrastructure to run.
# When building flatpak, tests have to be disabled by default due to some missing dependencies.
%if 0%{?flatpak}
%bcond_with perltests
%else
%bcond_without perltests
%endif

Name:           prusa-slicer
Version:        2.9.0
Release:        %autorelease
Summary:        3D printing slicer optimized for Prusa printers

# The main PrusaSlicer code and resources are AGPLv3, with small parts as
# Boost.  but it includes some bundled libraries under varying licenses which
# are statically linked into the main executable.  The full list would be:
# "AGPLv3 and CC-BY and GPLv2+ and (Copyright only or BSD) and Boost and
# MPLv2.0 and MIT and Unlicense and zlib and Qhull" (with Unlicense removed in
# F31) but the AGPLv3 dominates in the final executable.
# Technically the appdata.xml file is 0BSD but it seems quite pointless to list
# that here.
# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            https://github.com/prusa3d/PrusaSlicer/
Source0:        https://github.com/prusa3d/PrusaSlicer/archive/version_%version.tar.gz
Source2:        %name.appdata.xml
%global libbgcode_commit d33a277a3ce2c0a7f9ba325caac6d730e0f7a412
Source3:        https://github.com/prusa3d/libbgcode/archive/%{libbgcode_commit}.tar.gz#/libbgcode-%{libbgcode_commit}.tar.gz
Source4:        https://github.com/atomicobject/heatshrink/archive/refs/tags/v0.4.1.tar.gz#/heatshrink-0.4.1.tar.gz
Source5:        https://github.com/prusa3d/openvdb/archive/a68fd58d0e2b85f01adeb8b13d7555183ab10aa5.tar.gz#/openvdb-8.2.tar.gz

# Fix a couple of segfaults that happen with wxWidgets 3.2 (from Debian)
Patch5:         prusa-slicer-fix-uninitialized-imgui-segfault.patch

# https://github.com/prusa3d/PrusaSlicer/pull/13896
Patch6:		prusa-slicer-pr-13896.patch

# Beware!
# Patches >= 340 are only applied on Fedora 34+
# Patches >= 350 are only applied on Fedora 35+
# ...

# OpenEXR 3 fixes
Patch351:       https://github.com/archlinux/svntogit-community/blob/1dea61c0b5/trunk/prusa-slicer-openexr3.patch

# https://github.com/prusa3d/PrusaSlicer/pull/11769
Patch394:       prusa-slicer-pr-11769.patch
# Work with OpenCASCADE 7.8.0 which is in Fedora 41
Patch395:       prusa-slicer-opencascade.patch
# https://github.com/prusa3d/PrusaSlicer/pull/13761
Patch396:	prusa-slicer-pr-13761.patch
# https://github.com/prusa3d/PrusaSlicer/pull/13081
Patch421:       prusa-slicer-pr-13081.patch

# Highly-parallel uild can run out of memory on PPC64le
%ifarch ppc64le
%global _smp_ncpus_max 8
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

BuildRequires:  boost-devel
BuildRequires:  catch2-devel
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
BuildRequires:  nanosvg-devel
BuildRequires:  NLopt-devel
BuildRequires:  opencascade-devel
# Workaround https://bugzilla.redhat.com/show_bug.cgi?id=2301103
# BuildRequires:  openvdb
# BuildRequires:  openvdb-devel
BuildRequires:  qhull-devel
BuildRequires:  systemd-devel
BuildRequires:  tbb-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  wxGTK-devel

# Things we wish we could unbundle
#BuildRequires:  admesh-devel >= 0.98.1
#BuildRequires:  polyclipping-devel >= 6.2.0

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

# Not packaged in Fedora, but could be.
# License: MIT
# Upstream: https://github.com/ocornut/imgui
Provides: bundled(imgui) = 1.66

# Some old code extracted from mesa libGLU that was last changed upstream in
# 2010 and last substantially changed before things were imported to git.
# The files are in bundled_deps/glu-libtess.
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

# Not packaged in Fedora (but could be).
# License: AGPL-3.0-only
# Upstream: https://github.com/prusa3d/libbgcode
Provides: bundled(libbgcode)

# Not packaged in Fedora (but could be).
# License: ISC
# Upstream: https://github.com/atomicobject/heatshrink
Provides: bundled(heatshrink) = 0.4.1

# Workaround https://bugzilla.redhat.com/show_bug.cgi?id=2301103
# License: MPL 2.0
# Upstream: https://github.com/AcademySoftwareFoundation/openvdb
# Upstream: https://github.com/prusa3d/openvdb
Provides: bundled(openvdb) = 8.2.0

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

( cd bundled_deps && tar xvzf %SOURCE3 && mv libbgcode-* libbgcode )
sed -i 's#set(LibBGCode_SOURCE_DIR ""#set(LibBGCode_SOURCE_DIR "../../bundled_deps/libbgcode"#' deps/+LibBGCode/LibBGCode.cmake

( cd bundled_deps && tar xvzf %SOURCE4 && mv heatshrink-* heatshrink )
sed -i 's#URL https.*#SOURCE_DIR ../../bundled_deps/heatshrink#' deps/+heatshrink/heatshrink.cmake

( cd bundled_deps && tar xvzf %SOURCE5 && mv openvdb-* openvdb )
sed -i 's#URL https.*#SOURCE_DIR ../../bundled_deps/openvdb#; s/-DUSE_BLOSC=ON/-DUSE_BLOSC=OFF/' deps/+OpenVDB/OpenVDB.cmake

mkdir deps/ignored
mv deps/+* deps/ignored
mv deps/ignored/+LibBGCode deps/ignored/+heatshrink deps/ignored/+OpenVDB deps

# Copy out specific license files so we can reference them later.
license () { basename=$( basename $1 ) ; mv bundled_deps/$1/$2 $2-$basename; git add $2-$basename; echo %%license $2-$basename >> license-files; }
license agg/agg copying
license avrdude/avrdude COPYING
license imgui LICENSE.txt
license libnest2d LICENSE.txt
license libbgcode LICENSE
license heatshrink LICENSE
license openvdb LICENSE
git add license-files
commit "Move license files"

%build
# -DSLIC3R_PCH=0 - Disable precompiled headers, which break cmake for some reason
# -DSLIC3R_FHS=1 - Enable FHS layout instead of installing things into the resources directory
%cmake -DSLIC3R_PCH=0 -DSLIC3R_FHS=1 -DSLIC3R_GTK=3 \
    -DSLIC3R_BUILD_TESTS=1 -DCMAKE_BUILD_TYPE=Release \
    -DPrusaSlicer_BUILD_DEPS:BOOL=ON \
    -DOPENVDB_USE_STATIC_LIBS=1 \
    -DCMAKE_EXE_LINKER_FLAGS=-lcrypto \
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

# Delete font files that are only needed for tests
rm -rf %buildroot%_datadir/PrusaSlicer/fonts

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
%_libdir/OCCTWrapper.so
%_datadir/icons/hicolor/*/apps/PrusaSlicer*.png
%_datadir/applications/PrusaGcodeviewer.desktop
%_datadir/applications/PrusaSlicer.desktop
%_datadir/appdata/%name.appdata.xml
%dir %_datadir/PrusaSlicer
%_datadir/PrusaSlicer/{icons,models,profiles,shaders,shapes,udev,applications,data,web}/
%if !0%{?flatpak}
%_udevrulesdir/90-3dconnexion.rules
%endif

%changelog
%autochangelog
