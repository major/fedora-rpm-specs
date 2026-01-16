# BUNDLING NOTES
# Macaulay2's memory management scheme requires close cooperation with libgc,
# and some of the supporting libraries must be compiled with special options to
# accomplish this.  In particular, Macaulay2 needs:
# - mpfr configured with --disable-thread-safe
# - flint linked with the GC-enabled mpfr
# - factory (from Singular) configured with --disable-omalloc --enable-streamio
#   and linked with the flint that is linked with the GC-enabled mpfr
# Since the main Fedora packages are not built in this way, we are forced to
# bundle these packages to avoid random GC-related crashes.
#
# We have to use the static versions of the libfplll and givaro libraries.
# They have global objects whose constructors run before GC is initialized.
# If we allow the shared libraries to be unloaded, which happens as a normal
# part of Macaulay2's functioning, then GC tries to free objects it did not
# allocate, which leads to a segfault.
#
# We have to bundle the linbox package.  It has global constructors that cause
# the same problem as libfplll.

%global emacscommit 524968452e95d010769ece30092edaa09d1e814f
%global emacsurl    https://github.com/Macaulay2/M2-emacs
%global emacsshort  %(cut -b -7 <<< %{emacscommit})
%global m2url       https://github.com/Macaulay2/M2

# Address randomization interferes with Macaulay2's memory management scheme,
# and linking with -z now breaks configure.
%undefine _hardened_build

## define to create -common subpkg
#global common 1
#if 0%%{?fedora}
# use system normaliz
%global system_normaliz 1
#endif
%global ISSUE %{?fedora:Fedora-%{fedora}}%{?rhel:RedHatEnterprise-%{rhel}}
%global M2_machine %{_target_cpu}-Linux-%{ISSUE}

# The examples contain some python files which should not be byte compiled
%global _python_bytecompile_extra 0

# Starting with GCC 12, Macaulay2 segfaults during the build on all
# architectures when LTO is enabled.  (With GCC 11, s390x did this, but the
# other architectures did not.)  Until somebody can figure out what is going
# on, disable LTO universally.
%define _lto_cflags %{nil}

Summary: System for algebraic geometry and commutative algebra
Name:    Macaulay2
Version: 1.25.11
Release: %autorelease

