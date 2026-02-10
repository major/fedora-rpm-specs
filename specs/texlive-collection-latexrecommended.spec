%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-latexrecommended
Epoch:          12
Version:        svn77082
Release:        2%{?dist}
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
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmanagement-testphase.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfmanagement-testphase.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfpages.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfpages.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyglossia.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polyglossia.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psfrag.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psfrag.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ragged2e.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ragged2e.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rcs.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rcs.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmath.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sansmath.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/section.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/section.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seminar.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seminar.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sepnum.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sepnum.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/setspace.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/setspace.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subfig.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subfig.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textcase.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textcase.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translator.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translator.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typehtml.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typehtml.doc.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharcat.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ucharcat.doc.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/underscore.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/underscore.doc.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-math.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-math.doc.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcolor.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcolor.doc.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xfrac.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xfrac.doc.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xkeyval.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xkeyval.doc.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xltxtra.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xltxtra.doc.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xunicode.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xunicode.doc.tar.xz
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
Requires:       texlive-pdfmanagement-testphase
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
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(anysize.sty) = %{tl_version}

%description -n texlive-anysize
This package is considered obsolete; alternatives are the typearea package from
the koma-script bundle, or the geometry package.

%package -n texlive-beamer
Summary:        A LaTeX class for producing presentations and slides
Version:        svn77450
License:        LPPL-1.3c AND GPL-2.0-or-later AND GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
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
Provides:       tex(beamerarticle.sty) = %{tl_version}
Provides:       tex(beamerbasearticle.sty) = %{tl_version}
Provides:       tex(beamerbaseauxtemplates.sty) = %{tl_version}
Provides:       tex(beamerbaseboxes.sty) = %{tl_version}
Provides:       tex(beamerbasecolor.sty) = %{tl_version}
Provides:       tex(beamerbasecompatibility.sty) = %{tl_version}
Provides:       tex(beamerbasedecode.sty) = %{tl_version}
Provides:       tex(beamerbasefont.sty) = %{tl_version}
Provides:       tex(beamerbaseframe.sty) = %{tl_version}
Provides:       tex(beamerbaseframecomponents.sty) = %{tl_version}
Provides:       tex(beamerbaseframesize.sty) = %{tl_version}
Provides:       tex(beamerbaselocalstructure.sty) = %{tl_version}
Provides:       tex(beamerbasemisc.sty) = %{tl_version}
Provides:       tex(beamerbasemodes.sty) = %{tl_version}
Provides:       tex(beamerbasenavigation.sty) = %{tl_version}
Provides:       tex(beamerbasenavigationsymbols.tex) = %{tl_version}
Provides:       tex(beamerbasenotes.sty) = %{tl_version}
Provides:       tex(beamerbaseoptions.sty) = %{tl_version}
Provides:       tex(beamerbaseoverlay.sty) = %{tl_version}
Provides:       tex(beamerbaserequires.sty) = %{tl_version}
Provides:       tex(beamerbasesection.sty) = %{tl_version}
Provides:       tex(beamerbasetemplates.sty) = %{tl_version}
Provides:       tex(beamerbasethemes.sty) = %{tl_version}
Provides:       tex(beamerbasetheorems.sty) = %{tl_version}
Provides:       tex(beamerbasetitle.sty) = %{tl_version}
Provides:       tex(beamerbasetoc.sty) = %{tl_version}
Provides:       tex(beamerbasetranslator.sty) = %{tl_version}
Provides:       tex(beamerbasetwoscreens.sty) = %{tl_version}
Provides:       tex(beamerbaseverbatim.sty) = %{tl_version}
Provides:       tex(beamercolorthemealbatross.sty) = %{tl_version}
Provides:       tex(beamercolorthemebeaver.sty) = %{tl_version}
Provides:       tex(beamercolorthemebeetle.sty) = %{tl_version}
Provides:       tex(beamercolorthemecrane.sty) = %{tl_version}
Provides:       tex(beamercolorthemedefault.sty) = %{tl_version}
Provides:       tex(beamercolorthemedolphin.sty) = %{tl_version}
Provides:       tex(beamercolorthemedove.sty) = %{tl_version}
Provides:       tex(beamercolorthemefly.sty) = %{tl_version}
Provides:       tex(beamercolorthemelily.sty) = %{tl_version}
Provides:       tex(beamercolorthememonarca.sty) = %{tl_version}
Provides:       tex(beamercolorthemeorchid.sty) = %{tl_version}
Provides:       tex(beamercolorthemerose.sty) = %{tl_version}
Provides:       tex(beamercolorthemeseagull.sty) = %{tl_version}
Provides:       tex(beamercolorthemeseahorse.sty) = %{tl_version}
Provides:       tex(beamercolorthemesidebartab.sty) = %{tl_version}
Provides:       tex(beamercolorthemespruce.sty) = %{tl_version}
Provides:       tex(beamercolorthemestructure.sty) = %{tl_version}
Provides:       tex(beamercolorthemewhale.sty) = %{tl_version}
Provides:       tex(beamercolorthemewolverine.sty) = %{tl_version}
Provides:       tex(beamerfoils.sty) = %{tl_version}
Provides:       tex(beamerfontthemedefault.sty) = %{tl_version}
Provides:       tex(beamerfontthemeprofessionalfonts.sty) = %{tl_version}
Provides:       tex(beamerfontthemeserif.sty) = %{tl_version}
Provides:       tex(beamerfontthemestructurebold.sty) = %{tl_version}
Provides:       tex(beamerfontthemestructureitalicserif.sty) = %{tl_version}
Provides:       tex(beamerfontthemestructuresmallcapsserif.sty) = %{tl_version}
Provides:       tex(beamericonarticle.tex) = %{tl_version}
Provides:       tex(beamericonbook.tex) = %{tl_version}
Provides:       tex(beamerinnerthemecircles.sty) = %{tl_version}
Provides:       tex(beamerinnerthemedefault.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeinmargin.sty) = %{tl_version}
Provides:       tex(beamerinnerthemerectangles.sty) = %{tl_version}
Provides:       tex(beamerinnerthemerounded.sty) = %{tl_version}
Provides:       tex(beamerouterthemedefault.sty) = %{tl_version}
Provides:       tex(beamerouterthemeinfolines.sty) = %{tl_version}
Provides:       tex(beamerouterthememiniframes.sty) = %{tl_version}
Provides:       tex(beamerouterthemeshadow.sty) = %{tl_version}
Provides:       tex(beamerouterthemesidebar.sty) = %{tl_version}
Provides:       tex(beamerouterthemesmoothbars.sty) = %{tl_version}
Provides:       tex(beamerouterthemesmoothtree.sty) = %{tl_version}
Provides:       tex(beamerouterthemesplit.sty) = %{tl_version}
Provides:       tex(beamerouterthemetree.sty) = %{tl_version}
Provides:       tex(beamerpatchparalist.sty) = %{tl_version}
Provides:       tex(beamerprosper.sty) = %{tl_version}
Provides:       tex(beamerseminar.sty) = %{tl_version}
Provides:       tex(beamertexpower.sty) = %{tl_version}
Provides:       tex(beamerthemeAnnArbor.sty) = %{tl_version}
Provides:       tex(beamerthemeAntibes.sty) = %{tl_version}
Provides:       tex(beamerthemeBergen.sty) = %{tl_version}
Provides:       tex(beamerthemeBerkeley.sty) = %{tl_version}
Provides:       tex(beamerthemeBerlin.sty) = %{tl_version}
Provides:       tex(beamerthemeBoadilla.sty) = %{tl_version}
Provides:       tex(beamerthemeCambridgeUS.sty) = %{tl_version}
Provides:       tex(beamerthemeCopenhagen.sty) = %{tl_version}
Provides:       tex(beamerthemeDarmstadt.sty) = %{tl_version}
Provides:       tex(beamerthemeDresden.sty) = %{tl_version}
Provides:       tex(beamerthemeEastLansing.sty) = %{tl_version}
Provides:       tex(beamerthemeFrankfurt.sty) = %{tl_version}
Provides:       tex(beamerthemeGoettingen.sty) = %{tl_version}
Provides:       tex(beamerthemeHannover.sty) = %{tl_version}
Provides:       tex(beamerthemeIlmenau.sty) = %{tl_version}
Provides:       tex(beamerthemeJuanLesPins.sty) = %{tl_version}
Provides:       tex(beamerthemeLuebeck.sty) = %{tl_version}
Provides:       tex(beamerthemeMadrid.sty) = %{tl_version}
Provides:       tex(beamerthemeMalmoe.sty) = %{tl_version}
Provides:       tex(beamerthemeMarburg.sty) = %{tl_version}
Provides:       tex(beamerthemeMontpellier.sty) = %{tl_version}
Provides:       tex(beamerthemePaloAlto.sty) = %{tl_version}
Provides:       tex(beamerthemePittsburgh.sty) = %{tl_version}
Provides:       tex(beamerthemeRochester.sty) = %{tl_version}
Provides:       tex(beamerthemeSingapore.sty) = %{tl_version}
Provides:       tex(beamerthemeSzeged.sty) = %{tl_version}
Provides:       tex(beamerthemeWarsaw.sty) = %{tl_version}
Provides:       tex(beamerthemebars.sty) = %{tl_version}
Provides:       tex(beamerthemeboxes.sty) = %{tl_version}
Provides:       tex(beamerthemeclassic.sty) = %{tl_version}
Provides:       tex(beamerthemecompatibility.sty) = %{tl_version}
Provides:       tex(beamerthemedefault.sty) = %{tl_version}
Provides:       tex(beamerthemelined.sty) = %{tl_version}
Provides:       tex(beamerthemeplain.sty) = %{tl_version}
Provides:       tex(beamerthemeshadow.sty) = %{tl_version}
Provides:       tex(beamerthemesidebar.sty) = %{tl_version}
Provides:       tex(beamerthemesplit.sty) = %{tl_version}
Provides:       tex(beamerthemetree.sty) = %{tl_version}
Provides:       tex(multimedia.sty) = %{tl_version}
Provides:       tex(multimediasymbols.sty) = %{tl_version}
Provides:       tex(xmpmulti.sty) = %{tl_version}

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
Version:        svn53402
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(booktabs.sty) = %{tl_version}

