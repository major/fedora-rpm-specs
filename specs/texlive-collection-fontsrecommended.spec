%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-fontsrecommended
Epoch:          12
Version:        svn54074
Release:        6%{?dist}
Summary:        Recommended fonts

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-fontsrecommended.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/avantgar.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookman.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/charter.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/charter.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-super.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm-super.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmextra.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/courier.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro-ce.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euro-ce.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eurosym.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eurosym.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fpl.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fpl.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/helvetic.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm-math.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lm-math.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marvosym.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/marvosym.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpazo.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathpazo.doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/manfnt-font.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflogo-font.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflogo-font.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ncntrsbk.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/palatino.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxfonts.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxfonts.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsfs.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rsfs.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/symbol.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre-math.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre-math.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/times.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipa.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipa.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txfonts.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/txfonts.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utopia.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utopia.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy-type1.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasy-type1.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasysym.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wasysym.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zapfchan.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zapfding.tar.xz

# AppStream metadata for font components
Source56:        lm.metainfo.xml
Source57:        lm-math.metainfo.xml
Source58:        tex-gyre.metainfo.xml
Source59:        tex-gyre-math.metainfo.xml
BuildRequires:  texlive-base
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-avantgar
Requires:       texlive-bookman
Requires:       texlive-charter
Requires:       texlive-cm-super
Requires:       texlive-cmextra
Requires:       texlive-courier
Requires:       texlive-euro
Requires:       texlive-euro-ce
Requires:       texlive-eurosym
Requires:       texlive-fpl
Requires:       texlive-helvetic
Requires:       texlive-lm
Requires:       texlive-lm-math
Requires:       texlive-marvosym
Requires:       texlive-mathpazo
Requires:       texlive-manfnt-font
Requires:       texlive-mflogo-font
Requires:       texlive-ncntrsbk
Requires:       texlive-palatino
Requires:       texlive-pxfonts
Requires:       texlive-rsfs
Requires:       texlive-symbol
Requires:       texlive-tex-gyre
Requires:       texlive-tex-gyre-math
Requires:       texlive-times
Requires:       texlive-tipa
Requires:       texlive-txfonts
Requires:       texlive-utopia
Requires:       texlive-wasy
Requires:       texlive-wasy-type1
Requires:       texlive-wasysym
Requires:       texlive-zapfchan
Requires:       texlive-zapfding

%description
Recommended fonts, including the base 35 PostScript fonts, Latin Modern, TeX
Gyre, and T1 and other encoding support for Computer Modern, in outline form.


%package -n texlive-avantgar
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-avantgar
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-bookman
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bookman
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-charter
Summary:        Charter fonts
Version:        svn15878
License:        LicenseRef-Charter
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-charter
A commercial text font donated for the common good. Support for use with LaTeX
is available in freenfss, part of psnfss.

%package -n texlive-cm-super
Summary:        CM-Super family of fonts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(type1ec.sty) = %{tl_version}

%description -n texlive-cm-super
The CM-Super family provides Adobe Type 1 fonts that replace the T1/TS1-encoded
Computer Modern (EC/TC), T1/TS1-encoded Concrete, T1/TS1-encoded CM bright and
LH Cyrillic fonts (thus supporting all European languages except Greek), and
bringing many ameliorations in typesetting quality. The fonts exhibit the same
metrics as the Metafont-encoded originals.

%package -n texlive-cmextra
Summary:        Knuth's local information
Version:        svn57866
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmextra
A collection of experimental programs and developments based on, or
complementary to, the matter in his distribution directories.

%package -n texlive-courier
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-courier
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-euro
Summary:        Provide Euro values for national currency amounts
Version:        svn22191
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp-basic.sty)
Requires:       tex(fp-snap.sty)
Provides:       tex(euro.sty) = %{tl_version}

%description -n texlive-euro
Converts arbitrary national currency amounts using the Euro as base unit, and
typesets monetary amounts in almost any desired way. Write, e.g., \ATS{17.6} to
get something like '17,60 oS (1,28 Euro)' automatically. Conversion rates for
the initial Euro-zone countries are already built-in. Further rates can be
added easily. The package uses the fp package to do its sums.

%package -n texlive-euro-ce
Summary:        Euro and CE sign font
Version:        svn25714
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-euro-ce
Metafont source for the symbols in several variants, designed to fit with the
Computer Modern-set text.

