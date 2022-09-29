# Tests excluded
# See https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=19&t=1733
%bcond_with check

%bcond_without flexiblas

%global subversion .19

Name:          giac
Summary:       Computer Algebra System, Symbolic calculus, Geometry
Version:       1.9.0%{subversion}
Release:       3%{?dist}
# LGPLv3+: src/Fl_GDI_Printer.cxx, src/Flv_List.cc, src/Flv_Table.cc
# BSD: src/tinymt32*
# MIT: libmicropython.a
License:       GPLv3+ and MIT
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
Patch2:        %{name}-1.6.0-fix_micropy_compiler_flags.patch

# Adapt to cocoalib 0.99700
Patch3:        %{name}-cocoalib.patch

# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=3&t=2724
Patch4:        %{name}-fix_graphe_file.patch

# https://xcas.univ-grenoble-alpes.fr/forum/viewtopic.php?f=4&t=2792
Patch5:        %{name}-1.9.0-bug2792.patch

# Adapt to pari 2.15.0
Patch6:        %{name}-pari2.15.patch

BuildRequires: autoconf, libtool
BuildRequires: python3-devel
BuildRequires: readline-devel
BuildRequires: gettext-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cliquer-devel
BuildRequires: cocoalib-devel
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
BuildRequires: hevea
BuildRequires: tex(latex), texinfo, texinfo-tex, texlive-stmaryrd

# Javascript provided
Provides: bundled(CodeMirror)
Provides: bundled(FileSaver.js)

License:   GPLv3+ and GFDL
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
%autosetup -p0 -n %{name}-%{majver} -N

%patch0 -p1 -b .backup
%patch1 -p1 -b .backup
%patch2 -p0 -b .backup
%patch3 -p0 -b .backup
%patch4 -p1 -b .backup
%ifarch s390x
%patch5 -p1 -b .backup
%endif
%patch6 -p1 -b .backup

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
sed -i 's|config/texinfo.tex|%{_datadir}/texmf/tex/texinfo/texinfo.tex|g' Makefile.in
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
export CXXFLAGS="-std=gnu++14 %build_cxxflags"
export CFLAGS="%build_cflags"
%configure --enable-static=yes --with-included-gettext=no --enable-nls=yes \
 --enable-tommath=no --enable-debug=no --enable-gc=no --enable-sscl=no \
 --enable-dl=yes --enable-gsl=yes --enable-lapack=yes --enable-pari=yes \
 --enable-ntl=yes --enable-gmpxx=yes --enable-cocoa=autodetect \
 --enable-gui=yes --disable-rpath

# The --disable-rpath option of configure was not enough to get rid of the hardcoded libdir
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Fix unused-direct-shlib-dependency with libgslcblas.so.0 and libgfortran.so.3
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

export CXXFLAGS="-std=gnu++14 %build_cxxflags"
export CFLAGS_FEDORA="%build_cflags"
export LDFLAGS_FEDORA="%build_ldflags"
%make_build V=1

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
install -pm 644 libmicropython.a %{buildroot}%{_libdir}/

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
ln -sf -T %{_datadir}/giac/doc/aide_cas %{buildroot}%{_datadir}/giac/doc/fr/aide_cas
ln -sf -T %{_datadir}/giac/doc/aide_cas %{buildroot}%{_datadir}/giac/doc/en/aide_cas
ln -sf -T %{_datadir}/giac/doc/en/casinter/index.html %{buildroot}%{_datadir}/giac/doc/en/casinter/casinter.html
ln -sf -T %{_datadir}/giac/doc/en/cascmd_en/index.html %{buildroot}%{_datadir}/giac/doc/en/cascmd_en/cascmd_en.html

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
export LD_LIBRARY_PATH=../src/.libs
make -C check check
%endif

