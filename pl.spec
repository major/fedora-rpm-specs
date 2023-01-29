# TESTING NOTE: The tests can be run by executing ctest in the build directory.
# However, some tests are guaranteed to fail when built by koji:
# - Those that require a network: http:http, semweb:load, ssl:ssl
# - Those that require JNI: jpl:prolog_in_java, jpl:java_in_prolog
# Also, the zlib:zlib test requires a Unicode locale (via the LC_ALL or LANG
# environment variables).  For example:
# export LC_ALL=C.UTF-8

%global separate_xpce 1

# Name of the architecture-specific lib directory
%ifarch %{arm}
%global swipl_arch armv7l-linux
%else
%global swipl_arch %{_target_cpu}-linux
%endif

Name:       pl
Version:    9.0.4
Release:    1%{?dist}
Summary:    SWI-Prolog - Edinburgh compatible Prolog compiler
#LICENSE:                               BSD-2-Clause
#library/dialect/iso/iso_predicates.pl  BSD-2-Clause AND (GPL-2.0-or-later WITH
#                                       SWI-Prolog extra clause or Artistic-2.0)
#library/ugraphs.pl                     BSD-2-Clause AND (GPL-2.0-or-later WITH
#                                       SWI-Prolog extra clause or Artistic-2.0)
#library/unicode/blocks.pl              BSD-2-Clause AND Unicode-DFS-2016
#man/main.doc                           CC-BY-SA-3.0
#man/swipl.cls                          LPPL-1.2
#packages/bdb/bdb4pl.doc                Sleepycat (due to linking with libdb)
#packages/clib/bsd-crypt.c              BSD-3-Clause
#packages/clib/clib.doc                 (BSD-3-Clause OR GPL-1.0-or-later) AND
#                                       BSD-3-Clause
#packages/clib/md5.c                    Zlib
#packages/clib/md5.h                    Zlib
#packages/clib/md5passwd.c              Beerware
#packages/clib/sha1/brg_endian.h        BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/brg_types.h         BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/hmac.c              BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/hmac.h              BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/pwd2key.c           BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/pwd2key.h           BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/sha1.c              BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/sha1.h              BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/sha1b.c             BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/sha2.c              BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/sha2.h              BSD-like (?) OR GPL-1.0-or-later
#packages/clib/sha1/sha2b.c             BSD-like (?) OR GPL-1.0-or-later
#packages/clpqr/clpq.pl                 GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/bb_q.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/bv_q.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/fourmotz_q.pl      GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/ineq_q.pl          GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/itf_q.pl           GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/nf_q.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpq/store_q.pl         GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/class.pl          GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/clpq.pl           GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/dump.pl           GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/geler.pl          GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/itf.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/ordering.pl       GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/project.pl        GPL-2.0-or-later with SWI exception
#packages/clpqr/clpqr/redund.pl         GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr.pl                 GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/bb_r.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/bv_r.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/fourmotz_r.pl      GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/ineq_r.pl          GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/itf_r.pl           GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/nf_r.pl            GPL-2.0-or-later with SWI exception
#packages/clpqr/clpr/store_r.pl         GPL-2.0-or-later with SWI exception
#packages/mqi/python/                   MIT
#packages/nlp/double_metaphone.c        GPL-1.0-or-later OR Artistic-1.0-Perl
#packages/nlp/isub.c                    LGPL-2.0-or-later
#packages/plunit/swi.pl                 BSD-2-Clause and (GPL-2.0-or-later WITH
#                                       SWI-Prolog extra clause OR Artistic-2.0)
#packages/protobufs/interop/google/     BSD-3-Clause
#packages/semweb/md5.c                  Zlib
#packages/semweb/md5.h                  Zlib
#packages/semweb/murmur.c               LicenseRef-Fedora-Public-Domain
#packages/semweb/murmur.h               LicenseRef-Fedora-Public-Domain
#packages/tipc/tipcutils/tipc-config.c  BSD-3-Clause
#packages/utf8proc/pgsql/utf8proc_pgsql.c MIT
#packages/utf8proc/ruby/utf8proc_native.c MIT
#packages/utf8proc/ruby/utf8proc_rb.c   MIT
#packages/utf8proc/utf8proc.c           MIT
#packages/utf8proc/utf8proc.doc         MIT AND Unicode-DFS-2015
#packages/utf8proc/utf8proc.h           MIT
#packages/utf8proc/utf8proc_data.c      Unicode-DFS-2015
#packages/xpce/src/gnu/getdate-source.y LicenseRef-Fedora-Public-Domain
#packages/xpce/src/gnu/getdate.c        LicenseRef-Fedora-Public-Domain AND
#                                      GPL-2.0-or-later WITH Bison-exception-2.2
#packages/xpce/src/gnu/y.tab            LicenseRef-Fedora-Public-Domain
#packages/xpce/src/img/gifwrite.c       Part is free for any purpose (?)
#packages/xpce/src/rgx/                 Spencer-99 AND TCL
#packages/xpce/src/x11/xdnd.h           GPL-2.0-or-later
#scripts/swipl-bt                       LicenseRef-Fedora-Public-Domain
#src/minizip/                           Zlib
#src/os/dtoa.c                          MIT-like (?)
#src/pl-hash.c                          LicenseRef-Fedora-Public-Domain
#src/pl-hash.h                          LicenseRef-Fedora-Public-Domain
#src/swipl-ld.1                         LGPL-2.0-or-later
#src/tools/functions.pm                 LicenseRef-Fedora-Public-Domain