%package -n texlive-eurosym
Summary:        Metafont and macros for Euro sign
Version:        svn17265
License:        Eurosym
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eurosym.sty) = %{tl_version}

%description -n texlive-eurosym
The European currency symbol for the Euro implemented in Metafont, using the
official European Commission dimensions, and providing several shapes (normal,
slanted, bold, outline). The package also includes a LaTeX package which
defines the macro, pre-compiled tfm files, and documentation.

%package -n texlive-fpl
Summary:        SC and OsF fonts for URW Palladio L
Version:        svn54512
License:        GPL-2.0-only AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L which are
compatible with respect to metrics with the Palatino SC/OsF fonts from Adobe.
Note that it is not my aim to exactly reproduce the outlines of the original
Adobe fonts. The SC and OsF in the FPL Fonts were designed with the glyphs from
URW Palladio L as starting point. For some glyphs (e.g. 'o') I got the best
result by scaling and boldening. For others (e.g. 'h') shifting selected
portions of the character gave more satisfying results. All this was done using
the free font editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is enabled by the
mathpazo package, which is part of the psnfss distribution.

%package -n texlive-helvetic
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-helvetic
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-lm
Summary:        Latin modern fonts in outline formats
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lmodern.sty) = %{tl_version}

%description -n texlive-lm
The Latin Modern family of fonts consists of 72 text fonts and 20 mathematics
fonts, and is based on the Computer Modern fonts released into public domain by
AMS (copyright (c) 1997 AMS). The lm font set contains a lot of additional
characters, mainly accented ones, but not exclusively. There is one set of
fonts, available both in Adobe Type 1 format (*.pfb) and in OpenType format
(*.otf). There are five sets of TeX Font Metric files, corresponding to: Cork
encoding (cork-*.tfm); QX encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding
(texnansi-*.tfm); T5 (Vietnamese) encoding (t5-*.tfm); and Text Companion for
EC fonts aka TS1 (ts1-*.tfm).

%package -n texlive-lm-math
Summary:        OpenType maths fonts for Latin Modern
Version:        svn67718
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lm-math
Latin Modern Math is a maths companion for the Latin Modern family of fonts, in
OpenType format. For use with LuaLaTeX or XeLaTeX, support is available from
the unicode-math package.

%package -n texlive-manfnt-font
Summary:        Knuth's "manual" fonts
Version:        svn45777
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-manfnt-font
Metafont (by Donald Knuth) and Adobe Type 1 (by Taco Hoekwater) versions of the
font containing the odd symbols Knuth uses in his books. LaTeX support is
available using the manfnt package

%package -n texlive-marvosym
Summary:        Martin Vogel's Symbols (marvosym) font
Version:        svn77677
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(marvosym.sty) = %{tl_version}

%description -n texlive-marvosym
Martin Vogel's Symbol font (marvosym) contains the Euro currency symbol as
defined by the European commission, along with symbols for structural
engineering; symbols for steel cross-sections; astronomy signs (sun, moon,
planets); the 12 signs of the zodiac; scissor symbols; CE sign and others. The
package contains both the original TrueType font and the derived Type 1 font,
together with support files for TeX (LaTeX).

%package -n texlive-mathpazo
Summary:        Fonts to typeset mathematics to match Palatino
Version:        svn77677
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fpl
Requires:       texlive-palatino

%description -n texlive-mathpazo
The Pazo Math fonts are a family of PostScript fonts suitable for typesetting
mathematics in combination with the Palatino family of text fonts. The Pazo
Math family is made up of five fonts provided in Adobe Type 1 format (PazoMath,
PazoMath-Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match Palatino, glyphs
that are usually not available in Palatino and for which Computer Modern looks
odd when combined with Palatino. These glyphs include the uppercase Greek
alphabet in upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold weights, several
mathematical glyphs (partialdiff, summation, product, coproduct, emptyset,
infinity, and proportional) in regular and bold weights, other glyphs (Euro and
dotlessj) in upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number sets (C, I, N, Q,
R, and Z) in blackboard bold. LaTeX macro support (using package mathpazo.sty)
is provided in psnfss (a required part of any LaTeX distribution).

%package -n texlive-mflogo-font
Summary:        Metafont logo font
Version:        svn54512
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mflogo-font
These fonts were created in Metafont by Knuth, for his own publications. At
some stage, the letters 'P' and 'S' were added, so that the MetaPost logo could
also be expressed. The fonts were originally issued (of course) as Metafont
source; they have since been autotraced and reissued in Adobe Type 1 format by
Taco Hoekwater.

%package -n texlive-ncntrsbk
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ncntrsbk
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-palatino
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-palatino
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-pxfonts
Summary:        Palatino-like fonts in support of mathematics
Version:        svn77677
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pxfonts.sty) = %{tl_version}