# GPL-2.0-only OR GPL-3.0-only:
#   - the project as a whole
#   - factory (bundled)
# GPL-1.0-or-later:
#   - Macaulay2/packages/FormalGroupLaws.m2
#   - Macaulay2/packages/WeylGroups.m2
# GPL-2.0-only:
#   - Macaulay2/packages/ModuleDeformations.m2
#   - Macaulay2/packages/QuillenSuslin.m2
#   - Macaulay2/packages/Visualize.m2
# GPL-2.0-or-later:
#   - Macaulay2/e/bibasis
#   - Macaulay2/m2/computations.m2
#   - Macaulay2/packages/AlgebraicSplines.m2
#   - Macaulay2/packages/BIBasis.m2
#   - Macaulay2/packages/Binomials.m2
#   - Macaulay2/packages/Chordal.m2
#   - Macaulay2/packages/Cremona.m2
#   - Macaulay2/packages/Cyclotomic.m2
#   - Macaulay2/packages/EdgeIdeals.m2
#   - Macaulay2/packages/FourierMotzkin.m2
#   - Macaulay2/packages/GKMVarieties.m2
#   - Macaulay2/packages/GradedLieAlgebras.m2
#   - Macaulay2/packages/GraphicalModels*
#   - Macaulay2/packages/Graphics.m2
#   - Macaulay2/packages/Graphs.m2
#   - Macaulay2/packages/GroebnerWalk.m2
#   - Macaulay2/packages/HyperplaneArrangements.m2
#   - Macaulay2/packages/InvariantRing*
#   - Macaulay2/packages/KustinMiller.m2
#   - Macaulay2/packages/LieTypes.m2
#   - Macaulay2/packages/MonomialAlgebras.m2
#   - Macaulay2/packages/MultiprojectiveVarieties.m2
#   - Macaulay2/packages/NAGtypes.m2
#   - Macaulay2/packages/Nauty*
#   - Macaulay2/packages/Normaliz.m2
#   - Macaulay2/packages/NumericalAlgebraicGeometry.m2
#   - Macaulay2/packages/PackageCitations.m2
#   - Macaulay2/packages/Posets.m2
#   - Macaulay2/packages/RationalPoints*
#   - Macaulay2/packages/ResLengthThree.m2
#   - Macaulay2/packages/ResolutionsOfStanleyReisnerRings.m2
#   - Macaulay2/packages/Resultants.m2
#   - Macaulay2/packages/RunExternalM2.m2
#   - Macaulay2/packages/SLPexpressions.m2
#   - Macaulay2/packages/SLnEquivariantMatrices.m2
#   - Macaulay2/packages/SimplicialDecomposability.m2
#   - Macaulay2/packages/SparseResultants.m2
#   - Macaulay2/packages/SpecialFanoFourfolds.m2
#   - Macaulay2/packages/StatGraphs.m2
#   - Macaulay2/packages/TriangularSets.m2
#   - Macaulay2/packages/VectorFields.m2
# GPL-3.0-or-later:
#   - normaliz, when it is bundled
#   - Macaulay2/e/mpreal.h
#   - Macaulay2/packages/BettiCharacters.m2
#   - Macaulay2/packages/CodingTheory.m2
#   - Macaulay2/packages/FGLM.m2
#   - Macaulay2/packages/HighestWeights*
#   - Macaulay2/packages/Jets.m2
#   - Macaulay2/packages/LocalRings
#   - Macaulay2/packages/MonomialIntegerPrograms.m2
#   - Macaulay2/packages/MultiplierIdeals.m2
#   - Macaulay2/packages/NormalToricVarieties.m2
#   - Macaulay2/packages/NumericSolutions.m2
#   - Macaulay2/packages/OldPolyhedra.m2
#   - Macaulay2/packages/OldToricVectorBundles.m2
#   - Macaulay2/packages/PieriMaps.m2
#   - Macaulay2/packages/Polyhedra.m2
#   - Macaulay2/packages/PositivityToricBundles.m2
#   - Macaulay2/packages/SchurRings.m2
#   - Macaulay2/packages/SchurVeronese.m2
#   - Macaulay2/packages/Simplicial*
#   - Macaulay2/packages/SpectralSequences.m2
#   - Macaulay2/packages/TensorComplexes.m2
#   - Macaulay2/packages/ToricTopology.m2
#   - Macaulay2/packages/ToricVectorBundles.m2
#   - Macaulay2/packages/VersalDeformations.m2
# LGPL-2.0-or-later:
#   - flint (bundled)
#   - linbox (bundled)
# LGPL-3.0-or-later:
#   - mpfr (bundled)
# Apache-2.0:
#   - Macaulay2/packages/OpenMath.m2
#   - Macaulay2/packages/SCSCP.m2
# MIT:
#   - Macaulay2/packages/Visualize/css
#   - Macaulay2/packages/Visualize/js
# MIT AND OFL-1.1-RFN:
#   - Macaulay2/packages/Style
# LicenseRef-Fedora-Public-Domain:
#   - Macaulay2/e/localring*
#   - Macaulay2/e/mutablecomplex*
#   - Macaulay2/e/NAG*
#   - Macaulay2/e/SLP*
#   - Macaulay2/packages/Depth.m2
#   - Macaulay2/packages/Divisor.m2
#   - Macaulay2/packages/FastMinors.m2
#   - Macaulay2/packages/LatticePolytopes.m2
#   - Macaulay2/packages/NoetherNormalization.m2
#   - Macaulay2/packages/RationalMaps.m2
#   - Macaulay2/packages/SectionRing.m2
License: (GPL-2.0-only OR GPL-3.0-only) AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND Apache-2.0 AND MIT AND OFL-1.1-RFN AND LicenseRef-Fedora-Public-Domain
URL:     https://macaulay2.com/
VCS:     git:%{m2url}.git
%if 0%{?snap:1}
Source0: %{name}-%{version}-%{snap}.tar.xz
%else
Source0: %{m2url}/archive/release-%{version}/%{name}-%{version}.tar.gz
%endif
Source1: %{emacsurl}/tarball/%{emacscommit}/M2-emacs-%{emacsshort}.tar.gz