%description -n texlive-booktabs
The package enhances the quality of tables in LaTeX, providing extra commands
as well as behind-the-scenes optimisation. Guidelines are given as to what
constitutes a good table in this context. From version 1.61, the package offers
longtable compatibility.

%package -n texlive-breqn
Summary:        Automatic line breaking of displayed equations
Version:        svn60881
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Provides:       tex(breqn.sty) = %{tl_version}
Provides:       tex(flexisym.sty) = %{tl_version}
Provides:       tex(mathstyle.sty) = %{tl_version}

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
Version:        svn68425
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(newfloat.sty)
Provides:       tex(bicaption.sty) = %{tl_version}
Provides:       tex(caption-light.sty) = %{tl_version}
Provides:       tex(caption.sty) = %{tl_version}
Provides:       tex(caption2.sty) = %{tl_version}
Provides:       tex(caption2_1995-10-09.sty) = %{tl_version}
Provides:       tex(caption2_2005-10-03.sty) = %{tl_version}
Provides:       tex(caption3.sty) = %{tl_version}
Provides:       tex(caption3_2007-04-11.sty) = %{tl_version}
Provides:       tex(caption3_2010-01-14.sty) = %{tl_version}
Provides:       tex(caption3_2011-11-01.sty) = %{tl_version}
Provides:       tex(caption3_2019-09-01.sty) = %{tl_version}
Provides:       tex(caption3_2020-07-29.sty) = %{tl_version}
Provides:       tex(caption3_2020-10-26.sty) = %{tl_version}
Provides:       tex(caption_1995-04-05.sty) = %{tl_version}
Provides:       tex(caption_2007-04-16.sty) = %{tl_version}
Provides:       tex(caption_2010-01-09.sty) = %{tl_version}
Provides:       tex(caption_2011-11-10.sty) = %{tl_version}
Provides:       tex(caption_2019-09-01.sty) = %{tl_version}
Provides:       tex(caption_2020-07-29.sty) = %{tl_version}
Provides:       tex(caption_2020-10-26.sty) = %{tl_version}
Provides:       tex(ltcaption.sty) = %{tl_version}
Provides:       tex(subcaption.sty) = %{tl_version}

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
Version:        svn36428
License:        Borceux
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chapterbib.sty) = %{tl_version}
Provides:       tex(cite.sty) = %{tl_version}
Provides:       tex(drftcite.sty) = %{tl_version}
Provides:       tex(overcite.sty) = %{tl_version}

%description -n texlive-cite
The package supports compressed, sorted lists of numerical citations, and also
deals with various punctuation and other issues of representation, including
comprehensive management of break points. The package is compatible with both
hyperref and backref. The package is (unsurprisingly) part of the cite bundle
of the author's citation-related packages.

