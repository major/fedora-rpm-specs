%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-latex
Epoch:          12
Version:        svn77034
Release:        1%{?dist}
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
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftexcmds.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftexcmds.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pslatex.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psnfss.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psnfss.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pspicture.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pspicture.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/refcount.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/refcount.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rerunfilecheck.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rerunfilecheck.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stringenc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stringenc.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tools.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tools.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uniquecounter.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uniquecounter.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/url.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/url.doc.tar.xz
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
Requires:       texlive-pdftexcmds
Requires:       texlive-pslatex
Requires:       texlive-psnfss
Requires:       texlive-pspicture
Requires:       texlive-refcount
Requires:       texlive-rerunfilecheck
Requires:       texlive-stringenc
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
Requires:       tex(fontenc.sty)
Provides:       tex(ae.sty) = %{tl_version}
Provides:       tex(aecompl.sty) = %{tl_version}

%description -n texlive-ae
A set of virtual fonts which emulates T1 coded fonts using the standard CM
fonts. The package name, AE fonts, supposedly stands for "Almost European". The
main use of the package was to produce PDF files using Adobe Type 1 versions of
the CM fonts instead of bitmapped EC fonts. Note that direct substitutes for
the bitmapped EC fonts are now available, via the CM-super, Latin Modern and
(in a restricted way) CM-LGC font sets.

%package -n texlive-amscls
Summary:        AMS document classes for LaTeX
Version:        svn55378
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(amsbooka.sty) = %{tl_version}
Provides:       tex(amsmidx.sty) = %{tl_version}
Provides:       tex(amsthm.sty) = %{tl_version}
Provides:       tex(upref.sty) = %{tl_version}

%description -n texlive-amscls
This bundle contains three AMS classes, amsart (for writing articles for the
AMS), amsbook (for books) and amsproc (for proceedings), together with some
supporting material. This material forms one branch of what was originally the
AMS-LaTeX distribution. The other branch, amsmath, is now maintained and
distributed separately. The user documentation can be found in the package
amscls-doc.

%package -n texlive-amsmath
Summary:        AMS mathematical facilities for LaTeX
Version:        svn76708
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(amsbsy.sty) = %{tl_version}
Provides:       tex(amscd.sty) = %{tl_version}
Provides:       tex(amsgen.sty) = %{tl_version}
Provides:       tex(amsmath-2018-12-01.sty) = %{tl_version}
Provides:       tex(amsmath.sty) = %{tl_version}
Provides:       tex(amsopn.sty) = %{tl_version}
Provides:       tex(amstex.sty) = %{tl_version}
Provides:       tex(amstext.sty) = %{tl_version}
Provides:       tex(amsxtra.sty) = %{tl_version}

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
Version:        svn53051
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(atbegshi.sty) = %{tl_version}

%description -n texlive-atbegshi
This package is a modern reimplementation of package everyshi, providing
various commands to be executed before a \shipout command. It makes use of
e-TeX's facilities if they are available. The package may be used either with
LaTeX or with plain TeX.

%package -n texlive-atveryend
Summary:        Hooks at the very end of a document
Version:        svn72507
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(atveryend.sty) = %{tl_version}

%description -n texlive-atveryend
This LaTeX package provides some wrapper commands around LaTeX end document
hooks.

%package -n texlive-auxhook
Summary:        Hooks for auxiliary files
Version:        svn53173
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(auxhook.sty) = %{tl_version}

%description -n texlive-auxhook
This package auxhook provides hooks for adding stuff at the begin of .aux
files.

