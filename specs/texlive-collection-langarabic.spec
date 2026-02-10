%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langarabic
Epoch:          12
Version:        svn76980
Release:        2%{?dist}
Summary:        Arabic

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langarabic.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alkalami.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alkalami.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alpha-persian.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/alpha-persian.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amiri.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amiri.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabi.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabi.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabi-add.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabi-add.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabic-book.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabic-book.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabluatex.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabluatex.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabtex.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabtex.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/awami.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/awami.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidihl.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidihl.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dad.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dad.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ghab.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ghab.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hvarabic.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hvarabic.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-arabic.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-farsi.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imsproc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/imsproc.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iran-bibtex.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iran-bibtex.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/khatalmaqala.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/khatalmaqala.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kurdishlipsum.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kurdishlipsum.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-persian.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-persian.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luabidi.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luabidi.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mohe-book.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mohe-book.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/na-box.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/na-box.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parsimatn.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parsimatn.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parsinevis.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parsinevis.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/persian-bib.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/persian-bib.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sexam.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sexam.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simurgh.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simurgh.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texnegar.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texnegar.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tram.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tram.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xepersian.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xepersian.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xepersian-hm.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xepersian-hm.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xindy-persian.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xindy-persian.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-alkalami
Requires:       texlive-alpha-persian
Requires:       texlive-amiri
Requires:       texlive-arabi
Requires:       texlive-arabi-add
Requires:       texlive-arabic-book
Requires:       texlive-arabluatex
Requires:       texlive-arabtex
Requires:       texlive-awami
Requires:       texlive-bidi
Requires:       texlive-bidihl
Requires:       texlive-collection-basic
Requires:       texlive-dad
Requires:       texlive-ghab
Requires:       texlive-hvarabic
Requires:       texlive-hyphen-arabic
Requires:       texlive-hyphen-farsi
Requires:       texlive-imsproc
Requires:       texlive-iran-bibtex
Requires:       texlive-khatalmaqala
Requires:       texlive-kurdishlipsum
Requires:       texlive-lshort-persian
Requires:       texlive-luabidi
Requires:       texlive-mohe-book
Requires:       texlive-na-box
Requires:       texlive-parsimatn
Requires:       texlive-parsinevis
Requires:       texlive-persian-bib
Requires:       texlive-quran
Requires:       texlive-sexam
Requires:       texlive-simurgh
Requires:       texlive-texnegar
Requires:       texlive-tram
Requires:       texlive-xepersian
Requires:       texlive-xepersian-hm
Requires:       texlive-xindy-persian

%description
Support for Arabic and Persian.


%package -n texlive-alkalami
Summary:        A font for Arabic-based writing systems in Nigeria and Niger
Version:        svn44497
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-alkalami
This font is designed for Arabic-based writing systems in the Kano region of
Nigeria and Niger.

%package -n texlive-alpha-persian
Summary:        Persian version of alpha.bst
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-alpha-persian
The package provides a Persian version of the alpha BibTeX style and offers
several enhancements. It is compatible with the hyperref, url, natbib, and cite
packages.

%package -n texlive-amiri
Summary:        A classical Arabic typeface, Naskh style
Version:        svn65191
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-amiri
Amiri is a classical Arabic typeface in Naskh style for typesetting books and
other running text. It is a revival of the beautiful typeface pioneered in the
early 20th century by Bulaq Press in Cairo, also known as Amiria Press, after
which the font is named. The project aims at the revival of the aesthetics and
traditions of Arabic typesetting, and adapting it to the era of digital
typesetting, in a publicly available form.

