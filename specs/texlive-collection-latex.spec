%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-latex
Epoch:          12
Version:        svn78733
Release:        4%{?dist}
Summary:        LaTeX fundamental packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-latex.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ae.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ae.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscls.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscls.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsmath.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsmath.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atbegshi.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atbegshi.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atveryend.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/atveryend.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auxhook.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/auxhook.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-english.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-english.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babelbib.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babelbib.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigintcalc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigintcalc.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitset.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bitset.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookmark.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bookmark.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carlisle.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/carlisle.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colortbl.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colortbl.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epstopdf-pkg.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epstopdf-pkg.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etexcmds.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etexcmds.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyhdr.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyhdr.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firstaid.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/firstaid.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fix2col.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fix2col.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geometry.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/geometry.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gettitlestring.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gettitlestring.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-cfg.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-cfg.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grfext.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grfext.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hopatch.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hopatch.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hycolor.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hycolor.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypcap.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypcap.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyperref.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyperref.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intcalc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intcalc.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvdefinekeys.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvdefinekeys.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvoptions.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvoptions.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvsetkeys.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kvsetkeys.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3backend.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3backend.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3kernel.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3kernel.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3packages.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3packages.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-fonts.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-fonts.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-lab.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-lab.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexconfig.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letltxmacro.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letltxmacro.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxcmds.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxcmds.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxmisc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uni-algos.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uni-algos.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfnfss.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfnfss.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/natbib.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/natbib.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pagesel.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pagesel.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfescape.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfescape.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmanagement.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmanagement.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftexcmds.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftexcmds.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pslatex.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psnfss.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psnfss.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pspicture.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pspicture.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/refcount.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/refcount.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rerunfilecheck.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rerunfilecheck.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stringenc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stringenc.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tagpdf.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tagpdf.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tools.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tools.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uniquecounter.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uniquecounter.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/url.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/url.doc.tar.xz

# Patches
Patch0:         tools-2026-02-10.patch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-ae
Requires:       texlive-amscls
Requires:       texlive-amsmath
Requires:       texlive-atbegshi
Requires:       texlive-atveryend
Requires:       texlive-auxhook
Requires:       texlive-babel
Requires:       texlive-babel-english
Requires:       texlive-babelbib
Requires:       texlive-bigintcalc
Requires:       texlive-bitset
Requires:       texlive-bookmark
Requires:       texlive-carlisle
Requires:       texlive-collection-basic
Requires:       texlive-colortbl
Requires:       texlive-epstopdf-pkg
Requires:       texlive-etexcmds
Requires:       texlive-etoolbox
Requires:       texlive-fancyhdr
Requires:       texlive-firstaid
Requires:       texlive-fix2col
Requires:       texlive-geometry
Requires:       texlive-gettitlestring
Requires:       texlive-graphics
Requires:       texlive-graphics-cfg
Requires:       texlive-grfext
Requires:       texlive-hopatch
Requires:       texlive-hycolor
Requires:       texlive-hypcap
Requires:       texlive-hyperref
Requires:       texlive-intcalc
Requires:       texlive-kvdefinekeys
Requires:       texlive-kvoptions
Requires:       texlive-kvsetkeys
Requires:       texlive-l3backend
Requires:       texlive-l3kernel
Requires:       texlive-l3packages
Requires:       texlive-latex
Requires:       texlive-latex-bin
Requires:       texlive-latex-fonts
Requires:       texlive-latex-lab
Requires:       texlive-latexconfig
Requires:       texlive-letltxmacro
Requires:       texlive-ltxcmds
Requires:       texlive-ltxmisc
Requires:       texlive-lua-uni-algos
Requires:       texlive-mfnfss
Requires:       texlive-mptopdf
Requires:       texlive-natbib
Requires:       texlive-oberdiek
Requires:       texlive-pagesel
Requires:       texlive-pdfescape
Requires:       texlive-pdfmanagement
Requires:       texlive-pdftexcmds
Requires:       texlive-pslatex
Requires:       texlive-psnfss
Requires:       texlive-pspicture
Requires:       texlive-refcount
Requires:       texlive-rerunfilecheck
Requires:       texlive-stringenc
Requires:       texlive-tagpdf
Requires:       texlive-tools
Requires:       texlive-uniquecounter
Requires:       texlive-url

%description
These packages are either mandated by the core LaTeX team, or very widely used
and strongly recommended in practice.


%package -n texlive-ae
Summary:        Virtual fonts for T1 encoded CMR-fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ae-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ae-doc <= 11:%{version}
Requires:       tex(fontenc.sty)

%description -n texlive-ae
A set of virtual fonts which emulates T1 coded fonts using the standard CM
fonts. The package name, AE fonts, supposedly stands for "Almost European". The
main use of the package was to produce PDF files using Adobe Type 1 versions of
the CM fonts instead of bitmapped EC fonts. Note that direct substitutes for
the bitmapped EC fonts are now available, via the CM-super, Latin Modern and
(in a restricted way) CM-LGC font sets.

%package -n texlive-amscls
Summary:        AMS document classes for LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amscls-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amscls-doc <= 11:%{version}

%description -n texlive-amscls
This bundle contains three AMS classes, amsart (for writing articles for the
AMS), amsbook (for books) and amsproc (for proceedings), together with some
supporting material. This material forms one branch of what was originally the
AMS-LaTeX distribution. The other branch, amsmath, is now maintained and
distributed separately. The user documentation can be found in the package
amscls-doc.