%package -n texlive-babel
Summary:        Multilingual support for LaTeX, LuaLaTeX, XeLaTeX, and Plain TeX
Version:        svn77397
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(hhline.sty)
Provides:       tex(UKenglish.sty) = %{tl_version}
Provides:       tex(USenglish.sty) = %{tl_version}
Provides:       tex(afrikaans.sty) = %{tl_version}
Provides:       tex(albanian.sty) = %{tl_version}
Provides:       tex(american.sty) = %{tl_version}
Provides:       tex(austrian.sty) = %{tl_version}
Provides:       tex(babel-abkhazian.tex) = %{tl_version}
Provides:       tex(babel-acadian.tex) = %{tl_version}
Provides:       tex(babel-afar.tex) = %{tl_version}
Provides:       tex(babel-afrikaans.tex) = %{tl_version}
Provides:       tex(babel-aghem.tex) = %{tl_version}
Provides:       tex(babel-akan.tex) = %{tl_version}
Provides:       tex(babel-akkadian.tex) = %{tl_version}
Provides:       tex(babel-albanian.tex) = %{tl_version}
Provides:       tex(babel-alemannic.tex) = %{tl_version}
Provides:       tex(babel-algerianarabic.tex) = %{tl_version}
Provides:       tex(babel-alsatian.tex) = %{tl_version}
Provides:       tex(babel-american.tex) = %{tl_version}
Provides:       tex(babel-americanenglish.tex) = %{tl_version}
Provides:       tex(babel-amharic.tex) = %{tl_version}
Provides:       tex(babel-ancientegyptian.tex) = %{tl_version}
Provides:       tex(babel-ancientgreek.tex) = %{tl_version}
Provides:       tex(babel-ancienthebrew.tex) = %{tl_version}
Provides:       tex(babel-arabic-algeria.tex) = %{tl_version}
Provides:       tex(babel-arabic-dz.tex) = %{tl_version}
Provides:       tex(babel-arabic-eg.tex) = %{tl_version}
Provides:       tex(babel-arabic-egypt.tex) = %{tl_version}
Provides:       tex(babel-arabic-iq.tex) = %{tl_version}
Provides:       tex(babel-arabic-iraq.tex) = %{tl_version}
Provides:       tex(babel-arabic-jo.tex) = %{tl_version}
Provides:       tex(babel-arabic-jordan.tex) = %{tl_version}
Provides:       tex(babel-arabic-lb.tex) = %{tl_version}
Provides:       tex(babel-arabic-lebanon.tex) = %{tl_version}
Provides:       tex(babel-arabic-ma.tex) = %{tl_version}
Provides:       tex(babel-arabic-morocco.tex) = %{tl_version}
Provides:       tex(babel-arabic-palestinianterritories.tex) = %{tl_version}
Provides:       tex(babel-arabic-ps.tex) = %{tl_version}
Provides:       tex(babel-arabic-sa.tex) = %{tl_version}
Provides:       tex(babel-arabic-saudiarabia.tex) = %{tl_version}
Provides:       tex(babel-arabic-sy.tex) = %{tl_version}
Provides:       tex(babel-arabic-syria.tex) = %{tl_version}
Provides:       tex(babel-arabic-tn.tex) = %{tl_version}
Provides:       tex(babel-arabic-tunisia.tex) = %{tl_version}
Provides:       tex(babel-arabic.tex) = %{tl_version}
Provides:       tex(babel-aramaic-nabataean.tex) = %{tl_version}
Provides:       tex(babel-aramaic-nbat.tex) = %{tl_version}
Provides:       tex(babel-aramaic-palm.tex) = %{tl_version}
Provides:       tex(babel-aramaic-palmyrene.tex) = %{tl_version}
Provides:       tex(babel-aramaic.tex) = %{tl_version}
Provides:       tex(babel-armenian.tex) = %{tl_version}
Provides:       tex(babel-assamese.tex) = %{tl_version}
Provides:       tex(babel-asturian.tex) = %{tl_version}
Provides:       tex(babel-asu.tex) = %{tl_version}
Provides:       tex(babel-atsam.tex) = %{tl_version}
Provides:       tex(babel-australian.tex) = %{tl_version}
Provides:       tex(babel-australianenglish.tex) = %{tl_version}
Provides:       tex(babel-austrian.tex) = %{tl_version}
Provides:       tex(babel-austriangerman.tex) = %{tl_version}
Provides:       tex(babel-avestan.tex) = %{tl_version}
Provides:       tex(babel-awadhi.tex) = %{tl_version}
Provides:       tex(babel-aymara.tex) = %{tl_version}
Provides:       tex(babel-azerbaijani-cyrillic.tex) = %{tl_version}
Provides:       tex(babel-azerbaijani-cyrl.tex) = %{tl_version}
Provides:       tex(babel-azerbaijani-latin.tex) = %{tl_version}
Provides:       tex(babel-azerbaijani-latn.tex) = %{tl_version}
Provides:       tex(babel-azerbaijani.tex) = %{tl_version}
Provides:       tex(babel-bafia.tex) = %{tl_version}
Provides:       tex(babel-bahasa.tex) = %{tl_version}
Provides:       tex(babel-bahasai.tex) = %{tl_version}
Provides:       tex(babel-bahasam.tex) = %{tl_version}
Provides:       tex(babel-balinese.tex) = %{tl_version}
Provides:       tex(babel-baluchi.tex) = %{tl_version}
Provides:       tex(babel-bambara.tex) = %{tl_version}
Provides:       tex(babel-bangla.tex) = %{tl_version}
Provides:       tex(babel-basaa.tex) = %{tl_version}
Provides:       tex(babel-bashkir.tex) = %{tl_version}
Provides:       tex(babel-basque.tex) = %{tl_version}
Provides:       tex(babel-bataktoba.tex) = %{tl_version}
Provides:       tex(babel-bavarian.tex) = %{tl_version}
Provides:       tex(babel-belarusian-taraskievica.tex) = %{tl_version}
Provides:       tex(babel-belarusian.tex) = %{tl_version}
Provides:       tex(babel-bemba.tex) = %{tl_version}
Provides:       tex(babel-bena.tex) = %{tl_version}
Provides:       tex(babel-bengali.tex) = %{tl_version}
Provides:       tex(babel-betawi.tex) = %{tl_version}
Provides:       tex(babel-bhojpuri.tex) = %{tl_version}
Provides:       tex(babel-blin.tex) = %{tl_version}
Provides:       tex(babel-bodo.tex) = %{tl_version}
Provides:       tex(babel-bosnian-cyrillic.tex) = %{tl_version}
Provides:       tex(babel-bosnian-cyrl.tex) = %{tl_version}
Provides:       tex(babel-bosnian-latin.tex) = %{tl_version}
Provides:       tex(babel-bosnian-latn.tex) = %{tl_version}
Provides:       tex(babel-bosnian.tex) = %{tl_version}
Provides:       tex(babel-brazil.tex) = %{tl_version}
Provides:       tex(babel-brazilian.tex) = %{tl_version}
Provides:       tex(babel-brazilianportuguese.tex) = %{tl_version}
Provides:       tex(babel-breton.tex) = %{tl_version}
Provides:       tex(babel-british.tex) = %{tl_version}
Provides:       tex(babel-britishenglish.tex) = %{tl_version}
Provides:       tex(babel-bulgarian.tex) = %{tl_version}
Provides:       tex(babel-buriat.tex) = %{tl_version}
Provides:       tex(babel-burmese.tex) = %{tl_version}
Provides:       tex(babel-ca-buddhist.tex) = %{tl_version}
Provides:       tex(babel-ca-chinese.tex) = %{tl_version}
Provides:       tex(babel-ca-coptic.tex) = %{tl_version}
Provides:       tex(babel-ca-ethiopic.tex) = %{tl_version}
Provides:       tex(babel-ca-hebrew.tex) = %{tl_version}
Provides:       tex(babel-ca-islamic.tex) = %{tl_version}
Provides:       tex(babel-ca-julian.tex) = %{tl_version}
Provides:       tex(babel-ca-persian.tex) = %{tl_version}
Provides:       tex(babel-canadian.tex) = %{tl_version}
Provides:       tex(babel-canadianenglish.tex) = %{tl_version}
Provides:       tex(babel-canadianfrench.tex) = %{tl_version}
Provides:       tex(babel-cantonese.tex) = %{tl_version}
Provides:       tex(babel-carian.tex) = %{tl_version}
Provides:       tex(babel-catalan.tex) = %{tl_version}
Provides:       tex(babel-cebuano.tex) = %{tl_version}
Provides:       tex(babel-centralatlastamazight.tex) = %{tl_version}
Provides:       tex(babel-centralkurdish-latin.tex) = %{tl_version}
Provides:       tex(babel-centralkurdish-latn.tex) = %{tl_version}
Provides:       tex(babel-centralkurdish.tex) = %{tl_version}
Provides:       tex(babel-chakma.tex) = %{tl_version}
Provides:       tex(babel-chechen.tex) = %{tl_version}
Provides:       tex(babel-cherokee.tex) = %{tl_version}
Provides:       tex(babel-chiga.tex) = %{tl_version}
Provides:       tex(babel-chinese-hans-hk.tex) = %{tl_version}
Provides:       tex(babel-chinese-hans-mo.tex) = %{tl_version}
Provides:       tex(babel-chinese-hans-sg.tex) = %{tl_version}
Provides:       tex(babel-chinese-hans.tex) = %{tl_version}
Provides:       tex(babel-chinese-hant-hk.tex) = %{tl_version}
Provides:       tex(babel-chinese-hant-mo.tex) = %{tl_version}
Provides:       tex(babel-chinese-hant.tex) = %{tl_version}
Provides:       tex(babel-chinese-simplified-hongkongsarchina.tex) = %{tl_version}
Provides:       tex(babel-chinese-simplified-macausarchina.tex) = %{tl_version}
Provides:       tex(babel-chinese-simplified-singapore.tex) = %{tl_version}
Provides:       tex(babel-chinese-simplified.tex) = %{tl_version}
Provides:       tex(babel-chinese-traditional-hongkongsarchina.tex) = %{tl_version}
Provides:       tex(babel-chinese-traditional-macausarchina.tex) = %{tl_version}
Provides:       tex(babel-chinese-traditional.tex) = %{tl_version}
Provides:       tex(babel-chinese.tex) = %{tl_version}
Provides:       tex(babel-churchslavic-cyrs.tex) = %{tl_version}
Provides:       tex(babel-churchslavic-glag.tex) = %{tl_version}
Provides:       tex(babel-churchslavic-glagolitic.tex) = %{tl_version}
Provides:       tex(babel-churchslavic-oldcyrillic.tex) = %{tl_version}
Provides:       tex(babel-churchslavic.tex) = %{tl_version}
Provides:       tex(babel-churchslavonic.tex) = %{tl_version}
Provides:       tex(babel-chuvash.tex) = %{tl_version}
Provides:       tex(babel-classicallatin.tex) = %{tl_version}
Provides:       tex(babel-classicalmandaic.tex) = %{tl_version}
Provides:       tex(babel-classiclatin.tex) = %{tl_version}
Provides:       tex(babel-colognian.tex) = %{tl_version}
Provides:       tex(babel-coptic.tex) = %{tl_version}
Provides:       tex(babel-cornish.tex) = %{tl_version}
Provides:       tex(babel-corsican.tex) = %{tl_version}
Provides:       tex(babel-croatian.tex) = %{tl_version}
Provides:       tex(babel-czech.tex) = %{tl_version}
Provides:       tex(babel-danish.tex) = %{tl_version}
Provides:       tex(babel-divehi.tex) = %{tl_version}
Provides:       tex(babel-dogri.tex) = %{tl_version}
Provides:       tex(babel-duala.tex) = %{tl_version}
Provides:       tex(babel-dutch.tex) = %{tl_version}
Provides:       tex(babel-dzongkha.tex) = %{tl_version}
Provides:       tex(babel-ecclesiasticallatin.tex) = %{tl_version}
Provides:       tex(babel-ecclesiasticlatin.tex) = %{tl_version}
Provides:       tex(babel-egyptianarabic.tex) = %{tl_version}
Provides:       tex(babel-embu.tex) = %{tl_version}
Provides:       tex(babel-english-au.tex) = %{tl_version}
Provides:       tex(babel-english-australia.tex) = %{tl_version}
Provides:       tex(babel-english-ca.tex) = %{tl_version}
Provides:       tex(babel-english-canada.tex) = %{tl_version}
Provides:       tex(babel-english-gb.tex) = %{tl_version}
Provides:       tex(babel-english-newzealand.tex) = %{tl_version}
Provides:       tex(babel-english-nz.tex) = %{tl_version}
Provides:       tex(babel-english-unitedkingdom.tex) = %{tl_version}
Provides:       tex(babel-english-unitedstates.tex) = %{tl_version}
Provides:       tex(babel-english-us.tex) = %{tl_version}
Provides:       tex(babel-english.tex) = %{tl_version}
Provides:       tex(babel-erzya.tex) = %{tl_version}
Provides:       tex(babel-esperanto.tex) = %{tl_version}
Provides:       tex(babel-estonian.tex) = %{tl_version}
Provides:       tex(babel-etruscan.tex) = %{tl_version}
Provides:       tex(babel-europeanportuguese.tex) = %{tl_version}
Provides:       tex(babel-ewe.tex) = %{tl_version}
Provides:       tex(babel-ewondo.tex) = %{tl_version}
Provides:       tex(babel-faroese.tex) = %{tl_version}
Provides:       tex(babel-farsi.tex) = %{tl_version}
Provides:       tex(babel-filipino.tex) = %{tl_version}
Provides:       tex(babel-finnish.tex) = %{tl_version}
Provides:       tex(babel-french-be.tex) = %{tl_version}
Provides:       tex(babel-french-belgium.tex) = %{tl_version}
Provides:       tex(babel-french-ca.tex) = %{tl_version}
Provides:       tex(babel-french-canada.tex) = %{tl_version}
Provides:       tex(babel-french-ch.tex) = %{tl_version}
Provides:       tex(babel-french-lu.tex) = %{tl_version}
Provides:       tex(babel-french-luxembourg.tex) = %{tl_version}
Provides:       tex(babel-french-switzerland.tex) = %{tl_version}
Provides:       tex(babel-french.tex) = %{tl_version}
Provides:       tex(babel-friulan.tex) = %{tl_version}
Provides:       tex(babel-friulian.tex) = %{tl_version}
Provides:       tex(babel-fulah.tex) = %{tl_version}
Provides:       tex(babel-ga.tex) = %{tl_version}
Provides:       tex(babel-galician.tex) = %{tl_version}
Provides:       tex(babel-ganda.tex) = %{tl_version}
Provides:       tex(babel-geez.tex) = %{tl_version}
Provides:       tex(babel-georgian.tex) = %{tl_version}
Provides:       tex(babel-german-at.tex) = %{tl_version}
Provides:       tex(babel-german-austria-traditional.tex) = %{tl_version}
Provides:       tex(babel-german-austria.tex) = %{tl_version}
Provides:       tex(babel-german-ch.tex) = %{tl_version}
Provides:       tex(babel-german-de.tex) = %{tl_version}
Provides:       tex(babel-german-germany.tex) = %{tl_version}
Provides:       tex(babel-german-switzerland-traditional.tex) = %{tl_version}
Provides:       tex(babel-german-switzerland.tex) = %{tl_version}
Provides:       tex(babel-german-traditional.tex) = %{tl_version}
Provides:       tex(babel-german.tex) = %{tl_version}
Provides:       tex(babel-gothic.tex) = %{tl_version}
Provides:       tex(babel-greek.tex) = %{tl_version}
Provides:       tex(babel-guarani.tex) = %{tl_version}
Provides:       tex(babel-gujarati.tex) = %{tl_version}
Provides:       tex(babel-gusii.tex) = %{tl_version}
Provides:       tex(babel-haryanvi.tex) = %{tl_version}
Provides:       tex(babel-hausa-gh.tex) = %{tl_version}
Provides:       tex(babel-hausa-ghana.tex) = %{tl_version}
Provides:       tex(babel-hausa-ne.tex) = %{tl_version}
Provides:       tex(babel-hausa-niger.tex) = %{tl_version}
Provides:       tex(babel-hausa.tex) = %{tl_version}
Provides:       tex(babel-hawaiian.tex) = %{tl_version}
Provides:       tex(babel-hebrew.tex) = %{tl_version}
Provides:       tex(babel-hindi.tex) = %{tl_version}
Provides:       tex(babel-hmongnjua.tex) = %{tl_version}
Provides:       tex(babel-hungarian.tex) = %{tl_version}
Provides:       tex(babel-icelandic.tex) = %{tl_version}
Provides:       tex(babel-igbo.tex) = %{tl_version}
Provides:       tex(babel-inarisami.tex) = %{tl_version}
Provides:       tex(babel-indon.tex) = %{tl_version}
Provides:       tex(babel-indonesian.tex) = %{tl_version}
Provides:       tex(babel-ingush.tex) = %{tl_version}
Provides:       tex(babel-interlingua.tex) = %{tl_version}
Provides:       tex(babel-interslavic.tex) = %{tl_version}
Provides:       tex(babel-inuktitut.tex) = %{tl_version}
Provides:       tex(babel-irish.tex) = %{tl_version}
Provides:       tex(babel-italian.tex) = %{tl_version}
Provides:       tex(babel-japanese.tex) = %{tl_version}
Provides:       tex(babel-javanese.tex) = %{tl_version}
Provides:       tex(babel-jju.tex) = %{tl_version}
Provides:       tex(babel-jolafonyi.tex) = %{tl_version}
Provides:       tex(babel-kabuverdianu.tex) = %{tl_version}
Provides:       tex(babel-kabyle.tex) = %{tl_version}
Provides:       tex(babel-kaingang.tex) = %{tl_version}
Provides:       tex(babel-kako.tex) = %{tl_version}
Provides:       tex(babel-kalaallisut.tex) = %{tl_version}
Provides:       tex(babel-kalenjin.tex) = %{tl_version}
Provides:       tex(babel-kamba.tex) = %{tl_version}
Provides:       tex(babel-kangri.tex) = %{tl_version}
Provides:       tex(babel-kannada.tex) = %{tl_version}
Provides:       tex(babel-kashmiri.tex) = %{tl_version}
Provides:       tex(babel-kazakh.tex) = %{tl_version}
Provides:       tex(babel-khmer.tex) = %{tl_version}
Provides:       tex(babel-kikuyu.tex) = %{tl_version}
Provides:       tex(babel-kinyarwanda.tex) = %{tl_version}
Provides:       tex(babel-komi.tex) = %{tl_version}
Provides:       tex(babel-konkani.tex) = %{tl_version}
Provides:       tex(babel-korean-han.tex) = %{tl_version}
Provides:       tex(babel-korean-hani.tex) = %{tl_version}
Provides:       tex(babel-korean.tex) = %{tl_version}
Provides:       tex(babel-koyraborosenni.tex) = %{tl_version}
Provides:       tex(babel-koyrachiini.tex) = %{tl_version}
Provides:       tex(babel-kurdish-arab.tex) = %{tl_version}
Provides:       tex(babel-kurdish-arabic.tex) = %{tl_version}
Provides:       tex(babel-kurdish.tex) = %{tl_version}
Provides:       tex(babel-kurmanji.tex) = %{tl_version}
Provides:       tex(babel-kwasio.tex) = %{tl_version}
Provides:       tex(babel-kyrgyz.tex) = %{tl_version}
Provides:       tex(babel-ladino.tex) = %{tl_version}
Provides:       tex(babel-lakota.tex) = %{tl_version}
Provides:       tex(babel-langi.tex) = %{tl_version}
Provides:       tex(babel-lao.tex) = %{tl_version}
Provides:       tex(babel-latin.tex) = %{tl_version}
Provides:       tex(babel-latvian.tex) = %{tl_version}
Provides:       tex(babel-lepcha.tex) = %{tl_version}
Provides:       tex(babel-ligurian.tex) = %{tl_version}
Provides:       tex(babel-limbu-limb.tex) = %{tl_version}
Provides:       tex(babel-limbu-limbu.tex) = %{tl_version}
Provides:       tex(babel-limbu.tex) = %{tl_version}
Provides:       tex(babel-lineara.tex) = %{tl_version}
Provides:       tex(babel-lingala.tex) = %{tl_version}
Provides:       tex(babel-lithuanian.tex) = %{tl_version}
Provides:       tex(babel-lombard.tex) = %{tl_version}
Provides:       tex(babel-lowersorbian.tex) = %{tl_version}
Provides:       tex(babel-lowgerman.tex) = %{tl_version}
Provides:       tex(babel-lsorbian.tex) = %{tl_version}
Provides:       tex(babel-lu.tex) = %{tl_version}
Provides:       tex(babel-lubakatanga.tex) = %{tl_version}
Provides:       tex(babel-luo.tex) = %{tl_version}
Provides:       tex(babel-luxembourgish.tex) = %{tl_version}
Provides:       tex(babel-luyia.tex) = %{tl_version}
Provides:       tex(babel-lycian.tex) = %{tl_version}
Provides:       tex(babel-lydian.tex) = %{tl_version}
Provides:       tex(babel-macedonian.tex) = %{tl_version}
Provides:       tex(babel-machame.tex) = %{tl_version}
Provides:       tex(babel-magyar.tex) = %{tl_version}
Provides:       tex(babel-maithili.tex) = %{tl_version}
Provides:       tex(babel-makasar-bugi.tex) = %{tl_version}
Provides:       tex(babel-makasar-buginese.tex) = %{tl_version}
Provides:       tex(babel-makasar.tex) = %{tl_version}
Provides:       tex(babel-makhuwa.tex) = %{tl_version}
Provides:       tex(babel-makhuwameetto.tex) = %{tl_version}
Provides:       tex(babel-makonde.tex) = %{tl_version}
Provides:       tex(babel-malagasy.tex) = %{tl_version}
Provides:       tex(babel-malay-bn.tex) = %{tl_version}
Provides:       tex(babel-malay-brunei.tex) = %{tl_version}
Provides:       tex(babel-malay-sg.tex) = %{tl_version}
Provides:       tex(babel-malay-singapore.tex) = %{tl_version}
Provides:       tex(babel-malay.tex) = %{tl_version}
Provides:       tex(babel-malayalam.tex) = %{tl_version}
Provides:       tex(babel-maltese.tex) = %{tl_version}
Provides:       tex(babel-manipuri.tex) = %{tl_version}
Provides:       tex(babel-manx.tex) = %{tl_version}
Provides:       tex(babel-maori.tex) = %{tl_version}
Provides:       tex(babel-marathi.tex) = %{tl_version}
Provides:       tex(babel-masai.tex) = %{tl_version}
Provides:       tex(babel-mazanderani.tex) = %{tl_version}
Provides:       tex(babel-medievallatin.tex) = %{tl_version}
Provides:       tex(babel-melayu.tex) = %{tl_version}
Provides:       tex(babel-meru.tex) = %{tl_version}
Provides:       tex(babel-meta.tex) = %{tl_version}
Provides:       tex(babel-mexican.tex) = %{tl_version}
Provides:       tex(babel-mexicanspanish.tex) = %{tl_version}
Provides:       tex(babel-moldavian.tex) = %{tl_version}
Provides:       tex(babel-mongolian.tex) = %{tl_version}
Provides:       tex(babel-monotonicgreek.tex) = %{tl_version}
Provides:       tex(babel-morisyen.tex) = %{tl_version}
Provides:       tex(babel-mundang.tex) = %{tl_version}
Provides:       tex(babel-muscogee.tex) = %{tl_version}
Provides:       tex(babel-nama.tex) = %{tl_version}
Provides:       tex(babel-naustrian.tex) = %{tl_version}
Provides:       tex(babel-navajo.tex) = %{tl_version}
Provides:       tex(babel-nepali.tex) = %{tl_version}
Provides:       tex(babel-newari.tex) = %{tl_version}
Provides:       tex(babel-newzealand.tex) = %{tl_version}
Provides:       tex(babel-ngerman.tex) = %{tl_version}
Provides:       tex(babel-ngiemboon.tex) = %{tl_version}
Provides:       tex(babel-ngomba.tex) = %{tl_version}
Provides:       tex(babel-nheengatu.tex) = %{tl_version}
Provides:       tex(babel-nigerianpidgin.tex) = %{tl_version}
Provides:       tex(babel-nko.tex) = %{tl_version}
Provides:       tex(babel-norsk.tex) = %{tl_version}
Provides:       tex(babel-northernfrisian.tex) = %{tl_version}
Provides:       tex(babel-northernkurdish-arab.tex) = %{tl_version}
Provides:       tex(babel-northernkurdish-arabic.tex) = %{tl_version}
Provides:       tex(babel-northernkurdish.tex) = %{tl_version}
Provides:       tex(babel-northernluri.tex) = %{tl_version}
Provides:       tex(babel-northernsami.tex) = %{tl_version}
Provides:       tex(babel-northernsotho.tex) = %{tl_version}
Provides:       tex(babel-northndebele.tex) = %{tl_version}
Provides:       tex(babel-norwegian.tex) = %{tl_version}
Provides:       tex(babel-norwegianbokmal.tex) = %{tl_version}
Provides:       tex(babel-norwegiannynorsk.tex) = %{tl_version}
Provides:       tex(babel-nswissgerman.tex) = %{tl_version}
Provides:       tex(babel-nuer.tex) = %{tl_version}
Provides:       tex(babel-nyanja.tex) = %{tl_version}
Provides:       tex(babel-nyankole.tex) = %{tl_version}
Provides:       tex(babel-nynorsk.tex) = %{tl_version}
Provides:       tex(babel-occitan.tex) = %{tl_version}
Provides:       tex(babel-odia.tex) = %{tl_version}
Provides:       tex(babel-oldirish.tex) = %{tl_version}
Provides:       tex(babel-oldnorse.tex) = %{tl_version}
Provides:       tex(babel-oldpersian.tex) = %{tl_version}
Provides:       tex(babel-olduighur.tex) = %{tl_version}
Provides:       tex(babel-oriya.tex) = %{tl_version}
Provides:       tex(babel-oromo.tex) = %{tl_version}
Provides:       tex(babel-osage.tex) = %{tl_version}
Provides:       tex(babel-ossetic.tex) = %{tl_version}
Provides:       tex(babel-papiamento.tex) = %{tl_version}
Provides:       tex(babel-pashto.tex) = %{tl_version}
Provides:       tex(babel-persian.tex) = %{tl_version}
Provides:       tex(babel-phoenician.tex) = %{tl_version}
Provides:       tex(babel-piedmontese.tex) = %{tl_version}
Provides:       tex(babel-polish.tex) = %{tl_version}
Provides:       tex(babel-polutonikogreek.tex) = %{tl_version}
Provides:       tex(babel-polytonicgreek.tex) = %{tl_version}
Provides:       tex(babel-portuges.tex) = %{tl_version}
Provides:       tex(babel-portuguese-br.tex) = %{tl_version}
Provides:       tex(babel-portuguese-brazil.tex) = %{tl_version}
Provides:       tex(babel-portuguese-portugal.tex) = %{tl_version}
Provides:       tex(babel-portuguese-pt.tex) = %{tl_version}
Provides:       tex(babel-portuguese.tex) = %{tl_version}
Provides:       tex(babel-prussian.tex) = %{tl_version}
Provides:       tex(babel-punjabi-arab.tex) = %{tl_version}
Provides:       tex(babel-punjabi-arabic.tex) = %{tl_version}
Provides:       tex(babel-punjabi-gurmukhi.tex) = %{tl_version}
Provides:       tex(babel-punjabi-guru.tex) = %{tl_version}
Provides:       tex(babel-punjabi.tex) = %{tl_version}
Provides:       tex(babel-quechua.tex) = %{tl_version}
Provides:       tex(babel-rajasthani.tex) = %{tl_version}
Provides:       tex(babel-romanian-md.tex) = %{tl_version}
Provides:       tex(babel-romanian-moldova.tex) = %{tl_version}
Provides:       tex(babel-romanian.tex) = %{tl_version}
Provides:       tex(babel-romansh.tex) = %{tl_version}
Provides:       tex(babel-rombo.tex) = %{tl_version}
Provides:       tex(babel-rundi.tex) = %{tl_version}
Provides:       tex(babel-russian.tex) = %{tl_version}
Provides:       tex(babel-russianb.tex) = %{tl_version}
Provides:       tex(babel-rwa.tex) = %{tl_version}
Provides:       tex(babel-sabaean.tex) = %{tl_version}
Provides:       tex(babel-saho.tex) = %{tl_version}
Provides:       tex(babel-sakha.tex) = %{tl_version}
Provides:       tex(babel-samaritan.tex) = %{tl_version}
Provides:       tex(babel-samburu.tex) = %{tl_version}
Provides:       tex(babel-samin.tex) = %{tl_version}
Provides:       tex(babel-sango.tex) = %{tl_version}
Provides:       tex(babel-sangu.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-bangla.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-beng.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-bengali.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-deva.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-devanagari.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-gujarati.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-gujr.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-kannada.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-knda.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-malayalam.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-mlym.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-telu.tex) = %{tl_version}
Provides:       tex(babel-sanskrit-telugu.tex) = %{tl_version}
Provides:       tex(babel-sanskrit.tex) = %{tl_version}
Provides:       tex(babel-santali.tex) = %{tl_version}
Provides:       tex(babel-saraiki.tex) = %{tl_version}
Provides:       tex(babel-sardinian.tex) = %{tl_version}
Provides:       tex(babel-scottish.tex) = %{tl_version}
Provides:       tex(babel-scottishgaelic.tex) = %{tl_version}
Provides:       tex(babel-sena.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrillic-bosniaherzegovina.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrillic-kosovo.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrillic-montenegro.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrillic.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrl-ba.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrl-me.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrl-xk.tex) = %{tl_version}
Provides:       tex(babel-serbian-cyrl.tex) = %{tl_version}
Provides:       tex(babel-serbian-ijekavsk.tex) = %{tl_version}
Provides:       tex(babel-serbian-latin-bosniaherzegovina.tex) = %{tl_version}
Provides:       tex(babel-serbian-latin-kosovo.tex) = %{tl_version}
Provides:       tex(babel-serbian-latin-montenegro.tex) = %{tl_version}
Provides:       tex(babel-serbian-latin.tex) = %{tl_version}
Provides:       tex(babel-serbian-latn-ba.tex) = %{tl_version}
Provides:       tex(babel-serbian-latn-ijekavsk.tex) = %{tl_version}
Provides:       tex(babel-serbian-latn-me.tex) = %{tl_version}
Provides:       tex(babel-serbian-latn-xk.tex) = %{tl_version}
Provides:       tex(babel-serbian-latn.tex) = %{tl_version}
Provides:       tex(babel-serbian.tex) = %{tl_version}
Provides:       tex(babel-serbianc.tex) = %{tl_version}
Provides:       tex(babel-shambala.tex) = %{tl_version}
Provides:       tex(babel-shona.tex) = %{tl_version}
Provides:       tex(babel-sichuanyi.tex) = %{tl_version}
Provides:       tex(babel-sicilian.tex) = %{tl_version}
Provides:       tex(babel-silesian.tex) = %{tl_version}
Provides:       tex(babel-sindhi-deva.tex) = %{tl_version}
Provides:       tex(babel-sindhi-devanagari.tex) = %{tl_version}
Provides:       tex(babel-sindhi-khoj.tex) = %{tl_version}
Provides:       tex(babel-sindhi-khojki.tex) = %{tl_version}
Provides:       tex(babel-sindhi-khudawadi.tex) = %{tl_version}
Provides:       tex(babel-sindhi-sind.tex) = %{tl_version}
Provides:       tex(babel-sindhi.tex) = %{tl_version}
Provides:       tex(babel-sinhala.tex) = %{tl_version}
Provides:       tex(babel-sinteromani.tex) = %{tl_version}
Provides:       tex(babel-slovak.tex) = %{tl_version}
Provides:       tex(babel-slovene.tex) = %{tl_version}
Provides:       tex(babel-slovenian.tex) = %{tl_version}
Provides:       tex(babel-soga.tex) = %{tl_version}
Provides:       tex(babel-somali.tex) = %{tl_version}
Provides:       tex(babel-sorani.tex) = %{tl_version}
Provides:       tex(babel-southernaltai.tex) = %{tl_version}
Provides:       tex(babel-southernsotho.tex) = %{tl_version}
Provides:       tex(babel-southndebele.tex) = %{tl_version}
Provides:       tex(babel-spanish-mexico.tex) = %{tl_version}
Provides:       tex(babel-spanish-mx.tex) = %{tl_version}
Provides:       tex(babel-spanish.tex) = %{tl_version}
Provides:       tex(babel-standardmoroccantamazight.tex) = %{tl_version}
Provides:       tex(babel-sundanese.tex) = %{tl_version}
Provides:       tex(babel-swahili.tex) = %{tl_version}
Provides:       tex(babel-swati.tex) = %{tl_version}
Provides:       tex(babel-swedish.tex) = %{tl_version}
Provides:       tex(babel-swissfrench.tex) = %{tl_version}
Provides:       tex(babel-swissgerman.tex) = %{tl_version}
Provides:       tex(babel-swisshighgerman.tex) = %{tl_version}
Provides:       tex(babel-syriac.tex) = %{tl_version}
Provides:       tex(babel-tachelhit-latin.tex) = %{tl_version}
Provides:       tex(babel-tachelhit-latn.tex) = %{tl_version}
Provides:       tex(babel-tachelhit-tfng.tex) = %{tl_version}
Provides:       tex(babel-tachelhit-tifinagh.tex) = %{tl_version}
Provides:       tex(babel-tachelhit.tex) = %{tl_version}
Provides:       tex(babel-tainua.tex) = %{tl_version}
Provides:       tex(babel-taita.tex) = %{tl_version}
Provides:       tex(babel-tajik.tex) = %{tl_version}
Provides:       tex(babel-tamil.tex) = %{tl_version}
Provides:       tex(babel-tangut.tex) = %{tl_version}
Provides:       tex(babel-taroko.tex) = %{tl_version}
Provides:       tex(babel-tasawaq.tex) = %{tl_version}
Provides:       tex(babel-tatar.tex) = %{tl_version}
Provides:       tex(babel-telugu.tex) = %{tl_version}
Provides:       tex(babel-teso.tex) = %{tl_version}
Provides:       tex(babel-thai.tex) = %{tl_version}
Provides:       tex(babel-tibetan.tex) = %{tl_version}
Provides:       tex(babel-tigre.tex) = %{tl_version}
Provides:       tex(babel-tigrinya.tex) = %{tl_version}
Provides:       tex(babel-tokpisin.tex) = %{tl_version}
Provides:       tex(babel-tongan.tex) = %{tl_version}
Provides:       tex(babel-tsonga.tex) = %{tl_version}
Provides:       tex(babel-tswana.tex) = %{tl_version}
Provides:       tex(babel-turkish.tex) = %{tl_version}
Provides:       tex(babel-turkmen.tex) = %{tl_version}
Provides:       tex(babel-tyap.tex) = %{tl_version}
Provides:       tex(babel-ugaritic.tex) = %{tl_version}
Provides:       tex(babel-ukenglish.tex) = %{tl_version}
Provides:       tex(babel-ukraineb.tex) = %{tl_version}
Provides:       tex(babel-ukrainian.tex) = %{tl_version}
Provides:       tex(babel-uppersorbian.tex) = %{tl_version}
Provides:       tex(babel-urdu.tex) = %{tl_version}
Provides:       tex(babel-usenglish.tex) = %{tl_version}
Provides:       tex(babel-usorbian.tex) = %{tl_version}
Provides:       tex(babel-uyghur.tex) = %{tl_version}
Provides:       tex(babel-uzbek-arab.tex) = %{tl_version}
Provides:       tex(babel-uzbek-arabic.tex) = %{tl_version}
Provides:       tex(babel-uzbek-cyrillic.tex) = %{tl_version}
Provides:       tex(babel-uzbek-cyrl.tex) = %{tl_version}
Provides:       tex(babel-uzbek-latin.tex) = %{tl_version}
Provides:       tex(babel-uzbek-latn.tex) = %{tl_version}
Provides:       tex(babel-uzbek.tex) = %{tl_version}
Provides:       tex(babel-vai-latin.tex) = %{tl_version}
Provides:       tex(babel-vai-latn.tex) = %{tl_version}
Provides:       tex(babel-vai-vai.tex) = %{tl_version}
Provides:       tex(babel-vai-vaii.tex) = %{tl_version}
Provides:       tex(babel-vai.tex) = %{tl_version}
Provides:       tex(babel-venda.tex) = %{tl_version}
Provides:       tex(babel-venetian.tex) = %{tl_version}
Provides:       tex(babel-vietnamese.tex) = %{tl_version}
Provides:       tex(babel-volapuk.tex) = %{tl_version}
Provides:       tex(babel-vunjo.tex) = %{tl_version}
Provides:       tex(babel-walser.tex) = %{tl_version}
Provides:       tex(babel-waray.tex) = %{tl_version}
Provides:       tex(babel-welsh.tex) = %{tl_version}
Provides:       tex(babel-westernfrisian.tex) = %{tl_version}
Provides:       tex(babel-wolaytta.tex) = %{tl_version}
Provides:       tex(babel-wolof.tex) = %{tl_version}
Provides:       tex(babel-xhosa.tex) = %{tl_version}
Provides:       tex(babel-yangben.tex) = %{tl_version}
Provides:       tex(babel-yiddish.tex) = %{tl_version}
Provides:       tex(babel-yoruba.tex) = %{tl_version}
Provides:       tex(babel-zarma.tex) = %{tl_version}
Provides:       tex(babel-zhuang.tex) = %{tl_version}
Provides:       tex(babel-zulu.tex) = %{tl_version}
Provides:       tex(babel.def) = %{tl_version}
Provides:       tex(babel.sty) = %{tl_version}
Provides:       tex(bahasa.sty) = %{tl_version}
Provides:       tex(bahasam.sty) = %{tl_version}
Provides:       tex(basque.sty) = %{tl_version}
Provides:       tex(blplain.tex) = %{tl_version}
Provides:       tex(bplain.tex) = %{tl_version}
Provides:       tex(breton.sty) = %{tl_version}
Provides:       tex(british.sty) = %{tl_version}
Provides:       tex(bulgarian.sty) = %{tl_version}
Provides:       tex(catalan.sty) = %{tl_version}
Provides:       tex(croatian.sty) = %{tl_version}
Provides:       tex(czech.sty) = %{tl_version}
Provides:       tex(danish.sty) = %{tl_version}
Provides:       tex(dutch.sty) = %{tl_version}
Provides:       tex(english.sty) = %{tl_version}
Provides:       tex(errbabel.def) = %{tl_version}
Provides:       tex(esperanto.sty) = %{tl_version}
Provides:       tex(estonian.sty) = %{tl_version}
Provides:       tex(finnish.sty) = %{tl_version}
Provides:       tex(francais.sty) = %{tl_version}
Provides:       tex(galician.sty) = %{tl_version}
Provides:       tex(germanb.sty) = %{tl_version}
Provides:       tex(greek.sty) = %{tl_version}
Provides:       tex(hebrew.sty) = %{tl_version}
Provides:       tex(icelandic.sty) = %{tl_version}
Provides:       tex(interlingua.sty) = %{tl_version}
Provides:       tex(irish.sty) = %{tl_version}
Provides:       tex(italian.sty) = %{tl_version}
Provides:       tex(latin.sty) = %{tl_version}
Provides:       tex(lsorbian.sty) = %{tl_version}
Provides:       tex(luababel.def) = %{tl_version}
Provides:       tex(magyar.sty) = %{tl_version}
Provides:       tex(naustrian.sty) = %{tl_version}
Provides:       tex(ngermanb.sty) = %{tl_version}
Provides:       tex(nil.ldf) = %{tl_version}
Provides:       tex(norsk.sty) = %{tl_version}
Provides:       tex(plain.def) = %{tl_version}
Provides:       tex(polish.sty) = %{tl_version}
Provides:       tex(portuges.sty) = %{tl_version}
Provides:       tex(romanian.sty) = %{tl_version}
Provides:       tex(russianb.sty) = %{tl_version}
Provides:       tex(samin.sty) = %{tl_version}
Provides:       tex(scottish.sty) = %{tl_version}
Provides:       tex(serbian.sty) = %{tl_version}
Provides:       tex(slovak.sty) = %{tl_version}
Provides:       tex(slovene.sty) = %{tl_version}
Provides:       tex(spanish.sty) = %{tl_version}
Provides:       tex(swedish.sty) = %{tl_version}
Provides:       tex(switch.def) = %{tl_version}
Provides:       tex(turkish.sty) = %{tl_version}
Provides:       tex(txtbabel.def) = %{tl_version}
Provides:       tex(ukraineb.sty) = %{tl_version}
Provides:       tex(usorbian.sty) = %{tl_version}
Provides:       tex(welsh.sty) = %{tl_version}
Provides:       tex(xebabel.def) = %{tl_version}

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
Version:        svn70799
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyphen-english
Provides:       tex(UKenglish.ldf) = %{tl_version}
Provides:       tex(USenglish.ldf) = %{tl_version}
Provides:       tex(american.ldf) = %{tl_version}
Provides:       tex(australian.ldf) = %{tl_version}
Provides:       tex(british.ldf) = %{tl_version}
Provides:       tex(canadian.ldf) = %{tl_version}
Provides:       tex(english.ldf) = %{tl_version}
Provides:       tex(newzealand.ldf) = %{tl_version}

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
Requires:       tex(babel.sty)
Provides:       tex(babelbib.sty) = %{tl_version}

