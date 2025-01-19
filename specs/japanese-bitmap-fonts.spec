%global	fontname        japanese-bitmap
%global cataloguedir    %{_sysconfdir}/X11/fontpath.d
%global cidmapdir       %{_datadir}/ghostscript/conf.d

%global chxlfd          /usr/bin/perl $RPM_BUILD_DIR/%{name}-%{version}/%{vft}/chbdfxlfd.pl
%global mkalias         /usr/bin/perl $RPM_BUILD_DIR/%{name}-%{version}/%{vft}/mkalias.pl
%global mkbold          $RPM_BUILD_DIR/%{name}-%{version}/%{shinonome}-src/tools/mkbold
%global mkitalic        $RPM_BUILD_DIR/%{name}-%{version}/%{vft}/mkitalic

%global kappa           Kappa20-0.396
%global shinonome       shinonome-0.9.11
%global warabi12        warabi12-0.19a
%global mplus           mplus_bitmap_fonts-2.2.4
%global vft             vine-fonttools-0.1

Name:           %{fontname}-fonts
Version:        0.20080710
Release:        41%{?dist}
License:        LicenseRef-Fedora-Public-Domain AND BSD-3-Clause AND mplus
BuildArch:      noarch
BuildRequires:  xorg-x11-font-utils mkfontdir gawk fontpackages-devel
BuildRequires:	gcc /usr/bin/perl
BuildRequires: make bdftopcf

## files in ttfonts-ja
Source2:        FAPIcidfmap.ja
Source3:        cidfmap.ja
Source4:        CIDFnmap.ja
## files in jisksp14
### Licensed under Public Domain
Source10:       jisksp14.bdf.gz
## files in kaname
### Licensed under Public Domain
Source41:       ftp://ftp.freebsd.org/pub/FreeBSD/ports/distfiles/kaname_k12_bdf.tar.gz
## files in fonts-ja
Source50:       xfonts_jp.tgz
### Licensed under Public Domain
Source51:       http://kappa.allnet.ne.jp/20dot.fonts/%{kappa}.tar.bz2
### Licensed under Public Domain
Source52:       http://openlab.ring.gr.jp/efont/dist/shinonome/%{shinonome}-src.tar.bz2
## http://mlnews.com/marumoji/
### Licensed under Public Domain
Source53:       marumoji.tgz
# JIS X 0213-2000 fonts (14pxl, 16pxl)
# http://www.mars.sphere.ne.jp/imamura/jisx0213.html
# http://www.mars.sphere.ne.jp/imamura/K14-1.bdf.gz
# http://www.mars.sphere.ne.jp/imamura/K14-2.bdf.gz
# http://www.mars.sphere.ne.jp/imamura/jiskan16-2000-1.bdf.gz
# http://www.mars.sphere.ne.jp/imamura/jiskan16-2000-2.bdf.gz
### Licensed under Public Domain
Source54:       imamura-jisx0213.tgz
# jiskan16 JIS X 0208:1990 by Yasuoka
# http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/
### Licensed under Public Domain
Source55:       http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jiskan16-1990.bdf.Z
# jiskan16 JIS X 0208:1997 Old Kanji
### Licensed under Public Domain
Source56:       http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jiskano16-1997.bdf.Z
# k14 Old-Kanji
### Licensed under Public Domain
Source57:       k14-oldkanji.tar.gz
## k14 invalid glyphs patch
## http://kappa.allnet.ne.jp/kanou/fonts/k14-patch.html
# Warabi12 (12pxl) jisx0213
# http://www.gelgoog.org/warabi12/
### Licensed under BSD
Source58:       http://www.gelgoog.org/warabi12/archives/%{warabi12}.tar.gz
# mplus fonts
# http://mplus-fonts.sourceforge.jp/
### Licensed under mplus
Source59:       http://osdn.dl.sourceforge.jp/mplus-fonts/5030/%{mplus}.tar.gz
Source60:       %{vft}.tgz
# jiskan24 JIS X 0213
# http://gitatsu.hp.infoseek.co.jp/bdf/
### Licensed under Public Domain
Source61:	http://gitatsu.hp.infoseek.co.jp/bdf/jiskan24-2000-1.bdf.gz
Source62:	http://gitatsu.hp.infoseek.co.jp/bdf/jiskan24-2000-2.bdf.gz
Source63:	http://gitatsu.hp.infoseek.co.jp/bdf/jiskan24-2003-1.bdf.gz