%description -n texlive-pxfonts
Pxfonts supplies virtual text roman fonts using Adobe Palatino (or
URWPalladioL) with some modified and additional text symbols in the OT1, T1,
and TS1 encodings; maths alphabets using Palatino/Palladio; maths fonts
providing all the symbols of the Computer Modern and AMS fonts, including all
the Greek capital letters from CMR; and additional maths fonts of various other
symbols. The set is complemented by a sans-serif set of text fonts, based on
Helvetica/NimbusSanL, and a monospace set derived from the parallel TX font
set. All the fonts are in Type 1 format (AFM and PFB files), and are supported
by TeX metrics (VF and TFM files) and macros for use with LaTeX.

%package -n texlive-rsfs
Summary:        Ralph Smith's Formal Script font
Version:        svn15878
License:        LicenseRef-Rsfs
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(scrload.tex) = %{tl_version}

%description -n texlive-rsfs
The fonts provide uppercase 'formal' script letters for use as symbols in
scientific and mathematical typesetting (in contrast to the informal script
fonts such as that used for the 'calligraphic' symbols in the TeX maths symbol
font). The fonts are provided as Metafont source, and as derived Adobe Type 1
format. LaTeX support, for using these fonts in mathematics, is available via
one of the packages calrsfs and mathrsfs.

%package -n texlive-symbol
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-symbol
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-tex-gyre
Summary:        TeX Fonts extending freely available URW fonts
Version:        svn68624
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(qbookman.sty) = %{tl_version}
Provides:       tex(qcourier.sty) = %{tl_version}
Provides:       tex(qpalatin.sty) = %{tl_version}
Provides:       tex(qswiss.sty) = %{tl_version}
Provides:       tex(qtimes.sty) = %{tl_version}
Provides:       tex(qzapfcha.sty) = %{tl_version}
Provides:       tex(tgadventor.sty) = %{tl_version}
Provides:       tex(tgbonum.sty) = %{tl_version}
Provides:       tex(tgchorus.sty) = %{tl_version}
Provides:       tex(tgcursor.sty) = %{tl_version}
Provides:       tex(tgheros.sty) = %{tl_version}
Provides:       tex(tgpagella.sty) = %{tl_version}
Provides:       tex(tgschola.sty) = %{tl_version}
Provides:       tex(tgtermes.sty) = %{tl_version}

%description -n texlive-tex-gyre
The TeX-GYRE bundle consists of six font families: TeX Gyre Adventor is based
on the URW Gothic L family of fonts (which is derived from ITC Avant Garde
Gothic, designed by Herb Lubalin and Tom Carnase). TeX Gyre Bonum is based on
the URW Bookman L family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium Italic (from ITC
Zapf Chancery, designed by Hermann Zapf in 1979). TeX-Gyre Cursor is based on
URW Nimbus Mono L (based on Courier, designed by Howard G. Kettler in 1955, for
IBM). TeX Gyre Heros is based on URW Nimbus Sans L (from Helvetica, prepared by
Max Miedinger, with Eduard Hoffmann in 1957). TeX Gyre Pagella is based on URW
Palladio L (from Palatino, designed by Hermann Zapf in the 1940s). TeX Gyre
Schola is based on the URW Century Schoolbook L family (from Century
Schoolbook, designed by Morris Fuller Benton for the American Type Founders).
TeX Gyre Termes is based on the URW Nimbus Roman No9 L family of fonts (from
Times New Roman, designed by Stanley Morison together with Starling Burgess and
Victor Lardent and first offered by Monotype). The constituent standard faces
of each family have been greatly extended (though Chorus omits Greek support
and has no small-caps family). Each family is available in Adobe Type 1 and
Open Type formats, and LaTeX support (for use with a variety of encodings) is
provided. Vietnamese characters were added by Han The Thanh. There are
companion maths fonts for several of these designs, listed in the TeX Gyre Math
package.