%package -n texlive-amsmath
Summary:        AMS mathematical facilities for LaTeX
Version:        svn78101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsmath-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsmath-doc <= 11:%{version}

%description -n texlive-amsmath
The package provides the principal packages in the AMS-LaTeX distribution. It
adapts for use in LaTeX most of the mathematical features found in AMS-TeX; it
is highly recommended as an adjunct to serious mathematical typesetting in
LaTeX. When amsmath is loaded, AMS-LaTeX packages amsbsy (for bold symbols),
amsopn (for operator names) and amstext (for text embedded in mathematics) are
also loaded. amsmath is part of the LaTeX required distribution; however,
several contributed packages add still further to its appeal; examples are
empheq, which provides functions for decorating and highlighting mathematics,
and ntheorem, for specifying theorem (and similar) definitions.

%package -n texlive-atbegshi
Summary:        Execute stuff at \shipout time
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-atbegshi
This package is a modern reimplementation of package everyshi, providing
various commands to be executed before a \shipout command. It makes use of
e-TeX's facilities if they are available. The package may be used either with
LaTeX or with plain TeX.

%package -n texlive-atveryend
Summary:        Hooks at the very end of a document
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-atveryend
This LaTeX package provides some wrapper commands around LaTeX end document
hooks.

%package -n texlive-auxhook
Summary:        Hooks for auxiliary files
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-auxhook
This package auxhook provides hooks for adding stuff at the begin of .aux
files.

%package -n texlive-babel
Summary:        Multilingual support for LaTeX, LuaLaTeX, XeLaTeX, and Plain TeX
Version:        svn78713
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-babel-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-babel-doc <= 11:%{version}
Requires:       tex(fontspec.sty)
Requires:       tex(hhline.sty)

%description -n texlive-babel
Babel is the multilingual environment for LaTeX (tailored for LuaTeX, pdfTeX
and XeTeX), and sometimes Plain. Its aim is to provide a comprehensive
localization framework for different languages, scripts and cultures based on
the latest advances on international standards (Unicode, W3C, OpenType). It
supports about 300 languages (with various levels of coverage) across about 45
scripts, including complex (like CJK, Indic) and RTL ones. Besides the
traditional .ldf files, there are many locales built on a modern core that
utilizes descriptive .ini files, with tools providing precise control over
hyphenation and line breaking, captions, date formats (across various
calendars), spacing, transliteration, numbering and other locale-specific
typographical rules.

%package -n texlive-babel-english
Summary:        Babel support for English
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-babel-english-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-babel-english-doc <= 11:%{version}
Requires:       texlive-hyphen-english

%description -n texlive-babel-english
The package provides the language definition file for support of English in
babel. Care is taken to select british hyphenation patterns for British English
and Australian text, and default ('american') patterns for Canadian and USA
text.

%package -n texlive-babelbib
Summary:        Multilingual bibliographies
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-babelbib-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-babelbib-doc <= 11:%{version}
Requires:       tex(babel.sty)

%description -n texlive-babelbib
This package enables the user to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each citation may be
written in another language, or the whole bibliography can be typeset in a
language chosen by the user. In addition, the package supports commands to
change the typography of the bibliographies.

%package -n texlive-bigintcalc
Summary:        Integer calculations on very large numbers
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pdftexcmds.sty)

%description -n texlive-bigintcalc
This package provides expandable arithmetic operations with big integers that
can exceed TeX's number limits.

%package -n texlive-bitset
Summary:        Handle bit-vector datatype
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-bigintcalc
Requires:       tex(bigintcalc.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(intcalc.sty)

%description -n texlive-bitset
This package defines and implements the data type bit set, a vector of bits.
The size of the vector may grow dynamically. Individual bits can be
manipulated.

%package -n texlive-bookmark
Summary:        A new bookmark (outline) organization for hyperref
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)

%description -n texlive-bookmark
This package implements a new bookmark (outline) organization for package
hyperref. Bookmark properties such as style and color can now be set. Other
action types are available (URI, GoToR, Named). The bookmarks are generated in
the first compile run. Package hyperref uses two runs.

%package -n texlive-carlisle
Summary:        David Carlisle's small packages
Version:        svn59577
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-carlisle-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-carlisle-doc <= 11:%{version}
Requires:       tex(color.sty)
Requires:       tex(longtable.sty)
Requires:       tex(tabularx.sty)

%description -n texlive-carlisle
Many of David Carlisle's more substantial packages stand on their own, or as
part of the LaTeX latex-tools set; this set contains: Making dotless 'j'
characters for fonts that don't have them; A method for combining the
capabilities of longtable and tabularx; An environment for including Plain TeX
in LaTeX documents; A jiffy to remove counters from other counters' reset lists
(now obsolete as it has been incorporated into the LaTeX format); A jiffy to
create 'slashed' characters for physicists.

%package -n texlive-colortbl
Summary:        Add colour to LaTeX tables
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-colortbl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-colortbl-doc <= 11:%{version}
Requires:       tex(array.sty)
Requires:       tex(color.sty)

%description -n texlive-colortbl
The package allows rows and columns to be coloured, and even individual cells.

%package -n texlive-epstopdf-pkg
Summary:        Call epstopdf "on the fly"
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf
Requires:       tex(grfext.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)

