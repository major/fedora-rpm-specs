%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-latexrecommended
Epoch:          12
Version:        svn78568
Release:        3%{?dist}
Summary:        LaTeX recommended packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-latexrecommended.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anysize.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/anysize.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/booktabs.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/booktabs.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/breqn.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/breqn.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/caption.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/caption.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cite.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cite.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmap.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmap.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crop.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crop.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctable.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctable.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eso-pic.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eso-pic.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euenc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euenc.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euler.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/euler.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/everysel.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/everysel.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/everyshi.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/everyshi.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/extsizes.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/extsizes.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancybox.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancybox.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyref.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyref.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyvrb.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyvrb.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/filehook.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/filehook.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/float.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/float.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontspec.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontspec.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footnotehyper.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footnotehyper.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fp.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fp.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grffile.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/grffile.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hologo.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hologo.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/index.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/index.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/infwarerr.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/infwarerr.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jknapltx.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jknapltx.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/koma-script.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3experimental.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3experimental.doc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexbug.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexbug.doc.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lineno.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lineno.doc.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listings.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listings.doc.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltx-talk.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltx-talk.doc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-unicode-math.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-unicode-math.doc.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathspec.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathspec.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathtools.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathtools.doc.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mdwtools.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mdwtools.doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memoir.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memoir.doc.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metalogo.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metalogo.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/microtype.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/microtype.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newfloat.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/newfloat.doc.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntgclass.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntgclass.doc.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parskip.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parskip.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcolfoot.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcolfoot.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdflscape.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdflscape.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfpages.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfpages.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyglossia.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyglossia.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psfrag.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psfrag.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ragged2e.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ragged2e.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rcs.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rcs.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmath.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmath.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/section.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/section.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seminar.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seminar.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sepnum.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sepnum.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/setspace.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/setspace.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subfig.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subfig.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textcase.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textcase.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translator.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translator.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typehtml.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typehtml.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharcat.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharcat.doc.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/underscore.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/underscore.doc.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-math.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-math.doc.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcolor.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcolor.doc.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xfrac.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xfrac.doc.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xkeyval.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xkeyval.doc.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xltxtra.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xltxtra.doc.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xunicode.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xunicode.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-anysize
Requires:       texlive-attachfile2
Requires:       texlive-beamer
Requires:       texlive-booktabs
Requires:       texlive-breqn
Requires:       texlive-caption
Requires:       texlive-cite
Requires:       texlive-cmap
Requires:       texlive-collection-latex
Requires:       texlive-crop
Requires:       texlive-ctable
Requires:       texlive-eso-pic
Requires:       texlive-euenc
Requires:       texlive-euler
Requires:       texlive-everysel
Requires:       texlive-everyshi
Requires:       texlive-extsizes
Requires:       texlive-fancybox
Requires:       texlive-fancyref
Requires:       texlive-fancyvrb
Requires:       texlive-filehook
Requires:       texlive-float
Requires:       texlive-fontspec
Requires:       texlive-footnotehyper
Requires:       texlive-fp
Requires:       texlive-grffile
Requires:       texlive-hologo
Requires:       texlive-index
Requires:       texlive-infwarerr
Requires:       texlive-jknapltx
Requires:       texlive-koma-script
Requires:       texlive-l3experimental
Requires:       texlive-latexbug
Requires:       texlive-lineno
Requires:       texlive-listings
Requires:       texlive-ltx-talk
Requires:       texlive-lua-unicode-math
Requires:       texlive-lwarp
Requires:       texlive-mathspec
Requires:       texlive-mathtools
Requires:       texlive-mdwtools
Requires:       texlive-memoir
Requires:       texlive-metalogo
Requires:       texlive-microtype
Requires:       texlive-newfloat
Requires:       texlive-ntgclass
Requires:       texlive-parskip
Requires:       texlive-pdfcolfoot
Requires:       texlive-pdflscape
Requires:       texlive-pdfpages
Requires:       texlive-polyglossia
Requires:       texlive-psfrag
Requires:       texlive-ragged2e
Requires:       texlive-rcs
Requires:       texlive-sansmath
Requires:       texlive-section
Requires:       texlive-seminar
Requires:       texlive-sepnum
Requires:       texlive-setspace
Requires:       texlive-subfig
Requires:       texlive-textcase
Requires:       texlive-thumbpdf
Requires:       texlive-translator
Requires:       texlive-typehtml
Requires:       texlive-ucharcat
Requires:       texlive-underscore
Requires:       texlive-unicode-math
Requires:       texlive-xcolor
Requires:       texlive-xfrac
Requires:       texlive-xkeyval
Requires:       texlive-xltxtra
Requires:       texlive-xunicode
Provides:       tex(latex) = %{tl_version}
Provides:       texlive-latex = %{tl_version}

%description
A collection of recommended add-on packages for LaTeX which have widespread
use.


%package -n texlive-anysize
Summary:        A simple package to set up document margins
Version:        svn77682
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-anysize-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-anysize-doc <= 11:%{version}

%description -n texlive-anysize
This package is considered obsolete; alternatives are the typearea package from
the koma-script bundle, or the geometry package.

%package -n texlive-beamer
Summary:        A LaTeX class for producing presentations and slides
Version:        svn78101
License:        LPPL-1.3c AND GPL-2.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-beamer-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-beamer-doc <= 11:%{version}
Requires:       texlive-amscls
Requires:       texlive-amsfonts
Requires:       texlive-amsmath
Requires:       texlive-atbegshi
Requires:       texlive-etoolbox
Requires:       texlive-geometry
Requires:       texlive-hyperref
Requires:       texlive-iftex
Requires:       texlive-pgf
Requires:       texlive-translator
Requires:       texlive-xcolor
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfpages.sty)
Requires:       tex(sansmathaccent.sty)
Requires:       tex(translator.sty)
Requires:       tex(xcolor.sty)

%description -n texlive-beamer
The beamer LaTeX class can be used for producing slides. The class works in
both PostScript and direct PDF output modes, using the pgf graphics system for
visual effects. Content is created in the frame environment, and each frame can
be made up of a number of slides using a simple notation for specifying
material to appear on each slide within a frame. Short versions of title,
authors, institute can also be specified as optional parameters. Whole frame
graphics are supported by plain frames. The class supports figure and table
environments, transparency effects, varying slide transitions and animations.
Beamer also provides compatibility with other packages like prosper. The
package now incorporates the functionality of the former translator package,
which is used for customising the package for use in other language
environments. Beamer depends on the following other packages: atbegshi,
etoolbox, hyperref, ifpdf, pgf, and translator.

