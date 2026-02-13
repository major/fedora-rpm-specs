%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-humanities
Epoch:          12
Version:        svn75384
Release:        5%{?dist}
Summary:        Humanities packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-humanities.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adtrees.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adtrees.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-lds.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-lds.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-mouth.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-mouth.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-parse.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-parse.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/covington.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/covington.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dramatist.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dramatist.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvgloss.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvgloss.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecltree.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ecltree.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edfnotes.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edfnotes.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edmac.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/edmac.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledform.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledform.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledmac.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eledmac.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex-glossonly.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expex-glossonly.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e-next.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gb4e-next.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmverse.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmverse.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interlinear.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/interlinear.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jura.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jura.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juraabbrev.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juraabbrev.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juramisc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/juramisc.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jurarsp.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jurarsp.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langnames.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/langnames.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ledmac.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ledmac.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexikon.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexikon.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexref.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lexref.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ling-macros.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ling-macros.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguex.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguex.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguistix.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/linguistix.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturg.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturg.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturgy-cw.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liturgy-cw.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metrix.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metrix.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nnext.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nnext.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opbible.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/opbible.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parallel.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parallel.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parrun.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/parrun.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phonrule.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/phonrule.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plari.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plari.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/play.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/play.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poemscol.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poemscol.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetry.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetry.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetrytex.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/poetrytex.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qobitree.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qobitree.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qtree.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qtree.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reledmac.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reledmac.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rrgtrees.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rrgtrees.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rtklage.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rtklage.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay-pkg.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/screenplay-pkg.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sides.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sides.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stage.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stage.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textglos.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textglos.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thalie.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thalie.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theatre.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/theatre.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tree-dvips.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tree-dvips.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/verse.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/verse.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xyling.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xyling.doc.tar.xz

# Patches
Patch0:         texlive-rtklage-scrpage2-obsolete-fixes.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-adtrees
Requires:       texlive-bibleref
Requires:       texlive-bibleref-lds
Requires:       texlive-bibleref-mouth
Requires:       texlive-bibleref-parse
Requires:       texlive-collection-latex
Requires:       texlive-covington
Requires:       texlive-diadia
Requires:       texlive-dramatist
Requires:       texlive-dvgloss
Requires:       texlive-ecltree
Requires:       texlive-edfnotes
Requires:       texlive-edmac
Requires:       texlive-eledform
Requires:       texlive-eledmac
Requires:       texlive-expex
Requires:       texlive-expex-glossonly
Requires:       texlive-gb4e
Requires:       texlive-gb4e-next
Requires:       texlive-gmverse
Requires:       texlive-interlinear
Requires:       texlive-jura
Requires:       texlive-juraabbrev
Requires:       texlive-juramisc
Requires:       texlive-jurarsp
Requires:       texlive-langnames
Requires:       texlive-ledmac
Requires:       texlive-lexikon
Requires:       texlive-lexref
Requires:       texlive-ling-macros
Requires:       texlive-linguex
Requires:       texlive-linguistix
Requires:       texlive-liturg
Requires:       texlive-liturgy-cw
Requires:       texlive-metrix
Requires:       texlive-nnext
Requires:       texlive-opbible
Requires:       texlive-parallel
Requires:       texlive-parrun
Requires:       texlive-phonrule
Requires:       texlive-plari
Requires:       texlive-play
Requires:       texlive-poemscol
Requires:       texlive-poetry
Requires:       texlive-poetrytex
Requires:       texlive-qobitree
Requires:       texlive-qtree
Requires:       texlive-reledmac
Requires:       texlive-rrgtrees
Requires:       texlive-rtklage
Requires:       texlive-screenplay
Requires:       texlive-screenplay-pkg
Requires:       texlive-sides
Requires:       texlive-stage
Requires:       texlive-textglos
Requires:       texlive-thalie
Requires:       texlive-theatre
Requires:       texlive-tree-dvips
Requires:       texlive-verse
Requires:       texlive-xyling

%description
Packages for law, linguistics, social sciences, humanities, etc.


%package -n texlive-adtrees
Summary:        Macros for drawing adpositional trees
Version:        svn51618
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cancel.sty)
Requires:       tex(epic.sty)
Provides:       tex(adtrees.sty) = %{tl_version}

%description -n texlive-adtrees
This package provides a means to write adpositional trees, a formalism devoted
to representing natural language expressions. The package relies on epic and
cancel.

%package -n texlive-bibleref
Summary:        Format bible citations
Version:        svn75257
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsgen.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xstring.sty)
Provides:       tex(bibleref-xidx.sty) = %{tl_version}
Provides:       tex(bibleref.sty) = %{tl_version}

%description -n texlive-bibleref
The bibleref package offers consistent formatting of references to parts of the
Christian bible, in a number of well-defined formats. It depends on ifthen,
fmtcount, and amsgen.