%description -n texlive-babelbib
This package enables the user to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each citation may be
written in another language, or the whole bibliography can be typeset in a
language chosen by the user. In addition, the package supports commands to
change the typography of the bibliographies.

%package -n texlive-bigintcalc
Summary:        Integer calculations on very large numbers
Version:        svn53172
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pdftexcmds.sty)
Provides:       tex(bigintcalc.sty) = %{tl_version}

%description -n texlive-bigintcalc
This package provides expandable arithmetic operations with big integers that
can exceed TeX's number limits.

%package -n texlive-bitset
Summary:        Handle bit-vector datatype
Version:        svn53837
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-bigintcalc
Requires:       tex(bigintcalc.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(intcalc.sty)
Provides:       tex(bitset.sty) = %{tl_version}

%description -n texlive-bitset
This package defines and implements the data type bit set, a vector of bits.
The size of the vector may grow dynamically. Individual bits can be
manipulated.

%package -n texlive-bookmark
Summary:        A new bookmark (outline) organization for hyperref
Version:        svn69084
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Provides:       tex(bkm-dvipdfm.def) = %{tl_version}
Provides:       tex(bkm-dvips.def) = %{tl_version}
Provides:       tex(bkm-pdftex.def) = %{tl_version}
Provides:       tex(bkm-vtex.def) = %{tl_version}
Provides:       tex(bookmark.sty) = %{tl_version}

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
Requires:       tex(color.sty)
Requires:       tex(longtable.sty)
Requires:       tex(tabularx.sty)
Provides:       tex(dotlessj.sty) = %{tl_version}
Provides:       tex(ltxtable.sty) = %{tl_version}
Provides:       tex(plain.sty) = %{tl_version}
Provides:       tex(remreset.sty) = %{tl_version}
Provides:       tex(scalefnt.sty) = %{tl_version}
Provides:       tex(slashed.sty) = %{tl_version}

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
Version:        svn75287
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(color.sty)
Provides:       tex(colortbl.sty) = %{tl_version}

%description -n texlive-colortbl
The package allows rows and columns to be coloured, and even individual cells.

%package -n texlive-epstopdf-pkg
Summary:        Call epstopdf "on the fly"
Version:        svn71084
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf
Requires:       tex(grfext.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(epstopdf-base.sty) = %{tl_version}
Provides:       tex(epstopdf.sty) = %{tl_version}

%description -n texlive-epstopdf-pkg
The package adds support for EPS files in the graphicx package when running
under pdfTeX. If an EPS graphic is detected, the package spawns a process to
convert the EPS to PDF, using the script epstopdf. This of course requires that
shell escape is enabled for the pdfTeX run.

%package -n texlive-etexcmds
Summary:        Avoid name clashes with e-TeX commands
Version:        svn53171
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Provides:       tex(etexcmds.sty) = %{tl_version}

%description -n texlive-etexcmds
New primitive commands are introduced in e-TeX; sometimes the names collide
with existing macros. This package solves the name clashes by adding a prefix
to e-TeX's commands. For example, eTeX's \unexpanded is provided as
\etex@unexpanded.

%package -n texlive-etoolbox
Summary:        E-TeX tools for LaTeX
Version:        svn76474
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Provides:       tex(etoolbox.def) = %{tl_version}
Provides:       tex(etoolbox.sty) = %{tl_version}

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
Version:        svn73783
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(extramarks-v4.sty) = %{tl_version}
Provides:       tex(extramarks.sty) = %{tl_version}
Provides:       tex(fancyhdr.sty) = %{tl_version}
Provides:       tex(fancyheadings.sty) = %{tl_version}

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
Provides:       tex(filehook-ltx.sty) = %{tl_version}
Provides:       tex(underscore-ltx.sty) = %{tl_version}

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
Provides:       tex(fix2col.sty) = %{tl_version}

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
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-graphics
Requires:       texlive-iftex
Requires:       tex(atbegshi.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(keyval.sty)
Provides:       tex(geometry.sty) = %{tl_version}

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
Version:        svn53170
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(gettitlestring.sty) = %{tl_version}

%description -n texlive-gettitlestring
Cleans up the title string (removing \label commands) for packages (such as
nameref) that typeset such strings.

%package -n texlive-graphics
Summary:        The LaTeX standard graphics bundle
Version:        svn75374
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-graphics-cfg
Requires:       texlive-graphics-def
Requires:       tex(ifthen.sty)
Provides:       tex(color.sty) = %{tl_version}
Provides:       tex(dvipdf.def) = %{tl_version}
Provides:       tex(dvipsnam.def) = %{tl_version}
Provides:       tex(dvipsone.def) = %{tl_version}
Provides:       tex(dviwin.def) = %{tl_version}
Provides:       tex(emtex.def) = %{tl_version}
Provides:       tex(epsfig.sty) = %{tl_version}
Provides:       tex(graphics-2017-06-25.sty) = %{tl_version}
Provides:       tex(graphics.sty) = %{tl_version}
Provides:       tex(graphicx.sty) = %{tl_version}
Provides:       tex(keyval.sty) = %{tl_version}
Provides:       tex(lscape.sty) = %{tl_version}
Provides:       tex(pctex32.def) = %{tl_version}
Provides:       tex(pctexhp.def) = %{tl_version}
Provides:       tex(pctexps.def) = %{tl_version}
Provides:       tex(pctexwin.def) = %{tl_version}
Provides:       tex(rotating.sty) = %{tl_version}
Provides:       tex(tcidvi.def) = %{tl_version}
Provides:       tex(trig.sty) = %{tl_version}
Provides:       tex(truetex.def) = %{tl_version}

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

%description -n texlive-graphics-cfg
This bundle includes color.cfg and graphics.cfg files that set default "driver"
options for the color and graphics packages. It contains support for defaulting
the new LuaTeX option which was added to graphics and color in the 2016-02-01
release. The LuaTeX option is only used for LuaTeX versions from 0.87, older
versions use the pdfTeX option as before.

%package -n texlive-grfext
Summary:        Manipulate the graphics package's list of extensions
Version:        svn53024
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(kvdefinekeys.sty)
Provides:       tex(grfext.sty) = %{tl_version}

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
Provides:       tex(hopatch-2016-05-16.sty) = %{tl_version}
Provides:       tex(hopatch.sty) = %{tl_version}

%description -n texlive-hopatch
Hopatch provides a command with which the user may register of patch code for a
particular package. Hopatch will apply the patch immediately, if the relevant
package has already been loaded; otherwise it will store the patch until the
package appears.

%package -n texlive-hycolor
Summary:        Implements colour for packages hyperref and bookmark
Version:        svn53584
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hopatch.sty)
Provides:       tex(hycolor.sty) = %{tl_version}
Provides:       tex(xcolor-patch.sty) = %{tl_version}

%description -n texlive-hycolor
This package provides the code for the color option that is used by packages
hyperref and bookmark. It is not intended as package for the user.

%package -n texlive-hypcap
Summary:        Adjusting the anchors of captions
Version:        svn71912
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(letltxmacro.sty)
Provides:       tex(hypcap.sty) = %{tl_version}

%description -n texlive-hypcap
The package offers a solution to the problem that when you link to a float
using hyperref, the link anchors to below the float's caption, rather than the
beginning of the float. Hypcap defines a separate \capstart command, which you
put where you want links to end; you should have a \capstart command for each
\caption command. Package options can be used to auto-insert a \capstart at the
start of a float environment.

%package -n texlive-hyperref
Summary:        Extensive support for hypertext in LaTeX
Version:        svn75759
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
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
Provides:       tex(backref.sty) = %{tl_version}
Provides:       tex(hdvipdfm.def) = %{tl_version}
Provides:       tex(hdvips.def) = %{tl_version}
Provides:       tex(hdvipson.def) = %{tl_version}
Provides:       tex(hdviwind.def) = %{tl_version}
Provides:       tex(hluatex.def) = %{tl_version}
Provides:       tex(hpdftex.def) = %{tl_version}
Provides:       tex(htex4ht.def) = %{tl_version}
Provides:       tex(htexture.def) = %{tl_version}
Provides:       tex(hvtex.def) = %{tl_version}
Provides:       tex(hvtexhtm.def) = %{tl_version}
Provides:       tex(hvtexmrk.def) = %{tl_version}
Provides:       tex(hxetex.def) = %{tl_version}
Provides:       tex(hyperref-patches.sty) = %{tl_version}
Provides:       tex(hyperref.sty) = %{tl_version}
Provides:       tex(hypertex.def) = %{tl_version}
Provides:       tex(minitoc-hyper.sty) = %{tl_version}
Provides:       tex(nameref.sty) = %{tl_version}
Provides:       tex(nohyperref.sty) = %{tl_version}
Provides:       tex(ntheorem-hyper.sty) = %{tl_version}
Provides:       tex(pd1enc.def) = %{tl_version}
Provides:       tex(pdfmark.def) = %{tl_version}
Provides:       tex(psdextra.def) = %{tl_version}
Provides:       tex(puarenc.def) = %{tl_version}
Provides:       tex(puenc-extra.def) = %{tl_version}
Provides:       tex(puenc.def) = %{tl_version}
Provides:       tex(puvnenc.def) = %{tl_version}
Provides:       tex(xr-hyper.sty) = %{tl_version}

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
Version:        svn53168
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(intcalc.sty) = %{tl_version}

%description -n texlive-intcalc
This package provides expandable arithmetic operations with integers, using the
e-TeX extension \numexpr if it is available.

%package -n texlive-kvdefinekeys
Summary:        Define keys for use in the kvsetkeys package
Version:        svn53193
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kvdefinekeys.sty) = %{tl_version}

%description -n texlive-kvdefinekeys
The package provides a macro \kv@define@key (analogous to keyval's \define@key,
to define keys for use by kvsetkeys.

%package -n texlive-kvoptions
Summary:        Key value format for package options
Version:        svn63622
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etexcmds.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(kvoptions-patch.sty) = %{tl_version}
Provides:       tex(kvoptions.sty) = %{tl_version}

%description -n texlive-kvoptions
This package offers support for package authors who want to use options in
key-value format for their package options.

%package -n texlive-kvsetkeys
Summary:        Key value parser with default handler support
Version:        svn64632
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kvsetkeys.sty) = %{tl_version}

%description -n texlive-kvsetkeys
This package provides \kvsetkeys, a variant of package keyval's \setkeys. It
allows the user to specify a handler that deals with unknown options. Active
commas and equal signs may be used (e.g. see babel's shorthands) and only one
level of curly braces are removed from the values.

%package -n texlive-l3backend
Summary:        LaTeX3 backend drivers
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(l3backend-dvipdfmx.def) = %{tl_version}
Provides:       tex(l3backend-dvips.def) = %{tl_version}
Provides:       tex(l3backend-dvisvgm.def) = %{tl_version}
Provides:       tex(l3backend-luatex.def) = %{tl_version}
Provides:       tex(l3backend-pdftex.def) = %{tl_version}
Provides:       tex(l3backend-xetex.def) = %{tl_version}

%description -n texlive-l3backend
This package forms parts of expl3, and contains the code used to interface with
backends (drivers) across the expl3 codebase. The functions here are defined
differently depending on the engine in use. As such, these are distributed
separately from l3kernel to allow this code to be updated on an independent
schedule.

%package -n texlive-l3kernel
Summary:        LaTeX3 programming conventions
Version:        svn77438
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-l3backend
Requires:       texlive-lua-uni-algos
Provides:       tex(expl3-code.tex) = %{tl_version}
Provides:       tex(expl3-generic.tex) = %{tl_version}
Provides:       tex(expl3.sty) = %{tl_version}
Provides:       tex(l3debug.def) = %{tl_version}
Provides:       tex(l3docstrip.tex) = %{tl_version}
Provides:       tex(l3str-enc-iso88591.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885910.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885911.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885913.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885914.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885915.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885916.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88592.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88593.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88594.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88595.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88596.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88597.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88598.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88599.def) = %{tl_version}

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
Requires:       texlive-l3kernel
Provides:       tex(l3keys2e.sty) = %{tl_version}
Provides:       tex(xfp.sty) = %{tl_version}
Provides:       tex(xparse-2018-04-12.sty) = %{tl_version}
Provides:       tex(xparse-2020-10-01.sty) = %{tl_version}
Provides:       tex(xparse-generic.tex) = %{tl_version}
Provides:       tex(xparse.sty) = %{tl_version}
Provides:       tex(xtemplate-2023-10-10.sty) = %{tl_version}
Provides:       tex(xtemplate.sty) = %{tl_version}

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
Provides:       tex(glyphtounicode-cmex.tex) = %{tl_version}
Provides:       tex(latex-lab-kernel-changes.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-bib.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-block.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-context.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-firstaid.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-float.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-graphic.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-l3doc.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-latest.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-marginpar.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-math.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-minipage.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-names.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-new-or-1.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-new-or-2.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-sec.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-table.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-text.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-tikz.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-title.sty) = %{tl_version}
Provides:       tex(latex-lab-testphase-toc.sty) = %{tl_version}
Provides:       tex(tagpdf-ns-latex-lab.def) = %{tl_version}

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
Provides:       tex(lualatexiniconfig.tex) = %{tl_version}

%description -n texlive-latexconfig
configuration files for LaTeX-related formats

%package -n texlive-letltxmacro
Summary:        Let assignment for LaTeX macros
Version:        svn53022
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(letltxmacro.sty) = %{tl_version}

%description -n texlive-letltxmacro
TeX's \let assignment does not work for LaTeX macros with optional arguments or
for macros that are defined as robust macros by \DeclareRobustCommand. This
package defines \LetLtxMacro that also takes care of the involved internal
macros.

%package -n texlive-ltxcmds
Summary:        Some LaTeX kernel commands for general use
Version:        svn69032
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ltxcmds.sty) = %{tl_version}

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
Provides:       tex(bibcheck.sty) = %{tl_version}
Provides:       tex(concrete.sty) = %{tl_version}
Provides:       tex(linsys.sty) = %{tl_version}
Provides:       tex(mitpress.sty) = %{tl_version}
Provides:       tex(thrmappendix.sty) = %{tl_version}
Provides:       tex(topcapt.sty) = %{tl_version}
Provides:       tex(vrbexin.sty) = %{tl_version}

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
Version:        svn46036
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(oldgerm.sty) = %{tl_version}
Provides:       tex(pandora.sty) = %{tl_version}

%description -n texlive-mfnfss
This bundle contains two packages: - oldgerm, a package to typeset with old
german fonts designed by Yannis Haralambous. - pandora, a package to typeset
with Pandora fonts designed by Neena Billawala. Note that support for the
Pandora fonts is also available via the pandora-latex package.

%package -n texlive-natbib
Summary:        Flexible bibliography support
Version:        svn20668
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(citeref.sty)
Provides:       tex(bibentry.sty) = %{tl_version}
Provides:       tex(natbib.sty) = %{tl_version}

%description -n texlive-natbib
The bundle provides a package that implements both author-year and numbered
references, as well as much detailed of support for other bibliography use.
Also Provided are versions of the standard BibTeX styles that are compatible
with natbib--plainnat, unsrtnat, abbrnat. The bibliography styles produced by
custom-bib are designed from the start to be compatible with natbib.

%package -n texlive-pagesel
Summary:        Select pages of a document for output
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(everyshi.sty)
Provides:       tex(pagesel-2016-05-16.sty) = %{tl_version}
Provides:       tex(pagesel.sty) = %{tl_version}

%description -n texlive-pagesel
Selects single pages, ranges of pages, odd pages or even pages for output.

%package -n texlive-pdfescape
Summary:        Implements pdfTeX's escape features using TeX or e-TeX
Version:        svn53082
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(pdfescape.sty) = %{tl_version}

%description -n texlive-pdfescape
This package implements pdfTeX's escape features (\pdfescapehex,
\pdfunescapehex, \pdfescapename, \pdfescapestring) using TeX or e-TeX.