%description -n texlive-epstopdf-pkg
The package adds support for EPS files in the graphicx package when running
under pdfTeX. If an EPS graphic is detected, the package spawns a process to
convert the EPS to PDF, using the script epstopdf. This of course requires that
shell escape is enabled for the pdfTeX run.

%package -n texlive-etexcmds
Summary:        Avoid name clashes with e-TeX commands
Version:        svn78101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)

%description -n texlive-etexcmds
New primitive commands are introduced in e-TeX; sometimes the names collide
with existing macros. This package solves the name clashes by adding a prefix
to e-TeX's commands. For example, eTeX's \unexpanded is provided as
\etex@unexpanded.

%package -n texlive-etoolbox
Summary:        E-TeX tools for LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-etoolbox-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-etoolbox-doc <= 11:%{version}
Requires:       tex(etex.sty)

%description -n texlive-etoolbox
The package is a toolbox of programming facilities geared primarily towards
LaTeX class and package authors. It provides LaTeX frontends to some of the new
primitives provided by e-TeX as well as some generic tools which are not
strictly related to e-TeX but match the profile of this package. Note that the
initial versions of this package were released under the name elatex. The
package provides functions that seem to offer alternative ways of implementing
some LaTeX kernel commands; nevertheless, the package will not modify any part
of the LaTeX kernel.

%package -n texlive-fancyhdr
Summary:        Extensive control of page headers and footers in LaTeX2e
Version:        svn78348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancyhdr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancyhdr-doc <= 11:%{version}
Requires:       tex(xparse.sty)

%description -n texlive-fancyhdr
The package provides extensive facilities, both for constructing headers and
footers, and for controlling their use (for example, at times when LaTeX would
automatically change the heading style in use).

%package -n texlive-firstaid
Summary:        First aid for external LaTeX files and packages that need updating
Version:        svn76740
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-firstaid
This package contains some first aid for LaTeX packages or classes that require
updates because of internal changes to the LaTeX kernel that are not yet
reflected in the package's or class's code. The file
latex2e-first-aid-for-external-files.ltx provided by this package is meant to
be loaded during format generation and not by the user.

%package -n texlive-fix2col
Summary:        Fix miscellaneous two column mode features
Version:        svn38770
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fix2col-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fix2col-doc <= 11:%{version}

%description -n texlive-fix2col
OBSOLETE: do not use in new documents. This package will do nothing in LaTeX
formats after 2015/01/01 as the fixes that it implements were incorporated into
the fixltx2e package, which is itself obsolete as since the 2015/01/01 release
these fixes are in the LaTeX format itself. Fix mark handling so that
\firstmark is taken from the first column if that column has any marks at all;
keep two column floats like figure* in sequence with single column floats like
figure.

%package -n texlive-geometry
Summary:        Flexible and complete interface to document dimensions
Version:        svn78315
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-geometry-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-geometry-doc <= 11:%{version}
Requires:       texlive-graphics
Requires:       texlive-iftex
Requires:       tex(atbegshi.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(keyval.sty)

%description -n texlive-geometry
The package provides an easy and flexible user interface to customize page
layout, implementing auto-centering and auto-balancing mechanisms so that the
users have only to give the least description for the page layout. For example,
if you want to set each margin 2cm without header space, what you need is just
\usepackage[margin=2cm,nohead]{geometry}. The package knows about all the
standard paper sizes, so that the user need not know what the nominal 'real'
dimensions of the paper are, just its standard name (such as a4, letter, etc.).
An important feature is the package's ability to communicate the paper size
it's set up to the output (whether via DVI \specials or via direct interaction
with pdf(La)TeX).

%package -n texlive-gettitlestring
Summary:        Clean up title references
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)

%description -n texlive-gettitlestring
Cleans up the title string (removing \label commands) for packages (such as
nameref) that typeset such strings.

%package -n texlive-graphics
Summary:        The LaTeX standard graphics bundle
Version:        svn78282
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-graphics-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-graphics-doc <= 11:%{version}
Requires:       texlive-epstopdf-pkg
Requires:       texlive-graphics-cfg
Requires:       texlive-graphics-def
Requires:       tex(ifthen.sty)

%description -n texlive-graphics
This is a collection of LaTeX packages for: producing colour including graphics
(eg PostScript) files rotation and scaling of text in LaTeX documents. It
comprises the packages color, graphics, graphicx, trig, epsfig, keyval, and
lscape.

%package -n texlive-graphics-cfg
Summary:        Sample configuration files for LaTeX color and graphics
Version:        svn41448
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-graphics-cfg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-graphics-cfg-doc <= 11:%{version}

%description -n texlive-graphics-cfg
This bundle includes color.cfg and graphics.cfg files that set default "driver"
options for the color and graphics packages. It contains support for defaulting
the new LuaTeX option which was added to graphics and color in the 2016-02-01
release. The LuaTeX option is only used for LuaTeX versions from 0.87, older
versions use the pdfTeX option as before.

%package -n texlive-grfext
Summary:        Manipulate the graphics package's list of extensions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(kvdefinekeys.sty)

%description -n texlive-grfext
This package provides macros for adding to, and reordering the list of graphics
file extensions recognised by package graphics.

%package -n texlive-hopatch
Summary:        Load patches for packages
Version:        svn65491
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ltxcmds.sty)

