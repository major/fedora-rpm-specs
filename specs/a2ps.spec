Summary: Converts text and other types of files to PostScript
Name: a2ps
Version: 4.15.6
Release: 3%{?dist}
# several files in afm/, lib/, liba2ps/, src/ - GPL3+
# gnulib files in lib/ - LGPL-2.1+
# several files in lib/ - LGPL-3+
# Bison related files in src/ and liba2ps/ - GPL-3.0-or-later WITH Bison-exception-2.2
# another gnulib files in /lib - LGPL2+
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.0-or-later
Url: http://www.gnu.org/software/a2ps/
Source0: http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Source1: ftp://ftp.enst.fr/pub/unix/a2ps/i18n-fonts-0.1.tar.gz
# the latest upstream version does not have COPYING file...
# reported as https://savannah.gnu.org/bugs/index.php?64470
# copied the GPL3+ COPYING file from the previous versions
Source2: COPYING


Patch01: a2ps-4.13-conf.patch
Patch02: a2ps-4.13-etc.patch
Patch03: a2ps-4.13-glibcpaper.patch
Patch04: a2ps-sort.patch
Patch05: a2ps-iso5-minus.patch
Patch06: a2ps-perl.patch
Patch07: a2ps-4.13b-numeric.patch
Patch08: a2ps-4.13b-encoding.patch
Patch09: a2ps-4.13b-tilde.patch
Patch10: a2ps-4.13-euckr.patch
Patch11: a2ps-4.13-hebrew.patch
Patch12: a2ps-make-fonts-map.patch
Patch13: a2ps-wdiff.patch
Patch14: a2ps-U.patch
Patch15: a2ps-mb.patch
Patch16: a2ps-4.14-texinfo-nodes.patch
Patch17: a2ps-forward-null.patch
Patch18: a2ps-overrun-dynamic.patch
Patch19: a2ps-overrun-static.patch
Patch20: a2ps-resource-leak.patch


# most conversion rules are guarded by configure macros, so they
# are not enabled if the specific binary is not present in buildroot
# - thus to get full set of available rules there are lot of BuildRequires,
# but most binaries are only as Recommends during runtime to provide a way
# how to slim down the installation if needed.

# parser for PPDs and SSH (style sheet) files
BuildRequires: bison
# bzip2 is checked during build as well
BuildRequires: bzip2
# for emacs support - configure scripts looks for emacs command during build
BuildRequires: emacs
# for lexical scanning of postscript, ppds and style sheet (.ssh) files
BuildRequires: flex
# written in C - gcc no longer in buildroot by default
BuildRequires: gcc
# uses BDW Garbage Collector
BuildRequires: gc-devel
# for translations
BuildRequires: gettext
# for ps2pdf - PDF output, pdf2ps - PDF delegation
BuildRequires: ghostscript
# bundles gnulib source library
BuildRequires: gnulib-devel
# used for generating hash function for configuration options
BuildRequires: gperf
# Perl parts of groff text processor - ROFF delegation for man pages
BuildRequires: groff-perl
# for compressed delegations
BuildRequires: gzip
# generating manpages
BuildRequires: help2man
# for paper configs
BuildRequires: libpaper-devel
# used for building
BuildRequires: libtool
# make no longer in buildroot
BuildRequires: make
# for getting version of bundled gnulib
BuildRequires: perl-interpreter
# tools for manipulating with postscript docs
BuildRequires: psutils
# makeinfo for info documentation
BuildRequires: texinfo
# for DVI files support, it's DVI driver for tex
BuildRequires: texlive-dvips
# latex for LaTeX file support
BuildRequires: texlive-latex
# tex for Tex File support
BuildRequires: texlive-tex

%if 0%{?rhel} <= 8 || 0%{?fedora}
# for convert binary - used for converting images to postscript
BuildRequires: ImageMagick
# converting html files to postscript
BuildRequires: html2ps
%endif

# bundles gnulib of certain version
Provides: bundled(gnulib)%(perl -ne 'if($. == 1 and /\A(\d+)-(\d+)-(\d+)/) {print qq{ = $1$2$3}}' %{_defaultdocdir}/gnulib/ChangeLog 2>/dev/null)