%package -n texlive-booktabs
Summary:        Publication quality tables in LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-booktabs-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-booktabs-doc <= 11:%{version}

%description -n texlive-booktabs
The package enhances the quality of tables in LaTeX, providing extra commands
as well as behind-the-scenes optimisation. Guidelines are given as to what
constitutes a good table in this context. From version 1.61, the package offers
longtable compatibility.

%package -n texlive-breqn
Summary:        Automatic line breaking of displayed equations
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-breqn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-breqn-doc <= 11:%{version}
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)

%description -n texlive-breqn
The package provides solutions to a number of common difficulties in writing
displayed equations and getting high-quality output. For example, it is a
well-known inconvenience that if an equation must be broken into more than one
line, 'left...right' constructs cannot span lines. The breqn package makes them
work as one would expect whether or not there is an intervening line break. The
single most ambitious goal of the package, however, is to support automatic
linebreaking of displayed equations. Such linebreaking cannot be done without
substantial changes under the hood in the way formulae are processed; the code
must be watched carefully, keeping an eye on possible glitches. The bundle also
contains the flexisym and mathstyle packages, which are both designated as
support for breqn.

%package -n texlive-caption
Summary:        Customising captions in floating environments
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-caption-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-caption-doc <= 11:%{version}
Requires:       tex(keyval.sty)
Requires:       tex(newfloat.sty)

%description -n texlive-caption
The caption package provides many ways to customise the captions in floating
environments like figure and table, and cooperates with many other packages.
Facilities include rotating captions, sideways captions, continued captions
(for tables or figures that come in several parts). A list of compatibility
notes, for other packages, is provided in the documentation. The package also
provides the "caption outside float" facility, in the same way that simpler
packages like capt-of do. The package supersedes caption2.

%package -n texlive-cite
Summary:        Improved citation handling in LaTeX
Version:        svn77682
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cite-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cite-doc <= 11:%{version}

%description -n texlive-cite
The package supports compressed, sorted lists of numerical citations, and also
deals with various punctuation and other issues of representation, including
comprehensive management of break points. The package is compatible with both
hyperref and backref. The package is (unsurprisingly) part of the cite bundle
of the author's citation-related packages.

%package -n texlive-cmap
Summary:        Make PDF files searchable and copyable
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cmap-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cmap-doc <= 11:%{version}

%description -n texlive-cmap
The cmap package provides character map tables, which make PDF files generated
by pdfLaTeX both searchable and copy-able in acrobat reader and other compliant
PDF viewers. Encodings supported are OT1, OT6, T1, T2A, T2B, T2C and T5,
together with LAE (Arabic), LFE (Farsi) and LGR (Greek) and a variant OT1tt for
cmtt-like fonts. The package's main limitation currently is the inability to
work with virtual fonts, because of limitations of pdfTeX. This restriction may
be resolved in a future version of pdfTeX.

%package -n texlive-crop
Summary:        Support for cropmarks
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-crop-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-crop-doc <= 11:%{version}
Requires:       tex(color.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifluatex.sty)

%description -n texlive-crop
A package providing corner marks for camera alignment as well as for trimming
paper stacks, and additional page information on every page if required. Most
macros are easily adaptable to personal preferences. An option is provided for
selectively suppressing graphics or text, which may be useful for printing just
colour graphics on a colour laser printer and the rest on a cheap mono laser
printer. A page info line contains the time and a new cropmarks index and is
printed at the top of the page. A configuration command is provided for the
info line font. Options for better collaboration with dvips, pdfTeX and vtex
are provided.