%package -n texlive-cmap
Summary:        Make PDF files searchable and copyable
Version:        svn57640
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cmap.sty) = %{tl_version}

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
Version:        svn55424
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifluatex.sty)
Provides:       tex(crop.sty) = %{tl_version}

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
Version:        svn76639
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(rotating.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(transparent.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(ctable.sty) = %{tl_version}

%description -n texlive-ctable
Provides commands to typeset centered, left- or right-aligned table and
(multiple-)figure floats, with footnotes. Instead of an environment, a command
with 4 arguments is used; the first is optional and is used for key,value pairs
generating variations on the defaults and offering a route for future
extensions.

%package -n texlive-eso-pic
Summary:        Add picture commands (or backgrounds) to every page
Version:        svn77066
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(eso-pic.sty) = %{tl_version}
Provides:       tex(showframe.sty) = %{tl_version}

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
Provides:       tex(eu1enc.def) = %{tl_version}
Provides:       tex(eu2enc.def) = %{tl_version}

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
Version:        svn42428
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(euler.sty) = %{tl_version}

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
Provides:       tex(everysel-2011-10-28.sty) = %{tl_version}
Provides:       tex(everysel.sty) = %{tl_version}

%description -n texlive-everysel
The package provided hooks whose arguments are executed just after LaTeX has
loaded a new font by means of \selectfont. It has become obsolete with LaTeX
versions 2021/01/05 or newer, since LaTeX now provides its own hooks to fulfill
this task. For newer versions of LaTeX everysel only provides macros using
LaTeX's hook management due to compatibility reasons. See lthooks-doc.pdf for
instructions how to use lthooks instead of everysel.

%package -n texlive-everyshi
Summary:        Take action at every \shipout
Version:        svn57001
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(everyshi-2001-05-15.sty) = %{tl_version}
Provides:       tex(everyshi.sty) = %{tl_version}

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
Version:        svn17263
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(autopagewidth.sty) = %{tl_version}
Provides:       tex(extsizes.sty) = %{tl_version}

%description -n texlive-extsizes
Provides classes extarticle, extreport, extletter, extbook and extproc which
provide for documents with a base font size from 8-20pt. There is also a LaTeX
package, extsizes.sty, which can be used with nonstandard document classes. But
it cannot be guaranteed to work with any given class.

%package -n texlive-fancybox
Summary:        Variants of \fbox and other games with boxes
Version:        svn18304
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fancybox.sty) = %{tl_version}

%description -n texlive-fancybox
Provides variants of \fbox: \shadowbox, \doublebox, \ovalbox, \Ovalbox, with
helpful tools for using box macros and flexible verbatim macros. You can box
mathematics, floats, center, flushleft, and flushright, lists, and pages.

%package -n texlive-fancyref
Summary:        A LaTeX package for fancy cross-referencing
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(varioref.sty)
Provides:       tex(fancyref.sty) = %{tl_version}

%description -n texlive-fancyref
Provides fancy cross-referencing support, based on the package's reference
commands (\fref and \Fref) that recognise what sort of object is being
referenced. So, for example, the label for a \section would be expected to be
of the form 'sec:foo': the package would recognise the 'sec:' part.

%package -n texlive-fancyvrb
Summary:        Sophisticated verbatim text
Version:        svn75920
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(fancyvrb-ex.sty) = %{tl_version}
Provides:       tex(fancyvrb.sty) = %{tl_version}
Provides:       tex(hbaw.sty) = %{tl_version}
Provides:       tex(hcolor.sty) = %{tl_version}

%description -n texlive-fancyvrb
Flexible handling of verbatim text including: verbatim commands in footnotes; a
variety of verbatim environments with many parameters; ability to define new
customized verbatim environments; save and restore verbatim text and
environments; write and read files in verbatim mode; build "example"
environments (showing both result and verbatim source).

%package -n texlive-filehook
Summary:        Hooks for input files
Version:        svn64822
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(currfile.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfkeys.sty)
Provides:       tex(filehook-2019.sty) = %{tl_version}
Provides:       tex(filehook-2020.sty) = %{tl_version}
Provides:       tex(filehook-fink.sty) = %{tl_version}
Provides:       tex(filehook-listings.sty) = %{tl_version}
Provides:       tex(filehook-memoir.sty) = %{tl_version}
Provides:       tex(filehook-scrlfile.sty) = %{tl_version}
Provides:       tex(filehook.sty) = %{tl_version}
Provides:       tex(pgf-filehook.sty) = %{tl_version}

%description -n texlive-filehook
The package provides several file hooks (AtBegin, AtEnd, ...) for files read by
\input, \include and \InputIfFileExists. General hooks for all such files (e.g.
all \included ones) and file specific hooks only used for named files are
provided; two hooks are provided for the end of \included files -- one before,
and one after the final \clearpage.

%package -n texlive-float
Summary:        Improved interface for floating objects
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(float.sty) = %{tl_version}

%description -n texlive-float
Improves the interface for defining floating objects such as figures and
tables. Introduces the boxed float, the ruled float and the plaintop float. You
can define your own floats and improve the behaviour of the old ones. The
package also provides the H float modifier option of the obsolete here package.
You can select this as automatic default with \floatplacement{figure}{H}.

%package -n texlive-fontspec
Summary:        Advanced font selection in XeLaTeX and LuaLaTeX
Version:        svn76430
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-euenc
Requires:       texlive-iftex
Requires:       texlive-l3kernel
Requires:       texlive-l3packages
Requires:       texlive-lm
Requires:       texlive-xunicode
Requires:       tex(fontenc.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(xparse.sty)
Provides:       tex(fontspec-luatex.sty) = %{tl_version}
Provides:       tex(fontspec-xetex.sty) = %{tl_version}
Provides:       tex(fontspec.sty) = %{tl_version}

%description -n texlive-fontspec
Fontspec is a package for XeLaTeX and LuaLaTeX. It provides an automatic and
unified interface to feature-rich AAT and OpenType fonts through the NFSS in
LaTeX running on XeTeX or LuaTeX engines. The package requires the l3kernel and
xparse bundles from the LaTeX3 development team.

%package -n texlive-footnotehyper
Summary:        A hyperref aware footnote environment
Version:        svn76871
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(footnotehyper.sty) = %{tl_version}

%description -n texlive-footnotehyper
This package provides a footnote environment allowing verbatim material and a
savenotes environment which captures footnotes across problematic environments.
It is a successor to the footnote package by Mark Wooding which had various
compatibility issues with modern packages (hyperref, color, xcolor,
babel-french).

%package -n texlive-fp
Summary:        Fixed point arithmetic
Version:        svn49719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(defpattern.sty) = %{tl_version}
Provides:       tex(fp-addons.sty) = %{tl_version}
Provides:       tex(fp-basic.sty) = %{tl_version}
Provides:       tex(fp-eqn.sty) = %{tl_version}
Provides:       tex(fp-eval.sty) = %{tl_version}
Provides:       tex(fp-exp.sty) = %{tl_version}
Provides:       tex(fp-pas.sty) = %{tl_version}
Provides:       tex(fp-random.sty) = %{tl_version}
Provides:       tex(fp-snap.sty) = %{tl_version}
Provides:       tex(fp-trigo.sty) = %{tl_version}
Provides:       tex(fp-upn.sty) = %{tl_version}
Provides:       tex(fp.sty) = %{tl_version}
Provides:       tex(fp.tex) = %{tl_version}
Provides:       tex(lfp.sty) = %{tl_version}

%description -n texlive-fp
An extensive collection of arithmetic operations for fixed point real numbers
of high precision.

%package -n texlive-grffile
Summary:        Extended file name support for graphics (legacy package)
Version:        svn52756
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
Provides:       tex(grffile-2017-06-30.sty) = %{tl_version}
Provides:       tex(grffile.sty) = %{tl_version}

%description -n texlive-grffile
The original package extended the file name processing of package graphics to
support a larger range of file names. The base LaTeX code now supports multiple
dots and spaces, and this package by default is a stub that just loads
graphicx. However, \usepackage{grffile}[=v1] may be used to access version
1(.18) of the package if that is needed.

%package -n texlive-hologo
Summary:        A collection of logos with bookmark support
Version:        svn76851
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
Provides:       tex(hologo.sty) = %{tl_version}

%description -n texlive-hologo
The package defines a single command \hologo, whose argument is the usual
case-confused ASCII version of the logo. The command is bookmark-enabled, so
that every logo becomes available in bookmarks without further work.

%package -n texlive-index
Summary:        Extended index for LaTeX including multiple indexes
Version:        svn73880
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(index.sty) = %{tl_version}

%description -n texlive-index
This is a reimplementation of LaTeX's indexing macros to provide better support
for indexing. For example, it supports multiple indexes in a single document
and provides a more robust \index command. It supplies short hand notations for
the \index command (^{word}) and a * variation of \index (abbreviated _{word})
that prints the word being indexed, as well as creating an index entry for it.

%package -n texlive-infwarerr
Summary:        Complete set of information/warning/error message macros
Version:        svn53023
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(infwarerr.sty) = %{tl_version}

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
Requires:       tex(graphicx.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(greekctr.sty) = %{tl_version}
Provides:       tex(holtpolt.sty) = %{tl_version}
Provides:       tex(latin1jk.def) = %{tl_version}
Provides:       tex(latin2jk.def) = %{tl_version}
Provides:       tex(latin3jk.def) = %{tl_version}
Provides:       tex(mathbbol.sty) = %{tl_version}
Provides:       tex(mathrsfs.sty) = %{tl_version}
Provides:       tex(parboxx.sty) = %{tl_version}
Provides:       tex(sans.sty) = %{tl_version}
Provides:       tex(semtrans.sty) = %{tl_version}
Provides:       tex(sgmlcmpt.sty) = %{tl_version}
Provides:       tex(smartmn.sty) = %{tl_version}
Provides:       tex(tccompat.sty) = %{tl_version}
Provides:       tex(young.sty) = %{tl_version}

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
Provides:       tex(authorpart-de.tex) = %{tl_version}
Provides:       tex(authorpart-en.tex) = %{tl_version}
Provides:       tex(book-remarkbox-nopatch-de.tex) = %{tl_version}
Provides:       tex(book-remarkbox-nopatch-de.tex) = %{tl_version}
Provides:       tex(book-remarkbox-nopatch-en.tex) = %{tl_version}
Provides:       tex(book-remarkbox-nopatch-en.tex) = %{tl_version}
Provides:       tex(book-remarkbox-patch-de.tex) = %{tl_version}
Provides:       tex(book-remarkbox-patch-de.tex) = %{tl_version}
Provides:       tex(book-remarkbox-patch-en.tex) = %{tl_version}
Provides:       tex(book-remarkbox-patch-en.tex) = %{tl_version}
Provides:       tex(common-compatibility-de.tex) = %{tl_version}
Provides:       tex(common-compatibility-en.tex) = %{tl_version}
Provides:       tex(common-dictum-de.tex) = %{tl_version}
Provides:       tex(common-dictum-en.tex) = %{tl_version}
Provides:       tex(common-draftmode-de.tex) = %{tl_version}
Provides:       tex(common-draftmode-en.tex) = %{tl_version}
Provides:       tex(common-fontsize-de.tex) = %{tl_version}
Provides:       tex(common-fontsize-en.tex) = %{tl_version}
Provides:       tex(common-footnotes-de.tex) = %{tl_version}
Provides:       tex(common-footnotes-en.tex) = %{tl_version}
Provides:       tex(common-footnotes-experts-de.tex) = %{tl_version}
Provides:       tex(common-footnotes-experts-en.tex) = %{tl_version}
Provides:       tex(common-headfootheight-de.tex) = %{tl_version}
Provides:       tex(common-headfootheight-en.tex) = %{tl_version}
Provides:       tex(common-interleafpage-de.tex) = %{tl_version}
Provides:       tex(common-interleafpage-en.tex) = %{tl_version}
Provides:       tex(common-lists-de.tex) = %{tl_version}
Provides:       tex(common-lists-en.tex) = %{tl_version}
Provides:       tex(common-marginpar-de.tex) = %{tl_version}
Provides:       tex(common-marginpar-en.tex) = %{tl_version}
Provides:       tex(common-oddorevenpage-de.tex) = %{tl_version}
Provides:       tex(common-oddorevenpage-en.tex) = %{tl_version}
Provides:       tex(common-options-de.tex) = %{tl_version}
Provides:       tex(common-options-en.tex) = %{tl_version}
Provides:       tex(common-pagestylemanipulation-de.tex) = %{tl_version}
Provides:       tex(common-pagestylemanipulation-en.tex) = %{tl_version}
Provides:       tex(common-parmarkup-de.tex) = %{tl_version}
Provides:       tex(common-parmarkup-en.tex) = %{tl_version}
Provides:       tex(common-textmarkup-de.tex) = %{tl_version}
Provides:       tex(common-textmarkup-en.tex) = %{tl_version}
Provides:       tex(common-titles-de.tex) = %{tl_version}
Provides:       tex(common-titles-en.tex) = %{tl_version}
Provides:       tex(common-typearea-de.tex) = %{tl_version}
Provides:       tex(common-typearea-en.tex) = %{tl_version}
Provides:       tex(expertpart-de.tex) = %{tl_version}
Provides:       tex(expertpart-en.tex) = %{tl_version}
Provides:       tex(introduction-de.tex) = %{tl_version}
Provides:       tex(introduction-en.tex) = %{tl_version}
Provides:       tex(japanlco-en.tex) = %{tl_version}
Provides:       tex(letter-example-00-de.tex) = %{tl_version}
Provides:       tex(letter-example-00-en.tex) = %{tl_version}
Provides:       tex(letter-example-01-de.tex) = %{tl_version}
Provides:       tex(letter-example-01-en.tex) = %{tl_version}
Provides:       tex(letter-example-02-de.tex) = %{tl_version}
Provides:       tex(letter-example-02-en.tex) = %{tl_version}
Provides:       tex(letter-example-03-de.tex) = %{tl_version}
Provides:       tex(letter-example-03-en.tex) = %{tl_version}
Provides:       tex(letter-example-04-de.tex) = %{tl_version}
Provides:       tex(letter-example-04-en.tex) = %{tl_version}
Provides:       tex(letter-example-05-de.tex) = %{tl_version}
Provides:       tex(letter-example-05-en.tex) = %{tl_version}
Provides:       tex(letter-example-06-de.tex) = %{tl_version}
Provides:       tex(letter-example-06-en.tex) = %{tl_version}
Provides:       tex(letter-example-07-de.tex) = %{tl_version}
Provides:       tex(letter-example-07-en.tex) = %{tl_version}
Provides:       tex(letter-example-08-de.tex) = %{tl_version}
Provides:       tex(letter-example-08-en.tex) = %{tl_version}
Provides:       tex(letter-example-09-de.tex) = %{tl_version}
Provides:       tex(letter-example-09-en.tex) = %{tl_version}
Provides:       tex(letter-example-10-de.tex) = %{tl_version}
Provides:       tex(letter-example-10-en.tex) = %{tl_version}
Provides:       tex(letter-example-11-de.tex) = %{tl_version}
Provides:       tex(letter-example-11-en.tex) = %{tl_version}
Provides:       tex(letter-example-12-de.tex) = %{tl_version}
Provides:       tex(letter-example-12-en.tex) = %{tl_version}
Provides:       tex(letter-example-13-de.tex) = %{tl_version}
Provides:       tex(letter-example-13-en.tex) = %{tl_version}
Provides:       tex(letter-example-14-de.tex) = %{tl_version}
Provides:       tex(letter-example-14-en.tex) = %{tl_version}
Provides:       tex(letter-example-15-de.tex) = %{tl_version}
Provides:       tex(letter-example-15-en.tex) = %{tl_version}
Provides:       tex(letter-example-16-de.tex) = %{tl_version}
Provides:       tex(letter-example-16-en.tex) = %{tl_version}
Provides:       tex(letter-example-17-de.tex) = %{tl_version}
Provides:       tex(letter-example-17-en.tex) = %{tl_version}
Provides:       tex(letter-example-18-de.tex) = %{tl_version}
Provides:       tex(letter-example-18-en.tex) = %{tl_version}
Provides:       tex(letter-example-19-de.tex) = %{tl_version}
Provides:       tex(letter-example-19-en.tex) = %{tl_version}
Provides:       tex(letter-example-20-de.tex) = %{tl_version}
Provides:       tex(letter-example-20-en.tex) = %{tl_version}
Provides:       tex(letter-example-21-de.tex) = %{tl_version}
Provides:       tex(letter-example-21-en.tex) = %{tl_version}
Provides:       tex(letter-example-22-de.tex) = %{tl_version}
Provides:       tex(letter-example-22-en.tex) = %{tl_version}
Provides:       tex(letter-example-23-de.tex) = %{tl_version}
Provides:       tex(letter-example-23-en.tex) = %{tl_version}
Provides:       tex(linkalias.tex) = %{tl_version}
Provides:       tex(plength-tikz.tex) = %{tl_version}
Provides:       tex(preface-de.tex) = %{tl_version}
Provides:       tex(preface-en.tex) = %{tl_version}
Provides:       tex(scraddr-de.tex) = %{tl_version}
Provides:       tex(scraddr-en.tex) = %{tl_version}
Provides:       tex(scraddr.sty) = %{tl_version}
Provides:       tex(scrbase-de.tex) = %{tl_version}
Provides:       tex(scrbase-en.tex) = %{tl_version}
Provides:       tex(scrbase.sty) = %{tl_version}
Provides:       tex(scrbookreportarticle-de.tex) = %{tl_version}
Provides:       tex(scrbookreportarticle-en.tex) = %{tl_version}
Provides:       tex(scrbookreportarticle-experts-de.tex) = %{tl_version}
Provides:       tex(scrbookreportarticle-experts-en.tex) = %{tl_version}
Provides:       tex(scrdate-de.tex) = %{tl_version}
Provides:       tex(scrdate-en.tex) = %{tl_version}
Provides:       tex(scrdate.sty) = %{tl_version}
Provides:       tex(scrdocstrip.tex) = %{tl_version}
Provides:       tex(scrextend-de.tex) = %{tl_version}
Provides:       tex(scrextend-en.tex) = %{tl_version}
Provides:       tex(scrextend.sty) = %{tl_version}
Provides:       tex(scrfontsizes.sty) = %{tl_version}
Provides:       tex(scrguide-body.tex) = %{tl_version}
Provides:       tex(scrguide-de.tex) = %{tl_version}
Provides:       tex(scrguide-en.tex) = %{tl_version}
Provides:       tex(scrjura-de.tex) = %{tl_version}
Provides:       tex(scrjura-en.tex) = %{tl_version}
Provides:       tex(scrjura.sty) = %{tl_version}
Provides:       tex(scrkbase.sty) = %{tl_version}
Provides:       tex(scrlayer-de.tex) = %{tl_version}
Provides:       tex(scrlayer-en.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-de.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-en.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-example-de.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-example-de.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-example-en.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-example-en.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn.sty) = %{tl_version}
Provides:       tex(scrlayer-scrpage-de.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage-en.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage-experts-de.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage-experts-en.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage.sty) = %{tl_version}
Provides:       tex(scrlayer.sty) = %{tl_version}
Provides:       tex(scrletter.sty) = %{tl_version}
Provides:       tex(scrlfile-de.tex) = %{tl_version}
Provides:       tex(scrlfile-en.tex) = %{tl_version}
Provides:       tex(scrlfile-hook-3.34.sty) = %{tl_version}
Provides:       tex(scrlfile-hook.sty) = %{tl_version}
Provides:       tex(scrlfile-patcholdlatex.sty) = %{tl_version}
Provides:       tex(scrlfile.sty) = %{tl_version}
Provides:       tex(scrlogo-de.tex) = %{tl_version}
Provides:       tex(scrlogo-en.tex) = %{tl_version}
Provides:       tex(scrlogo.sty) = %{tl_version}
Provides:       tex(scrlttr2-de.tex) = %{tl_version}
Provides:       tex(scrlttr2-en.tex) = %{tl_version}
Provides:       tex(scrlttr2-experts-de.tex) = %{tl_version}
Provides:       tex(scrlttr2-experts-en.tex) = %{tl_version}
Provides:       tex(scrtime-de.tex) = %{tl_version}
Provides:       tex(scrtime-en.tex) = %{tl_version}
Provides:       tex(scrtime.sty) = %{tl_version}
Provides:       tex(scrwfile-de.tex) = %{tl_version}
Provides:       tex(scrwfile-en.tex) = %{tl_version}
Provides:       tex(terms-de.tex) = %{tl_version}
Provides:       tex(terms-en.tex) = %{tl_version}
Provides:       tex(tocbasic-de.tex) = %{tl_version}
Provides:       tex(tocbasic-en.tex) = %{tl_version}
Provides:       tex(tocbasic.sty) = %{tl_version}
Provides:       tex(typearea-de.tex) = %{tl_version}
Provides:       tex(typearea-en.tex) = %{tl_version}
Provides:       tex(typearea-experts-de.tex) = %{tl_version}
Provides:       tex(typearea-experts-en.tex) = %{tl_version}
Provides:       tex(typearea.sty) = %{tl_version}
Provides:       tex(variables-tikz.tex) = %{tl_version}

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
Version:        svn76637
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-l3kernel
Provides:       tex(l3draw.sty) = %{tl_version}
Provides:       tex(l3galley.sty) = %{tl_version}
Provides:       tex(xcoffins.sty) = %{tl_version}
Provides:       tex(xgalley.sty) = %{tl_version}

%description -n texlive-l3experimental
The l3experimental packages are a collection of experimental implementations
for aspects of the LaTeX3 kernel, dealing with higher-level ideas such as the
Designer Interface. Some of them work as stand alone packages, providing new
functionality, and can be used on top of LaTeX2e with no changes to the
existing kernel. The present release includes: l3draw, a code-level interface
for constructing drawings; xcoffins, which allows the alignment of boxes using
a series of 'handle' positions, supplementing the simple TeX reference point;
xgalley, which controls boxes receiving text for typesetting.

%package -n texlive-latexbug
Summary:        Bug classification for LaTeX related bugs
Version:        svn77050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(latexbug.sty) = %{tl_version}

%description -n texlive-latexbug
The package is written in order to help identifying the rightful addressee for
a bug report. The LaTeX team asks that it will be loaded in any test file that
is intended to be sent to the LaTeX bug database as part of a bug report.

%package -n texlive-lineno
Summary:        Line numbers on paragraphs
Version:        svn75200
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(finstrut.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(longtable.sty)
Requires:       tex(ltabptch.sty)
Requires:       tex(varioref.sty)
Provides:       tex(ednmath0.sty) = %{tl_version}
Provides:       tex(edtable.sty) = %{tl_version}
Provides:       tex(fnlineno.sty) = %{tl_version}
Provides:       tex(lineno.sty) = %{tl_version}
Provides:       tex(vplref.sty) = %{tl_version}

%description -n texlive-lineno
Adds line numbers to selected paragraphs with reference possible through the
LaTeX \ref and \pageref cross reference mechanism. Line numbering may be
extended to footnote lines, using the fnlineno package.

%package -n texlive-listings
Summary:        Typeset source code listings using LaTeX
Version:        svn76899
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithmic.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(keyval.sty)
# Ignoring dependency on lgrind.sty - non-free
Requires:       tex(textcomp.sty)
Requires:       tex(xurl.sty)
Provides:       tex(listings.sty) = %{tl_version}
Provides:       tex(lstdoc.sty) = %{tl_version}
Provides:       tex(lstlang1.sty) = %{tl_version}
Provides:       tex(lstlang2.sty) = %{tl_version}
Provides:       tex(lstlang3.sty) = %{tl_version}
Provides:       tex(lstmisc.sty) = %{tl_version}
Provides:       tex(lstpatch.sty) = %{tl_version}

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
Version:        svn77585
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
Version:        svn77584
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lua-unicode-math.sty) = %{tl_version}
Provides:       tex(lum-bonum.sty) = %{tl_version}
Provides:       tex(lum-concrete.sty) = %{tl_version}
Provides:       tex(lum-dejavu.sty) = %{tl_version}
Provides:       tex(lum-erewhon.sty) = %{tl_version}
Provides:       tex(lum-fira.sty) = %{tl_version}
Provides:       tex(lum-gfsneohellenic.sty) = %{tl_version}
Provides:       tex(lum-lmodern.sty) = %{tl_version}
Provides:       tex(lum-newcomputermodern.sty) = %{tl_version}
Provides:       tex(lum-newcomputermodernsans.sty) = %{tl_version}
Provides:       tex(lum-pagella.sty) = %{tl_version}
Provides:       tex(lum-schola.sty) = %{tl_version}
Provides:       tex(lum-stix2.sty) = %{tl_version}
Provides:       tex(lum-termes.sty) = %{tl_version}
Provides:       tex(lum-xcharter.sty) = %{tl_version}
Provides:       tex(lum-xits.sty) = %{tl_version}

%description -n texlive-lua-unicode-math
A faster and more compatible package to support using OpenType math fonts in
LuaLaTeX as an alternative for unicode-math.

%package -n texlive-mathspec
Summary:        Specify arbitrary fonts for mathematics in XeTeX
Version:        svn42773
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(MnSymbol.sty)
Requires:       tex(amstext.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mathspec.sty) = %{tl_version}

%description -n texlive-mathspec
The mathspec package provides an interface to typeset mathematics in XeLaTeX
with arbitrary text fonts using fontspec as a backend. The package is under
development and later versions might to be incompatible with this version, as
this version is incompatible with earlier versions. The package requires at
least version 0.9995 of XeTeX.

%package -n texlive-mathtools
Summary:        Mathematical tools to use with amsmath
Version:        svn72487
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-amsmath
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Provides:       tex(empheq.sty) = %{tl_version}
Provides:       tex(mathtools.sty) = %{tl_version}
Provides:       tex(mhsetup.sty) = %{tl_version}

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
Provides:       tex(at.sty) = %{tl_version}
Provides:       tex(cmtt.sty) = %{tl_version}
Provides:       tex(doafter.sty) = %{tl_version}
Provides:       tex(footnote.sty) = %{tl_version}
Provides:       tex(mTTenc.def) = %{tl_version}
Provides:       tex(mathenv.sty) = %{tl_version}
Provides:       tex(mdwlist.sty) = %{tl_version}
Provides:       tex(mdwmath.sty) = %{tl_version}
Provides:       tex(mdwtab.sty) = %{tl_version}
Provides:       tex(sverb.sty) = %{tl_version}
Provides:       tex(syntax.sty) = %{tl_version}

%description -n texlive-mdwtools
This collection of tools includes: support for short commands starting with @,
macros to sanitise the OT1 encoding of the cmtt fonts; a 'do after' command;
improved footnote support; mathenv for various alignment in maths; list
handling; mdwmath which adds some minor changes to LaTeX maths; a rewrite of
LaTeX's tabular and array environments; verbatim handling; and syntax diagrams.

%package -n texlive-memoir
Summary:        Typeset fiction, non-fiction and mathematical books
Version:        svn76756
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(memhfixc.sty) = %{tl_version}

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
Version:        svn18611
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifxetex.sty)
Provides:       tex(metalogo.sty) = %{tl_version}

%description -n texlive-metalogo
This package exposes spacing parameters for various TeX logos to the end user,
to optimise the logos for different fonts. Written especially for XeLaTeX
users.

%package -n texlive-microtype
Summary:        Subliminal refinements towards typographical perfection
Version:        svn75729
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-etoolbox
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iftex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(letterspace.sty) = %{tl_version}
Provides:       tex(microtype-luatex.def) = %{tl_version}
Provides:       tex(microtype-pdftex.def) = %{tl_version}
Provides:       tex(microtype-show.sty) = %{tl_version}
Provides:       tex(microtype-xetex.def) = %{tl_version}
Provides:       tex(microtype.sty) = %{tl_version}

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
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(newfloat.sty) = %{tl_version}
Provides:       tex(newfloat_v1.0.sty) = %{tl_version}
Provides:       tex(newfloat_v1.1.sty) = %{tl_version}

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
Provides:       tex(a4.sty) = %{tl_version}

%description -n texlive-ntgclass
The bundle offers versions of the standard LaTeX article and report classes,
rewritten to reflect a more European design, and the a4 package, which is
better tuned to the shape of a4 paper than is the a4paper class option of the
standard classes. The classes include several for article and report
requirements, and a letter class. The elements of the bundle were designed by
members of the Dutch TeX Users Group NTG.

%package -n texlive-parskip
Summary:        Layout with zero \parindent, non-zero \parskip
Version:        svn58358
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(parskip-2001-04-09.sty) = %{tl_version}
Provides:       tex(parskip.sty) = %{tl_version}

%description -n texlive-parskip
Simply changing \parskip and \parindent leaves a layout that is untidy; this
package (though it is no substitute for a properly-designed class) helps
alleviate this untidiness.

%package -n texlive-pdfcolfoot
Summary:        Separate color stack for footnotes with pdfTeX
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pdfcol.sty)
Provides:       tex(pdfcolfoot.sty) = %{tl_version}

%description -n texlive-pdfcolfoot
Since version 1.40 pdfTeX supports several colour stacks. This package uses a
separate colour stack for footnotes that can break across pages.

%package -n texlive-pdflscape
Summary:        Make landscape pages display as landscape
Version:        svn75593
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(lscape.sty)
Provides:       tex(pdflscape-nometadata.sty) = %{tl_version}
Provides:       tex(pdflscape.sty) = %{tl_version}

%description -n texlive-pdflscape
The package adds PDF support to the landscape environment of package lscape, by
setting the PDF /Rotate page attribute. Pages with this attribute will be
displayed in landscape orientation by conforming PDF viewers.

%package -n texlive-pdfmanagement-testphase
Summary:        LaTeX PDF management testphase bundle
Version:        svn77467
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tagpdf-base.sty)
Provides:       tex(color-ltx.sty) = %{tl_version}
Provides:       tex(colorspace-patches-tmp-ltx.sty) = %{tl_version}
Provides:       tex(hgeneric-testphase.def) = %{tl_version}
Provides:       tex(hgeneric.def) = %{tl_version}
Provides:       tex(hyperref-colorschemes.def) = %{tl_version}
Provides:       tex(l3backend-testphase-dvipdfmx.def) = %{tl_version}
Provides:       tex(l3backend-testphase-dvips.def) = %{tl_version}
Provides:       tex(l3backend-testphase-dvisvgm.def) = %{tl_version}
Provides:       tex(l3backend-testphase-luatex.def) = %{tl_version}
Provides:       tex(l3backend-testphase-pdftex.def) = %{tl_version}
Provides:       tex(l3backend-testphase-xetex.def) = %{tl_version}
Provides:       tex(l3pdffield-testphase.sty) = %{tl_version}
Provides:       tex(l3pdffield.sty) = %{tl_version}
Provides:       tex(pdfmanagement-firstaid.sty) = %{tl_version}
Provides:       tex(pdfmanagement-testphase.sty) = %{tl_version}
Provides:       tex(pdfmanagement.sty) = %{tl_version}
Provides:       tex(xcolor-patches-tmp-ltx.sty) = %{tl_version}

