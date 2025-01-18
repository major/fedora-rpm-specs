# BUNDLING NOTES
# Macaulay2's memory management scheme requires close cooperation with libgc,
# and some of the supporting libraries must be compiled with special options to
# accomplish this.  In particular, Macaulay2 needs:
# - mathicgb configured --without-tbb
# - mpfr configured with --disable-thread-safe
# - flint linked with the GC-enabled mpfr
# - factory (from Singular) configured with --disable-omalloc --enable-streamio
#   and linked with the flint that is linked with the GC-enabled mpfr
# Since the main Fedora packages are not built in this way, we are forced to
# bundle these packages to avoid random GC-related crashes.  The packages
# memtailor and mathic, which sit underneath mathicgb, must also be bundled or
# we get random GC-related crashes for an as yet undiagnosed reason.
#
# We have to use the static versions of the libfplll and givaro libraries.
# They have global objects whose constructors run before GC is initialized.
# If we allow the shared libraries to be unloaded, which happens as a normal
# part of Macaulay2's functioning, then GC tries to free objects it did not
# allocate, which leads to a segfault.
#
# We have to bundle the linbox package.  It has global constructors that cause
# the same problem as libfplll.

%global emacscommit 90ce16a15ea1f4fad08e8ba0b74b5045f4a72e8f
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
Version: 1.24.05
Release: 6%{?dist}

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
#   - mathicgb (bundled)
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
#   - mathic (bundled)
# LGPL-3.0-or-later:
#   - mpfr (bundled)
# Apache-2.0:
#   - Macaulay2/packages/OpenMath.m2
#   - Macaulay2/packages/SCSCP.m2
# BSD-3-Clause:
#   - memtailor (bundled)
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
License: (GPL-2.0-only OR GPL-3.0-only) AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT AND OFL-1.1-RFN AND LicenseRef-Fedora-Public-Domain
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
%global normalizver 3.9.2
Source100: http://www.math.uiuc.edu/Macaulay2/Downloads/OtherSourceCode/normaliz-%{normalizver}.tar.gz
Provides:  bundled(normaliz) = %{normalizver}
%endif

# MPFR is bundled because it must be built with different threading options
%global mpfrver 4.1.0
Source101: http://www.mpfr.org/mpfr-%{mpfrver}/mpfr-%{mpfrver}.tar.xz
Provides:  bundled(mpfr) = %{mpfrver}

# FLINT is bundled because it must be linked with the specially-built MPFR
%global flintver 2.8.4
Source102: http://www.flintlib.org/flint-%{flintver}.tar.gz
Provides:  bundled(flint) = %{flintver}

# FACTORY is bundled because it must be built with special options
%global factoryver 4.3.0
Source103: https://www.singular.uni-kl.de/ftp/pub/Math/Factory/factory-%{factoryver}.tar.gz
Provides:  bundled(factory) = %{factoryver}

# MATHICGB is bundled because it must be built with different threading options
%global mathicgbver 1.0
%global mathicgbcommit 4cd2bd1357107cf0c83661fdda66c94987de4608
Source104: https://github.com/Macaulay2/mathicgb/tarball/%{mathicgbcommit}/mathicgb-%{mathicgbver}.tar.gz
Provides:  bundled(mathicgb) = %{mathicgbver}

# GTEST is bundled because MATHICGB refuses to build otherwise
%global gtestver 1.10.0
Source105: https://macaulay2.com/Downloads/OtherSourceCode/gtest-%{gtestver}.tar.gz

# MEMTAILOR is bundled because it causes garbage collector crashes otherwise
%global memtailorver 1.0
%global memtailorcommit f785005b92a54463dbd5377ab80855a3d2a5f92d
Source106: https://github.com/Macaulay2/memtailor/tarball/%{memtailorcommit}/memtailor-%{memtailorver}.tar.gz
Provides:  bundled(memtailor) = %{memtailorver}

