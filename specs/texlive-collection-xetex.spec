%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-xetex
Epoch:          12
Version:        svn71515
Release:        3%{?dist}
Summary:        XeTeX and packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-xetex.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabxetex.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arabxetex.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi-atbegshi.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidi-atbegshi.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidicontour.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidicontour.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipagegrid.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipagegrid.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipresentation.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidipresentation.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidishadowtext.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bidishadowtext.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/businesscard-qrcode.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/businesscard-qrcode.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cqubeamer.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cqubeamer.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixlatvian.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixlatvian.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/font-change-xetex.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/font-change-xetex.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontbook.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontbook.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontwrap.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontwrap.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interchar.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interchar.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/na-position.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/na-position.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/philokalia.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/philokalia.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptext.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptext.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realscripts.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realscripts.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-resume-cv.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-resume-cv.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-thesis-dissertation.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simple-thesis-dissertation.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tetragonos.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tetragonos.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharclasses.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharclasses.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-bidi.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-bidi.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unimath-plain-xetex.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unimath-plain-xetex.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unisugar.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unisugar.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xebaposter.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xebaposter.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xechangebar.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xechangebar.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecolor.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecolor.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyr.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecyr.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xeindex.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xeindex.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xesearch.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xesearch.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xespotcolor.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xespotcolor.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-itrans.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-itrans.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-pstricks.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-pstricks.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-tibetan.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-tibetan.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexconfig.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexfontinfo.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexfontinfo.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexko.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexko.doc.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xevlna.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xevlna.doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zbmath-review-template.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zbmath-review-template.doc.tar.xz

# AppStream metadata for font components
Source79:        philokalia.metainfo.xml
BuildRequires:  texlive-base
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-arabxetex
Requires:       texlive-bidi-atbegshi
Requires:       texlive-bidicontour
Requires:       texlive-bidipagegrid
Requires:       texlive-bidipresentation
Requires:       texlive-bidishadowtext
Requires:       texlive-businesscard-qrcode
Requires:       texlive-collection-basic
Requires:       texlive-cqubeamer
Requires:       texlive-fixlatvian
Requires:       texlive-font-change-xetex
Requires:       texlive-fontbook
Requires:       texlive-fontwrap
Requires:       texlive-interchar
Requires:       texlive-na-position
Requires:       texlive-philokalia
Requires:       texlive-ptext
Requires:       texlive-realscripts
Requires:       texlive-simple-resume-cv
Requires:       texlive-simple-thesis-dissertation
Requires:       texlive-tetragonos
Requires:       texlive-ucharclasses
Requires:       texlive-unicode-bidi
Requires:       texlive-unimath-plain-xetex
Requires:       texlive-unisugar
Requires:       texlive-xebaposter
Requires:       texlive-xechangebar
Requires:       texlive-xecolor
Requires:       texlive-xecyr
Requires:       texlive-xeindex
Requires:       texlive-xelatex-dev
Requires:       texlive-xesearch
Requires:       texlive-xespotcolor
Requires:       texlive-xetex
Requires:       texlive-xetex-itrans
Requires:       texlive-xetex-pstricks
Requires:       texlive-xetex-tibetan
Requires:       texlive-xetexconfig
Requires:       texlive-xetexfontinfo
Requires:       texlive-xetexko
Requires:       texlive-xevlna
Requires:       texlive-zbmath-review-template

%description
Packages for XeTeX, the Unicode/OpenType-enabled TeX by Jonathan Kew. See
https://tug.org/xetex.


%package -n texlive-arabxetex
Summary:        An ArabTeX-like interface for XeLaTeX
Version:        svn38299
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(bidi.sty)
Requires:       tex(fontspec.sty)
Provides:       tex(arabxetex.sty) = %{tl_version}