%package -n texlive-tex-gyre-math
Summary:        Maths fonts to match tex-gyre text fonts
Version:        svn41264
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tex-gyre-math
TeX-Gyre-Math is a collection of maths fonts to match the text fonts of the
TeX-Gyre collection. The collection is available in OpenType format, only;
fonts conform to the developing standards for OpenType maths fonts.
TeX-Gyre-Math-Bonum (to match TeX-Gyre-Bonum), TeX-Gyre-Math-Pagella (to match
TeX-Gyre-Pagella), TeX-Gyre-Math-Schola (to match TeX-Gyre-Schola) and
TeX-Gyre-Math-Termes (to match TeX-Gyre-Termes) fonts are provided.

%package -n texlive-times
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-times
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-tipa
Summary:        Fonts and macros for IPA phonetics characters
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(exaccent.sty) = %{tl_version}
Provides:       tex(extraipa.sty) = %{tl_version}
Provides:       tex(t3enc.def) = %{tl_version}
Provides:       tex(tipa.sty) = %{tl_version}
Provides:       tex(tipaprm.def) = %{tl_version}
Provides:       tex(tipx.sty) = %{tl_version}
Provides:       tex(tone.sty) = %{tl_version}
Provides:       tex(ts3enc.def) = %{tl_version}
Provides:       tex(vowel.sty) = %{tl_version}
Provides:       tex(xipaprm.def) = %{tl_version}

%description -n texlive-tipa
These fonts are considered the 'ultimate answer' to IPA typesetting. The
encoding of these 8-bit fonts has been registered as LaTeX standard encoding
T3, and the set of addendum symbols as encoding TS3. 'Times-like' Adobe Type 1
versions are provided for both the T3 and the TS3 fonts.

%package -n texlive-txfonts
Summary:        Times-like fonts in support of mathematics
Version:        svn77677
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(txfonts.sty) = %{tl_version}

%description -n texlive-txfonts
Txfonts supplies virtual text roman fonts using Adobe Times (or URW
NimbusRomNo9L) with some modified and additional text symbols in the OT1, T1,
and TS1 encodings; maths alphabets using Times/URW Nimbus; maths fonts
providing all the symbols of the Computer Modern and AMS fonts, including all
the Greek capital letters from CMR; and additional maths fonts of various other
symbols. The set is complemented by a sans-serif set of text fonts, based on
Helvetica/NimbusSanL, and a monospace set. All the fonts are in Type 1 format
(AFM and PFB files), and are supported by TeX metrics (VF and TFM files) and
macros for use with LaTeX.

%package -n texlive-utopia
Summary:        Adobe Utopia fonts
Version:        svn77677
License:        LicenseRef-Utopia
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-utopia
The Adobe Standard Encoding set (upright and italic shapes, medium and bold
weights) of the Utopia font family, which Adobe donated to the X Consortium.
Macro support, and maths fonts that match the Utopia family, are provided by
the Fourier and the Mathdesign font packages.

%package -n texlive-wasy
Summary:        The wasy fonts (Waldi symbol fonts)
Version:        svn53533
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(wasyfont.tex) = %{tl_version}

%description -n texlive-wasy
This font contains all lasy characters (by L.Lamport, copyright notice in
lasychr.mf), and a lot more symbols. Provided are the Metafont files for
5-10pt, and bold and slanted 10pt fonts, together with a .tex and .pdf
documentation, and a file for using the fonts in a PLAIN-TeX document. Type-1
fonts by Michael Sharpe and Taco Hoekwater are available as separate package
wasy-type1. Support under LaTeX is provided by Axel Kielhorn's wasysym package.

%package -n texlive-wasy-type1
Summary:        Type 1 versions of wasy fonts
Version:        svn53534
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-wasy

%description -n texlive-wasy-type1
Converted (Adobe Type 1) outlines of the wasy fonts.

%package -n texlive-wasysym
Summary:        LaTeX support for the wasy fonts
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(wasysym.sty) = %{tl_version}

