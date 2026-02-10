%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langcyrillic
Epoch:          12
Version:        svn69727
Release:        4%{?dist}
Summary:        Cyrillic

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langcyrillic.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-belarusian.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-belarusian.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bulgarian.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bulgarian.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-russian.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-russian.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbian.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbian.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbianc.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-serbianc.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-ukrainian.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-ukrainian.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/churchslavonic.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/churchslavonic.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmcyr.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmcyr.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrplain.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/disser.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/disser.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskd.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskd.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskdx.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eskdx.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gost.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gost.doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-belarusian.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-churchslavonic.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-mongolian.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-russian.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-serbian.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-ukrainian.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lcyw.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lcyw.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lh.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lh.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lhcyr.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-bulgarian.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-bulgarian.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-mongol.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-mongol.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-russian.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-russian.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-ukr.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-ukr.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnhyphn.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mnhyphn.doc.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mongolian-babel.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mongolian-babel.doc.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/montex.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/montex.doc.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpman-ru.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpman-ru.doc.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numnameru.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numnameru.doc.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eucl-translation-bg.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-eucl-translation-bg.doc.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ruhyphen.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/russ.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/russ.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-apostrophe.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-apostrophe.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-date-lat.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-date-lat.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-def-cyr.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-def-cyr.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-lig.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/serbian-lig.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t2.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/t2.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-ru.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-ru.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-sr.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-sr.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ukrhyph.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ukrhyph.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyrmongolian.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyrmongolian.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-belarusian
Requires:       texlive-babel-bulgarian
Requires:       texlive-babel-russian
Requires:       texlive-babel-serbian
Requires:       texlive-babel-serbianc
Requires:       texlive-babel-ukrainian
Requires:       texlive-churchslavonic
Requires:       texlive-cmcyr
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-cyrillic
Requires:       texlive-cyrillic-bin
Requires:       texlive-cyrplain
Requires:       texlive-disser
Requires:       texlive-eskd
Requires:       texlive-eskdx
Requires:       texlive-gost
Requires:       texlive-hyphen-belarusian
Requires:       texlive-hyphen-bulgarian
Requires:       texlive-hyphen-churchslavonic
Requires:       texlive-hyphen-mongolian
Requires:       texlive-hyphen-russian
Requires:       texlive-hyphen-serbian
Requires:       texlive-hyphen-ukrainian
Requires:       texlive-lcyw
Requires:       texlive-lh
Requires:       texlive-lhcyr
Requires:       texlive-lshort-bulgarian
Requires:       texlive-lshort-mongol
Requires:       texlive-lshort-russian
Requires:       texlive-lshort-ukr
Requires:       texlive-mnhyphn
Requires:       texlive-mongolian-babel
Requires:       texlive-montex
Requires:       texlive-mpman-ru
Requires:       texlive-numnameru
Requires:       texlive-pst-eucl-translation-bg
Requires:       texlive-ruhyphen
Requires:       texlive-russ
Requires:       texlive-serbian-apostrophe
Requires:       texlive-serbian-date-lat
Requires:       texlive-serbian-def-cyr
Requires:       texlive-serbian-lig
Requires:       texlive-t2
Requires:       texlive-texlive-ru
Requires:       texlive-texlive-sr
Requires:       texlive-ukrhyph
Requires:       texlive-xecyrmongolian

%description
Support for Cyrillic scripts (Bulgarian, Russian, Serbian, Ukrainian), even if
Latin alphabets may also be used.


%package -n texlive-babel-belarusian
Summary:        Babel support for Belarusian
Version:        svn49022
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(belarusian.ldf) = %{tl_version}

%description -n texlive-babel-belarusian
The package provides support for use of Babel in documents written in
Belarusian.

%package -n texlive-babel-bulgarian
Summary:        Babel contributed support for Bulgarian
Version:        svn31902
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bulgarian.ldf) = %{tl_version}

%description -n texlive-babel-bulgarian
The package provides support for documents in Bulgarian (or simply containing
some Bulgarian text).

%package -n texlive-babel-russian
Summary:        Russian language module for Babel
Version:        svn57376
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(russianb.ldf) = %{tl_version}

%description -n texlive-babel-russian
The package provides support for use of Babel in documents written in Russian
(in both "traditional" and modern forms). The support is adapted for use both
under 'traditional' TeX engines, and under XeTeX and LuaTeX.

%package -n texlive-babel-serbian
Summary:        Babel/Polyglossia support for Serbian
Version:        svn64571
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(serbian.ldf) = %{tl_version}

%description -n texlive-babel-serbian
The package provides support for Serbian documents written in Latin, in babel.

%package -n texlive-babel-serbianc
Summary:        Babel module to support Serbian Cyrillic
Version:        svn64588
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(serbianc.ldf) = %{tl_version}

%description -n texlive-babel-serbianc
The package provides support for Serbian documents written in Cyrillic, in
babel.

%package -n texlive-babel-ukrainian
Summary:        Babel support for Ukrainian
Version:        svn56674
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ukraineb.ldf) = %{tl_version}