# MATHIC is bundled because it causes garbage collector crashes otherwise
%global mathicver 1.0
%global mathiccommit 07e8df4ded6b586c0ce9eec0f9096690379749cb
Source107: https://github.com/Macaulay2/mathic/tarball/%{mathiccommit}/mathic-%{mathicver}.tar.gz
Provides:  bundled(mathic) = %{mathicver}

# LINBOX is bundled because it introduces static global objects
%global linboxver 1.7.0
Source108: https://github.com/linbox-team/linbox/releases/download/v%{linboxver}/linbox-%{linboxver}.tar.gz
Provides:  bundled(linbox) = %{linboxver}

## PATCHES FOR BUNDLED code
# Fix a buffer overflow and some constness issues
# https://github.com/linbox-team/linbox/pull/307
Source200: linbox-1.7.0.patch
# MPFR bug fixes from mpfr upstream.
Source201: mpfr-4.1.0.patch

## FAKE library tarballs that convince Macaulay2 to use the system versions
Source300: frobby_v0.9.0.tar.gz
Source301: cddlib-094m.tar.gz
Source302: lapack-3.9.0.tgz
Source303: 4ti2-1.6.10.tar.gz
Source304: libfplll-5.2.0.tar.gz
Source305: gfan0.6.2.tar.gz
Source306: givaro-4.1.1.tar.gz
Source307: lrslib-071a.tar.gz
Source308: TOPCOM-0.17.8.tar.gz
Source309: cohomCalg-0.32.tar.gz
Source310: glpk-4.59.tar.gz
Source311: Csdp-6.2.0.tgz
Source312: mpsolve-3.2.1.tar.gz

# let Fedora optflags override the defaults
Patch0: %{name}-1.15-optflags.patch
# give the build a little more time and space than upstream permits
Patch1: %{name}-1.16-ulimit.patch
# drop 'tests' from default make target
Patch2: %{name}-1.17-default_make_targets.patch
# disable check for gftables
Patch3: %{name}-1.18-no_gftables.patch
# adapt to libfplll 5.2.1
Patch4: %{name}-1.15-fplll.patch
# do not override the debug level
Patch5: %{name}-1.17-configure.patch
# Fix "error: in conversion to html, unknown TeX control sequence(s): \rightarrow"
Patch6: %{name}-1.16-rightarrow.patch
# Fix LTO warnings about mismatched declarations and definitions
Patch7: %{name}-1.18-lto.patch
# Avoid accessing invalid vector elements
# https://github.com/Macaulay2/M2/issues/3316
Patch8: %{name}-1.24-vector-overrun.patch

BuildRequires: 4ti2
BuildRequires: appstream
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: chrpath
BuildRequires: cohomCalg
BuildRequires: csdp-tools
BuildRequires: desktop-file-utils
%if 0%{?fedora}
BuildRequires: doxygen-latex
%else
BuildRequires: doxygen
%endif
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
BuildRequires: libfplll-static
BuildRequires: libfrobby-devel
BuildRequires: libgfan-devel
BuildRequires: libnormaliz-devel >= 3.9.2
BuildRequires: libtool
BuildRequires: lrslib-devel
BuildRequires: lrslib-utils
BuildRequires: make
BuildRequires: mpsolve-devel
BuildRequires: msolve-devel
BuildRequires: nauty
BuildRequires: normaliz
BuildRequires: ntl-devel
BuildRequires: ocl-icd-devel
BuildRequires: pari-devel
BuildRequires: pkgconfig(atomic_ops)
BuildRequires: pkgconfig(bdw-gc) >= 8.0.4
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
BuildRequires: pkgconfig(mpfi)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(qd)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(tbb)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: polymake
BuildRequires: python3-devel
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

# Macaulay2 no longer builds successfully on 32-bit platforms
# https://bugzilla.redhat.com/show_bug.cgi?id=1874318
#
# Macaulay2 started segfaulting during the build on ppc64le just prior to
# F40 Beta Freeze.  Disable it for now until we can diagnose the problem.
ExcludeArch: %{ix86} ppc64le