%package -n texlive-ctable
Summary:        Flexible typesetting of table and figure floats using key/value directives
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ctable-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ctable-doc <= 11:%{version}
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(rotating.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(transparent.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)

%description -n texlive-ctable
Provides commands to typeset centered, left- or right-aligned table and
(multiple-)figure floats, with footnotes. Instead of an environment, a command
with 4 arguments is used; the first is optional and is used for key,value pairs
generating variations on the defaults and offering a route for future
extensions.

%package -n texlive-eso-pic
Summary:        Add picture commands (or backgrounds) to every page
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-eso-pic-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-eso-pic-doc <= 11:%{version}
Requires:       tex(color.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xcolor.sty)

%description -n texlive-eso-pic
The package adds one or more user commands to LaTeX's shipout routine, which
may be used to place the output at fixed positions. The grid option may be used
to find the correct places.

%package -n texlive-euenc
Summary:        Unicode font encoding definitions for XeTeX
Version:        svn19795
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-euenc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-euenc-doc <= 11:%{version}

%description -n texlive-euenc
Font encoding definitions for unicode fonts loaded by LaTeX in XeTeX or LuaTeX.
The package provides two encodings: EU1, designed for use with XeTeX, which the
fontspec uses for unicode fonts which require no macro-level processing for
accents, and EU2, which provides the same facilities for use with LuaTeX.
Neither encoding places any restriction on the glyphs provided by a font; use
of EU2 causes the package euxunicode to be loaded (the package is part of this
distribution). The package includes font definition files for use with the
Latin Modern OpenType fonts.

%package -n texlive-euler
Summary:        Use AMS Euler fonts for math
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-euler-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-euler-doc <= 11:%{version}

%description -n texlive-euler
Provides a setup for using the AMS Euler family of fonts for mathematics in
LaTeX documents. "The underlying philosophy of Zapf's Euler design was to
capture the flavour of mathematics as it might be written by a mathematician
with excellent handwriting." The euler package is based on Knuth's macros for
the book 'Concrete Mathematics'. The text fonts for the Concrete book are
supported by the beton package.

%package -n texlive-everysel
Summary:        Provides hooks into \selectfont
Version:        svn57489
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-everysel
The package provided hooks whose arguments are executed just after LaTeX has
loaded a new font by means of \selectfont. It has become obsolete with LaTeX
versions 2021/01/05 or newer, since LaTeX now provides its own hooks to fulfill
this task. For newer versions of LaTeX everysel only provides macros using
LaTeX's hook management due to compatibility reasons. See lthooks-doc.pdf for
instructions how to use lthooks instead of everysel.

%package -n texlive-everyshi
Summary:        Take action at every \shipout
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-everyshi
This package provides hooks into \sshipout called \EveryShipout and
\AtNextShipout analogous to \AtBeginDocument. With the introduction of the
LaTeX hook management this package became obsolete in 2020 and is only provided
for backwards compatibility. For current versions of LaTeX it is only mapping
the hooks to the original everyshi macros. In case you use an older LaTeX
format, everyshi will automatically fall back to its old implementation by
loading everyshi-2001-05-15.

%package -n texlive-extsizes
Summary:        Extend the standard classes' size options
Version:        svn78101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-extsizes-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-extsizes-doc <= 11:%{version}

%description -n texlive-extsizes
Provides classes extarticle, extreport, extletter, extbook and extproc which
provide for documents with a base font size from 8-20pt. There is also a LaTeX
package, extsizes.sty, which can be used with nonstandard document classes. But
it cannot be guaranteed to work with any given class.

%package -n texlive-fancybox
Summary:        Variants of \fbox and other games with boxes
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancybox-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancybox-doc <= 11:%{version}

%description -n texlive-fancybox
Provides variants of \fbox: \shadowbox, \doublebox, \ovalbox, \Ovalbox, with
helpful tools for using box macros and flexible verbatim macros. You can box
mathematics, floats, center, flushleft, and flushright, lists, and pages.

%package -n texlive-fancyref
Summary:        A LaTeX package for fancy cross-referencing
Version:        svn77682
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancyref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancyref-doc <= 11:%{version}
Requires:       tex(varioref.sty)

%description -n texlive-fancyref
Provides fancy cross-referencing support, based on the package's reference
commands (\fref and \Fref) that recognise what sort of object is being
referenced. So, for example, the label for a \section would be expected to be
of the form 'sec:foo': the package would recognise the 'sec:' part.

%package -n texlive-fancyvrb
Summary:        Sophisticated verbatim text
Version:        svn78721
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancyvrb-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancyvrb-doc <= 11:%{version}
Requires:       tex(keyval.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xcolor.sty)

%description -n texlive-fancyvrb
Flexible handling of verbatim text including: verbatim commands in footnotes; a
variety of verbatim environments with many parameters; ability to define new
customized verbatim environments; save and restore verbatim text and
environments; write and read files in verbatim mode; build "example"
environments (showing both result and verbatim source).

%package -n texlive-filehook
Summary:        Hooks for input files
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-filehook-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-filehook-doc <= 11:%{version}
Requires:       tex(currfile.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfkeys.sty)

%description -n texlive-filehook
The package provides several file hooks (AtBegin, AtEnd, ...) for files read by
\input, \include and \InputIfFileExists. General hooks for all such files (e.g.
all \included ones) and file specific hooks only used for named files are
provided; two hooks are provided for the end of \included files -- one before,
and one after the final \clearpage.

%package -n texlive-float
Summary:        Improved interface for floating objects
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-float-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-float-doc <= 11:%{version}

%description -n texlive-float
Improves the interface for defining floating objects such as figures and
tables. Introduces the boxed float, the ruled float and the plaintop float. You
can define your own floats and improve the behaviour of the old ones. The
package also provides the H float modifier option of the obsolete here package.
You can select this as automatic default with \floatplacement{figure}{H}.

%package -n texlive-fontspec
Summary:        Advanced font selection in XeLaTeX and LuaLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fontspec-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fontspec-doc <= 11:%{version}
Requires:       texlive-euenc
Requires:       texlive-iftex
Requires:       texlive-l3kernel
Requires:       texlive-l3packages
Requires:       texlive-lm
Requires:       texlive-xunicode
Requires:       tex(fontenc.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(xparse.sty)

%description -n texlive-fontspec
Fontspec is a package for XeLaTeX and LuaLaTeX. It provides an automatic and
unified interface to feature-rich AAT and OpenType fonts through the NFSS in
LaTeX running on XeTeX or LuaTeX engines. The package requires the l3kernel and
xparse bundles from the LaTeX3 development team.

%package -n texlive-footnotehyper
Summary:        A hyperref aware footnote environment
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-footnotehyper-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-footnotehyper-doc <= 11:%{version}

%description -n texlive-footnotehyper
This package provides a footnote environment allowing verbatim material and a
savenotes environment which captures footnotes across problematic environments.
It is a successor to the footnote package by Mark Wooding which had various
compatibility issues with modern packages (hyperref, color, xcolor,
babel-french).

%package -n texlive-fp
Summary:        Fixed point arithmetic
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fp-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fp-doc <= 11:%{version}

%description -n texlive-fp
An extensive collection of arithmetic operations for fixed point real numbers
of high precision.

%package -n texlive-grffile
Summary:        Extended file name support for graphics (legacy package)
Version:        svn78101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(stringenc.sty)

%description -n texlive-grffile
The original package extended the file name processing of package graphics to
support a larger range of file names. The base LaTeX code now supports multiple
dots and spaces, and this package by default is a stub that just loads
graphicx. However, \usepackage{grffile}[=v1] may be used to access version
1(.18) of the package if that is needed.

%package -n texlive-hologo
Summary:        A collection of logos with bookmark support
Version:        svn78580
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(kvdefinekeys.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)

%description -n texlive-hologo
The package defines a single command \hologo, whose argument is the usual
case-confused ASCII version of the logo. The command is bookmark-enabled, so
that every logo becomes available in bookmarks without further work.

%package -n texlive-index
Summary:        Extended index for LaTeX including multiple indexes
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-index-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-index-doc <= 11:%{version}

%description -n texlive-index
This is a reimplementation of LaTeX's indexing macros to provide better support
for indexing. For example, it supports multiple indexes in a single document
and provides a more robust \index command. It supplies short hand notations for
the \index command (^{word}) and a * variation of \index (abbreviated _{word})
that prints the word being indexed, as well as creating an index entry for it.

%package -n texlive-infwarerr
Summary:        Complete set of information/warning/error message macros
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-infwarerr
This package provides a complete set of macros for information, warning and
error messages. Under LaTeX, the commands are wrappers for the corresponding
LaTeX commands; under Plain TeX they are available as complete implementations.

%package -n texlive-jknapltx
Summary:        Miscellaneous packages by Joerg Knappen
Version:        svn19440
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-jknapltx-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-jknapltx-doc <= 11:%{version}
Requires:       tex(graphicx.sty)
Requires:       tex(textcomp.sty)

%description -n texlive-jknapltx
Miscellaneous macros by Jorg Knappen, including: represent counters in greek;
Maxwell's non-commutative division; latin1jk, latin2jk and latin3jk, which are
their inputenc definition files that allow verbatim input in the respective ISO
Latin codes; blackboard bold fonts in maths; use of RSFS fonts in maths; extra
alignments for \parboxes; swap Roman and Sans fonts; transliterate semitic
languages; patches to make (La)TeX formulae embeddable in SGML; use maths
"minus" in text as appropriate; simple Young tableaux.

%package -n texlive-koma-script
Summary:        A bundle of versatile classes and packages
Version:        svn77575
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       texlive-xpatch
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(multicol.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)

%description -n texlive-koma-script
The KOMA-Script bundle provides replacements for the article, report, and book
classes with emphasis on typography and versatility. There is also a letter
class. The bundle also offers: a package for calculating type areas in the way
laid down by the typographer Jan Tschichold, packages for easily changing and
defining page styles, a package scrdate for getting not only the current date
but also the name of the day, and a package scrtime for getting the current
time. All these packages may be used not only with KOMA-Script classes but also
with the standard classes. Since every package has its own version number, the
version number quoted only refers to the version of scrbook, scrreprt,
scrartcl, scrlttr2 and typearea (which are the main parts of the bundle).

%package -n texlive-l3experimental
Summary:        Experimental LaTeX3 concepts
Version:        svn78549
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l3experimental-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l3experimental-doc <= 11:%{version}
Requires:       texlive-l3kernel

%description -n texlive-l3experimental
The l3experimental packages are a collection of experimental implementations
for aspects of the LaTeX3 kernel, dealing with higher-level ideas such as the
Designer Interface. Some of them work as stand alone packages, providing new
functionality, and can be used on top of LaTeX2e with no changes to the
existing kernel. The present release includes: l3draw, a code-level interface
for constructing drawings; xcoffins, which allows the alignment of boxes using
a series of 'handle' positions, supplementing the simple TeX reference point;

%package -n texlive-latexbug
Summary:        Bug classification for LaTeX related bugs
Version:        svn78389
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-latexbug
The package is written in order to help identifying the rightful addressee for
a bug report. The LaTeX team asks that it will be loaded in any test file that
is intended to be sent to the LaTeX bug database as part of a bug report.

%package -n texlive-lineno
Summary:        Line numbers on paragraphs
Version:        svn78315
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lineno-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lineno-doc <= 11:%{version}
Requires:       tex(etoolbox.sty)
Requires:       tex(finstrut.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(longtable.sty)
Requires:       tex(ltabptch.sty)
Requires:       tex(varioref.sty)

%description -n texlive-lineno
Adds line numbers to selected paragraphs with reference possible through the
LaTeX \ref and \pageref cross reference mechanism. Line numbering may be
extended to footnote lines, using the fnlineno package.

%package -n texlive-listings
Summary:        Typeset source code listings using LaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-listings-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-listings-doc <= 11:%{version}
Requires:       tex(algorithmic.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(keyval.sty)
# Ignoring dependency on lgrind.sty - non-free
Requires:       tex(textcomp.sty)
Requires:       tex(xurl.sty)

%description -n texlive-listings
The package enables the user to typeset programs (programming code) within
LaTeX; the source code is read directly by TeX--no front-end processor is
needed. Keywords, comments and strings can be typeset using different styles
(default is bold for keywords, italic for comments and no special style for
strings). Support for hyperref is provided. To use, \usepackage{listings},
identify the language of the object to typeset, using a construct like:
\lstset{language=Python}, then use environment lstlisting for inline code.
External files may be formatted using \lstinputlisting to process a given file
in the form appropriate for the current language. Short (in-line) listings are
also available, using either \lstinline|...| or |...| (after defining the |
token with the \lstMakeShortInline command).

%package -n texlive-ltx-talk
Summary:        A class for typesetting presentations
Version:        svn78710
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ltx-talk
This class is experimental, and changes may occur to interfaces. Development is
focussed on tagging/functionality as the primary driver; as such, support for
design aspects is likely to be lower priority. It requires LaTeX 2025-11-01 or
later. The ltx-talk class is focused on producing (on-screen) presentations,
along with support material such as handouts and speaker notes. Content is
created in a frame environment, each of which can be divided up into a number
of slides (actual output pages). A simple 'overlay' notation is used to specify
which material appears on each slide within a frame. The class supports a range
of environments to enable complex slide relationships to be constructed. The
appearance of slides is controlled by a template system. Many of the elements
of slides can be adjusted by setting simple key-based values in the preamble.
More complex changes can be implemented by altering specific, targeted
definitions without needing to rewrite entire blocks of code. This allows a
variety of visual appearances to be selected for the same content source. The
ltx-talk class has syntax similar to the popular beamer class, although there
are some (deliberate) differences. However, ltx-talk has been implemented to
support creation of tagged (accessible) PDF output as a core aim. As such, it
is suited to creating output for reuse in other formats, e.g. HTML conversions,
without additional steps.

%package -n texlive-lua-unicode-math
Summary:        OpenType Math font support for LuaLaTeX
Version:        svn78498
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lua-unicode-math
A faster and more compatible package to support using OpenType math fonts in
LuaLaTeX as an alternative for unicode-math.

%package -n texlive-mathspec
Summary:        Specify arbitrary fonts for mathematics in XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mathspec-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mathspec-doc <= 11:%{version}
Requires:       tex(MnSymbol.sty)
Requires:       tex(amstext.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)

%description -n texlive-mathspec
The mathspec package provides an interface to typeset mathematics in XeLaTeX
with arbitrary text fonts using fontspec as a backend. The package is under
development and later versions might to be incompatible with this version, as
this version is incompatible with earlier versions. The package requires at
least version 0.9995 of XeTeX.

%package -n texlive-mathtools
Summary:        Mathematical tools to use with amsmath
Version:        svn78251
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mathtools-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mathtools-doc <= 11:%{version}
Requires:       texlive-amsmath
Requires:       texlive-tools
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)

%description -n texlive-mathtools
Mathtools provides a series of packages designed to enhance the appearance of
documents containing a lot of mathematics. The main backbone is amsmath, so
those unfamiliar with this required part of the LaTeX system will probably not
find the packages very useful. Mathtools provides many useful tools for
mathematical typesetting. It is based on amsmath and fixes various deficiencies
of amsmath and standard LaTeX. It provides: Extensible symbols, such as
brackets, arrows, harpoons, etc.; Various symbols such as \coloneqq (:=); Easy
creation of new tag forms; Showing equation numbers only for referenced
equations; Extensible arrows, harpoons and hookarrows; Starred versions of the
amsmath matrix environments for specifying the column alignment; More building
blocks: multlined, cases-like environments, new gathered environments; Maths
versions of \makebox, \llap, \rlap etc.; Cramped math styles; and more...
Mathtools requires mhsetup.

%package -n texlive-mdwtools
Summary:        Miscellaneous tools by Mark Wooding
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mdwtools-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mdwtools-doc <= 11:%{version}

%description -n texlive-mdwtools
This collection of tools includes: support for short commands starting with @,
macros to sanitise the OT1 encoding of the cmtt fonts; a 'do after' command;
improved footnote support; mathenv for various alignment in maths; list
handling; mdwmath which adds some minor changes to LaTeX maths; a rewrite of
LaTeX's tabular and array environments; verbatim handling; and syntax diagrams.

%package -n texlive-memoir
Summary:        Typeset fiction, non-fiction and mathematical books
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-memoir-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-memoir-doc <= 11:%{version}

%description -n texlive-memoir
The memoir class is for typesetting poetry, fiction, non-fiction, and
mathematical works. Permissible document 'base' font sizes range from 9 to
60pt. There is a range of page-styles and well over a dozen chapter-styles to
choose from, as well as methods for specifying your own layouts and designs.
The class also provides the functionality of over thirty of the more popular
packages, thus simplifying document sources. Users who wish to use the hyperref
package, in a document written with the memoir class, should also use the
memhfixc package (part of this bundle). Note, however, that any current version
of hyperref actually loads the package automatically if it detects that it is
running under memoir.

%package -n texlive-metalogo
Summary:        Extended TeX logo macros
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-metalogo-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-metalogo-doc <= 11:%{version}
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifxetex.sty)

%description -n texlive-metalogo
This package exposes spacing parameters for various TeX logos to the end user,
to optimise the logos for different fonts. Written especially for XeLaTeX
users.

%package -n texlive-microtype
Summary:        Subliminal refinements towards typographical perfection
Version:        svn78228
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-microtype-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-microtype-doc <= 11:%{version}
Requires:       texlive-etoolbox
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xcolor.sty)

%description -n texlive-microtype
The package provides a LaTeX interface to the micro-typographic extensions that
were introduced by pdfTeX and have since also propagated to XeTeX and LuaTeX:
most prominently, character protrusion and font expansion, furthermore the
adjustment of interword spacing and additional kerning, as well as hyphenatable
letterspacing (tracking) and the possibility to disable all or selected
ligatures. These features may be applied to customisable sets of fonts, and all
micro-typographic aspects of the fonts can be configured in a straight-forward
and flexible way. Settings for various fonts are provided. Note that character
protrusion requires pdfTeX, LuaTeX, or XeTeX. Font expansion works with pdfTeX
or LuaTeX. The package will by default enable protrusion and expansion if they
can safely be assumed to work. Disabling ligatures requires pdfTeX or LuaTeX,
while the adjustment of interword spacing and of kerning only works with
pdfTeX. Letterspacing is available with pdfTeX, LuaTeX or XeTeX. The
alternative package 'letterspace', which also works with plain TeX, provides
the user commands for letterspacing only, omitting support for all other
extensions.

%package -n texlive-newfloat
Summary:        Define new floating environments
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)