%description -n texlive-pdfmanagement-testphase
This is a temporary package, which is used during a test phase to load the new
PDF management code of LaTeX. The new PDF management code offers
backend-independent interfaces to central PDF dictionaries, tools to create
annotations, form Xobjects, to embed files, and to handle PDF standards. The
code is provided, during a testphase, as an independent package to allow users
and package authors to safely test the code. At a later stage it will be
integrated into the LaTeX kernel (or in parts into permanent support packages),
and the current testphase bundle will be removed.

%package -n texlive-pdfpages
Summary:        Include PDF documents in LaTeX
Version:        svn75881
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-eso-pic
Requires:       texlive-graphics
Requires:       texlive-oberdiek
Requires:       texlive-tools
Requires:       tex(calc.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pdflscape.sty)
Provides:       tex(pdfpages.sty) = %{tl_version}
Provides:       tex(ppdvipdfmx.def) = %{tl_version}
Provides:       tex(ppdvips.def) = %{tl_version}
Provides:       tex(ppluatex.def) = %{tl_version}
Provides:       tex(ppnull.def) = %{tl_version}
Provides:       tex(pppdftex.def) = %{tl_version}
Provides:       tex(ppvtex.def) = %{tl_version}
Provides:       tex(ppxetex.def) = %{tl_version}