# Do not advertise the bundled mpfr
%global __provides_exclude libmpfr.so*


%description
Macaulay 2 is a new software system devoted to supporting research in
algebraic geometry and commutative algebra written by Daniel R. Grayson
and Michael E. Stillman

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

## bundled code
%if ! %system_normaliz
install -p -m644 %{SOURCE100} BUILD/tarfiles/
%endif
install -p -m644 %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE105} \
    BUILD/tarfiles/
install -p -m644 %{SOURCE108} BUILD/tarfiles/v%{linboxver}.tar.gz
sed -i 's/\(VERSION = \).*/\1%{mpfrver}/' libraries/mpfr/Makefile.in
sed -e 's/\(VERSION = \).*/\1%{linboxver}/' \
    -e 's,--with-gmp.*,--without-archnative GIVARO_CFLAGS=-I$(LIBRARIESDIR) GIVARO_LIBS="%{_libdir}/libgivaro.a",' \
    -i libraries/linbox/Makefile.in
tar -C submodules/mathicgb -xf %{SOURCE104} --strip-components=1
tar -C submodules/memtailor -xf %{SOURCE106} --strip-components=1
tar -C submodules/mathic -xf %{SOURCE107} --strip-components=1

## patches for bundled code
sed -e 's,--with-blas,&=%{_includedir}/flexiblas --with-ntl,' \
    -i libraries/flint/Makefile.in
cp -p %{SOURCE200} libraries/linbox/patch-%{linboxver}
sed -i 's/^#\(PATCHFILE\)/\1/' libraries/linbox/Makefile.in
sed -e '/^TARFILE =/iPATCHFILE = @abs_srcdir@/patch-$(VERSION)' \
    -i libraries/mpfr/Makefile.in
cp -p %{SOURCE201} libraries/mpfr/patch-%{mpfrver}

## fake library tarballs
install -p -m644 %{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} \
  %{SOURCE304} %{SOURCE305} %{SOURCE306} %{SOURCE307} %{SOURCE308} \
  %{SOURCE309} %{SOURCE310} %{SOURCE311} %{SOURCE312} BUILD/tarfiles/
sed -i '/PRECONFIGURE/d' libraries/{4ti2,cddlib,givaro,normaliz,topcom}/Makefile.in
sed -i 's/VERSION = 4\.0\.4/VERSION = 5.2.0/;/PATCHFILE/d' libraries/fplll/Makefile.in
sed -i '/PATCHFILE/d' libraries/{csdp,frobby,gfan,givaro,mpsolve,normaliz,topcom}/Makefile.in
sed -i '/INSTALLCMD/,/stdinc/d' libraries/frobby/Makefile.in
sed -i 's,install \(lib.*\.a\),ln -s %{_libdir}/\1,' libraries/lapack/Makefile.in

## fake givaro submodule
tar -C submodules/givaro --strip-components=1 -xzf %{SOURCE306}

%patch -P0 -p1 -b .optflags
%patch -P1 -p1 -b .ulimit
%patch -P2 -p1 -b .default_make_targets
%patch -P3 -p1 -b .no_gftables
# factory-gftables symlink
mkdir -p BUILD/%{_target_platform}/usr-dist/common/share/Macaulay2/Core
ln -s %{_datadir}/factory \
         BUILD/%{_target_platform}/usr-dist/common/share/Macaulay2/Core/factory
%patch -P4 -p1 -b .fplll
%patch -P5 -p1 -b .configure
%patch -P6 -p1 -b .rightarrow
%patch -P7 -p1 -b .lto
%patch -P8 -p1 -b .vector

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
    -e 's,-llapack -lrefblas,-lflexiblas,' \
    -e 's,\$added_fclibs != yes,"$added_fclibs" != yes,' \
    -i configure.ac