# Various sizes of the planets icon from macaulay2.com.  See README.icons in
# the tar file for details on how these icons were created.
Source10: Macaulay2-icons.tar.xz
Source11: com.macaulay2.macaulay2.desktop
Source12: com.macaulay2.macaulay2.metainfo.xml
Source20: etags.sh

## BUNDLED code
# Normaliz must sometimes be bundled due to version differences
%if ! %system_normaliz
%global normalizver 3.11.0
Source100: http://www.math.uiuc.edu/Macaulay2/Downloads/OtherSourceCode/normaliz-%{normalizver}.tar.gz
Provides:  bundled(normaliz) = %{normalizver}
%endif

# MPFR is bundled because it must be built with different threading options
%global mpfrver 4.2.2
Source101: https://www.mpfr.org/mpfr-%{mpfrver}/mpfr-%{mpfrver}.tar.gz
Provides:  bundled(mpfr) = %{mpfrver}

# FLINT is bundled because it must be linked with the specially-built MPFR
%global flintver 3.3.1
Source102: https://github.com/flintlib/flint/archive/v%{flintver}/flint-%{flintver}.tar.gz
Provides:  bundled(flint) = %{flintver}

# FACTORY is bundled because it must be built with special options
%global factoryver 4.4.1
Source103: https://www.singular.uni-kl.de/ftp/pub/Math/Factory/factory-%{factoryver}.tar.gz
Provides:  bundled(factory) = %{factoryver}

# LINBOX is bundled because it introduces static global objects
%global linboxver 1.7.1
Source104: https://github.com/linbox-team/linbox/releases/download/v%{linboxver}/linbox-%{linboxver}.tar.gz
Provides:  bundled(linbox) = %{linboxver}

## PATCHES FOR BUNDLED code
# No patches

## FAKE library tarballs that convince Macaulay2 to use the system versions
Source300: frobby_v0.9.5.tar.gz
Source301: cddlib-094m.tar.gz
# lapack
Source302: v3.12.1.tar.gz
Source303: 4ti2-1.6.13.tar.gz
Source304: fplll-5.5.0.tar.gz
Source305: gfan0.6.2.tar.gz
Source306: givaro-4.2.1.tar.gz
Source307: lrslib-073.tar.gz
Source308: TOPCOM-1.1.2.tar.gz
Source309: cohomCalg-0.32.tar.gz
Source310: glpk-5.0.tar.gz
Source311: Csdp-6.2.0.tgz
Source312: mpsolve-3.2.3.tar.gz
# msolve
%global msolvever 0.9.2
Source313: v%{msolvever}.tar.gz

# let Fedora optflags override the defaults
Patch: %{name}-1.25-optflags.patch
# give the build a little more time and space than upstream permits
Patch: %{name}-1.16-ulimit.patch
# drop checking of html links from default make target
Patch: %{name}-1.25-default_make_targets.patch
# do not override the debug level
Patch: %{name}-1.17-configure.patch
# Fix LTO warnings about mismatched declarations and definitions
Patch: %{name}-1.18-lto.patch