%package -n texlive-arabi
Summary:        (La)TeX support for Arabic and Farsi, compliant with Babel
Version:        svn44662
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(pifont.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-key.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(8859-6.def) = %{tl_version}
Provides:       tex(PPRarabic.sty) = %{tl_version}
Provides:       tex(arabic.ldf) = %{tl_version}
Provides:       tex(arabicfnt.sty) = %{tl_version}
Provides:       tex(arabicore.sty) = %{tl_version}
Provides:       tex(arabiftoday.sty) = %{tl_version}
Provides:       tex(arabipoetry.sty) = %{tl_version}
Provides:       tex(arabnovowel.sty) = %{tl_version}
Provides:       tex(arfonts.sty) = %{tl_version}
Provides:       tex(calendrierfpar.sty) = %{tl_version}
Provides:       tex(calendrierfpmodified.sty) = %{tl_version}
Provides:       tex(cp1256.def) = %{tl_version}
Provides:       tex(farsi.ldf) = %{tl_version}
Provides:       tex(farsifnt.sty) = %{tl_version}
Provides:       tex(fmultico.sty) = %{tl_version}
Provides:       tex(fnum.sty) = %{tl_version}
Provides:       tex(frfonts.sty) = %{tl_version}
Provides:       tex(haparabica.sty) = %{tl_version}
Provides:       tex(laeenc.def) = %{tl_version}
Provides:       tex(lagally.sty) = %{tl_version}
Provides:       tex(lfeenc.def) = %{tl_version}
Provides:       tex(mosq.def) = %{tl_version}
Provides:       tex(puenc-ar.def) = %{tl_version}
Provides:       tex(translit.sty) = %{tl_version}

%description -n texlive-arabi
The package provides an Arabic and Farsi script support for TeX without the
need of any external pre-processor, and in a way that is compatible with babel.
The bi-directional capability supposes that the user has a TeX engine that
knows the four primitives \beginR, \endR, \beginL and \endL. That is the case
in both the TeX--XeT and e-TeX engines. Arabi will accept input in several
8-bit encodings, including UTF-8. Arabi can make use of a wide variety of
Arabic and Farsi fonts, and provides one of its own. PDF files generated using
Arabi may be searched, and text may be copied from them and pasted elsewhere.

%package -n texlive-arabi-add
Summary:        Using hyperref and bookmark packages with arabic and farsi languages
Version:        svn67573
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsthm.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(datatool.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(arabi-add.sty) = %{tl_version}

%description -n texlive-arabi-add
This package takes advantage of some of the possibilities that hyperref and
bookmark packages offer when you create a table of contents for Arabic texts
created by the arabi package.

%package -n texlive-arabic-book
Summary:        An Arabic book class
Version:        svn59594
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-arabic-book
This document class provides both Arabic and English support for TeX/LaTeX.
Input may be in ASCII transliteration or other encodings (including UTF-8), and
output may be Arabic, Hebrew, or any of several languages that use the Arabic
script, as can be specified by the polyglossia package. The Arabic font is
presently available in any Arabic fonts style. In order to use Amiri font
style, the user needs to install the amiri package. This document class runs
with the XeTeX engine. PDF files generated using this class can be searched,
and text can be copied from them and pasted elsewhere.

%package -n texlive-arabluatex
Summary:        ArabTeX for LuaLaTeX
Version:        svn67201
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(lua-ul.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luacolor.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(arabluatex-patch.sty) = %{tl_version}
Provides:       tex(arabluatex.sty) = %{tl_version}

%description -n texlive-arabluatex
This package provides for LuaLaTeX an ArabTeX-like interface to generate Arabic
writing from an ascii transliteration. It is particularly well-suited for
complex documents such as technical documents or critical editions where a lot
of left-to-right commands intertwine with Arabic writing. arabluatex is able to
process any ArabTeX input notation. Its output can be set in the same modes of
vocalization as ArabTeX, or in different roman transliterations. It further
allows many typographical refinements. It will eventually interact with some
other packages yet to come to produce from .tex source files, in addition to
printed books, TEI xml compliant critical editions and/or lexicons that can be
searched, analyzed and correlated in various ways.

%package -n texlive-arabtex
Summary:        Macros and fonts for typesetting Arabic
Version:        svn64260
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(abidir.sty) = %{tl_version}
Provides:       tex(abjad.sty) = %{tl_version}
Provides:       tex(aboxes.sty) = %{tl_version}
Provides:       tex(acjk.sty) = %{tl_version}
Provides:       tex(acmd.sty) = %{tl_version}
Provides:       tex(aconfig.sty) = %{tl_version}
Provides:       tex(aedpatch.sty) = %{tl_version}
Provides:       tex(afonts.sty) = %{tl_version}
Provides:       tex(afonts0.sty) = %{tl_version}
Provides:       tex(afonts1.sty) = %{tl_version}
Provides:       tex(afonts2.sty) = %{tl_version}
Provides:       tex(afoot.sty) = %{tl_version}
Provides:       tex(alatex.sty) = %{tl_version}
Provides:       tex(aligs.sty) = %{tl_version}
Provides:       tex(alists.sty) = %{tl_version}
Provides:       tex(alocal.sty) = %{tl_version}
Provides:       tex(altxext.sty) = %{tl_version}
Provides:       tex(amac.sty) = %{tl_version}
Provides:       tex(aoutput.sty) = %{tl_version}
Provides:       tex(aparse.sty) = %{tl_version}
Provides:       tex(apatch.sty) = %{tl_version}
Provides:       tex(arababel.sty) = %{tl_version}
Provides:       tex(arabaux.sty) = %{tl_version}
Provides:       tex(arabchrs.sty) = %{tl_version}
Provides:       tex(arabext.sty) = %{tl_version}
Provides:       tex(arabskel.sty) = %{tl_version}
Provides:       tex(arabsymb.sty) = %{tl_version}
Provides:       tex(arabtex.sty) = %{tl_version}
Provides:       tex(arabtex.tex) = %{tl_version}
Provides:       tex(arabtoks.sty) = %{tl_version}
Provides:       tex(ascan.sty) = %{tl_version}
Provides:       tex(asect.sty) = %{tl_version}
Provides:       tex(asmo449.sty) = %{tl_version}
Provides:       tex(asmo449a.sty) = %{tl_version}
Provides:       tex(atabg.sty) = %{tl_version}
Provides:       tex(atrans.sty) = %{tl_version}
Provides:       tex(awrite.sty) = %{tl_version}
Provides:       tex(bhs.sty) = %{tl_version}
Provides:       tex(bhslabel.sty) = %{tl_version}
Provides:       tex(buck.sty) = %{tl_version}
Provides:       tex(captions.def) = %{tl_version}
Provides:       tex(cp1256.sty) = %{tl_version}
Provides:       tex(etrans.sty) = %{tl_version}
Provides:       tex(gedalin.sty) = %{tl_version}
Provides:       tex(hebchrs.sty) = %{tl_version}
Provides:       tex(hebsymb.sty) = %{tl_version}
Provides:       tex(hebtex.sty) = %{tl_version}
Provides:       tex(hebtex.tex) = %{tl_version}
Provides:       tex(hecmd.sty) = %{tl_version}
Provides:       tex(hefonts.sty) = %{tl_version}
Provides:       tex(hefonts0.sty) = %{tl_version}
Provides:       tex(hefonts1.sty) = %{tl_version}
Provides:       tex(hefonts2.sty) = %{tl_version}
Provides:       tex(heparse.sty) = %{tl_version}
Provides:       tex(hepatch.sty) = %{tl_version}
Provides:       tex(hescan.sty) = %{tl_version}
Provides:       tex(hetrans.sty) = %{tl_version}
Provides:       tex(hewrite.sty) = %{tl_version}
Provides:       tex(hmac.sty) = %{tl_version}
Provides:       tex(isiri.sty) = %{tl_version}
Provides:       tex(iso88596.sty) = %{tl_version}
Provides:       tex(nashbf.sty) = %{tl_version}
Provides:       tex(raw.sty) = %{tl_version}
Provides:       tex(saw.sty) = %{tl_version}
Provides:       tex(sotoku.sty) = %{tl_version}
Provides:       tex(twoblks.sty) = %{tl_version}
Provides:       tex(utf8.sty) = %{tl_version}
Provides:       tex(utfcode.sty) = %{tl_version}
Provides:       tex(verses.sty) = %{tl_version}
Provides:       tex(witbhs.sty) = %{tl_version}
Provides:       tex(xarbskel.sty) = %{tl_version}
Provides:       tex(xarbsymb.sty) = %{tl_version}
Provides:       tex(yiddish.sty) = %{tl_version}

%description -n texlive-arabtex
ArabTeX is a package extending the capabilities of TeX/LaTeX to generate Arabic
and Hebrew text. Input may be in ASCII transliteration or other encodings
(including UTF-8); output may be Arabic, Hebrew, or any of several languages
that use the Arabic script. ArabTeX consists of a TeX macro package and Arabic
and Hebrew fonts (provided both in Metafont format and Adobe Type 1). The
Arabic font is presently only available in the Naskhi style. ArabTeX will run
with Plain TeX and also with LaTeX.

%package -n texlive-awami
Summary:        A collection of Awami Nastaliq fonts
Version:        svn76980
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-awami
Awami Nastaliq is a Nastaliq-style Arabic script font supporting a wide variety
of languages of southwest Asia, including but not limited to Urdu. This font is
aimed at minority language support. This makes it unique among Nastaliq fonts.
The font is also a Graphite-only font. It does not support OpenType rendering.

%package -n texlive-bidi
Summary:        Bidirectional typesetting in plain TeX and LaTeX, using XeTeX or LuaTeX
Version:        svn77301
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(auxhook.sty)
Requires:       tex(bibentry.sty)
Requires:       tex(changepage.sty)
Requires:       tex(chngpage.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(optparams.sty)
Requires:       tex(paralist.sty)
Requires:       tex(placeins.sty)
Requires:       tex(setspace.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(zref-abspage.sty)
Provides:       tex(adjmulticol-xetex-bidi.def) = %{tl_version}
Provides:       tex(algorithm2e-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsart-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsbook-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsmath-xetex-bidi.def) = %{tl_version}
Provides:       tex(amstext-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsthm-xetex-bidi.def) = %{tl_version}
Provides:       tex(array-xetex-bidi.def) = %{tl_version}
Provides:       tex(article-xetex-bidi.def) = %{tl_version}
Provides:       tex(artikel1-xetex-bidi.def) = %{tl_version}
Provides:       tex(artikel2-xetex-bidi.def) = %{tl_version}
Provides:       tex(artikel3-xetex-bidi.def) = %{tl_version}
Provides:       tex(arydshln-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamer-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbaseauxtemplates-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbaseboxes-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbasecolor-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbasecompatibility-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbaseframecomponents-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbaseframesize-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbaselocalstructure-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbasemisc-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbasenavigation-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerbaseoverlay-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthemecircles-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthemedefault-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthemefocus-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthemeinmargin-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthememetropolis-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthemerectangles-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerinnerthemerounded-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemedefault-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemefocus-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemeinfolines-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthememetropolis-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthememiniframes-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemeshadow-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemesidebar-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemesmoothbars-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemesmoothtree-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemesplit-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerouterthemetree-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerthemeHannover-xetex-bidi.def) = %{tl_version}
Provides:       tex(beamerthemeSingapore-xetex-bidi.def) = %{tl_version}
Provides:       tex(bidi-media9.sty) = %{tl_version}
Provides:       tex(bidi-perpage.sty) = %{tl_version}
Provides:       tex(bidi.sty) = %{tl_version}
Provides:       tex(bidi.tex) = %{tl_version}
Provides:       tex(bidi2in1.sty) = %{tl_version}
Provides:       tex(bidicode.sty) = %{tl_version}
Provides:       tex(bidiftnxtra.sty) = %{tl_version}
Provides:       tex(bidipoem.sty) = %{tl_version}
Provides:       tex(biditools.sty) = %{tl_version}
Provides:       tex(bidituftefloat.sty) = %{tl_version}
Provides:       tex(bidituftegeneralstructure.sty) = %{tl_version}
Provides:       tex(bidituftehyperref.sty) = %{tl_version}
Provides:       tex(bidituftesidenote.sty) = %{tl_version}
Provides:       tex(bidituftetitle.sty) = %{tl_version}
Provides:       tex(bidituftetoc.sty) = %{tl_version}
Provides:       tex(boek-xetex-bidi.def) = %{tl_version}
Provides:       tex(boek3-xetex-bidi.def) = %{tl_version}
Provides:       tex(book-xetex-bidi.def) = %{tl_version}
Provides:       tex(bookest-xetex-bidi.def) = %{tl_version}
Provides:       tex(breqn-xetex-bidi.def) = %{tl_version}
Provides:       tex(cals-xetex-bidi.def) = %{tl_version}
Provides:       tex(caption-xetex-bidi.def) = %{tl_version}
Provides:       tex(caption3-xetex-bidi.def) = %{tl_version}
Provides:       tex(color-xetex-bidi.def) = %{tl_version}
Provides:       tex(colortbl-xetex-bidi.def) = %{tl_version}
Provides:       tex(combine-xetex-bidi.def) = %{tl_version}
Provides:       tex(crop-xetex-bidi.def) = %{tl_version}
Provides:       tex(cuted-xetex-bidi.def) = %{tl_version}
Provides:       tex(cutwin-xetex-bidi.def) = %{tl_version}
Provides:       tex(cvthemebidicasual.sty) = %{tl_version}
Provides:       tex(cvthemebidiclassic.sty) = %{tl_version}
Provides:       tex(dblfnote-xetex-bidi.def) = %{tl_version}
Provides:       tex(diagbox-xetex-bidi.def) = %{tl_version}
Provides:       tex(draftwatermark-xetex-bidi.def) = %{tl_version}
Provides:       tex(empheq-xetex-bidi.def) = %{tl_version}
Provides:       tex(eso-pic-xetex-bidi.def) = %{tl_version}
Provides:       tex(extarticle-xetex-bidi.def) = %{tl_version}
Provides:       tex(extbook-xetex-bidi.def) = %{tl_version}
Provides:       tex(extletter-xetex-bidi.def) = %{tl_version}
Provides:       tex(extrafootnotefeatures-xetex-bidi.def) = %{tl_version}
Provides:       tex(extreport-xetex-bidi.def) = %{tl_version}
Provides:       tex(fancybox-xetex-bidi.def) = %{tl_version}
Provides:       tex(fancyhdr-xetex-bidi.def) = %{tl_version}
Provides:       tex(fix2col-xetex-bidi.def) = %{tl_version}
Provides:       tex(fleqn-xetex-bidi.def) = %{tl_version}
Provides:       tex(float-xetex-bidi.def) = %{tl_version}
Provides:       tex(floatrow-xetex-bidi.def) = %{tl_version}
Provides:       tex(flowfram-xetex-bidi.def) = %{tl_version}
Provides:       tex(fnpct-xetex-bidi.def) = %{tl_version}
Provides:       tex(footnote-xetex-bidi.def) = %{tl_version}
Provides:       tex(footnotebackref-xetex-bidi.def) = %{tl_version}
Provides:       tex(framed-xetex-bidi.def) = %{tl_version}
Provides:       tex(ftnright-xetex-bidi.def) = %{tl_version}
Provides:       tex(geometry-xetex-bidi.def) = %{tl_version}
Provides:       tex(graphicx-xetex-bidi.def) = %{tl_version}
Provides:       tex(hgeneric-testphase-xetex-bidi.def) = %{tl_version}
Provides:       tex(hvfloat-xetex-bidi.def) = %{tl_version}
Provides:       tex(hyperref-xetex-bidi.def) = %{tl_version}
Provides:       tex(imsproc-xetex-bidi.def) = %{tl_version}
Provides:       tex(latex-xetex-bidi.def) = %{tl_version}
Provides:       tex(leqno-xetex-bidi.def) = %{tl_version}
Provides:       tex(letter-xetex-bidi.def) = %{tl_version}
Provides:       tex(lettrine-xetex-bidi.def) = %{tl_version}
Provides:       tex(lineno-xetex-bidi.def) = %{tl_version}
Provides:       tex(listings-xetex-bidi.def) = %{tl_version}
Provides:       tex(longtable-xetex-bidi.def) = %{tl_version}
Provides:       tex(lscape-xetex-bidi.def) = %{tl_version}
Provides:       tex(mathtools-xetex-bidi.def) = %{tl_version}
Provides:       tex(mdframed-xetex-bidi.def) = %{tl_version}
Provides:       tex(media9-xetex-bidi.def) = %{tl_version}
Provides:       tex(memoir-xetex-bidi.def) = %{tl_version}
Provides:       tex(midfloat-xetex-bidi.def) = %{tl_version}
Provides:       tex(minitoc-xetex-bidi.def) = %{tl_version}
Provides:       tex(multicol-xetex-bidi.def) = %{tl_version}
Provides:       tex(multienum-xetex-bidi.def) = %{tl_version}
Provides:       tex(natbib-xetex-bidi.def) = %{tl_version}
Provides:       tex(newfloat-xetex-bidi.def) = %{tl_version}
Provides:       tex(nicematrix-xetex-bidi.def) = %{tl_version}
Provides:       tex(ntheorem-hyper-xetex-bidi.def) = %{tl_version}
Provides:       tex(ntheorem-xetex-bidi.def) = %{tl_version}
Provides:       tex(overpic-xetex-bidi.def) = %{tl_version}
Provides:       tex(pdfbase-xetex-bidi.def) = %{tl_version}
Provides:       tex(pdflscape-xetex-bidi.def) = %{tl_version}
Provides:       tex(pgfcorescopes.code-xetex-bidi.def) = %{tl_version}
Provides:       tex(pgfsys-xetex-bidi.def) = %{tl_version}
Provides:       tex(picinpar-xetex-bidi.def) = %{tl_version}
Provides:       tex(plain-xetex-bidi.def) = %{tl_version}
Provides:       tex(pstricks-xetex-bidi.def) = %{tl_version}
Provides:       tex(quotchap-xetex-bidi.def) = %{tl_version}
Provides:       tex(ragged2e-xetex-bidi.def) = %{tl_version}
Provides:       tex(rapport1-xetex-bidi.def) = %{tl_version}
Provides:       tex(rapport3-xetex-bidi.def) = %{tl_version}
Provides:       tex(refrep-xetex-bidi.def) = %{tl_version}
Provides:       tex(report-xetex-bidi.def) = %{tl_version}
Provides:       tex(rotating-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrartcl-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrbook-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrreprt-xetex-bidi.def) = %{tl_version}
Provides:       tex(sidecap-xetex-bidi.def) = %{tl_version}
Provides:       tex(soul-xetex-bidi.def) = %{tl_version}
Provides:       tex(stabular-xetex-bidi.def) = %{tl_version}
Provides:       tex(subfigure-xetex-bidi.def) = %{tl_version}
Provides:       tex(tabls-xetex-bidi.def) = %{tl_version}
Provides:       tex(tabularx-xetex-bidi.def) = %{tl_version}
Provides:       tex(tabulary-xetex-bidi.def) = %{tl_version}
Provides:       tex(tc-xetex-xetex-bidi.def) = %{tl_version}
Provides:       tex(tcolorbox-xetex-bidi.def) = %{tl_version}
Provides:       tex(thmbox-xetex-bidi.def) = %{tl_version}
Provides:       tex(titlesec-xetex-bidi.def) = %{tl_version}
Provides:       tex(titletoc-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocbasic-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocbibind-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocloft-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocstyle-xetex-bidi.def) = %{tl_version}
Provides:       tex(todonotes-xetex-bidi.def) = %{tl_version}
Provides:       tex(wrapfig-xetex-bidi.def) = %{tl_version}
Provides:       tex(xcolor-xetex-bidi.def) = %{tl_version}
Provides:       tex(xltxtra-xetex-bidi.def) = %{tl_version}

%description -n texlive-bidi
A convenient interface for typesetting bidirectional texts with plain TeX and
LaTeX, using XeTeX or LuaTeX. The package includes adaptations for use with
many other commonly-used packages.

%package -n texlive-bidihl
Summary:        Experimental bidi-aware text highlighting
Version:        svn37795
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(bidihl.sty) = %{tl_version}

%description -n texlive-bidihl
Experimental bidi-aware text highlighting.

%package -n texlive-dad
Summary:        Simple typesetting system for mixed Arabic/Latin documents
Version:        svn54191
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dad.sty) = %{tl_version}

%description -n texlive-dad
This package allows simple typesetting in Arabic script, intended for mixed
Arabic/Latin script usage in situations where heavy-duty solutions are
discouraged. The system operates with both Unicode and transliterated input,
allowing the user to choose the most appropriate approach for every situation.

%package -n texlive-ghab
Summary:        Typeset ghab boxes in LaTeX
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Provides:       tex(ghab.sty) = %{tl_version}

%description -n texlive-ghab
The package defines a command \darghab that will typeset its argument in a box
with a decorated frame. The width of the box may be set using an optional
argument.

%package -n texlive-hvarabic
Summary:        Macros for RTL typesetting
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(hvarabic.sty) = %{tl_version}

%description -n texlive-hvarabic
This package provides some macros for right-to-left typesetting. It uses by
default the arabic fonts Scheherazade and ALM fixed, the only monospaced arabic
font. The package works with LuaLaTeX or XeLaTeX, but not with pdfLaTeX or
latex.

%package -n texlive-hyphen-arabic
Summary:        (No) Arabic hyphenation patterns
Version:        svn74115
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ar.tex) = %{tl_version}

%description -n texlive-hyphen-arabic
Prevent hyphenation in Arabic.

%package -n texlive-hyphen-farsi
Summary:        (No) Persian hyphenation patterns
Version:        svn74115
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fa.tex) = %{tl_version}

%description -n texlive-hyphen-farsi
Prevent hyphenation in Persian.

%package -n texlive-imsproc
Summary:        Typeset IMS conference proceedings
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-imsproc
The class typesets papers for IMS (Iranian Mathematical Society) conference
proceedings. The class uses the XePersian package.

%package -n texlive-iran-bibtex
Summary:        Iran Manual of Style Citation Guide for BibTeX
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(natbib.sty)
Provides:       tex(iran-bibtex.sty) = %{tl_version}

%description -n texlive-iran-bibtex
The iran-bibtex package, designed for LaTeX, provides BibTeX styles in
accordance with the guidelines outlined in the Iran Manual of Style (1st edn.,
2016)--citation guide to Persian, and English information sources. A collection
of illustrative examples showcasing the usage of this package has been
meticulously prepared and is accessible in the package's GitHub repository
under the 'examples' sub-directory. To facilitate alphabetical sorting of
references, prioritizing Persian/Farsi items ahead of English/Latin ones, a
dedicated file named iran-bibtex-cp1256fa.csf is provided for use with this
package. This file, derived from the ascii.csf file, serves the purpose of
arranging references in the desired order. It is important to note that this
package relies on the natbib package, which is automatically loaded.

%package -n texlive-khatalmaqala
Summary:        Arabic font for university articles
Version:        svn68280
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-khatalmaqala
This font family is a modification of "cm-unicode" fonts, with Arabic support.
It was originally made for a group of undergraduate students at Misr University
For Science And Technology (Egypt) many years ago. After a few semesters, it
had become the main font for their articles and assignments. Now, it is on CTAN
for easier access. khatalmaqala = khat (font) + maqala (article) = font for
article

%package -n texlive-kurdishlipsum
Summary:        A 'lipsum' package for the Kurdish language
Version:        svn47518
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Provides:       tex(kurdishlipsum.sty) = %{tl_version}

%description -n texlive-kurdishlipsum
This package provides lipsum-like facilities for the Kurdish language. The
package gives you easy access to the Kurdish poetry and balladry texts of the
Diwany Vafaiy, Ahmedy Xani, Naly, Mahwy,.... The package needs to be run under
XeLaTeX.

%package -n texlive-lshort-persian
Summary:        Persian (Farsi) introduction to LaTeX
Version:        svn31296
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-persian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-persian-doc <= 11:%{version}

%description -n texlive-lshort-persian
A Persian (Farsi) translation of Oetiker's (not so) short introduction.

%package -n texlive-luabidi
Summary:        Bidi functions for LuaTeX
Version:        svn68432
License:        LPPL-1.3c AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(luabidi-arabmaths.def) = %{tl_version}
Provides:       tex(luabidi-autofootnoterule.def) = %{tl_version}
Provides:       tex(luabidi-footnotes.def) = %{tl_version}
Provides:       tex(luabidi-test-arabmaths.tex) = %{tl_version}
Provides:       tex(luabidi.sty) = %{tl_version}

%description -n texlive-luabidi
The package attempts to emulate the XeTeX bidi package, in the context of
LuaTeX.

%package -n texlive-mohe-book
Summary:        Typeset authored, translated, and research books according to mohe rules
Version:        svn74912
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mohe-book
The mohe-book LaTeX class is a specialized template designed to streamline the
typesetting of academic and educational materials, including authored
textbooks, translated works, research publications, and course materials.
Tailored for faculty members and academic staff in Afghanistan, it adheres to
rigorous scholarly standards while offering customizable layouts for bilingual
(e.g., Dari-English) or multilingual content. Key features include
preconfigured chapter/section styles, support for complex scripts, and
templates for front matter (prefaces, dedications) and back matter
(bibliographies, indices). The package aims to simplify the creation of
professional-grade academic documents, ensuring consistency and compliance with
institutional or regional publishing guidelines.

%package -n texlive-na-box
Summary:        Arabic-aware version of pas-cours package
Version:        svn45130
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(na-box.sty) = %{tl_version}

%description -n texlive-na-box
This is a modified version of the pas-cours package made compatible with
XeLaTeX/polyglossia to write arabic documents with fancy boxed theorem-alike
environments.

%package -n texlive-parsimatn
Summary:        Contemporary Persian font for scientific and formal writings
Version:        svn70775
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-parsimatn
This Persian font is suitable for official and scientific writings. All Persian
and Arabic letters and numbers are designed by the author. During the design
process, attention has been paid to the fact that, in addition to being new and
innovative, the letters be familiar to the average Persian/Arabic viewer.

%package -n texlive-parsinevis
Summary:        "Scheherazade New" adapted for Persian typesetting and scientific writings
Version:        svn70776
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-parsinevis
This font has been made by editing SIL's "Scheherazade New", making it more
suitable for Persian typesetting. (Scheherazade New has SIL OFL license.)

%package -n texlive-persian-bib
Summary:        Persian translations of classic BibTeX styles
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-persian-bib
Currently 9 files: acm-fa.bst, asa-fa.bst, chicago-fa.bst, ieeetr-fa.bst,
plain-fa-inLTR-beamer.bst, plain-fa-inLTR.bst, plain-fa.bst, plainnat-fa.bst
and unsrt-fa.bst are modified for Persian documents prepared with XePersian
(which the present package depends on). The Persian .bst files can
simultaneously handle both Latin and Persian references. A file cp1256fa.csf is
provided for correct sorting of Persian references and three fields LANGUAGE,
TRANSLATOR and AUTHORFA are defined.

%package -n texlive-quran
Summary:        An easy way to typeset any part of The Holy Quran
Version:        svn75029
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-transde.def) = %{tl_version}
Provides:       tex(quran-transen.def) = %{tl_version}
Provides:       tex(quran-transfa.def) = %{tl_version}
Provides:       tex(quran-transfr.def) = %{tl_version}
Provides:       tex(quran-translt.def) = %{tl_version}
Provides:       tex(quran.sty) = %{tl_version}
Provides:       tex(qurantext-de.translation.def) = %{tl_version}
Provides:       tex(qurantext-en.translation.def) = %{tl_version}
Provides:       tex(qurantext-en.transliteration.def) = %{tl_version}
Provides:       tex(qurantext-fa.translation.def) = %{tl_version}
Provides:       tex(qurantext-fr.translation.def) = %{tl_version}
Provides:       tex(qurantext-simple.def) = %{tl_version}
Provides:       tex(qurantext-uthmani-min.def) = %{tl_version}
Provides:       tex(qurantext-uthmani.def) = %{tl_version}

%description -n texlive-quran
This package offers the user an easy way to typeset The Holy Quran. It has been
inspired by the lipsum and ptext packages and provides several macros for
typesetting the whole or any part of the Quran based on its popular division,
including surah, ayah, juz, hizb, quarter, and page. Besides the Arabic
original, translations to English, German, French, and Persian are provided, as
well as an English transliteration.

%package -n texlive-sexam
Summary:        Package for typesetting arabic exam scripts
Version:        svn46628
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(background.sty)
Requires:       tex(bclogo.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(fouriernc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathpple.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(moreenum.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pifont.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tikz.sty)
Requires:       tex(ulem.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(yagusylo.sty)
Provides:       tex(bacex.sty) = %{tl_version}
Provides:       tex(sexam.sty) = %{tl_version}
Provides:       tex(wexam.sty) = %{tl_version}

%description -n texlive-sexam
The package provides a modified version of the exam package made compatible
with XeLaTeX/polyglossia to typesetting arabic exams.

%package -n texlive-simurgh
Summary:        Typeset Parsi in LuaLaTeX
Version:        svn31719
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(auxhook.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(zref-abspage.sty)
Provides:       tex(simurgh-abjad.sty) = %{tl_version}
Provides:       tex(simurgh-adadi.sty) = %{tl_version}
Provides:       tex(simurgh-algorithm.sty) = %{tl_version}
Provides:       tex(simurgh-algorithmic.sty) = %{tl_version}
Provides:       tex(simurgh-amsart.sty) = %{tl_version}
Provides:       tex(simurgh-amsbook.sty) = %{tl_version}
Provides:       tex(simurgh-amsmath.sty) = %{tl_version}
Provides:       tex(simurgh-amstext.sty) = %{tl_version}
Provides:       tex(simurgh-amsthm.sty) = %{tl_version}
Provides:       tex(simurgh-array.sty) = %{tl_version}
Provides:       tex(simurgh-article.sty) = %{tl_version}
Provides:       tex(simurgh-artikel1.sty) = %{tl_version}
Provides:       tex(simurgh-artikel2.sty) = %{tl_version}
Provides:       tex(simurgh-artikel3.sty) = %{tl_version}
Provides:       tex(simurgh-arydshln.sty) = %{tl_version}
Provides:       tex(simurgh-backref.sty) = %{tl_version}
Provides:       tex(simurgh-bidi.sty) = %{tl_version}
Provides:       tex(simurgh-boek.sty) = %{tl_version}
Provides:       tex(simurgh-boek3.sty) = %{tl_version}
Provides:       tex(simurgh-book.sty) = %{tl_version}
Provides:       tex(simurgh-bookest.sty) = %{tl_version}
Provides:       tex(simurgh-caption3.sty) = %{tl_version}
Provides:       tex(simurgh-chkeng.sty) = %{tl_version}
Provides:       tex(simurgh-clss.sty) = %{tl_version}
Provides:       tex(simurgh-counters.sty) = %{tl_version}
Provides:       tex(simurgh-cptns.sty) = %{tl_version}
Provides:       tex(simurgh-empheq.sty) = %{tl_version}
Provides:       tex(simurgh-extarticle.sty) = %{tl_version}
Provides:       tex(simurgh-extbook.sty) = %{tl_version}
Provides:       tex(simurgh-extletter.sty) = %{tl_version}
Provides:       tex(simurgh-extreport.sty) = %{tl_version}
Provides:       tex(simurgh-fleqn.sty) = %{tl_version}
Provides:       tex(simurgh-fonts.sty) = %{tl_version}
Provides:       tex(simurgh-footnotes.sty) = %{tl_version}
Provides:       tex(simurgh-ftnxtra.sty) = %{tl_version}
Provides:       tex(simurgh-glossaries.sty) = %{tl_version}
Provides:       tex(simurgh-harfi.sty) = %{tl_version}
Provides:       tex(simurgh-jalalical.sty) = %{tl_version}
Provides:       tex(simurgh-leqno.sty) = %{tl_version}
Provides:       tex(simurgh-letter.sty) = %{tl_version}
Provides:       tex(simurgh-lettrine.sty) = %{tl_version}
Provides:       tex(simurgh-loader.sty) = %{tl_version}
Provides:       tex(simurgh-ltx.sty) = %{tl_version}
Provides:       tex(simurgh-mathdigitspec.sty) = %{tl_version}
Provides:       tex(simurgh-memoir.sty) = %{tl_version}
Provides:       tex(simurgh-minitoc.sty) = %{tl_version}
Provides:       tex(simurgh-natbib.sty) = %{tl_version}
Provides:       tex(simurgh-pkgs.sty) = %{tl_version}
Provides:       tex(simurgh-poem.sty) = %{tl_version}
Provides:       tex(simurgh-rapport1.sty) = %{tl_version}
Provides:       tex(simurgh-rapport3.sty) = %{tl_version}
Provides:       tex(simurgh-refrep.sty) = %{tl_version}
Provides:       tex(simurgh-report.sty) = %{tl_version}
Provides:       tex(simurgh-scrartcl.sty) = %{tl_version}
Provides:       tex(simurgh-scrbook.sty) = %{tl_version}
Provides:       tex(simurgh-scrlettr.sty) = %{tl_version}
Provides:       tex(simurgh-scrreprt.sty) = %{tl_version}
Provides:       tex(simurgh-shellescape.sty) = %{tl_version}
Provides:       tex(simurgh-tags.sty) = %{tl_version}
Provides:       tex(simurgh-tartibi.sty) = %{tl_version}
Provides:       tex(simurgh-tools.sty) = %{tl_version}
Provides:       tex(simurgh-unibidi.sty) = %{tl_version}
Provides:       tex(simurgh.sty) = %{tl_version}

%description -n texlive-simurgh
The package provides an automatic and unified interface for Parsi typesetting
in LaTeX, using the LuaTeX engine. The project to produce this system is
dedicated to Ferdowsi The Great.

%package -n texlive-texnegar
Summary:        Kashida justification in XeLaTeX and LuaLaTeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(environ.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(newverbs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(zref-savepos.sty)
Provides:       tex(texnegar-common-kashida.tex) = %{tl_version}
Provides:       tex(texnegar-ini.tex) = %{tl_version}
Provides:       tex(texnegar-luatex.sty) = %{tl_version}
Provides:       tex(texnegar-xetex-kashida.tex) = %{tl_version}
Provides:       tex(texnegar-xetex.sty) = %{tl_version}
Provides:       tex(texnegar.sty) = %{tl_version}

%description -n texlive-texnegar
In some cursive scripts such as Persian or Arabic, kashida is used to create
justification. In this type of justification characters are elongated rather
than expanding spaces between words. The kashida justification in xepersian has
many bugs. Also it has problems with some fonts. The xepersian-hm package was
the first attempt to fix these bugs in xepersian, which uses the XeTeX engine.
This package extends the kashida justification to be used with the LuaTeX
engine, too. Explanation of the package name: Negar, in Persian, is the present
stem of negaashtan meaning to design, to paint, to write; and as a noun it
means "sweetheart, idol, beloved, figuratively referring to a beautiful woman,
pattern, painting, and artistic design".

%package -n texlive-tram
Summary:        Typeset tram boxes in LaTeX
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tram.sty) = %{tl_version}

%description -n texlive-tram
Tram boxes are highlighted with patterns of dots; the package defines an
environment tram that typesets its content into a tram box. The pattern used
may be selected in an optional argument to the environment.

%package -n texlive-xepersian
Summary:        Persian for LaTeX, using LuaTeX or XeTeX
Version:        svn77228
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bidi.sty)
Requires:       tex(calc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(fullpage.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pifont.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(algorithm-xetex-xepersian.def) = %{tl_version}
Provides:       tex(algorithmic-xetex-xepersian.def) = %{tl_version}
Provides:       tex(amsart-xetex-xepersian.def) = %{tl_version}
Provides:       tex(amsbook-xetex-xepersian.def) = %{tl_version}
Provides:       tex(appendix-xetex-xepersian.def) = %{tl_version}
Provides:       tex(article-xetex-xepersian.def) = %{tl_version}
Provides:       tex(artikel1-xetex-xepersian.def) = %{tl_version}
Provides:       tex(artikel2-xetex-xepersian.def) = %{tl_version}
Provides:       tex(artikel3-xetex-xepersian.def) = %{tl_version}
Provides:       tex(backref-xetex-xepersian.def) = %{tl_version}
Provides:       tex(beamer-xetex-xepersian.def) = %{tl_version}
Provides:       tex(beamerbasetranslator-xetex-xepersian.def) = %{tl_version}
Provides:       tex(bidimoderncv-xetex-xepersian.def) = %{tl_version}
Provides:       tex(bidituftesidenote-xetex-xepersian.def) = %{tl_version}
Provides:       tex(boek-xetex-xepersian.def) = %{tl_version}
Provides:       tex(boek3-xetex-xepersian.def) = %{tl_version}
Provides:       tex(book-xetex-xepersian.def) = %{tl_version}
Provides:       tex(bookest-xetex-xepersian.def) = %{tl_version}
Provides:       tex(breqn-xetex-xepersian.def) = %{tl_version}
Provides:       tex(color-localize-xetex-xepersian.def) = %{tl_version}
Provides:       tex(enumerate-xetex-xepersian.def) = %{tl_version}
Provides:       tex(enumitem-xetex-xepersian.def) = %{tl_version}
Provides:       tex(extarticle-xetex-xepersian.def) = %{tl_version}
Provides:       tex(extbook-xetex-xepersian.def) = %{tl_version}
Provides:       tex(extrafootnotefeatures-xetex-bidi-xetex-xepersian.def) = %{tl_version}
Provides:       tex(extreport-xetex-xepersian.def) = %{tl_version}
Provides:       tex(fancyref-xetex-xepersian.def) = %{tl_version}
Provides:       tex(footnote-xetex-bidi-xetex-xepersian.def) = %{tl_version}
Provides:       tex(framed-xetex-xepersian.def) = %{tl_version}
Provides:       tex(glossaries-xetex-xepersian.def) = %{tl_version}
Provides:       tex(hyperref-xetex-xepersian.def) = %{tl_version}
Provides:       tex(imsproc-xetex-xepersian.def) = %{tl_version}
Provides:       tex(kashida-xetex-xepersian.def) = %{tl_version}
Provides:       tex(latex-localize-commands-xetex-xepersian.def) = %{tl_version}
Provides:       tex(latex-localize-environments-xetex-xepersian.def) = %{tl_version}
Provides:       tex(latex-localize-messages-xetex-xepersian.def) = %{tl_version}
Provides:       tex(latex-localize-misc-xetex-xepersian.def) = %{tl_version}
Provides:       tex(listings-xetex-xepersian.def) = %{tl_version}
Provides:       tex(localize-xetex-xepersian.def) = %{tl_version}
Provides:       tex(memoir-xetex-xepersian.def) = %{tl_version}
Provides:       tex(minitoc-xetex-xepersian.def) = %{tl_version}
Provides:       tex(natbib-xetex-xepersian.def) = %{tl_version}
Provides:       tex(packages-localize-xetex-xepersian.def) = %{tl_version}
Provides:       tex(rapport1-xetex-xepersian.def) = %{tl_version}
Provides:       tex(rapport3-xetex-xepersian.def) = %{tl_version}
Provides:       tex(refrep-xetex-xepersian.def) = %{tl_version}
Provides:       tex(report-xetex-xepersian.def) = %{tl_version}
Provides:       tex(scrartcl-xetex-xepersian.def) = %{tl_version}
Provides:       tex(scrbook-xetex-xepersian.def) = %{tl_version}
Provides:       tex(scrreprt-xetex-xepersian.def) = %{tl_version}
Provides:       tex(soul-xetex-xepersian.def) = %{tl_version}
Provides:       tex(tkz-linknodes-xetex-xepersian.def) = %{tl_version}
Provides:       tex(tocloft-xetex-xepersian.def) = %{tl_version}
Provides:       tex(unicode-persiancal.sty) = %{tl_version}
Provides:       tex(unicode-persianmath.sty) = %{tl_version}
Provides:       tex(url-xetex-xepersian.def) = %{tl_version}
Provides:       tex(varioref-xetex-xepersian.def) = %{tl_version}
Provides:       tex(xepersian-localize-commands-xetex-xepersian.def) = %{tl_version}
Provides:       tex(xepersian-localize-environments-xetex-xepersian.def) = %{tl_version}
Provides:       tex(xepersian-multiplechoice.sty) = %{tl_version}
Provides:       tex(xepersian.sty) = %{tl_version}

%description -n texlive-xepersian
This package provides a convenient interface for typesetting Persian and
English texts in LaTeX, using the LuaTeX or the XeTeX engine. The name
"XePersian" is derived from the words experience and persian and captures the
author's philosophy of writing the package for the best Persian typesetting
experience in TeX.

%package -n texlive-xepersian-hm
Summary:        Fixes kashida feature in xepersian package
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xepersian.sty)
Requires:       tex(zref-savepos.sty)
Provides:       tex(xepersian-hm-common-kashida.tex) = %{tl_version}
Provides:       tex(xepersian-hm-kashida.tex) = %{tl_version}
Provides:       tex(xepersian-hm.sty) = %{tl_version}

%description -n texlive-xepersian-hm
The kashida feature in xepersian has problems with some fonts such as the HM
Series fonts and the XB Series fonts. This package fixes these problems. The
package requires xepersian and l3keys2e.

%package -n texlive-xindy-persian
Summary:        Support for the Persian language in xindy
Version:        svn59013
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xindy-persian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xindy-persian-doc <= 11:%{version}

%description -n texlive-xindy-persian
The package offers Persian language support for indexing using xindy.

%post -n texlive-hyphen-arabic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/arabic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "arabic hyph-ar.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{arabic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{arabic}{hyph-ar.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-arabic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/arabic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{arabic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-farsi
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/farsi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "farsi hyph-fa.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=persian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=persian" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{farsi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{farsi}{hyph-fa.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{persian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{persian}{hyph-fa.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-farsi
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/farsi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=persian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{farsi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{persian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

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
tar -xf %{SOURCE24} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE25} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE26} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE27} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE28} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE29} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE30} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE31} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE32} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE33} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE34} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE35} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE36} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE37} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE38} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE39} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE42} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE43} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE44} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE45} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE46} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE47} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE48} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE49} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE50} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE51} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE52} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE53} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE54} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE55} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE56} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE57} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE58} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE59} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE60} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE61} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE62} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE63} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE64} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE65} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE66} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE67} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE68} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE69} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-alkalami
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/alkalami/
%doc %{_texmf_main}/doc/fonts/alkalami/

