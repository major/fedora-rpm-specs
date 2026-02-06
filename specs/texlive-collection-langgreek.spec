%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langgreek
Epoch:          12
Version:        svn65038
Release:        3%{?dist}
Summary:        Greek

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langgreek.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-greek.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-greek.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/begingreek.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/begingreek.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/betababel.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/betababel.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts-fd.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cbfonts-fd.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsbaskerville.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsbaskerville.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsporson.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gfsporson.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-fontenc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-fontenc.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-inputenc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greek-inputenc.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greekdates.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greekdates.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektex.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektex.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektonoi.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/greektonoi.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-ancientgreek.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-greek.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-greek.doc.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibycus-babel.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibycus-babel.doc.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibygrk.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ibygrk.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kerkis.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kerkis.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/levy.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/levy.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgreek.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgreek.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgrmath.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lgrmath.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/talos.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/talos.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/teubner.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/teubner.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xgreek.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xgreek.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yannisgr.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yannisgr.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-greek
Requires:       texlive-begingreek
Requires:       texlive-betababel
Requires:       texlive-cbfonts
Requires:       texlive-cbfonts-fd
Requires:       texlive-collection-basic
Requires:       texlive-gfsbaskerville
Requires:       texlive-gfsporson
Requires:       texlive-greek-fontenc
Requires:       texlive-greek-inputenc
Requires:       texlive-greekdates
Requires:       texlive-greektex
Requires:       texlive-greektonoi
Requires:       texlive-hyphen-ancientgreek
Requires:       texlive-hyphen-greek
Requires:       texlive-ibycus-babel
Requires:       texlive-ibygrk
Requires:       texlive-kerkis
Requires:       texlive-levy
Requires:       texlive-lgreek
Requires:       texlive-lgrmath
Requires:       texlive-mkgrkindex
Requires:       texlive-talos
Requires:       texlive-teubner
Requires:       texlive-xgreek
Requires:       texlive-yannisgr

%description
Support for Greek.


%package -n texlive-babel-greek
Summary:        Babel support for the Greek language and script
Version:        svn68532
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(athnum.sty) = %{tl_version}
Provides:       tex(greek.ldf) = %{tl_version}
Provides:       tex(grmath.sty) = %{tl_version}

%description -n texlive-babel-greek
The bundle provides comprehensive support for the Greek language and script via
the Babel system. Document authors can select between the monotonic
(single-diacritic), polytonic (multiple-diacritic), and ancient orthography of
the Greek language. Included are the packages grmath for Greek function names
in mathematics, and athnum for Attic numerals.

%package -n texlive-begingreek
Summary:        Greek environment to be used with pdfLaTeX only
Version:        svn63255
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(begingreek.sty) = %{tl_version}

%description -n texlive-begingreek
This simple package defines a greek environment to be used with pdfLaTeX only,
that accepts an optional Greek font family name to type its contents with. A
similar \greektxt command does a similar action for shorter texts.

%package -n texlive-betababel
Summary:        Insert ancient greek text coded in Beta Code
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(teubner.sty)
Provides:       tex(betababel.sty) = %{tl_version}

%description -n texlive-betababel
The betababel package extends the babel polutonikogreek option to provide a
simple way to insert ancient Greek texts with diacritical characters into your
document using the commonly used Beta Code transliteration. You can directly
insert Beta Code texts -- as they can be found at the Perseus project, for
example -- without modification.

%package -n texlive-cbfonts
Summary:        Complete set of Greek fonts
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cbfonts-fd

%description -n texlive-cbfonts
This bundle presents the whole of Beccari's original Greek font set, which use
the 'Lispiakos' font shape derived from the shape of the fonts used in
printers' shops in Lispia. The fonts are available both as Metafont source and
in Adobe Type 1 format, and at the same wide set of design sizes as are such
font sets as the EC fonts. Please note that this package needs the
complementary cbfonts-fd package to work properly.

%package -n texlive-cbfonts-fd
Summary:        LaTeX font description files for the CB Greek fonts
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cbfonts-fd
The package provides font description files for all the many shapes available
from the cbfonts collection. The files provide the means whereby the NFSS knows
which fonts a LaTeX user is requesting. The package depends on
cbgreek-complete.

%package -n texlive-gfsbaskerville
Summary:        A Greek font, from one such by Baskerville
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfsbaskerville.sty) = %{tl_version}

