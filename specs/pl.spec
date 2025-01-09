# Name of the architecture-specific lib directory
%global swipl_arch %{_target_cpu}-linux

Name:           pl
Version:        9.2.9
Release:        %autorelease
Summary:        ISO/Edinburgh-style Prolog interpreter

License:        BSD-2-Clause
URL:            https://www.swi-prolog.org/
VCS:            git:https://github.com/SWI-Prolog/swipl.git
# Source0: %%{url}download/stable/src/swipl-%%{version}.tar.gz
# To create the repackaged archive, use ./repackage.sh %%{version}
Source0:        swipl-%{version}_repackaged.tar.gz
Source1:        %{url}download/xpce/doc/userguide/userguide.html.tgz
Source2:        repackage.sh
# Use JNI for Java binding
Patch0:         swipl-8.2.1-Fix-JNI.patch
# Upstream installation paths differ from distribution ones
Patch1:         swipl-8.2.0-Remove-files-locations-from-swipl-1-manual.patch
# Unbundle libstemmer
Patch2:         swipl-8.2.0-unbundle-libstemmer.patch
# Expose inclpr plugin dependency on the math library to RPM
Patch3:         swipl-9.2.7-inclpr-math.patch
# Use zlib-ng directly rather than via the zlib compatibility interface
Patch4:         swipl-9.2.9-zlib-ng.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# Base
BuildRequires:  gmp-devel
BuildRequires:  libatomic
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
# archive
BuildRequires:  pkgconfig(libarchive)
# http
BuildRequires:  js-jquery
# XPCE
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  texinfo-tex
# bdb
BuildRequires:  libdb-devel
# mqi / swiplserver
BuildRequires:  python3-devel
# ODBC
BuildRequires:  pkgconfig(odbc)
# SSL
BuildRequires:  openssl
BuildRequires:  pkgconfig(openssl)
# jpl
%ifarch %{java_arches}
BuildRequires:  java-devel
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.hamcrest:hamcrest)
%endif
# nlp
BuildRequires:  libstemmer-devel
# sweep
BuildRequires:  emacs-devel
# uuid
BuildRequires:  pkgconfig(ossp-uuid)
# win
BuildRequires:  pkgconfig(Qt6)
# yaml
BuildRequires:  pkgconfig(yaml-0.1)
# zlib
BuildRequires:  pkgconfig(zlib-ng)
# Doc building
# Gated to Fedora as EL is currently missing tex(a4wide.sty)
%if 0%{?fedora}
BuildRequires:  tex(latex)
BuildRequires:  tex(a4wide.sty)
BuildRequires:  tex(tabulary.sty)
%endif

%global _desc %{expand:
SWI-Prolog is a fast and powerful ISO/Edinburgh-style Prolog compiler with a
rich set of built-in predicates.  It offers a fast, robust and small
environment which enables substantial applications to be developed with it.

SWI-Prolog additionally offers:

* A powerful module system
* Garbage collection
* Unicode character set handling
* Unbounted integer and rational number arithmetic
* Multithreading support
* A powerful C/C++ interface
* GNU Readline interface
}

%description %_desc

# Not compiled into a binary package:
#External: repackage.sh                 GPL-2.0-or-later
#bench/                                 Various licenses
#packages/RDF/configure                 FSFUL
#packages/clib/configure                FSFUL
#packagfes/clib/demo/                   Public Domain
#packages/clpqr/.fileheader             GPL-2.0-or-later with SWI exception
#packages/clpqr/configure               FSFUL
#packages/cpp/configure                 FSFUL
#packages/http/examples/                LicenseRef-Fedora-Public-Domain
#packages/http/web/js/jquery*           MIT
#packages/nlp/configure                 FSFUL
#packages/pcre/cmake/FindPCRE.cmake     MIT
#packages/protobufs/configure           FSFUL
#packages/sgml/configure                FSFUL
#packages/ssl/configure                 FSFUL
#packages/ssl/https.pl                  LicenseRef-Fedora-Public-Domain
#packages/stomp/examples/               LicenseRef-Fedora-Public-Domain
#packages/swipy/tests/                  LicenseRef-Fedora-Public-Domain
#packages/utf8proc/LICENSE              MIT AND Unicode-DFS-2015
#packages/utf8proc/data_generator.rb    MIT AND Unicode-DFS-2015
#packages/utf8proc/ruby/gem/LICENSE     MIT AND Unicode-DFS-2015
#packages/xpce/TeX/name.bst             LicenseRef-Bibtex
#packages/xpce/deps/xpm/                X11
#packages/xpce/src/configure            FSFUL
#packages/xpce/src/msw/simx.h           SGI-B-2.0
#packages/xpce/src/msw/xpm.h            SGI-B-2.0
#packages/zlib/configure                FSFUL
#scripts/swipl-bt                       LicenseRef-Fedora-Public-Domain
#src/libbf/cutils.c                     MIT
#src/libbf/cutils.h                     MIT
#src/libbf/libbf.c                      MIT
#src/libbf/libbf.h                      MIT
#src/tools/functions.pm                 LicenseRef-Fedora-Public-Domain
#src/tools/update-deps                  LicenseRef-Fedora-Public-Domain
# Removed from repackaged tar ball, see
# <https://github.com/SWI-Prolog/issues/issues/16>:
#bench/unify.pl                         Free for non-commercial
#bench/simple_analyzer.pl               Free for non-commercial