%description -n texlive-wasysym
The wasy (Waldi Symbol) font by Roland Waldi provides many glyphs like male and
female symbols and astronomical symbols, as well as the complete lasy font set
and other odds and ends. This package implements an easy to use interface for
these symbols.

%package -n texlive-zapfchan
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zapfchan
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).

%package -n texlive-zapfding
Summary:        URW 'Base 35' font pack for LaTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zapfding
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus Mono L
(substituting for Adobe's Courier); Nimbus Roman No9 L (substituting for
Adobe's Times); Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW Chancery L Medium
Italic (substituting for Adobe's Zapf Chancery); URW Gothic L Book
(substituting for Adobe's Avant Garde); and URW Palladio L (substituting for
Adobe's Palatino).


%prep
# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

mkdir -p %{buildroot}%{_datadir}/fonts
mkdir -p %{buildroot}%{_datadir}/appdata

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

# Install AppStream metadata for font components
cp %{SOURCE56} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE57} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE58} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE59} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/lm %{buildroot}%{_datadir}/fonts/lm
ln -sf %{_texmf_main}/fonts/opentype/public/lm-math %{buildroot}%{_datadir}/fonts/lm-math
ln -sf %{_texmf_main}/fonts/opentype/public/tex-gyre %{buildroot}%{_datadir}/fonts/tex-gyre
ln -sf %{_texmf_main}/fonts/opentype/public/tex-gyre-math %{buildroot}%{_datadir}/fonts/tex-gyre-math

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-avantgar
%license gpl2.txt
%{_texmf_main}/dvips/avantgar/
%{_texmf_main}/fonts/afm/adobe/avantgar/
%{_texmf_main}/fonts/afm/urw/avantgar/
%{_texmf_main}/fonts/map/dvips/avantgar/
%{_texmf_main}/fonts/tfm/adobe/avantgar/
%{_texmf_main}/fonts/tfm/urw35vf/avantgar/
%{_texmf_main}/fonts/type1/urw/avantgar/
%{_texmf_main}/fonts/vf/adobe/avantgar/
%{_texmf_main}/fonts/vf/urw35vf/avantgar/
%{_texmf_main}/tex/latex/avantgar/

%files -n texlive-bookman
%license gpl2.txt
%{_texmf_main}/dvips/bookman/
%{_texmf_main}/fonts/afm/adobe/bookman/
%{_texmf_main}/fonts/afm/urw/bookman/
%{_texmf_main}/fonts/map/dvips/bookman/
%{_texmf_main}/fonts/tfm/adobe/bookman/
%{_texmf_main}/fonts/tfm/urw35vf/bookman/
%{_texmf_main}/fonts/type1/urw/bookman/
%{_texmf_main}/fonts/vf/adobe/bookman/
%{_texmf_main}/fonts/vf/urw35vf/bookman/
%{_texmf_main}/tex/latex/bookman/

%files -n texlive-charter
%license other-free.txt
%{_texmf_main}/fonts/afm/bitstrea/charter/
%{_texmf_main}/fonts/tfm/bitstrea/charter/
%{_texmf_main}/fonts/type1/bitstrea/charter/
%{_texmf_main}/fonts/vf/bitstrea/charter/
%doc %{_texmf_main}/doc/fonts/charter/

%files -n texlive-cm-super
%license gpl2.txt
%{_texmf_main}/dvips/cm-super/
%{_texmf_main}/fonts/afm/public/cm-super/
%{_texmf_main}/fonts/enc/dvips/cm-super/
%{_texmf_main}/fonts/map/dvips/cm-super/
%{_texmf_main}/fonts/map/vtex/cm-super/
%{_texmf_main}/fonts/type1/public/cm-super/
%{_texmf_main}/tex/latex/cm-super/
%doc %{_texmf_main}/doc/fonts/cm-super/

%files -n texlive-cmextra
%license pd.txt
%{_texmf_main}/fonts/source/public/cmextra/
%{_texmf_main}/fonts/tfm/public/cmextra/