%package -n texlive-bibleref-lds
Summary:        Bible references, including those to the scriptures of the Church of Jesus Christ of Latter Day Saints
Version:        svn25526
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref-mouth.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(bibleref-lds.sty) = %{tl_version}

%description -n texlive-bibleref-lds
The package extends the bibleref-mouth package to support references to the
scriptures of The Church of Jesus Christ of Latter-day Saints (LDS). The
package requires bibleref-mouth to run, and its reference syntax is the same as
that of the parent package.

%package -n texlive-bibleref-mouth
Summary:        Consistent formatting of Bible references
Version:        svn25527
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fmtcount.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(bibleref-mouth.sty) = %{tl_version}

%description -n texlive-bibleref-mouth
The package allows Bible references to be formatted in a consistent way. It is
similar to the bibleref package, except that the formatting macros are all
purely expandable -- that is, they are all implemented in TeX's mouth. This
means that they can be used in any expandable context, such as an argument to a
\url command.

%package -n texlive-bibleref-parse
Summary:        Specify Bible passages in human-readable format
Version:        svn22054
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(scrlfile.sty)
Provides:       tex(bibleref-parse.sty) = %{tl_version}

%description -n texlive-bibleref-parse
The package parses Bible passages that are given in human readable format. It
accepts a wide variety of formats. This allows for a simpler and more
convenient interface to the functionality of the bibleref package.

%package -n texlive-covington
Summary:        LaTeX macros for Linguistics
Version:        svn77216
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(varwidth.sty)
Provides:       tex(covington.sty) = %{tl_version}

%description -n texlive-covington
Numerous minor LaTeX enhancements for linguistics, including multiple accents
on the same letter, interline glosses (word-by-word translations), Discourse
Representation Structures, and example numbering.

%package -n texlive-dramatist
Summary:        Typeset dramas, both in verse and in prose
Version:        svn35866
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(dramatist.sty) = %{tl_version}

%description -n texlive-dramatist
This package is intended for typesetting drama of any length. It provides two
environments for typesetting dialogues in prose or in verse; new document
divisions corresponding to acts and scenes; macros that control the appearance
of characters and stage directions; and automatic generation of a `dramatis
personae' list.

%package -n texlive-dvgloss
Summary:        Facilities for setting interlinear glossed text
Version:        svn29103
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dvgloss.sty) = %{tl_version}

%description -n texlive-dvgloss
The package provides extensible macros for setting interlinear glossed text --
useful, for instance, for typing linguistics papers. The operative word here is
"extensible": few features are built in, but some flexible and powerful
facilities are included for adding your own.

%package -n texlive-ecltree
Summary:        Trees using epic and eepic macros
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ecltree.sty) = %{tl_version}

%description -n texlive-ecltree
The package recursively draws trees: each subtree is defined in a 'bundle'
environment, with a set of leaves described by \chunk macros. A chunk may have
a bundle environment inside it.

%package -n texlive-edfnotes
Summary:        Critical annotations to footnotes with ednotes
Version:        svn21540
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fnlineno.sty)
Provides:       tex(edfnotes.sty) = %{tl_version}

%description -n texlive-edfnotes
The package modifies the annotation commands and label-test mechanism of the
ednotes package so that critical notes appear on the pages and in the order
that one would expect.

%package -n texlive-edmac
Summary:        Typeset critical editions
Version:        svn72250
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(edmac.tex) = %{tl_version}
Provides:       tex(edmacfss.sty) = %{tl_version}
Provides:       tex(edstanza.tex) = %{tl_version}
Provides:       tex(tabmac.tex) = %{tl_version}

%description -n texlive-edmac
This is the type example package for typesetting scholarly critical editions.

%package -n texlive-eledform
Summary:        Define textual variants
Version:        svn38114
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(eledmac.sty)
Provides:       tex(eledform.sty) = %{tl_version}

%description -n texlive-eledform
The package provides commands to formalize textual variants in critical
editions typeset using eledmac.

%package -n texlive-eledmac
Summary:        Typeset scholarly editions
Version:        svn45418
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(eledmac.sty) = %{tl_version}
Provides:       tex(eledpar.sty) = %{tl_version}

%description -n texlive-eledmac
A package for typesetting scholarly critical editions, replacing the
established ledmac package. Ledmac itself was a LaTeX port of the plain TeX
EDMAC macros. The package supports indexing by page and by line numbers, and
simple tabular- and array-style environments. The package is distributed with
the related eledpar package. The package is now superseded by reledmac.

%package -n texlive-expex
Summary:        Linguistic examples and glosses, with reference capabilities
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(epltxchapno.sty) = %{tl_version}
Provides:       tex(epltxfn.sty) = %{tl_version}
Provides:       tex(eptexfn.tex) = %{tl_version}
Provides:       tex(expex-demo.tex) = %{tl_version}
Provides:       tex(expex.sty) = %{tl_version}
Provides:       tex(expex.tex) = %{tl_version}

%description -n texlive-expex
The package provides macros for typesetting linguistic examples and glosses,
with a refined mechanism for referencing examples and parts of examples. The
package can be used with LaTeX using the .sty wrapper or with PlainTex.

%package -n texlive-expex-glossonly
Summary:        Help gb4e, linguex, and covington users use the ExPex glossing macros
Version:        svn69914
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(covington.sty)
Requires:       tex(expex.sty)
# Ignoring dependency on gb4e-emulate.sty - not part of TeX Live
Requires:       tex(linguex.sty)
Provides:       tex(expex-glossonly.sty) = %{tl_version}

%description -n texlive-expex-glossonly
The ExPex package by John Frampton provides very fine-grained control over
glossing and example formatting, including unlimited gloss lines and various
ways of formatting multiline glosses. By contrast the cgloss4e glossing macros
provided with gb4e, linguex, and covington, although very capable at basic
glossing, lack the degree of customization that is sometimes needed for more
complex glossing. On the other hand, for those users who have heavily invested
in using either gb4e or linguex, or covington, shifting to ExPex can be quite
daunting and burdensome, especially since the basic syntax of the examples is
quite different. This package is an attempt to have the best of both worlds: it
allows gb4e, linguex and covington users to keep using those packages for basic
example numbering and formatting, but also allows them to use the glossing
macros that ExPex provides.

%package -n texlive-gb4e
Summary:        Linguistic tools
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cgloss4e.sty) = %{tl_version}
Provides:       tex(gb4e.sty) = %{tl_version}

%description -n texlive-gb4e
Provides an environment for linguistic examples, tools for glosses, and various
other goodies. The code was developed from the midnight and covington packages.

%package -n texlive-gb4e-next
Summary:        Linguistic tools
Version:        svn72692
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gb4e-next.sty) = %{tl_version}

%description -n texlive-gb4e-next
The package provides gb4e users two relative example reference commands. \Next
refers to the next example in the document and \Prev refers to the previous
example. No explicit label command is required.

%package -n texlive-gmverse
Summary:        A package for typesetting (short) poems
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gmverse.sty) = %{tl_version}

%description -n texlive-gmverse
A redefinition of the verse environment to make the \\ command optional for
line ends and to give it a possibility of optical centering and `right-hanging'
alignment of lines broken because of length.