%package     -n swi-prolog
Summary:        ISO/Edinburgh-style Prolog interpreter
BuildArch:      noarch
Requires:       swi-prolog-doc = %{version}-%{release}
Requires:       swi-prolog-nox = %{version}-%{release}
Requires:       swi-prolog-x = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl < 9.2.9-2
Provides:       pl = %{version}-%{release}
Obsoletes:      pl-devel < 9.2.9-2
Provides:       pl-devel = %{version}-%{release}
Obsoletes:      pl-compat-yap-devel < 9.2.9-2
Provides:       pl-compat-yap-devel = %{version}-%{release}

%description -n swi-prolog %_desc
This is a metapackage, which installs the SWI-Prolog suite, except Java, ODBC,
Berkeley DB support and tests.

%package     -n swi-prolog-full
Summary:        ISO/Edinburgh-style Prolog interpreter - full suite
BuildArch:      noarch
Requires:       swi-prolog = %{version}-%{release}
Requires:       swi-prolog-bdb = %{version}-%{release}
Requires:       swi-prolog-java = %{version}-%{release}
Requires:       swi-prolog-odbc = %{version}-%{release}
Requires:       swi-prolog-win = %{version}-%{release}

%description -n swi-prolog-full %_desc
This is a metapackage, which installs the full SWI-Prolog suite, except tests.

%package     -n swi-prolog-core
# NOTE: There is no swi-prolog-core-devel package.  Instead, the header files
# and other development files are included in this package.  It is a Prolog
# compiler, and therefore is a development package itself.
#
# The project as a whole is distributed under the BSD-2-Clause license.
# These files carry different licenses:
# library/aggregate.pl                   BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
# library/dialect/bim.pl                 LicenseRef-Fedora-Public-Domain
# library/unicode/blocks.pl              BSD-2-Clause AND Unicode-DFS-2016
# src/libbf/mersenne-twister.c           BSD-3-Clause
# src/libbf/mersenne-twister.h           BSD-3-Clause
# src/libtai/                            LicenseRef-Fedora-Public-Domain
# src/minizip/                           Zlib
# src/os/dtoa.c                          dtoa
# src/pl-hash.{c,h}                      LicenseRef-Fedora-Public-Domain
License:        BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain AND Unicode-DFS-2016 AND Zlib AND dtoa
Summary:        ISO/Edinburgh-style Prolog interpreter - core system
Recommends:     swi-prolog-bdb%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-core-packages%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-doc = %{version}-%{release}
Recommends:     swi-prolog-java%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-odbc%{?_isa} = %{version}-%{release}

# Old version of minizip is bundled
Provides:       bundled(minizip) = 1.3.1

%description -n swi-prolog-core %_desc
This package contains the core SWI-Prolog system.