%package -n texlive-pdftexcmds
Summary:        LuaTeX support for pdfTeX utility functions
Version:        svn55777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(pdftexcmds.sty) = %{tl_version}

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
Provides:       tex(pslatex.sty) = %{tl_version}

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
Version:        svn54694
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-symbol
Requires:       texlive-zapfding
Requires:       texlive-graphics
Requires:       tex(keyval.sty)
Provides:       tex(avant.sty) = %{tl_version}
Provides:       tex(bookman.sty) = %{tl_version}
Provides:       tex(chancery.sty) = %{tl_version}
Provides:       tex(charter.sty) = %{tl_version}
Provides:       tex(courier.sty) = %{tl_version}
Provides:       tex(helvet.sty) = %{tl_version}
Provides:       tex(mathpazo.sty) = %{tl_version}
Provides:       tex(mathpple.sty) = %{tl_version}
Provides:       tex(mathptm.sty) = %{tl_version}
Provides:       tex(mathptmx.sty) = %{tl_version}
Provides:       tex(newcent.sty) = %{tl_version}
Provides:       tex(palatino.sty) = %{tl_version}
Provides:       tex(pifont.sty) = %{tl_version}
Provides:       tex(times.sty) = %{tl_version}
Provides:       tex(utopia.sty) = %{tl_version}

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
Provides:       tex(pspicture.sty) = %{tl_version}