%package -n texlive-interlinear
Summary:        A package for creating interlinear glossed texts with customizable formatting
Version:        svn72106
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-enumitem
Requires:       texlive-etoolbox
Requires:       texlive-l3packages
Requires:       texlive-marginnote
Requires:       texlive-xifthen
Requires:       texlive-xkeyval
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Provides:       tex(interlinear.sty) = %{tl_version}

%description -n texlive-interlinear
The interlinear package facilitates the creation of interlinear glossed texts,
commonly used in linguistic examples. It is based on the gb4e package and
builds upon its functionality to provide enhanced features. It offers extensive
customization options, allowing users to control font styles, formatting, and
layout. With predefined styles and margin note customization, interlinear
provides a flexible solution for presenting linguistic data.

%package -n texlive-jura
Summary:        A document class for German legal texts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(alphanum.sty) = %{tl_version}
Provides:       tex(jura.cls) = %{tl_version}

%description -n texlive-jura
Implements the standard layout for German term papers in law (one-and-half
linespacing, 7 cm margins, etc.). Includes alphanum that permits alphanumeric
section numbering (e.g., A. Introduction; III. International Law).

%package -n texlive-juraabbrev
Summary:        Abbreviations for typesetting (German) juridical documents
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(juraabbrev.sty) = %{tl_version}

%description -n texlive-juraabbrev
This package should be helpful for people working on (German) law. It helps you
to handle abbreviations and creates a list of those (pre-defined) abbreviations
that have actually been used in the document

%package -n texlive-juramisc
Summary:        Typesetting German juridical documents
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xspace.sty)
Provides:       tex(jurabase.sty) = %{tl_version}
Provides:       tex(jurabook.cls) = %{tl_version}
Provides:       tex(juraovw.cls) = %{tl_version}
Provides:       tex(juraurtl.cls) = %{tl_version}

%description -n texlive-juramisc
A collection of classes for typesetting court sentences, legal opinions, books
and dissertations for German lawyers. A jurabook class is also provided, which
may not yet be complete.

%package -n texlive-jurarsp
Summary:        Citations of judgements and official documents in (German) juridical documents
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xspace.sty)
Provides:       tex(jurarsp.sty) = %{tl_version}

%description -n texlive-jurarsp
This package should be helpful for people working on (German) law. It (ab)uses
BibTeX for citations of judgements and official documents. For this purpose, a
special BibTeX-style is provided.