%package     -n swi-prolog-core-packages
# The project as a whole is distributed under the BSD-2-Clause license.
# These files carry different licenses:
# library/ugraphs.pl                     BSD-2-Clause OR Artistic-2.0
# packages/clib/bsd-crypt.c              BSD-3-Clause
# packages/clib/md5.{c,h}                Zlib
# packages/clib/md5passwd.c              Beerware
# packages/clib/sha1/                    Brian-Gladman-3-Clause OR GPL-1.0+
# packages/clpqr/                        GPL-2.0-or-later with SWI-exception
# packages/http/http_server_health.pl    GPL-2.0-or-later with SWI-exception
# packages/http/http_stream.pl           BSD-2-Clause AND MIT
# packages/http/multipart.c              BSD-2-Clause AND MIT
# packages/mqi/python/                   MIT
# packages/nlp/double_metaphone.c        GPL-1.0-or-later OR Artistic-1.0-Perl
# packages/nlp/isub.c                    LGPL-2.0-or-later
# packages/protobufs/interop/google/     BSD-3-Clause
# packages/semweb/md5.{c,h}              Zlib
# packages/semweb/murmur.{c,h}           LicenseRef-Fedora-Public-Domain
# packages/sgml/DTD/                     W3C
# packages/sweep/emacs-module.h          GPL-3.0-or-later
# packages/sweep/sweep.texi              GFDL-1.3-no-invariants-or-later
# packages/utf8proc/                     MIT AND Unicode-DFS-2015
#
# Note that packages/redis/redis.pl was relicensed.  It contains a note about
# the former license (MIT), but is no longer distributed under that license.
License:        BSD-2-Clause AND (Brian-Gladman-3-Clause OR GPL-1.0-or-later) AND (BSD-2-Clause OR Artistic-2.0) AND BSD-3-Clause AND Beerware AND GFDL-1.3-no-invariants-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later with SWI-exception AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND MIT AND Unicode-DFS-2015 AND W3C AND Zlib
Summary:        ISO/Edinburgh-style Prolog interpreter - core packages
Requires:       swi-prolog-core%{?_isa} = %{version}-%{release}
Requires:       js-jquery
Requires:       texlive-base
Recommends:     swi-prolog-bdb%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-doc = %{version}-%{release}
Recommends:     swi-prolog-java%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-odbc%{?_isa} = %{version}-%{release}

# packages/clib and packages/semweb both contain an MD5 implementation
# See https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides
Provides:       bundled(md5-deutsch)

%description -n swi-prolog-core-packages %_desc
This package contains the core SWI-Prolog packages.

%package     -n swi-prolog-nox
# The project as a whole is distributed under the BSD-2-Clause license.
# These files carry different licenses:
# packages/ssl/crypt_blowfish.{c,h}      bcrypt-Solar-Designer
# packages/tipc/tipcutils/tipc-config.c  BSD-3-Clause
License:        BSD-2-Clause AND BSD-3-Clause AND bcrypt-Solar-Designer
Summary:        ISO/Edinburgh-style Prolog interpreter - without X support
Requires:       swi-prolog-core%{?_isa} = %{version}-%{release}
Requires:       swi-prolog-core-packages%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-bdb%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-doc = %{version}-%{release}
Recommends:     swi-prolog-java%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-odbc%{?_isa} = %{version}-%{release}

%description -n swi-prolog-nox %_desc
This package contains a SWI-Prolog installation without GUI components.

%package     -n swi-prolog-x
# The project as a whole is distributed under the BSD-2-Clause license.
# These files carry different licenses:
# packages/xpce/man/course               CC-BY-SA-3.0
# packages/xpce/man/info                 CC-BY-SA-3.0
# packages/xpce/src/gnu/getdate.c        LicenseRef-Fedora-Public-Domain AND
#                                      GPL-2.0-or-later WITH Bison-exception-2.2
# packages/xpce/src/gnu/getdate-source.y LicenseRef-Fedora-Public-Domain
# packages/xpce/src/gnu/y.tab            LicenseRef-Fedora-Public-Domain
# packages/xpce/src/img/gifwrite.c       BSD-2-Clause AND FBM AND HPND-Pbmplus
# packages/xpce/src/img/jdatadst.c       BSD-2-Clause AND IJG
# packages/xpce/src/rgx/                 Spencer-99 AND TCL AND PostgreSQL
# packages/xpce/src/x11/xdnd.{c,h}       LGPL-2.0-or-later
License:        BSD-2-Clause AND CC-BY-SA-3.0 AND FBM AND GPL-2.0-or-later WITH Bison-exception-2.2 AND HPND-Pbmplus AND IJG AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND PostgreSQL AND Spencer-99 AND TCL
Summary:        ISO/Edinburgh-style Prolog interpreter - with X support
Requires:       swi-prolog-nox%{?_isa} = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl-xpce < 9.2.9-2
Provides:       pl-xpce = %{version}-%{release}