# Not compiled into a binary package:
#External: JavaConfig.java              GPL-3.0-or-later
#External: repackage.sh                 GPL-2.0-or-later
#bench/chat_parser.pl                   MIT
#packages/RDF/configure                 FSFUL
#packages/clib/configure                FSFUL
#packages/clpqr/.fileheader             GPL-2.0-or-later with SWI exception
#packages/clpqr/configure               FSFUL
#packages/cpp/configure                 FSFUL
#packages/http/examples/calc.pl         LicenseRef-Fedora-Public-Domain
#packages/http/web/js/jquery*           MIT
#packages/nlp/configure                 FSFUL
#packages/pcre/cmake/FindPCRE.cmake     MIT
#packages/protobufs/configure           FSFUL
#packages/sgml/configure                FSFUL
#packages/ssl/configure                 FSFUL
#packages/stomp/examples/ping.pl        LicenseRef-Fedora-Public-Domain
#packages/stomp/examples/pong.pl        LicenseRef-Fedora-Public-Domain
#packages/stomp/examples/simple.pl      LicenseRef-Fedora-Public-Domain
#packages/swipl-win/README.md           LGPL-2.1-only
#packages/utf8proc/LICENSE              MIT AND Unicode-DFS-2015
#packages/utf8proc/data_generator.rb    MIT AND Unicode-DFS-2015
#packages/utf8proc/ruby/gem/LICENSE     MIT AND Unicode-DFS-2015
#packages/xpce/TeX/name.bst             LicenseRef-Bibtex
#packages/xpce/man/info/texinfo.tex     GPL-2.0-or-later
#packages/xpce/src/configure            FSFUL
#packages/xpce/src/msw/simx.h           SGI-B-2.0
#packages/xpce/src/msw/xpm.h            SGI-B-2.0
#packages/zlib/configure                FSFUL
#src/libbf/cutils.c                     MIT
#src/libbf/cutils.h                     MIT
#src/libbf/libbf.c                      MIT
#src/libbf/libbf.h                      MIT
#src/libbf/mersenne-twister.c           BSD-3-Clause
#src/libbf/mersenne-twister.h           BSD-3-Clause
#src/Tests/                             BSD-2-Clause AND GPL-2.0-or-later WITH
#                                       SWI-Prolog extra clause
#src/tools/update-deps                  LicenseRef-Fedora-Public-Domain
# Removed from repackaged tar ball, see
# <https://github.com/SWI-Prolog/issues/issues/16>:
#bench/unify.pl                         Free for non-commercial
#bench/simple_analyzer.pl               Free for non-commercial
License:    BSD-2-Clause AND BSD-3-Clause AND (BSD-3-Clause OR GPL-1.0-or-later) AND Beerware AND CC-BY-SA-3.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later AND (GPL-2.0-or-later OR Artistic-2.0) AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND LPPL-1.2 AND MIT AND Sleepycat AND Unicode-DFS-2015 AND Unicode-DFS-2016 AND Zlib
URL:        https://www.swi-prolog.org/
# Source0: %%{url}download/stable/src/swipl-%%{version}.tar.gz
# To create the repackaged archive, use ./repackage.sh %%{version}
Source0:    swipl-%{version}_repackaged.tar.gz
Source1:    %{url}download/xpce/doc/userguide/userguide.html.tgz
Source2:    JavaConfig.java
Source3:    repackage.sh
# Use JNI for Java binding
Patch0:     swipl-8.2.1-Fix-JNI.patch
# Upstream installation paths differ from distribution ones
Patch1:     swipl-8.2.0-Remove-files-locations-from-swipl-1-manual.patch
# Unbundle libstemmer
Patch2:     swipl-8.2.0-unbundle-libstemmer.patch

BuildRequires:  cmake
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# Base
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(ncurses)
%if 0%{?el8}
# on el8 readline isn't picked up by pkgconfig
BuildRequires:  readline-devel
%else
BuildRequires:  pkgconfig(readline)
%endif
# archive
BuildRequires:  pkgconfig(libarchive)
# http
BuildRequires:  js-jquery
# XPCE
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
# Freetype support in XPCE
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrender)
# bdb
BuildRequires:  libdb-devel
# mqi / swiplserver
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}
# ODBC
BuildRequires:  pkgconfig(odbc)
# SSL
BuildRequires:  openssl
BuildRequires:  pkgconfig(openssl)
# jpl
%ifarch %{java_arches}
BuildRequires:  java-devel
BuildRequires:  junit
%endif
# nlp
BuildRequires:  libstemmer-devel
# uuid
BuildRequires:  pkgconfig(ossp-uuid)
# win
BuildRequires:  pkgconfig(Qt5)
# yaml
BuildRequires:  pkgconfig(yaml-0.1)
# zlib
BuildRequires:  pkgconfig(zlib)
# Doc building
# Gated to Fedora as EL is currently missing tex(a4wide.sty)
%if 0%{?fedora}
BuildRequires:  tex(latex)
BuildRequires:  tex(a4wide.sty)
BuildRequires:  tex(tabulary.sty)
%endif
# http
Requires:       js-jquery