BuildRequires: 4ti2
BuildRequires: appstream
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: chrpath
BuildRequires: cmake
BuildRequires: cohomCalg
BuildRequires: csdp-tools
BuildRequires: desktop-file-utils
BuildRequires: diffutils
%if 0%{?fedora}
BuildRequires: doxygen-latex
%else
BuildRequires: doxygen
%endif
BuildRequires: e-antic-devel
BuildRequires: eigen3-static
# etags
BuildRequires: emacs
BuildRequires: factory-gftables
BuildRequires: flex
BuildRequires: gawk
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: gdb
BuildRequires: gdbm-devel
BuildRequires: gettext-devel
BuildRequires: gfan
BuildRequires: git-core
BuildRequires: givaro-static
BuildRequires: glpk-devel
BuildRequires: iml-devel
BuildRequires: info
BuildRequires: libappstream-glib
BuildRequires: libatomic
BuildRequires: libfplll-static
BuildRequires: libfrobby-devel
BuildRequires: libgfan-devel
BuildRequires: libnormaliz-devel >= 3.10.4
BuildRequires: libtool
BuildRequires: lrslib-devel
BuildRequires: lrslib-utils
BuildRequires: make
BuildRequires: mpsolve-devel
BuildRequires: msolve
BuildRequires: msolve-devel
BuildRequires: nauty
BuildRequires: normaliz
BuildRequires: ocl-icd-devel
BuildRequires: pari-devel
BuildRequires: pkgconfig(bdw-gc) >= 8.2.6
BuildRequires: pkgconfig(cddlib)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fflas-ffpack)
BuildRequires: pkgconfig(flexiblas)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libmariadb)
BuildRequires: pkgconfig(libnauty)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(m4ri)
BuildRequires: pkgconfig(m4rie)
BuildRequires: pkgconfig(mathic)
BuildRequires: pkgconfig(mathicgb)
BuildRequires: pkgconfig(memtailor)
BuildRequires: pkgconfig(mpfi)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(ntl)
BuildRequires: pkgconfig(qd)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(tbb)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: polymake
BuildRequires: python3-devel
BuildRequires: R
BuildRequires: scip
BuildRequires: texinfo
BuildRequires: time
BuildRequires: TOPCOM
BuildRequires: transfig
%ifarch %{valgrind_arches}
BuildRequires: valgrind
%endif

Requires: 4ti2
Requires: cohomCalg
Requires: csdp-tools
Requires: emacs-filesystem
Requires: factory-gftables
Requires: gfan
Requires: hicolor-icon-theme
Requires: lrslib-utils
Requires: nauty
Requires: normaliz
Requires: TOPCOM

# M2-help
Requires: xdg-utils

Recommends: mathicgb
Recommends: msolve
Recommends: scip

%if 0%{?common}
Requires:  %{name}-common = %{version}-%{release}
%else
Obsoletes: Macaulay2-common < %{version}-%{release}
Provides:  Macaulay2-common = %{version}-%{release}
%endif
Obsoletes: Macaulay2-doc < %{version}-%{release} 
Provides:  Macaulay2-doc = %{version}-%{release}
Obsoletes: Macaulay2-emacs < %{version}-%{release}
Provides:  Macaulay2-emacs = %{version}-%{release}

Provides:  macaulay2 = %{version}-%{release}

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Macaulay2 takes more than 14 hours to build on ppc64le, more than twice as
# long as the x86_64 build, and it is doubtful that anyone will ever use it on
# that platform anyway.
ExcludeArch: %{ix86} %{power64}

# Do not advertise the bundled mpfr
%global __provides_exclude libmpfr.so*


%description
Macaulay 2 is a new software system devoted to supporting research in
algebraic geometry and commutative algebra written by Daniel R. Grayson and
Michael E. Stillman.

%package common
Summary: Common files for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description common
%{summary}.


%prep
%setup -q -n M2-release-%{version}/M2
%setup -q -n M2-release-%{version}/M2 -T -D -a 10
tar -C Macaulay2/editors/emacs --strip-components=1 -xzf %{SOURCE1}

install -p -m755 %{SOURCE20} ./etags

## TODO: Remove this when Fedora moves to normaliz 3.11.0
sed -i 's/3\.11\.0/3.10.5/' libraries/normaliz/Makefile.in

## bundled code
%if ! %system_normaliz
install -p -m644 %{SOURCE100} BUILD/tarfiles/
%endif
install -p -m644 %{SOURCE101} %{SOURCE102} %{SOURCE103} BUILD/tarfiles/
install -p -m644 %{SOURCE104} BUILD/tarfiles/v%{linboxver}.tar.gz
sed -i 's/\(VERSION = \).*/\1%{mpfrver}/' libraries/mpfr/Makefile.in
sed -e 's/\(VERSION = \).*/\1%{linboxver}/' \
    -e 's,--with-gmp.*,--without-archnative GIVARO_CFLAGS=-I$(LIBRARIESDIR) GIVARO_LIBS="%{_libdir}/libgivaro.a",' \
    -i libraries/linbox/Makefile.in