# We call it flint.  Upstream calls it flint2.
sed -i 's/\(LIBNAME = flint\)2/\1/' libraries/flint/Makefile.in

# Cannot do git submodule operations on a koji builder
sed -i 's/git-checkout-in-\$1, git-checkout-warning-for-\$1//' GNUmakefile.in

# Avoid obsolescence warnings
sed -i 's/egrep/grep -E/g' GNUmakefile.in Makefile Macaulay2/bin/Makefile.in \
    Macaulay2/tests/Makefile{,.test}.in libraries/Makefile.library.in
sed -i 's/fgrep/grep -F/g' Macaulay2/util/linkexec-alternative

# (re)generate configure
autoreconf -fi .


%build
%ifarch s390x
# For as yet unknown reasons, when this package is built with optimization
# level -O2 on s390x, the mathicgb code accesses out-of-bounds array elements.
# In addition, valgrind shows accesses to uninitialized elements of arrays
# that should not have any uninitialized elements.  The code eventually
# segfaults.
optflags=$(sed 's/-O2/-O/g' <<< "%{build_cflags}")
%else
optflags="%{build_cflags}"
%endif

# Let the configure script find lrslib utilities
module load lrslib-%{_arch}

## configure macro currently broken, due to some odd prefix-checks.  probably fixable -- Rex
mkdir -p BUILD/%{_target_platform}
pushd BUILD/%{_target_platform}
CPPFLAGS="$CPPFLAGS -I%{_includedir}/cddlib -I%{_includedir}/frobby" \
CFLAGS="$optflags -fsigned-char" \
CXXFLAGS="$optflags -fsigned-char" \
LIBS="-lflexiblas" \
../../configure \
  --build=%{_build} \
  --host=%{_host} \
  --with-issue=%{ISSUE} \
  --prefix=%{_prefix} \
  --disable-dumpdata \
  --enable-shared \
  --disable-fc-lib-ldflags \
  --disable-strip \
  --enable-fplll \
  --enable-linbox \
  --with-integer-package=gmp \
  --with-unbuilt-programs="cddplus nauty" \
  --enable-build-libraries="mpfr flint factory lapack fplll givaro linbox gtest"
  # The list of libraries and submodules above should include only those that:
  # 1. We bundle (mpfr, flint, factory, and linbox)
  # 2. We sneakily substitute one library for another (lapack -> flexiblas)
  # 3. Have to be linked with the static library (fplll and givaro)
popd

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
pushd %{buildroot}%{_emacs_sitelispdir}/macaulay2
mv M2-emacs* %{buildroot}%{_pkgdocdir}
mv README.md %{buildroot}%{_pkgdocdir}/README-emacs.md
%{_emacs_bytecompile} *.el
popd

## unpackaged files
# info dir
rm -fv %{buildroot}%{_infodir}/dir

# Delete misinstalled memtailor, mathic, and mathicgb libraries
rm -fr %{buildroot}/builddir


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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.24.05-5
- Rebuild for libfplll 5.5.0

* Mon Sep 23 2024 Jerry James <loganjerry@gmail.com> - 1.24.05-4
- Rebuild for nauty 2.8.9

* Sat Aug 24 2024 Jerry James <loganjerry@gmail.com> - 1.24.05-3
- Rebuild for Singular 4.4.0p4

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Jerry James <loganjerry@gmail.com> - 1.24.05-1
- Version 1.24.05

* Fri Feb 23 2024 Jerry James <loganjerry@gmail.com> - 1.22-6
- Build the polymake and scip examples
- Recommend scip
- Disable ppc64le build until segfaults can be diagnosed

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.22-3
- Rebuilt for Boost 1.83

* Fri Nov 10 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.22-2
- Correct appstreamcli invocation (--nonet no longer works)
- Ask appstreamcli to explain validation findings
- Also validate AppStream XML with appstream-util, required by guidelines