%description -n swi-prolog-x %_desc
This package contains XPCE, an object-oriented symbolic programming
environment for user interfaces.  Although XPCE was designed to be
language-independent, it has gained the most popularity with Prolog.  XPCE
follows a rather unique approach for developing GUI applications, as follows:

- Add object layer to Prolog
- High level of abstraction
- Exploit rapid Prolog development cycle
- Platform independent programs

%ifarch %{java_arches}
%package     -n swi-prolog-java
Summary:        Bidirectional interface between SWI-Prolog and Java
Requires:       swi-prolog-nox%{?_isa} = %{version}-%{release}
Requires:       java-headless
Requires:       javapackages-tools

# This can be removed when F45 reaches EOL
Obsoletes:      pl-jpl < 9.2.9-2
Provides:       pl-jpl = %{version}-%{release}

%description -n swi-prolog-java %_desc
This package provides JPL, a library using the SWI-Prolog foreign interface
and the Java Native Interface to provide a bidirectional interface between
Java and Prolog.  Prolog can be embedded in Java, and Java can be embedded in
Prolog.  It provides a reentrant bidirectional interface in both cases.
%endif

%package     -n swi-prolog-odbc
Summary:        SWI-Prolog ODBC interface
Requires:       swi-prolog-nox%{?_isa} = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl-odbc < 9.2.9-2
Provides:       pl-odbc = %{version}-%{release}

%description -n swi-prolog-odbc %_desc
The value of RDMS for Prolog is often overestimated, as Prolog itself can
manage substantial amounts of data.  Nevertheless a Prolog/RDMS interface
provides advantages if data is already provided in an RDMS, data must be
shared with other applications, there are strong persistence requirements or
there is too much data to fit in memory.

The popularity of ODBC makes it possible to design a single foreign-language
module that provides RDMS access for a wide variety of databases on a wide
variety of platforms.  The SWI-Prolog RDMS interface is closely modeled after
the ODBC API.  This API is rather low-level, but defaults and dynamic typing
provided by Prolog give the user quite simple access to RDMS, while the
interface provides the best possible performance given the RDMS independence
constraint.

%package     -n swi-prolog-bdb
Summary:        SWI-Prolog Berkeley DB interface
Requires:       swi-prolog-nox%{?_isa} = %{version}-%{release}

%description -n swi-prolog-bdb %_desc
This package provides a foreign language extension to the Berkeley DB (libdb)
embedded database.

%package     -n swi-prolog-doc
# The project as a whole is distributed under the BSD-2-Clause license.
# These files carry different licenses:
# man/bk9.co                             LPPL-1.3a+
# man/main.doc                           CC-BY-SA-3.0
# man/name.bst                           Knuth-CTAN
# man/swipl.cls                          LPPL-1.3a+
# The PDF of the manual contains embedded fonts with these licenses:
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        BSD-2-Clause AND AGPL-3.0-only AND CC-BY-SA-3.0 AND Knuth-CTAN AND LPPL-1.3a+
Summary:        Documentation and examples for SWI-Prolog
BuildArch:      noarch
Requires:       swi-prolog-core = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl-doc < 9.2.9-2
Provides:       pl-doc = %{version}-%{release}

%description -n swi-prolog-doc %_desc
This package provides documentation and examples.

%package     -n swi-prolog-test
# The project as a whole is distributed under the BSD-2-Clause license.
# These files carry different licenses:
# src/Tests/compile/test_autoload.pl     GPL-2.0-or-later WITH SWI-exception
# src/Tests/core/test_arith.pl           LGPL-2.1-or-later
# src/Tests/core/test_coroutining.pl     BSD-2-Clause AND GPL-2.0-or-later
License:        BSD-2-Clause AND GPL-2.0-or-later AND GPL-2.0-or-later WITH SWI-exception AND LGPL-2.1-or-later
Summary:        Tests and checks for SWI-Prolog
BuildArch:      noarch
Requires:       swi-prolog-nox = %{version}-%{release}

