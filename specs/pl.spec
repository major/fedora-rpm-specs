# Name of the architecture-specific lib directory
%global swipl_arch %{_target_cpu}-linux

Name:           pl
Version:        10.0.1
Release:        %autorelease
Summary:        ISO/Edinburgh-style Prolog interpreter

# For the license breakdown, see licenses.txt, Source2
License:        BSD-2-Clause
URL:            https://www.swi-prolog.org/
VCS:            git:https://github.com/SWI-Prolog/swipl.git
# Source0: %%{url}download/stable/src/swipl-%%{version}.tar.gz
# To create the repackaged archive, use ./repackage.sh %%{version}
Source0:        swipl-%{version}_repackaged.tar.gz
Source1:        repackage.sh
Source2:        licenses.txt
# Use JNI for Java binding
Patch0:         swipl-8.2.1-Fix-JNI.patch
# Upstream installation paths differ from distribution ones
Patch1:         swipl-8.2.0-Remove-files-locations-from-swipl-1-manual.patch
# Unbundle libstemmer
Patch2:         swipl-8.2.0-unbundle-libstemmer.patch
# Expose inclpr plugin dependency on the math library to RPM
Patch3:         swipl-9.2.7-inclpr-math.patch
# Use zlib-ng directly rather than via the zlib compatibility interface
Patch4:         swipl-10.0.1-zlib-ng.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# Base
BuildRequires:  cmake(zlib-ng)
BuildRequires:  libatomic
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
# archive
BuildRequires:  pkgconfig(libarchive)
# bdb
BuildRequires:  libdb-devel
# crypt
BuildRequires:  libxcrypt-devel
# http
BuildRequires:  js-jquery
# jpl
%ifarch %{java_arches}
BuildRequires:  java-25-devel
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.hamcrest:hamcrest)
%endif
# mqi / swiplserver
BuildRequires:  python3-devel
# nlp
BuildRequires:  libstemmer-devel
# ODBC
BuildRequires:  pkgconfig(odbc)
# SSL
BuildRequires:  openssl
BuildRequires:  pkgconfig(openssl)
# sweep
BuildRequires:  emacs-devel
# term
BuildRequires:  pkgconfig(libedit)
# uuid
BuildRequires:  pkgconfig(ossp-uuid)
# win
BuildRequires:  cmake(Qt6)
# XPCE
BuildRequires:  cmake(SDL3)
BuildRequires:  cmake(SDL3_image)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  texinfo-tex
# yaml
BuildRequires:  pkgconfig(yaml-0.1)