%description -n texlive-gfsbaskerville
The font is a digital implementation of Baskerville's classic Greek font,
provided by the Greek Font Society. The font covers Greek only, and LaTeX
support provides for the use of LGR encoding.

%package -n texlive-gfsporson
Summary:        A Greek font, originally from Porson
Version:        svn18651
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gfsporson.sty) = %{tl_version}

%description -n texlive-gfsporson
Porson is an elegant Greek font, originally cut at the turn of the 19th Century
in England. The present version has been provided by the Greek Font Society.
The font supports the Greek alphabet only. LaTeX support is provided, using the
LGR encoding.

%package -n texlive-greek-fontenc
Summary:        LICR macros and encoding definition files for Greek
Version:        svn68877
License:        LPPL-1.3c AND BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(alphabeta.sty) = %{tl_version}
Provides:       tex(greek-euenc.def) = %{tl_version}
Provides:       tex(greek-fontenc.def) = %{tl_version}
Provides:       tex(lgrenc.def) = %{tl_version}
Provides:       tex(puenc-greek.def) = %{tl_version}
Provides:       tex(textalpha.sty) = %{tl_version}
Provides:       tex(tuenc-greek.def) = %{tl_version}

%description -n texlive-greek-fontenc
LICR macros for characters from the Greek script and encoding definition files
for Greek text font encodings.

%package -n texlive-greek-inputenc
Summary:        Greek encoding support for inputenc
Version:        svn66634
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(iso-8859-7.def) = %{tl_version}
Provides:       tex(macgreek.def) = %{tl_version}

%description -n texlive-greek-inputenc
Input encoding definition files for UTF-8, Macintosh Greek, and ISO 8859-7
enabling the use of literal characters for Greek letters and symbols with 8-bit
TeX engines (pdfLaTeX).

%package -n texlive-greekdates
Summary:        Provides ancient Greek day and month names, dates, etc.
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Provides:       tex(greekdates.sty) = %{tl_version}

%description -n texlive-greekdates
The package provides easy access to ancient Greek names of days and months of
various regions of Greece. In case the historical information about a region is
not complete, we use the Athenian name of the month. Moreover commands and
options are provided, in order to completely switch to the "ancient way",
commands such as \today.

%package -n texlive-greektex
Summary:        Fonts for typesetting Greek/English documents
Version:        svn28327
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(greektex.sty) = %{tl_version}

%description -n texlive-greektex
The fonts are based on Silvio Levy's classical Greek fonts; macros and Greek
hyphenation patterns for the fonts' encoding are also provided.

%package -n texlive-greektonoi
Summary:        Facilitates writing/editing of multiaccented greek
Version:        svn39419
License:        LGPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(greektonoi.sty) = %{tl_version}

%description -n texlive-greektonoi
The greektonoi mapping extends the betababel package or the babel
polutonikogreek option to provide a simple way to insert ancient Greek texts
with diacritical characters into your document using a similar method to the
commonly used Beta Code transliteration, but with much more freedom. It is
designed especially for the XeTeX engine and it could also be used for fast and
easy modification of monotonic greek texts to polytonic. The output text is
natively encoded in Unicode, so it can be reused in any possible way. The
greektonoi package provides, in addition to inserting greek accents and
breathings, many other symbols used in greek numbers and arithmetic or in the
greek archaic period. It could be used with greektonoi mapping or indepedently.

%package -n texlive-hyphen-ancientgreek
Summary:        Ancient Greek hyphenation patterns.
Version:        svn74823
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(grahyph5.tex) = %{tl_version}
Provides:       tex(hyph-grc.tex) = %{tl_version}
Provides:       tex(ibyhyph.tex) = %{tl_version}
Provides:       tex(loadhyph-grc.tex) = %{tl_version}

%description -n texlive-hyphen-ancientgreek
Hyphenation patterns for Ancient Greek in LGR and UTF-8 encodings, including
support for (obsolete) Ibycus font encoding. Patterns in UTF-8 use two code
positions for each of the vowels with acute accent (a.k.a tonos, oxia), e.g.,
U+03AE, U+1F75 for eta.

