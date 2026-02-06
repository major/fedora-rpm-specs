%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langkorean
Epoch:          12
Version:        svn54074
Release:        3%{?dist}
Summary:        Korean

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langkorean.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baekmuk.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/baekmuk.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-ko.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-ko.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-oblivoir.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-oblivoir.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-plain.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-plain.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-utf.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-utf.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-korean.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-korean.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanumtype1.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanumtype1.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmhanguljamo.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmhanguljamo.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhc.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-core.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-core.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-extra.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unfonts-extra.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-langcjk
Requires:       texlive-baekmuk
Requires:       texlive-cjk-ko
Requires:       texlive-kotex-oblivoir
Requires:       texlive-kotex-plain
Requires:       texlive-kotex-utf
Requires:       texlive-kotex-utils
Requires:       texlive-lshort-korean
Requires:       texlive-nanumtype1
Requires:       texlive-pmhanguljamo
Requires:       texlive-uhc
Requires:       texlive-unfonts-core
Requires:       texlive-unfonts-extra

%description
Support for Korean; additional packages in collection-langcjk.


%package -n texlive-baekmuk
Summary:        Baekmuk Korean TrueType fonts
Version:        svn56915
License:        Baekmuk
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-baekmuk
This bundle consists of four Korean fonts: batang.ttf: serif dotum.ttf:
sans-serif gulim.ttf: sans-serif (rounded) hline.ttf: headline These fonts were
originally retrieved from http://kldp.net/baekmuk/ and are no longer
maintained.

%package -n texlive-cjk-ko
Summary:        Extension of the CJK package for Korean typesetting
Version:        svn70300
License:        GPL-2.0-or-later AND LPPL-1.3c AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cjk
Requires:       tex(CJKfntef.sty)
# Ignoring dependency on kotex-euc.sty - not part of TeX Live
Requires:       tex(kotexutf.sty)
Requires:       tex(luatexko.sty)
Requires:       tex(ulem.sty)
Requires:       tex(xetexko.sty)
Provides:       tex(cjkutf8-josa.sty) = %{tl_version}
Provides:       tex(cjkutf8-ko.sty) = %{tl_version}
Provides:       tex(cjkutf8-nanummjhanja.sty) = %{tl_version}
Provides:       tex(kolabels-utf.sty) = %{tl_version}
Provides:       tex(konames-utf.sty) = %{tl_version}
Provides:       tex(kotex.sty) = %{tl_version}

%description -n texlive-cjk-ko
The package supports typesetting UTF-8-encoded modern Korean documents with the
help of the LaTeX2e CJK package. It provides some enhanced features focused on
Korean typesetting culture, one of them being allowing line-break between Latin
and CJK characters. The package requires nanumtype1 fonts.