%description -n texlive-pspicture
A replacement for LaTeX's picture macros, that uses PostScript \special
commands. The package is now largely superseded by pict2e.

%package -n texlive-refcount
Summary:        Counter operations with label references
Version:        svn53164
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(refcount.sty) = %{tl_version}

%description -n texlive-refcount
Provides commands \setcounterref and \addtocounterref which use the section (or
whatever) number from the reference as the value to put into the counter, as
in: ...\label{sec:foo} ... \setcounterref{foonum}{sec:foo} Commands
\setcounterpageref and \addtocounterpageref do the corresponding thing with the
page reference of the label. No .ins file is distributed; process the .dtx with
plain TeX to create one.

%package -n texlive-rerunfilecheck
Summary:        Checksum based rerun checks on auxiliary files
Version:        svn75559
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-atveryend
Requires:       texlive-uniquecounter
Requires:       tex(infwarerr.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(uniquecounter.sty)
Provides:       tex(rerunfilecheck.sty) = %{tl_version}

%description -n texlive-rerunfilecheck
The package provides additional rerun warnings if some auxiliary files have
changed. It is based on MD5 checksum provided by pdfTeX, LuaTeX, XeTeX.

%package -n texlive-stringenc
Summary:        Converting a string between different encodings
Version:        svn52982
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdfescape.sty)
Provides:       tex(se-ascii-print.def) = %{tl_version}
Provides:       tex(se-ascii.def) = %{tl_version}
Provides:       tex(se-clean7bit.def) = %{tl_version}
Provides:       tex(se-cp1250.def) = %{tl_version}
Provides:       tex(se-cp1251.def) = %{tl_version}
Provides:       tex(se-cp1252.def) = %{tl_version}
Provides:       tex(se-cp1257.def) = %{tl_version}
Provides:       tex(se-cp437.def) = %{tl_version}
Provides:       tex(se-cp850.def) = %{tl_version}
Provides:       tex(se-cp852.def) = %{tl_version}
Provides:       tex(se-cp855.def) = %{tl_version}
Provides:       tex(se-cp858.def) = %{tl_version}
Provides:       tex(se-cp865.def) = %{tl_version}
Provides:       tex(se-cp866.def) = %{tl_version}
Provides:       tex(se-dec-mcs.def) = %{tl_version}
Provides:       tex(se-iso-8859-1.def) = %{tl_version}
Provides:       tex(se-iso-8859-10.def) = %{tl_version}
Provides:       tex(se-iso-8859-11.def) = %{tl_version}
Provides:       tex(se-iso-8859-13.def) = %{tl_version}
Provides:       tex(se-iso-8859-14.def) = %{tl_version}
Provides:       tex(se-iso-8859-15.def) = %{tl_version}
Provides:       tex(se-iso-8859-16.def) = %{tl_version}
Provides:       tex(se-iso-8859-2.def) = %{tl_version}
Provides:       tex(se-iso-8859-3.def) = %{tl_version}
Provides:       tex(se-iso-8859-4.def) = %{tl_version}
Provides:       tex(se-iso-8859-5.def) = %{tl_version}
Provides:       tex(se-iso-8859-6.def) = %{tl_version}
Provides:       tex(se-iso-8859-7.def) = %{tl_version}
Provides:       tex(se-iso-8859-8.def) = %{tl_version}
Provides:       tex(se-iso-8859-9.def) = %{tl_version}
Provides:       tex(se-koi8-r.def) = %{tl_version}
Provides:       tex(se-mac-centeuro.def) = %{tl_version}
Provides:       tex(se-mac-cyrillic.def) = %{tl_version}
Provides:       tex(se-mac-roman.def) = %{tl_version}
Provides:       tex(se-nextstep.def) = %{tl_version}
Provides:       tex(se-pdfdoc.def) = %{tl_version}
Provides:       tex(se-utf16le.def) = %{tl_version}
Provides:       tex(se-utf32be.def) = %{tl_version}
Provides:       tex(se-utf32le.def) = %{tl_version}
Provides:       tex(se-utf8.def) = %{tl_version}
Provides:       tex(stringenc.sty) = %{tl_version}