%description -n texlive-hopatch
Hopatch provides a command with which the user may register of patch code for a
particular package. Hopatch will apply the patch immediately, if the relevant
package has already been loaded; otherwise it will store the patch until the
package appears.

%package -n texlive-hycolor
Summary:        Implements colour for packages hyperref and bookmark
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hopatch.sty)

%description -n texlive-hycolor
This package provides the code for the color option that is used by packages
hyperref and bookmark. It is not intended as package for the user.

%package -n texlive-hypcap
Summary:        Adjusting the anchors of captions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(letltxmacro.sty)

%description -n texlive-hypcap
The package offers a solution to the problem that when you link to a float
using hyperref, the link anchors to below the float's caption, rather than the
beginning of the float. Hypcap defines a separate \capstart command, which you
put where you want links to end; you should have a \capstart command for each
\caption command. Package options can be used to auto-insert a \capstart at the
start of a float environment.

%package -n texlive-hyperref
Summary:        Extensive support for hypertext in LaTeX
Version:        svn78811
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hyperref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hyperref-doc <= 11:%{version}
Requires:       texlive-atbegshi
Requires:       texlive-auxhook
Requires:       texlive-bitset
Requires:       texlive-etexcmds
Requires:       texlive-gettitlestring
Requires:       texlive-hycolor
Requires:       texlive-iftex
Requires:       texlive-infwarerr
Requires:       texlive-intcalc
Requires:       texlive-kvdefinekeys
Requires:       texlive-kvoptions
Requires:       texlive-kvsetkeys
Requires:       texlive-letltxmacro
Requires:       texlive-ltxcmds
Requires:       texlive-pdfescape
Requires:       texlive-pdftexcmds
Requires:       texlive-refcount
Requires:       texlive-rerunfilecheck
Requires:       texlive-stringenc
Requires:       texlive-url
Requires:       texlive-zapfding
Requires:       tex(bitset.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(gettitlestring.sty)
Requires:       tex(hycolor.sty)
Requires:       tex(iftex.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvdefinekeys.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(minitoc.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(pdfescape.sty)
Requires:       tex(refcount.sty)
Requires:       tex(rerunfilecheck.sty)
Requires:       tex(stringenc.sty)
Requires:       tex(url.sty)

%description -n texlive-hyperref
The hyperref package is used to handle cross-referencing commands in LaTeX to
produce hypertext links in the document. The package provides backends for the
\special set defined for HyperTeX DVI processors; for embedded pdfmark commands
for processing by Acrobat Distiller (dvips and Y&Y's dvipsone); for Y&Y's
dviwindo; for PDF control within pdfTeX and dvipdfm; for TeX4ht; and for VTeX's
pdf and HTML backends. The package is distributed with the backref and nameref
packages, which make use of the facilities of hyperref. The package depends on
the author's kvoptions, ltxcmds and refcount packages.

%package -n texlive-intcalc
Summary:        Expandable arithmetic operations with integers
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-intcalc
This package provides expandable arithmetic operations with integers, using the
e-TeX extension \numexpr if it is available.

%package -n texlive-kvdefinekeys
Summary:        Define keys for use in the kvsetkeys package
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kvdefinekeys
The package provides a macro \kv@define@key (analogous to keyval's \define@key,
to define keys for use by kvsetkeys.

%package -n texlive-kvoptions
Summary:        Key value format for package options
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etexcmds.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-kvoptions
This package offers support for package authors who want to use options in
key-value format for their package options.

%package -n texlive-kvsetkeys
Summary:        Key value parser with default handler support
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-kvsetkeys
This package provides \kvsetkeys, a variant of package keyval's \setkeys. It
allows the user to specify a handler that deals with unknown options. Active
commas and equal signs may be used (e.g. see babel's shorthands) and only one
level of curly braces are removed from the values.

%package -n texlive-l3backend
Summary:        LaTeX3 backend drivers
Version:        svn78544
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-l3backend
This package forms parts of expl3, and contains the code used to interface with
backends (drivers) across the expl3 codebase. The functions here are defined
differently depending on the engine in use. As such, these are distributed
separately from l3kernel to allow this code to be updated on an independent
schedule.

%package -n texlive-l3kernel
Summary:        LaTeX3 programming conventions
Version:        svn78545
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l3kernel-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l3kernel-doc <= 11:%{version}
Requires:       texlive-l3backend
Requires:       texlive-lua-uni-algos

%description -n texlive-l3kernel
The l3kernel bundle provides an implementation of the LaTeX3 programmers'
interface, as a set of packages that run under LaTeX2e. The interface provides
the foundation on which the LaTeX3 kernel and other future code are built: it
is an API for TeX programmers. The packages are set up so that the LaTeX3
conventions can be used with regular LaTeX2e packages.

%package -n texlive-l3packages
Summary:        High-level LaTeX3 concepts
Version:        svn76637
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l3packages-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l3packages-doc <= 11:%{version}
Requires:       texlive-l3kernel

%description -n texlive-l3packages
This collection deals with higher-level ideas such as the Designer Interface,
as part of LaTeX3 developments. The packages here have over time migrated into
the LaTeX kernel: the material here is retained to support older files. The
appropriate LaTeX kernel releases incorporating the ideas from the packages
here are l3keys2e 2022-06-01 xfp 2022-06-01 xparse 2020-10-01 xtemplate
2024-06-01

%package -n texlive-latex-fonts
Summary:        A collection of fonts used in LaTeX distributions
Version:        svn28888
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-fonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-fonts-doc <= 11:%{version}

%description -n texlive-latex-fonts
This is a collection of fonts for use with standard LaTeX packages and classes.
It includes 'invisible' fonts (for use with the slides class), line and circle
fonts (for use in the picture environment) and 'LaTeX symbol' fonts. For full
support of a LaTeX installation, some Computer Modern font variants cmbsy(6-9),
cmcsc(8,9), cmex(7-9) and cmmib(5-9) from the amsfonts distribution, are also
necessary. The fonts are available as Metafont source, and metric (tfm) files
are also provided. Most of the fonts are also available in Adobe Type 1 format,
in the amsfonts distribution.

%package -n texlive-latex-lab
Summary:        LaTeX laboratory
Version:        svn76739
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tagpdf.sty)

%description -n texlive-latex-lab
This bundle holds optional files that are loaded in certain situations by
kernel code (if available). While this code is still in development and the use
is experimental, it is stored outside the format so that there can be
intermediate releases not affecting the production use of LaTeX. Once the code
is finalized and properly tested it will eventually move to the kernel and the
corresponding file in this bundle will vanish. Note that none of these files
are directly user accessible in documents (i.e., they aren't packages), so the
process is transparent to documents already using the new functionality.

%package -n texlive-latexconfig
Summary:        Configuration files for LaTeX-related formats
Version:        svn68923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-latexconfig
configuration files for LaTeX-related formats

%package -n texlive-letltxmacro
Summary:        Let assignment for LaTeX macros
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-letltxmacro
TeX's \let assignment does not work for LaTeX macros with optional arguments or
for macros that are defined as robust macros by \DeclareRobustCommand. This
package defines \LetLtxMacro that also takes care of the involved internal
macros.

%package -n texlive-ltxcmds
Summary:        Some LaTeX kernel commands for general use
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ltxcmds
This package exports some utility macros from the LaTeX kernel into a separate
namespace and also makes them available for other formats such as plain TeX.

%package -n texlive-ltxmisc
Summary:        Miscellaneous LaTeX packages, etc.
Version:        svn75878
License:        GPL-2.0-or-later AND LPPL-1.3c AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(beton.sty)
Requires:       tex(euler.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pifont.sty)
Requires:       tex(verbatim.sty)

%description -n texlive-ltxmisc
Miscellaneous LaTeX packages, etc.

%package -n texlive-lua-uni-algos
Summary:        Unicode algorithms for LuaTeX
Version:        svn76195
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lua-uni-algos
Lua code working with Unicode data has to deal with quite some challenges. For
example there are many canonically equivalent sequences which should be treated
in the same way, and even identifying a single character becomes quite
different once you have to deal with all kinds of combining characters, emoji
sequences and syllables in different scripts. Therefore lua-uni-algos wants to
build a collection of small libraries implementing algorithms to deal with lots
of the details in Unicode, such that authors of LuaTeX packages can focus on
their actual functionality instead of having to fight against the peculiarities
of Unicode. Given that this package provides Lua modules, it is only useful in
Lua(HB)TeX. Additionally, it expects an up-to-date version of the unicode-data
package to be present. This package is intended for package authors only; no
user-level functionality provided.

%package -n texlive-mfnfss
Summary:        Packages to typeset oldgerman and pandora fonts in LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mfnfss-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mfnfss-doc <= 11:%{version}

%description -n texlive-mfnfss
This bundle contains two packages: - oldgerm, a package to typeset with old
german fonts designed by Yannis Haralambous. - pandora, a package to typeset
with Pandora fonts designed by Neena Billawala. Note that support for the
Pandora fonts is also available via the pandora-latex package.

%package -n texlive-natbib
Summary:        Flexible bibliography support
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-natbib-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-natbib-doc <= 11:%{version}
Requires:       tex(citeref.sty)

%description -n texlive-natbib
The bundle provides a package that implements both author-year and numbered
references, as well as much detailed of support for other bibliography use.
Also Provided are versions of the standard BibTeX styles that are compatible
with natbib--plainnat, unsrtnat, abbrnat. The bibliography styles produced by
custom-bib are designed from the start to be compatible with natbib.

%package -n texlive-pagesel
Summary:        Select pages of a document for output
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(everyshi.sty)

%description -n texlive-pagesel
Selects single pages, ranges of pages, odd pages or even pages for output.

%package -n texlive-pdfescape
Summary:        Implements pdfTeX's escape features using TeX or e-TeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)

%description -n texlive-pdfescape
This package implements pdfTeX's escape features (\pdfescapehex,
\pdfunescapehex, \pdfescapename, \pdfescapestring) using TeX or e-TeX.

%package -n texlive-pdfmanagement
Summary:        LaTeX PDF management bundle
Version:        svn78778
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Requires:       tex(tagpdf-base.sty)

%description -n texlive-pdfmanagement
This package is used to load LaTeX's PDF management code. The PDF management
code offers backend independent interfaces to central PDF dictionaries, tools
to create annotations, outlines, form Xobjects, form fields, to embed files,
and to handle PDF standards. The code is currently provided as independent
package. It is automatically loaded if a document uses \DocumentMetadata. It
can also be loaded as a package. At a later stage it will be integrated into
the LaTeX kernel (or in parts into permanent support packages).

%package -n texlive-pdftexcmds
Summary:        LuaTeX support for pdfTeX utility functions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-pdftexcmds
LuaTeX provides most of the commands of pdfTeX 1.40. However, a number of
utility functions are not available. This package tries to fill the gap and
implements some of the missing primitives using Lua.

%package -n texlive-pslatex
Summary:        Use PostScript fonts by default
Version:        svn67469
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pslatex
A small package that makes LaTeX default to 'standard' PostScript fonts. It is
basically a merger of the times and the (obsolete) mathptm packages from the
psnfss suite. You must have installed standard LaTeX and the psnfss PostScript
fonts to use this package. The main novel feature is that the pslatex package
tries to compensate for the visual differences between the Adobe fonts by
scaling Helvetica by 90%, and 'condensing' Courier (i.e. scaling horizontally)
by 85%. The package is supplied with a (unix) shell file for a 'pslatex'
command that allows standard LaTeX documents to be processed, without needing
to edit the file. Note that current psnfss uses a different technique for
scaling Helvetica, and treats Courier as a lost cause (there are better free
fixed-width available now, than there were when pslatex was designed). As a
result, pslatex is widely considered obsolete.

%package -n texlive-psnfss
Summary:        Font support for common PostScript fonts
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-psnfss-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-psnfss-doc <= 11:%{version}
Requires:       texlive-graphics
Requires:       texlive-symbol
Requires:       texlive-zapfding
Requires:       tex(keyval.sty)

%description -n texlive-psnfss
Font definition files, macros and font metrics for freely-available Adobe Type
1 fonts. The font set consists of the 'LaserWriter 35' set (originally 'freely
available' because embedded in PostScript printers), and a variety of other
free fonts, together with some additions. Note that while many of the fonts are
available in PostScript (and other) printers, most publishers require fonts
embedded in documents, which requires that you have the fonts in your TeX
system. Fortunately, there are free versions of the fonts from URW (available
in the URW base5 bundle). The base set of text fonts covered by PSNFSS are:
AvantGarde, Bookman, Courier, Helvetica, New Century Schoolbook, Palatino,
Symbol, Times Roman and Zapf Dingbats. In addition, the fonts Bitstream Charter
and Adobe Utopia are covered (those fonts were contributed to the Public Domain
by their commercial foundries). Separate packages are provided to load each
font for use as main text font. The packages helvet (which allows Helvetica to
be loaded with its size scaled to something more nearly appropriate for its use
as a Sans-Serif font to match Times) and pifont (which provides the means to
select single glyphs from symbol fonts) are tailored to special requirements of
their fonts. Mathematics are covered by the mathptmx package, which constructs
passable mathematics from a combination of Times Roman, Symbol and some glyphs
from Computer Modern, and by Pazo Math (optionally extended with the fpl
small-caps and old-style figures fonts) which uses Palatino as base font, with
the mathpazo fonts. The bundle as a whole is part of the LaTeX 'required' set
of packages.

%package -n texlive-pspicture
Summary:        PostScript picture support
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pspicture-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pspicture-doc <= 11:%{version}

%description -n texlive-pspicture
A replacement for LaTeX's picture macros, that uses PostScript \special
commands. The package is now largely superseded by pict2e.

%package -n texlive-refcount
Summary:        Counter operations with label references
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)

%description -n texlive-refcount
Provides commands \setcounterref and \addtocounterref which use the section (or
whatever) number from the reference as the value to put into the counter, as
in: ...\label{sec:foo} ... \setcounterref{foonum}{sec:foo} Commands
\setcounterpageref and \addtocounterpageref do the corresponding thing with the
page reference of the label. No .ins file is distributed; process the .dtx with
plain TeX to create one.

%package -n texlive-rerunfilecheck
Summary:        Checksum based rerun checks on auxiliary files
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-atveryend
Requires:       texlive-uniquecounter
Requires:       tex(infwarerr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(uniquecounter.sty)

%description -n texlive-rerunfilecheck
The package provides additional rerun warnings if some auxiliary files have
changed. It is based on MD5 checksum provided by pdfTeX, LuaTeX, XeTeX.

%package -n texlive-stringenc
Summary:        Converting a string between different encodings
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdfescape.sty)

%description -n texlive-stringenc
This package provides \StringEncodingConvert for converting a string between
different encodings. Both LaTeX and plain-TeX are supported.

%package -n texlive-tagpdf
Summary:        Code for PDF tagging using pdfLaTeX and LuaLaTeX
Version:        svn78799
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(xpatch.sty)

%description -n texlive-tagpdf
The package contains the core code for tagging and accessibility used by the
LaTeX kernel in the Tagged PDF project. See
https://github.com/latex3/tagging-project for more information.

%package -n texlive-tools
Summary:        The LaTeX standard tools bundle
Version:        svn76708
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tools-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tools-doc <= 11:%{version}
Requires:       tex(color.sty)

%description -n texlive-tools
A collection of (variously) simple tools provided as part of the LaTeX required
tools distribution, comprising the packages: afterpage, array, bm, calc,
dcolumn, delarray, enumerate, fileerr, fontsmpl, ftnright, hhline, indentfirst,
layout, longtable, multicol, rawfonts, shellesc, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%package -n texlive-uniquecounter
Summary:        Provides unlimited unique counter
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bigintcalc.sty)
Requires:       tex(infwarerr.sty)

%description -n texlive-uniquecounter
This package provides a kind of counter that provides unique number values.
Several counters can be created with different names. The numeric values are
not limited.

%package -n texlive-url
Summary:        Verbatim with URL-sensitive line breaks
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-url-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-url-doc <= 11:%{version}

%description -n texlive-url
The command \url is a form of verbatim command that allows linebreaks at
certain characters or combinations of characters, accepts reconfiguration, and
can usually be used in the argument to another command. (The \urldef command
provides robust commands that serve in cases when \url doesn't work in an
argument.) The command is intended for email addresses, hypertext links,
directories/paths, etc., which normally have no spaces, so by default the
package ignores spaces in its argument. However, a package option "allows
spaces", which is useful for operating systems where spaces are a common part
of file names.


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
tar -xf %{SOURCE80} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE81} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE82} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE83} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE84} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE85} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE86} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE87} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE88} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE89} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE90} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE91} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE92} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE93} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE94} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE95} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE96} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE97} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE98} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE99} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE100} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE101} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE102} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE103} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE104} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE105} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE106} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE107} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE108} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE109} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE110} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE111} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE112} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE113} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE114} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE115} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE116} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Apply tools patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/tools-2026-02-10.patch
popd