* Thu Oct 26 2023 Jerry James <loganjerry@gmail.com> - 1.22-1
- Version 1.22
- Drop upstreamed Macaulay2-configure-c99.patch
- Build against mariadb-connector-c instead of the server package

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 15 2023 Florian Weimer <fweimer@redhat.com> - 1.21-5
- Port configure script to C99

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.21-4
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.21-2
- Rebuild for libfplll 5.4.4

* Thu Dec 22 2022 Jerry James <loganjerry@gmail.com> - 1.21-1
- Version 1.21
- Drop upstreamed patch for crash when building documentation
- Use rdns names for the desktop and metainfo files

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 1.20-2
- Convert License tag to SPDX

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 1.20-2
- Rebuild for tinyxml2-9.0.0

* Thu Aug  4 2022 Jerry James <loganjerry@gmail.com> - 1.20-1
- Version 1.20

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.19.1-2
- Rebuilt for Boost 1.78

* Mon Feb 21 2022 Jerry James <loganjerry@gmail.com> - 1.19.1-1
- Version 1.19.1
- Disable LTO to work around segfaults

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Jerry James <loganjerry@gmail.com> - 1.19-1
- Version 1.19

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.18-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Jerry James <loganjerry@gmail.com> - 1.18-2
- Rebuild for ntl 11.5.1

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.18-1
- Version 1.18

* Thu Feb 18 2021 Jerry James <loganjerry@gmail.com> - 1.17-2
- Reduce optimization level on s390x to work around FTBFS
- Install metainfo
- Add -mathic patch to silence GCC warnings
- Add -lto patch to silence LTO warnings

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Jerry James <loganjerry@gmail.com> - 1.17-1
- Version 1.17
- Drop upstreamed patches: -nauty-paths, -format
- Merge -gcc11 patch into mathicgb-1.0.patch

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 1.16-2
- Add missing #includes for gcc-11

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.16-1
- Version 1.16
- Drop upstreamed patch: -xdg_open
- Add -ulimit patch for the slower builders
- Add -format and -rightarrow patches
- Bundle packages due to garbage collector crashes: linbox, memtailor, mathic
- Drop the XEmacs subpackage; XEmacs support no longer works

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.15.1.0-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Jeff Law <law@redhat.com> - 1.15.1.0-2
- Disable LTO

* Wed Jun  3 2020 Jerry James <loganjerry@gmail.com> - 1.15.1.0-1
- Version 1.15.1.0
- Drop upstreamed patches: -no_Werror, -mpir, -pthreads, -fflas-ffpack,
  -fno-common, -gtest, -pthreads

* Tue Feb 11 2020 Jerry James <loganjerry@gmail.com> - 1.14.0.1-4
- Add -fno-common patch to fix FTBFS with GCC 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 1.14.0.1-3
- Rebuild for ntl 11.4.3

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 1.14.0.1-2
- Rebuild for givaro 4.1.1, fflas-ffpack 2.4.3, and linbox 1.6.3

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 1.14.0.1-1
- Macaulay2-1.14.0.1
- Drop upstreamed -format and -exception patches
- Also bundle libmpc since it is linked with mpfr
- Drop fix for F26 symlink-file snafu
- Build with python 3 instead of python 2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.12.0.1-5
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Jerry James <loganjerry@gmail.com> - 1.12.0.1-3
- Rebuild for lrslib 070

* Wed Oct 10 2018 Jerry James <loganjerry@gmail.com> - 1.12.0.1-2
- Rebuild for ntl 11.3.0
- Build with openblas instead of atlas (bz 1618938)

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.12.0.1-1
- Macaulay2-1.12.0.1
- Replace tiny icon of unknown origin with various sizes of upstream's icon
- Remove deprecated entries from the desktop file
- Add upstream mpfr 3.1.6 patches

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 1.11-2
- Rebuild for ntl 11.1.0
- Remove scriptlets that call install-info
- Do not byte compile python files in the examples

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.11-1
- Macaulay2-1.11
- Drop upstreamed patches: -verbose_build, -givaro, -pari, -endian
- New patches: -fflas-ffpack, -format, -exception, -fplll, -configure
- Update bundled software
- Refresh INFO_FILES list

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.2-8
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.2-6
- Remove obsolete scriptlets