%description -n texlive-arabxetex
ArabXeTeX provides a convenient ArabTeX-like user-interface for typesetting
languages using the Arabic script in XeLaTeX, with flexible access to font
features. Input in ArabTeX notation can be set in three different vocalization
modes or in roman transliteration. Direct UTF-8 input is also supported. The
parsing and converting of ArabTeX input to Unicode is done by means of TECkit
mappings. Version 1.0 provides support for Arabic, Maghribi Arabic, Farsi
(Persian), Urdu, Sindhi, Kashmiri, Ottoman Turkish, Kurdish, Jawi (Malay) and
Uighur. The documentation covers topics such as typesetting the Holy Quran and
typesetting bidirectional critical editions with the package ednotes.

%package -n texlive-bidi-atbegshi
Summary:        Bidi-aware shipout macros
Version:        svn62009
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi-ltx.sty)
Provides:       tex(bidi-atbegshi.sty) = %{tl_version}

%description -n texlive-bidi-atbegshi
The package adds some commands to the atbegshi package for proper placement of
background material in the left and right corners of the output page, in both
LTR and RTL modes. The package only works with xelatex format and should be
loaded before the bidi package.

%package -n texlive-bidicontour
Summary:        Bidi-aware coloured contour around text
Version:        svn34631
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(trig.sty)
Provides:       tex(bidicontour.sty) = %{tl_version}

%description -n texlive-bidicontour
The package is a re-implementation of the contour package, making it
bidi-aware, and adding support of the xdvipdfmx (when the outline option of the
package is used).

%package -n texlive-bidipagegrid
Summary:        Bidi-aware page grid in background
Version:        svn34632
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
Provides:       tex(bidipagegrid.sty) = %{tl_version}

%description -n texlive-bidipagegrid
The package is based on pagegrid.

%package -n texlive-bidipresentation
Summary:        Experimental bidi presentation
Version:        svn35267
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bidipresentation
A great portion of the code is borrowed from the texpower bundle, with
modifications to get things working properly in both right to left and left to
right modes.

%package -n texlive-bidishadowtext
Summary:        Bidi-aware shadow text
Version:        svn34633
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(bidishadowtext.sty) = %{tl_version}

%description -n texlive-bidishadowtext
This package allows you to typeset bidi-aware shadow text. It is a
re-implementation of the shadowtext package adding bidi support.

%package -n texlive-businesscard-qrcode
Summary:        Business cards with QR-Code
Version:        svn76924
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-businesscard-qrcode
What happens when you give your visiting card to someone? Either they manually
type the text into their computer or mobile phone, or it will end up in a box
and be forgotten. Nowadays data is required electronically, not on paper. Here
is the solution: A visiting card with QR-Code that contains a full vcard so
that it can be scanned with an app on the mobile phone and thereby
automatically imported into the electronic contacts. This also works well when
you are offline and bluetooth transfer fails. So here is the highly
configurable business card or visiting card with full vcard as QR-Code, ready
to send to online printers. You can specify the exact size of the paper and the
content within the paper, including generation of crop marks. The package
depends on the following other LaTeX packages: calc, crop, DejaVuSans,
etoolbox, fontawesome, fontenc, geometry, kvoptions, marvosym, qrcode,
varwidth, and wrapfig. The package needs XeLaTeX for working properly.

%package -n texlive-cqubeamer
Summary:        LaTeX Beamer Template for Chongqing University
Version:        svn54512
License:        MIT AND CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bookmark.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(perpage.sty)
Provides:       tex(cqubeamer.sty) = %{tl_version}

%description -n texlive-cqubeamer
This package provides a LaTeX beamer template designed for researchers of
Chongqing University. It can be used for academic reports, conferences, or
thesis defense, and can be helpful for delivering a speech. It should be used
with the XeTeX engine.