%files -n texlive-courier
%license gpl2.txt
%{_texmf_main}/dvips/courier/
%{_texmf_main}/fonts/afm/adobe/courier/
%{_texmf_main}/fonts/afm/urw/courier/
%{_texmf_main}/fonts/map/dvips/courier/
%{_texmf_main}/fonts/tfm/adobe/courier/
%{_texmf_main}/fonts/tfm/urw35vf/courier/
%{_texmf_main}/fonts/type1/adobe/courier/
%{_texmf_main}/fonts/type1/urw/courier/
%{_texmf_main}/fonts/vf/adobe/courier/
%{_texmf_main}/fonts/vf/urw35vf/courier/
%{_texmf_main}/tex/latex/courier/

%files -n texlive-euro
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euro/
%doc %{_texmf_main}/doc/latex/euro/

%files -n texlive-euro-ce
%license bsd.txt
%{_texmf_main}/fonts/source/public/euro-ce/
%{_texmf_main}/fonts/tfm/public/euro-ce/
%doc %{_texmf_main}/doc/fonts/euro-ce/

%files -n texlive-eurosym
%license other-free.txt
%{_texmf_main}/fonts/map/dvips/eurosym/
%{_texmf_main}/fonts/source/public/eurosym/
%{_texmf_main}/fonts/tfm/public/eurosym/
%{_texmf_main}/fonts/type1/public/eurosym/
%{_texmf_main}/tex/latex/eurosym/
%doc %{_texmf_main}/doc/fonts/eurosym/

%files -n texlive-fpl
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fpl/
%{_texmf_main}/fonts/type1/public/fpl/
%doc %{_texmf_main}/doc/fonts/fpl/

%files -n texlive-helvetic
%license gpl2.txt
%{_texmf_main}/dvips/helvetic/
%{_texmf_main}/fonts/afm/adobe/helvetic/
%{_texmf_main}/fonts/afm/urw/helvetic/
%{_texmf_main}/fonts/map/dvips/helvetic/
%{_texmf_main}/fonts/tfm/adobe/helvetic/
%{_texmf_main}/fonts/tfm/monotype/helvetic/
%{_texmf_main}/fonts/tfm/urw35vf/helvetic/
%{_texmf_main}/fonts/type1/urw/helvetic/
%{_texmf_main}/fonts/vf/adobe/helvetic/
%{_texmf_main}/fonts/vf/monotype/helvetic/
%{_texmf_main}/fonts/vf/urw35vf/helvetic/
%{_texmf_main}/tex/latex/helvetic/

%files -n texlive-lm
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/lm/
%{_texmf_main}/fonts/enc/dvips/lm/
%{_texmf_main}/fonts/map/dvipdfm/lm/
%{_texmf_main}/fonts/map/dvips/lm/
%{_texmf_main}/fonts/opentype/public/lm/
%{_texmf_main}/fonts/tfm/public/lm/
%{_texmf_main}/fonts/type1/public/lm/
%{_texmf_main}/tex/latex/lm/
%doc %{_texmf_main}/doc/fonts/lm/
%{_datadir}/fonts/lm
%{_datadir}/appdata/lm.metainfo.xml

%files -n texlive-lm-math
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/lm-math/
%doc %{_texmf_main}/doc/fonts/lm-math/
%{_datadir}/fonts/lm-math
%{_datadir}/appdata/lm-math.metainfo.xml

%files -n texlive-manfnt-font
%license knuth.txt
%{_texmf_main}/fonts/afm/hoekwater/manfnt-font/
%{_texmf_main}/fonts/map/dvips/manfnt-font/
%{_texmf_main}/fonts/type1/hoekwater/manfnt-font/

%files -n texlive-marvosym
%license ofl.txt
%{_texmf_main}/fonts/afm/public/marvosym/
%{_texmf_main}/fonts/map/dvips/marvosym/
%{_texmf_main}/fonts/tfm/public/marvosym/
%{_texmf_main}/fonts/truetype/public/marvosym/
%{_texmf_main}/fonts/type1/public/marvosym/
%{_texmf_main}/tex/latex/marvosym/
%doc %{_texmf_main}/doc/fonts/marvosym/

%files -n texlive-mathpazo
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/mathpazo/
%{_texmf_main}/fonts/tfm/public/mathpazo/
%{_texmf_main}/fonts/type1/public/mathpazo/
%{_texmf_main}/fonts/vf/public/mathpazo/
%doc %{_texmf_main}/doc/latex/mathpazo/

