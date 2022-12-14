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
%bcond_with jreality

# Disable LTO on arm due to lack of memory.
%ifarch %{arm}
%global _lto_cflags %{nil}
%endif

%global upver   4.7
%global majver  %(cut -dr -f1 <<< %{upver})

Name:           polymake
Version:        %(tr r . <<< %{upver})
Release:        3%{?dist}

# GPL-2.0-or-later: the project as a whole
# MIT: external/js/three.js
# BSD-3-Clause: due to including permlib headers
# MPL-2.0 AND BSD-3-Clause AND Apache-2.0: Due to including eigen3 headers
License:        GPL-2.0-or-later AND MIT AND MPL-2.0 AND BSD-3-Clause AND Apache-2.0
Summary:        Algorithms on convex polytopes and polyhedra
URL:            https://polymake.org/
Source0:        https://polymake.org/lib/exe/fetch.php/download/%{name}-%{upver}-minimal.tar.bz2
# Man page written by Jerry James from text found in the sources.  Therefore,
# the copyright and license are the same as for the sources.
Source1:        %{name}.1
# Fake polymake-config script to use while building the Jupyter packages.
# The real polymake-config is nonfunctional until it is installed.
Source2:        %{name}-config
# This patch will not be sent upstream, since it is Fedora-specific.  Link
# against existing system libraries instead of building them from source,
# and do not use -rpath.
Patch0:         %{name}-fedora.patch
# Do not use the hardening flags.  See above.
Patch1:         %{name}-no-hardening.patch
# Fix detection of LattE
Patch2:         %{name}-latte.patch
# Do not use the gold linker, which does not have support for DWARF 5
Patch3:         %{name}-no-gold.patch
# Avoid a name clash with Singular
Patch4:         %{name}-name-clash.patch
# Due to the fact that /usr/lib[64] == /lib[64], polymake deduces that the
# installation prefix is /lib[64] instead of /usr.
Patch5:         %{name}-prefix.patch

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
BuildRequires:  ocaml-tplib-tools
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(MongoDB)
BuildRequires:  perl(SVG)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::Writer)
BuildRequires:  permlib-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(nauty)
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
Requires:       perl(:MODULE_COMPAT_%{perl_version})
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
Recommends:     ocaml-tplib-tools
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
Provides:       perl(PolyDB::DatabaseCursor)
Provides:       perl(PolyDB::JsonIO)
Provides:       perl(Polymake::ConfigureStandalone)
Provides:       perl(Polymake::Core::ShellHelpers)
Provides:       perl(Polymake::Core::ShellMock)
Provides:       perl(Polymake::Namespaces)
Provides:       perl(Polymake::Test::Validation)
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

# This can be removed when F38 reaches EOL
Obsoletes:      polymake-singular < 4.4-1
Provides:       polymake-singular = %{version}-%{release}

%description
Polymake is a tool to study the combinatorics and the geometry of convex
polytopes and polyhedra.  It is also capable of dealing with simplicial
complexes, matroids, polyhedral fans, graphs, tropical objects, and so
forth.

Polymake can use various computational packages if they are installed.
Those available from Fedora are: 4ti2, azove, gfan, latte-integrale,
normaliz, ocaml-tplib-tools, qhull, Singular, TOPCOM, and vinci.

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

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Adapt to the Fedora version of sympol
sed -i.orig "s|yal/||;s|symmetrygroupconstruction/||" \
    bundled/sympol/apps/polytope/src/sympol_interface.cc
fixtimestamp bundled/sympol/apps/polytope/src/sympol_interface.cc

# Help polymake find the 4ti2 tools
sed -i.orig "/global variables/i\$ENV{'PATH'} = \"\$ENV{PATH}:%{_libdir}/4ti2/bin\";\n" perl/polymake
fixtimestamp perl/polymake

# Linking with libnormaliz requires linking with libeanticxx and libcocoa
sed -i 's/-leantic/-leanticxx -lcocoa/' bundled/libnormaliz/support/configure.pl

# Fix nauty detection
sed -i 's,@@LIBDIR@@,%{_libdir},' bundled/nauty/support/configure.pl