## patches for bundled code
sed -e 's,--disable-shared,& --disable-arch --with-blas-include=%{_includedir}/flexiblas --with-ntl-include=%{_includedir}/NTL,' \
    -e 's/3\.2\.1/%{flintver}/' \
    -e 's/\(LICENSEFILES = \).*/\1COPYING COPYING.LESSER/' \
    -e 's/-pedantic-errors/& -fno-strict-aliasing/' \
    -e "s,PRECONFIGURE.*,& \&\& sed -i 's/openblas/flexiblas/' configure," \
    -i libraries/flint/Makefile.in

## fake library tarballs
install -p -m644 %{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} \
  %{SOURCE304} %{SOURCE305} %{SOURCE306} %{SOURCE307} %{SOURCE308} \
  %{SOURCE309} %{SOURCE310} %{SOURCE311} %{SOURCE312} %{SOURCE313} \
  BUILD/tarfiles/
sed -i '/PRECONFIGURE/d' libraries/{4ti2,cddlib,givaro,normaliz,topcom}/Makefile.in
sed -i '/PATCHFILE/d' libraries/{csdp,frobby,gfan,givaro,mpsolve,normaliz,topcom}/Makefile.in
sed -i '/INSTALLCMD/,/stdinc/d' libraries/frobby/Makefile.in
sed -i 's,install \(lib.*\.a\),ln -s %{_libdir}/\1,' libraries/lapack/Makefile.in

## fake givaro submodule
tar -C submodules/givaro --strip-components=1 -xzf %{SOURCE306}

## flint submodule
tar -C submodules/flint --strip-components=1 -xzf %{SOURCE102}

%autopatch -p1


%conf
# repeatable builds: inject a node name
sed -i 's,`uname -n`,build.fedoraproject.org,' configure.ac

# gdb is used during the build; let it autoload some files
if [ "$HOME" = "/builddir" ]; then
  echo "set auto-load safe-path /" > /builddir/.gdbinit
fi

# Use, but don't build, cddlib, fflas-ffpack, and gc.  Use the static versions
# of libfplll and givaro.  Link with flexiblas instead of the reference blas
# and lapack.  Fix typos.
sed -e 's/BUILD_cddlib=yes/BUILD_cddlib=no/' \
    -e 's/BUILD_gc=yes/BUILD_gc=no/' \
    -e 's/BUILD_fflas_ffpack=yes/BUILD_fflas_ffpack=no/' \
    -e 's,-lfplll,%{_libdir}/libfplll.a -lqd,' \
    -e 's,`\$PKG_CONFIG --libs givaro`,%{_libdir}/libgivaro.a,' \
    -e 's,-lgivaro,%{_libdir}/libgivaro.a,' \
    -e 's,-lrefblas,-lflexiblas,' \
    -e 's,-llapack,-lflexiblas,' \
    -e 's,\$added_fclibs != yes,"$added_fclibs" != yes,' \
    -i configure.ac

# Do not try to download tarballs
sed -i '/^fetch: download-enabled/d' libraries/Makefile.library.in

# Do not try to fetch sources with git
sed -i 's/^\(fetch:\) update-submodule/\1/' libraries/Makefile.library.in

# All examples should produce expected results on x86_64.  Other platforms
# sometimes encounter problems; e.g., due to differences in rounding error of
# floating point numbers.
%ifnarch %{x86_64}
sed -e '/^IgnoreExampleErrors/s/false/true/' \
    -e '/^CheckDocumentation/s/true/false/' \
    -i Macaulay2/packages/Makefile.in
%endif

# (re)generate configure
autoreconf -fi .


%build
# Let the configure script find lrslib utilities
module load lrslib-%{_arch}