# Doc building
# Gated to Fedora as EL is currently missing tex(a4wide.sty)
%if 0%{?fedora}
BuildRequires:  tex(latex)
BuildRequires:  tex(a4wide.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  texlive-courier
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-times
%endif

%global _desc %{expand:SWI-Prolog is a fast and powerful ISO/Edinburgh-style Prolog compiler with a
rich set of built-in predicates.  It offers a fast, robust and small
environment which enables substantial applications to be developed with it.

SWI-Prolog additionally offers:

* A powerful module system
* Garbage collection
* Unicode character set handling
* Unbounted integer and rational number arithmetic
* Multithreading support
* A powerful C/C++ interface
* GNU Readline interface}

%description
%_desc

%package     -n swi-prolog
Summary:        ISO/Edinburgh-style Prolog interpreter
BuildArch:      noarch
Requires:       swi-prolog-doc = %{version}-%{release}
Requires:       swi-prolog-cli = %{version}-%{release}
Requires:       swi-prolog-win = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl < 9.2.9-2
Provides:       pl = %{version}-%{release}
Obsoletes:      pl-devel < 9.2.9-2
Provides:       pl-devel = %{version}-%{release}
Obsoletes:      pl-compat-yap-devel < 9.2.9-2
Provides:       pl-compat-yap-devel = %{version}-%{release}

%description -n swi-prolog
%_desc

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

%description -n swi-prolog-full
%_desc

This is a metapackage, which installs the full SWI-Prolog suite, except tests.

%package     -n swi-prolog-core
# NOTE: There is no swi-prolog-core-devel package.  Instead, the header files
# and other development files are included in this package.  It is a Prolog
# compiler, and therefore is a development package itself.
License:        %{shrink:
                  BSD-2-Clause AND
                  (Brian-Gladman-3-Clause OR GPL-1.0-or-later) AND
                  BSD-3-Clause AND
                  dtoa AND
                  LicenseRef-Fedora-Public-Domain AND
                  MIT AND
                  Unicode-DFS-2016 AND
                  Zlib
                }
Summary:        ISO/Edinburgh-style Prolog interpreter - core system
Recommends:     swi-prolog-bdb%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-core-packages%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-doc = %{version}-%{release}
Recommends:     swi-prolog-java%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-odbc%{?_isa} = %{version}-%{release}

# Old version of minizip is bundled
Provides:       bundled(minizip) = 1.3.1

%description -n swi-prolog-core
%_desc

This package contains the core SWI-Prolog system.

%package     -n swi-prolog-core-packages
License:        %{shrink:
                  BSD-2-Clause AND
                  Beerware AND
                  (Brian-Gladman-3-Clause OR GPL-1.0-or-later) AND
                  (BSD-2-Clause OR Artistic-2.0) AND
                  BSD-3-Clause AND
                  GFDL-1.3-no-invariants-or-later AND
                  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND
                  GPL-2.0-or-later WITH SWI-exception AND
                  GPL-3.0-or-later AND
                  LGPL-2.0-or-later AND
                  LicenseRef-Fedora-Public-Domain AND
                  MIT AND
                  Unicode-DFS-2016 AND
                  W3C AND
                  Zlib
                }
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

# An old version of ut8proc is bundled, not fully compatible with the 2.x
# versions available in Fedora
Provides:       bundled(utf8proc) = 1.1.6

%description -n swi-prolog-core-packages
%_desc

This package contains the core SWI-Prolog packages.

%package     -n swi-prolog-cli
License:        BSD-2-Clause AND BSD-3-Clause AND bcrypt-Solar-Designer
Summary:        ISO/Edinburgh-style Prolog interpreter - command line interface
Requires:       swi-prolog-core%{?_isa} = %{version}-%{release}
Requires:       swi-prolog-core-packages%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-bdb%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-doc = %{version}-%{release}
Recommends:     swi-prolog-java%{?_isa} = %{version}-%{release}
Recommends:     swi-prolog-odbc%{?_isa} = %{version}-%{release}

# This can be removed when F47 reaches EOL
Obsoletes:      swi-prolog-nox < 10.0.0
Provides:       swi-prolog-nox = %{version}-%{release}

%description -n swi-prolog-cli
%_desc

This package contains a SWI-Prolog installation with a command line interface
but no GUI components.

%package     -n swi-prolog-win
License:        %{shrink:
                  BSD-2-Clause AND
                  CC-BY-SA-3.0 AND
                  FBM AND
                  GPL-2.0-or-later WITH Bison-exception-2.2 AND
                  HPND-Pbmplus AND
                  IJG AND
                  Knuth-CTAN AND
                  LicenseRef-Fedora-Public-Domain AND
                  PostgreSQL AND
                  Spencer-99 AND
                  TCL
                }
Summary:        ISO/Edinburgh-style Prolog interpreter - with GUI support
Requires:       swi-prolog-cli%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info%{?_isa}

# This can be removed when F45 reaches EOL
Obsoletes:      pl-xpce < 9.2.9-2
Provides:       pl-xpce = %{version}-%{release}

# This can be removed when F47 reaches EOL
Obsoletes:      swi-prolog-x < 10.0.0
Provides:       swi-prolog-x = %{version}-%{release}

%description -n swi-prolog-win
%_desc

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
Requires:       swi-prolog-cli%{?_isa} = %{version}-%{release}
Requires:       java-25-headless
Requires:       javapackages-tools

# This can be removed when F45 reaches EOL
Obsoletes:      pl-jpl < 9.2.9-2
Provides:       pl-jpl = %{version}-%{release}

%description -n swi-prolog-java
%_desc

This package provides JPL, a library using the SWI-Prolog foreign interface
and the Java Native Interface to provide a bidirectional interface between
Java and Prolog.  Prolog can be embedded in Java, and Java can be embedded in
Prolog.  It provides a reentrant bidirectional interface in both cases.
%endif

%package     -n swi-prolog-odbc
Summary:        SWI-Prolog ODBC interface
Requires:       swi-prolog-cli%{?_isa} = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl-odbc < 9.2.9-2
Provides:       pl-odbc = %{version}-%{release}

%description -n swi-prolog-odbc
%_desc

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
Requires:       swi-prolog-cli%{?_isa} = %{version}-%{release}

%description -n swi-prolog-bdb
%_desc

This package provides a foreign language extension to the Berkeley DB (libdb)
embedded database.

%package     -n swi-prolog-doc
License:        %{shrink:
                  BSD-2-Clause AND
                  CC-BY-SA-3.0 AND
                  Knuth-CTAN AND
                  LPPL-1.3c
                }
Summary:        Documentation and examples for SWI-Prolog
BuildArch:      noarch
Requires:       swi-prolog-core = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      pl-doc < 9.2.9-2
Provides:       pl-doc = %{version}-%{release}

%description -n swi-prolog-doc
%_desc

This package provides documentation and examples.

%package     -n swi-prolog-test
License:        %{shrink:
                  BSD-2-Clause AND
                  GPL-2.0-or-later AND
                  GPL-2.0-or-later WITH SWI-exception AND
                  LGPL-2.1-or-later
                }
Summary:        Tests and checks for SWI-Prolog
BuildArch:      noarch
Requires:       swi-prolog-cli = %{version}-%{release}

%description -n swi-prolog-test
%_desc

This package provides a set of prepared tests and checks for installed
SWI-Prolog systems.  This package is intended for SWI-Prolog development and
is of no use for ordinary users.  If you are not sure if you need this
package, you do not.

%prep
%global docdir doc-install
%autosetup -N -n swipl-%{version}
%patch -P0 -p1 -b .jni
%autopatch -p1 -m1
cp -p %{SOURCE2} .

%conf
# Fix the installation path on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
  sed -e 's,lib\(/\${SWIPL_INSTALL_DIR}\),lib64\1,' \
      -e '/SWIPL_INSTALL_CMAKE_CONFIG_DIR/s/lib/&64/' \
      -i cmake/LocationsPostPorts.cmake
fi

# Adjustments to take into account the new location of JNI stuff
sed -i 's#LIBDIR#%{_libdir}#g' packages/jpl/jpl.pl
sed -i.jni -e 's#LIBDIR#"%{_libdir}/swipl-jpl"#g' packages/jpl/src/main/java/org/jpl7/JPL.java

# Build documentation with the original jpl.pl, since the new version refers
# to install paths that don't exist yet; then switch before installing.
cp -p packages/jpl/jpl.pl packages/jpl/jpl.pl.install
cp -p packages/jpl/jpl.pl.jni packages/jpl/jpl.pl

# Do not use the bundled libedit
rm -fr packages/libedit/libedit

# Do not use the bundled libstemmer
rm -fr packages/nlp/libstemmer_c

# Do not use the bundled texinfo.tex
rm packages/xpce/man/info/texinfo.tex
ln -s %{_texmf_main}/tex/texinfo/texinfo.tex packages/xpce/man/info

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
  -DSYSTEM_LIBEDIT:BOOL=ON \
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
  %{buildroot}%{_libdir}/swipl/test/xsb/delay_tests/*.sh \
  %{buildroot}%{_libdir}/swipl/test/xsb/ptq/*.sh \
  %{buildroot}%{_libdir}/swipl/test/xsb/wfs_tests/*.sh

# Some XPCE files do not get installed
cp -p packages/xpce/man/*.1 %{buildroot}%{_mandir}/man1
cp -a packages/xpce/man/course %{buildroot}%{_libdir}/swipl/xpce/man

# Let LaTeX know about the style file
mkdir -p %{buildroot}%{_texmf_main}/tex/latex/swi-prolog
ln -s %{_libdir}/swipl/library/ext/pldoc/pldoc/pldoc.sty \
      %{buildroot}%{_texmf_main}/tex/latex/swi-prolog/pldoc.sty

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
find %{buildroot}%{_libdir} -name .gitignore -delete

# Move the desktop files to where we really want them
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}%{_libdir}/swipl/desktop/*.desktop \
   %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_libdir}/swipl/desktop/swipl.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mv %{buildroot}%{_libdir}/swipl/desktop/swipl-cli.png \
   %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
mv %{buildroot}%{_libdir}/swipl/desktop/prolog-mime.xml \
   %{buildroot}%{_datadir}/mime/packages
rmdir %{buildroot}%{_libdir}/swipl/desktop

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
%license LICENSE licenses.txt
%doc README.md README-customize.md
%{_bindir}/swipl
%{_bindir}/swipl-ld
%{_libdir}/cmake/swipl/
%dir %{_libdir}/swipl/
%{_libdir}/swipl/ABI
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
%{_libdir}/libswipl.so.10{,.*}
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
%{_libdir}/swipl/library/ext/json/
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
%{_texmf_main}/tex/latex/swi-prolog/

%files -n swi-prolog-cli
%{_libdir}/swipl/app/
%{_libdir}/swipl/lib/%{swipl_arch}/archive4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/crypto4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/libedit4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/pcre4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/ssl4pl.so
%{_libdir}/swipl/lib/%{swipl_arch}/tipc.so
%{_libdir}/swipl/lib/%{swipl_arch}/yaml4pl.so
%{_libdir}/swipl/library/ext/archive/
%{_libdir}/swipl/library/ext/libedit/
%{_libdir}/swipl/library/ext/pcre/
%{_libdir}/swipl/library/ext/ssl/
%{_libdir}/swipl/library/ext/tipc/
%{_libdir}/swipl/library/ext/yaml/

%files -n swi-prolog-win
%doc packages/xpce/{CUSTOMISE,EXTENDING,README}.md
%{_bindir}/swipl-win
%{_datadir}/applications/swipl.desktop
%{_datadir}/applications/swipl-win.desktop
%{_datadir}/icons/hicolor/64x64/apps/swipl.png
%{_datadir}/icons/hicolor/96x96/apps/swipl-cli.png
%{_datadir}/mime/packages/prolog-mime.xml
%{_libdir}/swipl/bin/%{swipl_arch}/swipl-win
%{_libdir}/swipl/lib/%{swipl_arch}/pl2xpce.so
%{_libdir}/swipl/swipl.rc
%{_libdir}/swipl/swipl-win.rc
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

%changelog
%autochangelog