%files -n texlive-alpha-persian
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/alpha-persian/
%doc %{_texmf_main}/doc/bibtex/alpha-persian/

%files -n texlive-amiri
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/amiri/
%doc %{_texmf_main}/doc/fonts/amiri/

%files -n texlive-arabi
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/arabi/arabeyes/
%{_texmf_main}/fonts/enc/dvips/arabi/
%{_texmf_main}/fonts/map/dvips/arabi/
%{_texmf_main}/fonts/tfm/arabi/arabeyes/
%{_texmf_main}/fonts/tfm/arabi/farsiweb/
%{_texmf_main}/fonts/type1/arabi/arabeyes/
%{_texmf_main}/fonts/type1/arabi/farsiweb/
%{_texmf_main}/tex/latex/arabi/
%doc %{_texmf_main}/doc/latex/arabi/

%files -n texlive-arabi-add
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/arabi-add/
%doc %{_texmf_main}/doc/latex/arabi-add/

%files -n texlive-arabic-book
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/arabic-book/
%doc %{_texmf_main}/doc/xelatex/arabic-book/

%files -n texlive-arabluatex
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/lualatex/arabluatex/
%doc %{_texmf_main}/doc/lualatex/arabluatex/

%files -n texlive-arabtex
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/arabtex/
%{_texmf_main}/fonts/source/public/arabtex/
%{_texmf_main}/fonts/tfm/public/arabtex/
%{_texmf_main}/fonts/type1/public/arabtex/
%{_texmf_main}/tex/latex/arabtex/
%doc %{_texmf_main}/doc/latex/arabtex/