%package -n texlive-hyphen-greek
Summary:        Modern Greek hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(grmhyph5.tex) = %{tl_version}
Provides:       tex(grphyph5.tex) = %{tl_version}
Provides:       tex(hyph-el-monoton.tex) = %{tl_version}
Provides:       tex(hyph-el-polyton.tex) = %{tl_version}
Provides:       tex(loadhyph-el-monoton.tex) = %{tl_version}
Provides:       tex(loadhyph-el-polyton.tex) = %{tl_version}

%description -n texlive-hyphen-greek
Hyphenation patterns for Modern Greek in monotonic and polytonic spelling in
LGR and UTF-8 encodings. Patterns in UTF-8 use two code positions for each of
the vowels with acute accent (a.k.a tonos, oxia), e.g., U+03AC, U+1F71 for
alpha.

%package -n texlive-ibycus-babel
Summary:        Use the Ibycus 4 Greek font with Babel
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ibycus.ldf) = %{tl_version}
Provides:       tex(lgienc.def) = %{tl_version}

%description -n texlive-ibycus-babel
The package allows you to use the Ibycus 4 font for ancient Greek with Babel.
It uses a Perl script to generate hyphenation patterns for Ibycus from those
for the ordinary Babel encoding, cbgreek. It sets up ibycus as a
pseudo-language you can specify in the normal Babel manner. For proper
hyphenation of Greek quoted in mid-paragraph, you should use it with elatex
(all current distributions of LaTeX are built with e-TeX, so the constraint
should not be onerous).

%package -n texlive-ibygrk
Summary:        Fonts and macros to typeset ancient Greek
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(iby4extr.tex) = %{tl_version}
Provides:       tex(ibycus4.sty) = %{tl_version}
Provides:       tex(ibycus4.tex) = %{tl_version}
Provides:       tex(ibycusps.tex) = %{tl_version}
Provides:       tex(psibycus.sty) = %{tl_version}
Provides:       tex(pssetiby.tex) = %{tl_version}
Provides:       tex(setiby4.tex) = %{tl_version}
Provides:       tex(tlgsqq.tex) = %{tl_version}
Provides:       tex(version4.tex) = %{tl_version}

%description -n texlive-ibygrk
Ibycus is a Greek typeface, based on Silvio Levy's realisation of a classic
Didot cut of Greek type from around 1800. The fonts are available both as
Metafont source and in Adobe Type 1 format. This distribution of ibycus is
accompanied by a set of macro packages to use it with Plain TeX or LaTeX, but
for use with Babel, see the ibycus-babel package.

%package -n texlive-kerkis
Summary:        Kerkis (Greek) font family
Version:        svn56271
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(txfonts.sty)
Provides:       tex(kerkis.sty) = %{tl_version}
Provides:       tex(kmath.sty) = %{tl_version}

%description -n texlive-kerkis
Sans-serif Greek fonts to match the URW Bookman set (which are distributed with
Kerkis). The Kerkis font set has some support for mathematics as well as other
glyphs missing from the base URW Bookman fonts. Macros are provided to use the
fonts in OT1, T1 (only NG/ng glyphs missing) and LGR encodings, as well as in
mathematics; small caps and old-style number glyphs are also available. The
philosophy, and the design process, of the Kerkis fonts is discussed in a paper
in TUGboat 23(3/4), 2002.

%package -n texlive-levy
Summary:        Fonts for typesetting classical greek
Version:        svn76924
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(greekmacros.tex) = %{tl_version}
Provides:       tex(slgreek.sty) = %{tl_version}

%description -n texlive-levy
These fonts are derivatives of Knuth's CM fonts. Macros for use with Plain TeX
are included in the package; for use with LaTeX, see lgreek (with English
documentation) or levy (with German documentation).

%package -n texlive-lgreek
Summary:        LaTeX macros for using Silvio Levy's Greek fonts
Version:        svn21818
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(LGenc.def) = %{tl_version}
Provides:       tex(lgreek.sty) = %{tl_version}

%description -n texlive-lgreek
A conversion of Silvio Levy's Plain TeX macros for use with LaTeX.

%package -n texlive-lgrmath
Summary:        Use LGR-encoded fonts in math mode
Version:        svn65038
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(lgrmath.sty) = %{tl_version}

%description -n texlive-lgrmath
The lgrmath package is a LaTeX package which sets the Greek letters in math
mode to use glyphs from the LGR-encoded font of one's choice. The documentation
includes a rather extensive list of the available font family names on typical
LaTeX installations.