%description -n texlive-babel-ukrainian
The package provides support for use of babel in documents written in
Ukrainian. The support is adapted for use under legacy TeX engines as well as
XeTeX and LuaTeX.

%package -n texlive-churchslavonic
Summary:        Typeset documents in Church Slavonic language using Unicode
Version:        svn67474
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       texlive-fonts-churchslavonic
Requires:       texlive-hyphen-churchslavonic
Requires:       texlive-oberdiek
Requires:       texlive-xcolor
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(luacolor.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(churchslavonic.sty) = %{tl_version}
Provides:       tex(cu-calendar.sty) = %{tl_version}
Provides:       tex(cu-kinovar.sty) = %{tl_version}
Provides:       tex(cu-kruk.sty) = %{tl_version}
Provides:       tex(cu-num.sty) = %{tl_version}
Provides:       tex(cu-util.sty) = %{tl_version}
Provides:       tex(gloss-churchslavonic.ldf) = %{tl_version}

%description -n texlive-churchslavonic
The package provides fonts, hyphenation patterns, and supporting macros to
typeset Church Slavonic texts. It depends on the following other packages:
fonts-churchslavonic, hyph-utf8, intcalc, etoolbox, and xcolor.

%package -n texlive-cmcyr
Summary:        Computer Modern fonts with cyrillic extensions
Version:        svn68681
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmcyr
These are the Computer Modern fonts extended with Russian letters, in Metafont
sources and ATM Compatible Type 1 format. The fonts are provided in KOI-7, but
virtual fonts are available to recode them to three other Russian 8-bit
encodings.

%package -n texlive-cyrplain
Summary:        Support for using T2 encoding
Version:        svn45692
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cyrcmfnt.tex) = %{tl_version}
Provides:       tex(cyrecfnt.tex) = %{tl_version}
Provides:       tex(cyrtex.tex) = %{tl_version}
Provides:       tex(plainenc.tex) = %{tl_version}
Provides:       tex(txxdefs.tex) = %{tl_version}
Provides:       tex(txxextra.tex) = %{tl_version}

%description -n texlive-cyrplain
The T2 bundle provides a variety of separate support functions for using
Cyrillic characters in LaTeX: the mathtext package, for using Cyrillic letters
'transparently' in formulae; the citehack package, for using Cyrillic (or
indeed any non-ascii) characters in citation keys; support for Cyrillic in
BibTeX; support for Cyrillic in Makeindex; and various items of font support.

%package -n texlive-disser
Summary:        Class and templates for typesetting dissertations in Russian
Version:        svn43417
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-disser
Disser comprises a document class and set of templates for typesetting
dissertations in Russian. One of its primary advantages is a simplicity of
format specification for titlepage, headers and elements of automatically
generated lists (table of contents, list of figures, etc). Bibliography styles,
that conform to the requirements of the Russian standard GOST R 7.0.11-2011,
are provided.

%package -n texlive-eskd
Summary:        Modern Russian typesetting
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-eskd
The class offers modern Russian text formatting, in accordance with accepted
design standards. Fonts not (apparently) available on CTAN are required for use
of the class.

%package -n texlive-eskdx
Summary:        Modern Russian typesetting
Version:        svn29235
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(chngpage.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(lscape.sty)
Requires:       tex(rotating.sty)
Requires:       tex(zref-perpage.sty)
Provides:       tex(eskdafterpkg.sty) = %{tl_version}
Provides:       tex(eskdappsheet.sty) = %{tl_version}
Provides:       tex(eskdbiblist.sty) = %{tl_version}
Provides:       tex(eskdcap.sty) = %{tl_version}
Provides:       tex(eskdchngsheet.sty) = %{tl_version}
Provides:       tex(eskddstu.sty) = %{tl_version}
Provides:       tex(eskdexplan.sty) = %{tl_version}
Provides:       tex(eskdfont.sty) = %{tl_version}
Provides:       tex(eskdfootnote.sty) = %{tl_version}
Provides:       tex(eskdfreesize.sty) = %{tl_version}
Provides:       tex(eskdhash.sty) = %{tl_version}
Provides:       tex(eskdindent.sty) = %{tl_version}
Provides:       tex(eskdinfo.sty) = %{tl_version}
Provides:       tex(eskdlang.sty) = %{tl_version}
Provides:       tex(eskdlist.sty) = %{tl_version}
Provides:       tex(eskdpara.sty) = %{tl_version}
Provides:       tex(eskdplain.sty) = %{tl_version}
Provides:       tex(eskdrussian.def) = %{tl_version}
Provides:       tex(eskdsect.sty) = %{tl_version}
Provides:       tex(eskdspec.sty) = %{tl_version}
Provides:       tex(eskdspecii.sty) = %{tl_version}
Provides:       tex(eskdstamp.sty) = %{tl_version}
Provides:       tex(eskdtitle.sty) = %{tl_version}
Provides:       tex(eskdtitlebase.sty) = %{tl_version}
Provides:       tex(eskdtotal.sty) = %{tl_version}
Provides:       tex(eskdukrainian.def) = %{tl_version}

%description -n texlive-eskdx
Eskdx is a collection of LaTeX classes and packages to typeset textual and
graphical documents in accordance with Russian (and probably post USSR)
standards for designers.

%package -n texlive-gost
Summary:        BibTeX styles to format according to GOST
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-gost
BibTeX styles to format bibliographies in English, Russian or Ukrainian
according to GOST 7.0.5-2008 or GOST 7.1-2003. Both 8-bit and Unicode (UTF-8)
versions of each BibTeX style, in each case offering a choice of sorted and
unsorted. Further, a set of three styles (which do not conform to current
standards) are retained for backwards compatibility.

%package -n texlive-hyphen-belarusian
Summary:        Belarusian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-be.t2a.tex) = %{tl_version}
Provides:       tex(hyph-be.tex) = %{tl_version}
Provides:       tex(hyph-quote-be.tex) = %{tl_version}
Provides:       tex(loadhyph-be.tex) = %{tl_version}