%description -n swi-prolog-test %_desc
This package provides a set of prepared tests and checks for installed
SWI-Prolog systems.  This package is intended for SWI-Prolog development and
is of no use for ordinary users.  If you are not sure if you need this
package, you do not.

%package     -n swi-prolog-win
Summary:        SWI-Prolog GUI interface
Requires:       swi-prolog-core%{?_isa} = %{version}-%{release}

%description -n swi-prolog-win %_desc
This package provides a Qt-based GUI for SWI-Prolog.

%prep
%global docdir doc-install
%autosetup -N -n swipl-%{version}
%patch -P0 -p1 -b .jni
%autopatch -p1 -m1

# Fix the installation path on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
  sed -e 's,lib\(/\${SWIPL_INSTALL_DIR}\),lib64\1,' \
      -e '/SWIPL_INSTALL_CMAKE_CONFIG_DIR/s/lib/&64/' \
      -i cmake/LocationsPostPorts.cmake
fi

# Unpack the XPCE user guide
mkdir %{docdir}-xpce
pushd %{docdir}-xpce
tar -xzf %{SOURCE1}
mv UserGuide xpce-UserGuide
popd

# Get the Java config sources
cp -p %{SOURCE2} .

# Adjustments to take into account the new location of JNI stuff
sed -i 's#LIBDIR#%{_libdir}#g' packages/jpl/jpl.pl
sed -i.jni -e 's#LIBDIR#"%{_libdir}/swipl-jpl"#g' packages/jpl/src/main/java/org/jpl7/JPL.java

# Build documentation with the original jpl.pl, since the new version refers
# to install paths that don't exist yet; then switch before installing.
cp -p packages/jpl/jpl.pl packages/jpl/jpl.pl.install
cp -p packages/jpl/jpl.pl.jni packages/jpl/jpl.pl

# Do not use the bundled libstemmer
rm -fr packages/nlp/libstemmer_c

# Do not use the bundled texinfo.tex
rm packages/xpce/man/info/texinfo.tex
ln -s %{_texmf}/tex/texinfo/texinfo.tex packages/xpce/man/info

# Avoid a clash on doc names
cp -p customize/README.md README-customize.md

%generate_buildrequires
cd packages/mqi/python
%pyproject_buildrequires

%build
%ifarch %{java_arches}
export JAVA_HOME=%{java_home}
export LD_LIBRARY_PATH=%{java_home}/lib/server
%else
# Processed by packages/configure
export DISABLE_PKGS="jpl"
%endif

# Configure
%cmake \
  -DBUILD_PDF_DOCUMENTATION:BOOL=%{?fedora:ON}%{!?fedora:OFF} \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
  -DCPACK_GENERATOR:STRING=RPM \
  -DINSTALL_TESTS:BOOL=ON \
  -DJQUERYDIR:PATH=%{_datadir}/javascript/jquery/latest \
  -DSKIP_SSL_TESTS:BOOL=ON \
  -DSWIPL_INSTALL_IN_LIB:BOOL=ON \
  -DSWIPL_INSTALL_IN_SHARE:BOOL=ON \
  -DSWIPL_VERSIONED_DIR:BOOL=OFF \
  -DUSE_TCMALLOC:BOOL=ON \
  -G Ninja