%description -n texlive-newfloat
The package offers the command \DeclareFloatingEnvironment, which the user may
use to define new floating environments which behave like the LaTeX standard
floating environments figure and table.

%package -n texlive-ntgclass
Summary:        "European" versions of standard classes
Version:        svn77239
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ntgclass-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ntgclass-doc <= 11:%{version}

%description -n texlive-ntgclass
The bundle offers versions of the standard LaTeX article and report classes,
rewritten to reflect a more European design, and the a4 package, which is
better tuned to the shape of a4 paper than is the a4paper class option of the
standard classes. The classes include several for article and report
requirements, and a letter class. The elements of the bundle were designed by
members of the Dutch TeX Users Group NTG.

%package -n texlive-parskip
Summary:        Layout with zero \parindent, non-zero \parskip
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-parskip-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-parskip-doc <= 11:%{version}
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)

%description -n texlive-parskip
Simply changing \parskip and \parindent leaves a layout that is untidy; this
package (though it is no substitute for a properly-designed class) helps
alleviate this untidiness.

%package -n texlive-pdfcolfoot
Summary:        Separate color stack for footnotes with pdfTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pdfcol.sty)

%description -n texlive-pdfcolfoot
Since version 1.40 pdfTeX supports several colour stacks. This package uses a
separate colour stack for footnotes that can break across pages.