%files -n texlive-awami
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/awami/
%doc %{_texmf_main}/doc/fonts/awami/

%files -n texlive-bidi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bidi/
%doc %{_texmf_main}/doc/latex/bidi/

%files -n texlive-bidihl
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidihl/
%doc %{_texmf_main}/doc/xelatex/bidihl/

%files -n texlive-dad
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/dad/
%{_texmf_main}/fonts/map/dvips/dad/
%{_texmf_main}/fonts/ofm/public/dad/
%{_texmf_main}/fonts/ovf/public/dad/
%{_texmf_main}/fonts/tfm/public/dad/
%{_texmf_main}/fonts/type1/public/dad/
%{_texmf_main}/tex/lualatex/dad/
%doc %{_texmf_main}/doc/fonts/dad/

%files -n texlive-ghab
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/ghab/
%{_texmf_main}/tex/latex/ghab/
%doc %{_texmf_main}/doc/latex/ghab/

%files -n texlive-hvarabic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hvarabic/
%doc %{_texmf_main}/doc/latex/hvarabic/

%files -n texlive-hyphen-arabic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-farsi
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-imsproc
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/imsproc/
%doc %{_texmf_main}/doc/xelatex/imsproc/

%files -n texlive-iran-bibtex
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/iran-bibtex/
%{_texmf_main}/bibtex/csf/iran-bibtex/
%{_texmf_main}/tex/latex/iran-bibtex/
%doc %{_texmf_main}/doc/bibtex/iran-bibtex/