%package -n texlive-talos
Summary:        A Greek cult font from the eighties
Version:        svn61820
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-talos
A cult Greek font from the eighties, used at the University of Crete, Greece.
It belonged to the first TeX installation in a Greek University and most
probably the first TeX installation that supported the Greek language.

%package -n texlive-teubner
Summary:        Philological typesetting of classical Greek
Version:        svn68074
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(exscale.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(trace.sty)
Provides:       tex(teubner.sty) = %{tl_version}
Provides:       tex(teubnertx.sty) = %{tl_version}

%description -n texlive-teubner
An extension to babel greek option for typesetting classical Greek with a
philological approach. The package works with the author's greek fonts using
the 'Lispiakos' font shape derived from that of the fonts used in printers'
shops in Lispia. The package name honours the publisher B.G. Teubner
Verlaggesellschaft whose Greek text publications are of high quality.

%package -n texlive-xgreek
Summary:        Greek Language Support for XeLaTeX and LuaLaTeX
Version:        svn73620
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listings.sty)
Requires:       tex(luahyphenrules.sty)
Provides:       tex(xelistings.sty) = %{tl_version}
Provides:       tex(xgreek.sty) = %{tl_version}

%description -n texlive-xgreek
This package has been designed so to allow people to typeset Greek language
documents using XeLaTeX or LuaLaTeX. It is released in the hope that people
will use it and spot errors, bugs, features so to improve it. Practically, it
provides all the capabilities of the greek option of the babel package. The
package can be invoked with any of the following options: monotonic (for
typesetting modern monotonic Greek), polytonic (for typesetting modern
polytonic Greek), and ancient (for typesetting ancient texts). The default
option is monotonic. The command \setlanguage{<lang>} activates the hyphenation
patterns of the language <lang>. This, however, can only be done if the format
file has not been built with the babel mechanism.

%package -n texlive-yannisgr
Summary:        Greek fonts by Yannis Haralambous
Version:        svn22613
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-yannisgr
A family of 7-bit fonts with a code table designed for setting modern polytonic
Greek. The fonts are provided as Metafont source; macros to produce a Greek
variant of Plain TeX (including a hyphenation table adapted to the fonts' code
table) are provided.