# Old version of minizip is bundled
Provides:       bundled(minizip) = 1.2.11

# See https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides
Provides:       bundled(md5-deutsch)

# This can be removed when F40 reaches EOL
%ifnarch %{java_arches}
Obsoletes: pl-java < 8.4.3-2
%endif

%description
ISO/Edinburgh-style Prolog compiler including modules, auto-load,
libraries, Garbage-collector, stack-expandor, C/C++-interface,
GNU-readline interface, very fast compiler.  Including packages clib
(Unix process control and sockets), cpp (C++ interface), sgml (reading
XML/SGML), sgml/RDF (reading RDF into triples).
%if %{separate_xpce}
XPCE (Graphics UI toolkit, integrated editor (Emacs-clone) and source-level
debugger) is available in %{name}-xpce package.
%else
Also XPCE (Graphics UI toolkit, integrated editor (Emacs-clone) and
source-level debugger) is included.
%endif


%package devel
Summary:  Development files for SWI Prolog
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc
Requires: pkgconfig%{?_isa}
Requires: readline-devel%{?_isa}

%description devel
Development files for SWI Prolog.


%package compat-yap-devel
Summary:  Development files building YAP application against SWI Prolog
License:  BSD-2-Clause
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description compat-yap-devel
This package allows to build Yet Annother Prolog applications against SWI
Prolog implementation.


%package doc
Summary:  Documentation for SWI Prolog
License:  BSD-2-Clause
# This must be architecture dependent because some files live in %%{_libdir}
# because they are used by built-in documentation system.
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
%{summary}.


%package odbc
Summary:  SWI-Prolog ODBC interface
License:  BSD-2-Clause
Requires: %{name}%{?_isa} = %{version}-%{release}

%description odbc
The value of RDMS for Prolog is often over-estimated, as Prolog itself can
manage substantial amounts of data. Nevertheless a Prolog/RDMS interface
provides advantages if data is already provided in an RDMS, data must be
shared with other applications, there are strong persistency requirements
or there is too much data to fit in memory.                                  
                                                                            
The popularity of ODBC makes it possible to design a single
foreign-language module that provides RDMS access for a wide variety of
databases on a wide variety of platforms. The SWI-Prolog RDMS interface is
closely modeled after the ODBC API. This API is rather low-level, but
defaults and dynamic typing provided by Prolog give the user quite simple
access to RDMS, while the interface provides the best possible performance
given the RDMS independency constraint.   


%if %{separate_xpce}
%package xpce
License:  BSD-2-Clause AND AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Bison-exception-2.2 AND LicenseRef-Fedora-Public-Domain AND Spencer-99 AND TCL
Summary:  A toolkit for developing graphical applications in Prolog
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xpce
XPCE is a toolkit for developing graphical applications in Prolog and other
interactive and dynamically typed languages. XPCE follows a rather unique
approach of for developing GUI applications, as follows:

- Add object layer to Prolog
- High level of abstraction
- Exploit rapid Prolog development cycle
- Platform independent programs
%endif


%ifarch %{java_arches}
%package jpl
License:  BSD-2-Clause
Summary:  A bidirectional Prolog/Java interface for SWI Prolog
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-headless
Requires: javapackages-tools

%description jpl
JPL is a library using the SWI-Prolog foreign interface and the Java Native
Interface providing a bidirectional interface between Java and Prolog
that can be used to embed Prolog in Java as well as for embedding Java
in Prolog. In both setups it provides a re-entrant bidirectional interface.
%endif


%prep
%global docdir doc-install
%autosetup -N -n swipl-%{version}
%patch0 -p1 -b .jni
%autopatch -p1 -m1

# Fix the installation path on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
  sed -e 's,\${CMAKE_INSTALL_PREFIX}/lib,&64,' \
      -e 's,lib\(/\${SWIPL_INSTALL_DIR}\),lib64\1,' \
      -e '/SWIPL_INSTALL_CMAKE_CONFIG_DIR/s/lib/&64/' \
      -i CMakeLists.txt
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

# Find junit.jar
sed --in-place 's,\(%{_datadir}/java/junit\)4\.jar,\1.jar,' \
    packages/jpl/cmake/JUnit.cmake

# Build documentation with the original jpl.pl, since the new version refers
# to install paths that don't exist yet; then switch before installing.
cp -p packages/jpl/jpl.pl packages/jpl/jpl.pl.install
cp -p packages/jpl/jpl.pl.jni packages/jpl/jpl.pl

# Do not use the bundled libstemmer
rm -fr packages/nlp/libstemmer_c

# Avoid a clash on doc names
cp -p customize/README.md README-customize.md


%build
export LC_ALL=C.UTF-8
%ifarch %{java_arches}
javac JavaConfig.java
JAVA_HOME=$(java JavaConfig --home)
JAVA_LIBS=$(java JavaConfig --libs-only-L)
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server
%else
# Processed by packages/configure
export DISABLE_PKGS="jpl"
%endif

# Configure
%cmake \
%if 0%{?fedora}
%ifnarch aarch64
  -DBUILD_PDF_DOCUMENTATION:BOOL=ON \
%else
  -DBUILD_PDF_DOCUMENTATION:BOOL=OFF \