%package -n texlive-kotex-oblivoir
Summary:        A LaTeX document class for typesetting Korean documents
Version:        svn76503
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-kotex-utf
Requires:       texlive-memoir
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(cjkutf8-ko.sty)
Requires:       tex(dhucs-paralist.sty)
Requires:       tex(dhucs.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kolabels-utf.sty)
Requires:       tex(kotex.sty)
Requires:       tex(luatexko.sty)
Requires:       tex(memhfixc.sty)
Requires:       tex(paralist.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(xetexko-font.sty)
Requires:       tex(xetexko-josa.sty)
Requires:       tex(xetexko-space.sty)
Requires:       tex(xetexko-vertical.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(10_5.sty) = %{tl_version}
Provides:       tex(fapapersize.sty) = %{tl_version}
Provides:       tex(hfontsel.sty) = %{tl_version}
Provides:       tex(memhangul-common.sty) = %{tl_version}
Provides:       tex(memhangul-patch.sty) = %{tl_version}
Provides:       tex(memhangul-ucs.sty) = %{tl_version}
Provides:       tex(memhangul-x.sty) = %{tl_version}
Provides:       tex(memucs-enumerate.sty) = %{tl_version}
Provides:       tex(memucs-gremph.sty) = %{tl_version}
Provides:       tex(memucs-interword-x.sty) = %{tl_version}
Provides:       tex(memucs-interword.sty) = %{tl_version}
Provides:       tex(memucs-setspace.sty) = %{tl_version}
Provides:       tex(nanumfontsel.sty) = %{tl_version}
Provides:       tex(ob-koreanappendix.sty) = %{tl_version}
Provides:       tex(ob-mathleading.sty) = %{tl_version}
Provides:       tex(ob-nokoreanappendix.sty) = %{tl_version}
Provides:       tex(ob-toclof.sty) = %{tl_version}
Provides:       tex(ob-unfontsdefault.sty) = %{tl_version}
Provides:       tex(obchapterstyles.sty) = %{tl_version}
Provides:       tex(obchaptertoc.sty) = %{tl_version}
Provides:       tex(oblivoir-misc.sty) = %{tl_version}
Provides:       tex(xetexko-var.sty) = %{tl_version}
Provides:       tex(xob-amssymb.sty) = %{tl_version}
Provides:       tex(xob-dotemph.sty) = %{tl_version}
Provides:       tex(xob-font.sty) = %{tl_version}
Provides:       tex(xob-hyper.sty) = %{tl_version}
Provides:       tex(xob-lwarp.sty) = %{tl_version}
Provides:       tex(xob-paralist.sty) = %{tl_version}

%description -n texlive-kotex-oblivoir
The class is based on memoir, and is adapted to typesetting Korean documents.
The bundle (of class and associated packages) belongs to the ko.TeX bundle. It
depends on memoir and kotex-utf to function.

%package -n texlive-kotex-plain
Summary:        Macros for typesetting Korean under Plain TeX
Version:        svn63689
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hangulcweb.tex) = %{tl_version}
Provides:       tex(kotexplain.tex) = %{tl_version}
Provides:       tex(kotexutf-core.tex) = %{tl_version}
Provides:       tex(kotexutf.tex) = %{tl_version}

%description -n texlive-kotex-plain
The package provides macros for typesetting Hangul, the native alphabet of the
Korean language, using plain *TeX. Input Korean text should be encoded in
UTF-8. The package belongs to the ko.TeX bundle.

%package -n texlive-kotex-utf
Summary:        Typeset Hangul, coded in UTF-8
Version:        svn63690
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cjk-ko
Requires:       tex(enumerate.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fnpara.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kolabels-utf.sty)
Requires:       tex(luatexko.sty)
Requires:       tex(paralist.sty)
Requires:       tex(sectsty.sty)
Requires:       tex(setspace.sty)
Requires:       tex(varioref.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xetexko.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(dhucs-cmap.sty) = %{tl_version}
Provides:       tex(dhucs-enumerate.sty) = %{tl_version}
Provides:       tex(dhucs-enumitem.sty) = %{tl_version}
Provides:       tex(dhucs-gremph.sty) = %{tl_version}
Provides:       tex(dhucs-interword.sty) = %{tl_version}
Provides:       tex(dhucs-nanumfont.sty) = %{tl_version}
Provides:       tex(dhucs-paralist.sty) = %{tl_version}
Provides:       tex(dhucs-sectsty.sty) = %{tl_version}
Provides:       tex(dhucs-setspace.sty) = %{tl_version}
Provides:       tex(dhucs-trivcj.sty) = %{tl_version}
Provides:       tex(dhucs-ucshyper.sty) = %{tl_version}
Provides:       tex(dhucs.sty) = %{tl_version}
Provides:       tex(dhucsfn.sty) = %{tl_version}
Provides:       tex(kosections-utf.sty) = %{tl_version}
Provides:       tex(kotex-logo.sty) = %{tl_version}
Provides:       tex(kotex-sections.sty) = %{tl_version}
Provides:       tex(kotex-varioref.sty) = %{tl_version}
Provides:       tex(kotexutf.sty) = %{tl_version}

%description -n texlive-kotex-utf
The package typesets Hangul, which is the native alphabet of the Korean
language; input Korean text should be encoded in UTF-8. The bundle (of class
and associated packages) belongs to the ko.TeX bundle.

%package -n texlive-lshort-korean
Summary:        Korean introduction to LaTeX
Version:        svn73814
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-korean-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-korean-doc <= 11:%{version}

%description -n texlive-lshort-korean
A translation of Oetiker's original (not so) short introduction.

%package -n texlive-nanumtype1
Summary:        Type1 subfonts of Nanum Korean fonts
Version:        svn29558
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nanumtype1
Nanum is a unicode font designed especially for Korean-language script. The
font was designed by Sandoll Communication and Fontrix; it includes the sans
serif (gothic), serif (myeongjo), pen script and brush script typefaces. The
package provides Type1 subfonts converted from Nanum Myeongjo (Regular and
ExtraBold) and Nanum Gothic (Regular and Bold) OTFs. C70, LUC, T1, and TS1 font
definition files are also provided. (The package does not include
OpenType/TrueType files, which are available from Naver)

%package -n texlive-pmhanguljamo
Summary:        Poor man's Hangul Jamo input method
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(frkjamofull.data.tex) = %{tl_version}
Provides:       tex(pmhanguljamo-frkim.code.tex) = %{tl_version}
Provides:       tex(pmhanguljamo-frkim.sty) = %{tl_version}
Provides:       tex(pmhanguljamo-rrk.sty) = %{tl_version}
Provides:       tex(pmhanguljamo.sty) = %{tl_version}

%description -n texlive-pmhanguljamo
This package provides a Hangul transliteration input method that allows to
typeset Korean letters (Hangul) using the proper fonts. The name is derived
from "Poor man's Hangul Jamo Input Method". The use of XeLaTeX is recommended.
pdfTeX is not supported.

%package -n texlive-uhc
Summary:        Fonts for the Korean language
Version:        svn16791
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uhc
Support for Korean documents written in Korean standard KSC codes for LaTeX2e.

%package -n texlive-unfonts-core
Summary:        TrueType version of Un-fonts
Version:        svn56291
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unfonts-core
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by Koaunghi Un, he
made type1 fonts to use with Korean TeX (HLaTeX) in the late 1990's and
released it under the GPL license. They were converted to TrueType with the
FontForge (PfaEdit) by Won-kyu Park in 2003. Core families (9 fonts): UnBatang,
UnBatangBold: serif UnDotum, UnDotumBold: sans-serif UnGraphic, UnGraphicBold:
sans-serif style UnPilgi, UnPilgiBold: script UnGungseo: cursive, brush-stroke

%package -n texlive-unfonts-extra
Summary:        TrueType version of Un-fonts
Version:        svn56291
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-unfonts-extra
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by Koaunghi Un, he
made type1 fonts to use with Korean TeX (HLaTeX) in the late 1990's and
released it under the GPL license. They were converted to TrueType with the
FontForge (PfaEdit) by Won-kyu Park in 2003. Extra families (10 fonts): UnPen,
UnPenheulim: script UnTaza: typewriter style UnBom: decorative UnShinmun
UnYetgul: old Korean printing style UnJamoSora, UnJamoNovel, UnJamoDotum,
UnJamoBatang


%prep
# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE3} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE4} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE5} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE6} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE7} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE8} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE9} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE10} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE11} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE12} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE13} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE14} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE15} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE16} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE17} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE18} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE19} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE20} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE21} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE22} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE23} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-baekmuk
%license other-free.txt
%{_texmf_main}/fonts/truetype/public/baekmuk/
%doc %{_texmf_main}/doc/fonts/baekmuk/

%files -n texlive-cjk-ko
%license gpl2.txt
%license lppl1.3c.txt
%license pd.txt
%{_texmf_main}/tex/latex/cjk-ko/
%doc %{_texmf_main}/doc/latex/cjk-ko/

%files -n texlive-kotex-oblivoir
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kotex-oblivoir/
%doc %{_texmf_main}/doc/latex/kotex-oblivoir/

%files -n texlive-kotex-plain
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/kotex-plain/
%doc %{_texmf_main}/doc/plain/kotex-plain/

%files -n texlive-kotex-utf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kotex-utf/
%doc %{_texmf_main}/doc/latex/kotex-utf/

%files -n texlive-lshort-korean
%license fdl.txt
%doc %{_texmf_main}/doc/latex/lshort-korean/

%files -n texlive-nanumtype1
%license ofl.txt
%{_texmf_main}/fonts/afm/public/nanumtype1/
%{_texmf_main}/fonts/map/dvips/nanumtype1/
%{_texmf_main}/fonts/tfm/public/nanumtype1/
%{_texmf_main}/fonts/type1/public/nanumtype1/
%{_texmf_main}/fonts/vf/public/nanumtype1/
%{_texmf_main}/tex/latex/nanumtype1/
%doc %{_texmf_main}/doc/fonts/nanumtype1/

%files -n texlive-pmhanguljamo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pmhanguljamo/
%doc %{_texmf_main}/doc/latex/pmhanguljamo/

%files -n texlive-uhc
%license lppl1.3c.txt
%{_texmf_main}/dvips/uhc/
%{_texmf_main}/fonts/afm/uhc/umj/
%{_texmf_main}/fonts/map/dvips/uhc/
%{_texmf_main}/fonts/tfm/uhc/umj/
%{_texmf_main}/fonts/tfm/uhc/uwmj/
%{_texmf_main}/fonts/tfm/uhc/wmj/
%{_texmf_main}/fonts/type1/uhc/umj/
%{_texmf_main}/fonts/vf/uhc/uwmj/
%{_texmf_main}/fonts/vf/uhc/wmj/
%doc %{_texmf_main}/doc/fonts/uhc/

%files -n texlive-unfonts-core
%license gpl2.txt
%{_texmf_main}/fonts/truetype/public/unfonts-core/
%doc %{_texmf_main}/doc/fonts/unfonts-core/

%files -n texlive-unfonts-extra
%license gpl2.txt
%{_texmf_main}/fonts/truetype/public/unfonts-extra/
%doc %{_texmf_main}/doc/fonts/unfonts-extra/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-3
- fix licensing, descriptions
- update to latest pmhanguljamo

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-1
- Update to TeX Live 2025