# used during runtime for delegation
Recommends: bzip2
# Perl parts of groff text processor - ROFF delegation for man pages
Recommends: groff-perl
# for compressed delegations
Recommends: gzip
# makeinfo for info documentation
Recommends: texinfo
# for DVI files support, it's DVI driver for tex
Recommends: texlive-dvips
# latex for LaTeX file support
Recommends: texlive-latex
# tex for Tex File support
Recommends: texinfo-tex

# a2ps-lpr-wrapper uses lp/lpr
Requires: cups-client
# for hebrew support, path set. 
# culmus-fonts
# And certainly other font sets for other languages may be needed
Requires: emacs-filesystem
Requires: file
# for ps2pdf - PDF output, pdf2ps - PDF delegation
Requires: ghostscript
# postscript delegation
Requires: psutils
Requires: psutils-perl
# set of recommended fonts, looks to be for postscript as well
Requires: texlive-collection-fontsrecommended

Requires(post): coreutils

%if 0%{?rhel} <= 8 || 0%{?fedora}
# image delegations
Requires: ImageMagick
# html delegations
Recommends: html2ps
%endif

# for emacs support
Suggests: emacs

%description
The a2ps filter converts text and other types of files to PostScript.
A2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.


%prep
%setup -q -a 1

# use fedora postscript font paths
%patch -P 01 -p1 -b .conf
# add /etc/a2ps in directories searched for config files
%patch -P 02 -p1 -b .etc
%patch -P 03 -p1 -b .glibcpaper
%patch -P 04 -p1 -b .sort
%patch -P 05 -p1 -b .iso5-minus
%patch -P 06 -p1 -b .perl
# Use C locale's decimal point style (bug #53715).
%patch -P 07 -p1 -b .numeric
# Use locale to determine a sensible default encoding (bug #64584).
%patch -P 08 -p1 -b .encoding
# Fix koi8 tilde (bug #66393).
%patch -P 09 -p1 -b .tilde
# Add Korean resource file (bug #81421).
%patch -P 10 -p1 -b .euckr
# Hebrew support (bug #113191).
%patch -P 11 -p1 -b .hebrew
# Fix problems in make_fonts_map script (bug #142299).  Patch from
# Michal Jaegermann.
%patch -P 12 -p1 -b .make-fonts-map
# Make pdiff default to not requiring wdiff (bug #68537).
%patch -P 13 -p1 -b .wdiff
# Make pdiff use diff(1) properly (bug #156916).
%patch -P 14 -p1 -b .U
# Fixed multibyte handling (bug #212154).
%patch -P 15 -p1 -b .mb
# Remove dots in node names, patch from Vitezslav Crhonek (Bug #445971)
%patch -P 16 -p1 -b .nodes
# Coverity fix (forward-null).
%patch -P 17 -p1 -b .forward-null
# Coverity fix (overrun-dynamic).
%patch -P 18 -p1 -b .overrun-dynamic
# Coverity fix (overrun-static).
%patch -P 19 -p1 -b .overrun-static
# Coverity fix (resource-leak).
%patch -P 20 -p1 -b .resource-leak

for file in AUTHORS ChangeLog; do
  iconv -f latin1 -t UTF-8 < $file > $file.utf8
  touch -c -r $file $file.utf8
  mv $file.utf8 $file
done

autoreconf -fi

mv doc/encoding.texi doc/encoding.texi.utf8
iconv -f KOI-8 -t UTF-8 doc/encoding.texi.utf8 -o doc/encoding.texi

# Fix reference to a2ps binary (bug #112930).
sed -i -e "s,/usr/local/bin,%{_bindir}," contrib/emacs/a2ps.el

chmod 644 encoding/iso8.edf.hebrew
chmod 644 encoding/euc-kr.edf.euckr


%build
# preset the date in README.in to avoid the timestamp of the build time
sed -e "s!@date@!`date -r NEWS`!" etc/README.in > etc/README.in.tmp
touch -c -r etc/README.in etc/README.in.tmp
mv etc/README.in.tmp etc/README.in

EMACS=emacs %configure \
  --with-medium=_glibc \
  --enable-kanji \
  --with-lispdir=%{_emacs_sitelispdir}/%{name}