* Wed Oct 11 2017 Jerry James <loganjerry@gmail.com> - 1.9.2-5
- Link rather than copy the normaliz binary
- Fix accidental replacement of factory symlink with a directory

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 1.9.2-4
- Rebuild for ntl 10.5.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 1.9.2-1
- Macaulay2-1.9.2
- Drop upstreamed patches: -disable_broken_debug_functions, -gc, -rpath,
  -rh_configure_hack
- Add patches: -givaro, -gtest, -pari
- Create fake library and submodule tarballs to fool the build system into
  building in support for system libraries
- Bundle mpfr, flint, and factory to avoid garbage collector crashes
- Replace the (X)Emacs triggers with (x)emacs-filesystem dependencies
- New URLs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.6-33
- Rebuild for readline 7.x

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 1.6-32
- Rebuild for ntl 10.1.0

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 1.6-31
- Rebuild for ntl 9.11.0

* Fri Aug 12 2016 Jerry James <loganjerry@gmail.com> - 1.6-30
- Rebuild for fflas-ffpack 2.2.2, givaro 4.0.2, and linbox 1.4.2

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 1.6-29
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 1.6-28
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 1.6-27
- Rebuild for ntl 9.8.0
- Nauty is now available
- Drop -gcc-template-bug patch; gcc bug has been fixed

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 1.6-26
- Rebuild for ntl 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 1.6-25
- Rebuild for ntl 9.6.4
- Add -gcc-template-bug patch to work around gcc bug (bz 1307282)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6-23
- Rebuilt for Boost 1.60

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 1.6-22
- Rebuild for ntl 9.6.2
- Add python2 BR for the tests

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 1.6-21
- Rebuilt for libntl soname bump

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 1.6-20
- Rebuild for ntl 9.4.0

* Tue Sep 29 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-19
- refresh config.guess/config.sub hack, fix FTBFS on aarch64

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 1.6-18
- Rebuild for flint 2.5.2 and ntl 9.3.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.6-17
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.6-15
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 1.6-13
- Rebuild for ntl 9.1.1 and cddlib-094h

* Fri May 15 2015 Jerry James <loganjerry@gmail.com> - 1.6-12
- Bump and rebuild

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 1.6-11
- Rebuild for ntl 9.1.0

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 1.6-10
- Rebuild for ntl 8.1.2

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.6-9
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 1.6-8
- Rebuild for ntl 8.1.0
- Fix the desktop file name

* Wed Oct 29 2014 Jerry James <loganjerry@gmail.com> - 1.6-7
- Rebuild for ntl 6.2.1
- Revert Apr 8 HTML creation timeout, now handled upstream
- Revert use of -common subpkg; various arches timeout differently

* Wed Sep 24 2014 Rex Dieter <rdieter@fedoraproject.org> 1.6-6
- enable -common subpkg (to be more compatible with upstream packaging)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.6-4
- restore --build/--host configure options lost in 1.6 update, should help arm

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.6-2
- Rebuild for boost 1.55.0