# Help latex2html find the bibliographies
for d in $(find . -name gen); do
  target=$(dirname $d)
  mkdir -p %{_vpath_builddir}/$target
  cp -p $d/*.bbl %{_vpath_builddir}/$target
done

# Build
%cmake_build

# Switch back before installing; see above
cp -p packages/jpl/jpl.pl.install packages/jpl/jpl.pl

%install
# See <http://www.swi-prolog.org/build/guidelines.html> for file layout
%cmake_install

# Scripts with shebang should be executable
chmod 0755 \
  %{buildroot}%{_datadir}/swipl/doc/packages/examples/http/linux-init-script \
  %{buildroot}%{_datadir}/swipl/doc/packages/examples/jpl/java/zahed/run.sh \
  %{buildroot}%{_datadir}/swipl/doc/packages/examples/pldoc/man_server.pl \
  %{buildroot}%{_datadir}/swipl/doc/packages/examples/protobufs/interop/test_read.py \
  %{buildroot}%{_datadir}/swipl/doc/packages/examples/protobufs/interop/test_write.py \
  %{buildroot}%{_datadir}/swipl/doc/packages/examples/stomp/server-loop.sh \
  %{buildroot}%{_libdir}/swipl/customize/edit \
  %{buildroot}%{_libdir}/swipl/library/dialect/sicstus/swipl-lfr.pl \
  %{buildroot}%{_libdir}/swipl/test/Tests/xsb/delay_tests/*.sh \
  %{buildroot}%{_libdir}/swipl/test/Tests/xsb/ptq/*.sh \
  %{buildroot}%{_libdir}/swipl/test/Tests/xsb/wfs_tests/*.sh

# Some XPCE files do not get installed
cp -p packages/xpce/man/*.1 %{buildroot}%{_mandir}/man1
cp -a packages/xpce/man/course %{buildroot}%{_libdir}/swipl/xpce/man

# Let LaTeX know about the style file
mkdir -p %{buildroot}%{_texmf}/tex/latex/swi-prolog
ln -s %{_libdir}/swipl/library/ext/pldoc/pldoc/pldoc.sty \
      %{buildroot}%{_texmf}/tex/latex/swi-prolog/pldoc.sty

# Install the sweep info file
mkdir -p %{buildroot}%{_infodir}
cd packages/sweep
makeinfo sweep.texi
cp -p sweep.info %{buildroot}%{_infodir}
cd -

# Fix the pkgconfig file
sed -i 's,/usr//usr,/usr,' %{buildroot}%{_datadir}/pkgconfig/swipl.pc

%ifarch %{java_arches}
# Move the JPL JNI stuff to where the Java packaging guidelines 
# say it should be
jpl_ver=$(sed -n 's/.*JPL_VERSION \([.[:digit:]]*\).*/\1/p' packages/jpl/CMakeLists.txt)

mkdir -p %{buildroot}%{_libdir}/swipl-jpl
mv %{buildroot}%{_libdir}/swipl/lib/%{swipl_arch}/libjpl.so \
   %{buildroot}%{_libdir}/swipl-jpl

mkdir -p %{buildroot}%{_jnidir}
mv %{buildroot}%{_libdir}/swipl/lib/jpl.jar %{buildroot}%{_jnidir}
ln -s ../../lib/java/jpl.jar %{buildroot}%{_libdir}/swipl-jpl

# Original locations are referenced by internal libraries and examples
cd %{buildroot}%{_libdir}
ln -s ../../../swipl-jpl/libjpl.so swipl/lib/%{swipl_arch}/libjpl.so
ln -s ../../swipl-jpl/jpl.jar swipl/lib/jpl.jar
cd -
%endif

# Remove stuff we do not want to package
rm %{buildroot}%{_libdir}/swipl/{LICENSE,README.md}
rm %{buildroot}%{_libdir}/swipl/customize/README.md
rm %{buildroot}%{_libdir}/swipl/lib/swiplserver/LICENSE
rm %{buildroot}%{_libdir}/swipl/test/Tests/xsb/.gitignore
rm %{buildroot}%{_libdir}/swipl/xpce/man/course/.gitignore

# Link duplicates
%fdupes %{buildroot}%{_datadir}/swipl
%fdupes %{buildroot}%{_libdir}/swipl

%check
# Test with the original jpl.pl, since the new version refers to paths that
# don't exist; then switch back.
cp -p packages/jpl/jpl.pl.jni packages/jpl/jpl.pl
%ctest
cp -p packages/jpl/jpl.pl.install packages/jpl/jpl.pl

%files -n swi-prolog

%files -n swi-prolog-full