%package -n texlive-pdflscape
Summary:        Make landscape pages display as landscape
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(lscape.sty)

%description -n texlive-pdflscape
The package adds PDF support to the landscape environment of package lscape, by
setting the PDF /Rotate page attribute. Pages with this attribute will be
displayed in landscape orientation by conforming PDF viewers.

%package -n texlive-pdfpages
Summary:        Include PDF documents in LaTeX
Version:        svn78558
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pdfpages-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pdfpages-doc <= 11:%{version}
Requires:       texlive-eso-pic
Requires:       texlive-graphics
Requires:       texlive-oberdiek
Requires:       texlive-pdflscape
Requires:       texlive-tools
Requires:       tex(calc.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pdflscape.sty)

%description -n texlive-pdfpages
This package simplifies the inclusion of external multi-page PDF documents in
LaTeX documents. Pages may be freely selected and similar to psnup it is
possible to put several logical pages onto each sheet of paper. Furthermore a
lot of hypertext features like hyperlinks and article threads are provided. The
package supports pdfTeX (pdfLaTeX) and VTeX. With VTeX it is even possible to
use this package to insert PostScript files, in addition to PDF files.

%package -n texlive-polyglossia
Summary:        An alternative to babel for XeLaTeX and LuaLaTeX
Version:        svn78740
License:        MIT AND LPPL-1.3c AND CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-polyglossia-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-polyglossia-doc <= 11:%{version}
Requires:       texlive-etoolbox
Requires:       texlive-filehook
Requires:       texlive-fontspec
Requires:       texlive-iftex
Requires:       texlive-makecmds
Requires:       texlive-xkeyval
Requires:       tex(bidi.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(luabidi.sty)
Requires:       tex(unibidi-lua.sty)

%description -n texlive-polyglossia
This package provides a complete Babel replacement for users of LuaLaTeX and
XeLaTeX; it relies on the fontspec package, version 2.0 at least.

%package -n texlive-psfrag
Summary:        Replace strings in encapsulated PostScript figures
Version:        svn15878
License:        psfrag
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-psfrag-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-psfrag-doc <= 11:%{version}
Requires:       tex(graphics.sty)

%description -n texlive-psfrag
Allows LaTeX constructions (equations, picture environments, etc.) to be
precisely superimposed over Encapsulated PostScript figures, using your own
favorite drawing tool to create an EPS figure and placing simple text 'tags'
where each replacement is to be placed, with PSfrag automatically removing
these tags from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

%package -n texlive-ragged2e
Summary:        Alternative versions of "ragged"-type commands
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(everysel.sty)
Requires:       tex(footmisc.sty)

%description -n texlive-ragged2e
The package defines new commands \Centering, \RaggedLeft, and \RaggedRight and
new environments Center, FlushLeft, and FlushRight, which set ragged text and
are easily configurable to allow hyphenation (the corresponding commands in
LaTeX, all of whose names are lower-case, prevent hyphenation altogether).

%package -n texlive-rcs
Summary:        Use RCS (revision control system) tags in LaTeX documents
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-rcs-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-rcs-doc <= 11:%{version}

%description -n texlive-rcs
The rcs package utilizes the inclusion of RCS supplied data in LaTeX documents.
It's upward compatible to *all* rcs styles I know of. In particular, you can
easily access values of every RCS field in your document put the checkin date
on the titlepage put RCS fields in a footline You can typeset revision logs.
Not in verbatim -- real LaTeX text! But you need a configurable RCS for that.
Refer to the user manual for more detailed information. You can also configure
the rcs package easily to do special things for any keyword. This bundle comes
with a user manual, an internal interface description, full documentation of
the implementation, style information for AUC-TeX, and test cases.

%package -n texlive-sansmath
Summary:        Maths in a sans font
Version:        svn77682
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-sansmath-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-sansmath-doc <= 11:%{version}

%description -n texlive-sansmath
The package defines a new math version sans, and a command \sansmath that
behaves somewhat like \boldmath

%package -n texlive-section
Summary:        Modifying section commands in LaTeX
Version:        svn20180
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-section-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-section-doc <= 11:%{version}

%description -n texlive-section
The package implements a pretty extensive scheme to make more manageable the
business of configuring LaTeX output.

%package -n texlive-seminar
Summary:        Make overhead slides
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-seminar-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-seminar-doc <= 11:%{version}
Requires:       tex(hyperref.sty)
Requires:       tex(pst-ovl.sty)

%description -n texlive-seminar
A class that produces overhead slides (transparencies), with many facilities.
The class requires availability of the fancybox package. Seminar is also the
basis of other classes, such as prosper. In fact, seminar is not nowadays
reckoned a good basis for a presentation -- users are advised to use more
recent classes such as powerdot or beamer, both of which are tuned to
21st-century presentation styles. Note that the seminar distribution relies on
the xcomment package, which was once part of the bundle, but now has a separate
existence.

%package -n texlive-sepnum
Summary:        Print numbers in a "friendly" format
Version:        svn20186
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-sepnum-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-sepnum-doc <= 11:%{version}

%description -n texlive-sepnum
Provides a command to print a number with (potentially different) separators
every three digits in the parts either side of the decimal point (the point
itself is also configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command \sepnumform, that
may be used when defining \the<counter> macros.

%package -n texlive-setspace
Summary:        Set space between lines
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-setspace-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-setspace-doc <= 11:%{version}

%description -n texlive-setspace
Provides support for setting the spacing between lines in a document. Package
options include singlespacing, onehalfspacing, and doublespacing. Alternatively
the spacing can be changed as required with the \singlespacing,
\onehalfspacing, and \doublespacing commands. Other size spacings also
available.

%package -n texlive-subfig
Summary:        Figures broken into subfigures
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-subfig-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-subfig-doc <= 11:%{version}
Requires:       tex(caption.sty)
Requires:       tex(keyval.sty)

%description -n texlive-subfig
The package provides support for the manipulation and reference of small or
'sub' figures and tables within a single figure or table environment. It is
convenient to use this package when your subfigures are to be separately
captioned, referenced, or are to be included in the List-of-Figures. A new
\subfigure command is introduced which can be used inside a figure environment
for each subfigure. An optional first argument is used as the caption for that
subfigure. This package supersedes the subfigure package (which is no longer
maintained). The name was changed since the package is not completely backward
compatible with the older package The major advantage of the new package is
that the user interface is keyword/value driven and easier to use. To ease the
transition from the subfigure package, the distribution includes a
configuration file (subfig.cfg) which nearly emulates the subfigure package.
The functionality of the package is provided by the (more recent still)
subcaption package.

%package -n texlive-textcase
Summary:        Case conversion ignoring mathematics, etc.
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-textcase-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-textcase-doc <= 11:%{version}

%description -n texlive-textcase
The textcase package offers commands \MakeTextUppercase and \MakeTextLowercase
which are similar to the standard \MakeUppercase and \MakeLowercase, but they
do not change the case of any sections of mathematics, or the arguments of
\cite, \label and \ref commands within the argument. A further command
\NoCaseChange does nothing but suppress case change within its argument, so to
force uppercase of a section including an environment, one might say:
\MakeTextUppercase{...\NoCaseChange{\begin{foo}}
...\NoCaseChange{\end{foo}}...} In current LaTeX this package is obsolete. You
can use the standard \MakeUppercase and \MakeLowercase, but it defines legacy
names \MakeTextUppercase and \MakeTextLowercase.

%package -n texlive-translator
Summary:        Easy translation of strings in LaTeX
Version:        svn77682
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)

%description -n texlive-translator
This LaTeX package provides a flexible mechanism for translating individual
words into different languages. For example, it can be used to translate a word
like "figure" into, say, the German word "Abbildung". Such a translation
mechanism is useful when the author of some package would like to localize the
package such that texts are correctly translated into the language preferred by
the user. This package is not intended to be used to automatically translate
more than a few words.

%package -n texlive-typehtml
Summary:        Typeset HTML directly from LaTeX
Version:        svn17134
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-typehtml-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-typehtml-doc <= 11:%{version}
Requires:       tex(exscale.sty)

%description -n texlive-typehtml
Can handle almost all of HTML2, and most of the math fragment of the draft
HTML3.

%package -n texlive-ucharcat
Summary:        Implementation of the (new in 2015) XeTeX \Ucharcat command in Lua, for LuaTeX
Version:        svn78415
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ucharcat-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ucharcat-doc <= 11:%{version}

%description -n texlive-ucharcat
The package implements the \Ucharcat command for LuaLaTeX. \Ucharcat is a new
primitive in XeTeX, an extension of the existing \Uchar command, that allows
the specification of the catcode as well as character code of the character
token being constructed.

%package -n texlive-underscore
Summary:        Control the behaviour of "_" in text
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-underscore-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-underscore-doc <= 11:%{version}
Requires:       tex(chicago.sty)
Requires:       tex(fontenc.sty)

%description -n texlive-underscore
With the package, \_ in text mode (i.e., \textunderscore) prints an underscore
so that hyphenation of words either side of it is not affected; a package
option controls whether an actual hyphenation point appears after the
underscore, or merely a break point. The package also arranges that, while in
text, '_' itself behaves as \textunderscore (the behaviour of _ in maths mode
is not affected).

%package -n texlive-unicode-math
Summary:        Unicode mathematics support for XeTeX and LuaTeX
Version:        svn78251
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-unicode-math-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-unicode-math-doc <= 11:%{version}
Requires:       texlive-amsmath
Requires:       texlive-fontspec
Requires:       texlive-lm-math
Requires:       texlive-lualatex-math
Requires:       tex(amsmath.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(lualatex-math.sty)
Requires:       tex(xparse.sty)

%description -n texlive-unicode-math
This package provides a comprehensive implementation of unicode maths for
XeLaTeX and LuaLaTeX. Unicode maths requires an OpenType mathematics font, of
which there are now a number available via CTAN. While backwards compatibility
is strived for, there are some differences between the legacy mathematical
definitions in LaTeX and amsmath, and the Unicode mathematics definitions. Care
should be taken when transitioning from a legacy workflow to a Unicode-based
one.

%package -n texlive-xcolor
Summary:        Driver-independent color extensions for LaTeX and pdfLaTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xcolor-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xcolor-doc <= 11:%{version}
Requires:       tex(colortbl.sty)
Requires:       tex(pdfcolmk.sty)

%description -n texlive-xcolor
The package starts from the basic facilities of the color package, and provides
easy driver-independent access to several kinds of color tints, shades, tones,
and mixes of arbitrary colors. It allows a user to select a document-wide
target color model and offers complete tools for conversion between eight color
models. Additionally, there is a command for alternating row colors plus
repeated non-aligned material (like horizontal lines) in tables. Colors can be
mixed like \color{red!30!green!40!blue}.

%package -n texlive-xfrac
Summary:        Split-level fractions
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(graphicx.sty)

%description -n texlive-xfrac
This package uses the interface defined by LaTeX templates to provide flexible
split-level fractions via the \sfrac macro. This is both a demonstration of the
power of the template concept and also a useful addition to the available
functionality in LaTeX2e.

%package -n texlive-xkeyval
Summary:        Extension of the keyval package
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xkeyval-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xkeyval-doc <= 11:%{version}
Requires:       tex(longtable.sty)

%description -n texlive-xkeyval
This package is an extension of the keyval package and offers additional macros
for setting keys and declaring and setting class or package options. The
package allows the programmer to specify a prefix to the name of the macros it
defines for keys, and to define families of key definitions; these all help use
in documents where several packages define their own sets of keys.

%package -n texlive-xltxtra
Summary:        "Extras" for LaTeX users of XeTeX
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xltxtra-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xltxtra-doc <= 11:%{version}
Requires:       texlive-metalogo
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(realscripts.sty)

%description -n texlive-xltxtra
This package was previously used to provide a number of features that were
useful for typesetting documents with XeLaTeX. Many of those features have now
been incorporated into the fontspec package and other packages, but the package
persists for backwards compatibility. Nowadays, loading xltxtra will: load the
fontspec, metalogo, and realscripts packages; redefine \showhyphens so it works
correctly; and define two extra commands: \vfrac and \namedglyph.

%package -n texlive-xunicode
Summary:        Generate Unicode characters from accented glyphs
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xunicode-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xunicode-doc <= 11:%{version}
Requires:       texlive-tipa
Requires:       tex(graphicx.sty)

%description -n texlive-xunicode
The package supports XeTeX's (and other putative future similar engines') need
for Unicode characters, in a similar way to what the fontenc does for 8-bit
(and the like) fonts: convert accent-glyph sequence to a single Unicode
character for output. The package also covers glyphs specified by packages
(such as tipa) which define many commands for single text glyphs.


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
tar -xf %{SOURCE117} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE118} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE119} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE120} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE121} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE122} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE123} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE124} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE125} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE126} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE127} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE128} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE129} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE130} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE131} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE132} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE133} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE134} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE135} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE136} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-anysize
%license pd.txt
%{_texmf_main}/tex/latex/anysize/
%doc %{_texmf_main}/doc/latex/anysize/