%post -n texlive-hyphen-ancientgreek
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ancientgreek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ancientgreek loadhyph-grc.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ancientgreek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/ibycus.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ibycus ibyhyph.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ibycus}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ancientgreek
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ancientgreek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ancientgreek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/ibycus.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ibycus}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-greek
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/greek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "greek loadhyph-el-polyton.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=polygreek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=polygreek" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{greek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{greek}{loadhyph-el-polyton.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{polygreek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{polygreek}{loadhyph-el-polyton.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/monogreek.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "monogreek loadhyph-el-monoton.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{monogreek}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{monogreek}{loadhyph-el-monoton.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-greek
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/greek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=polygreek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{greek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{polygreek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/monogreek.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{monogreek}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-greek
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-greek/
%doc %{_texmf_main}/doc/generic/babel-greek/

%files -n texlive-begingreek
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/begingreek/
%doc %{_texmf_main}/doc/latex/begingreek/

%files -n texlive-betababel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/betababel/
%doc %{_texmf_main}/doc/latex/betababel/

%files -n texlive-cbfonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/cbfonts/
%{_texmf_main}/fonts/map/dvips/cbfonts/
%{_texmf_main}/fonts/source/public/cbfonts/
%{_texmf_main}/fonts/tfm/public/cbfonts/
%{_texmf_main}/fonts/type1/public/cbfonts/
%doc %{_texmf_main}/doc/fonts/cbfonts/

%files -n texlive-cbfonts-fd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cbfonts-fd/
%doc %{_texmf_main}/doc/fonts/cbfonts-fd/

%files -n texlive-gfsbaskerville
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsbaskerville/
%{_texmf_main}/fonts/enc/dvips/gfsbaskerville/
%{_texmf_main}/fonts/map/dvips/gfsbaskerville/
%{_texmf_main}/fonts/opentype/public/gfsbaskerville/
%{_texmf_main}/fonts/tfm/public/gfsbaskerville/
%{_texmf_main}/fonts/type1/public/gfsbaskerville/
%{_texmf_main}/fonts/vf/public/gfsbaskerville/
%{_texmf_main}/tex/latex/gfsbaskerville/
%doc %{_texmf_main}/doc/fonts/gfsbaskerville/

%files -n texlive-gfsporson
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/gfsporson/
%{_texmf_main}/fonts/enc/dvips/gfsporson/
%{_texmf_main}/fonts/map/dvips/gfsporson/
%{_texmf_main}/fonts/opentype/public/gfsporson/
%{_texmf_main}/fonts/tfm/public/gfsporson/
%{_texmf_main}/fonts/type1/public/gfsporson/
%{_texmf_main}/fonts/vf/public/gfsporson/
%{_texmf_main}/tex/latex/gfsporson/
%doc %{_texmf_main}/doc/fonts/gfsporson/

%files -n texlive-greek-fontenc
%license lppl1.3c.txt
%license bsd2.txt
%{_texmf_main}/tex/latex/greek-fontenc/
%doc %{_texmf_main}/doc/latex/greek-fontenc/

%files -n texlive-greek-inputenc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/greek-inputenc/
%doc %{_texmf_main}/doc/latex/greek-inputenc/

%files -n texlive-greekdates
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/greekdates/
%doc %{_texmf_main}/doc/latex/greekdates/

%files -n texlive-greektex
%license pd.txt
%{_texmf_main}/tex/latex/greektex/
%doc %{_texmf_main}/doc/fonts/greektex/

%files -n texlive-greektonoi
%license lgpl.txt
%{_texmf_main}/fonts/map/dvips/greektonoi/
%{_texmf_main}/tex/latex/greektonoi/
%doc %{_texmf_main}/doc/latex/greektonoi/

%files -n texlive-hyphen-ancientgreek
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%{_texmf_main}/tex/generic/hyphen/

%files -n texlive-hyphen-greek
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%{_texmf_main}/tex/generic/hyphen/
%doc %{_texmf_main}/doc/generic/elhyphen/

%files -n texlive-ibycus-babel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ibycus-babel/
%doc %{_texmf_main}/doc/latex/ibycus-babel/

%files -n texlive-ibygrk
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/ibygrk/
%{_texmf_main}/fonts/enc/dvips/ibygrk/
%{_texmf_main}/fonts/map/dvips/ibygrk/
%{_texmf_main}/fonts/source/public/ibygrk/
%{_texmf_main}/fonts/tfm/public/ibygrk/
%{_texmf_main}/fonts/type1/public/ibygrk/
%{_texmf_main}/tex/generic/ibygrk/
%doc %{_texmf_main}/doc/fonts/ibygrk/

%files -n texlive-kerkis
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/kerkis/
%{_texmf_main}/fonts/enc/dvips/kerkis/
%{_texmf_main}/fonts/map/dvips/kerkis/
%{_texmf_main}/fonts/opentype/public/kerkis/
%{_texmf_main}/fonts/tfm/public/kerkis/
%{_texmf_main}/fonts/type1/public/kerkis/
%{_texmf_main}/fonts/vf/public/kerkis/
%{_texmf_main}/tex/latex/kerkis/
%doc %{_texmf_main}/doc/fonts/kerkis/

%files -n texlive-levy
%license gpl2.txt
%{_texmf_main}/fonts/source/public/levy/
%{_texmf_main}/fonts/tfm/public/levy/
%{_texmf_main}/tex/generic/levy/
%doc %{_texmf_main}/doc/fonts/levy/

%files -n texlive-lgreek
%license gpl2.txt
%{_texmf_main}/tex/latex/lgreek/
%doc %{_texmf_main}/doc/latex/lgreek/

%files -n texlive-lgrmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lgrmath/
%doc %{_texmf_main}/doc/latex/lgrmath/

%files -n texlive-talos
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/talos/
%doc %{_texmf_main}/doc/fonts/talos/

%files -n texlive-teubner
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/teubner/
%doc %{_texmf_main}/doc/latex/teubner/

%files -n texlive-xgreek
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xgreek/
%doc %{_texmf_main}/doc/latex/xgreek/

%files -n texlive-yannisgr
%license gpl2.txt
%{_texmf_main}/fonts/source/public/yannisgr/
%{_texmf_main}/fonts/tfm/public/yannisgr/
%doc %{_texmf_main}/doc/fonts/yannisgr/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn65038-3
- Fix licensing, descriptions, update components to latest

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn65038-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn65038-1
- Update to TeX Live 2025