%files -n texlive-mflogo-font
%license knuth.txt
%{_texmf_main}/fonts/afm/hoekwater/mflogo-font/
%{_texmf_main}/fonts/map/dvips/mflogo-font/
%{_texmf_main}/fonts/type1/hoekwater/mflogo-font/
%doc %{_texmf_main}/doc/fonts/mflogo-font/

%files -n texlive-ncntrsbk
%license gpl2.txt
%{_texmf_main}/dvips/ncntrsbk/
%{_texmf_main}/fonts/afm/adobe/ncntrsbk/
%{_texmf_main}/fonts/afm/urw/ncntrsbk/
%{_texmf_main}/fonts/map/dvips/ncntrsbk/
%{_texmf_main}/fonts/tfm/adobe/ncntrsbk/
%{_texmf_main}/fonts/tfm/urw35vf/ncntrsbk/
%{_texmf_main}/fonts/type1/urw/ncntrsbk/
%{_texmf_main}/fonts/vf/adobe/ncntrsbk/
%{_texmf_main}/fonts/vf/urw35vf/ncntrsbk/
%{_texmf_main}/tex/latex/ncntrsbk/

%files -n texlive-palatino
%license gpl2.txt
%{_texmf_main}/dvips/palatino/
%{_texmf_main}/fonts/afm/adobe/palatino/
%{_texmf_main}/fonts/afm/urw/palatino/
%{_texmf_main}/fonts/map/dvips/palatino/
%{_texmf_main}/fonts/tfm/adobe/palatino/
%{_texmf_main}/fonts/tfm/urw35vf/palatino/
%{_texmf_main}/fonts/type1/urw/palatino/
%{_texmf_main}/fonts/vf/adobe/palatino/
%{_texmf_main}/fonts/vf/urw35vf/palatino/
%{_texmf_main}/tex/latex/palatino/

%files -n texlive-pxfonts
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/pxfonts/
%{_texmf_main}/fonts/map/dvips/pxfonts/
%{_texmf_main}/fonts/tfm/public/pxfonts/
%{_texmf_main}/fonts/type1/public/pxfonts/
%{_texmf_main}/fonts/vf/public/pxfonts/
%{_texmf_main}/tex/latex/pxfonts/
%doc %{_texmf_main}/doc/fonts/pxfonts/

%files -n texlive-rsfs
%license other-free.txt
%{_texmf_main}/fonts/afm/public/rsfs/
%{_texmf_main}/fonts/map/dvips/rsfs/
%{_texmf_main}/fonts/source/public/rsfs/
%{_texmf_main}/fonts/tfm/public/rsfs/
%{_texmf_main}/fonts/type1/public/rsfs/
%{_texmf_main}/tex/plain/rsfs/
%doc %{_texmf_main}/doc/fonts/rsfs/

%files -n texlive-symbol
%license gpl2.txt
%{_texmf_main}/dvips/symbol/
%{_texmf_main}/fonts/afm/adobe/symbol/
%{_texmf_main}/fonts/afm/urw/symbol/
%{_texmf_main}/fonts/map/dvips/symbol/
%{_texmf_main}/fonts/tfm/adobe/symbol/
%{_texmf_main}/fonts/tfm/monotype/symbol/
%{_texmf_main}/fonts/tfm/urw35vf/symbol/
%{_texmf_main}/fonts/type1/urw/symbol/
%{_texmf_main}/tex/latex/symbol/

%files -n texlive-tex-gyre
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/tex-gyre/
%{_texmf_main}/fonts/enc/dvips/tex-gyre/
%{_texmf_main}/fonts/map/dvips/tex-gyre/
%{_texmf_main}/fonts/opentype/public/tex-gyre/
%{_texmf_main}/fonts/tfm/public/tex-gyre/
%{_texmf_main}/fonts/type1/public/tex-gyre/
%{_texmf_main}/tex/latex/tex-gyre/
%doc %{_texmf_main}/doc/fonts/tex-gyre/
%{_datadir}/fonts/tex-gyre
%{_datadir}/appdata/tex-gyre.metainfo.xml

%files -n texlive-tex-gyre-math
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/tex-gyre-math/
%doc %{_texmf_main}/doc/fonts/tex-gyre-math/
%{_datadir}/fonts/tex-gyre-math
%{_datadir}/appdata/tex-gyre-math.metainfo.xml