%files -n texlive-khatalmaqala
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/khatalmaqala/
%doc %{_texmf_main}/doc/fonts/khatalmaqala/

%files -n texlive-kurdishlipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/kurdishlipsum/
%doc %{_texmf_main}/doc/xelatex/kurdishlipsum/

%files -n texlive-lshort-persian
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-persian/

%files -n texlive-luabidi
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/lualatex/luabidi/
%doc %{_texmf_main}/doc/lualatex/luabidi/

%files -n texlive-mohe-book
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/mohe-book/
%doc %{_texmf_main}/doc/xelatex/mohe-book/

%files -n texlive-na-box
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/na-box/
%doc %{_texmf_main}/doc/xelatex/na-box/

%files -n texlive-parsimatn
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/parsimatn/
%doc %{_texmf_main}/doc/fonts/parsimatn/

%files -n texlive-parsinevis
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/parsinevis/
%doc %{_texmf_main}/doc/fonts/parsinevis/

%files -n texlive-persian-bib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/persian-bib/
%{_texmf_main}/bibtex/csf/persian-bib/
%doc %{_texmf_main}/doc/xelatex/persian-bib/

%files -n texlive-quran
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quran/
%doc %{_texmf_main}/doc/latex/quran/

%files -n texlive-sexam
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/sexam/
%doc %{_texmf_main}/doc/xelatex/sexam/

%files -n texlive-simurgh
%license gpl2.txt
%{_texmf_main}/tex/lualatex/simurgh/
%doc %{_texmf_main}/doc/lualatex/simurgh/

%files -n texlive-texnegar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/texnegar/
%doc %{_texmf_main}/doc/latex/texnegar/

%files -n texlive-tram
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/tram/
%{_texmf_main}/tex/latex/tram/
%doc %{_texmf_main}/doc/latex/tram/

%files -n texlive-xepersian
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/latex/xepersian/
%doc %{_texmf_main}/doc/latex/xepersian/

%files -n texlive-xepersian-hm
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xepersian-hm/
%doc %{_texmf_main}/doc/xelatex/xepersian-hm/

%files -n texlive-xindy-persian
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/support/xindy-persian/

%changelog
* Sun Feb  8 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76980-2
- fix licensing files

* Wed Jan 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76980-1
- Update to svn76980
- fix descriptions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74912-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74912-1
- Update to TeX Live 2025