%files -f %{name}.lang
%license COPYING micropython-1.12/micropython-LICENSE
%license LICENSE.tinymt32
%{_bindir}/icas
%{_bindir}/giac
%{_bindir}/hevea2mml
%{_bindir}/*_help
%{_libdir}/libgiac.so.*
%{_libdir}/libgiac.a
%{_libdir}/libmicropython.a
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
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.9.0.19-3
- Rebuild for pari 2.15.0

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.0.19-2
- Rebuild for gsl-2.7.1

* Fri Aug 12 2022 Antonio Trande <sagitter@fedoraproject.org> 1.9.0.19-1
- Update to 1.9.0 sub-19

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 24 2022 Jerry James <loganjerry@gmail.com> - 1.7.0.29-3
- Rebuild for cocoalib 0.99800

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 04 2021 Antonio Trande <sagitter@fedoraproject.org> 1.7.0.29-1
- Update to 1.7.0 sub-29

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Jerry James <loganjerry@gmail.com> - 1.7.0.13-3
- Rebuild for ntl 11.5.1

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.7.0.13-2
- Rebuild for cocoalib 0.99713
- Build with cliquer support

* Sat Jun 12 2021 Antonio Trande <sagitter@fedoraproject.org> 1.7.0.13-1
- Update to 1.7.0 sub-13

* Thu Mar 25 2021 Antonio Trande <sagitter@fedoraproject.org> 1.7.0.1-1
- Update to 1.7.0 sub-1
- Remove wasm file with bad magic number
- Obsolete old appdata file

* Thu Mar 25 2021 Antonio Trande <sagitter@fedoraproject.org> 1.6.0.25-5
- Fix Version tag in desktop file
- Fix rhbz#1943048

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 1.6.0.25-4
- Rebuild for cocoalib 0.99712
- Work harder to avoid depending on libgslcblas

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Jerry James <loganjerry@gmail.com> - 1.6.0.25-2
- Rebuild for pari 2.13.0
- Bring back (modified) cocoalib patch, still needed for cocoalib support

* Wed Oct 21 2020 Antonio Trande <sagitter@fedoraproject.org> 1.6.0.25-1
- Update to 1.6.0 sub-25
- Patch configure.ac instead of configure.in

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.0.7-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.6.0.7-4
- Force C++14 as this code is not C++17 ready

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Antonio Trande <sagitter@fedoraproject.org> 1.6.0.7-1
- Update to 1.6.0 sub-7

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 1.5.0.85-4
- Fix broken configure test compromised by LTO

* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 1.5.0.85-3
- Rebuild for nauty 2.7.1

* Fri Mar 20 2020 Jerry James <loganjerry@gmail.com> - 1.5.0.85-2
- Rebuild for CoCoAlib 0.99700
- Add cocoalib patch
- Build with gmp-ecm, libcurl, libsamplerate, and nauty support

* Tue Feb 04 2020 Antonio Trande <sagitter@fedoraproject.org> 1.5.0.85-1
- Update to 1.5.0 sub-85

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 1.5.0.75-3
- Rebuild for ntl 11.4.3

* Sat Dec  7 2019 Jerry James <loganjerry@gmail.com> - 1.5.0.75-2
- Rebuild for CoCoAlib 0.99650 again

* Thu Nov 28 2019 Antonio Trande <sagitter@fedoraproject.org> 1.5.0.75-1
- Update to 1.5.0 sub-75
- Drop cocoalib patch

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 1.5.0.63-4
- Rebuild for CoCoAlib 0.99650

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 1.5.0.63-3
- Rebuild for mpfr 4

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 1.5.0.63-2
- Rebuild for ntl 11.3.4

* Sat Sep 14 2019 Antonio Trande <sagitter@fedoraproject.org> 1.5.0.63-1
- Update to 1.5.0 sub-63

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.0.53-3
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Antonio Trande <sagitter@fedoraproject.org> 1.5.0.53-1
- Update to 1.5.0 sub-53

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.5.0.35-4
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0.35-3
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Antonio Trande <sagitter@fedoraproject.org> 1.5.0.35-1
- Update to 1.5.0 sub-35

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 1.5.0.3-2
- Rebuild for ntl 11.3.0

* Wed Oct 10 2018 Antonio Trande <sagitter@fedoraproject.org> 1.5.0.3-1
- Update to 1.5.0 sub-3

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.4.9.59-5
- Rebuild for CoCoAlib 0.99600, ntl 11.2.1, and pari 2.11.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 1.4.9.59-3
- Build with CoCoAlib, glpk, and libao support
- Remove scriptlets that call install-info

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.4.9.59-2
- Rebuild for libfplll 5.2.1 and mpfi 1.5.3

* Fri May 18 2018 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.59-1
- Update to 1.4.9 sub-59
- Tests still disabled (some of them fail again)

* Wed Mar 28 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.9.45-5
- Build on all arches (tests now pass)

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.4.9.45-4
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.45-2
- Re-set previous ldconfig scripts

* Sat Feb 03 2018 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.45-1
- Update to 1.4.9 sub-45
- Use %%ldconfig_scriptlets

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.9.43-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.43-1
- Update to 1.4.9 sub-43

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.41-3
- Symlink restored

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.41-2
- Undo latest symlink changes

* Sun Dec 17 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.41-1
- Update to 1.4.9 sub-41
- Appdata file moved into metainfo shared data directory

* Sat Dec 02 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.33-1
- Update to 1.4.9 sub-33
- Fix symlinks

* Fri Dec 01 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.29-2
- Make symlinks used by QCAS

* Thu Nov 30 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.9.29-1
- Update to 1.4.9 sub-29

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 1.2.3.57-1
- Rebuild for ntl 10.5.0
- Fix versioning scheme

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9.57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Antonio Trande <sagitter@fedoraproject.org> 1.2.3-8.57
- Update to 1.2.3 sub-57

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7.49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.2.3-6.49
- perl dependency renamed to perl-interpreter <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sun Jun 11 2017 Antonio Trande <sagitter@fedoraproject.org> 1.2.3-5.49
- Update to 1.2.3 sub-49

* Sun May 14 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-4.43
- Bump Release so upgrade path works

* Fri May 12 2017 Antonio Trande <sagitter@fedoraproject.org> 1.2.3-1.43
- Update to 1.2.3 sub-43

* Wed Apr 05 2017 Jerry James <loganjerry@gmail.com> - 1.2.3-3.25
- Rebuild for ntl 10.3.0
- Make EVR greater than 1.2.3-3.13

* Sun Feb 19 2017 Antonio Trande <sagitter@fedoraproject.org> 1.2.3-1.25
- Update to 1.2.3 sub-25

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-2.13
- Adjust release so it's newer than the previous rev

* Wed Jan 18 2017 Antonio Trande <sagitter@fedoraproject.org> 1.2.3-1.13
- Update to 1.2.3 sub-13

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.3-2.9
- Rebuild for readline 7.x

* Thu Jan 05 2017 Antonio Trande <sagitter@fedoraproject.org> 1.2.3-1.9
- Update to 1.2.3 sub-9
- Conformed to new rules for scriptlets

* Sun Dec 25 2016 Antonio Trande <sagitter@fedoraproject.org> 1.2.2-14.105
- Update to subversion 105

* Fri Dec 02 2016 Paul Howarth <paul@city-fan.org> 1.2.2-13.103
- Rebuild for pari 2.9.0

* Tue Nov 15 2016 Antonio Trande <sagitter@fedoraproject.org> 1.2.2-12.103
- Update to subversion 103

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> 1.2.2-11.85
- Rebuild for ntl 10.1.0
- Add -iszero patch to fix breakage with recent glibc versions

* Tue Sep 27 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-10.85
- Update to subversion 85

* Mon Sep 05 2016 Jerry James <loganjerry@gmail.com> 1.2.2-9.75
- Rebuild for ntl 9.11.0

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> 1.2.2-8.75
- Rebuild for ntl 9.10.0

* Fri Jul 15 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-7.75
- Update to subversion 75

* Thu Jul 07 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-6.63
- Exclude s390x

* Sat Jul 02 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-5.63
- Fix directories ownership
- Exclude PPC and aarch64

* Thu Jun 30 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-4.63
- Update to subversion 63
- Add libXinerama BR
- Fix co-owning of documentation sub-directories
- Fix appdata file
- Add Provides tags

* Thu May 19 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-3.45
- Source tarball repacked without non-free docs
- Licenses combined in GPLv3+ only

* Fri May 13 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-2
- Fix required package of pgiac

* Fri May 13 2016 Antonio Trande <sagitter@fedoraproject.org>  1.2.2-1
- Update to 1.2.2
- pgiac script packaged separately
- Fix cSolveorder check
- Update scriptlets
- Add appdata file
- Excluded PPC and aarch64
- Drop the filesystem sub-package

* Sun Jul  6 2014  Frederic Han <han@math.jussieu.fr>  1.1.1-1
- Update to current stable upstream version. Remove obsolete patches.
- Add mpfi-devel dependency. (New feature in 1.1.1)
- Add requires of hicolor-icon-theme instead of owning dirs.
 
* Sun Apr 27 2014 Frederic Han <han@math.jussieu.fr>  1.1.0-1
- Let the doc package be independent of the binary packages. So create 
  a filesystem package containing the shared directories

* Wed Apr 16 2014 Frederic Han <han@math.jussieu.fr>  1.1.0-1
- Dont delete  intl/Makefile to avoid Makefile and configure modif/rebuilt
- Create a file list: giacdocfile for giac/doc files that are not needed
  at runtime
- Remove %%dir %%{_datadir}/mime and %%dir %%{_datadir}/mime/packages from 
  giac-xcas package list

* Mon Apr 14 2014 Frederic Han <han@math.jussieu.fr>  1.1.0-1
- Add tinymt32 License in %%doc, and LGPLv2+ tag 
- Add gettext-devel in BR and disable included intl
- removed doc/*/texinfo.tex, add BR texinfo, and rebuild *.info with 
  the system texinfo.tex file for License clarity, also convert them to utf-8
- Add missing %%dir in %%files xcas  and %%files
- Fix unused-direct-shlib-dependency for libgiac
- Remove x perms in examples, clean backup files
- Move the mime and desktop updates to %%post xcas and %%postun xcas
- Add a warning to *not* try to convert .xws files to UTF-8

* Fri Apr 11 2014 Frederic Han <han@math.jussieu.fr>  1.1.0-1
- Initial version 
- Found GPLv3 and v2 files in 1.1.0 sources. So package the GPLv3 LICENSE.
- Put GPLv3+ tag on the -doc package according to 1.1.1.
- Rename the package giac-gui to giac-xcas.
- Add a check patch and make check.
- Some files of %%{_datadir}/giac are need at runtime. So, 
  add them in the main or -xcas package filelist.
- Move all the %%{_docdir}/giac files except LICENSE to the -doc package
- Add extra pdf doc found in source archive.
- Untabify spec file.
- remove the README patch to keep the original 1.1.0 unchanged. add a README.fedora
  to explain the License evolution of giac non FR doc.
- Improve giac.1 manpage.