%endif
%else
  -DBUILD_PDF_DOCUMENTATION:BOOL=OFF \
%endif
  -DCPACK_GENERATOR:STRING=RPM \
  -DGET0SIG_CONST_T:STRING=const \
  -DJQUERYDIR:STRING=%{_datadir}/javascript/jquery/latest \
  -DSWIPL_VERSIONED_DIR:BOOL=ON \
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

# Script with shebang should be executable
chmod 0755 %{buildroot}%{_libdir}/swipl-%{version}/library/dialect/sicstus/swipl-lfr.pl
chmod 0755 %{buildroot}%{_libdir}/swipl-%{version}/customize/edit

# Some XPCE files do not get installed
cp -p packages/xpce/man/*.1 %{buildroot}%{_mandir}/man1

%ifarch %{java_arches}
# Move the JPL JNI stuff to where the Java packaging guidelines 
# say it should be
jpl_ver=$(sed -n 's/.*JPL_VERSION \([.[:digit:]]*\).*/\1/p' packages/jpl/CMakeLists.txt)

mkdir -p %{buildroot}%{_libdir}/swipl-jpl
mv %{buildroot}%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/libjpl.so \
   %{buildroot}%{_libdir}/swipl-jpl

mkdir -p %{buildroot}%{_jnidir}
mv %{buildroot}%{_libdir}/swipl-%{version}/lib/jpl.jar %{buildroot}%{_jnidir}
ln -s ../lib/jpl.jar %{buildroot}%{_libdir}/swipl-jpl

# Original locations are referenced by internal libraries and examples
cd %{buildroot}%{_libdir}
ln -s ../../../swipl-jpl/libjpl.so swipl-%{version}/lib/%{swipl_arch}/libjpl.so
ln -s ../../swipl-jpl/jpl.jar swipl-%{version}/lib/jpl.jar
cd -
%endif

# Remove stuff we do not want to package
rm %{buildroot}%{_libdir}/swipl-%{version}/{LICENSE,README.md}
rm %{buildroot}%{_libdir}/swipl-%{version}/customize/README.md
rm %{buildroot}%{_libdir}/swipl-%{version}/lib/swiplserver/LICENSE

# FIXME: src/Tests/transaction/test_transaction_constraints.pl fails on 32-bit
%if 0%{?__isa_bits} == 64
%ifnarch ppc64le
%check
export LC_ALL=C.UTF-8
# Test with the original jpl.pl, since the new version refers to paths that
# don't exist; then switch back.
cp -p packages/jpl/jpl.pl.jni packages/jpl/jpl.pl
%ctest
cp -p packages/jpl/jpl.pl.install packages/jpl/jpl.pl
%endif
%endif

%files
%license LICENSE
%doc README.md README-customize.md
%{_mandir}/man1/swipl*
%{_bindir}/swipl
%{_bindir}/swipl-ld
%dir %{_libdir}/swipl-%{version}/
%dir %{_libdir}/swipl-%{version}/bin/
%{_libdir}/swipl-%{version}/bin/latex2html
%{_libdir}/swipl-%{version}/bin/swipl.home
%dir %{_libdir}/swipl-%{version}/bin/%{swipl_arch}/
%{_libdir}/swipl-%{version}/bin/%{swipl_arch}/swipl
%{_libdir}/swipl-%{version}/bin/%{swipl_arch}/swipl-ld
%{_libdir}/swipl-%{version}/boot*
%{_libdir}/swipl-%{version}/customize/
%{_libdir}/swipl-%{version}/demo/
%dir %{_libdir}/swipl-%{version}/lib/
%dir %{_libdir}/swipl-%{version}/lib/%{swipl_arch}
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/archive4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/bdb4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/cgi.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/crypto4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/crypt.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/double_metaphone.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/files.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/hashstream.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/http_stream.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/inclpr.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/isub.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/json.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/libedit4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/libswipl.so.*
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/mallocinfo.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/md54pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/memfile.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/ntriples.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/pcre4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/pdt_console.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/porter_stem.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/process.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/prolog_stream.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/protobufs.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/rdf_db.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/readline4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/readutil.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/redis4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/rlimit.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/sched.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/sgml2pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/sha4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/snowball.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/socket.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/ssl4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/streaminfo.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/syslog.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/table.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/tex.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/time.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/tipc.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/turtle.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/uid.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/unicode4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/unix.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/uri.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/uuid.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/websocket.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/yaml4pl.so
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/zlib4pl.so
%{_libdir}/swipl-%{version}/lib/swiplserver/
%{_libdir}/swipl-%{version}/library/
%{_libdir}/swipl-%{version}/swipl.home

# Exclude the files that are in the sub-packages
%ifarch %{java_arches}
# JPL
%exclude %{_libdir}/swipl-%{version}/library/jpl.pl
%endif
# ODBC
%exclude %{_libdir}/swipl-%{version}/library/odbc.pl

%if %{separate_xpce}
%files xpce
%doc packages/xpce/CUSTOMISE.md packages/xpce/README.md
%{_bindir}/swipl-win
%{_libdir}/swipl-%{version}/bin/%{swipl_arch}/swipl-win
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/pl2xpce.so
%{_libdir}/swipl-%{version}/swipl.rc
%{_libdir}/swipl-%{version}/swipl-win.rc
%{_libdir}/swipl-%{version}/xpce/
%{_mandir}/man1/xpce*
%endif