# Rename .map files to .oldmap to avoid updmap-sys
mv %{buildroot}%{_texmf_main}/fonts/map/dvips/psnfss/psnfss.map %{buildroot}%{_texmf_main}/fonts/map/dvips/psnfss/psnfss.oldmap

# Main collection metapackage (empty)
%files

%files -n texlive-ae
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/ae/
%{_texmf_main}/fonts/vf/public/ae/
%{_texmf_main}/tex/latex/ae/
%doc %{_texmf_main}/doc/fonts/ae/

%files -n texlive-amscls
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/amscls/
%{_texmf_main}/tex/latex/amscls/
%doc %{_texmf_main}/doc/latex/amscls/

%files -n texlive-amsmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/amsmath/
%doc %{_texmf_main}/doc/latex/amsmath/

%files -n texlive-atbegshi
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/atbegshi/
%doc %{_texmf_main}/doc/latex/atbegshi/

%files -n texlive-atveryend
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/atveryend/
%doc %{_texmf_main}/doc/latex/atveryend/

%files -n texlive-auxhook
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/auxhook/
%doc %{_texmf_main}/doc/latex/auxhook/

%files -n texlive-babel
%license lppl1.3c.txt
%{_texmf_main}/makeindex/babel/
%{_texmf_main}/tex/generic/babel/
%doc %{_texmf_main}/doc/latex/babel/