%package -n texlive-langnames
Summary:        Name languages and their genetic affiliations consistently
Version:        svn69101
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(langnames.sty) = %{tl_version}
Provides:       tex(ln_fams_glot.tex) = %{tl_version}
Provides:       tex(ln_fams_wals.tex) = %{tl_version}
Provides:       tex(ln_langs_glot.tex) = %{tl_version}
Provides:       tex(ln_langs_glot_native.tex) = %{tl_version}
Provides:       tex(ln_langs_wals.tex) = %{tl_version}
Provides:       tex(ln_langs_wals_native.tex) = %{tl_version}

%description -n texlive-langnames
This package attempts to make the typing of language names, codes, and families
slightly easier by providing macros to access pre-defined
language--code--family combinations from two important databases, as well as
the possibility to create new combinations. It may be particularly useful for
large, collaborative projects as well as typologically minded ones with a
variety of language examples.

%package -n texlive-ledmac
Summary:        Typeset scholarly editions
Version:        svn41811
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(afoot.sty) = %{tl_version}
Provides:       tex(ledarab.sty) = %{tl_version}
Provides:       tex(ledmac.sty) = %{tl_version}
Provides:       tex(ledpar.sty) = %{tl_version}

%description -n texlive-ledmac
A macro package for typesetting scholarly critical editions. The ledmac package
is a LaTeX port of the plain TeX EDMAC macros. It supports indexing by page and
line number and simple tabular- and array-style environments. The package is
distributed with the related ledpar and ledarab packages. The package is now
superseded by reledmac.

%package -n texlive-lexikon
Summary:        Macros for a two language dictionary
Version:        svn17364
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ipa.sty)
Provides:       tex(lexikon.sty) = %{tl_version}

%description -n texlive-lexikon
Macros for a two language dictionary

%package -n texlive-lexref
Summary:        Convenient and uniform references to legal provisions
Version:        svn36026
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(nomencl.sty)
Requires:       tex(splitidx.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xstring.sty)
Provides:       tex(lexref.sty) = %{tl_version}

%description -n texlive-lexref
The package is aimed at continental lawyers (especially those in Switzerland
and Germany), allowing the user to make references to legal provisions
conveniently and uniformly. The package also allows the user to add cited Acts
to a nomenclature list (automatically), and to build specific indexes for each
cited Act. The package is still under development, and should be treated as an
'alpha'-release.

%package -n texlive-ling-macros
Summary:        Macros for typesetting formal linguistics
Version:        svn42268
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(pbox.sty)
Requires:       tex(relsize.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(ulem.sty)
Requires:       tex(upgreek.sty)
Provides:       tex(ling-macros.sty) = %{tl_version}

%description -n texlive-ling-macros
This package contains macros for typesetting glosses and formal expressions. It
covers a range of subfields in formal linguistics.

%package -n texlive-linguex
Summary:        Format linguists' examples
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tree-dvips.sty)
Requires:       tex(xspace.sty)
Provides:       tex(linguex.sty) = %{tl_version}
Provides:       tex(linguho.sty) = %{tl_version}
Provides:       tex(ps-trees.sty) = %{tl_version}

%description -n texlive-linguex
This bundle comprises two packages: The linguex package facilitates the
formatting of linguist examples, automatically taking care of example
numbering, indentations, indexed brackets, and the '*' in grammaticality
judgments. The ps-trees package provides linguistic trees, building on the
macros of tree-dvips, but overcoming some of the older package's shortcomings.

%package -n texlive-linguistix
Summary:        Enhanced support for linguistics
Version:        svn77571
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(linguistix-american.sty) = %{tl_version}
Provides:       tex(linguistix-base.sty) = %{tl_version}
Provides:       tex(linguistix-british.sty) = %{tl_version}
Provides:       tex(linguistix-english.sty) = %{tl_version}
Provides:       tex(linguistix-fixpex.sty) = %{tl_version}
Provides:       tex(linguistix-fonts.sty) = %{tl_version}
Provides:       tex(linguistix-glossing.sty) = %{tl_version}
Provides:       tex(linguistix-greek.sty) = %{tl_version}
Provides:       tex(linguistix-ipa.sty) = %{tl_version}
Provides:       tex(linguistix-languages.sty) = %{tl_version}
Provides:       tex(linguistix-leipzig.sty) = %{tl_version}
Provides:       tex(linguistix-logos.sty) = %{tl_version}
Provides:       tex(linguistix-marathi.sty) = %{tl_version}
Provides:       tex(linguistix-nfss.sty) = %{tl_version}
Provides:       tex(linguistix.sty) = %{tl_version}

%description -n texlive-linguistix
This is an experimental bundle of packages that provide enhanced support for
typesetting in linguistics. It can be used as a single package, or the packages
can be loaded independently for separate features. Currently, it provides the
following packages: LinguisTiX-base: A base package used by other LinguisTiX
siblings LinguisTiX-fixpex: Solves the compatibility bug between expex and
unicode-math LinguisTiX-fonts: General text in the New Computer Modern font
family LinguisTiX-ipa: IPA text in the New Computer Modern font family
LinguisTiX-glossing: Accessible interlinear glossing LinguisTiX-leipzig:
Leipzig-style glossing with tagging LinguisTiX-languages: Support for modern
multilingual typesetting LinguisTiX-logos: For printing the logos of the
LinguisTiX bundle LinguisTiX-nfss: Extra control over NFSS