# Build verbosely.  Avoid parallelism, which often leads to resource exhaustion.
sed -i 's,\${NINJA},& -j 1 -v,' Makefile

%build
export LC_ALL=C.UTF-8
export CFLAGS="%{build_cflags} -I%{_includedir}/arb -I%{_includedir}/eigen3 -I%{_includedir}/gfanlib -I%{_includedir}/nauty -Wno-unused-local-typedefs"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="%{build_ldflags} -lnormaliz -ldl"
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
  --with-singular=%{_prefix} \
  --with-sympol-include=%{_includedir}/sympol/ \
  --with-sympol-lib=%{_libdir} \
%if %{with jreality}
  --with-java=%{java_home} \
%else
  --without-java \
%endif
  --without-javaview

# No, really, we can't have the hardening flags on, and we do not want to
# specify -lpthread before -Wl,--as-needed
sed -e 's| -Wl,-z,now -specs=.*redhat-hardened-ld||g' \
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

%files
%license COPYING
%doc Readme.md ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_datadir}/%{name}/
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_libdir}/lib%{name}*.so
%{_libdir}/lib%{name}*.so.4.7
%{_mandir}/man1/%{name}.1*

%files doc
%doc doc/*

%changelog
* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - %(tr r . <<< %{upver})-3
- Convert License tags to SPDX

* Sat Aug 27 2022 Jerry James <loganjerry@gmail.com> - 4.7-3
- Rebuild for normaliz 3.9.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 4.7-1
- Version 4.7
- Drop upstreamed perl 5.36 patch
- Stop building on 32-bit architectures due to limited integer range

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 4.6-8
- Rebuild for flint 2.9.0

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.6-7
- Perl 5.36 rebuild

* Fri May 13 2022 Jerry James <loganjerry@gmail.com> - 4.6-6
- Bump and rebuild to fix Singular dependency

* Fri Apr 22 2022 Jerry James <loganjerry@gmail.com> - 4.6-5
- Rebuild for normaliz 3.9.3

* Tue Mar 29 2022 Jerry James <loganjerry@gmail.com> - 4.6-4.2
- Bump and rebuild to fix perl dependency

* Sat Mar 26 2022 Jerry James <loganjerry@gmail.com> - 4.6-4.1
- Bump and rebuild to preserve upgrade path from F36

* Sun Mar 20 2022 Jerry James <loganjerry@gmail.com> - 4.6-4
- Rebuild for Singular 4.2.1p3
- Add -prefix patch to fix bad prefix deduction
- Remove bad package notes path from config.ninja

* Wed Mar 16 2022 Paul Howarth <paul@city-fan.org> - 4.6-3
- Rebuild for perl 5.34.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Jerry James <loganjerry@gmail.com> - 4.6-1
- Version 4.6

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 4.5-1
- Version 4.5
- Add -name-clash patch to fix name collision with Singular

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 4.4-4
- Rebuild for flint 2.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Jerry James <loganjerry@gmail.com> - 4.4-2
- Rebuild for flint 2.7.1 and normaliz 3.9.0
- Do not link with gold until it has DWARF 5 support

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 4.4-1
- Version 4.4
- Drop the -singular subpackage; the circular dependency no longer exists

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.3-5
- Perl 5.34 rebuild

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 4.3-4
- Rebuild for normaliz 3.8.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Jerry James <loganjerry@gmail.com> - 4.3-2
- Rebuild for perl 5.32.1

* Wed Dec 16 2020 Jerry James <loganjerry@gmail.com> - 4.3-1
- Version 4.3

* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 4.2-2
- Rebuild for normaliz 3.8.9

* Thu Sep 24 2020 Jerry James <loganjerry@gmail.com> - 4.2-1
- Version 4.2

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 4.1-5
- Rebuild for normaliz 3.8.8

* Mon Aug 10 2020 Jerry James <loganjerry@gmail.com> - 4.1-4
- Rebuild for normaliz 3.8.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 4.1-1
- Version 4.1
- Drop upstreamed -sizet patch

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.1-4
- Perl 5.32 rebuild

* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 4.0.1-3
- Rebuild for perl 5.30.3

* Mon Mar 16 2020 Jerry James <loganjerry@gmail.com> - 4.0.1-2
- Rebuild for perl 5.30.2

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- Version 4.0r1
- Add -sizet patch to work around FTBFS with GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 3.6-1
- Version 3.6
- Drop the JuPyMake and jupyter-polymake support; those packages are now
  built and installed separately

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 3.5-6
- Rebuild for perl 5.30.1

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 3.5-5
- Rebuild for mpfr 4

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 3.5-4
- Rebuild for normaliz 3.8.0

* Wed Aug 28 2019 Jerry James <loganjerry@gmail.com> - 3.5-3
- Bump all of the release numbers and rebuild

* Tue Aug 27 2019 Jerry James <loganjerry@gmail.com> - 3.5-2
- Fix permlib-devel R; it is noarch

* Mon Aug 26 2019 Jerry James <loganjerry@gmail.com> - 3.5-1
- New upstream version
- Drop upstreamed -tempref patch

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-7
- Rebuilt for Python 3.8

* Fri Aug  2 2019 Jerry James <loganjerry@gmail.com> - 3.4-6
- Rebuild for normaliz 3.7.4 and to fix subpackage release number issues

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Jerry James <loganjerry@gmail.com> - 3.4-4
- Rebuild for normaliz 3.7.3

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.4-3
- Perl 5.30 rebuild

* Thu May  9 2019 Jerry James <loganjerry@gmail.com> - 3.4-2
- Rebuild for normaliz 3.7.2

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 3.4-1
- New upstream version

* Tue Apr 23 2019 Jerry James <loganjerry@gmail.com> - 3.3-2
- Rebuild for perl 5.28.2

* Mon Mar 18 2019 Jerry James <loganjerry@gmail.com> - 3.3-1
- New upstream version
- Add python3-JuPyMake and -jupyter subpackages

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2r4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Jerry James <loganjerry@gmail.com> - 3.2r4-2
- Rebuild for perl 5.28.1

* Tue Nov 20 2018 Jerry James <loganjerry@gmail.com> - 3.2r4-1
- New upstream version

* Thu Oct 25 2018 Jerry James <loganjerry@gmail.com> - 3.2r3-8
- Rebuild for Singular 4.1.1p3

* Wed Oct 17 2018 Jerry James <loganjerry@gmail.com> - 3.2r3-7
- Call the right count program from latte-integrale

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 3.2r3-6
- Rebuild for cddlib 0.94j

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 3.2r3-5
- perl(MongoDB) is now available on all arches
- Reverse the sense of the main package and the singular subpackage, so that
  users who install "polymake" get a working package.  The singular subpackage,
  perversely, has no dependency on Singular.  It is to be used to build
  Singular; otherwise, the Singular BR on polymake pulls in the old version of
  Singular, which is often broken due to an soname bump.

* Sat Aug  4 2018 Jerry James <loganjerry@gmail.com> - 3.2r3-4
- Fix separation of Singular dependencies into subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2r3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.2r3-2
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 3.2r3-1
- New upstream version
- Drop upstreamed -lrs-system-fix and -gcc7 patches
- Add -no-hardening patch to fix FTBFS
- BR gmp-devel, ninja-build, perl(JSON), and permlib-devel

* Wed May  2 2018 Jerry James <loganjerry@gmail.com> - 3.1-12
- Rebuild for perl 5.26.2

* Fri Mar  2 2018 Jerry James <loganjerry@gmail.com> - 3.1-11
- Turn off _strict_symbol_defs_build so the plugins will build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 3.1-9
- Rebuild for cddlib and normaliz 3.4.0

* Wed Sep 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.1-8
- Rebuild for Perl 5.26.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 3.1-5
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.1-4
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Apr  6 2017 Jerry James <loganjerry@gmail.com> - 3.1-2
- Rebuild with Singular support

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 3.1-1
- New upstream release

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 3.0r2-8
- Rebuild for ppl 1.2
- Drop -ppl patch
- Add -gcc7 patch to fix FTBFS
- Reduce debug level on 32-bit ARM to try to avoid memory exhaustion

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0r2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0r2-6
- Rebuilt for Boost 1.63

* Sat Jan 21 2017 Jerry James <loganjerry@gmail.com> - 3.0r2-5
- Help polymake find the LattE and 4ti2 tools
- Add Requires needed for polymake to compile tools at runtime (bz 1414594)
- Merge polymake-devel into main package, needed to build tools at runtime
- Bring back libpolymake-apps, needed by Singular 4 (bz 1389956)

* Mon Jan 16 2017 Jerry James <loganjerry@gmail.com> - 3.0r2-4
- Rebuild for perl 5.24.1

* Wed Jan 11 2017 Jerry James <loganjerry@gmail.com> - 3.0r2-3
- Add -magic, -ppl, and -endian patches to fix build problems
- Add the option to build with a bundled version of jreality

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 3.0r2-3
- Rebuild for eigen3-3.3.1

* Fri Nov  4 2016 Jerry James <loganjerry@gmail.com> - 3.0r2-2
- Do not ship libpolymake-apps (bz 1389956)
- Suggest sketch

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 3.0r2-1
- New upstream release

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 3.0r1-5
- Rebuild for lrslib 062 and sympol 0.1.9

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.0r1-4
- Perl 5.24 rebuild

* Tue May  3 2016 Jerry James <loganjerry@gmail.com> - 3.0r1-3
- Rebuild for perl 5.22.2

* Thu Apr 28 2016 Jerry James <loganjerry@gmail.com> - 3.0r1-2
- Build against nauty instead of bliss

* Tue Apr 12 2016 Jerry James <loganjerry@gmail.com> - 3.0r1-1
- New upstream release
- Add Recommends and Suggests for optional tools
- Bundle libnormaliz for now until the system version can catch up

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14r1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.14r1-5
- Rebuilt for Boost 1.60

* Tue Dec 15 2015 Jerry James <loganjerry@gmail.com> - 2.14r1-4
- Rebuild for perl 5.22.1

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 2.14r1-3
- Rebuild for lrslib 061

* Sat Oct  3 2015 Jerry James <loganjerry@gmail.com> - 2.14r1-2
- Fix Requires snafu that made the package uninstallable

* Fri Oct  2 2015 Jerry James <loganjerry@gmail.com> - 2.14r1-1
- The 2.15 branch is not ready; go back to the latest 2.14 release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.15-0.2.beta2
- Rebuilt for Boost 1.59

* Wed Aug 26 2015 Tom Callaway <spot@fedoraproject.org> - 2.15-0.1.beta2
- update to 2.15-beta2 for newer perl support

* Mon Aug 10 2015 Tom Callaway <spot@fedoraproject.org> - 2.14-1
- update to 2.14

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-26.git20141013
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.13-25.git20141013
- rebuild for Boost 1.58

* Tue Jun 23 2015 Jerry James <loganjerry@gmail.com> - 2.13-24.git20141013
- Add -perl522 patch to fix the build

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-24.git20141013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-23.git20141013
- Perl 5.22 rebuild
- Disable BR Singular-devel

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 2.13-22.git20141013
- Rebuild for cddlib 094h

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.13-21.git20141013
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jerry James <loganjerry@gmail.com> - 2.13-20.git20141013
- Rebuild with Singular support

* Fri Mar  6 2015 Jerry James <loganjerry@gmail.com> - 2.13-19.git20141013
- Add -gcc5 patch
- Disable hardening flags, which kill RTLD_LAZY
- Don't try to fix undefined symbols in the plugins anymore

* Thu Mar 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-19.git20141013
- Rebuild for perl 5.20.2

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 2.13-18.git20141013
- Bump for rebuild.

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 2.13-17.git20141013
- Rebuild for eigen3 3.2.4, lrslib 0.5.1, and normaliz 2.12.2

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 2.13-16.git20141013
- Rebuild for boost 1.57.0

* Mon Jan 19 2015 Jerry James <loganjerry@gmail.com> - 2.13-15.git20141013
- Add -exit patch to fix crash on exit

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 2.13-14.git20141013
- Rebuild for eigen3 3.2.3

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 2.13-13.git20141013
- Rebuild with Singular support

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 2.13-12.git20141013
- Update to latest perpetual beta snapshot

* Tue Sep 16 2014 Jerry James <loganjerry@gmail.com> - 2.13-11.git20140811
- Rebuild with Singular support

* Tue Sep 16 2014 Jerry James <loganjerry@gmail.com> - 2.13-10.git20140811
- Rebuild for perl 5.20.1
- New -singular subpackage to reduce pain of Singular+polymake updates

* Thu Sep 11 2014 Jerry James <loganjerry@gmail.com> - 2.13-9.git20140811
- Rebuild with Singular support

* Thu Sep 11 2014 Jerry James <loganjerry@gmail.com> - 2.13-8.git20140811
- Update to perpetual beta snapshot that supports perl 5.20 (bz 1139212)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-8
- Perl 5.20 rebuild
- Disable BR Singular-devel when perl bootstrapping

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug  8 2014 Jerry James <loganjerry@gmail.com> - 2.13-6
- Rebuild with Singular support

* Tue Aug  5 2014 Jerry James <loganjerry@gmail.com> - 2.13-5
- Rebuild for libnormaliz 2.11.2 and eigen3 3.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jerry James <loganjerry@gmail.com> - 2.13-3
- Rebuild for Singular 3-1-6
- Add configuration workarounds for Singular support

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.13-2
- Rebuild for boost 1.55.0

* Tue Apr 29 2014 Jerry James <loganjerry@gmail.com> - 2.13-1
- New upstream release: build against rebuilt Singular

* Tue Apr 29 2014 Jerry James <loganjerry@gmail.com> - 2.13-0
- New upstream release: bootstrap build without Singular support

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 2.12-15.svn20140326
- Update to latest "perpetual beta" for bug fixes
- Add conditional to build without Singular support

* Wed Mar 12 2014 Jerry James <loganjerry@gmail.com> - 2.12-14.svn20131128
- Build with Singular support
- Make transitive dependency on eigen3 (via sympol) explicit

* Sat Jan 18 2014 Jerry James <loganjerry@gmail.com> - 2.12-13.svn20131128
- Update Requires filters

* Fri Jan 17 2014 Jerry James <loganjerry@gmail.com> - 2.12-12.svn20131128
- Update to latest "perpetual beta" for bug fixes
- Enable building new ppl and libnormaliz extensions

* Wed Jan  8 2014 Jerry James <loganjerry@gmail.com> - 2.12-11.svn20130813
- Rebuild for perl 5.18.2
- Add -format patch to fix -Werror=format-security failure

* Wed Aug 14 2013 Jerry James <loganjerry@gmail.com> - 2.12-10.svn20130813
- Update to latest "perpetual beta" for perl 5.18 compatibility (bz 992813)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 2.12-8
- Perl 5.18 rebuild

* Sun Jul 21 2013 Rich Mattes <richmattes@gmail.com> - 2.12-7
- Rebuild for eigen3-3.1.3

* Wed May 15 2013 Jerry James <loganjerry@gmail.com> - 2.12-6
- Require version of perl used to build (bz 963486)
- perl(Term::ReadLine::Gnu) dependency is not autogenerated (bz 963486)

* Wed Mar 20 2013 Jerry James <loganjerry@gmail.com> - 2.12-5
- Add -lrslib patch to fix a segfault (bz 923269)

* Wed Feb 27 2013 Jerry James <loganjerry@gmail.com> - 2.12-4
- Remove rpath and -L%%{_libdir} from polymake-config --ldflags output

* Thu Jan 24 2013 Jerry James <loganjerry@gmail.com> - 2.12-3
- Also need to filter perl(Graphviz)

* Wed Jan 23 2013 Jerry James <loganjerry@gmail.com> - 2.12-2
- Change -libs patch to also remove -rpath arguments
- Filter Provides/Requires to hide private perl interfaces
- Remove the broken check script and explain why

* Thu Jan 10 2013 Jerry James <loganjerry@gmail.com> - 2.12-1
- Initial RPM