# Remove prebuilt info files to force regeneration at build time
find . -name "*.info*" -exec rm -f {} \;
# force rebuilding scanners by flex - patched or not
find src lib -name '*.l' -exec touch {} \;
# these scanners use 'lineno' - incompatible with -CFe flex flags
#(
#    cd src
#    /bin/sh ../auxdir/ylwrap "flex" sheets-map.l lex.yy.c sheets-map.c --
#    /bin/sh ../auxdir/ylwrap "flex" lexssh.l lex.yy.c lexssh.c --
#    cd ../lib
#    /bin/sh ../auxdir/ylwrap "flex" lexppd.l lex.yy.c lexppd.c --
#)

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install INSTALL='install -p'

# reset the timestamp for the generated etc/README file
touch -r etc/README.in %{buildroot}%{_datadir}/a2ps/README

mkdir -p %{buildroot}%{_sysconfdir}/a2ps

mkdir -p %{buildroot}%{_datadir}/a2ps/{afm,fonts}
pushd i18n-fonts-0.1/afm
install -p -m 0644 *.afm %{buildroot}%{_datadir}/a2ps/afm
pushd ../fonts
install -p -m 0644 *.pfb %{buildroot}%{_datadir}/a2ps/fonts
popd
popd

rm -f %{buildroot}%{_infodir}/dir

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_defaultlicensedir}/%{name}/COPYING

for lang in af be bg ca cs da de el eo es et eu fi fr ga gl hu it ja ka ko ms nb nl pl pt pt_BR ro ru rw sk sl sr sv tr uk vi zh_CN zh_TW
do
  mv %{buildroot}/usr/share/locale/$lang/LC_MESSAGES/a2ps{-gnulib,}.mo
done

%find_lang %name


%post
%{?ldconfig}
(cd %{_datadir}/a2ps/afm;
 ./make_fonts_map.sh > /dev/null 2>&1 || /bin/true
 if [ -f fonts.map.new ]; then
   mv fonts.map.new fonts.map
 fi
)
exit 0