%package -n texlive-liturg
Summary:        Support for typesetting Catholic liturgical texts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(color.sty)
Requires:       tex(ecclesiastic.sty)
Requires:       tex(lettrine.sty)
Provides:       tex(liturg.sty) = %{tl_version}

%description -n texlive-liturg
The packages offers simple macros for typesetting Catholic liturgical texts,
particularly Missal and Breviary texts. The package assumes availability of
Latin typesetting packages.

%package -n texlive-liturgy-cw
Summary:        Create Common Worship style documents
Version:        svn76053
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(bibleref.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(framed.sty)
Requires:       tex(geometry.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(liturgy-cw.sty) = %{tl_version}

%description -n texlive-liturgy-cw
This package greatly simplifies the typesetting of service sheets and booklets
in the style of the Common Worship liturgical resources of the Church of
England. The package provides commands for a number of liturgical elements,
including rubrics, responsories and 'required part' indicators.

%package -n texlive-metrix
Summary:        Typeset metric marks for Latin text
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(metrix.sty) = %{tl_version}

%description -n texlive-metrix
The package may be used to type the prosodics/metrics of (latin) verse; it
provides macros to typeset the symbols standing alone, and in combination with
symbols, giving automatic alignment. The package requires TikZ (including the
calc library), xpatch, and xparse (thus also requiring the experimental LaTeX3
environment).

%package -n texlive-nnext
Summary:        Extension for the gb4e package
Version:        svn56575
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(xspace.sty)
Provides:       tex(nnext.sty) = %{tl_version}

%description -n texlive-nnext
This is an add-on for the gb4e package used in linguistics. It implements the
\Next, \NNext, \Last, and \LLast commands from the linguex package or the
\nextx, \anextx, \lastx, \blastx, and \bblastx commands from the expex package.

%package -n texlive-opbible
Summary:        Creating a study Bible with OpTeX
Version:        svn77161
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(opbible-hebrew.tex) = %{tl_version}

%description -n texlive-opbible
This package includes OpTeX macros which allow to create a study Bible in many
language variants. The main Bible text is in separate files while the
commentary apparatus can be written in other files. TeX is able to join all
these data into a single print of a study Bible. Moreover, multiple language
variants and translation subvariants are provided.

%package -n texlive-parallel
Summary:        Typeset parallel texts
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(parallel.sty) = %{tl_version}

%description -n texlive-parallel
Provides a parallel environment which allows two potentially different texts to
be typeset in two columns, while maintaining alignment. The two columns may be
on the same page, or on facing pages. This arrangement of text is commonly used
when typesetting translations, but it can have value when comparing any two
texts.

%package -n texlive-parrun
Summary:        Typesets (two) streams of text running parallel
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(parrun.sty) = %{tl_version}

%description -n texlive-parrun
For typesetting translated text and the original source, parallel on the same
page, one above the other.

%package -n texlive-phonrule
Summary:        Typeset linear phonological rules
Version:        svn43963
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(phonrule.sty) = %{tl_version}

%description -n texlive-phonrule
The package provides macros for typesetting phonological rules like those in
'Sound Pattern of English' (Chomsky and Halle 1968).

%package -n texlive-plari
Summary:        Typesetting stageplay scripts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(plari.cls) = %{tl_version}

%description -n texlive-plari
Plari (the name comes from the Finnish usage for the working copy of a play) is
a report-alike class, without section headings, and with paragraphs vertically
separated rather than indented.

%package -n texlive-play
Summary:        Typeset drama using LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(play.cls) = %{tl_version}
Provides:       tex(play.sty) = %{tl_version}

%description -n texlive-play
A class and style file that supports the typesetting of plays, including
options for line numbering.

%package -n texlive-poemscol
Summary:        Typesetting Critical Editions of Poetry
Version:        svn56082
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(poemscol.sty) = %{tl_version}

%description -n texlive-poemscol
The package offers LaTeX macros for typesetting critical editions of poetry.
Its features include automatic linenumbering, generation of separate endnotes
sections for emendations, textual collations, and explanatory notes, special
marking for cases in which page breaks occur during stanza breaks, running
headers of the form 'Notes to pp. xx-yy' for the notes sections, index of
titles and first lines, and automatic generation of a table of contents.

%package -n texlive-poetry
Summary:        Facilities for typesetting poetry and poetical structure
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(imakeidx.sty)
Requires:       tex(modulus.sty)
Provides:       tex(poetry.sty) = %{tl_version}

%description -n texlive-poetry
This package provides some macros and general doodads for typesetting poetry.
There is, of course, already the excellent verse package, and the poetrytex
package provides some extra functionality on top of it. But poetry provides
much of the same functionality in a bit of a different way, and with a few
additional abilities, such as facilities for a list of poems, an index of first
lines, and some structural commands.

%package -n texlive-poetrytex
Summary:        Typeset anthologies of poetry
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tocloft.sty)
Provides:       tex(poetrytex.sty) = %{tl_version}

%description -n texlive-poetrytex
The package is designed to aid in the management and formatting of anthologies
of poetry and other writings; it does not concern itself with actually
typesetting the verse itself.

%package -n texlive-qobitree
Summary:        LaTeX macros for typesetting trees
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(qobitree.tex) = %{tl_version}

%description -n texlive-qobitree
Provides commands \branch and \leaf for specifying the elements of the tree;
you build up your tree with those commands, and then issue the \tree command to
typeset the whole.

%package -n texlive-qtree
Summary:        Draw tree structures
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(qtree.sty) = %{tl_version}

%description -n texlive-qtree
The package offers support for drawing tree diagrams, and is especially
suitable for linguistics use. It allows trees to be specified in a simple
bracket notation, automatically calculates branch sizes, and supports both
DVI/PostScript and PDF output by use of pict2e facilities. The package is a
development of the existing qobitree package, offering a new front end.

%package -n texlive-reledmac
Summary:        Typeset scholarly editions
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(reledmac.sty) = %{tl_version}
Provides:       tex(reledpar.sty) = %{tl_version}

%description -n texlive-reledmac
A package for typesetting scholarly critical editions, replacing the
established ledmac and eledmac packages. Ledmac itself was a LaTeX port of the
plain TeX EDMAC macros. The package supports indexing by page and by line
numbers, and simple tabular- and array-style environments. The package is
distributed with the related reledpar package.

%package -n texlive-rrgtrees
Summary:        Linguistic tree diagrams for Role and Reference Grammar (RRG) with LaTeX
Version:        svn27322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tree.sty)
Provides:       tex(rrgtrees.sty) = %{tl_version}