%description -n texlive-hyphen-belarusian
Belarusian hyphenation patterns in T2A and UTF-8 encodings

%package -n texlive-hyphen-bulgarian
Summary:        Bulgarian hyphenation patterns.
Version:        svn73410
License:        LicenseRef-Unknown
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-bg.t2a.tex) = %{tl_version}
Provides:       tex(hyph-bg.tex) = %{tl_version}
Provides:       tex(loadhyph-bg.tex) = %{tl_version}

%description -n texlive-hyphen-bulgarian
Hyphenation patterns for Bulgarian in T2A and UTF-8 encodings.

%package -n texlive-hyphen-churchslavonic
Summary:        Church Slavonic hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-cu.tex) = %{tl_version}
Provides:       tex(loadhyph-cu.tex) = %{tl_version}

%description -n texlive-hyphen-churchslavonic
Hyphenation patterns for Church Slavonic in UTF-8 encoding

%package -n texlive-hyphen-mongolian
Summary:        Mongolian hyphenation patterns in Cyrillic script.
Version:        svn74203
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-mn-cyrl-x-lmc.lmc.tex) = %{tl_version}
Provides:       tex(hyph-mn-cyrl-x-lmc.tex) = %{tl_version}
Provides:       tex(hyph-mn-cyrl.t2a.tex) = %{tl_version}
Provides:       tex(hyph-mn-cyrl.tex) = %{tl_version}
Provides:       tex(loadhyph-mn-cyrl-x-lmc.tex) = %{tl_version}
Provides:       tex(loadhyph-mn-cyrl.tex) = %{tl_version}

%description -n texlive-hyphen-mongolian
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8 encodings. LMC
encoding is used in MonTeX. The package includes two sets of patterns that will
hopefully be merged in future.

%package -n texlive-hyphen-russian
Summary:        Russian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Requires:       texlive-ruhyphen
Provides:       tex(hyph-ru.t2a.tex) = %{tl_version}
Provides:       tex(hyph-ru.tex) = %{tl_version}
Provides:       tex(loadhyph-ru.tex) = %{tl_version}

%description -n texlive-hyphen-russian
Hyphenation patterns for Russian in T2A and UTF-8 encodings. For 8-bit engines,
the 'ruhyphen' package provides a number of different pattern sets, as well as
different (8-bit) encodings, that can be chosen at format-generation time. The
UTF-8 version only provides the default pattern set. A mechanism similar to the
one used for 8-bit patterns may be implemented in the future.

%package -n texlive-hyphen-serbian
Summary:        Serbian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sh-cyrl.t2a.tex) = %{tl_version}
Provides:       tex(hyph-sh-cyrl.tex) = %{tl_version}
Provides:       tex(hyph-sh-latn.ec.tex) = %{tl_version}
Provides:       tex(hyph-sh-latn.tex) = %{tl_version}
Provides:       tex(hyph-sr-cyrl.tex) = %{tl_version}
Provides:       tex(loadhyph-sr-cyrl.tex) = %{tl_version}
Provides:       tex(loadhyph-sr-latn.tex) = %{tl_version}

%description -n texlive-hyphen-serbian
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8 encodings. For 8-bit
engines the patterns are available separately as 'serbian' in T1/EC encoding
for Latin script and 'serbianc' in T2A encoding for Cyrillic script. Unicode
engines should only use 'serbian' which has patterns in both scripts combined.

%package -n texlive-hyphen-ukrainian
Summary:        Ukrainian hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Requires:       texlive-ukrhyph
Provides:       tex(hyph-quote-uk.tex) = %{tl_version}
Provides:       tex(hyph-uk.t2a.tex) = %{tl_version}
Provides:       tex(hyph-uk.tex) = %{tl_version}
Provides:       tex(loadhyph-uk.tex) = %{tl_version}