%files -n texlive-beamer
%license lppl1.3c.txt
%license gpl2.txt
%license fdl.txt
%{_texmf_main}/tex/latex/beamer/
%doc %{_texmf_main}/doc/latex/beamer/

%files -n texlive-booktabs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/booktabs/
%doc %{_texmf_main}/doc/latex/booktabs/

%files -n texlive-breqn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/breqn/
%doc %{_texmf_main}/doc/latex/breqn/

%files -n texlive-caption
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/caption/
%doc %{_texmf_main}/doc/latex/caption/

%files -n texlive-cite
%license other-free.txt
%{_texmf_main}/tex/latex/cite/
%doc %{_texmf_main}/doc/latex/cite/

%files -n texlive-cmap
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cmap/
%doc %{_texmf_main}/doc/latex/cmap/

%files -n texlive-crop
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/crop/
%doc %{_texmf_main}/doc/latex/crop/

%files -n texlive-ctable
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ctable/
%doc %{_texmf_main}/doc/latex/ctable/

%files -n texlive-eso-pic
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eso-pic/
%doc %{_texmf_main}/doc/latex/eso-pic/

%files -n texlive-euenc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euenc/
%doc %{_texmf_main}/doc/latex/euenc/

%files -n texlive-euler
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/euler/
%doc %{_texmf_main}/doc/latex/euler/