%package -n texlive-fixlatvian
Summary:        Improve Latvian language support in XeLaTeX
Version:        svn21631
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(caption.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(icomma.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(perpage.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(svn-prov.sty)
Requires:       tex(xstring.sty)
Provides:       tex(fixlatvian.sty) = %{tl_version}

%description -n texlive-fixlatvian
The package offers improvement of the Latvian language support in polyglossia,
in particular in the area of the standard classes.

%package -n texlive-font-change-xetex
Summary:        Macros to change text and mathematics fonts in plain XeTeX
Version:        svn40404
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(font-change-xetex.tex) = %{tl_version}

%description -n texlive-font-change-xetex
This package consists of macros that can be used to typeset "plain" XeTeX
documents using any OpenType or TrueType font installed on the computer system.
The macros allow the user to change the text mode fonts and some math mode
fonts. For any declared font family, various font style, weight, and size
variants like bold, italics, small caps, etc., are available through standard
and custom TeX control statements. Using the optional argument of the macros,
the available XeTeX font features and OpenType tags can be accessed. Other
features of the package include activating and deactivating hanging
punctuation, and support for special Unicode characters.

%package -n texlive-fontbook
Summary:        Generate a font book
Version:        svn23608
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(fontbook.sty) = %{tl_version}

%description -n texlive-fontbook
The package provides a means of producing a 'book' of font samples (for
evaluation, etc.).

%package -n texlive-fontwrap
Summary:        Bind fonts to specific unicode blocks
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(perltex.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(fontwrap.sty) = %{tl_version}

%description -n texlive-fontwrap
The package (which runs under XeLaTeX) lets you bind fonts to specific unicode
blocks, for automatic font tagging of multilingual text. The package uses Perl
(via perltex) to construct its tables.

%package -n texlive-interchar
Summary:        Managing character class schemes in XeTeX
Version:        svn36312
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(interchar.sty) = %{tl_version}

%description -n texlive-interchar
The package manages character class schemes of XeTeX. Using this package, you
may switch among different character class schemes. Migration commands are
provided for make packages using this mechanism compatible with each others.

%package -n texlive-na-position
Summary:        Tables of relative positions of curves and asymptotes or tangents in Arabic documents
Version:        svn55559
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tkz-tab.sty)
Provides:       tex(na-position.sty) = %{tl_version}

%description -n texlive-na-position
This package facilitates, in most cases, the creation of tables of relative
positions of a curve and its asymptote, or a curve and a tangent in one of its
points. It depends on tkz-tab and listofitems, as well as amsmath, amsfonts,
mathrsfs, and amssymb. This package has to be used with polyglossia and XeLaTeX
to produce documents in Arabic.

%package -n texlive-philokalia
Summary:        A font to typeset the Philokalia Books
Version:        svn45356
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(lettrine.sty)
Requires:       tex(xltxtra.sty)
Provides:       tex(philokalia.sty) = %{tl_version}

%description -n texlive-philokalia
The philokalia package has been designed to ease the use of the
Philokalia-Regular OpenType font with XeLaTeX. The font started as a project to
digitize the typeface used to typeset the Philokalia books.

%package -n texlive-ptext
Summary:        A 'lipsum' for Persian
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Provides:       tex(ptext.sty) = %{tl_version}

%description -n texlive-ptext
The package provides lipsum-like facilities for the Persian language. The
source of the filling text is the Persian epic "the Shanameh" (100 paragraphs
are used.) The package needs to be run under XeLaTeX.

%package -n texlive-realscripts
Summary:        Access OpenType subscript and superscript glyphs
Version:        svn56594
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(realscripts.sty) = %{tl_version}

%description -n texlive-realscripts
This small package replaces \textsuperscript and \textsubscript commands by
equivalent commands that use OpenType font features to access appropriate
glyphs if possible. The package also patches LaTeX's default footnote command
to use this new \textsuperscript for footnote symbols. The package requires
fontspec running on either XeLaTeX or LuaLaTeX. The package holds functions
that were once parts of the xltxtra package, which now loads realscripts by
default.

%package -n texlive-simple-resume-cv
Summary:        Template for a simple resume or curriculum vitae (CV), in XeLaTeX
Version:        svn43057
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-simple-resume-cv
Template for a simple resume or curriculum vitae (CV), in XeLaTeX. Simple
template that can be further customized or extended, with numerous examples.

%package -n texlive-simple-thesis-dissertation
Summary:        Template for a simple thesis or dissertation (Ph.D. or master's degree) or technical report, in XeLaTeX
Version:        svn43058
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-simple-thesis-dissertation
Template for a simple thesis or dissertation (Ph.D. or master's degree) or
technical report, in XeLaTeX. Simple template that can be further customized or
extended, with numerous examples. Consistent style for figures, tables,
mathematical theorems, definitions, lemmas, etc.

%package -n texlive-tetragonos
Summary:        Four-Corner codes of Chinese characters
Version:        svn49732
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tetragonos-database.def) = %{tl_version}
Provides:       tex(tetragonos.sty) = %{tl_version}

%description -n texlive-tetragonos
This is a XeLaTeX package for mapping Chinese characters to their codes in the
Four-Corner Method.

%package -n texlive-ucharclasses
Summary:        Font actions in XeTeX according to what is being processed
Version:        svn64782
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifxetex.sty)
Provides:       tex(ucharclasses.sty) = %{tl_version}

%description -n texlive-ucharclasses
The package takes care of switching fonts when you switch from one Unicode
block to another in the text of a document. This way, you can write a document
with no explicit font selection, but a series of rules of the form "when
entering block ..., switch font to use ...".

%package -n texlive-unicode-bidi
Summary:        Experimental unicode bidi package for XeTeX
Version:        svn42482
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(unicode-bidi.sty) = %{tl_version}

%description -n texlive-unicode-bidi
The experimental unicode-bidi package allows to mix non-RTL script with RTL
script without any markup.

%package -n texlive-unimath-plain-xetex
Summary:        OpenType math support in (plain) XeTeX
Version:        svn72498
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(unimath-plain-xetex.tex) = %{tl_version}

%description -n texlive-unimath-plain-xetex
This package provides OpenType math font support in plain TeX format. It only
works with the XeTeX engine.

%package -n texlive-unisugar
Summary:        Define syntactic sugar for Unicode LaTeX
Version:        svn22357
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifxetex.sty)
Provides:       tex(unisugar.sty) = %{tl_version}

%description -n texlive-unisugar
The package allows the user to define shorthand aliases for single Unicode
characters, and also provides support for such aliases in RTL-text. The package
requires an TeX-alike system that uses Unicode input in a native way: current
examples are XeTeX and LuaTeX.

%package -n texlive-xebaposter
Summary:        Create beautiful scientific Persian/Latin posters using TikZ
Version:        svn75290
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xebaposter
This package is designed for making beautiful scientific Persian/Latin posters.
It is a fork of baposter by Brian Amberg and Reinhold Kainhofer available at
LaTeX Poster Template. baposter's users should be able to compile their poster
using xebaposter (instead of baposter) without any problem.

%package -n texlive-xechangebar
Summary:        An extension of package changebar that can be used with XeLaTeX
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xechangebar.sty) = %{tl_version}

%description -n texlive-xechangebar
The package extends package changebar so it can be used with XeLaTeX. It
introduces the new option xetex for use with XeLaTeX. Everything else remains
the same and users should consult the original documentation for usage
information.

%package -n texlive-xecolor
Summary:        Support for color in XeLaTeX
Version:        svn29660
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Provides:       tex(xecolor.sty) = %{tl_version}

%description -n texlive-xecolor
This is a simple package which defines about 140 different colours using
XeTeX's colour feature. The colours can be used in bidirectional texts without
any problem.

%package -n texlive-xecyr
Summary:        Using Cyrillic languages in XeTeX
Version:        svn54308
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(luatextra.sty)
Requires:       tex(misccorr.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(xecyr.sty) = %{tl_version}

%description -n texlive-xecyr
Helper tools for using Cyrillic languages with XeLaTeX and babel.

%package -n texlive-xeindex
Summary:        Automatic index generation for XeLaTeX
Version:        svn35756
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(makeidx.sty)
Requires:       tex(xesearch.sty)
Provides:       tex(xeindex.sty) = %{tl_version}

%description -n texlive-xeindex
The package is based on XeSearch, and will automatically index words or phrases
in an XeLaTeX document. Words are declared in a list, and every occurrence then
creates an index entry whose content can be fully specified beforehand.

%package -n texlive-xesearch
Summary:        A string finder for XeTeX
Version:        svn51908
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(t-xesearch.tex) = %{tl_version}
Provides:       tex(xesearch.sty) = %{tl_version}

%description -n texlive-xesearch
The package finds strings (e.g. (parts of) words or phrases) and manipulates
them (apply any macro), thus turning each word or phrase into a possible
command. It is written in plain XeTeX and should thus work with any format (it
is known to work with LaTeX and ConTeXt). The main application for the moment
is XeIndex, an automatic index for XeLaTeX, but examples are given of simple
use to check spelling, count words, and highlight syntax of programming
languages.

%package -n texlive-xespotcolor
Summary:        Spot colours support for XeLaTeX
Version:        svn58212
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphics.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(xespotcolor.sty) = %{tl_version}

%description -n texlive-xespotcolor
The package provides macros for using spot colours in LaTeX documents. The
package is a reimplementation of the spotcolor package for use with XeLaTeX. As
such, it has the same user interface and the same capabilities.

%package -n texlive-xetex-itrans
Summary:        Itrans input maps for use with XeLaTeX
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetex-itrans
The package provides maps for use with XeLaTeX with coding done using itrans.
Fontspec maps are provided for Devanagari (Sanskrit), for Sanskrit in Kannada
and for Kannada itself.

%package -n texlive-xetex-pstricks
Summary:        Running PSTricks under XeTeX
Version:        svn17055
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetex-pstricks
The package provides an indirection scheme for XeTeX to use the pstricks
xdvipdfmx.cfg configuration file, so that XeTeX documents will load it in
preference to the standard pstricks.con configuration file. With this
configuration, many PSTricks features can be used in XeLaTeX or plain XeTeX
documents.

%package -n texlive-xetex-tibetan
Summary:        XeTeX input maps for Unicode Tibetan
Version:        svn28847
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetex-tibetan
The package provides a map for use with Jonathan Kew's TECkit, to translate
Tibetan to Unicode (range 0F00-0FFF).

%package -n texlive-xetexconfig
Summary:        Crop.cfg for XeLaTeX
Version:        svn45845
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetexconfig
crop.cfg for XeLaTeX

%package -n texlive-xetexfontinfo
Summary:        Report font features in XeTeX
Version:        svn15878
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(aat-info.tex) = %{tl_version}
Provides:       tex(opentype-info.tex) = %{tl_version}

%description -n texlive-xetexfontinfo
A pair of documents to reveal the font features supported by fonts usable in
XeTeX. Use OpenType-info.tex for OpenType fonts, and AAT-info.tex for AAT fonts
(Mac OS X only).

%package -n texlive-xetexko
Summary:        Typeset Korean with Xe(La)TeX
Version:        svn76133
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(kolabels-utf.sty)
Provides:       tex(xetexko-font.sty) = %{tl_version}
Provides:       tex(xetexko-hanging.sty) = %{tl_version}
Provides:       tex(xetexko-josa.sty) = %{tl_version}
Provides:       tex(xetexko-space.sty) = %{tl_version}
Provides:       tex(xetexko-vertical.sty) = %{tl_version}
Provides:       tex(xetexko.sty) = %{tl_version}

%description -n texlive-xetexko
The package supports typesetting Korean documents (including old Hangul texts),
using XeTeX. It enhances the existing support, in XeTeX, providing features
that provide quality typesetting. This package requires the cjk-ko package for
its full functionality.

%package -n texlive-xevlna
Summary:        Insert non-breakable spaces using XeTeX
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xevlna.sty) = %{tl_version}

%description -n texlive-xevlna
The package will directly insert nonbreakable spaces (in Czech, vlna or vlnka),
after nonsyllabic prepositions and single letter conjunctions, while the
document is being typeset. (The macros recognised maths and verbatim by TeX
means.) (Inserting nonbreakable spaces by a preprocessor will probably never be
fully reliable, because user defined macros and environments cannot reliably be
recognised.) The package works both with (Plain) XeTeX and with XeLaTeX.

%package -n texlive-zbmath-review-template
Summary:        Template for a zbMATH Open review
Version:        svn59693
License:        GPL-3.0-only AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(gensymb.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz-cd.sty)
Provides:       tex(zb-basics.sty) = %{tl_version}

%description -n texlive-zbmath-review-template
This package contains a template for zbMATH Open reviews. It will show what
your review will look like on zbMATH Open and you can test whether your
LaTeX-Code will compile on our system. The template has to be compiled using
XeLaTeX and relies on scrartcl, scrlayer-scrpage, amsfonts, amssymb, amsmath,
babel, enumitem, etoolbox, fontspec, gensymb, geometry, graphicx, mathrsfs,
mathtools, stmaryrd, textcomp, tikz-cd, xcolor, and xparse.


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

# Install AppStream metadata for font components
cp %{SOURCE79} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/philokalia %{buildroot}%{_datadir}/fonts/philokalia

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-arabxetex
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xelatex/arabxetex/
%doc %{_texmf_main}/doc/xelatex/arabxetex/

%files -n texlive-bidi-atbegshi
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidi-atbegshi/
%doc %{_texmf_main}/doc/xelatex/bidi-atbegshi/

%files -n texlive-bidicontour
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidicontour/
%doc %{_texmf_main}/doc/xelatex/bidicontour/

%files -n texlive-bidipagegrid
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidipagegrid/
%doc %{_texmf_main}/doc/xelatex/bidipagegrid/

%files -n texlive-bidipresentation
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidipresentation/
%doc %{_texmf_main}/doc/xelatex/bidipresentation/

%files -n texlive-bidishadowtext
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/bidishadowtext/
%doc %{_texmf_main}/doc/xelatex/bidishadowtext/

%files -n texlive-businesscard-qrcode
%license lgpl2.1.txt
%{_texmf_main}/tex/xelatex/businesscard-qrcode/
%doc %{_texmf_main}/doc/xelatex/businesscard-qrcode/

%files -n texlive-cqubeamer
%license mit.txt
%license cc-by-4.txt
%{_texmf_main}/tex/xelatex/cqubeamer/
%doc %{_texmf_main}/doc/xelatex/cqubeamer/

%files -n texlive-fixlatvian
%license lppl1.3c.txt
%{_texmf_main}/makeindex/fixlatvian/
%{_texmf_main}/tex/xelatex/fixlatvian/
%doc %{_texmf_main}/doc/xelatex/fixlatvian/

%files -n texlive-font-change-xetex
%license cc-by-sa-4.txt
%{_texmf_main}/tex/xetex/font-change-xetex/
%doc %{_texmf_main}/doc/xetex/font-change-xetex/

%files -n texlive-fontbook
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/fontbook/
%doc %{_texmf_main}/doc/xelatex/fontbook/

%files -n texlive-fontwrap
%license gpl2.txt
%{_texmf_main}/tex/xelatex/fontwrap/
%doc %{_texmf_main}/doc/xelatex/fontwrap/

%files -n texlive-interchar
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/interchar/
%doc %{_texmf_main}/doc/xelatex/interchar/

%files -n texlive-na-position
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/na-position/
%doc %{_texmf_main}/doc/xelatex/na-position/

%files -n texlive-philokalia
%license lppl1.3c.txt
%{_texmf_main}/fonts/opentype/public/philokalia/
%{_texmf_main}/tex/xelatex/philokalia/
%doc %{_texmf_main}/doc/xelatex/philokalia/
%{_datadir}/fonts/philokalia
%{_datadir}/appdata/philokalia.metainfo.xml

%files -n texlive-ptext
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/ptext/
%doc %{_texmf_main}/doc/xelatex/ptext/

%files -n texlive-realscripts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/realscripts/
%doc %{_texmf_main}/doc/latex/realscripts/

%files -n texlive-simple-resume-cv
%license pd.txt
%{_texmf_main}/tex/xelatex/simple-resume-cv/
%doc %{_texmf_main}/doc/xelatex/simple-resume-cv/

%files -n texlive-simple-thesis-dissertation
%license pd.txt
%{_texmf_main}/tex/xelatex/simple-thesis-dissertation/
%doc %{_texmf_main}/doc/xelatex/simple-thesis-dissertation/

%files -n texlive-tetragonos
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/tetragonos/
%doc %{_texmf_main}/doc/xelatex/tetragonos/

%files -n texlive-ucharclasses
%license pd.txt
%{_texmf_main}/tex/xelatex/ucharclasses/
%doc %{_texmf_main}/doc/xelatex/ucharclasses/

%files -n texlive-unicode-bidi
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/unicode-bidi/
%doc %{_texmf_main}/doc/xelatex/unicode-bidi/

%files -n texlive-unimath-plain-xetex
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xetex/unimath-plain-xetex/
%doc %{_texmf_main}/doc/xetex/unimath-plain-xetex/

%files -n texlive-unisugar
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/unisugar/
%doc %{_texmf_main}/doc/xelatex/unisugar/

%files -n texlive-xebaposter
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xebaposter/
%doc %{_texmf_main}/doc/latex/xebaposter/

%files -n texlive-xechangebar
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xechangebar/
%doc %{_texmf_main}/doc/xelatex/xechangebar/

%files -n texlive-xecolor
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xecolor/
%doc %{_texmf_main}/doc/xelatex/xecolor/

%files -n texlive-xecyr
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xecyr/
%doc %{_texmf_main}/doc/xelatex/xecyr/

%files -n texlive-xeindex
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xeindex/
%doc %{_texmf_main}/doc/xelatex/xeindex/

%files -n texlive-xesearch
%license lppl1.3c.txt
%{_texmf_main}/tex/xetex/xesearch/
%doc %{_texmf_main}/doc/xetex/xesearch/

%files -n texlive-xespotcolor
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xespotcolor/
%doc %{_texmf_main}/doc/xelatex/xespotcolor/

%files -n texlive-xetex-itrans
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xelatex/xetex-itrans/

%files -n texlive-xetex-pstricks
%license pd.txt
%{_texmf_main}/tex/xelatex/xetex-pstricks/
%{_texmf_main}/tex/xetex/xetex-pstricks/
%doc %{_texmf_main}/doc/xetex/xetex-pstricks/

%files -n texlive-xetex-tibetan
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xetex/xetex-tibetan/

%files -n texlive-xetexconfig
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xetexconfig/

%files -n texlive-xetexfontinfo
%license apache2.txt
%{_texmf_main}/tex/xetex/xetexfontinfo/
%doc %{_texmf_main}/doc/xetex/xetexfontinfo/

%files -n texlive-xetexko
%license lppl1.3c.txt
%{_texmf_main}/tex/xetex/xetexko/
%doc %{_texmf_main}/doc/xetex/xetexko/

%files -n texlive-xevlna
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xevlna/
%doc %{_texmf_main}/doc/xelatex/xevlna/

%files -n texlive-zbmath-review-template
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/tex/xelatex/zbmath-review-template/
%doc %{_texmf_main}/doc/xelatex/zbmath-review-template/

%changelog
* Wed Feb 04 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn71515-3
- fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn71515-2
- regen, no deps from docs

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn71515-1
- Update to TeX Live 2025