%description -n texlive-hyphen-ukrainian
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings. For 8-bit
engines, the 'ukrhyph' package provides a number of different pattern sets, as
well as different (8-bit) encodings, that can be chosen at format-generation
time. The UTF-8 version only provides the default pattern set. A mechanism
similar to the one used for 8-bit patterns may be implemented in the future.

%package -n texlive-lcyw
Summary:        Make Classic Cyrillic CM fonts accessible in LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifpdf.sty)
Provides:       tex(cmap-cyr-vf.sty) = %{tl_version}
Provides:       tex(lcywenc.def) = %{tl_version}

%description -n texlive-lcyw
The package makes the classic CM Cyrillic fonts accessible for use with LaTeX.

%package -n texlive-lh
Summary:        Cyrillic fonts that support LaTeX standard encodings
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-ec
Provides:       tex(lh-lcy.sty) = %{tl_version}
Provides:       tex(lh-lcyccr.sty) = %{tl_version}
Provides:       tex(lh-lcyxccr.sty) = %{tl_version}
Provides:       tex(lh-ot2.sty) = %{tl_version}
Provides:       tex(lh-ot2ccr.sty) = %{tl_version}
Provides:       tex(lh-ot2xccr.sty) = %{tl_version}
Provides:       tex(lh-t2accr.sty) = %{tl_version}
Provides:       tex(lh-t2axccr.sty) = %{tl_version}
Provides:       tex(lh-t2bccr.sty) = %{tl_version}
Provides:       tex(lh-t2bxccr.sty) = %{tl_version}
Provides:       tex(lh-t2cccr.sty) = %{tl_version}
Provides:       tex(lh-t2cxccr.sty) = %{tl_version}
Provides:       tex(lh-x2ccr.sty) = %{tl_version}
Provides:       tex(lh-x2xccr.sty) = %{tl_version}
Provides:       tex(nfssfox.tex) = %{tl_version}
Provides:       tex(testfox.tex) = %{tl_version}
Provides:       tex(testkern.tex) = %{tl_version}

%description -n texlive-lh
The LH fonts address the problem of the wide variety of alphabets that are
written with Cyrillic-style characters. The fonts are the original basis of the
set of T2* and X2 encodings that are now used when LaTeX users need to write in
Cyrillic languages. Macro support in standard LaTeX encodings is offered
through the latex-cyrillic and t2 bundles, and the package itself offers
support for other (more traditional) encodings. The fonts, in the standard T2*
and X2 encodings are available in Adobe Type 1 format, in the CM-Super family
of fonts. The package also offers its own LaTeX support for OT2 encoded fonts,
CM bright shaped fonts and Concrete shaped fonts.

%package -n texlive-lhcyr
Summary:        A non-standard Cyrillic input scheme
Version:        svn77050
License:        LicenseRef-Lhcyr
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(karabas.tex) = %{tl_version}
Provides:       tex(kniga.tex) = %{tl_version}
Provides:       tex(lhcyralt-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyralt.sty) = %{tl_version}
Provides:       tex(lhcyrkoi-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyrkoi.sty) = %{tl_version}
Provides:       tex(lhcyrwin-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyrwin.sty) = %{tl_version}
Provides:       tex(otchet.tex) = %{tl_version}
Provides:       tex(pismo.tex) = %{tl_version}
Provides:       tex(rusfonts.tex) = %{tl_version}
Provides:       tex(statya.tex) = %{tl_version}

%description -n texlive-lhcyr
A collection of three LaTeX2e styles intended for typesetting Russian and
bilingual English-Russian documents, using the lh fonts and without the benefit
of babel's language-switching mechanisms. The packages (lhcyralt and lhcyrwin
for use under emTeX, and lhcyrkoi for use under teTeX) provide mappings between
the input encoding and the font encoding (which is described as OT1). The way
this is done does not match the way inputenc would do the job, for output via
fontenc to one of the T2 series of font encodings.

%package -n texlive-lshort-bulgarian
Summary:        Bulgarian translation of the "Short Introduction to LaTeX2e"
Version:        svn77050
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-bulgarian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-bulgarian-doc <= 11:%{version}

%description -n texlive-lshort-bulgarian
The source files, PostScript and PDF files of the Bulgarian translation of the
"Short Introduction to LaTeX2e".

%package -n texlive-lshort-mongol
Summary:        Short introduction to LaTeX, in Mongolian
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-mongol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-mongol-doc <= 11:%{version}

%description -n texlive-lshort-mongol
A translation of Oetiker's Not so short introduction.

%package -n texlive-lshort-russian
Summary:        Russian introduction to LaTeX
Version:        svn55643
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-russian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-russian-doc <= 11:%{version}

%description -n texlive-lshort-russian
Russian version of A Short Introduction to LaTeX2e.

%package -n texlive-lshort-ukr
Summary:        Ukrainian version of the LaTeX introduction
Version:        svn55643
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-ukr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-ukr-doc <= 11:%{version}

%description -n texlive-lshort-ukr
Ukrainian version of A Short Introduction to LaTeX2e.