Patch50:        http://kappa.allnet.ne.jp/kanou/fonts/k14.patch
# k14 to jisx0208.1990 patch
# http://www.brl.ntt.co.jp/people/takada/goodies/k14-1990/
# http://www.brl.ntt.co.jp/people/takada/goodies/k14-1990/patch.txt
Patch51:        k14-1990.patch
Patch52:        fonts-ja-8.0-gcc-warnings.patch
Patch53:        mplus_bitmap_fonts-install.patch
Patch54:        fonttools-replace.patch
Patch55:        japanese-bitmap-fonts-c99.patch

Summary:        Free Japanese Bitmap fonts

Requires:	fontpackages-filesystem

%description
This package provides various free Japanese Bitmap fonts.


%prep
#%%setup -q -T -c -a 5 -a 40 -a 41 -a 50 -a 51 -a 52 -a 53 -a 54 -a 57 -a 58 -a 59 -a 60
%setup -q -T -c -a 41 -a 50 -a 51 -a 52 -a 53 -a 54 -a 57 -a 58 -a 59 -a 60
## ttfonts-ja
## jisksp14
gunzip -c %{SOURCE10} > jisksp14.bdf
## kappa20
## fonts-ja
gunzip -c %{SOURCE55} > jiskan16-1990.bdf
gunzip -c %{SOURCE56} > jiskano16-1997.bdf
%patch -P50 -p0
cp k14.bdf k14-1990.bdf
%patch -P51 -p0
%patch -P52 -p1
pushd %{mplus}
%patch -P53 -p1
popd
%patch -P54 -p1
%patch -P55 -p1
zcat %{SOURCE61} > jiskan24-2000-1.bdf
zcat %{SOURCE62} > jiskan24-2000-2.bdf
zcat %{SOURCE63} > jiskan24-2003-1.bdf

%build
## jisksp14
bdftopcf jisksp14.bdf | gzip -9 > jisksp14.pcf.gz
## kappa20
## fonts-ja
pushd %{shinonome}-src
%configure --disable-bold --disable-italic --with-fontdir=$RPM_BUILD_ROOT%{fontdir}
make bdf
popd
### rename Kappa and remove the bold fonts
pushd %{kappa}
  mv k20m.bdf k20.bdf
  mv 10x20rkm.bdf 10x20rk.bdf
  rm k20b.bdf 10x20rkb.bdf
popd
### rename in xfonts_jp
mv 7x14.bdf 7x14a.bdf
mv 8x16.bdf 8x16a.bdf
mv 12x24.bdf 12x24a.bdf
### marumoji
pushd marumoji
  for i in *.bdf; do
      %{chxlfd} $i '-Marumoji Club-Marumoji-.-.-.-.-.-.-.-.-.-.-.-.' $i.new && mv -f $i.new $i
  done
popd
### imamura jiskan16
pushd imamura-jisx0213
  for i in *.bdf; do
      %{chxlfd} $i '-Imamura-Fixed-.-.-.-.-.-.-.-.-.-.-.-.' $i.new && mv -f $i.new $i
  done
  mv K14-1.bdf k14-2000-1.bdf
  mv K14-2.bdf k14-2000-2.bdf
popd
### k14 and k14-1990 is used as Mincho
for i in k14.bdf k14-1990.bdf; do
    %{chxlfd} $i '-Misc-Mincho-.-.-.-.-.-.-.-.-.-.-.-.' $i.new && mv $i.new $i
done
### oldkanji
rm k14-oldkanji.pcf*
for i in k14-oldkanji.bdf jiskano16-1997.bdf; do
    %{chxlfd} $i '-Misc-.-.-.-.-Old Style-.-.-.-.-.-.-.-.' $i.new && mv $i.new $i