%description -n texlive-pdfpages
This package simplifies the inclusion of external multi-page PDF documents in
LaTeX documents. Pages may be freely selected and similar to psnup it is
possible to put several logical pages onto each sheet of paper. Furthermore a
lot of hypertext features like hyperlinks and article threads are provided. The
package supports pdfTeX (pdfLaTeX) and VTeX. With VTeX it is even possible to
use this package to insert PostScript files, in addition to PDF files.

%package -n texlive-polyglossia
Summary:        An alternative to babel for XeLaTeX and LuaLaTeX
Version:        svn76990
License:        MIT AND LPPL-1.3c AND CC0-1.0
Requires:       texlive-base
Requires:       texlive-kpathsea
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
Provides:       tex(arabicnumbers.sty) = %{tl_version}
Provides:       tex(babel-hebrewalph.def) = %{tl_version}
Provides:       tex(babelsh.def) = %{tl_version}
Provides:       tex(bengalidigits.sty) = %{tl_version}
Provides:       tex(cal-util.def) = %{tl_version}
Provides:       tex(devanagaridigits.sty) = %{tl_version}
Provides:       tex(farsical.sty) = %{tl_version}
Provides:       tex(gloss-acadian.ldf) = %{tl_version}
Provides:       tex(gloss-aeb.ldf) = %{tl_version}
Provides:       tex(gloss-af.ldf) = %{tl_version}
Provides:       tex(gloss-afb.ldf) = %{tl_version}
Provides:       tex(gloss-afrikaans.ldf) = %{tl_version}
Provides:       tex(gloss-albanian.ldf) = %{tl_version}
Provides:       tex(gloss-am.ldf) = %{tl_version}
Provides:       tex(gloss-american.ldf) = %{tl_version}
Provides:       tex(gloss-amharic.ldf) = %{tl_version}
Provides:       tex(gloss-apd.ldf) = %{tl_version}
Provides:       tex(gloss-ar-IQ.ldf) = %{tl_version}
Provides:       tex(gloss-ar-JO.ldf) = %{tl_version}
Provides:       tex(gloss-ar-LB.ldf) = %{tl_version}
Provides:       tex(gloss-ar-MR.ldf) = %{tl_version}
Provides:       tex(gloss-ar-PS.ldf) = %{tl_version}
Provides:       tex(gloss-ar-SY.ldf) = %{tl_version}
Provides:       tex(gloss-ar-YE.ldf) = %{tl_version}
Provides:       tex(gloss-ar.ldf) = %{tl_version}
Provides:       tex(gloss-arabic.ldf) = %{tl_version}
Provides:       tex(gloss-armenian.ldf) = %{tl_version}
Provides:       tex(gloss-arq.ldf) = %{tl_version}
Provides:       tex(gloss-ary.ldf) = %{tl_version}
Provides:       tex(gloss-arz.ldf) = %{tl_version}
Provides:       tex(gloss-ast.ldf) = %{tl_version}
Provides:       tex(gloss-asturian.ldf) = %{tl_version}
Provides:       tex(gloss-australian.ldf) = %{tl_version}
Provides:       tex(gloss-austrian.ldf) = %{tl_version}
Provides:       tex(gloss-ayl.ldf) = %{tl_version}
Provides:       tex(gloss-bahasa.ldf) = %{tl_version}
Provides:       tex(gloss-bahasai.ldf) = %{tl_version}
Provides:       tex(gloss-bahasam.ldf) = %{tl_version}
Provides:       tex(gloss-basque.ldf) = %{tl_version}
Provides:       tex(gloss-be-tarask.ldf) = %{tl_version}
Provides:       tex(gloss-be.ldf) = %{tl_version}
Provides:       tex(gloss-belarusian.ldf) = %{tl_version}
Provides:       tex(gloss-bengali.ldf) = %{tl_version}
Provides:       tex(gloss-bg.ldf) = %{tl_version}
Provides:       tex(gloss-bn.ldf) = %{tl_version}
Provides:       tex(gloss-bo.ldf) = %{tl_version}
Provides:       tex(gloss-bosnian.ldf) = %{tl_version}
Provides:       tex(gloss-br.ldf) = %{tl_version}
Provides:       tex(gloss-brazil.ldf) = %{tl_version}
Provides:       tex(gloss-breton.ldf) = %{tl_version}
Provides:       tex(gloss-british.ldf) = %{tl_version}
Provides:       tex(gloss-bs.ldf) = %{tl_version}
Provides:       tex(gloss-bulgarian.ldf) = %{tl_version}
Provides:       tex(gloss-ca.ldf) = %{tl_version}
Provides:       tex(gloss-canadian.ldf) = %{tl_version}
Provides:       tex(gloss-canadien.ldf) = %{tl_version}
Provides:       tex(gloss-catalan.ldf) = %{tl_version}
Provides:       tex(gloss-chinese.ldf) = %{tl_version}
Provides:       tex(gloss-ckb-Arab.ldf) = %{tl_version}
Provides:       tex(gloss-ckb-Latn.ldf) = %{tl_version}
Provides:       tex(gloss-ckb.ldf) = %{tl_version}
Provides:       tex(gloss-classicallatin.ldf) = %{tl_version}
Provides:       tex(gloss-classiclatin.ldf) = %{tl_version}
Provides:       tex(gloss-cop.ldf) = %{tl_version}
Provides:       tex(gloss-coptic.ldf) = %{tl_version}
Provides:       tex(gloss-croatian.ldf) = %{tl_version}
Provides:       tex(gloss-cy.ldf) = %{tl_version}
Provides:       tex(gloss-cz.ldf) = %{tl_version}
Provides:       tex(gloss-czech.ldf) = %{tl_version}
Provides:       tex(gloss-da.ldf) = %{tl_version}
Provides:       tex(gloss-danish.ldf) = %{tl_version}
Provides:       tex(gloss-de-AT-1901.ldf) = %{tl_version}
Provides:       tex(gloss-de-AT-1996.ldf) = %{tl_version}
Provides:       tex(gloss-de-AT.ldf) = %{tl_version}
Provides:       tex(gloss-de-CH-1901.ldf) = %{tl_version}
Provides:       tex(gloss-de-CH-1996.ldf) = %{tl_version}
Provides:       tex(gloss-de-CH.ldf) = %{tl_version}
Provides:       tex(gloss-de-DE-1901.ldf) = %{tl_version}
Provides:       tex(gloss-de-DE-1996.ldf) = %{tl_version}
Provides:       tex(gloss-de-DE.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-AT-1901.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-AT-1996.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-AT.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-CH-1901.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-CH-1996.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-CH.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-DE-1901.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-DE-1996.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf-DE.ldf) = %{tl_version}
Provides:       tex(gloss-de-Latf.ldf) = %{tl_version}
Provides:       tex(gloss-de.ldf) = %{tl_version}
Provides:       tex(gloss-divehi.ldf) = %{tl_version}
Provides:       tex(gloss-dsb.ldf) = %{tl_version}
Provides:       tex(gloss-dutch.ldf) = %{tl_version}
Provides:       tex(gloss-dv.ldf) = %{tl_version}
Provides:       tex(gloss-ecclesiasticallatin.ldf) = %{tl_version}
Provides:       tex(gloss-ecclesiasticlatin.ldf) = %{tl_version}
Provides:       tex(gloss-el-monoton.ldf) = %{tl_version}
Provides:       tex(gloss-el-polyton.ldf) = %{tl_version}
Provides:       tex(gloss-el.ldf) = %{tl_version}
Provides:       tex(gloss-en-AU.ldf) = %{tl_version}
Provides:       tex(gloss-en-CA.ldf) = %{tl_version}
Provides:       tex(gloss-en-GB.ldf) = %{tl_version}
Provides:       tex(gloss-en-NZ.ldf) = %{tl_version}
Provides:       tex(gloss-en-US.ldf) = %{tl_version}
Provides:       tex(gloss-en.ldf) = %{tl_version}
Provides:       tex(gloss-english.ldf) = %{tl_version}
Provides:       tex(gloss-eo.ldf) = %{tl_version}
Provides:       tex(gloss-es-ES.ldf) = %{tl_version}
Provides:       tex(gloss-es-MX.ldf) = %{tl_version}
Provides:       tex(gloss-es.ldf) = %{tl_version}
Provides:       tex(gloss-esperanto.ldf) = %{tl_version}
Provides:       tex(gloss-estonian.ldf) = %{tl_version}
Provides:       tex(gloss-et.ldf) = %{tl_version}
Provides:       tex(gloss-eu.ldf) = %{tl_version}
Provides:       tex(gloss-fa.ldf) = %{tl_version}
Provides:       tex(gloss-farsi.ldf) = %{tl_version}
Provides:       tex(gloss-fi.ldf) = %{tl_version}
Provides:       tex(gloss-finnish.ldf) = %{tl_version}
Provides:       tex(gloss-fr-CA-u-sd-canb.ldf) = %{tl_version}
Provides:       tex(gloss-fr-CA.ldf) = %{tl_version}
Provides:       tex(gloss-fr-CH.ldf) = %{tl_version}
Provides:       tex(gloss-fr-FR.ldf) = %{tl_version}
Provides:       tex(gloss-fr.ldf) = %{tl_version}
Provides:       tex(gloss-french.ldf) = %{tl_version}
Provides:       tex(gloss-friulan.ldf) = %{tl_version}
Provides:       tex(gloss-friulian.ldf) = %{tl_version}
Provides:       tex(gloss-fur.ldf) = %{tl_version}
Provides:       tex(gloss-ga.ldf) = %{tl_version}
Provides:       tex(gloss-gaelic.ldf) = %{tl_version}
Provides:       tex(gloss-galician.ldf) = %{tl_version}
Provides:       tex(gloss-gd.ldf) = %{tl_version}
Provides:       tex(gloss-georgian.ldf) = %{tl_version}
Provides:       tex(gloss-german.ldf) = %{tl_version}
Provides:       tex(gloss-germanb.ldf) = %{tl_version}
Provides:       tex(gloss-gl.ldf) = %{tl_version}
Provides:       tex(gloss-grc.ldf) = %{tl_version}
Provides:       tex(gloss-greek.ldf) = %{tl_version}
Provides:       tex(gloss-he.ldf) = %{tl_version}
Provides:       tex(gloss-hebrew.ldf) = %{tl_version}
Provides:       tex(gloss-hi.ldf) = %{tl_version}
Provides:       tex(gloss-hindi.ldf) = %{tl_version}
Provides:       tex(gloss-hr.ldf) = %{tl_version}
Provides:       tex(gloss-hsb.ldf) = %{tl_version}
Provides:       tex(gloss-hu.ldf) = %{tl_version}
Provides:       tex(gloss-hungarian.ldf) = %{tl_version}
Provides:       tex(gloss-hy.ldf) = %{tl_version}
Provides:       tex(gloss-ia.ldf) = %{tl_version}
Provides:       tex(gloss-icelandic.ldf) = %{tl_version}
Provides:       tex(gloss-id.ldf) = %{tl_version}
Provides:       tex(gloss-interlingua.ldf) = %{tl_version}
Provides:       tex(gloss-irish.ldf) = %{tl_version}
Provides:       tex(gloss-is.ldf) = %{tl_version}
Provides:       tex(gloss-it.ldf) = %{tl_version}
Provides:       tex(gloss-italian.ldf) = %{tl_version}
Provides:       tex(gloss-ja.ldf) = %{tl_version}
Provides:       tex(gloss-japanese.ldf) = %{tl_version}
Provides:       tex(gloss-ka.ldf) = %{tl_version}
Provides:       tex(gloss-kannada.ldf) = %{tl_version}
Provides:       tex(gloss-khmer.ldf) = %{tl_version}
Provides:       tex(gloss-km.ldf) = %{tl_version}
Provides:       tex(gloss-kmr-Arab.ldf) = %{tl_version}
Provides:       tex(gloss-kmr-Latn.ldf) = %{tl_version}
Provides:       tex(gloss-kmr.ldf) = %{tl_version}
Provides:       tex(gloss-kn.ldf) = %{tl_version}
Provides:       tex(gloss-ko.ldf) = %{tl_version}
Provides:       tex(gloss-korean.ldf) = %{tl_version}
Provides:       tex(gloss-ku-Arab.ldf) = %{tl_version}
Provides:       tex(gloss-ku-Latn.ldf) = %{tl_version}
Provides:       tex(gloss-ku.ldf) = %{tl_version}
Provides:       tex(gloss-kurdish.ldf) = %{tl_version}
Provides:       tex(gloss-kurmanji.ldf) = %{tl_version}
Provides:       tex(gloss-la-x-classic.ldf) = %{tl_version}
Provides:       tex(gloss-la-x-ecclesia.ldf) = %{tl_version}
Provides:       tex(gloss-la-x-medieval.ldf) = %{tl_version}
Provides:       tex(gloss-la.ldf) = %{tl_version}
Provides:       tex(gloss-lao.ldf) = %{tl_version}
Provides:       tex(gloss-latex.ldf) = %{tl_version}
Provides:       tex(gloss-latin.ldf) = %{tl_version}
Provides:       tex(gloss-latvian.ldf) = %{tl_version}
Provides:       tex(gloss-lithuanian.ldf) = %{tl_version}
Provides:       tex(gloss-lo.ldf) = %{tl_version}
Provides:       tex(gloss-lowersorbian.ldf) = %{tl_version}
Provides:       tex(gloss-lsorbian.ldf) = %{tl_version}
Provides:       tex(gloss-lt.ldf) = %{tl_version}
Provides:       tex(gloss-lv.ldf) = %{tl_version}
Provides:       tex(gloss-macedonian.ldf) = %{tl_version}
Provides:       tex(gloss-magyar.ldf) = %{tl_version}
Provides:       tex(gloss-malay.ldf) = %{tl_version}
Provides:       tex(gloss-malayalam.ldf) = %{tl_version}
Provides:       tex(gloss-marathi.ldf) = %{tl_version}
Provides:       tex(gloss-medievallatin.ldf) = %{tl_version}
Provides:       tex(gloss-mk.ldf) = %{tl_version}
Provides:       tex(gloss-ml.ldf) = %{tl_version}
Provides:       tex(gloss-mn.ldf) = %{tl_version}
Provides:       tex(gloss-mongolian.ldf) = %{tl_version}
Provides:       tex(gloss-mr.ldf) = %{tl_version}
Provides:       tex(gloss-naustrian.ldf) = %{tl_version}
Provides:       tex(gloss-nb.ldf) = %{tl_version}
Provides:       tex(gloss-newzealand.ldf) = %{tl_version}
Provides:       tex(gloss-ngerman.ldf) = %{tl_version}
Provides:       tex(gloss-nko.ldf) = %{tl_version}
Provides:       tex(gloss-norsk.ldf) = %{tl_version}
Provides:       tex(gloss-norwegian.ldf) = %{tl_version}
Provides:       tex(gloss-nswissgerman.ldf) = %{tl_version}
Provides:       tex(gloss-nynorsk.ldf) = %{tl_version}
Provides:       tex(gloss-occitan.ldf) = %{tl_version}
Provides:       tex(gloss-odia.ldf) = %{tl_version}
Provides:       tex(gloss-or.ldf) = %{tl_version}
Provides:       tex(gloss-pa.ldf) = %{tl_version}
Provides:       tex(gloss-persian.ldf) = %{tl_version}
Provides:       tex(gloss-piedmontese.ldf) = %{tl_version}
Provides:       tex(gloss-polish.ldf) = %{tl_version}
Provides:       tex(gloss-polutonikogreek.ldf) = %{tl_version}
Provides:       tex(gloss-portuges.ldf) = %{tl_version}
Provides:       tex(gloss-portuguese.ldf) = %{tl_version}
Provides:       tex(gloss-punjabi.ldf) = %{tl_version}
Provides:       tex(gloss-romanian.ldf) = %{tl_version}
Provides:       tex(gloss-romansh.ldf) = %{tl_version}
Provides:       tex(gloss-russian.ldf) = %{tl_version}
Provides:       tex(gloss-sami.ldf) = %{tl_version}
Provides:       tex(gloss-samin.ldf) = %{tl_version}
Provides:       tex(gloss-sanskrit.ldf) = %{tl_version}
Provides:       tex(gloss-scottish.ldf) = %{tl_version}
Provides:       tex(gloss-serbian.ldf) = %{tl_version}
Provides:       tex(gloss-serbianc.ldf) = %{tl_version}
Provides:       tex(gloss-slovak.ldf) = %{tl_version}
Provides:       tex(gloss-slovene.ldf) = %{tl_version}
Provides:       tex(gloss-slovenian.ldf) = %{tl_version}
Provides:       tex(gloss-sorbian.ldf) = %{tl_version}
Provides:       tex(gloss-spanish.ldf) = %{tl_version}
Provides:       tex(gloss-spanishmx.ldf) = %{tl_version}
Provides:       tex(gloss-swedish.ldf) = %{tl_version}
Provides:       tex(gloss-swissgerman.ldf) = %{tl_version}
Provides:       tex(gloss-syriac.ldf) = %{tl_version}
Provides:       tex(gloss-tamil.ldf) = %{tl_version}
Provides:       tex(gloss-telugu.ldf) = %{tl_version}
Provides:       tex(gloss-thai.ldf) = %{tl_version}
Provides:       tex(gloss-tibetan.ldf) = %{tl_version}
Provides:       tex(gloss-turkish.ldf) = %{tl_version}
Provides:       tex(gloss-turkmen.ldf) = %{tl_version}
Provides:       tex(gloss-ug.ldf) = %{tl_version}
Provides:       tex(gloss-ukrainian.ldf) = %{tl_version}
Provides:       tex(gloss-uppersorbian.ldf) = %{tl_version}
Provides:       tex(gloss-urdu.ldf) = %{tl_version}
Provides:       tex(gloss-usorbian.ldf) = %{tl_version}
Provides:       tex(gloss-uyghur.ldf) = %{tl_version}
Provides:       tex(gloss-vietnamese.ldf) = %{tl_version}
Provides:       tex(gloss-welsh.ldf) = %{tl_version}
Provides:       tex(gloss-zh-CN.ldf) = %{tl_version}
Provides:       tex(gloss-zh-TW.ldf) = %{tl_version}
Provides:       tex(gurmukhidigits.sty) = %{tl_version}
Provides:       tex(hebrewcal.sty) = %{tl_version}
Provides:       tex(hijrical.sty) = %{tl_version}
Provides:       tex(nkonumbers.sty) = %{tl_version}
Provides:       tex(odiadigits.sty) = %{tl_version}
Provides:       tex(polyglossia.sty) = %{tl_version}
Provides:       tex(xgreek-fixes.def) = %{tl_version}
Provides:       tex(xpg-cyrillicnumbers.sty) = %{tl_version}