* Mon May 19 2014 Rex Dieter <rdieter@fedoraproject.org> 1.6-1
- Macaulay2-1.6 (#1074594)
- ExcludeArch: %%arm (#1099598)

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-8
- rebuild (gc)

* Tue Apr  8 2014 Jerry James <loganjerry@gmail.com> - 1.5-7
- Build for all arches
- Increase HTML creation timeouts for slower processors, such as ARM
- Add --build and --host invocations to configure to fix mismatched ARM names

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 1.5-6
- Rebuild for ntl 6.1.0

* Fri Mar 21 2014 Jerry James <loganjerry@gmail.com> - 1.5-5
- The normaliz patch was used; bring it back
- Complete the removal of the system_normaliz variable
- Link with RPM_LD_FLAGS
- Due to use of a static library, explicitly link with -lflint

* Fri Jan 24 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.5-5
- drop unused patches (4ti2, normalize)

* Tue Jan 21 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.5-4
- utilize %%_libexecdir/Macaulay2/... for helper/system binaries
- libdir: %%_libdir => %%_prefix/lib
- -common subpkg option (not used yet)

* Tue Jan 14 2014 Jerry James <loganjerry@gmail.com> - 1.5-3
- Update normaliz interface for normaliz 2.8 and later

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.5-2
- Rebuild for boost 1.54.0

* Thu May 23 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-1
- Release: 1 (using non-snapshot release tarball now)

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.5-0.7.20130401
- update to 20130401 r15955 snapshot release
- (Build)Requires: factory-gftables (see bug #965655)
- refresh INFO_FILES content

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 1.5-0.6.20130214
- Rebuild for m4ri 20130416

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.5.20130214
- r15838 (20130214 snapshot)

* Wed Feb 13 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.4.20120807
- BR: doxygen-latex

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-0.3.20120807
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.2.20120807
- 1.5 20120807 r15022 snapshot

* Thu Jul 19 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-9
- rebuild against (Singular's) libfac/factory 3.1.3

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-7
- rebuild (pari)

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4-6
- Link to gmp not mpir.
- Rebuild with pari 2.5.

* Wed May 30 2012 Rex Dieter <rdieter@fedoraproject.org>
- 1.4-5
- License: GPLv2 or GPLv3 (#821036)
- pkgconfig-style deps

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-2
- rebuild (gdbm)

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-1
- 1.4

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-9
- Typo in INFO_FILES (#708086)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-7
- BR: cddlib-static (#609698)

* Tue Mar 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-6
- rebuild (factory/libfac)

* Tue Mar 16 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-5
- Run install-info on all of the .info files we installed
- Re-enable the now functional ppc64 build

* Wed Mar 10 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-4
- Add in missing Requires runtime dependancies

* Wed Mar 10 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-3
- GPLv3/GPLv2 conflict, use compat-readline5 - bz#511299

* Tue Mar 09 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-2
- Replace DSO patch with one accepted upstream
- Completely disable static linking

* Wed Feb 24 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-1
- Upstream version increment
- Remove unused patch
- Remove patch applied upstream
- Ensure consistent use of buildroot macro instead of RPM_BUILD_ROOT
- Fix implicit linking DSO failure
- Don't package empty .okay files which simply indicate test passes

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2-7
- Explicitly BR factory-static and libfac-static in accordance with the
  Packaging Guidelines (factory-devel/libfac-devel are still static-only).

* Tue Sep 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-6
- fixup/optimize scriplets

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-4
- rebuild for ntl-devel (shared)

* Wed Feb 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-3
- BR: libfac-devel,factory-devel >= 3.1
- restore ExcludeArch: ppc64 (#253847)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Rex Dieter <rdieter@fedoraproject.org> 1.2-1
- Macaulay-1.2

* Thu Oct 02 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1-2
- respin (factory/libfac)

* Tue Mar 11 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1-1
- Macaulay2-1.1
- Obsoletes/Provides: Macaulay2-common (upstream compatibility)
- re-enable ppc64 (#253847)
- IgnoreExampleErrors=true

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.95-10
- Autorebuild for GCC 4.3

* Tue Dec 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-9
- Provides: macaulay2
- respin against new(er) factory,libfac,ntl

* Wed Aug 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-8
- ExcludeArch: ppc64 (#253847)

* Tue Aug 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-7
- BR: gawk

* Tue Aug 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-6
- gc-7.0 patches

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-5
- License: GPLv2

* Mon Jan 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-4
- Ob/Pr: Macaulay2-doc, not -docs (#222609)

* Sat Jan 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-3
- re-enable ppc build (#201739)

* Tue Jan 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-2
- ./configure --disable-strip, for usable -debuginfo (#220893)

* Mon Dec 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.95-1
- Macaulay2-0.9.95

* Wed Nov 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.5.20060808svn
- .desktop Categories: -Application,Scientific,X-Fedora +ConsoleOnly

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.4.20060808svn
- fc6 respin

* Tue Aug 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.3.20060808svn
- ExcludeArch: ppc (bug #201739)
- %%ghost (x)emacs site-lisp bits (using hints from fedora-rpmdevtools)

* Tue Aug 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.2.20060808svn
- 20060808 snapshot

* Mon Jul 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.1.20060724svn
- 2006-07-15-0.9.20

* Wed Jul 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.10-0.6.20060710svn
- 0.9.10

-* Mon Jul 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.6.cvs20060327
- BR: ncurses-devel

* Fri May 05 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.4.cvs20060327
- 64bit patch (#188709)

* Wed Apr 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.3.cvs20060327 
- omit x86_64, for now (#188709)

* Tue Apr 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.2.cvs20060327
- 0.9.8 (cvs, no tarball yet)
- drop -doc subpkg (in main now)

* Mon Apr 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-22
- fix icon location (#188384)

* Thu Mar 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-21
- really disable %%check (fails on fc5+ anyway) 

* Fri Jan 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-20
- .desktop: drop Category=Development
- app icon: follow icon spec
- drop -emacs subpkg (in main now) 

* Fri Sep 16 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 0.9.2-19
- disable 'make check' (fc5/buildsystem error), besides, we get a 
  good consistency check when M2 builds all the doc examples.

* Wed Sep 14 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 0.9.2-18
- rebuild against gc-6.6

* Thu May 26 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-17
- rebuild (build system x86_64 repository access failed for 0.9.2-16)
- fix build for GCC 4 (#156223)

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-15
- rebuilt

* Mon Feb 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:0.9.2-14
- x86_64 issues (%%_libdir -> %%_prefix/lib )
- remove desktop_file macro usage

* Sat Oct 23 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.13
- BR: time (again)
- omit m2_dir/setup (not needed/wanted)

* Mon Oct 18 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.12
- actually *apply* gcc34 patch this time.

* Mon Oct 18 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.11
- gcc34 patch

* Fri Oct 1 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.10
- explicit BR versions for gc-devel, libfac-devel, factory-devel

* Tue Aug 10 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.9
- BR: time

* Thu Jun 03 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.8
- .desktop: remove Terminaloptions to be desktop agnostic
- .desktop: Categories += Education;Math;Development (Devel only
  added so it shows *somewhere* in gnome menus)

* Tue Jun 01 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.7
- disable default 'make check' (util/screen fails on fc2)

* Tue Mar 30 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.6
- desktop-file is now on by default
- use separate (not inline) .desktop file

* Mon Jan 05 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.5
- fix BuildRequires: desktop-file-utils to satisfy rpmlint.
- put emacs files in emacs subdir too (to follow supplied docs)
- *really* nuke .cvsignore files
- fix desktop-file-install --add-cateagories usage

* Tue Dec 23 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.4
- -emacs: use %%defattr
- -emacs: fix M2-init.el

* Mon Nov 17 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.3
- update/simplify macros
- desktop_file support.
- emacs subpkg.
- relax Req's on subpkgs to just: Requires: %%name = %%epoch:%%version
- use non-versioned BuildRequires
- remove redundant BuildRequires: gmp-devel
- remove gc patch, no longer needed.
- delete/not-package a bunch of unuseful files.
- use --disable-strip when debug_package is in use.

* Thu Nov 13 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.2
- no longer explictly Requires: emacs

* Wed Nov 05 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.1
- missing Epoch: 0

* Fri Sep 12 2003 Rex Dieter <rexdieter at sf.net> 0.9.2-0.fdr.0
- fedora'ize