%files -n swi-prolog-core
%license LICENSE
%doc README.md README-customize.md
%{_bindir}/swipl
%{_bindir}/swipl-ld
%{_libdir}/cmake/swipl/
%dir %{_libdir}/swipl/
%dir %{_libdir}/swipl/bin/
%{_libdir}/swipl/bin/swipl.home
%dir %{_libdir}/swipl/bin/%{swipl_arch}/
%{_libdir}/swipl/bin/%{swipl_arch}/swipl
%{_libdir}/swipl/bin/%{swipl_arch}/swipl-ld
%{_libdir}/swipl/boot/
%{_libdir}/swipl/boot.prc
%{_libdir}/swipl/cmake/
%{_libdir}/swipl/customize/
%{_libdir}/swipl/demo/
%dir %{_libdir}/swipl/include/
%{_libdir}/swipl/include/SWI-Prolog.h
%{_libdir}/swipl/include/SWI-Stream.h
%{_libdir}/swipl/include/Yap/
%{_libdir}/swipl/include/sicstus/
%dir %{_libdir}/swipl/library/
%{_libdir}/swipl/library/*.pl
%{_libdir}/swipl/library/*.qlf
%{_libdir}/swipl/library/build/
%{_libdir}/swipl/library/clp/
%{_libdir}/swipl/library/dcg/
%{_libdir}/swipl/library/dialect/
%{_libdir}/swipl/library/iri_scheme/
%{_libdir}/swipl/library/lynx/
%{_libdir}/swipl/library/theme/
%{_libdir}/swipl/library/unicode/
%{_libdir}/swipl/swipl.home
%{_libdir}/libswipl.so.9*
%{_libdir}/libswipl.so
%{_mandir}/man1/swipl*
%{_datadir}/pkgconfig/swipl.pc
%{_infodir}/sweep.info*

%files -n swi-prolog-core-packages
%{_libdir}/swipl/bin/latex2html
%{_libdir}/swipl/include/SWI-cpp.h
%{_libdir}/swipl/include/SWI-cpp2*
%dir %{_libdir}/swipl/lib/
%{_libdir}/swipl/lib/swiplserver/
%dir %{_libdir}/swipl/lib/%{swipl_arch}/
%{_libdir}/swipl/lib/%{swipl_arch}/cgi.so
%{_libdir}/swipl/lib/%{swipl_arch}/crypt.so
%{_libdir}/swipl/lib/%{swipl_arch}/double_metaphone.so
%{_libdir}/swipl/lib/%{swipl_arch}/files.so
%{_libdir}/swipl/lib/%{swipl_arch}/hashstream.so
%{_libdir}/swipl/lib/%{swipl_arch}/http_stream.so
%{_libdir}/swipl/lib/%{swipl_arch}/inclpr.so
%{_libdir}/swipl/lib/%{swipl_arch}/isub.so
%{_libdir}/swipl/lib/%{swipl_arch}/janus.so
%{_libdir}/swipl/lib/%{swipl_arch}/json.so
%{_libdir}/swipl/lib/%{swipl_arch}/mallocinfo.so
%{_libdir}/swipl/lib/%{swipl_arch}/md54pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/memfile.so
%{_libdir}/swipl/lib/%{swipl_arch}/ntriples.so
%{_libdir}/swipl/lib/%{swipl_arch}/pdt_console.so
%{_libdir}/swipl/lib/%{swipl_arch}/porter_stem.so
%{_libdir}/swipl/lib/%{swipl_arch}/process.so
%{_libdir}/swipl/lib/%{swipl_arch}/prolog_stream.so
%{_libdir}/swipl/lib/%{swipl_arch}/protobufs.so
%{_libdir}/swipl/lib/%{swipl_arch}/rdf_db.so
%{_libdir}/swipl/lib/%{swipl_arch}/readutil.so
%{_libdir}/swipl/lib/%{swipl_arch}/redis4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/rlimit.so
%{_libdir}/swipl/lib/%{swipl_arch}/sched.so
%{_libdir}/swipl/lib/%{swipl_arch}/sgml2pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/sha4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/snowball.so
%{_libdir}/swipl/lib/%{swipl_arch}/socket.so
%{_libdir}/swipl/lib/%{swipl_arch}/streaminfo.so
%{_libdir}/swipl/lib/%{swipl_arch}/sweep-module.so
%{_libdir}/swipl/lib/%{swipl_arch}/syslog.so
%{_libdir}/swipl/lib/%{swipl_arch}/table.so
%{_libdir}/swipl/lib/%{swipl_arch}/test_cpp.so
%{_libdir}/swipl/lib/%{swipl_arch}/test_ffi.so
%{_libdir}/swipl/lib/%{swipl_arch}/tex.so
%{_libdir}/swipl/lib/%{swipl_arch}/time.so
%{_libdir}/swipl/lib/%{swipl_arch}/turtle.so
%{_libdir}/swipl/lib/%{swipl_arch}/uid.so
%{_libdir}/swipl/lib/%{swipl_arch}/unicode4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/unix.so
%{_libdir}/swipl/lib/%{swipl_arch}/uri.so
%{_libdir}/swipl/lib/%{swipl_arch}/uuid.so
%{_libdir}/swipl/lib/%{swipl_arch}/websocket.so
%{_libdir}/swipl/lib/%{swipl_arch}/zlib4pl.so
%dir %{_libdir}/swipl/library/ext/
%{_libdir}/swipl/library/ext/PDT/
%{_libdir}/swipl/library/ext/RDF/
%{_libdir}/swipl/library/ext/chr/
%{_libdir}/swipl/library/ext/clib/
%{_libdir}/swipl/library/ext/clpqr
%{_libdir}/swipl/library/ext/http/
%{_libdir}/swipl/library/ext/inclpr/
%{_libdir}/swipl/library/ext/ltx2htm/
%{_libdir}/swipl/library/ext/mqi/
%{_libdir}/swipl/library/ext/nlp/
%{_libdir}/swipl/library/ext/paxos/
%{_libdir}/swipl/library/ext/pengines/
%{_libdir}/swipl/library/ext/pldoc/
%{_libdir}/swipl/library/ext/plunit/
%{_libdir}/swipl/library/ext/protobufs/
%{_libdir}/swipl/library/ext/redis/
%{_libdir}/swipl/library/ext/semweb/
%{_libdir}/swipl/library/ext/sgml/
%{_libdir}/swipl/library/ext/stomp/
%{_libdir}/swipl/library/ext/sweep/
%{_libdir}/swipl/library/ext/swipy/
%{_libdir}/swipl/library/ext/table/
%{_libdir}/swipl/library/ext/utf8proc/
%{_libdir}/swipl/library/ext/zlib/
%{_libdir}/swipl/library/http/
%{_libdir}/swipl/library/protobufs/
%{_libdir}/swipl/library/semweb/
%{_texmf}/tex/latex/swi-prolog/

%files -n swi-prolog-nox
%{_libdir}/swipl/app/
%{_libdir}/swipl/lib/%{swipl_arch}/archive4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/crypto4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/libedit4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/pcre4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/readline4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/ssl4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/tipc.so
%{_libdir}/swipl/lib/%{swipl_arch}/yaml4pl.so
%{_libdir}/swipl/library/ext/archive/
%{_libdir}/swipl/library/ext/libedit/
%{_libdir}/swipl/library/ext/pcre/
%{_libdir}/swipl/library/ext/readline/
%{_libdir}/swipl/library/ext/ssl/
%{_libdir}/swipl/library/ext/tipc/
%{_libdir}/swipl/library/ext/yaml/

%files -n swi-prolog-x
%doc packages/xpce/{CUSTOMISE,EXTENDING,README}.md
%{_libdir}/swipl/lib/%{swipl_arch}/pl2xpce.so
%{_libdir}/swipl/swipl.rc
%{_libdir}/swipl/xpce/
%{_mandir}/man1/xpce-client.1*

%ifarch %{java_arches}
%files -n swi-prolog-java
%doc packages/jpl/README.md
%{_jnidir}/jpl.jar
%{_libdir}/swipl/lib/jpl*jar
%{_libdir}/swipl/lib/%{swipl_arch}/libjpl.so
%{_libdir}/swipl/library/ext/jpl/
%{_libdir}/swipl-jpl/
%endif

%files -n swi-prolog-odbc
%doc packages/odbc/README
%{_libdir}/swipl/lib/%{swipl_arch}/odbc4pl.so
%{_libdir}/swipl/library/ext/cql/
%{_libdir}/swipl/library/ext/odbc/

%files -n swi-prolog-bdb
%doc packages/bdb/README.md
%{_libdir}/swipl/lib/%{swipl_arch}/bdb4pl.so
%{_libdir}/swipl/library/ext/bdb/

%files -n swi-prolog-doc
%if 0%{?fedora}
%doc %{_vpath_builddir}/man/SWI-Prolog-%{version}.pdf
%endif
%{_datadir}/swipl/

%files -n swi-prolog-test
%{_libdir}/swipl/test/

%files -n swi-prolog-win
%doc packages/swipl-win/README.md
%{_bindir}/swipl-win
%{_libdir}/swipl/bin/%{swipl_arch}/swipl-win
%{_libdir}/swipl/swipl-win.rc

%changelog
%autochangelog