%description -n texlive-polyglossia
This package provides a complete Babel replacement for users of LuaLaTeX and
XeLaTeX; it relies on the fontspec package, version 2.0 at least.

%package -n texlive-psfrag
Summary:        Replace strings in encapsulated PostScript figures
Version:        svn15878
License:        psfrag
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(psfrag.sty) = %{tl_version}

%description -n texlive-psfrag
Allows LaTeX constructions (equations, picture environments, etc.) to be
precisely superimposed over Encapsulated PostScript figures, using your own
favorite drawing tool to create an EPS figure and placing simple text 'tags'
where each replacement is to be placed, with PSfrag automatically removing
these tags from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

%package -n texlive-ragged2e
Summary:        Alternative versions of "ragged"-type commands
Version:        svn67441
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(everysel.sty)
Requires:       tex(footmisc.sty)
Provides:       tex(ragged2e.sty) = %{tl_version}

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
Provides:       tex(rcs.sty) = %{tl_version}

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
Version:        svn17997
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sansmath.sty) = %{tl_version}

%description -n texlive-sansmath
The package defines a new math version sans, and a command \sansmath that
behaves somewhat like \boldmath

%package -n texlive-section
Summary:        Modifying section commands in LaTeX
Version:        svn20180
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(section.sty) = %{tl_version}