%package -n texlive-mnhyphn
Summary:        Mongolian hyphenation patterns in T2A encoding
Version:        svn69727
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mnhyphn.tex) = %{tl_version}

%description -n texlive-mnhyphn
Serves Mongolian written using Cyrillic letters, using T2A-encoded output.
(Note that the montex bundle provides hyphenation patterns for its own encoding
setup.)

%package -n texlive-mongolian-babel
Summary:        A language definition file for Mongolian in Babel
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mn.def) = %{tl_version}
Provides:       tex(mongolian.ldf) = %{tl_version}
Provides:       tex(mongolian.sty) = %{tl_version}

%description -n texlive-mongolian-babel
This package provides support for Mongolian in a Cyrillic alphabet. (The work
derives from the earlier Russian work for babel.)

%package -n texlive-montex
Summary:        Mongolian LaTeX
Version:        svn29349
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cbfonts
Requires:       tex(diagnose.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lscape.sty)
Requires:       tex(rotating.sty)
Provides:       tex(bicig.def) = %{tl_version}
Provides:       tex(bithe.def) = %{tl_version}
Provides:       tex(buryat.def) = %{tl_version}
Provides:       tex(cpctt.def) = %{tl_version}
Provides:       tex(cpdbk.def) = %{tl_version}
Provides:       tex(cpibmrus.def) = %{tl_version}
Provides:       tex(cpkoi.def) = %{tl_version}
Provides:       tex(cpmls.def) = %{tl_version}
Provides:       tex(cpmnk.def) = %{tl_version}
Provides:       tex(cpmos.def) = %{tl_version}
Provides:       tex(cpncc.def) = %{tl_version}
Provides:       tex(english.def) = %{tl_version}
Provides:       tex(kazakh.def) = %{tl_version}
Provides:       tex(lmaenc.def) = %{tl_version}
Provides:       tex(lmcenc.def) = %{tl_version}
Provides:       tex(lmoenc.def) = %{tl_version}
Provides:       tex(lmsenc.def) = %{tl_version}
Provides:       tex(lmuenc.def) = %{tl_version}
Provides:       tex(mls.sty) = %{tl_version}
Provides:       tex(mlsgalig.tex) = %{tl_version}
Provides:       tex(mlstrans.tex) = %{tl_version}
Provides:       tex(mnhyphex.tex) = %{tl_version}
Provides:       tex(rlbicig.sty) = %{tl_version}
Provides:       tex(russian.def) = %{tl_version}
Provides:       tex(xalx.def) = %{tl_version}

%description -n texlive-montex
MonTeX provides Mongolian and Manju support for the TeX/LaTeX community.
Mongolian is a language spoken in North East Asia, namely Mongolia and the
Inner Mongol Autonomous Region of China. Today, it is written in an extended
Cyrillic alphabet in Mongolia whereas the Uighur writing continues to be in use
in Inner Mongolia, though it is also, legally speaking, the official writing
system of Mongolia. Manju is another language of North East Asia, belonging to
the Tungusic branch of the Altaic languages. Though it is hardly spoken
nowadays, it survives in written form as Manju was the native language of the
rulers of the Qing dynasty (1644-1911) in China. Large quantities of documents
of the Imperial Archives survive, as well as some of the finest dictionaries
ever compiled in Asia, like the Pentaglot, a dictionary comprising Manju,
Tibetan, Mongolian, Uighur and Chinese. MonTeX provides all necessary
characters for writing standard Mongolian in Cyrillic and Classical (aka
Traditional or Uighur) writing, and Manju as well as transliterated Tibetan
texts, for which purpose a number of additional characters was created. In
MonTeX, both Mongolian and Manju are entered in romanized form. The
retransliteration (from Latin input to Mongolian and Manju output) is
completely realized in TeX/Metafont so that no external preprocessor is
required. Please note that most of the enhanced functions of MonTeX require a
working e-LaTeX environment. This is especially true when compiling documents
with Mongolian or Manju as the main document language. It is recommended to
choose pdfelatex as the resulting PDF files are truly portable. Vertical text
generated by MonTeX is not supported in DVI.

%package -n texlive-mpman-ru
Summary:        A Russian translation of the MetaPost manual
Version:        svn15878
License:        HPND
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mpman-ru-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mpman-ru-doc <= 11:%{version}

%description -n texlive-mpman-ru
A translation of the user manual, as distributed with MetaPost itself.

%package -n texlive-numnameru
Summary:        Converts a number to the russian spelled out name
Version:        svn44895
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(numnameru.sty) = %{tl_version}

%description -n texlive-numnameru
This package converts a numerical number to the russian spelled out name of the
number. For example, 1 - odin, 2 - dva, 12 - dvenadtsat'.

%package -n texlive-pst-eucl-translation-bg
Summary:        Bulgarian translation of the pst-eucl documentation
Version:        svn19296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pst-eucl-translation-bg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pst-eucl-translation-bg-doc <= 11:%{version}