%files -n texlive-babel-english
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-english/
%doc %{_texmf_main}/doc/generic/babel-english/

%files -n texlive-babelbib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/babelbib/
%{_texmf_main}/tex/latex/babelbib/
%doc %{_texmf_main}/doc/bibtex/babelbib/

%files -n texlive-bigintcalc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bigintcalc/
%doc %{_texmf_main}/doc/latex/bigintcalc/

%files -n texlive-bitset
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bitset/
%doc %{_texmf_main}/doc/latex/bitset/

%files -n texlive-bookmark
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bookmark/
%doc %{_texmf_main}/doc/latex/bookmark/

%files -n texlive-carlisle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/carlisle/
%doc %{_texmf_main}/doc/latex/carlisle/

%files -n texlive-colortbl
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/colortbl/
%doc %{_texmf_main}/doc/latex/colortbl/

%files -n texlive-epstopdf-pkg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/epstopdf-pkg/
%doc %{_texmf_main}/doc/latex/epstopdf-pkg/

%files -n texlive-etexcmds
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/etexcmds/
%doc %{_texmf_main}/doc/latex/etexcmds/

%files -n texlive-etoolbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/etoolbox/
%doc %{_texmf_main}/doc/latex/etoolbox/

%files -n texlive-fancyhdr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fancyhdr/
%doc %{_texmf_main}/doc/latex/fancyhdr/