%description -n texlive-section
The package implements a pretty extensive scheme to make more manageable the
business of configuring LaTeX output.

%package -n texlive-seminar
Summary:        Make overhead slides
Version:        svn59801
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Requires:       tex(pst-ovl.sty)
Provides:       tex(npsfont.sty) = %{tl_version}
Provides:       tex(sem-a4.sty) = %{tl_version}
Provides:       tex(sem-dem.sty) = %{tl_version}
Provides:       tex(sem-page.sty) = %{tl_version}
Provides:       tex(semcolor.sty) = %{tl_version}
Provides:       tex(semhelv.sty) = %{tl_version}
Provides:       tex(seminar.sty) = %{tl_version}
Provides:       tex(semlayer.sty) = %{tl_version}
Provides:       tex(semlcmss.sty) = %{tl_version}
Provides:       tex(semrot.sty) = %{tl_version}
Provides:       tex(slidesec.sty) = %{tl_version}
Provides:       tex(tvz-code.sty) = %{tl_version}
Provides:       tex(tvz-hax.sty) = %{tl_version}
Provides:       tex(tvz-user.sty) = %{tl_version}

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
Provides:       tex(sepnum.sty) = %{tl_version}

%description -n texlive-sepnum
Provides a command to print a number with (potentially different) separators
every three digits in the parts either side of the decimal point (the point
itself is also configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command \sepnumform, that
may be used when defining \the<counter> macros.

%package -n texlive-setspace
Summary:        Set space between lines
Version:        svn65206
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(setspace.sty) = %{tl_version}

%description -n texlive-setspace
Provides support for setting the spacing between lines in a document. Package
options include singlespacing, onehalfspacing, and doublespacing. Alternatively
the spacing can be changed as required with the \singlespacing,
\onehalfspacing, and \doublespacing commands. Other size spacings also
available.

%package -n texlive-subfig
Summary:        Figures broken into subfigures
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(caption.sty)
Requires:       tex(keyval.sty)
Provides:       tex(subfig.sty) = %{tl_version}

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
Version:        svn75878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(textcase.sty) = %{tl_version}

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
Version:        svn59412
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(translator.sty) = %{tl_version}

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
Requires:       tex(exscale.sty)
Provides:       tex(typehtml.sty) = %{tl_version}

%description -n texlive-typehtml
Can handle almost all of HTML2, and most of the math fragment of the draft
HTML3.

%package -n texlive-ucharcat
Summary:        Implementation of the (new in 2015) XeTeX \Ucharcat command in lua, for LuaTeX
Version:        svn38907
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ucharcat.sty) = %{tl_version}