%files -n texlive-times
%license gpl2.txt
%{_texmf_main}/dvips/times/
%{_texmf_main}/fonts/afm/adobe/times/
%{_texmf_main}/fonts/afm/urw/times/
%{_texmf_main}/fonts/map/dvips/times/
%{_texmf_main}/fonts/tfm/adobe/times/
%{_texmf_main}/fonts/tfm/urw35vf/times/
%{_texmf_main}/fonts/type1/urw/times/
%{_texmf_main}/fonts/vf/adobe/times/
%{_texmf_main}/fonts/vf/urw35vf/times/
%{_texmf_main}/tex/latex/times/

%files -n texlive-tipa
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/tipa/
%{_texmf_main}/fonts/source/public/tipa/
%{_texmf_main}/fonts/tfm/public/tipa/
%{_texmf_main}/fonts/type1/public/tipa/
%{_texmf_main}/tex/latex/tipa/
%doc %{_texmf_main}/doc/fonts/tipa/

%files -n texlive-txfonts
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/txfonts/
%{_texmf_main}/fonts/enc/dvips/txfonts/
%{_texmf_main}/fonts/map/dvips/txfonts/
%{_texmf_main}/fonts/tfm/public/txfonts/
%{_texmf_main}/fonts/type1/public/txfonts/
%{_texmf_main}/fonts/vf/public/txfonts/
%{_texmf_main}/tex/latex/txfonts/
%doc %{_texmf_main}/doc/fonts/txfonts/

%files -n texlive-utopia
%{_texmf_main}/fonts/afm/adobe/utopia/
%{_texmf_main}/fonts/tfm/adobe/utopia/
%{_texmf_main}/fonts/type1/adobe/utopia/
%{_texmf_main}/fonts/vf/adobe/utopia/
%doc %{_texmf_main}/doc/fonts/utopia/

%files -n texlive-wasy
%license pd.txt
%{_texmf_main}/fonts/source/public/wasy/
%{_texmf_main}/fonts/tfm/public/wasy/
%{_texmf_main}/tex/plain/wasy/
%doc %{_texmf_main}/doc/fonts/wasy/

%files -n texlive-wasy-type1
%license pd.txt
%{_texmf_main}/fonts/afm/public/wasy-type1/
%{_texmf_main}/fonts/map/dvips/wasy-type1/
%{_texmf_main}/fonts/type1/public/wasy-type1/
%doc %{_texmf_main}/doc/fonts/wasy-type1/

%files -n texlive-wasysym
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/wasysym/
%doc %{_texmf_main}/doc/latex/wasysym/

%files -n texlive-zapfchan
%license gpl2.txt
%{_texmf_main}/dvips/zapfchan/
%{_texmf_main}/fonts/afm/adobe/zapfchan/
%{_texmf_main}/fonts/afm/urw/zapfchan/
%{_texmf_main}/fonts/map/dvips/zapfchan/
%{_texmf_main}/fonts/tfm/adobe/zapfchan/
%{_texmf_main}/fonts/tfm/urw35vf/zapfchan/
%{_texmf_main}/fonts/type1/urw/zapfchan/
%{_texmf_main}/fonts/vf/adobe/zapfchan/
%{_texmf_main}/fonts/vf/urw35vf/zapfchan/
%{_texmf_main}/tex/latex/zapfchan/

%files -n texlive-zapfding
%license gpl2.txt
%{_texmf_main}/dvips/zapfding/
%{_texmf_main}/fonts/afm/adobe/zapfding/
%{_texmf_main}/fonts/afm/urw/zapfding/
%{_texmf_main}/fonts/map/dvips/zapfding/
%{_texmf_main}/fonts/tfm/adobe/zapfding/
%{_texmf_main}/fonts/tfm/urw35vf/zapfding/
%{_texmf_main}/fonts/type1/urw/zapfding/
%{_texmf_main}/tex/latex/zapfding/

%changelog
* Wed Feb 11 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-6
- Update lm marvosym mathpazo pxfonts tipa txfonts utopia wasysym

* Sun Feb  8 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-5
- fix licensing file

* Tue Jan 20 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-4
- fix licensing tags
- validate AppData

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-3
- fix descriptions, licensing
- update to latest components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-2
- regenerated, no deps from docs

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-1
- Update to TeX Live 2025