%description -n texlive-rrgtrees
A set of LaTeX macros that makes it easy to produce linguistic tree diagrams
suitable for Role and Reference Grammar (RRG). This package allows the
construction of trees with crossing lines, as is required by this theory for
many languages. There is no known limit on number of tree nodes or levels.
Requires the pst-node and pst-tree LaTeX packages.

%package -n texlive-rtklage
Summary:        A package for German lawyers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(rtklage.cls) = %{tl_version}

%description -n texlive-rtklage
RATeX is a newly developed bundle of packages and classes provided for German
lawyers. Now in the early beginning it only contains rtklage, a class to make
lawsuits.

%package -n texlive-screenplay
Summary:        A class file to typeset screenplays
Version:        svn27223
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hardmarg.sty) = %{tl_version}
Provides:       tex(screenplay.cls) = %{tl_version}

%description -n texlive-screenplay
The class implements the format recommended by the Academy of Motion Picture
Arts and Sciences.

%package -n texlive-screenplay-pkg
Summary:        Package version of the screenplay document class
Version:        svn44965
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(setspace.sty)
Provides:       tex(screenplay-pkg.sty) = %{tl_version}

%description -n texlive-screenplay-pkg
This package implements the tools of the screenplay document class in the form
of a package so that screenplay fragments can be included within another
document class. For full documentation of the available commands, please
consult the screenplay class documentation in addition to the included package
documentation.

%package -n texlive-sides
Summary:        A LaTeX class for typesetting stage plays
Version:        svn76924
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sides.cls) = %{tl_version}

%description -n texlive-sides
This is a LaTeX class for typesetting stage plays, based on the plari class
written by Antti-Juhani Kaijanaho in 1998. It has been updated and several
formatting changes have been made to it--most noticeably there are no longer
orphans.

%package -n texlive-stage
Summary:        A LaTeX class for stage plays
Version:        svn62929
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(stage.cls) = %{tl_version}

%description -n texlive-stage
Stage.cls is a LaTeX class for creating plays of any length in a standard
manuscript format for production and submission.

%package -n texlive-textglos
Summary:        Typeset and index linguistic gloss abbreviations
Version:        svn30788
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(textglos.sty) = %{tl_version}

%description -n texlive-textglos
The package provides a set of macros for in-line linguistic examples (as
opposed to interlinear glossing, set apart from the main text). It prevents
hyphenated examples from breaking across lines and consistently formats
phonemic examples, orthographic examples, and more.

%package -n texlive-thalie
Summary:        Typeset drama plays
Version:        svn65249
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(translations.sty)
Requires:       tex(xspace.sty)
Provides:       tex(thalie.sty) = %{tl_version}

%description -n texlive-thalie
The package provides tools to typeset drama plays. It defines commands to
introduce characters' lines, to render stage directions, to divide a play into
acts and scenes and to build the dramatis personae automatically.