%description -n texlive-pst-eucl-translation-bg
The pst-eucl package documentation in Bulgarian language - Euclidean Geometry
with PSTricks.

%package -n texlive-ruhyphen
Summary:        Russian hyphenation
Version:        svn21081
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(catkoi.tex) = %{tl_version}
Provides:       tex(cyryoal.tex) = %{tl_version}
Provides:       tex(cyryoas.tex) = %{tl_version}
Provides:       tex(cyryoct.tex) = %{tl_version}
Provides:       tex(cyryodv.tex) = %{tl_version}
Provides:       tex(cyryomg.tex) = %{tl_version}
Provides:       tex(cyryovl.tex) = %{tl_version}
Provides:       tex(cyryozn.tex) = %{tl_version}
Provides:       tex(enrhm2.tex) = %{tl_version}
Provides:       tex(hypht2.tex) = %{tl_version}
Provides:       tex(koi2koi.tex) = %{tl_version}
Provides:       tex(koi2lcy.tex) = %{tl_version}
Provides:       tex(koi2ot2.tex) = %{tl_version}
Provides:       tex(koi2t2a.tex) = %{tl_version}
Provides:       tex(koi2ucy.tex) = %{tl_version}
Provides:       tex(ruenhyph.tex) = %{tl_version}
Provides:       tex(ruhyphal.tex) = %{tl_version}
Provides:       tex(ruhyphas.tex) = %{tl_version}
Provides:       tex(ruhyphct.tex) = %{tl_version}
Provides:       tex(ruhyphdv.tex) = %{tl_version}
Provides:       tex(ruhyphen.tex) = %{tl_version}
Provides:       tex(ruhyphmg.tex) = %{tl_version}
Provides:       tex(ruhyphvl.tex) = %{tl_version}
Provides:       tex(ruhyphzn.tex) = %{tl_version}

%description -n texlive-ruhyphen
A collection of Russian hyphenation patterns supporting a number of Cyrillic
font encodings, including T2, UCY (Omega Unicode Cyrillic), LCY, LWN (OT2), and
koi8-r.

%package -n texlive-russ
Summary:        LaTeX in Russian, without babel
Version:        svn25209
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(inputenc.sty)
Requires:       tex(xspace.sty)
Provides:       tex(russ.sty) = %{tl_version}

%description -n texlive-russ
The package aims to facilitate Russian typesetting (based on input using
MicroSoft Code Page 1251). Russian hyphenation is selected, and various
mathematical commands are set up in Russian style. Furthermore all Cyrillic
letters' catcodes are set to "letter", so that commands with Cyrillic letters
in their names may be defined.

%package -n texlive-serbian-apostrophe
Summary:        Commands for Serbian words with apostrophes
Version:        svn23799
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tipa.sty)
Requires:       tex(xspace.sty)
Provides:       tex(serbian-apostrophe.sty) = %{tl_version}

%description -n texlive-serbian-apostrophe
The package provides a collection of commands (whose names are Serbian words)
whose expansion is the Serbian word with appropriate apostrophes.

%package -n texlive-serbian-date-lat
Summary:        Updated date typesetting for Serbian
Version:        svn23446
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(serbian-date-lat.sty) = %{tl_version}

%description -n texlive-serbian-date-lat
Babel defines dates for Serbian texts, in Latin script. The style it uses does
not match current practices. The present package defines a \date command that
solves the problem.

%package -n texlive-serbian-def-cyr
Summary:        Serbian cyrillic localization
Version:        svn23734
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(inputenc.sty)
Provides:       tex(serbian-def-cyr.sty) = %{tl_version}

%description -n texlive-serbian-def-cyr
This package provides abstract, chapter, title, date etc, for serbian language
in cyrillic scripts in T2A encoding and cp1251 code pages.

%package -n texlive-serbian-lig
Summary:        Control ligatures in Serbian
Version:        svn53127
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(serbian-lig.sty) = %{tl_version}

%description -n texlive-serbian-lig
The package suppresses fi and fl (and other ligatures) in Serbian text written
using Roman script.

%package -n texlive-t2
Summary:        Support for using T2 encoding
Version:        svn47870
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(enumerate.sty)
Provides:       tex(alias-cmc.tex) = %{tl_version}
Provides:       tex(alias-wncy.tex) = %{tl_version}
Provides:       tex(citehack.sty) = %{tl_version}
Provides:       tex(cyralias.tex) = %{tl_version}
Provides:       tex(fnstcorr.tex) = %{tl_version}
Provides:       tex(mathtext.sty) = %{tl_version}
Provides:       tex(misccorr.sty) = %{tl_version}

%description -n texlive-t2
The T2 bundle provides a variety of separate support functions for using
Cyrillic characters in LaTeX: the mathtext package, for using Cyrillic letters
'transparently' in formulae; the citehack package, for using Cyrillic (or
indeed any non-ascii) characters in citation keys; support for Cyrillic in
BibTeX; support for Cyrillic in Makeindex; and various items of font support.