%description -n texlive-ucharcat
The package implements the \Ucharcat command for LuaLaTeX. \Ucharcat is a new
primitive in XeTeX, an extension of the existing \Uchar command, that allows
the specification of the catcode as well as character code of the character
token being constructed.

%package -n texlive-underscore
Summary:        Control the behaviour of "_" in text
Version:        svn18261
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chicago.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(underscore.sty) = %{tl_version}

%description -n texlive-underscore
With the package, \_ in text mode (i.e., \textunderscore) prints an underscore
so that hyphenation of words either side of it is not affected; a package
option controls whether an actual hyphenation point appears after the
underscore, or merely a break point. The package also arranges that, while in
text, '_' itself behaves as \textunderscore (the behaviour of _ in maths mode
is not affected).

%package -n texlive-unicode-math
Summary:        Unicode mathematics support for XeTeX and LuaTeX
Version:        svn75152
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fontspec
Requires:       texlive-lm-math
Requires:       tex(amsmath.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(lualatex-math.sty)
Requires:       tex(xparse.sty)
Provides:       tex(unicode-math-luatex.sty) = %{tl_version}
Provides:       tex(unicode-math-table.tex) = %{tl_version}
Provides:       tex(unicode-math-xetex.sty) = %{tl_version}
Provides:       tex(unicode-math.sty) = %{tl_version}

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
Version:        svn72484
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(colortbl.sty)
Requires:       tex(pdfcolmk.sty)
Provides:       tex(svgnam.def) = %{tl_version}
Provides:       tex(x11nam.def) = %{tl_version}
Provides:       tex(xcolor-2022-06-12.sty) = %{tl_version}
Provides:       tex(xcolor.sty) = %{tl_version}

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
Version:        svn71430
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amstext.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(xfrac.sty) = %{tl_version}

%description -n texlive-xfrac
This package uses the interface defined by LaTeX templates to provide flexible
split-level fractions via the \sfrac macro. This is both a demonstration of the
power of the template concept and also a useful addition to the available
functionality in LaTeX2e.

%package -n texlive-xkeyval
Summary:        Extension of the keyval package
Version:        svn76763
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(longtable.sty)
Provides:       tex(keyval.tex) = %{tl_version}
Provides:       tex(pst-xkey.sty) = %{tl_version}
Provides:       tex(pst-xkey.tex) = %{tl_version}
Provides:       tex(xkeyval.sty) = %{tl_version}
Provides:       tex(xkeyval.tex) = %{tl_version}
Provides:       tex(xkvltxp.sty) = %{tl_version}
Provides:       tex(xkvtxhdr.tex) = %{tl_version}
Provides:       tex(xkvutils.tex) = %{tl_version}
Provides:       tex(xkvview.sty) = %{tl_version}

%description -n texlive-xkeyval
This package is an extension of the keyval package and offers additional macros
for setting keys and declaring and setting class or package options. The
package allows the programmer to specify a prefix to the name of the macros it
defines for keys, and to define families of key definitions; these all help use
in documents where several packages define their own sets of keys.

%package -n texlive-xltxtra
Summary:        "Extras" for LaTeX users of XeTeX
Version:        svn56594
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-metalogo
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(realscripts.sty)
Provides:       tex(xltxtra.sty) = %{tl_version}

%description -n texlive-xltxtra
This package was previously used to provide a number of features that were
useful for typesetting documents with XeLaTeX. Many of those features have now
been incorporated into the fontspec package and other packages, but the package
persists for backwards compatibility. Nowadays, loading xltxtra will: load the
fontspec, metalogo, and realscripts packages; redefine \showhyphens so it works
correctly; and define two extra commands: \vfrac and \namedglyph.

%package -n texlive-xunicode
Summary:        Generate Unicode characters from accented glyphs
Version:        svn30466
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-tipa
Requires:       tex(graphicx.sty)
Provides:       tex(xunicode.sty) = %{tl_version}

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
tar -xf %{SOURCE137} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE138} -C %{buildroot}%{_texmf_main}

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

%files -n texlive-pdfmanagement-testphase
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pdfmanagement-testphase/
%doc %{_texmf_main}/doc/latex/pdfmanagement-testphase/

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