%files -n texlive-everysel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/everysel/
%doc %{_texmf_main}/doc/latex/everysel/

%files -n texlive-everyshi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/everyshi/
%doc %{_texmf_main}/doc/latex/everyshi/

%files -n texlive-extsizes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/extsizes/
%doc %{_texmf_main}/doc/latex/extsizes/

%files -n texlive-fancybox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fancybox/
%doc %{_texmf_main}/doc/latex/fancybox/

%files -n texlive-fancyref
%license gpl2.txt
%{_texmf_main}/tex/latex/fancyref/
%doc %{_texmf_main}/doc/latex/fancyref/

%files -n texlive-fancyvrb
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fancyvrb/
%doc %{_texmf_main}/doc/latex/fancyvrb/

%files -n texlive-filehook
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/filehook/
%doc %{_texmf_main}/doc/latex/filehook/

%files -n texlive-float
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/float/
%doc %{_texmf_main}/doc/latex/float/

%files -n texlive-fontspec
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fontspec/
%doc %{_texmf_main}/doc/latex/fontspec/

%files -n texlive-footnotehyper
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/footnotehyper/
%doc %{_texmf_main}/doc/latex/footnotehyper/

%files -n texlive-fp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fp/
%{_texmf_main}/tex/plain/fp/
%doc %{_texmf_main}/doc/latex/fp/