%package -n texlive-texlive-ru
Summary:        TeX Live manual (Russian)
Version:        svn58426
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-ru-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-ru-doc <= 11:%{version}

%description -n texlive-texlive-ru
TeX Live manual (Russian)

%package -n texlive-texlive-sr
Summary:        TeX Live manual (Serbian)
Version:        svn54594
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-sr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-sr-doc <= 11:%{version}

%description -n texlive-texlive-sr
TeX Live manual (Serbian)

%package -n texlive-ukrhyph
Summary:        Hyphenation Patterns for Ukrainian
Version:        svn21081
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(catlcy.tex) = %{tl_version}
Provides:       tex(lcy2koi.tex) = %{tl_version}
Provides:       tex(lcy2lcy.tex) = %{tl_version}
Provides:       tex(lcy2ot2.tex) = %{tl_version}
Provides:       tex(lcy2t2a.tex) = %{tl_version}
Provides:       tex(lcy2ucy.tex) = %{tl_version}
Provides:       tex(rules60.tex) = %{tl_version}
Provides:       tex(rules90.tex) = %{tl_version}
Provides:       tex(rules_ph.tex) = %{tl_version}
Provides:       tex(ukrenhyp.tex) = %{tl_version}
Provides:       tex(ukrhypfa.tex) = %{tl_version}
Provides:       tex(ukrhyph.tex) = %{tl_version}
Provides:       tex(ukrhypmp.tex) = %{tl_version}
Provides:       tex(ukrhypmt.tex) = %{tl_version}
Provides:       tex(ukrhypsm.tex) = %{tl_version}
Provides:       tex(ukrhypst.tex) = %{tl_version}

%description -n texlive-ukrhyph
A range of patterns, depending on the encoding of the output font (including
the standard T2A, so one can use the patterns with free fonts).

%package -n texlive-xecyrmongolian
Summary:        Basic support for the typesetting of Cyrillic Mongolian documents using (Xe|Lua)LaTeX
Version:        svn53160
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luahyphenrules.sty)
Provides:       tex(xecyrmongolian.sty) = %{tl_version}

%description -n texlive-xecyrmongolian
The 'xecyrmongolian' package can be used to produce documents in Cyrillic
Mongolian using either XeLaTeX or LuaLaTeX. The command \setlanguage can be
used to load alternative hyphenation patterns so to be able to create
multilingual documents.

%post -n texlive-hyphen-belarusian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/belarusian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "belarusian loadhyph-be.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{belarusian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{belarusian}{loadhyph-be.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-belarusian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/belarusian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{belarusian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-bulgarian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/bulgarian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "bulgarian loadhyph-bg.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{bulgarian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{bulgarian}{loadhyph-bg.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-bulgarian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/bulgarian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{bulgarian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-churchslavonic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/churchslavonic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "churchslavonic loadhyph-cu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{churchslavonic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{churchslavonic}{loadhyph-cu.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-churchslavonic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/churchslavonic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{churchslavonic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-mongolian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/mongolian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "mongolian loadhyph-mn-cyrl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{mongolian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/mongolianlmc.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "mongolianlmc loadhyph-mn-cyrl-x-lmc.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{mongolianlmc}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-mongolian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/mongolian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{mongolian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/mongolianlmc.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{mongolianlmc}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-russian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/russian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "russian loadhyph-ru.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{russian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-russian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/russian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{russian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-serbian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/serbian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "serbian loadhyph-sr-latn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{serbian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/serbianc.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "serbianc loadhyph-sr-cyrl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{serbianc}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-serbian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/serbian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{serbian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/serbianc.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{serbianc}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-ukrainian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ukrainian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ukrainian loadhyph-uk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ukrainian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ukrainian}{loadhyph-uk.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ukrainian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ukrainian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ukrainian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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
tar -xf %{SOURCE70} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE71} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE72} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE73} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE74} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE75} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE76} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE77} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE78} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE79} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-belarusian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-belarusian/
%doc %{_texmf_main}/doc/generic/babel-belarusian/

%files -n texlive-babel-bulgarian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-bulgarian/
%doc %{_texmf_main}/doc/generic/babel-bulgarian/

%files -n texlive-babel-russian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-russian/
%doc %{_texmf_main}/doc/generic/babel-russian/

%files -n texlive-babel-serbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-serbian/
%doc %{_texmf_main}/doc/generic/babel-serbian/

%files -n texlive-babel-serbianc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-serbianc/
%doc %{_texmf_main}/doc/generic/babel-serbianc/

%files -n texlive-babel-ukrainian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-ukrainian/
%doc %{_texmf_main}/doc/generic/babel-ukrainian/

%files -n texlive-churchslavonic
%license mit.txt
%{_texmf_main}/tex/latex/churchslavonic/
%doc %{_texmf_main}/doc/latex/churchslavonic/

