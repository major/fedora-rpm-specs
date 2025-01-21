# Tests excluded
# See https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=19&t=1733
%ifarch s390x
%bcond_with check
%else
%bcond_without check
%endif

%bcond_without flexiblas

%global _lto_cflags %{nil}

%global subversion .998

Name:          giac
Summary:       Computer Algebra System, Symbolic calculus, Geometry
Version:       1.9.0%{subversion}
Release:       %autorelease
# GPL-3.0-or-later: the project as a whole
# GPL-3.0-only: src/TmpFGLM.*, src/TmpLESystemSolver.*
# GPL-2.0-or-later: pariinl.h
# GPL-1.0-or-later OR Artistic-1.0-Perl: src/pgiac
# LGPL-3.0-or-later: src/Fl_GDK_Printer.cxx, Flv_List.cc, Flv_Table.cc
# LGPL-2.0-or-later: intl/, src/Flv_Data_Source.H, src/Flv_List.H,
#   src/Flv_Table.H, src/Flve_Check_Button.H, src/Flve_Combo.H, src/Flve_Input.H
# MIT: micropython-1.12/, src/cutils.*, src/js.c, src/libbf.*, src/libregexp*,
#   src/libunicode.*, src/list.h, src/qjs*, src/quickjs*
License:       GPL-3.0-or-later AND GPL-3.0-only AND GPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LGPL-3.0-or-later AND LGPL-2.0-or-later AND MIT
URL:           http://www-fourier.ujf-grenoble.fr/~parisse/giac.html
## Source package is downloaded from
## http://www-fourier.ujf-grenoble.fr/~parisse/debian/dists/stable/main/source/
## and re-packed without non-free FR documentation by giac-makesrc script.
Source0:       %{name}-%{version}.tar.gz
Source1:       %{name}-makesrc.sh

# Recent math.h adds an iszero macro, but giac has an iszero function
Patch0:        %{name}-iszero.patch

# Deal with LTO compromised configure test
Patch1:        %{name}-config.patch

# Use Fedora compiler flags
Patch2:        %{name}-1.9.0-fix_micropy_compiler_flags.patch

# Adapt to cocoalib 0.99700
Patch3:        %{name}-cocoalib.patch

# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=3&t=2724
Patch4:        %{name}-fix_graphe_file.patch

# Adapt to pari 2.15.0
Patch5:        %{name}-pari2.15.patch

# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=3&t=2895
Patch6:        %{name}-undefine_GLIBCXX_ASSERTIONS.patch

# 'mkjs' is not correctly compiled 
# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=4&t=2930
Patch7:        %{name}-faking_mkjs.patch

BuildRequires: autoconf, libtool
BuildRequires: python3-devel
BuildRequires: readline-devel
BuildRequires: gettext-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cliquer-devel
%ifnarch %{ix86}
BuildRequires: cocoalib-devel
%endif
BuildRequires: glpk-devel
BuildRequires: gmp-devel
BuildRequires: gmp-ecm-devel
BuildRequires: gsl-devel
BuildRequires: libnauty-devel
BuildRequires: mpfr-devel
BuildRequires: ntl-devel
BuildRequires: pari-devel
%if %{with flexiblas}
BuildRequires: flexiblas-devel
%else
BuildRequires: blas-devel, lapack-devel
%endif
BuildRequires: mpfi-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libao-devel
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libsamplerate-devel
BuildRequires: fltk-devel
BuildRequires: libXinerama-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Provides: bundled(tinymt32)

# The micropython inside is a custom port with
# addtional built-in modules that are linked to giac.
Provides: libmicropython-static = 1.12
Provides: libgiac-static = 1.9.0
Provides: libxcas-static = 1.9.0

%global majver %(cut -d. -f1-3 <<< %{version})

%description
Giac is a Computer Algebra System made by Bernard Parisse. It  provides 
features from the C/C++ libraries PARI, NTL (arithmetic), GSL (numerics), 
GMP (big integers), MPFR (bigfloats) and also
  - Efficient algorithms for multivariate polynomial operations 
        (product, GCD, factorization, groebner bases),
  - Symbolic computations: solver, simplifications, limits/series, integration,
  - Linear algebra with numerical or symbolic coefficients.
  - Partial Maple and TI compatibility.
  - It has interfaces in texmacs and sagemath.

It consists of:
   - a C++ library (libgiac)
   - a command line interpreter (icas/giac)
   - an FLTK-based GUI (xcas) with interactive geometry and formal spreadsheets.

####################
%package devel
Summary: C++ development files for libgiac
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: fltk-devel%{?_isa}
Requires: gsl-devel%{?_isa}
Requires: mpfi-devel%{?_isa}
Requires: ntl-devel%{?_isa}