## configure macro currently broken, due to some odd prefix-checks.  probably fixable -- Rex
mkdir -p BUILD/%{_target_platform}
cd BUILD/%{_target_platform}
CPPFLAGS="$CPPFLAGS -I%{_includedir}/cddlib -I%{_includedir}/frobby" \
CFLAGS='%{build_cflags} -fsigned-char' \
CXXFLAGS='%{build_cflags} -fsigned-char' \
LIBS="-lflexiblas" \
../../configure \
  --build=%{_build} \
  --host=%{_host} \
  --with-issue=%{ISSUE} \
  --prefix=%{_prefix} \
  --enable-shared \
  --disable-strip \
  --enable-linbox \
  --with-blas=flexiblas \
  --with-lapack=flexiblas \
  --with-system-libs \
  --with-unbuilt-programs="cddplus nauty" \
  --enable-build-libraries="mpfr flint factory lapack fplll givaro linbox"
  # The list of libraries and submodules above should include only those that:
  # 1. We bundle (mpfr, flint, factory, and linbox)
  # 2. We sneakily substitute one library for another (lapack -> flexiblas)
  # 3. Have to be linked with the static library (fplll and givaro)
cd -

# link with static libraries when global constructors run prior to GC
# initialization.  Otherwise, unloading the shared object causes a crash.
# We have to do this because we pick up references to -lgivaro from other
# packages during the configure script execution.
for fil in $(grep -Erl -e '-lfplll|-lgivaro' .); do
  sed -e 's,-lfplll,%{_libdir}/libfplll.a,' \
      -e 's,-lgivaro,%{_libdir}/libgivaro.a,' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm -f $fil.orig
done

# Do not try to checkout submodules with git
mkdir -p BUILD/%{_target_platform}/libraries/{flint,givaro}
touch BUILD/%{_target_platform}/libraries/{flint,givaro}/.submodule-updated

# Build
make -C BUILD/%{_target_platform} VERBOSE=true Verbose=true IgnoreExampleErrors=true

# log errors
find BUILD/%{_target_platform}/ -name *.errors -execdir echo {} \; -execdir cat {} \;


%install
%make_install -C BUILD/%{_target_platform} IgnoreExampleErrors=true

# link, don't copy, the binaries
mbindir=%{buildroot}%{_libexecdir}/Macaulay2/bin
for fil in checkregularity chiro2circuits chiro2cocircuits cohomcalg csdp lrs \
    normaliz points2allfinetriangs points2alltriangs points2chiro \
    points2finetriang points2finetriangs points2flips points2nallfinetriangs \
    points2nalltriangs points2nfinetriangs points2nflips points2ntriangs \
    points2triangs points2volume; do
  rm -f $mbindir/$fil
  ln -s %{_bindir}/$fil $mbindir/$fil
done

# unbundle factory-gftables
rm -fr %{buildroot}%{_datadir}/Macaulay2/Core/factory
ln -s ../../factory %{buildroot}%{_datadir}/Macaulay2/Core

# app img
for sz in 64 72 96 128 192 256 512; do
  sz2=${sz}x${sz}
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$sz2/apps
  install -p -m644 icons/NinePlanets-${sz2}.png \
                   %{buildroot}%{_datadir}/icons/hicolor/$sz2/apps/%{name}.png
done

desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE11}

mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE12} %{buildroot}%{_metainfodir}
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/com.macaulay2.macaulay2.metainfo.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}%{_metainfodir}/com.macaulay2.macaulay2.metainfo.xml

# Byte compile the Emacs files, and move the documentation
cd %{buildroot}%{_emacs_sitelispdir}/macaulay2
mv M2-emacs* %{buildroot}%{_pkgdocdir}
mv README.md %{buildroot}%{_pkgdocdir}/README-emacs.md
%{_emacs_bytecompile} *.el
cd -

## unpackaged files
# info dir
rm -fv %{buildroot}%{_infodir}/dir


%check
# The test suite has grown to the point where it takes many hours to run.
# Just run the most basic tests.
make check -C BUILD/%{_target_platform}/Macaulay2/e
make check -C BUILD/%{_target_platform}/Macaulay2/bin


%files
%{_bindir}/M2
%{_bindir}/M2-binary
%{_prefix}/lib/Macaulay2/
%{_libexecdir}/Macaulay2/

%if 0%{?common}
%files common
%endif
%{_datadir}/Macaulay2/
%{_datadir}/applications/com.macaulay2.macaulay2.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/com.macaulay2.macaulay2.metainfo.xml
%{_docdir}/Macaulay2/
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_emacs_sitelispdir}/macaulay2/


%changelog
%autochangelog