done
### warabi12
pushd %{warabi12}
  mv warabi12-1.bdf warabi12-2000-1.bdf
popd
### mplus
pushd %{mplus}
  DESTDIR=`pwd`/tmp/ ./install_mplus_fonts
popd

### move bdfs to topdir
mkdir fonts-ja
find -name "*.bdf" -path "./*/*" ! -path "./fonts-ja/*" ! -path "./fonts/*" -exec mv {} ./fonts-ja \;
mv k14-oldkanji.bdf jiskano16-1997.bdf k14-1990.bdf jiskan16-1990.bdf 7x14a.bdf 7x14rk.bdf 12x24a.bdf 12x24rk.bdf 8x16a.bdf 8x16rk.bdf k14.bdf jiskan16.bdf jiskan24*.bdf ./fonts-ja/
### move the documents to topdir
for i in */README */COPYRIGHT */{LICENSE,README}_{E,J}; do
    mv $i fonts-ja/`basename $i`-`dirname $i`
done

ALL_MEDIUM_BDF_FONT="\
  shnmk12maru/     maru14/-L        maru16/                        \
  k14-oldkanji/    jiskano16-1997/                                 \
  k14-1990/-L      jiskan16-1990/                                  \
  warabi12-2000-1/                                                 \
  k14-2000-1/-L    k14-2000-2/-L                                   \
  jiskan16-2000-1/ jiskan16-2000-2/                                \
  shnm6x12a/-r     shnm6x12r/-r     shnmk12/ shnmk12p/ shnmk12min/ \
  shnm8x16a/-r     shnm8x16r/-r     shnmk16/           shnmk16min/ \
  7x14a/           7x14rk/          shnmk14/ k14/-L    shnmk14min/ \
  8x16a/           8x16rk/          jiskan16/                      \
  shnm9x18a/-r     shnm9x18r/-r                                    \
  10x20rk/         k20/                                            \
  12x24a/          12x24rk/         jiskan24/                      \
  jiskan24-2000-1/ jiskan24-2000-2/ jiskan24-2003-1/
"
ALL_BOLD_BDF_FONT="\
mplus_f10WEIGHT-euro/-r mplus_f10WEIGHT/-r                             \
mplus_f12WEIGHT-euro/-r mplus_f12WEIGHT-jisx0201/-r mplus_f12WEIGHT/-r \
mplus_h10WEIGHT-euro/-r mplus_h10WEIGHT-jisx0201/-r mplus_h10WEIGHT/-r \
mplus_h12WEIGHT-euro/-r mplus_h12WEIGHT-jisx0201/-r mplus_h12WEIGHT/-r \
mplus_j10WEIGHT-iso/-r  mplus_j10WEIGHT-jisx0201/-r mplus_j10WEIGHT/-r \
mplus_j12WEIGHT/-r                                                     \
mplus_s10WEIGHT-euro/-r mplus_s10WEIGHT/-r
"
gcc $RPM_OPT_FLAGS %{vft}/mkitalic.c -o %{vft}/mkitalic

pushd fonts-ja
### delete 'r' from the filenames
for src in $ALL_BOLD_BDF_FONT; do
    mv `echo ${src%/*}.bdf | sed -e 's/WEIGHT/r/'` `echo ${src%/*}.bdf | sed -e 's/WEIGHT//'`
done