%ldconfig_postun


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO THANKS
%dir %{_sysconfdir}/a2ps
%config %{_sysconfdir}/a2ps.cfg
%config(noreplace) %{_sysconfdir}/a2ps-site.cfg
%{_bindir}/a2ps
%{_bindir}/a2ps-lpr-wrapper
%{_bindir}/card
%{_bindir}/composeglyphs
%{_bindir}/fixps
%{_bindir}/lp2
%{_bindir}/ogonkify
%{_bindir}/pdiff
%dir %{_datadir}/a2ps
%dir %{_datadir}/a2ps/afm
%{_datadir}/a2ps/afm/*.afm
# automatically regenerated at install and update time
%verify(not size mtime md5) %{_datadir}/a2ps/afm/fonts.map
%{_datadir}/a2ps/afm/make_fonts_map.sh
%{_datadir}/a2ps/README
%{_datadir}/a2ps/encoding
%{_datadir}/a2ps/fonts
%{_datadir}/a2ps/ppd
%{_datadir}/a2ps/ps
%{_datadir}/a2ps/sheets
%{_datadir}/ogonkify/
%{_emacs_sitelispdir}/%{name}
%{_infodir}/a2ps.info*
%{_infodir}/ogonkify.info*
%{_infodir}/regex.info*
%{_mandir}/man1/a2ps-lpr-wrapper.1.gz
%{_mandir}/man1/a2ps.1.gz
%{_mandir}/man1/card.1.gz
%{_mandir}/man1/fixps.1.gz
%{_mandir}/man1/lp2.1.gz
%{_mandir}/man1/ogonkify.1.gz
%{_mandir}/man1/pdiff.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Zdenek Dohnal <zdohnal@redhat.com> - 4.15.6-1
- 2269423 - a2ps-4.15.6 is available

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Zdenek Dohnal <zdohnal@redhat.com> - 4.15.5-1
- 2225694 - a2ps: FTBFS in Fedora rawhide/f39
- 2189133 - a2ps: FTBFS in rawhide, 64-bit and C99 compatibility issues
- 2176254 - a2ps-4.15.5 is available
- SPDX migration done

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-47
- make eln changes - remove dependency on ImageMagick and html2ps

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-46
- make nor gcc are in buildroot anymore

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-45
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-42
- a2ps: new texinfo needs to have documentencoding defined

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-38
- removing install-info, because now it is done automatically

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-37
- fix tetex-fonts dependency - now provided by texlive-collections-fontsrecommended

* Fri Feb 16 2018 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-36
- remove tetex dependency 

* Thu Feb 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 4.14-35
- remove old stuff https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MRWOMRZ6KPCV25EFHJ2O67BCCP3L4Y6N/

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14-33
- Remove old crufty coreutils requires

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Tim Waugh <twaugh@redhat.com> - 4.14-28
- Moved emacs sub-packages into main package (bug #1234582).

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr  3 2014 Tim Waugh <twaugh@redhat.com> - 4.14-24
- Prevent another build failure with -Werror=format-security.

* Tue Apr  1 2014 Tim Waugh <twaugh@redhat.com> - 4.14-23
- Invoke gs with the -dSAFER option in fixps (CVE-2014-0466, bug #1082411).

* Tue Dec  3 2013 Tim Waugh <twaugh@redhat.com> - 4.14-22
- Prevent build failure with -Werror=format-security (bug #1036979).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Tim Waugh <twaugh@redhat.com> - 4.14-20
- Avoid a bad free in the encoding handling logic (bug #954104).

* Mon Apr 29 2013 Tim Waugh <twaugh@redhat.com> - 4.14-19
- Support for building on aarch64 (bug #924962).

* Tue Mar 26 2013 Tim Waugh <twaugh@redhat.com> - 4.14-18
- Fixed texi build failure (bug #927633).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr  4 2012 Tim Waugh <twaugh@redhat.com> - 4.14-15
- Link to libm in liba2ps (bug #809673).

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 10 2011 Tim Waugh <twaugh@redhat.com> - 4.14-13
- Coverity fixes (resource-leak, overrun-static, overrun-dynamic,
  forward-null).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 4.14-11
- Spec file fixes for Emacs add-on guideline compliance
- Move *.el(c) files to their own directory
- Use Emacs packaging macros
- Remove unneeded pkgconfig macros

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Adam Jackson <ajax@redhat.com> 4.14-9
- Requires: psutils-perl for fixps

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Tim Waugh <twaugh@redhat.com> 4.14-7
- Removed trade marks to avoid potential confusion.

* Wed Sep 24 2008 Tim Waugh <twaugh@redhat.com> 4.14-6
- Removed patch fuzz.

* Thu May 29 2008 Tim Waugh <twaugh@redhat.com> 4.14-5
- Removed old patches.

* Sun May 18 2008 Patrice Dumas <pertusus@free.fr> 4.14-4
- remove dots in node names, patch from Vitezslav Crhonek (bug #445971)

* Wed May 14 2008 Patrice Dumas <pertusus@free.fr> 4.14-3
- %%{_datadir}/a2ps/afm/fonts.map is dynamically generated, mark it
  as such in %%files (bug #70919)

* Sun Apr 27 2008 Patrice Dumas <pertusus@free.fr> 4.14-2
- update to 4.14
- don't obsolete the provided version of a2ps-i18n
- use html2ps for the html delegation
- BuildRequires gperf

* Tue Feb 12 2008 Patrice Dumas <pertusus@free.fr> 4.13b-71
- use a predictable stamp inside the etc/README file
- follow emacs packaging guidelines

* Tue Feb 12 2008 Tim Waugh <twaugh@redhat.com> 4.13b-70
- Separate out libs sub-package for multilib (bug #340571).

* Wed Sep 26 2007 Tim Waugh <twaugh@redhat.com> 4.13b-69
- Try out a perl stylesheet speed improvement (bug #252183).

* Tue Sep 25 2007 Tim Waugh <twaugh@redhat.com> 4.13b-68
- Make minus sign work in ISO-8859-5 (bug #252314).

* Thu Aug 23 2007 Tim Waugh <twaugh@redhat.com> 4.13b-67
- More specific license tag.

* Fri Jul 13 2007 Tim Waugh <twaugh@redhat.com> 4.13b-66
- Change build requirement from /usr/bin/emacs to emacs to fix build.
- Hebrew fix (bug #247999).

* Wed Mar 14 2007 Tim Waugh <twaugh@redhat.com> 4.13b-65
- Fix encoding of encoding.texi (bug #225235).
- Make a2ps.cfg %%config again, but not noreplace (bug #225235).
- Added post/postun ldconfig (bug #225235).

* Mon Mar 12 2007 Tim Waugh <twaugh@redhat.com> 4.13b-64
- Renamed tarball generation script (bug #225235).

* Fri Mar  9 2007 Tim Waugh <twaugh@redhat.com> 4.13b-63
- Removed bad files (bug #225235).
- Add sysconfdir/a2ps to search path (bug #225235).
- Build does not require gperf after all (bug #225235).
- Don't remove needed library (bug #225235).

* Thu Mar  8 2007 Tim Waugh <twaugh@redhat.com> 4.13b-62
- Build requires bison.
- Use sed instead of perl for string replacement (bug #225235).
- Better install-info scriptlets (bug #225235).
- Added BuildRequires and Requires for more packages (bug #225235).
- a2ps.cfg needn't be %%config (bug #225235).
- No need to gzip the info files (bug #225235).
- Use external libtool and don't run the autotools (bug #225235).

* Wed Feb 28 2007 Tim Waugh <twaugh@redhat.com> 4.13b-61
- Clean up tmpdir in pdiff (bug #214400).
- Fixed permissions on C source files (bug #225235).
- Use %%configure (bug #225235).
- Preserve timestamps (bug #225235).
- Use smp_mflags (bug #225235).
- Requires install-info for post and preun scriptlets (bug #225235).
- Avoid tabs (bug #225235).
- Explicity versioning for obsoletes/provides (bug #225235).
- PreReq->Requires(post) (bug #225235).
- Fixed macros in changelog (bug #225235).
- Fixed summary (bug #225235).
- Converted spec file to UTF-8 (bug #225235).
- Fixed build root (bug #225235).
- Remove ExcludeArch (bug #225235).
- Use buildroot macro consistently (bug #225235).
- Don't ship the library file or header (bug #203536).

* Tue Jan 23 2007 Tim Waugh <twaugh@redhat.com> 4.13b-60
- Force it to build by hacking the configure script.
- Don't need rm patch.
- Make scriptlets unconditionally succeed (bug #223674).

* Fri Oct 27 2006 Tim Waugh <twaugh@redhat.com>
- Build requires cups (bug #204119).

* Wed Oct 25 2006 Tim Waugh <twaugh@redhat.com>
- Make ogonkify build.

* Wed Oct 25 2006 Tim Waugh <twaugh@redhat.com> 4.13b-59
- Fixed multibyte handling (bug #212154).

* Tue Oct 17 2006 Tim Waugh <twaugh@redhat.com> 4.13b-58
- Fixed psset sed expression (bug #209613).

* Mon Oct  9 2006 Tim Waugh <twaugh@redhat.com>
- Build requires ImageMagick for a2ps.cfg to use convert(1).
- Build requires groff-perl for a2ps.cfg to use grog(1).

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 4.13b-57
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Tim Waugh <twaugh@redhat.com> 4.13b-56
- Fixed build (bug #188156).

* Fri Aug 25 2006 Tim Waugh <twaugh@redhat.com>
- Build requires groff.

* Fri Aug 25 2006 Tim Waugh <twaugh@redhat.com> 4.13b-55
- Use better manifest flags for fonts.map.

* Tue Aug  8 2006 Tim Waugh <twaugh@redhat.com> 4.13b-54
- Prevent fixps tmpdir problem (bug #188156).

* Fri Jul 14 2006 Tim Waugh <twaugh@redhat.com> 4.13b-53
- Fixed Hebrew font names (bug #174304).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.13b-52
- rebuild
- exclude ppc64 as no emacs there right now.
- get rid of stupid ver and rel defines.

* Tue May 30 2006 Tim Waugh <twaugh@redhat.com> 4.13b-51
- Build requires gettext (bug #193346).

* Tue Apr  4 2006 Tim Waugh <twaugh@redhat.com> 4.13b-50
- Use sort correctly in make_font_map.sh (bug #187884).

* Wed Feb 15 2006 Tim Waugh <twaugh@redhat.com> 4.13b-49
- Use mktemp in scripts.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.13b-48.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.13b-48.2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 18 2005 Bill Nottingham <notting@redhat.com> 4.13b-48
- Migrate font paths from /usr/X11R6 to /usr/share/X11

* Thu May  5 2005 Tim Waugh <twaugh@redhat.com> 4.13b-47
- Make pdiff use diff(1) properly (bug #156916).

* Wed Mar 23 2005 Tim Waugh <twaugh@redhat.com> 4.13b-46
- Make pdiff default to not requiring wdiff (bug #68537).

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 4.13b-45
- Rebuild for new GCC.

* Wed Feb  2 2005 Tim Waugh <twaugh@redhat.com> 4.13b-44
- Don't try to run netscape.  Run mozilla instead (bug #121393).

* Thu Dec  9 2004 Tim Waugh <twaugh@redhat.com> 4.13b-43
- Fixed font path (bug #142294).
- Fixed problems in make_fonts_map script (bug #142299).  Patch from
  Michal Jaegermann.

* Tue Dec  7 2004 Tim Waugh <twaugh@redhat.com> 4.13b-42
- Fixed configure.in.
- Fixed m4 files.
- Apply patch from bug #122699 to fix "too many includes" error.

* Tue Oct  5 2004 Tim Waugh <twaugh@redhat.com> 4.13b-41
- Build requires texinfo (bug #134663).

* Thu Jul 29 2004 Tim Waugh <twaugh@redhat.com> 4.13b-40
- Use environment variable to pass filenames to shell (bug #128647).

* Thu Jun 24 2004 Tim Waugh <twaugh@redhat.com> 4.13b-39
- Build requires libtool (bug #125823).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 22 2004 Tim Waugh <twaugh@redhat.com> 4.13b-37
- Build requires flex (bug #118892).

* Wed Mar  3 2004 Tim Waugh <twaugh@redhat.com> 4.13b-36
- Oops, use system C compiler.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar  2 2004 Tim Waugh <twaugh@redhat.com> 4.13b-35
- Prevent "error: conflicting types for 'malloc'".

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Tim Waugh <twaugh@redhat.com> 4.13b-33
- Post scriptlet requires sed, coreutils (bug #107322).

* Mon Jan 12 2004 Tim Waugh <twaugh@redhat.com> 4.13b-32
- Hebrew support (bug #113191).

* Tue Jan  6 2004 Tim Waugh <twaugh@redhat.com> 4.13b-31
- Build requires gperf.
- Fix problems in .y file spotted by stricter bison.
- Fix reference to a2ps binary (bug #112930).

* Fri Oct 17 2003 Tim Waugh <twaugh@redhat.com> 4.13b-30
- Prevent strsignal segfaulting (bug #104970).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan  9 2003 Tim Waugh <twaugh@redhat.com> 4.13b-27
- Add Korean resource file (bug #81421).

* Tue Jan  7 2003 Jeff Johnson <jbj@redhat.com> 4.13b-26
- don't include -debuginfo files in package.

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches
- remove lingering files from the buildroot that we aren't shipping
- pass %%{_libdir} and %%{_datadir} to configure so that we are lib64'ized
- fix bad perms on some files

* Mon Aug  5 2002 Tim Waugh <twaugh@redhat.com> 4.13b-24
- Prevent configure from going interactive (bug #70333).
- Try to cope with UTF-8 a little bit (bug #70057).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 4.13b-23
- automated rebuild

* Fri Jun 21 2002 Tim Waugh <twaugh@redhat.com> 4.13b-22
- Fix koi8 tilde (bug #66393).

* Thu May 30 2002 Tim Waugh <twaugh@redhat.com> 4.13b-21
- Provide a2ps-i18n (bug #65231).
- Fix default encoding (bug #64584).

* Thu May 23 2002 Tim Powers <timp@redhat.com> 4.13b-20
- automated rebuild

* Mon Feb 25 2002 Tim Waugh <twaugh@redhat.com> 4.13b-19
- Rebuild in new environment.

* Tue Jan 22 2002 Tim Waugh <twaugh@redhat.com> 4.13b-18
- Fix a2ps-4.13-conf.patch (bug #31360).
- Add documentation about the default behaviour concerning LC_PAPER
  (bug #43829).

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 4.13b-17
- automated rebuild

* Wed Jan  9 2002 Tim Waugh <twaugh@redhat.com>
- Fix build with newer compiler.
- s/Copyright:/License:/.
- Use C locale's decimal point style (bug #53715).

* Fri Jun  1 2001 Oliver Paukstadt <oliver.paukstadt@millenux.com>
- fixed varargs-usage in title.c

* Thu Apr 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- call libtoolize to allow easy porting to new archs

* Wed Feb 28 2001 SATO Satoru <ssato@redhat.com>
- bunzip2-ed all patches except eucjp

* Thu Feb 22 2001 SATO Satoru <ssato@redhat.com>
- support Japanese
- bzip2-ed all patches
- replace macros (%%makeinstall, %%configure) with traditional 
  commands to avoid some troubles those macros caused.

* Tue Feb 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Using letter is as weird as oz, fl. oz, Fahrenheit, lb etc. 
  Add a patch for using the glibc media type for giving US
  letter for en_US (only locale with this paper), and A4
  for everyone else.

* Tue Feb 20 2001 Tim Powers <timp@redhat.com>
- changed default medium back to letter (bug 27794)

* Mon Feb 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- use %%{_tmppath}

* Mon Feb 12 2001 Tim Waugh <twaugh@redhat.com>
- Fix tmpfile security patch so that it actually _works_ (bug #27155).

* Sun Jan 21 2001 Tim Waugh <twaugh@redhat.com>
- New-style prereq line.
- %%post script requires fileutils (mv) and sh-utils (true).  This
  should fix bug #24251).

* Mon Jan 08 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add /usr/bin/emacs to BuildRequires
- A4
- specify use of GNU Emacs for building

* Fri Jan 05 2001 Preston Brown <pbrown@redhat.com>
- security patch for tmpfile creation from Olaf Kirch <okir@lst.de>

* Mon Dec 11 2000 Preston Brown <pbrown@redhat.com>
- obsoleted old a2ps-i18n package (it was tiny) and included those fonts
  directly here.

* Thu Dec  7 2000 Tim Powers <timp@redhat.com>
- built for dist-7.1

* Mon Aug 07 2000 Tim Powers <timp@redhat.com>
- update to 4.13b to fix some bugs, thanks to czar@acm.org for giving me a
  heads up on this (bug #15679)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jun 23 2000 Tim Powers <timp@redhat.com>
- info pages weren't getting gzipped.
- stdout & stderror redirected to /dev/null in post section

* Mon Jun 19 2000 Tim Powers <timp@redhat.com>
- fixed bug 12451 which was a stupid mistake by me.
- quiet the post section
- added patches from michal@ellpspace.math.ualberta.ca and did some spec file
  magic he suggested as well.

* Fri Jun 2 2000 Tim Powers <timp@redhat.com>
- fixed bug 5876, was not setting the paper size to Letter again :(
- man pages and info pages to /usr/share, FHS compliant.
- used macros wherever possible

* Wed May 31 2000 Tim Powers <timp@rehat.com>
- fixed bug #11078, now requires psutils

* Wed Apr 26 2000 Tim Powers <timp@redhat.com>
- updated to 4.13
- compress man pages

* Thu Feb 10 2000 Tim Powers <timp@redhat.com>
- gzip man pages
- strip binaries

* Mon Jan 24 2000 Tim Powers <timp@redhat.com>
- had to be more specific since the i18n stuff was removed from the package.
        There is a new a2ps-i18n package which treats the
        /usr/share/a2ps/afm/fonts.map file as a config file

* Wed Oct 27 1999 Tim Powers <timp@redhat.com>
- added the --with-medium=Letter option to the configure process

* Thu Aug 5 1999 Tim Powers <timp@redhat.com>
- fixed problems with missing dirs as reported in bug 3822
- built for powertools

* Tue Jul 6 1999 Tim Powers <timp@redhat.com>
- rebuilt for powertools 6.1

* Wed May 12 1999 Bill Nottingham <notting@redhat.com>
- add a2ps-site.cfg

* Mon Apr 26 1999 Preston Brown <pbrown@redhat.com>
- update to 4.12 for Powertools 6.0

* Sat Oct 24 1998 Jeff Johnson <jbj@redhat.com>
- narrower range of %%files splats.
- install info correctly.
- new description/summary text.

* Tue Oct 06 1998 Michael Maher <mike@redhat.com>
- updated source

* Sat Jul 04 1998 Michael Maher <mike@redhat.com>
- built package