%description devel
Development files for libgiac.

####################
%package doc
Summary: Detailed html documentation for Giac/Xcas
BuildArch: noarch
%ifnarch %{ix86}
BuildRequires: hevea
%endif
BuildRequires: tex(latex), texinfo, texinfo-tex, texlive-stmaryrd

# Javascript provided
Provides: bundled(CodeMirror)
Provides: bundled(FileSaver.js)

License:   GPL-3.0-or-later AND GFDL-1.1-or-later
%description doc
The detailled html documentation and examples for giac and xcas. It is directly
accessible from xcas in many ways (browser, context search, thematic indexes).
It is strongly recommended for xcas usage. Note that the french part has been 
removed from the original source due to non free Licence.

####################
%package xcas
# The name Xcas is better known than the name giac itself, 
#     so many users will search for the name xcas instead of giac or giac-gui. 
Summary: GUI application for Giac
Provides: xcas%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme

%description xcas
Xcas is the Fltk graphic user interface to the computer algebra system giac. 
It supports formal computations, interactive 2D geometry, 3D plotting, 
spreadsheets with formal calculus and a Logo mode. There is also a programming 
editor, and many ways to consult the html help.

####################
%package -n pgiac
Summary:   Perl script for the computer algebra system Giac
URL:       http://melusine.eu.org/syracuse/giac/pgiac
BuildArch: noarch
BuildRequires: perl-generators
Requires:  %{name} = %{version}-%{release}

%description -n pgiac
The pgiac command is a perl script to mix Latex documents
with Giac computations.

%prep
%autosetup -n %{name}-%{majver} -N

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p0 -b .backup
%patch -P 3 -p0 -b .backup
%patch -P 4 -p1 -b .backup
%patch -P 5 -p1 -b .backup
%patch -P 6 -p1 -b .backup
%patch -P 7 -p1 -b .backup

# Remove local intl (already bundled in fedora)
rm -rf intl/*.h
rm -rf intl/*.cc

# Remove unecessary files and force the rebuild of info. 
rm -f doc/pari/gphtml
rm -f doc/*/texinfo.tex
rm -f doc/*/giac_*.info

# Some files in the upstream source have unnecessary executable rights
chmod -x src/*.h
chmod -x src/*.cc
find examples -type f -name '*.xws' -exec chmod -x '{}' \;
find examples -type f -name '*.cas' -exec chmod -x '{}' \;
find examples -type f -name '*.cxx' -exec chmod -x '{}' \;
chmod -x examples/lewisw/fermat*
# Clean backups in doc
find doc -name *~ -delete

# Unbundle texinfo file
sed -i 's|config/texinfo.tex|%{_texmf_main}/tex/texinfo/texinfo.tex|g' Makefile.in
rm -f config/texinfo.tex

# Remove hidden files
rm -f examples/Exemples/demo/._*
rm -f examples/Exemples/analyse/._*

%if %{with flexiblas}
sed -e 's|LIB(blas|LIB(flexiblas|g' -e 's|LIB(lapack|LIB(flexiblas|g' \
 -e 's|-lgslcblas|-lflexiblas|' -i configure.ac
%endif

# Prepare Micropython lib's License
cp -p micropython-1.12/LICENSE micropython-1.12/micropython-LICENSE

# Update configure.ac obsolete macros
autoupdate -vf

# Re-configuration
autoreconf -ivf

%build
# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=4&t=2817
OPT_FLAGS=$(echo "%build_cxxflags" | %{__sed} -e 's/-Werror=format-security/-Wno-error=format-security/')
export CXXFLAGS="$OPT_FLAGS -std=gnu++17"
export CFLAGS_FEDORA="$OPT_FLAGS -std=gnu17"
%configure --enable-static=yes --with-included-gettext=no --enable-nls=yes \
 --enable-tommath=no --enable-debug=no --enable-gc=no --enable-sscl=no \
 --enable-dl=yes --enable-gsl=yes --enable-lapack=yes --enable-pari=yes \
 --enable-ntl=yes --enable-gmpxx=yes --enable-cocoa=autodetect \
 --enable-gui=yes --disable-rpath \
%ifarch %{power64}
 --disable-micropy
%endif

# The --disable-rpath option of configure was not enough to get rid of the hardcoded libdir
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Compile 'mkjs' executable
# See patch7's comment
export OPT_FLAGS=$(echo "%build_cxxflags" | %{__sed} -e 's/-Werror=format-security/-Wno-error=format-security/')
g++ $OPT_FLAGS -std=gnu++17 src/mkjs.cc -o src/mkjs
#

# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=4&t=2817
OPT_FLAGS=$(echo "%build_cflags" | %{__sed} -e 's/-Werror=format-security/-Wno-error=format-security/')
export CXXFLAGS="$OPT_FLAGS -std=gnu++17"
export CFLAGS_FEDORA="$OPT_FLAGS -std=gnu17"
export LDFLAGS_FEDORA="$OPT_FLAGS"
%make_build

# Rebuild giac_*.info and Convert info file to utf-8
(cd doc ; make)
for i in doc/*/giac_*.info doc/en/html_* ; do 
   iconv -f ISO-8859-1 -t UTF-8 -o $i.new $i && \
   touch -r $i $i.new && \
   mv $i.new $i