%files -n texlive-firstaid
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/firstaid/
%doc %{_texmf_main}/doc/latex/firstaid/

%files -n texlive-fix2col
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fix2col/
%doc %{_texmf_main}/doc/latex/fix2col/

%files -n texlive-geometry
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/geometry/
%doc %{_texmf_main}/doc/latex/geometry/

%files -n texlive-gettitlestring
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/gettitlestring/
%doc %{_texmf_main}/doc/latex/gettitlestring/

%files -n texlive-graphics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/graphics/
%doc %{_texmf_main}/doc/latex/graphics/

%files -n texlive-graphics-cfg
%license pd.txt
%{_texmf_main}/tex/latex/graphics-cfg/
%doc %{_texmf_main}/doc/latex/graphics-cfg/

%files -n texlive-grfext
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/grfext/
%doc %{_texmf_main}/doc/latex/grfext/

%files -n texlive-hopatch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hopatch/
%doc %{_texmf_main}/doc/latex/hopatch/

%files -n texlive-hycolor
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hycolor/
%doc %{_texmf_main}/doc/latex/hycolor/

%files -n texlive-hypcap
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hypcap/
%doc %{_texmf_main}/doc/latex/hypcap/

%files -n texlive-hyperref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hyperref/
%doc %{_texmf_main}/doc/latex/hyperref/

