# Polymake intentionally leaves symbols undefined in the plugins, but Fedora's
# hardening flags disable RTLD_LAZY, resulting in undefined symbol errors while
# building the documentation.
%undefine _hardened_build

# In addition, we have to not tell the linker to require all symbols to be
# defined, else the plugin builds fail.
%undefine _strict_symbol_defs_build

# Build with the bundled version of jreality.  This currently includes bundled
# versions of several other Java projects (e.g., bsh, janino, jinput), and also
# itextpdf 5.3.2, whose license is problematic.
%bcond jreality 0

Name:           polymake
Version:        4.13
Release:        %autorelease

# GPL-2.0-or-later: the project as a whole
# MIT: external/js/three.js
# BSD-3-Clause: due to including permlib headers
# MPL-2.0 AND BSD-3-Clause AND Apache-2.0: Due to including eigen3 headers
License:        GPL-2.0-or-later AND MIT AND MPL-2.0 AND BSD-3-Clause AND Apache-2.0
Summary:        Algorithms on convex polytopes and polyhedra
URL:            https://polymake.org/
VCS:            git:https://github.com/polymake/polymake.git
Source0:        https://polymake.org/lib/exe/fetch.php/download/%{name}-%{version}-minimal.tar.bz2
# Man page written by Jerry James from text found in the sources.  Therefore,
# the copyright and license are the same as for the sources.
Source1:        %{name}.1
# This patch will not be sent upstream, since it is Fedora-specific.  Link
# against existing system libraries instead of building them from source,
# and do not use -rpath.
Patch:          %{name}-fedora.patch
# Do not use the hardening flags.  See above.
Patch:          %{name}-no-hardening.patch
# Fix detection of LattE
Patch:          %{name}-latte.patch
# Do not use the gold linker, which does not have support for DWARF 5
Patch:          %{name}-no-gold.patch
# Avoid a name clash with Singular
Patch:          %{name}-name-clash.patch
# Due to the fact that /usr/lib[64] == /lib[64], polymake deduces that the
# installation prefix is /lib[64] instead of /usr.
Patch:          %{name}-prefix.patch
# Do not try to read soplex configuration from scip.  The Fedora soplex
# package is independent of scip.
Patch:          %{name}-soplex.patch
# Adapt to a changed function name in Singular 4.3.2
Patch:          %{name}-Singular-4.3.2.patch
# Adapt to streamlined headers in GCC 15
Patch:          %{name}-gcc-15.patch

# Polymake 4.7 and later cannot be built on 32 bit platforms due to the
# limited integer ranges on those platforms.
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  4ti2
%if %{with jreality}
BuildRequires:  ant
%endif
BuildRequires:  azove
BuildRequires:  boost-devel
BuildRequires:  cddlib-devel
BuildRequires:  cmake
BuildRequires:  cmake(scip)
BuildRequires:  cmake(soplex)
BuildRequires:  doxygen
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  graphviz
%if %{with jreality}
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
%endif
BuildRequires:  libnormaliz-devel
BuildRequires:  lrslib-devel
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(SVG)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::Writer)
BuildRequires:  permlib-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libmongoc-1.0)
BuildRequires:  pkgconfig(libnauty)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(Singular)
BuildRequires:  ppl-devel
BuildRequires:  qhull
BuildRequires:  sympol-devel
BuildRequires:  TOPCOM
BuildRequires:  vinci
BuildRequires:  xhtml1-dtds

Requires:       boost-devel%{?_isa}
Requires:       cddlib-devel%{?_isa}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
%if %{with jreality}
Requires:       java
Requires:       javapackages-tools
%endif
Requires:       gcc-c++
Requires:       glibc-devel%{?_isa}
Requires:       libgcc%{?_isa}
Requires:       libnormaliz-devel%{?_isa}
Requires:       make
Requires:       mpfr-devel%{?_isa}
Requires:       ninja-build
Requires:       perl-interpreter = 4:%{?perl_version}%{!?perl_version:0}
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       permlib-devel
Requires:       ppl-devel%{?_isa}
Requires:       sympol-devel%{?_isa}

Recommends:     4ti2
Recommends:     azove
Recommends:     gfan
Recommends:     latte-integrale
Recommends:     normaliz
Recommends:     plantri
Recommends:     qhull
Recommends:     Singular
Recommends:     TOPCOM
Recommends:     vinci

Suggests:       evince
Suggests:       geomview
Suggests:       graphviz
Suggests:       gv
Suggests:       okular
Suggests:       sketch

# Add some provides the automatic generator missed
Provides:       perl(PolyDB::JsonIO)
Provides:       perl(Polymake::ConfigureStandalone)
Provides:       perl(Polymake::Namespaces)
Provides:       perl(Polymake::file_utils.pl)
Provides:       perl(Polymake::regex.pl)
Provides:       perl(Polymake::utils.pl)