done
#

%install
%make_install

# Install libmicropython.a library
%ifnarch %{power64}
install -pm 644 libmicropython.a %{buildroot}%{_libdir}/
%endif

# Install libxcas.a library
install -pm 644 src/.libs/libxcas.a %{buildroot}%{_libdir}/
install -pm 644 src/.libs/libgiac.a %{buildroot}%{_libdir}/

cp -p src/tinymt32_license.h LICENSE.tinymt32

# Remove unwanted files.
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_datadir}/application-registry

# The .la is still built despite the built of libgiac.a has been disabled
rm -f %{buildroot}%{_libdir}/libgiac.la 

# I have tried to remove the empty files in the setup stage, it was not a good idea
#   because make install will then require hevea as an extra (and big) dependancy and I guess
#   that it will recreate those empty files, so it's better to delete them here.
find %{buildroot} -size 0 -delete

# Obsolete symbolic link
rm -f %{buildroot}%{_bindir}/xcasnew
#

# Remove wasm file (??) with Bad Magic Number
rm -f %{buildroot}%{_docdir}/giacwasm.wasm

# Mime package was not installed.
install -pm 644 -D debian/giac.sharedmimeinfo \
                     %{buildroot}%{_datadir}/mime/packages/giac.xml
#

# Check appdata file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
#