%files -n texlive-intcalc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/intcalc/
%doc %{_texmf_main}/doc/latex/intcalc/

%files -n texlive-kvdefinekeys
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/kvdefinekeys/
%doc %{_texmf_main}/doc/latex/kvdefinekeys/

%files -n texlive-kvoptions
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kvoptions/
%doc %{_texmf_main}/doc/latex/kvoptions/

%files -n texlive-kvsetkeys
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kvsetkeys/
%doc %{_texmf_main}/doc/latex/kvsetkeys/

%files -n texlive-l3backend
%license lppl1.3c.txt
%{_texmf_main}/dvips/l3backend/
%{_texmf_main}/tex/latex/l3backend/
%doc %{_texmf_main}/doc/latex/l3backend/

%files -n texlive-l3kernel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/l3kernel/
%doc %{_texmf_main}/doc/latex/l3kernel/

%files -n texlive-l3packages
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/l3packages/
%doc %{_texmf_main}/doc/latex/l3packages/

%files -n texlive-latex-fonts
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/latex-fonts/
%{_texmf_main}/fonts/tfm/public/latex-fonts/
%doc %{_texmf_main}/doc/fonts/latex-fonts/

%files -n texlive-latex-lab
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latex-lab/
%doc %{_texmf_main}/doc/latex/latex-lab/

%files -n texlive-latexconfig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latexconfig/

%files -n texlive-letltxmacro
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/letltxmacro/
%doc %{_texmf_main}/doc/latex/letltxmacro/

%files -n texlive-ltxcmds
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ltxcmds/
%doc %{_texmf_main}/doc/generic/ltxcmds/

%files -n texlive-ltxmisc
%license gpl2.txt
%license lppl1.3c.txt
%license pd.txt
%{_texmf_main}/tex/latex/ltxmisc/

%files -n texlive-lua-uni-algos
%license lppl1.3c.txt
%{_texmf_main}/tex/luatex/lua-uni-algos/
%doc %{_texmf_main}/doc/luatex/lua-uni-algos/

%files -n texlive-mfnfss
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mfnfss/
%doc %{_texmf_main}/doc/latex/mfnfss/

%files -n texlive-natbib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/natbib/
%{_texmf_main}/tex/latex/natbib/
%doc %{_texmf_main}/doc/latex/natbib/

%files -n texlive-pagesel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pagesel/
%doc %{_texmf_main}/doc/latex/pagesel/

%files -n texlive-pdfescape
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pdfescape/
%doc %{_texmf_main}/doc/latex/pdfescape/

%files -n texlive-pdfmanagement
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pdfmanagement/
%doc %{_texmf_main}/doc/latex/pdfmanagement/

%files -n texlive-pdftexcmds
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/pdftexcmds/
%doc %{_texmf_main}/doc/generic/pdftexcmds/

%files -n texlive-pslatex
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/pslatex/
%{_texmf_main}/fonts/tfm/public/pslatex/
%{_texmf_main}/fonts/vf/public/pslatex/
%{_texmf_main}/tex/latex/pslatex/

%files -n texlive-psnfss
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/psnfss/
%{_texmf_main}/tex/latex/psnfss/
%doc %{_texmf_main}/doc/latex/psnfss/

%files -n texlive-pspicture
%license lppl1.3c.txt
%{_texmf_main}/dvips/pspicture/
%{_texmf_main}/tex/latex/pspicture/
%doc %{_texmf_main}/doc/latex/pspicture/

%files -n texlive-refcount
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/refcount/
%doc %{_texmf_main}/doc/latex/refcount/

%files -n texlive-rerunfilecheck
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rerunfilecheck/
%doc %{_texmf_main}/doc/latex/rerunfilecheck/

%files -n texlive-stringenc
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/stringenc/
%doc %{_texmf_main}/doc/latex/stringenc/

%files -n texlive-tagpdf
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tagpdf/
%doc %{_texmf_main}/doc/latex/tagpdf/

%files -n texlive-tools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tools/
%doc %{_texmf_main}/doc/latex/tools/

%files -n texlive-uniquecounter
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/uniquecounter/
%doc %{_texmf_main}/doc/latex/uniquecounter/

%files -n texlive-url
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/url/
%doc %{_texmf_main}/doc/latex/url/

%changelog
* Tue Apr 28 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn78733-4
- Update collection from svn77034 to svn78733
- Add pdfmanagement
- Add tagpdf
- Update 41 components

* Mon Feb 09 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77034-3
- update latex2e tools to the latest upstream version as of 2026-02-10 (bz2437303)
  this is mostly longtable, array, and varioref
- update amscls amsmath atbegshi atveryend auxhook babel-english bigintcalc bitset
  bookmark colortbl epstopdf-pkg etoolbox fancyhdr geometry gettitlestring grfext
  hycolor hypcap hyperref intcalc kvdefinekeys kvoptions kvsetkeys letltxmacro
  ltxcmds mfnfss natbib pagesel pdfescape pdftexcmds psnfss refcount
  rerunfilecheck stringenc uniquecounter url

* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77034-2
- Update babel, hyperref
- fix licensing files

* Fri Jan 23 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77034-1
- Update to svn77034
- fix licensing tags
- update components to latest

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73720-2
- regen, no deps from docs

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73720-1
- Update to TeX Live 2025