%files devel
%{_libdir}/swipl-%{version}/cmake/
%dir %{_libdir}/swipl-%{version}/include/
%{_libdir}/swipl-%{version}/include/sicstus/
%{_libdir}/swipl-%{version}/include/SWI*
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/libswipl.so
%{_libdir}/cmake/swipl/
%{_datadir}/pkgconfig/swipl.pc

%files compat-yap-devel
%{_libdir}/swipl-%{version}/include/Yap/

%files doc
%{_libdir}/swipl-%{version}/doc/
%if 0%{?fedora}
%ifnarch aarch64
%doc %{_vpath_builddir}/man/SWI-Prolog-%{version}.pdf
%endif
%endif
%doc %{docdir}-xpce/*

%files odbc
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/odbc4pl.so
%{_libdir}/swipl-%{version}/library/odbc.pl
%doc packages/odbc/{demo,ChangeLog,README}

%ifarch %{java_arches}
%files jpl
%doc packages/jpl/docs/* packages/jpl/src/examples
%{_jnidir}/jpl.jar
%{_libdir}/swipl-%{version}/lib/jpl*jar
%{_libdir}/swipl-%{version}/lib/%{swipl_arch}/libjpl.so
%{_libdir}/swipl-%{version}/library/jpl.pl
%{_libdir}/swipl-jpl/
%endif


%changelog
* Fri Jan 27 2023 Jerry James <loganjerry@gmail.com> - 9.0.4-1
- Version 9.0.4
- Drop upstreamed C99 patch
- Use a Unicode locale while testing to avoid a failed test
- Disable tests on ppc64le until we can diagnose 1 failed test
- Disable docs on aarch until bz 2165146 is fixed

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 9.0.3-2
- Fix C99 compatibility issues in CMake checks

* Sun Dec 18 2022 Jerry James <loganjerry@gmail.com> - 9.0.3-1
- Version 9.0.3

* Thu Dec 15 2022 Jerry James <loganjerry@gmail.com> - 9.0.2-1
- Version 9.0.2
- Convert License tag to SPDX (with some licenses pending review)
- Add %%check script for 64-bit architectures

* Wed Aug 24 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 8.4.3-4
- Make it buildable for EPEL

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 8.4.3-2
- Do not build pl-jpl for i686 (rhbz#2104088)

* Tue Jun 21 2022 Jerry James <loganjerry@gmail.com> - 8.4.3-1
- Version 8.4.3

* Fri Mar  4 2022 Jerry James <loganjerry@gmail.com> - 8.4.2-2
- Remove . from %%cmake to fix FTBFS

* Mon Feb 14 2022 Jerry James <loganjerry@gmail.com> - 8.4.2-1
- Version 8.4.2

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 8.4.1-3
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Jerry James <loganjerry@gmail.com> - 8.4.1-1
- Version 8.4.1
- Drop upstreamed -pclose patch

* Sat Oct  2 2021 Jerry James <loganjerry@gmail.com> - 8.4.0-1
- Version 8.4.0
- Drop upstreamed -qt-deprecated and -openssl3 patches
- Add -pclose patch to avoid zombie processes

* Thu Sep 16 2021 Jerry James <loganjerry@gmail.com> - 8.2.4-3
- Add -openssl3 patch to fix FTBFS with OpenSSL 3.0.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 8.2.4-3
- Rebuilt with OpenSSL 3.0.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.4-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Jerry James <loganjerry@gmail.com> - 8.2.4-1
- Version 8.2.4
- Drop upstreamed swipl-8.2.2-underscore.patch

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Jerry James <loganjerry@gmail.com> - 8.2.3-1
- Version 8.2.3
- Add swipl-8.2.3-qt-deprecated.patch to silence Qt deprecation warnings

* Tue Oct 27 2020 Jerry James <loganjerry@gmail.com> - 8.2.2-1
- Version 8.2.2
- Remove upstreamed -bad-bibtex-entry patch
- Add -underscore patch to work around LaTeX errors

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 8.2.1-3
- Update for cmake changes in Rawhide

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 8.2.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 29 2020 Jerry James <loganjerry@gmail.com> - 8.2.1-1
- 8.2.1 bump
- Add -bad-bibtex-entry patch

* Tue Jun 16 2020 Jerry James <loganjerry@gmail.com> - 8.2.0-2
- Fix broken symlinks in the jpl subpackage (bz 1847510)

* Thu May 28 2020 Jerry James <loganjerry@gmail.com> - 8.2.0-1
- 8.2.0 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Jerry James <loganjerry@gmail.com> - 8.0.3-1
- 8.0.3 bump (bz 1722172)

* Fri Mar 22 2019 Jerry James <loganjerry@gmail.com> - 8.0.2-1
- 8.0.2 bump (bz 1669571)
- Drop the -static subpackage
- Drop the -jpl-configure, -pc, and -Use-system-js-query patches
- Add -unbundle-libstemmer patch
- Add a check script
- Build the PDF instead of using the one provided by upstream

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.6.4-9
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 7.6.4-7
- Rebuilt for libcrypt.so.2 (#1666033)

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.6.4-6
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Aug 28 2018 Petr Pisar <ppisar@redhat.com> - 7.6.4-5
- Use latest jquery from js-jquery package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 7.6.4-2
- Rebuilt for switch to libxcrypt

* Mon Jan 15 2018 Petr Pisar <ppisar@redhat.com> - 7.6.4-1
- 7.6.4 bump

* Wed Nov 08 2017 Petr Pisar <ppisar@redhat.com> - 7.6.1-1
- 7.6.1 bump
- License changed from ((BSD and (GPLv2+ with exceptions or Artistic 2.0)) and
  (GPL+ or Artistic) and (BSD or GPL) and LGPLv2+ and TCL and UCD and MIT and
  BSD and Public Domain) to ((BSD and (GPLv2+ with exceptions or Artistic 2.0))
  and (GPL+ or Artistic) and (BSD or GPL) and TCL and UCD and MIT and BSD and
  Public Domain)

* Fri Oct 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 7.6.0-1
- 7.6.0 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Petr Pisar <ppisar@redhat.com> - 7.4.2-1
- 7.4.2 bump

* Mon Mar 06 2017 Petr Pisar <ppisar@redhat.com> - 7.4.1-1
- 7.4.1 bump
- License changed from ((GPLv2+ with exceptions or Artistic 2.0) and (GPLv2+
  with exceptions) and (GPLv2 with exception) and (GPL+ or Artistic) and
  LGPLv2+ and LGPLv2 and UCD and (UCD and MIT) and BSD and Public Domain and
  EPL and GPLv2 and GPLv2+ and GPLv3+) to ((BSD and (GPLv2+ with exceptions or
  Artistic 2.0)) and (GPL+ or Artistic) and (BSD or GPL) and LGPLv2+ and TCL
  and UCD and MIT and BSD and Public Domain)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 7.2.3-4
- Rebuild for readline 7.x
- Adapt Java library path to java-1.8.0-openjdk-aarch32 (bug #1412771)

* Wed Apr 13 2016 Petr Pisar <ppisar@redhat.com> - 7.2.3-3
- Correct swipl-ld tool to handle 268-byte long compiler flags (bug #1326581)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Petr Pisar <ppisar@redhat.com> - 7.2.3-1
- 7.2.3 bump

* Thu Jun 25 2015 Petr Pisar <ppisar@redhat.com> - 7.2.2-1
- 7.2.2 bump
- License changed from ((GPLv2+ with exceptions or Artistic 2.0) and (GPLv2+
  with exceptions) and (GPLv2 with exception) and (GPL+ or Artistic) and
  LGPLv2+ and LGPLv2 and UCD and (UCD and MIT) and BSD and Public Domain and
  EPL and GPLv2 and GPLv3+) to ((GPLv2+ with exceptions or Artistic 2.0) and
  (GPLv2+ with exceptions) and (GPLv2 with exception) and (GPL+ or Artistic)
  and LGPLv2+ and LGPLv2 and UCD and (UCD and MIT) and BSD and Public Domain
  and EPL and GPLv2 and GPLv2+ and GPLv3+)

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 7.2.1-3
- Depend on javapackages-tools instead of jpackage-utils to conform to new Java
  guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Petr Pisar <ppisar@redhat.com> - 7.2.1-1
- 7.2.1 bump
- Depend on gcc because glibc-headers package will be removed (bug #1230490)
- Unbundle jquery-1

* Fri Jun 05 2015 Petr Pisar <ppisar@redhat.com> - 7.2.0-1
- 7.2.0 bump
- License changed from ((GPLv2+ with exceptions or Artistic 2.0) and (GPLv2+
  with exceptions) and LGPLv2+ and LGPLv2 and UCD and BSD and Public Domain
  and EPL and GPLv2 and GPLv3+) to ((GPLv2+ with exceptions or Artistic 2.0)
  and (GPLv2+ with exceptions) and (GPLv2 with exception) and (GPL+ or
  Artistic) and LGPLv2+ and LGPLv2 and UCD and (UCD and MIT) and BSD and Public
  Domain and EPL and GPLv2 and GPLv3+)

* Wed Apr 22 2015 Petr Pisar <ppisar@redhat.com> - 6.6.6-6
- Describe XPCE is in pl-xpce (bug #1204623)

* Fri Feb 27 2015 Petr Pisar <ppisar@redhat.com> - 6.6.6-5
- Build binding for libarchive (bug #1195960)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 6.6.6-3
- Fix detection of libjvm on aarch64 (#1112012)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Petr Pisar <ppisar@redhat.com> - 6.6.6-1
- 6.6.6 bump

* Mon Apr 28 2014 Petr Pisar <ppisar@redhat.com> - 6.6.5-1
- 6.6.5 bump

* Mon Mar 24 2014 Petr Pisar <ppisar@redhat.com> - 6.6.4-1
- 6.6.4 bump

* Thu Mar 20 2014 Petr Pisar <ppisar@redhat.com> - 6.6.3-1
- 6.6.3 bump

* Wed Mar 05 2014 Petr Pisar <ppisar@redhat.com> - 6.6.2-1
- 6.6.2 bump
- License changed from ((GPLv2+ with exceptions or Artistic 2.0) and (GPLv2+
  with exceptions) and LGPLv2+ and LGPLv2 and UCD and BSD and Public Domain
  and GPLv2 and GPLv3+) to ((GPLv2+ with exceptions or Artistic 2.0) and (GPLv2+
  with exceptions) and LGPLv2+ and LGPLv2 and UCD and BSD and Public Domain and
  EPL and GPLv2 and GPLv3+)

* Tue Feb 25 2014 Petr Pisar <ppisar@redhat.com> - 6.6.1-2
- Require headless JRE only (bug #1068485)

* Mon Dec 16 2013 Petr Pisar <ppisar@redhat.com> - 6.6.1-1
- 6.6.1 bump

* Mon Dec 02 2013 Petr Pisar <ppisar@redhat.com> - 6.6.0-1
- 6.6.0 bump
- Inhibit format-security compiler warning on custom sscanf() parser
  (bug #1037250)

* Tue Sep 03 2013 Petr Pisar <ppisar@redhat.com> - 6.4.1-1
- 6.4.1 bump
- License changed from ((GPLv2+ or Artistic 2.0) and LGPLv2+ and LGPLv2 and
  GPLv2 and GPLv2+ and UCD and Public Domain and GPLv3+) to ((GPLv2+ with
  exceptions or Artistic 2.0) and (GPLv2+ with exceptions) and LGPLv2+ and
  LGPLv2 and UCD and Public Domain and GPLv3+ and CC-BY-SA)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 6.2.6-2
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan 14 2013 Petr Pisar <ppisar@redhat.com> - 6.2.6-1
- 6.2.6 bump

* Thu Jan 03 2013 Petr Pisar <ppisar@redhat.com> - 6.2.5-1
- 6.2.5 bump

* Thu Dec 13 2012 Petr Pisar <ppisar@redhat.com> - 6.2.4-1
- 6.2.4 bump

* Mon Dec 03 2012 Petr Pisar <ppisar@redhat.com> - 6.2.3-2
- Sub-package YAP compatibility headers because they are not compatible with
  real YAP

* Thu Nov 22 2012 Petr Pisar <ppisar@redhat.com> - 6.2.3-1
- 6.2.3 bump

* Tue Oct 02 2012 Petr Pisar <ppisar@redhat.com> - 6.2.2-1
- 6.2.2 bump

* Mon Sep 10 2012 Petr Pisar <ppisar@redhat.com> - 6.2.1-1
- 6.2.1 bump

* Thu Aug 23 2012 Petr Pisar <ppisar@redhat.com> - 6.2.0-1
- 6.2.0 bump

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-3
- Remove JDK version constrain by hacking JDK paths (bug #740897)

* Fri Mar 09 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-2
- Own jpl.jar file by jpl sub-package only

* Mon Mar 05 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-1
- 6.0.2 bump
- Artistic licensed code dual-lincensed under GPLv2+ or Artistic 2.0 now
- Keep executables as symlinks because interpreter uses the symlink value to
  locate standard library
- xpce is run as swipl now
- Move documentation into separate sub-package
- Move XPCE into separate sub-package
- Move ODBC interface into separate sub-package
- Fix JPL interface (bug #590499)

* Thu Mar 01 2012 Petr Pisar <ppisar@redhat.com> - 6.0.1-1
- 6.0.1 bump
- Clean spec file

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.5-6
- Rebuilt for glibc bug#747377

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.10.5-5
- rebuild with new gmp

* Tue Sep 27 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-4
- Unify java path search (bug #740897)

* Fri Sep 23 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-3
- Correct Java paths on ARM (thanks to David A. Marlin)

* Wed Aug 24 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-2
- Fix segfault in PutImagePixels32() while displaying malformed GIF
  (bug #732952)

* Mon Aug 22 2011 Petr Pisar <ppisar@redhat.com> - 5.10.5-1
- 5.10.5 bump
- Adjust patches and remove merged ones

* Fri Aug 19 2011 Petr Pisar <ppisar@redhat.com> - 5.10.2-4
- Fix CVE-2011-2896 (David Koblas' GIF decoder LZW decoder buffer overflow)
  (bug #727800)
- Fix other GIF decoder bug
  (http://www.swi-prolog.org/bugzilla/show_bug.cgi?id=7#c4)

* Thu Feb 10 2011 Petr Pisar <ppisar@redhat.com> - 5.10.2-3
- Pass -export-dynamic to linker properly

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Petr Pisar <ppisar@redhat.com> - 5.10.2-1
- 5.10.2 bump
- Use DT_RUNPATH instead of pl-5.7.11-rpath.patch
- Adjust jpl-configure.patch to 5.10.2
- Adjust man-files.patch to 5.10.2
- Adjust jni.patch to 5.10.2
- Adjust pc.patch to 5.10.2
- Use make install method for installation
- Adjust license tag to 5.10.2 version (LGPLv2+ added)
- Add executable permission to some files to be properly packaged
- Re-add XPCE user guide

* Wed Dec  8 2010 Petr Pisar <ppisar@redhar.com> - 5.7.11-6
- Inhibit XPCE by macro to silent rpmlint 
- Define implicit attributes for jpl files 
- Expand tabs to spaces to silent rpmlint 
- Remove executable bit from jpl documentation files 
- Fix spelling in package descriptions 
- Strip debuginfo from libpl.so by setting executable bit 
- Change license to reflect reality (yes, Artistic1) 
- Make java part optional

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 5.7.11-5
- rebuilt with new openssl

* Fri Aug 14 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.7.11-4
- move include files to expected place

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.11-2
- Really fix issue with compiling "maildrop" packages

* Mon Jul  6 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.11-1
- Move binaries into /usr/bin directly to fix multilib issues
- Update to latest upstream release
- Use officially-distributed PDF documentation instead of HTML
- Unify Java patches
- Remove strndup package; they fixed it upstream
- Fix compilation of "maildrop" packages
- Give the xpce documentation directory a clearer name
- Removed the FILES section of the man page because it also caused
  multilib conflicts (and was inaccurate anyway)

* Fri Jun 12 2009 Dennis Gilmore <dennis@ausil.us> 5.7.6-5
-dont use a static definition for strndup

* Mon Mar 02 2009 Dennis Gilmore <dennis@ausil.us> 5.7.6-4
- fix JAVA_HOME and JAVA_LIB for sparc arches

* Sun Mar 01 2009 Karsten Hopp <karsten@redhat.com> 5.7.6-3
- fix java LIBDIRS for mainframe, similar to alpha

* Wed Feb 25 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.6-2
- Unify all changes:
  - Fix java LIBDIRS on alpha (Oliver Falk)

* Wed Feb 25 2009 Mary Ellen Foster <mefoster at gmail.com> - 5.7.6-1
- Update to version 5.7
  - Cleaned up virtual machine and compiler
  - Increased performance

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 5.6.60-3
- rebuild with new openssl

* Fri Sep 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.6.60-2
- forgot to remove ANNOUNCE from doc list

* Fri Sep 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.6.60-1
- update to 5.6.60
- use openjdk (FIXME: there may be a way to make this more generic)

* Wed Jul  2 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.57-2
- Build using any Java
- Include patch from SWI for Turkish locale (thanks to Keri Harris)

* Wed Jun 25 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.57-1
- Another update, after vacation

* Mon May 19 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.55-1
- Update to 5.6.55 (wow, fast updates!)
- Un-split xpce for now
- Conditionally build jpl (on Fedora 9 with openjdk, and on 
  Fedora 8 non-ppc with icedtea)

* Wed May 07 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.54-1
- Update to 5.6.54 and prepare to actually push this
- Try splitting xpce into own package

* Tue Apr 15 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.53-1
- Update to 5.6.53 -- fixes ppc64 problems, yay!

* Wed Apr 09 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.52-2
- Put JPL stuff where the new Java packaging guidelines say it should be
  and make all of the necessary adjustments in other files
- Split out "-devel" and "-static" packages per guidelines

* Mon Mar 31 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.52-1
- Switch jpl requirement from IcedTea to OpenJDK and enable it everywhere
- Upgrade to 5.6.52
- Patch jpl configure script to find Java libraries on ppc{64}
- NB: Still broken on ppc64, still trying to figure out why

* Mon Feb 25 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.51-1
- Upgrade to 5.6.51

* Fri Feb 22 2008 Mary Ellen Foster <mefoster at gmail.com> - 5.6.50-1
- Update to 5.6.50
- Enable JPL (as a sub-package) -- NB: it only builds with icedtea for now,
  so we disable that sub-package on ppc64 and ppc for the moment

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.6.47-9
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-8
- compile with -fno-strict-aliasing

* Wed Dec  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-5
- disable jpl for now

* Wed Dec  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-4
- enable shared library building

* Wed Dec  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.47-1
- new release 5.6.47

* Fri Jun  8 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.35-1
- new version 5.6.35
- add requires readline-devel

* Mon Apr 23 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.34-1
- new version 5.6.34

* Fri Feb 23 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.28-1
- new version 5.6.28

* Fri Dec  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.24-1
- new version 5.6.24

* Sun Oct  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.20-1
- new version 5.6.20

* Sat Sep  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.18-1
- updated to 5.6.18

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.16-3
- Rebuild for FE6

* Tue Jul 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.16-1
- new version 5.6.16

* Mon May  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.12-3
- added buildreq for libXinerama-devel

* Mon May  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.12-2
- added patch to compile with xft

* Sun Apr 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.12-1
- new version 5.6.12

* Wed Mar  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.7-1
- new version 5.6.7

* Sat Jan 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.3-1
- new version 5.6.3

* Mon Jan  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.6.0-1
- new version 5.6.0

* Wed Jun 22 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.7-1
- new version 5.4.7

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 5.4.6-9
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb 23 2005 David Woodhouse <dwmw2@infradead.org> - 5.4.6-7
- Fix visibility abuse. This may well fix x86_64 too, so re-enable that.

* Mon Feb 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.6-6
- Exclude x86_64 for now (bugzilla 149038)

* Sun Feb 20 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 5.4.6-5
- Added patch1 for a few multilib Makefile/configure fixes.
- Use %%makeinstall and set libdir in install section.

* Sat Feb 12 2005 Warren Togami <wtogami@redhat.com> - 5.4.6-4
- remove duplicate RPATH patch
- remove Epoch
- remove redundant unixODBC from BR

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.6-2
- Added BuildRequires: unixODBC, unixODBC-devel
- Removed rpath from shared libs: pl-rpath.patch

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.6-1
- New Version 5.4.6

* Thu Jan 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4.5-0.fdr.1
- New Version 5.4.5