%package -n texlive-theatre
Summary:        A sophisticated package for typesetting stage plays
Version:        svn45363
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-theatre-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-theatre-doc <= 11:%{version}

%description -n texlive-theatre
This package enables the user to typeset stage plays in a way that permits to
create highly customized printouts for each actor.

%package -n texlive-tree-dvips
Summary:        Trees and other linguists' macros
Version:        svn21751
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lingmacros.sty) = %{tl_version}
Provides:       tex(tree-dvips.sty) = %{tl_version}

%description -n texlive-tree-dvips
The package defines a mechanism for specifying connected trees that uses a
tabular environment to generate node positions. The package uses PostScript
code, loaded by dvips, so output can only be generated by use of dvips. The
package lingmacros.sty defines a few macros for linguists: \enumsentence for
enumerating sentence examples, simple tabular-based non-connected tree macros,
and gloss macros.

%package -n texlive-verse
Summary:        Aids for typesetting simple verse
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(verse.sty) = %{tl_version}

%description -n texlive-verse
The package documentation discusses approaches to the problem; the package is
strong on layout, from simple alternate-line indentation to the Mouse's tale
from Alice in Wonderland.

%package -n texlive-xyling
Summary:        Draw syntactic trees, etc., for linguistics literature, using xy-pic
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xy.sty)
Provides:       tex(xyling.sty) = %{tl_version}

%description -n texlive-xyling
The macros in this package model the construction of linguistic tree structures
as a genuinely graphical problem: they contain two types of objects, BRANCHES
and NODE LABELS, and these are positioned relative to a GRID. It is essential
that each of these three elements is constructed independent of the other two,
and hence they can be modified without unwanted side effects. The macros are
based on the xy-pic package.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Removing pre-built binary from opbible.doc
rm -rf %{buildroot}%{_texmf_main}/doc/optex/opbible/txs-gen/mod2tex

# Apply scrpage2 obsolete fix patches
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-rtklage-scrpage2-obsolete-fixes.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-adtrees
%license gpl2.txt
%{_texmf_main}/tex/latex/adtrees/
%doc %{_texmf_main}/doc/latex/adtrees/

%files -n texlive-bibleref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref/
%doc %{_texmf_main}/doc/latex/bibleref/

%files -n texlive-bibleref-lds
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-lds/
%doc %{_texmf_main}/doc/latex/bibleref-lds/

%files -n texlive-bibleref-mouth
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-mouth/
%doc %{_texmf_main}/doc/latex/bibleref-mouth/

%files -n texlive-bibleref-parse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-parse/
%doc %{_texmf_main}/doc/latex/bibleref-parse/

%files -n texlive-covington
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/covington/
%doc %{_texmf_main}/doc/latex/covington/

%files -n texlive-dramatist
%license gpl2.txt
%{_texmf_main}/tex/latex/dramatist/
%doc %{_texmf_main}/doc/latex/dramatist/

%files -n texlive-dvgloss
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dvgloss/
%doc %{_texmf_main}/doc/latex/dvgloss/

%files -n texlive-ecltree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ecltree/
%doc %{_texmf_main}/doc/latex/ecltree/

%files -n texlive-edfnotes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/edfnotes/
%doc %{_texmf_main}/doc/latex/edfnotes/

%files -n texlive-edmac
%license gpl2.txt
%{_texmf_main}/tex/generic/edmac/
%doc %{_texmf_main}/doc/generic/edmac/

%files -n texlive-eledform
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eledform/
%doc %{_texmf_main}/doc/latex/eledform/

%files -n texlive-eledmac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eledmac/
%doc %{_texmf_main}/doc/latex/eledmac/

%files -n texlive-expex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/expex/
%doc %{_texmf_main}/doc/generic/expex/

%files -n texlive-expex-glossonly
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/expex-glossonly/
%doc %{_texmf_main}/doc/latex/expex-glossonly/

%files -n texlive-gb4e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gb4e/
%doc %{_texmf_main}/doc/latex/gb4e/

%files -n texlive-gb4e-next
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gb4e-next/
%doc %{_texmf_main}/doc/latex/gb4e-next/

%files -n texlive-gmverse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gmverse/
%doc %{_texmf_main}/doc/latex/gmverse/

%files -n texlive-interlinear
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/interlinear/
%doc %{_texmf_main}/doc/latex/interlinear/

%files -n texlive-jura
%license gpl2.txt
%{_texmf_main}/tex/latex/jura/
%doc %{_texmf_main}/doc/latex/jura/

%files -n texlive-juraabbrev
%license gpl2.txt
%{_texmf_main}/makeindex/juraabbrev/
%{_texmf_main}/tex/latex/juraabbrev/
%doc %{_texmf_main}/doc/latex/juraabbrev/

%files -n texlive-juramisc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/juramisc/
%doc %{_texmf_main}/doc/latex/juramisc/