%files -n texlive-grffile
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/grffile/
%doc %{_texmf_main}/doc/latex/grffile/

%files -n texlive-hologo
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hologo/
%doc %{_texmf_main}/doc/generic/hologo/

%files -n texlive-index
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/index/
%doc %{_texmf_main}/doc/latex/index/

%files -n texlive-infwarerr
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/infwarerr/
%doc %{_texmf_main}/doc/latex/infwarerr/

%files -n texlive-jknapltx
%license gpl2.txt
%{_texmf_main}/tex/latex/jknapltx/
%doc %{_texmf_main}/doc/latex/jknapltx/

%files -n texlive-koma-script
%license lppl1.3c.txt
%{_texmf_main}/doc/latex/koma-script/
%{_texmf_main}/source/latex/koma-script/
%{_texmf_main}/tex/latex/koma-script/

%files -n texlive-l3experimental
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/l3experimental/
%doc %{_texmf_main}/doc/latex/l3experimental/

%files -n texlive-latexbug
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latexbug/
%doc %{_texmf_main}/doc/latex/latexbug/

%files -n texlive-lineno
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lineno/
%doc %{_texmf_main}/doc/latex/lineno/

%files -n texlive-listings
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/listings/
%doc %{_texmf_main}/doc/latex/listings/

%files -n texlive-ltx-talk
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ltx-talk/
%doc %{_texmf_main}/doc/latex/ltx-talk/

%files -n texlive-lua-unicode-math
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/lua-unicode-math/
%doc %{_texmf_main}/doc/lualatex/lua-unicode-math/

%files -n texlive-mathspec
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/mathspec/
%doc %{_texmf_main}/doc/xelatex/mathspec/

%files -n texlive-mathtools
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mathtools/
%doc %{_texmf_main}/doc/latex/mathtools/

%files -n texlive-mdwtools
%license gpl2.txt
%{_texmf_main}/tex/latex/mdwtools/
%doc %{_texmf_main}/doc/latex/mdwtools/

%files -n texlive-memoir
%license lppl1.3c.txt
%{_texmf_main}/makeindex/memoir/
%{_texmf_main}/tex/latex/memoir/
%doc %{_texmf_main}/doc/latex/memoir/

%files -n texlive-metalogo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/metalogo/
%doc %{_texmf_main}/doc/latex/metalogo/

%files -n texlive-microtype
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/microtype/
%doc %{_texmf_main}/doc/latex/microtype/

%files -n texlive-newfloat
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/newfloat/
%doc %{_texmf_main}/doc/latex/newfloat/

%files -n texlive-ntgclass
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ntgclass/
%doc %{_texmf_main}/doc/latex/ntgclass/

%files -n texlive-parskip
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/parskip/
%doc %{_texmf_main}/doc/latex/parskip/

%files -n texlive-pdfcolfoot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pdfcolfoot/
%doc %{_texmf_main}/doc/latex/pdfcolfoot/

%files -n texlive-pdflscape
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pdflscape/
%doc %{_texmf_main}/doc/latex/pdflscape/

%files -n texlive-pdfpages
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pdfpages/
%doc %{_texmf_main}/doc/latex/pdfpages/

%files -n texlive-polyglossia
%license mit.txt
%license lppl1.3c.txt
%license cc-zero-1.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/latex/polyglossia/
%doc %{_texmf_main}/doc/latex/polyglossia/

%files -n texlive-psfrag
%license other-free.txt
%{_texmf_main}/dvips/psfrag/
%{_texmf_main}/tex/latex/psfrag/
%doc %{_texmf_main}/doc/latex/psfrag/

%files -n texlive-ragged2e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ragged2e/
%doc %{_texmf_main}/doc/latex/ragged2e/

%files -n texlive-rcs
%license gpl2.txt
%{_texmf_main}/tex/latex/rcs/
%doc %{_texmf_main}/doc/latex/rcs/

%files -n texlive-sansmath
%license pd.txt
%{_texmf_main}/tex/latex/sansmath/
%doc %{_texmf_main}/doc/latex/sansmath/

%files -n texlive-section
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/section/
%doc %{_texmf_main}/doc/latex/section/

%files -n texlive-seminar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/seminar/
%doc %{_texmf_main}/doc/latex/seminar/

%files -n texlive-sepnum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sepnum/
%doc %{_texmf_main}/doc/latex/sepnum/

%files -n texlive-setspace
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/setspace/
%doc %{_texmf_main}/doc/latex/setspace/

%files -n texlive-subfig
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/subfig/
%doc %{_texmf_main}/doc/latex/subfig/

%files -n texlive-textcase
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/textcase/
%doc %{_texmf_main}/doc/latex/textcase/

%files -n texlive-translator
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/tex/latex/translator/
%doc %{_texmf_main}/doc/latex/translator/

%files -n texlive-typehtml
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/typehtml/
%doc %{_texmf_main}/doc/latex/typehtml/

%files -n texlive-ucharcat
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ucharcat/
%doc %{_texmf_main}/doc/latex/ucharcat/

%files -n texlive-underscore
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/underscore/
%doc %{_texmf_main}/doc/latex/underscore/

%files -n texlive-unicode-math
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/unicode-math/
%doc %{_texmf_main}/doc/latex/unicode-math/

%files -n texlive-xcolor
%license lppl1.3c.txt
%{_texmf_main}/dvips/xcolor/
%{_texmf_main}/tex/latex/xcolor/
%doc %{_texmf_main}/doc/latex/xcolor/

%files -n texlive-xfrac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xfrac/
%doc %{_texmf_main}/doc/latex/xfrac/

%files -n texlive-xkeyval
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/xkeyval/
%{_texmf_main}/tex/latex/xkeyval/
%doc %{_texmf_main}/doc/latex/xkeyval/

%files -n texlive-xltxtra
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xltxtra/
%doc %{_texmf_main}/doc/xelatex/xltxtra/

%files -n texlive-xunicode
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/xunicode/
%doc %{_texmf_main}/doc/xelatex/xunicode/

%changelog
* Wed Apr 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn78568-3
- Update collection from svn77082 to svn78568
- Update 57 components
- Remove pdfmanagement-testphase

* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77082-2
- fix licensing files
- update koma-script, ltx-talk, lua-unicode-math, pdfmanagement-testphase

* Sat Jan 24 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77082-1
- Update to svn77082
- fix descriptions, licensing
- update components to latest

* Wed Oct  8 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75762-3
- update fontspec, ltx-talk, memoir, polyglossia
- filter requires from doc dir

* Mon Sep 22 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75762-2
- add "legacy" provides for tex(latex) and texlive-latex

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75762-1
- Update to TeX Live 2025