# Add extra pdf docs. (NB: make dvi gives only the same doc in dvi format)
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc doc/en/cas*.pdf
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc/en doc/en/*.pdf
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc/el doc/el/*.pdf
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc/es doc/es/*.pdf

# Symlinks used by QCAS and giacpy
mkdir -p %{buildroot}%{_datadir}/giac/doc/fr
ln -srf -T %{_datadir}/giac/doc/aide_cas %{buildroot}%{_datadir}/giac/doc/fr/aide_cas
ln -srf -T %{_datadir}/giac/doc/aide_cas %{buildroot}%{_datadir}/giac/doc/en/aide_cas
ln -srf -T %{_datadir}/giac/doc/en/casinter/index.html %{buildroot}%{_datadir}/giac/doc/en/casinter/casinter.html
ln -srf -T %{_datadir}/giac/doc/en/cascmd_en/index.html %{buildroot}%{_datadir}/giac/doc/en/cascmd_en/cascmd_en.html

#
# DOC Files (1-4):
#   1) Man: 
# 
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 debian/giac.1 %{buildroot}%{_mandir}/man1
install -pm 644 debian/cas_help.1 %{buildroot}%{_mandir}/man1
install -pm 644 debian/pgiac.1 %{buildroot}%{_mandir}/man1

#      Add a link for FR env users to have the english help instead of a page 
#      not found.
mkdir -p %{buildroot}%{_datadir}/giac/doc/fr
(cd %{buildroot}%{_datadir}/giac/doc/fr ; ln -s ../en/cascmd_en cascmd_fr )

%find_lang %{name} 
desktop-file-install --vendor="" --remove-key=Encoding \
                     --set-key=Version --set-value=1.0 \
                     --dir=%{buildroot}%{_datadir}/applications/ \
                     %{buildroot}%{_datadir}/applications/xcas.desktop

# Create a list of files non required at runtime by icas nor xcas
#      that are under %%{_datadir}/giac/doc for packaging in giac-doc
#      a) The non required files at runtime in %%{_datadir}/giac/doc/[a-z]{2}
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 2 -type f| \
             grep  -E "%{_datadir}/giac/doc/[a-z]{2}/" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}/keywords$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}/xcasmenu$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}/xcasex$" | \
             sed -e "s:%{buildroot}::" >giacdoclist
#      b) Add the files under doc
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 1 -type f| \
             grep  -v -E "%{_datadir}/giac/doc/aide_cas$" | \
             sed -e "s:%{buildroot}::" >>giacdoclist

#      c) Add the dir under %%{_datadir}/giac/doc/[a-z]{2}
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 2 -type d| \
             grep  -E "%{_datadir}/giac/doc/[a-z]{2}/" | \
             grep  -v -E "%{_datadir}/giac/doc$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}$" | \
             sed -e "s:%{buildroot}::" | \
             sed -e "s:$:/:" >>giacdoclist
#      d) Add all the doc subdir different from %%{_datadir}/giac/doc/[a-z]{2}
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 1 -type d| \
             grep  -v -E "%{_datadir}/giac/doc$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}$" | \
             sed -e "s:%{buildroot}::" | \
             sed -e "s:$:/:" >>giacdoclist
#      e) Add all the links but aide_cas
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 2 -type l| \
             grep  -v -E "%{_datadir}/giac/doc/aide_cas$" | \
             sed -e "s:%{buildroot}::" >>giacdoclist

%if %{with check}
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make -C check check
# This is for debugging purpose only
#make -C check check && exit 1
#cat check/test-suite.log && exit 1
%endif

%files -f %{name}.lang
%license COPYING micropython-1.12/micropython-LICENSE
%license LICENSE.tinymt32
%{_bindir}/icas
%{_bindir}/giac
%{_bindir}/hevea2mml
%{_bindir}/*_help
%{_libdir}/libgiac.so.0.0.0
%{_libdir}/libgiac.so.0
%{_libdir}/libgiac.a
%ifnarch %{power64}
%{_libdir}/libmicropython.a
%endif
%{_libdir}/libxcas.a
#    The following files are required at runtime by icas AND xcas. 
#       (Ex: if LANG is fr, alea(5) should give an INT)
#       Moreover, without aide_cas the keywords files are not found in icas 
#       and xcas. Additionally xcas uses it for tab completions.
%{_datadir}/giac/doc/*/keywords
%{_datadir}/giac/aide_cas
%{_datadir}/giac/doc/aide_cas
# The dirs shared
%dir %{_datadir}/giac
%dir %{_datadir}/giac/doc
#
%dir %{_datadir}/giac/doc/de
%dir %{_datadir}/giac/doc/el
%dir %{_datadir}/giac/doc/en
%dir %{_datadir}/giac/doc/es
%dir %{_datadir}/giac/doc/fr
%dir %{_datadir}/giac/doc/pt
%dir %{_datadir}/giac/doc/zh
#
%{_infodir}/giac_*.info.*
%{_mandir}/man1/giac*
%{_mandir}/man1/*_help*

# The gui files
%files xcas
%{_bindir}/xcas
# The dirs shared
%dir %{_datadir}/giac
%dir %{_datadir}/giac/doc
#
%dir %{_datadir}/giac/doc/de
%dir %{_datadir}/giac/doc/el
%dir %{_datadir}/giac/doc/en
%dir %{_datadir}/giac/doc/es
%dir %{_datadir}/giac/doc/fr
%dir %{_datadir}/giac/doc/pt
%dir %{_datadir}/giac/doc/zh
#
# Required at runtime. (additional menu)
%{_datadir}/giac/doc/*/xcasmenu
%{_datadir}/giac/doc/*/xcasex

#    Files under dirs shared with other packages
%{_datadir}/applications/xcas.desktop
%{_metainfodir}/xcas.metainfo.xml
%{_datadir}/mime/packages/giac.xml
%{_datadir}/pixmaps/xcas.xpm
%{_datadir}/icons/hicolor/*/apps/xcas.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-xcas.png

%files -n pgiac
%{_bindir}/pgiac
%{_mandir}/man1/pgiac*

%files devel
%{_includedir}/giac/
%{_libdir}/libgiac.so

# DOC Files
%files doc -f giacdoclist
#   3) As we have removed the FR doc, more than 2/3 of the following files are 
#      for the EN doc, so it is meaningfull to put all the GPL doc together.   
#
# a GPLv3  COPYING file
%doc README
%license COPYING
#    4) Warning about *.xws:
#     - All the .xws files are examples of sessions saved from xcas. They are
#       not text files and they *must not* be converted to UTF-8 or any other
#       character encoding.
#     - The .cas and .cxx files are giac code and function. They are text files
#
#   NB: %%{_docdir}/giac is in  the -filsystem package 
%{_docdir}/giac/*
#     Add all the files that are in %%{_datadir}/giac but not giac/aide_cas 
#     and not those in giac/doc/
%dir %{_datadir}/giac
%dir %{_docdir}/giac
%dir %{_datadir}/giac/doc
# The dirs shared
#
%dir %{_datadir}/giac/doc/de
%dir %{_datadir}/giac/doc/el
%dir %{_datadir}/giac/doc/en
%dir %{_datadir}/giac/doc/es
%dir %{_datadir}/giac/doc/fr
%dir %{_datadir}/giac/doc/pt
%dir %{_datadir}/giac/doc/zh
#
%{_datadir}/giac/examples/

%changelog
%autochangelog