### making roman-bold fonts
for src in $ALL_MEDIUM_BDF_FONT; do
    %{mkbold} ${src#*/} -V ${src%/*}.bdf > ${src%/*}b.bdf
done
### making italic-medium fonts
for src in $ALL_MEDIUM_BDF_FONT; do
    %{mkitalic} -s 0.2 ${src%/*}.bdf > ${src%/*}i.bdf
done
for src in $ALL_BOLD_BDF_FONT; do
    %{mkitalic} -s 0.2 `echo ${src%/*}.bdf | sed -e 's/WEIGHT//'` > `echo ${src%/*}.bdf | sed -e 's/WEIGHT/i/'`
done
### making italic-bold fonts
for src in $ALL_MEDIUM_BDF_FONT; do
    %{mkbold} ${src#*/} -V ${src%/*}i.bdf > ${src%/*}bi.bdf
done
for src in $ALL_BOLD_BDF_FONT; do
    %{mkitalic} -s 0.2 `echo ${src%/*}.bdf | sed -e 's/WEIGHT/b/'` > `echo ${src%/*}.bdf | sed -e 's/WEIGHT/bi/'`
done

grep '^FONT ' *.bdf | sed -e 's/\.bdf:FONT//' > ALLFONTS.txt

### check the duplicated xlfds
DUP="`cut -d' ' -f2- ALLFONTS.txt | sort | uniq -d`"
if [ ! -z "$DUP" ]; then
    echo Duplicated XLFDs found. Please fix.
    echo -----------------------------------------
    echo "$DUP"
    exit 1
fi

cp ALLFONTS.txt mkalias.dat
# CHARSET PXL MISC FIXED MINCHO GOTHIC
# now, pixel 10 jisx0201 and pixel 20 gothic,
#      pixel 12 jisx0201 and pixel 24 gothic does not exist (fake)
%{mkalias} Misc-Fixed Alias-Fixed Alias-Gothic Alias-Mincho - \
ISO8859-1       10 mplus_f10WEIGHT mplus_f10WEIGHT mplus_j10WEIGHT - \
ISO8859-1       12 shnm6x12a shnm6x12a shnm6x12a shnm6x12a \
ISO8859-1       14 7x14a 7x14a 7x14a 7x14a \
ISO8859-1       16 shnm8x16a shnm8x16a shnm8x16a shnm8x16a \
ISO8859-1       18 shnm9x18a shnm9x18a shnm9x18a shnm9x18a \
ISO8859-1       20 10x20rk 10x20rk - 10x20rk \
ISO8859-1       24 12x24a 12x24a - 12x24a \
JISX0201.1976-0 10 mplus_j10WEIGHT-jisx0201 mplus_j10WEIGHT-jisx0201 mplus_j10WEIGHT-jisx0201 mplus_j10WEIGHT-jisx0201 \
JISX0201.1976-0 12 shnm6x12r shnm6x12r shnm6x12r shnm6x12r \
JISX0201.1976-0 14 7x14rk 7x14rk 7x14rk 7x14rk \
JISX0201.1976-0 16 shnm8x16r shnm8x16r shnm8x16r shnm8x16r \
JISX0201.1976-0 18 shnm9x18r shnm9x18r shnm9x18r shnm9x18r \
JISX0201.1976-0 20 10x20rk 10x20rk - 10x20rk \
JISX0201.1976-0 24 12x24rk 12x24rk - 12x24rk \
JISX0208.1983-0 10 mplus_j10WEIGHT mplus_j10WEIGHT mplus_j10WEIGHT - \
JISX0208.1983-0 12 shnmk12 shnmk12 shnmk12 shnmk12min \
JISX0208.1983-0 14 shnmk14 shnmk14 shnmk14 k14 \
JISX0208.1983-0 16 shnmk16 shnmk16 shnmk16 shnmk16min \
JISX0208.1983-0 20 - - - k20 \
JISX0208.1983-0 24 - - - jiskan24 \
JISX0208.1990-0 10 mplus_j10WEIGHT mplus_j10WEIGHT mplus_j10WEIGHT - \
JISX0213.2000-1 12 warabi12-2000-1 warabi12-2000-1 warabi12-2000-1 warabi12-2000-1 \
JISX0213.2000-1 14 k14-2000-1 k14-2000-1 k14-2000-1 k14-2000-1 \
JISX0213.2000-2 14 k14-2000-2 k14-2000-2 k14-2000-2 k14-2000-2 \
JISX0213.2000-1 16 jiskan16-2000-1 jiskan16-2000-1 jiskan16-2000-1 jiskan16-2000-1 \
JISX0213.2000-2 16 jiskan16-2000-2 jiskan16-2000-2 jiskan16-2000-2 jiskan16-2000-2 \
JISX0213.2000-1 24 jiskan24-2000-1 jiskan24-2000-1 jiskan24-2000-1 jiskan24-2000-1 \
JISX0213.2000-2 24 jiskan24-2000-2 jiskan24-2000-2 jiskan24-2000-2 jiskan24-2000-2 \
JISX0213.2003-1 24 jiskan24-2003-1 jiskan24-2003-1 jiskan24-2003-1 jiskan24-2003-1 \
> fonts.alias
mkdir BDFS
for src in *.bdf; do
    bdftopcf $src | gzip -9 > ${src%.bdf}.pcf.gz && mv $src BDFS/
done
popd

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{cidmapdir}

## jisksp14
install -m 0644 -p jisksp14.pcf* $RPM_BUILD_ROOT%{_fontdir}/

## kappa20

## knm_new
for i in knmhn12x.bdf knmzn12x.bdf; do
    bdftopcf $i | gzip -9 > $RPM_BUILD_ROOT%{_fontdir}/`basename $i | sed -e 's/.bdf/.pcf.gz/'`
done

## fonts-ja
### remove an unnecessary file
rm -f fonts-ja/mplus_cursors.pcf.gz
for i in fonts-ja/*.pcf.gz; do
    install -m 0644 -p $i $RPM_BUILD_ROOT%{_fontdir}/`basename $i`
done

# for ghostscript
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{cidmapdir}/
install -m 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{cidmapdir}/
install -m 0644 -p %{SOURCE4} $RPM_BUILD_ROOT%{cidmapdir}/

# Create fonts.scale and fonts.dir
/usr/bin/mkfontdir $RPM_BUILD_ROOT%{_fontdir}
# for dummy
touch $RPM_BUILD_ROOT%{_fontdir}/encodings.dir

install -m 0644 -p fonts-ja/fonts.alias $RPM_BUILD_ROOT%{_fontdir}/

# Install catalogue symlink
install -m 0755 -d $RPM_BUILD_ROOT%{cataloguedir}
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{cataloguedir}/%{fontname}

%_font_pkg *.pcf.gz

%doc doc.orig readme.kaname_bdf
%doc fonts-ja/README* fonts-ja/ALLFONTS.txt
%license fonts-ja/COPYRIGHT* fonts-ja/LICENSE*
%verify(not md5 size mtime) %{_fontdir}/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%ghost %verify(not md5 size mtime) %{_fontdir}/encodings.dir
%{cidmapdir}/FAPIcidfmap.ja
%{cidmapdir}/cidfmap.ja
%{cidmapdir}/CIDFnmap.ja
%{cataloguedir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 0.20080710-36
- Fix C99 compatibility issue (#2167285)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  1 2022 Akira TAGOH <tagoh@redhat.com> - 0.20080710-34
- Convert License tag to SPDX.

* Wed Nov  2 2022 Akira TAGOH <tagoh@redhat.com> - 0.20080710-33
- Drop old Provides/Obsoletes lines.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Akira TAGOH <tagoh@redhat.com> - 0.20080710-30
- Add bdftopcf to BR and update BR for perl.
  Resolves: rhbz#2021739

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Akira TAGOH <tagoh@redhat.com> - 0.20080710-26
- Add BR: perl

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com> - 0.20080710-21
- Add BR: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080710-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar  2 2010 Akira TAGOH <tagoh@redhat.com> - 0.20080710-9
- Stop owning the unnecessary directory. (#569452)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Akira TAGOH <tagoh@redhat.com> - 0.20080710-6
- Contains the correct fonts from kaname. (#505757)
- Correct FAPIcidfmap.ja, cidfmap.ja and CIDFnmap.ja (#499634)

* Fri Mar 27 2009 Akira TAGOH <tagoh@redhat.com> - 0.20080710-5
- Clean up a spec file.
- Rebuilt (#491963)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080710-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Akira TAGOH <tagoh@redhat.com> - 0.20080710-3
- Get rid of the unreachable URL in source.
- Fix a source URL.

* Thu Jul 10 2008 Akira TAGOH <tagoh@redhat.com> - 0.20080710-1
- Renamed package from fonts-japanese. (#253149)
- Get rid of ttf font packages' dependencies.
- clean up the spec file a bit.

* Tue Apr  8 2008 Akira TAGOH <tagoh@redhat.com> - 0.20061016-13
- Add VLGothic-fonts deps and drop sazanami-fonts-gothic.

* Wed Sep 26 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-12
- Remove jisksp16-1990 and knm_new fonts so that it has been packaged separately.
- clean up the spec file.

* Fri Aug 31 2007 Akira TAGOH <tagoh@redhat.com>
- Add jiskan24-2000-{1,2} and jiskan24-2003-1.

* Thu Aug 30 2007 Akira TAGOH <tagoh@redhat.com>
- drop BR gzip

* Wed Aug 29 2007 Akira TAGOH <tagoh@redhat.com>
- clean up the spec file.

* Tue Aug 28 2007 Jens Petersen <petersen@redhat.com> - 0.20061016-11
- use the standard font scriptlets (Michal Jaegermann, #259041)

* Mon Aug 27 2007 Jens Petersen <petersen@redhat.com> - 0.20061016-10
- sazanami fonts have been moved to a new package sazanami-fonts (#253149)

* Wed Aug 22 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-9
- No need to own /etc/X11/fontpath.d.
- Update BR.

* Wed Aug 15 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-8
- Migrate to /etc/X11/fontpath.d instead of running chkfontpath. (#252275)
- Generate fonts.dir at the build time instead of the runtime.
- Drop fc-cache dependency since it's a conditional scriptlet.

* Tue Aug 14 2007 Akira TAGOH <tagoh@redhat.com>
- Update License tag.

* Thu Apr 12 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-6
- Remove %%config from the files under /usr/share/ghostscript/conf.d.
- clean up more in spec file.

* Tue Apr 10 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-5
- Move the configuration files for ghostscript under /usr/share/ghostscript/conf.d

* Thu Mar 15 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-4
- more cleanups. (#225765)

* Thu Mar  1 2007 Akira TAGOH <tagoh@redhat.com> - 0.20061016-3
- cleanup spec file.
- updated mplus to 2.2.4

* Fri Nov 24 2006 Akira TAGOH <tagoh@redhat.com> - 0.20061016-2
- added CIDFnmap.ja (#215980)

* Fri Oct 27 2006 Akira TAGOH <tagoh@redhat.com> - 0.20061016-1
- correct U+7E6B. (#196433)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.20050222-11.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 17 2005 Warren Togami <wtogami@redhat.com> - 0.20050222-11
- split req(foo,bar) for erasure ordering

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> - 0.20050222-10
- better mkfontdir

* Mon Nov 14 2005 Warren Togami <wtogami@redhat.com> - 0.20050222-9
- rebuild against modular X

* Mon Nov  7 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-8
- rely on PATH to find mkfontdir instead of /usr/X11R6/bin hardcoded.
- replace Requires: mkfontdir instead of /usr/X11R6/bin/mkfontdir.

* Tue Aug 16 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-7
- Added cidfmap.ja for the latest ghostscript.
- Removed Kochi fonts.

* Tue Aug  2 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-6
- contain Sazanami fonts.

* Thu Jul 14 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-5
- use FAPIcidfmap instead of CIDFnmap for gs8.

* Thu Jun  9 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-4
- removed VFlib2 dependency.

* Wed Apr 20 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-3
- Updated the font path in CIDFnmap.ja (John Thacker, #155403)

* Thu Feb 24 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-2
- Use /usr/share/fonts/japanese instead of /usr/share/fonts/ja

* Tue Feb 22 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050222-1
- gets back Kochi font temporarily.

* Thu Feb 10 2005 Akira TAGOH <tagoh@redhat.com> - 0.20050210-1
- Initial release.
- integrated the below packages:
  - ttfonts-ja
  - jisksp14
  - jisksp16-1990
  - kappa20
  - knm_new
  - fonts-ja
- Update shinonome font to 0.9.11.
- Use Sazanami fonts instead of Kochi fonts.