%files -n texlive-jurarsp
%license gpl2.txt
%{_texmf_main}/bibtex/bst/jurarsp/
%{_texmf_main}/tex/latex/jurarsp/
%doc %{_texmf_main}/doc/latex/jurarsp/

%files -n texlive-langnames
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/langnames/
%doc %{_texmf_main}/doc/latex/langnames/

%files -n texlive-ledmac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ledmac/
%doc %{_texmf_main}/doc/latex/ledmac/

%files -n texlive-lexikon
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lexikon/
%doc %{_texmf_main}/doc/latex/lexikon/

%files -n texlive-lexref
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/lexref/
%doc %{_texmf_main}/doc/latex/lexref/

%files -n texlive-ling-macros
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ling-macros/
%doc %{_texmf_main}/doc/latex/ling-macros/

%files -n texlive-linguex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/linguex/
%doc %{_texmf_main}/doc/latex/linguex/

%files -n texlive-linguistix
%license gpl3.txt
%{_texmf_main}/tex/latex/linguistix/
%doc %{_texmf_main}/doc/latex/linguistix/

%files -n texlive-liturg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liturg/
%doc %{_texmf_main}/doc/latex/liturg/

%files -n texlive-liturgy-cw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liturgy-cw/
%doc %{_texmf_main}/doc/latex/liturgy-cw/

%files -n texlive-metrix
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/metrix/
%doc %{_texmf_main}/doc/latex/metrix/

%files -n texlive-nnext
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nnext/
%doc %{_texmf_main}/doc/latex/nnext/

%files -n texlive-opbible
%license gpl2.txt
%{_texmf_main}/tex/optex/opbible/
%doc %{_texmf_main}/doc/optex/opbible/

%files -n texlive-parallel
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/parallel/
%doc %{_texmf_main}/doc/latex/parallel/

%files -n texlive-parrun
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/parrun/
%doc %{_texmf_main}/doc/latex/parrun/

%files -n texlive-phonrule
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/phonrule/
%doc %{_texmf_main}/doc/latex/phonrule/

%files -n texlive-plari
%license gpl2.txt
%{_texmf_main}/tex/latex/plari/
%doc %{_texmf_main}/doc/latex/plari/

%files -n texlive-play
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/play/
%doc %{_texmf_main}/doc/latex/play/

%files -n texlive-poemscol
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/poemscol/
%doc %{_texmf_main}/doc/latex/poemscol/

%files -n texlive-poetry
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/poetry/
%doc %{_texmf_main}/doc/latex/poetry/

%files -n texlive-poetrytex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/poetrytex/
%doc %{_texmf_main}/doc/latex/poetrytex/

%files -n texlive-qobitree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qobitree/
%doc %{_texmf_main}/doc/latex/qobitree/

%files -n texlive-qtree
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/qtree/
%doc %{_texmf_main}/doc/latex/qtree/

%files -n texlive-reledmac
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/reledmac/
%doc %{_texmf_main}/doc/latex/reledmac/

%files -n texlive-rrgtrees
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rrgtrees/
%doc %{_texmf_main}/doc/latex/rrgtrees/

%files -n texlive-rtklage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rtklage/
%doc %{_texmf_main}/doc/latex/rtklage/

%files -n texlive-screenplay
%license gpl2.txt
%{_texmf_main}/tex/latex/screenplay/
%doc %{_texmf_main}/doc/latex/screenplay/

%files -n texlive-screenplay-pkg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/screenplay-pkg/
%doc %{_texmf_main}/doc/latex/screenplay-pkg/

%files -n texlive-sides
%license gpl2.txt
%{_texmf_main}/tex/latex/sides/
%doc %{_texmf_main}/doc/latex/sides/

%files -n texlive-stage
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/stage/
%doc %{_texmf_main}/doc/latex/stage/

%files -n texlive-textglos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/textglos/
%doc %{_texmf_main}/doc/latex/textglos/

%files -n texlive-thalie
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thalie/
%doc %{_texmf_main}/doc/latex/thalie/

%files -n texlive-theatre
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/theatre/

%files -n texlive-tree-dvips
%license lppl1.3c.txt
%{_texmf_main}/dvips/tree-dvips/
%{_texmf_main}/tex/latex/tree-dvips/
%doc %{_texmf_main}/doc/latex/tree-dvips/

%files -n texlive-verse
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/verse/
%doc %{_texmf_main}/doc/latex/verse/

%files -n texlive-xyling
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xyling/
%doc %{_texmf_main}/doc/latex/xyling/

%changelog
* Wed Feb 11 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75384-5
- Update expex gb4e linguex linguistix parallel poetry verse
- Add cls Provides

* Mon Feb  9 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75384-4
- rebuild to land outside the side tag

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75384-3
- fix descriptions, update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75384-2
- regen, no deps from docs

* Thu Sep 18 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75384-1
- Update to TeX Live 2025