%files -n texlive-cmcyr
%license pd.txt
%{_texmf_main}/fonts/map/dvips/cmcyr/
%{_texmf_main}/fonts/source/public/cmcyr/
%{_texmf_main}/fonts/tfm/public/cmcyr/
%{_texmf_main}/fonts/type1/public/cmcyr/
%{_texmf_main}/fonts/vf/public/cmcyr/
%doc %{_texmf_main}/doc/fonts/cmcyr/

%files -n texlive-cyrplain
%license lppl1.3c.txt
%{_texmf_main}/tex/plain/cyrplain/

%files -n texlive-disser
%license lppl1.3c.txt
%{_texmf_main}/makeindex/disser/
%{_texmf_main}/tex/latex/disser/
%doc %{_texmf_main}/doc/latex/disser/

%files -n texlive-eskd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eskd/
%doc %{_texmf_main}/doc/latex/eskd/

%files -n texlive-eskdx
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eskdx/
%doc %{_texmf_main}/doc/latex/eskdx/

%files -n texlive-gost
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/gost/
%{_texmf_main}/bibtex/csf/gost/
%doc %{_texmf_main}/doc/bibtex/gost/

%files -n texlive-hyphen-belarusian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-bulgarian
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-churchslavonic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-mongolian
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-russian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-serbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-ukrainian
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-lcyw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lcyw/
%doc %{_texmf_main}/doc/latex/lcyw/

%files -n texlive-lh
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/lh/base/
%{_texmf_main}/fonts/source/lh/lh-XSlav/
%{_texmf_main}/fonts/source/lh/lh-conc/
%{_texmf_main}/fonts/source/lh/lh-lcy/
%{_texmf_main}/fonts/source/lh/lh-ot2/
%{_texmf_main}/fonts/source/lh/lh-t2a/
%{_texmf_main}/fonts/source/lh/lh-t2b/
%{_texmf_main}/fonts/source/lh/lh-t2c/
%{_texmf_main}/fonts/source/lh/lh-t2d/
%{_texmf_main}/fonts/source/lh/lh-x2/
%{_texmf_main}/fonts/source/lh/nont2/
%{_texmf_main}/fonts/source/lh/specific/
%{_texmf_main}/tex/latex/lh/
%{_texmf_main}/tex/plain/lh/
%doc %{_texmf_main}/doc/fonts/lh/

%files -n texlive-lhcyr
%license other-free.txt
%{_texmf_main}/tex/latex/lhcyr/

%files -n texlive-lshort-bulgarian
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-bulgarian/

%files -n texlive-lshort-mongol
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/lshort-mongol/

%files -n texlive-lshort-russian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-russian/

%files -n texlive-lshort-ukr
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-ukr/

%files -n texlive-mnhyphn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mnhyphn/
%doc %{_texmf_main}/doc/latex/mnhyphn/

%files -n texlive-mongolian-babel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mongolian-babel/
%doc %{_texmf_main}/doc/latex/mongolian-babel/

%files -n texlive-montex
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/montex/
%{_texmf_main}/fonts/source/public/montex/
%{_texmf_main}/fonts/tfm/public/montex/
%{_texmf_main}/fonts/type1/public/montex/
%{_texmf_main}/tex/latex/montex/
%doc %{_texmf_main}/doc/latex/montex/

%files -n texlive-mpman-ru
%license other-free.txt
%doc %{_texmf_main}/doc/metapost/mpman-ru/

%files -n texlive-numnameru
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numnameru/
%doc %{_texmf_main}/doc/latex/numnameru/

%files -n texlive-pst-eucl-translation-bg
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/pst-eucl-translation-bg/

%files -n texlive-ruhyphen
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ruhyphen/

%files -n texlive-russ
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/russ/
%doc %{_texmf_main}/doc/latex/russ/

%files -n texlive-serbian-apostrophe
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/serbian-apostrophe/
%doc %{_texmf_main}/doc/latex/serbian-apostrophe/

%files -n texlive-serbian-date-lat
%license gpl2.txt
%{_texmf_main}/tex/latex/serbian-date-lat/
%doc %{_texmf_main}/doc/latex/serbian-date-lat/

%files -n texlive-serbian-def-cyr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/serbian-def-cyr/
%doc %{_texmf_main}/doc/latex/serbian-def-cyr/

%files -n texlive-serbian-lig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/serbian-lig/
%doc %{_texmf_main}/doc/latex/serbian-lig/

%files -n texlive-t2
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/t2/
%{_texmf_main}/tex/generic/t2/
%{_texmf_main}/tex/latex/t2/
%doc %{_texmf_main}/doc/generic/t2/

%files -n texlive-texlive-ru
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-ru/

%files -n texlive-texlive-sr
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-sr/

%files -n texlive-ukrhyph
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ukrhyph/
%doc %{_texmf_main}/doc/generic/ukrhyph/

%files -n texlive-xecyrmongolian
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xecyrmongolian/
%doc %{_texmf_main}/doc/latex/xecyrmongolian/

%changelog
* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn69727-4
- fix licensing files

* Thu Jan 15 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn69727-3
- fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn69727-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn69727-1
- Update to TeX Live 2025