# Don't expose private perl interfaces
%global __provides_exclude perl\\\(Geomview.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Graphviz.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(JSON.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Metapost.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(PerlIO.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Postscript.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Povray.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Sage\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Sketch.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(SplitsTree.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(ThreeJS.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(TikZ.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(X3d.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(application\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(namespaces\\\)

# Exclude private perl interfaces that we don't Provide
%global __requires_exclude perl\\\(namespaces.*\\\)

# Major version number
%global majver  %(cut -dr -f1 <<< %{version})

%description
Polymake is a tool to study the combinatorics and the geometry of convex
polytopes and polyhedra.  It is also capable of dealing with simplicial
complexes, matroids, polyhedral fans, graphs, tropical objects, and so
forth.

Polymake can use various computational packages if they are installed.
Those available from Fedora are: 4ti2, azove, gfan, latte-integrale,
normaliz, qhull, Singular, TOPCOM, and vinci.

Polymake can interface with various visualization packages if they are
installed.  Install one or more of the tools from the following list:
evince, geomview, graphviz, gv, and okular.

%package        doc
# GPL-2.0-or-later: the project as whole.  Other licenses are due to doxygen.
# GPL-1.0-or-later: *.{css,png,svg}
# MIT: *.js
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%prep
%autosetup -p0 -n %{name}-%{majver}

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Adapt to the Fedora version of sympol
sed -i.orig 's|yal/||;s|symmetrygroupconstruction/||' \
    bundled/sympol/apps/polytope/src/sympol_interface.cc
fixtimestamp bundled/sympol/apps/polytope/src/sympol_interface.cc

# Help polymake find the 4ti2 tools
sed -i.orig '/global variables/i\$ENV{'PATH'} = \"\$ENV{PATH}:%{_libdir}/4ti2/bin\";\n' perl/polymake
fixtimestamp perl/polymake

# The Fedora normaliz library is not linked with libsha256
sed -i '/NMZ_HASHLIBRARY/,+2d' bundled/libnormaliz/support/configure.pl

# Fix nauty detection
sed -i 's,@@LIBDIR@@,%{_libdir},' bundled/nauty/support/configure.pl

# Build verbosely.  Avoid parallelism, which often leads to resource exhaustion.
sed -i 's,\${NINJA},& -j 1 -v,' Makefile

# Avoid obsolescence warnings
sed -i 's/fgrep/grep -F/' perllib/Polymake/ConfigureStandalone.pm

%build
export CFLAGS='%{build_cflags} -I%{_includedir}/eigen3 -I%{_includedir}/gfanlib -I%{_includedir}/nauty -Wno-unused-local-typedefs'
export CXXFLAGS='%{build_cxxflags} -I%{_includedir}/eigen3 -I%{_includedir}/gfanlib -I%{_includedir}/nauty -Wno-unused-local-typedefs'
export LDFLAGS='%{build_ldflags} -lnormaliz -ldl'
export Arch=%{_arch}
# NOT an autoconf-generated configure script; do not use %%configure.
./configure --build=%{_arch} --prefix=%{_prefix} --libdir=%{_libdir} \
  --libexecdir=%{_libdir}/%{name} \
  --without-native \
  --with-cdd-include=%{_includedir}/cddlib/ \
  --with-cdd-lib=%{_libdir} \
  --with-flint=%{_prefix} \
  --with-libnormaliz=%{_prefix} \
  --with-lrs=%{_prefix} \
  --with-nauty-src=%{_prefix} \
  --with-permlib=%{_prefix} \
  --with-ppl=%{_prefix} \
  --with-scip=%{_prefix} \
  --with-singular=%{_prefix} \
  --with-soplex=%{_prefix} \
  --with-sympol-include=%{_includedir}/sympol/ \
  --with-sympol-lib=%{_libdir} \
  %{?with_jreality:--with-java=%{java_home}}%{!?with_jreality:--without-java} \
  --without-javaview

# No, really, we can't have the hardening flags on, and we do not want to
# specify -lpthread before -Wl,--as-needed
sed -e 's|-Wl,-z,now|-Wl,-z,lazy|g' \
    -e 's/-lpthread -shared/-shared/g' \
    -i build.%{_arch}/config.ninja

# FIXME: infrequent failures with %%{?_smp_mflags}, plus memory is tight
make all

%install
export Arch=%{_arch}
%make_install

# The doc building step looks in the wrong place for some files
mkdir ../xml
ln -s $PWD/xml/documentation/PTL-docs ../xml/documentation
ln -s build.%{_arch} build

# Build the documentation
mkdir doc
perl/polymake --script doxygen doc

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
sed "s/@VERSION@/%{version}/" %{SOURCE1} > %{buildroot}%{_mandir}/man1/%{name}.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

# Do not install app sources
rm -fr %{buildroot}%{_datadir}/%{name}/apps/*/src

# Fix permissions
chmod -R u+w %{buildroot}%{_prefix}

# JuPyMake and jupyter-polymake are built and installed separately
rm -fr %{buildroot}%{_datadir}/%{name}/resources/{JuPyMake,jupyter-polymake}

# Fix package notes breakage
sed -i 's@ -Wl,-dT,[^[:blank:]]*\.ld@@' %{buildroot}%{_libdir}/%{name}/config.ninja

%check
export COLUMNS=80
export LINES=25
make test

%files
%license COPYING
%doc Readme.md ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_datadir}/%{name}/
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_libdir}/lib%{name}*.so
%{_libdir}/lib%{name}*.so.4.13
%{_mandir}/man1/%{name}.1*

%files doc
%doc doc/*

%changelog
%autochangelog