%description -n texlive-stringenc
This package provides \StringEncodingConvert for converting a string between
different encodings. Both LaTeX and plain-TeX are supported.

%package -n texlive-tools
Summary:        The LaTeX standard tools bundle
Version:        svn76708
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(.tex) = %{tl_version}
Provides:       tex(afterpage.sty) = %{tl_version}
Provides:       tex(array-2016-10-06.sty) = %{tl_version}
Provides:       tex(array-2020-02-10.sty) = %{tl_version}
Provides:       tex(array-2023-11-01.sty) = %{tl_version}
Provides:       tex(array.sty) = %{tl_version}
Provides:       tex(bm.sty) = %{tl_version}
Provides:       tex(calc.sty) = %{tl_version}
Provides:       tex(dcolumn.sty) = %{tl_version}
Provides:       tex(delarray.sty) = %{tl_version}
Provides:       tex(e.tex) = %{tl_version}
Provides:       tex(enumerate.sty) = %{tl_version}
Provides:       tex(fontsmpl.sty) = %{tl_version}
Provides:       tex(fontsmpl.tex) = %{tl_version}
Provides:       tex(ftnright.sty) = %{tl_version}
Provides:       tex(h.tex) = %{tl_version}
Provides:       tex(hhline.sty) = %{tl_version}
Provides:       tex(indentfirst.sty) = %{tl_version}
Provides:       tex(l3sys-query.sty) = %{tl_version}
Provides:       tex(layout.sty) = %{tl_version}
Provides:       tex(longtable-2020-01-07.sty) = %{tl_version}
Provides:       tex(longtable.sty) = %{tl_version}
Provides:       tex(multicol-2017-04-11.sty) = %{tl_version}
Provides:       tex(multicol-2019-10-01.sty) = %{tl_version}
Provides:       tex(multicol-2024-05-23.sty) = %{tl_version}
Provides:       tex(multicol.sty) = %{tl_version}
Provides:       tex(q.tex) = %{tl_version}
Provides:       tex(r.tex) = %{tl_version}
Provides:       tex(rawfonts.sty) = %{tl_version}
Provides:       tex(s.tex) = %{tl_version}
Provides:       tex(shellesc.sty) = %{tl_version}
Provides:       tex(showkeys-2014-10-28.sty) = %{tl_version}
Provides:       tex(showkeys.sty) = %{tl_version}
Provides:       tex(somedefs.sty) = %{tl_version}
Provides:       tex(tabularx.sty) = %{tl_version}
Provides:       tex(thb.sty) = %{tl_version}
Provides:       tex(thc.sty) = %{tl_version}
Provides:       tex(thcb.sty) = %{tl_version}
Provides:       tex(theorem.sty) = %{tl_version}
Provides:       tex(thm.sty) = %{tl_version}
Provides:       tex(thmb.sty) = %{tl_version}
Provides:       tex(thp.sty) = %{tl_version}
Provides:       tex(trace.sty) = %{tl_version}
Provides:       tex(varioref-2016-02-16.sty) = %{tl_version}
Provides:       tex(varioref.sty) = %{tl_version}
Provides:       tex(verbatim.sty) = %{tl_version}
Provides:       tex(verbtest.tex) = %{tl_version}
Provides:       tex(x.tex) = %{tl_version}
Provides:       tex(xr-2023-07-04.sty) = %{tl_version}
Provides:       tex(xr.sty) = %{tl_version}
Provides:       tex(xspace.sty) = %{tl_version}

%description -n texlive-tools
A collection of (variously) simple tools provided as part of the LaTeX required
tools distribution, comprising the packages: afterpage, array, bm, calc,
dcolumn, delarray, enumerate, fileerr, fontsmpl, ftnright, hhline, indentfirst,
layout, longtable, multicol, rawfonts, shellesc, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%package -n texlive-uniquecounter
Summary:        Provides unlimited unique counter
Version:        svn53162
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bigintcalc.sty)
Requires:       tex(infwarerr.sty)
Provides:       tex(uniquecounter.sty) = %{tl_version}

%description -n texlive-uniquecounter
This package provides a kind of counter that provides unique number values.
Several counters can be created with different names. The numeric values are
not limited.

%package -n texlive-url
Summary:        Verbatim with URL-sensitive line breaks
Version:        svn32528
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(url.sty) = %{tl_version}

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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

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
* Fri Jan 23 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77034-1
- Update to svn77034
- fix licensing tags
- update components to latest

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73720-2
- regen, no deps from docs

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73720-1
- Update to TeX Live 2025
