%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langjapanese
Epoch:          12
Version:        svn76651
Release:        2%{?dist}
Summary:        Japanese

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langjapanese.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascmac.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascmac.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asternote.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asternote.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-japanese.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-japanese.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxbase.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxbase.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxcjkjatype.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxcjkjatype.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxcoloremoji.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxcoloremoji.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxghost.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxghost.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjaholiday.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjaholiday.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjalipsum.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjalipsum.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjaprnind.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjaprnind.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjatoucs.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjatoucs.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjscls.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxjscls.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxorigcapt.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxorigcapt.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxwareki.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bxwareki.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chuushaku.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chuushaku.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/convert-jpfonts.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/convert-jpfonts.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/endnotesj.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/endnotesj.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gckanbun.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gckanbun.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gentombow.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gentombow.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/haranoaji.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/haranoaji.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/haranoaji-extra.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/haranoaji-extra.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieejtran.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ieejtran.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifptex.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifptex.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifxptex.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifxptex.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/japanese-mathformulas.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/japanese-mathformulas.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/japanese-otf.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/japanese-otf.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jieeetran.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jieeetran.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jlreq.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jlreq.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jlreq-deluxe.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jlreq-deluxe.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jpneduenumerate.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jpneduenumerate.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jpnedumathsymbols.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jpnedumathsymbols.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jsclasses.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jsclasses.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kanbun.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kanbun.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-japanese.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-japanese.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexja.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexja.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luwa-ul.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luwa-ul.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mendex-doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mendex-doc.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/morisawa.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/morisawa.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/outoruby.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/outoruby.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pbibtex-base.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pbibtex-base.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pbibtex-manual.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pbibtex-manual.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex-tools.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platex-tools.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platexcheat.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/platexcheat.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plautopatch.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plautopatch.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-base.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-base.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-fonts.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-fonts.doc.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-manual.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-manual.doc.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxbase.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxbase.doc.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxchfon.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxchfon.doc.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxcjkcat.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxcjkcat.doc.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxjahyper.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxjahyper.doc.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxjodel.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxjodel.doc.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxrubrica.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxrubrica.doc.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxufont.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxufont.doc.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-ja.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-ja.doc.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-base.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-base.doc.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-fonts.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-fonts.doc.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wadalab.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wadalab.doc.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zxjafbfont.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zxjafbfont.doc.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zxjatype.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zxjatype.doc.tar.xz

# AppStream metadata for font components
Source126:        haranoaji.metainfo.xml
Source127:        haranoaji-extra.metainfo.xml
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-ascmac
Requires:       texlive-asternote
Requires:       texlive-babel-japanese
Requires:       texlive-bxbase
Requires:       texlive-bxcjkjatype
Requires:       texlive-bxcoloremoji
Requires:       texlive-bxghost
Requires:       texlive-bxjaholiday
Requires:       texlive-bxjalipsum
Requires:       texlive-bxjaprnind
Requires:       texlive-bxjatoucs
Requires:       texlive-bxjscls
Requires:       texlive-bxorigcapt
Requires:       texlive-bxwareki
Requires:       texlive-chuushaku
Requires:       texlive-collection-langcjk
Requires:       texlive-convbkmk
Requires:       texlive-convert-jpfonts
Requires:       texlive-endnotesj
Requires:       texlive-gckanbun
Requires:       texlive-gentombow
Requires:       texlive-haranoaji
Requires:       texlive-haranoaji-extra
Requires:       texlive-ieejtran
Requires:       texlive-ifptex
Requires:       texlive-ifxptex
Requires:       texlive-ipaex
Requires:       texlive-japanese-mathformulas
Requires:       texlive-japanese-otf
Requires:       texlive-jieeetran
Requires:       texlive-jlreq
Requires:       texlive-jlreq-deluxe
Requires:       texlive-jpneduenumerate
Requires:       texlive-jpnedumathsymbols
Requires:       texlive-jsclasses
Requires:       texlive-kanbun
Requires:       texlive-lshort-japanese
Requires:       texlive-luatexja
Requires:       texlive-luwa-ul
Requires:       texlive-mendex-doc
Requires:       texlive-morisawa
Requires:       texlive-outoruby
Requires:       texlive-pbibtex-base
Requires:       texlive-pbibtex-manual
Requires:       texlive-platex
Requires:       texlive-platex-tools
Requires:       texlive-platexcheat
Requires:       texlive-plautopatch
Requires:       texlive-ptex
Requires:       texlive-ptex-base
Requires:       texlive-ptex-fontmaps
Requires:       texlive-ptex-fonts
Requires:       texlive-ptex-manual
Requires:       texlive-ptex2pdf
Requires:       texlive-pxbase
Requires:       texlive-pxchfon
Requires:       texlive-pxcjkcat
Requires:       texlive-pxjahyper
Requires:       texlive-pxjodel
Requires:       texlive-pxrubrica
Requires:       texlive-pxufont
Requires:       texlive-texlive-ja
Requires:       texlive-uplatex
Requires:       texlive-uptex
Requires:       texlive-uptex-base
Requires:       texlive-uptex-fonts
Requires:       texlive-wadalab
Requires:       texlive-zxjafbfont
Requires:       texlive-zxjatype

%description
Support for Japanese; additional packages are in collection-langcjk.


%package -n texlive-ascmac
Summary:        Boxes and picture macros with Japanese vertical writing support
Version:        svn53411
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ascmac.sty) = %{tl_version}
Provides:       tex(tascmac.sty) = %{tl_version}

%description -n texlive-ascmac
The bundle provides boxes and picture macros with Japanese vertical writing
support. It uses only native picture macros and fonts for drawing boxes and is
thus driver-independent. Formerly part of the Japanese pLaTeX bundle, it now
supports all LaTeX engines.

%package -n texlive-asternote
Summary:        Annotation symbols enclosed in square brackets and marked with an asterisk
Version:        svn63838
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(asternote.sty) = %{tl_version}

%description -n texlive-asternote
This LaTeX package can output annotation symbols enclosed in square brackets
and marked with an asterisk.

%package -n texlive-babel-japanese
Summary:        Babel support for Japanese
Version:        svn57733
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(japanese.ldf) = %{tl_version}

%description -n texlive-babel-japanese
This package provides a japanese option for the babel package. It defines all
the language definition macros in Japanese. Currently this package works with
pLaTeX, upLaTeX, XeLaTeX and LuaLaTeX.

%package -n texlive-bxbase
Summary:        BX bundle base components
Version:        svn66115
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifxetex.sty)
Provides:       tex(bxbase.def) = %{tl_version}
Provides:       tex(bxbase.sty) = %{tl_version}
Provides:       tex(bxtoolbox-ext.def) = %{tl_version}
Provides:       tex(bxtoolbox-ja.def) = %{tl_version}
Provides:       tex(bxtoolbox.def) = %{tl_version}
Provides:       tex(bxtoolbox.sty) = %{tl_version}
Provides:       tex(bxutf8.def) = %{tl_version}
Provides:       tex(bxutf8x.def) = %{tl_version}
Provides:       tex(zxbase.sty) = %{tl_version}

%description -n texlive-bxbase
The main purpose of this bundle is to serve as an underlying library for other
packages created by the same author (their names start with "BX" or "PX").
However bxbase package contains a few user-level commands and is of some use by
itself.

%package -n texlive-bxcjkjatype
Summary:        Typeset Japanese with pdfLaTeX and CJK
Version:        svn67705
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(CJK.sty)
Requires:       tex(CJKpunct.sty)
Requires:       tex(CJKspace.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Provides:       tex(bxcjkjatype.sty) = %{tl_version}

%description -n texlive-bxcjkjatype
The package provides a working configuration of the CJK package, suitable for
Japanese typesetting of moderate quality. Moreover, it facilitates use of the
CJK package for pLaTeX users, by providing commands that are similar to those
used by the pLaTeX kernel and some other packages used with it.

%package -n texlive-bxcoloremoji
Summary:        Use color emojis more conveniently
Version:        svn74806
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-twemojis
Requires:       tex(bxghost-lib.sty)
Requires:       tex(bxghost.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(twemojis.sty)
Provides:       tex(bxcoloremoji-names.def) = %{tl_version}
Provides:       tex(bxcoloremoji.sty) = %{tl_version}

%description -n texlive-bxcoloremoji
This package lets users output color emojis in LaTeX documents. Compared to
other packages with similar functionality, this package has the following
merits: It supports all major LaTeX engines. Emojis can be entered as the
characters themselves, as their Unicode code values, or as their short names.
It works reasonably well in PDF strings when using hyperref. Emojis can be
handled properly even in Japanese typesetting environments. This package has
been widely used among the Japanese LaTeX community, but there are already many
emoji packages on CTAN and in TeX Live. To avoid uploading a large amount of
emoji image data that are essentially identical, the package was revised in
version 1.0 so that the image output was delegated to the twmojis package.
Therefore, this package now contains no image data.

%package -n texlive-bxghost
Summary:        Ghost insertion for proper xkanjiskip
Version:        svn66147
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(luatexja-adjust.sty)
Requires:       tex(luatexja.sty)
Provides:       tex(bxghost-lib.sty) = %{tl_version}
Provides:       tex(bxghost.sty) = %{tl_version}

%description -n texlive-bxghost
The package provides two commands to help authors for documents in Japanese to
insert proper xkanjiskips. It supports LuaTeX, XeTeX, pTeX, upTeX, and ApTeX
(pTeX-ng).

%package -n texlive-bxjaholiday
Summary:        Support for Japanese holidays
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bxjaholiday.sty) = %{tl_version}

%description -n texlive-bxjaholiday
This LaTeX package provides a command to convert dates to names of Japanese
holidays. Another command, converting dates to the day of the week in Japanese,
is available as a free gift. Further (lower-level) APIs are provided for expl3.
The package supports pdfTeX, XeTeX, LuaTeX, pTeX, and upTeX.

%package -n texlive-bxjalipsum
Summary:        Dummy text in Japanese
Version:        svn67620
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(intcalc.sty)
Provides:       tex(bxjalipsum.sty) = %{tl_version}

%description -n texlive-bxjalipsum
This package enables users to print some Japanese text that can be used as
dummy text. It is a Japanese counterpart of the lipsum package. Since there is
no well-known nonsense text like Lipsum in the Japanese language, the package
uses some real text in public domain.

%package -n texlive-bxjaprnind
Summary:        Adjust the position of parentheses at paragraph head
Version:        svn59641
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bxtoolbox.sty)
Requires:       tex(everyhook.sty)
Provides:       tex(bxjaprnind.sty) = %{tl_version}

%description -n texlive-bxjaprnind
In Japanese typesetting, opening parentheses placed at the beginning of
paragraphs or lines are treated specially; for example, while the paragraph
indent before normal kanji characters is 1em, the indent before parentheses can
be 0.5em, 1em or 1.5em deoending on the local rule in effect.

%package -n texlive-bxjatoucs
Summary:        Convert Japanese character code to Unicode
Version:        svn71870
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(bxjatoucs.sty) = %{tl_version}

%description -n texlive-bxjatoucs
This package is meant for macro/package developers: It provides function-like
(fully-expandable) macros that convert a character code value in one of several
Japanese encodings to a Unicode value. Supported source encodings are:
ISO-2022-JP (jis), EUC-JP (euc), Shift_JIS (sjis), and the Adobe-Japan1 glyph
set.

%package -n texlive-bxjscls
Summary:        Japanese document class collection for all major engines
Version:        svn75447
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
# Ignoring dependency on bxpandola.sty - not part of TeX Live
Requires:       tex(inputenc.sty)
Provides:       tex(bxjscjkcat.sty) = %{tl_version}
Provides:       tex(bxjscompat.sty) = %{tl_version}
Provides:       tex(bxjsja-minimal.def) = %{tl_version}
Provides:       tex(bxjsja-modern.def) = %{tl_version}
Provides:       tex(bxjsja-pandoc.def) = %{tl_version}
Provides:       tex(bxjsja-standard.def) = %{tl_version}
Provides:       tex(bxjspandoc.sty) = %{tl_version}

%description -n texlive-bxjscls
This package provides an extended version of the Japanese document class
collection provided by jsclasses. While the original version supports only
pLaTeX and upLaTeX, the extended version also supports pdfLaTeX, XeLaTeX and
LuaLaTeX, with the aid of suitable packages that provide capability of Japanese
typesetting.

%package -n texlive-bxorigcapt
Summary:        To retain the original caption names when using Babel
Version:        svn64072
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(bxorigcapt.sty) = %{tl_version}

%description -n texlive-bxorigcapt
This package forces the caption names (\chaptername, \today, etc) declared by
the document class in use to be used as the caption names for a specific
language introduced by the Babel package.

%package -n texlive-bxwareki
Summary:        Convert dates from Gregorian to Japanese calender
Version:        svn67594
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bxwareki-cd.def) = %{tl_version}
Provides:       tex(bxwareki.sty) = %{tl_version}

%description -n texlive-bxwareki
This LaTeX package provides commands to convert from the Gregorian calendar (e.
g. 2018/8/28) to the Japanese rendering of the Japanese calendar (e. g. Heisei
30 nen 8 gatsu 28 nichi; actually with kanji characters). You can choose
whether the numbers are written in Western numerals or kanji numerals. Note
that the package only deals with dates in the year 1873 or later, where the
Japanese calendar is really a Gregorian calendar with a different notation of
years.

%package -n texlive-chuushaku
Summary:        Flexible book notes in Japanese
Version:        svn73263
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(framed.sty)
Requires:       tex(tikz.sty)
Provides:       tex(chuushaku.sty) = %{tl_version}

%description -n texlive-chuushaku
This style file is designed for compiling book notes in Japanese as part of the
body text. ("Chuushaku" means "booknotes" in Japanese.) The "remember picture"
feature automatically calculates coordinates, eliminating the need for manual
adjustment of note positions. The main packages used in chuushaku.sty are TikZ,
amsmath, framed, and calc.

%package -n texlive-convert-jpfonts
Summary:        Convert half-width Japanese to full-width beautifully
Version:        svn73551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xparse.sty)
Provides:       tex(convert-jpfonts.sty) = %{tl_version}

%description -n texlive-convert-jpfonts
This style file is designed for converting Japanese half-width characters to
full-width characters beautifully. This is useful when alphabet characters
don't render properly in a Japanese font.

%package -n texlive-endnotesj
Summary:        Japanese-style endnotes
Version:        svn47703
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(endnotes.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(otf.sty)
# Ignoring dependency on utf.sty - not part of TeX Live
Provides:       tex(endnotesj.sty) = %{tl_version}

%description -n texlive-endnotesj
This package provides customized styles for endnotes to be used with Japanese
documents. It can be used on pLaTeX, upLaTeX, and LuaLaTeX (LuaTeX-ja).

%package -n texlive-gckanbun
Summary:        Kanbun typesetting for (u)pLaTeX and LuaLaTeX
Version:        svn77307
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bxghost.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifuptex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(luatexja-adjust.sty)
Provides:       tex(gckanbun.sty) = %{tl_version}

%description -n texlive-gckanbun
This package provides a Kanbun (Han Wen , "Chinese writing") typesetting for
(u)pLaTeX and LuaLaTeX.

%package -n texlive-gentombow
Summary:        Generate Japanese-style crop marks
Version:        svn64333
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(filehook.sty)
Requires:       tex(pxatbegshi.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(textpos.sty)
Provides:       tex(bounddvi.sty) = %{tl_version}
Provides:       tex(gentombow.sty) = %{tl_version}
Provides:       tex(pxesopic.sty) = %{tl_version}
Provides:       tex(pxgentombow.sty) = %{tl_version}
Provides:       tex(pxpdfpages.sty) = %{tl_version}
Provides:       tex(pxtextpos.sty) = %{tl_version}

%description -n texlive-gentombow
This bundle provides a LaTeX package for generating Japanese-style crop marks
(called 'tombow' in Japanese) for practical use in self-publishing. The bundle
contains the following packages: gentombow.sty: Generate crop marks (called
'tombow' in Japanese) for practical use in self-publishing. It provides the
core 'tombow' feature if not available. pxgentombow.sty: Superseded by
gentombow.sty; kept for compatibility only. bounddvi.sty: Set papersize special
to DVI file. Can be used on LaTeX/pLaTeX/upLaTeX (with DVI output mode) with
dvips or dvipdfmx drivers.

%package -n texlive-haranoaji
Summary:        Harano Aji Fonts
Version:        svn76078
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-haranoaji
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are fonts obtained
by replacing Adobe-Identity-0 (AI0) CIDs of Source Han fonts (Source Han Serif
and Source Han Sans) with Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7
weights each for Mincho and Gothic.

%package -n texlive-haranoaji-extra
Summary:        Harano Aji Fonts
Version:        svn76079
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-haranoaji-extra
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are fonts obtained
by replacing Adobe-Identity-0 (AI0) CIDs of Source Han fonts (Source Han Serif
and Source Han Sans) with Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7
weights each for Mincho and Gothic.

%package -n texlive-ieejtran
Summary:        Unofficial bibliography style file for the Institute of Electrical Engineers of Japan
Version:        svn76790
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ieejtran
This package provides an unofficial BibTeX style for authors of the Institute
of Electrical Engineers of Japan (IEEJ) transactions journals and conferences.

%package -n texlive-ifptex
Summary:        Check if the engine is pTeX or one of its derivatives
Version:        svn66803
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(ifptex.sty) = %{tl_version}
Provides:       tex(ifuptex.sty) = %{tl_version}

%description -n texlive-ifptex
The ifptex package is a counterpart of ifxetex, ifluatex, etc. for the ptex
engine. The ifuptex package is an alias to ifptex provided for backward
compatibility.

%package -n texlive-ifxptex
Summary:        Detect pTeX and its derivatives
Version:        svn46153
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ifxptex.sty) = %{tl_version}

%description -n texlive-ifxptex
The package provides commands for detecting pTeX and its derivatives (e-pTeX,
upTeX, e-upTeX, and ApTeX). Both LaTeX and plain TeX are supported.

%package -n texlive-ipaex
Summary:        IPA (Japanese) fonts
Version:        svn61719
License:        IPA
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ipaex
The fonts provide fixed-width glyphs for Kana and Kanji characters,
proportional width glyphs for Western characters.

%package -n texlive-japanese-mathformulas
Summary:        Compiling basic math formulas in Japanese using LuaLaTeX
Version:        svn64678
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(esvect.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(luatexja-fontspec.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(luatexja.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(japanese-mathformulas.sty) = %{tl_version}

%description -n texlive-japanese-mathformulas
This is a style file for compiling basic maths formulas in Japanese using
LuaLaTeX. \NewDocumentCommand allows you to specify whether the formula should
be used within a sentence or on a new line. The main packages used in
japanese-mathformulas.sty are amsmath, amssymb, siunitx, ifthen, xparse, TikZ,
mathtools, and graphics.

%package -n texlive-japanese-otf
Summary:        Advanced font selection for platex and its friends
Version:        svn77048
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(ajmacros.sty) = %{tl_version}
Provides:       tex(mlcid.sty) = %{tl_version}
Provides:       tex(mlutf.sty) = %{tl_version}
Provides:       tex(otf.sty) = %{tl_version}
Provides:       tex(redeffont.sty) = %{tl_version}

%description -n texlive-japanese-otf
The package contains pLaTeX support files and virtual fonts for supporting a
wide variety of fonts in LaTeX using the pTeX engine.

%package -n texlive-jieeetran
Summary:        Unofficial BibTeX style for citing Japanese articles in IEEE format
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jieeetran
This package provides an unofficial BibTeX style for authors trying to cite
Japanese articles in the Institute of Electrical and Electronics Engineers
(IEEE) format.

%package -n texlive-jlreq
Summary:        Japanese document class based on requirements for Japanese text layout
Version:        svn76924
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(filehook.sty)
Provides:       tex(jlreq-complements.sty) = %{tl_version}
Provides:       tex(jlreq-helpers.sty) = %{tl_version}
Provides:       tex(jlreq-trimmarks.sty) = %{tl_version}

%description -n texlive-jlreq
This package provides a Japanese document class based on requirements for
Japanese text layout. The class file and the JFM (Japanese font metric) files
for LuaTeX-ja / pLaTeX / upLaTeX are provided.

%package -n texlive-jlreq-deluxe
Summary:        Multi-weight Japanese font support for the jlreq class
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pxjodel.sty)
Provides:       tex(jlreq-deluxe.sty) = %{tl_version}

%description -n texlive-jlreq-deluxe
This package provides multi-weight Japanese font support for the jlreq class.

%package -n texlive-jpneduenumerate
Summary:        Enumerative expressions in Japanese education
Version:        svn72898
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(otf.sty)
Requires:       tex(refcount.sty)
Provides:       tex(jpneduenumerate.sty) = %{tl_version}

%description -n texlive-jpneduenumerate
Mathematical equation representation in Japanese education differs somewhat
from the standard LaTeX writing style. This package introduces enumerative
expressions in Japanese education.

%package -n texlive-jpnedumathsymbols
Summary:        Mathematical equation representation in Japanese education
Version:        svn72959
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(empheq.sty)
Requires:       tex(luatexja-otf.sty)
Requires:       tex(otf.sty)
Requires:       tex(xparse.sty)
Provides:       tex(jpnedumathsymbols.sty) = %{tl_version}

%description -n texlive-jpnedumathsymbols
Mathematical equation representation in Japanese education differs somewhat
from the standard LaTeX writing style. This package introduces mathematical
equation representation in Japanese education.

%package -n texlive-jsclasses
Summary:        Classes tailored for use with Japanese
Version:        svn75174
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(jslogo.sty) = %{tl_version}
Provides:       tex(jsverb.sty) = %{tl_version}
Provides:       tex(minijs.sty) = %{tl_version}
Provides:       tex(okumacro.sty) = %{tl_version}
Provides:       tex(okuverb.sty) = %{tl_version}

%description -n texlive-jsclasses
Classes jsarticle and jsbook are provided, together with packages okumacro and
okuverb. These classes are designed to work under ASCII Corporation's Japanese
TeX system ptex.

%package -n texlive-kanbun
Summary:        Typeset kanbun-kundoku with support for kanbun annotation
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(xparse.sty)
Provides:       tex(kanbun.sty) = %{tl_version}

%description -n texlive-kanbun
This package allows users to manually input macros for elements in a
kanbun-kundoku (Han Wen Xun Du ) paragraph. More importantly, it accepts plain
text input in the "kanbun annotation" form when used with LuaLaTeX, which
allows typesetting kanbun-kundoku paragraphs efficiently.

%package -n texlive-lshort-japanese
Summary:        Japanese version of A Short Introduction to LaTeX2e
Version:        svn36207
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-japanese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-japanese-doc <= 11:%{version}

%description -n texlive-lshort-japanese
Japanese version of A Short Introduction to LaTeX2e

%package -n texlive-luatexja
Summary:        Typeset Japanese with Lua(La)TeX
Version:        svn77538
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-luatexbase
Requires:       tex(array.sty)
Requires:       tex(collcell.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everyhook.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(listings.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase-cctb.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(preview.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stfloats.sty)
Requires:       tex(tascmac.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xunicode.sty)
Provides:       tex(lltjcore-241201.sty) = %{tl_version}
Provides:       tex(lltjcore.sty) = %{tl_version}
Provides:       tex(lltjdefs.sty) = %{tl_version}
Provides:       tex(lltjext.sty) = %{tl_version}
Provides:       tex(lltjfont.sty) = %{tl_version}
Provides:       tex(lltjp-array.sty) = %{tl_version}
Provides:       tex(lltjp-atbegshi.sty) = %{tl_version}
Provides:       tex(lltjp-collcell.sty) = %{tl_version}
Provides:       tex(lltjp-everyshi.sty) = %{tl_version}
Provides:       tex(lltjp-fontspec.sty) = %{tl_version}
Provides:       tex(lltjp-footmisc.sty) = %{tl_version}
Provides:       tex(lltjp-geometry.sty) = %{tl_version}
Provides:       tex(lltjp-listings.sty) = %{tl_version}
Provides:       tex(lltjp-microtype.sty) = %{tl_version}
Provides:       tex(lltjp-preview.sty) = %{tl_version}
Provides:       tex(lltjp-siunitx.sty) = %{tl_version}
Provides:       tex(lltjp-stfloats.sty) = %{tl_version}
Provides:       tex(lltjp-tascmac.sty) = %{tl_version}
Provides:       tex(lltjp-unicode-math.sty) = %{tl_version}
Provides:       tex(lltjp-xunicode.sty) = %{tl_version}
Provides:       tex(ltj-base.sty) = %{tl_version}
Provides:       tex(ltj-kinsoku.tex) = %{tl_version}
Provides:       tex(ltj-latex.sty) = %{tl_version}
Provides:       tex(ltj-plain.sty) = %{tl_version}
Provides:       tex(luatexja-adjust.sty) = %{tl_version}
Provides:       tex(luatexja-ajmacros.sty) = %{tl_version}
Provides:       tex(luatexja-compat.sty) = %{tl_version}
Provides:       tex(luatexja-core.sty) = %{tl_version}
Provides:       tex(luatexja-fontspec-29e.sty) = %{tl_version}
Provides:       tex(luatexja-fontspec.sty) = %{tl_version}
Provides:       tex(luatexja-otf.sty) = %{tl_version}
Provides:       tex(luatexja-preset.sty) = %{tl_version}
Provides:       tex(luatexja-ruby.sty) = %{tl_version}
Provides:       tex(luatexja-zhfonts.sty) = %{tl_version}
Provides:       tex(luatexja.sty) = %{tl_version}

%description -n texlive-luatexja
The package offers support for typesetting Japanese documents with LuaTeX.
Either of the Plain and LaTeX2e formats may be used with the package.

%package -n texlive-luwa-ul
Summary:        Provides underlines and other highlighting which can be used in vertical mode
Version:        svn77595
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(lua-ul.sty)
Requires:       tex(luacolor.sty)
Requires:       tex(luatexja-adjust.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(luwa-ul.sty) = %{tl_version}

%description -n texlive-luwa-ul
This package provides underlining and highlighting that remain intact even in
vertical writing environments and when used together with ruby text. It
internally uses lua-ul package, so it can be used only under LuaLaTeX.

%package -n texlive-mendex-doc
Summary:        Documentation for Mendex index processor
Version:        svn75172
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mendex-doc
This package provides documentation for Mendex (Japanese index processor). The
source code of the program is not included, it can be obtained from TeX Live
subversion repository.

%package -n texlive-morisawa
Summary:        Enables selection of 5 standard Japanese fonts for pLaTeX + dvips
Version:        svn46946
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(morisawa.sty) = %{tl_version}

%description -n texlive-morisawa
The package enables selection of 5 standard Japanese fonts for pLaTeX + dvips.
It was originally written by Haruhiko Okumura as part of jsclasses bundle, and
the TFM/VF files were previously distributed as part of the ptex-fonts package.

%package -n texlive-outoruby
Summary:        Ruby with line break support for Japanese text
Version:        svn74638
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-pxrubrica
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pxrubrica.sty)
Provides:       tex(outoruby.sty) = %{tl_version}

%description -n texlive-outoruby
This package provides the \outoruby command, which supports line breaks when
typesetting ruby anotations. It automatically switches between appropriate ruby
forms at the beginning and the end of lines according to JIS X 4051 and JLReq.
This package depends on pxrubrica and supports any engine that is supported by
that package.

%package -n texlive-pbibtex-base
Summary:        Bibliography styles and miscellaneous files for pBibTeX
Version:        svn66085
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pbibtex-base
These are miscellaneous files, including bibliography styles (.bst), for
pBibTeX, which is a Japanese extended version of BibTeX contained in TeX Live.
The bundle is a redistribution derived from the ptex-texmf distribution by
ASCII MEDIA WORKS.

%package -n texlive-pbibtex-manual
Summary:        Documentation files for (u)pBibTeX
Version:        svn66181
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pbibtex-manual-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pbibtex-manual-doc <= 11:%{version}

%description -n texlive-pbibtex-manual
The bundle contains documentation files for Japanese pBibTeX and upBibTeX. For
historical reasons, this also contains old documentation files for JBibTeX.

%package -n texlive-platex
Summary:        PLaTeX2e and miscellaneous macros for pTeX
Version:        svn73848
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-babel
Requires:       texlive-cm
Requires:       texlive-firstaid
Requires:       texlive-hyphen-base
Requires:       texlive-knuth-lib
Requires:       texlive-l3backend
Requires:       texlive-l3backend-dev
Requires:       texlive-l3kernel
Requires:       texlive-l3kernel-dev
Requires:       texlive-latex
Requires:       texlive-latex-base-dev
Requires:       texlive-latex-firstaid-dev
Requires:       texlive-latex-fonts
Requires:       texlive-platex
Requires:       texlive-ptex
Requires:       texlive-ptex-fonts
Requires:       texlive-tex-ini-files
Requires:       texlive-unicode-data
Requires:       texlive-uptex
Requires:       tex(oldlfont.sty)
Requires:       tex(plautopatch.sty)
Provides:       tex(exppl2e.sty) = %{tl_version}
Provides:       tex(jarticle.sty) = %{tl_version}
Provides:       tex(jbook.sty) = %{tl_version}
Provides:       tex(jreport.sty) = %{tl_version}
Provides:       tex(kinsoku.tex) = %{tl_version}
Provides:       tex(oldpfont.sty) = %{tl_version}
Provides:       tex(pfltrace.sty) = %{tl_version}
Provides:       tex(pl209.def) = %{tl_version}
Provides:       tex(platexrelease.sty) = %{tl_version}
Provides:       tex(plexpl3.sty) = %{tl_version}
Provides:       tex(plext.sty) = %{tl_version}
Provides:       tex(ptrace.sty) = %{tl_version}
Provides:       tex(tarticle.sty) = %{tl_version}
Provides:       tex(tbook.sty) = %{tl_version}
Provides:       tex(treport.sty) = %{tl_version}

%description -n texlive-platex
The bundle provides pLaTeX2e and miscellaneous macros for pTeX and e-pTeX. This
is a community edition forked from the original ASCII edition (ptex-texmf-2.5).

%package -n texlive-platex-tools
Summary:        PLaTeX standard tools bundle
Version:        svn72097
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(delarray.sty)
Requires:       tex(doc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everysel.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(ftnright.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(plext.sty)
Requires:       tex(ptrace.sty)
# Ignoring dependency on uptrace.sty - not part of TeX Live
Requires:       tex(xspace.sty)
Provides:       tex(plarray.sty) = %{tl_version}
Provides:       tex(pldocverb.sty) = %{tl_version}
Provides:       tex(plextarray.sty) = %{tl_version}
Provides:       tex(plextcolortbl.sty) = %{tl_version}
Provides:       tex(plextdelarray.sty) = %{tl_version}
Provides:       tex(pxatbegshi.sty) = %{tl_version}
Provides:       tex(pxeverysel.sty) = %{tl_version}
Provides:       tex(pxeveryshi.sty) = %{tl_version}
Provides:       tex(pxftnright.sty) = %{tl_version}
Provides:       tex(pxmulticol.sty) = %{tl_version}
Provides:       tex(pxxspace.sty) = %{tl_version}

%description -n texlive-platex-tools
This bundle is an extended version of the latex-tools bundle developed by the
LaTeX team, mainly intended to support pLaTeX2e and upLaTeX2e. Currently
patches for the latex-tools bundle and Martin Schroder's ms bundle are
included.

%package -n texlive-platexcheat
Summary:        A LaTeX cheat sheet, in Japanese
Version:        svn49557
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-platexcheat-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-platexcheat-doc <= 11:%{version}

%description -n texlive-platexcheat
This is a translation to Japanese of Winston Chang's LaTeX cheat sheet (a
reference sheet for writing scientific papers). It has been adapted to Japanese
standards using pLaTeX, and also attached additional information of "standard
LaTeX" (especially about math-mode).

%package -n texlive-plautopatch
Summary:        Automated patches for pLaTeX/upLaTeX
Version:        svn64072
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(arydshln.sty)
Requires:       tex(filehook.sty)
Requires:       tex(pgfrcs.sty)
Requires:       tex(plarray.sty)
Requires:       tex(plext.sty)
Requires:       tex(plextarray.sty)
Requires:       tex(plextcolortbl.sty)
Requires:       tex(plextdelarray.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(stfloats.sty)
Provides:       tex(plarydshln.sty) = %{tl_version}
Provides:       tex(plautopatch.sty) = %{tl_version}
Provides:       tex(plcollcell.sty) = %{tl_version}
Provides:       tex(plextarydshln.sty) = %{tl_version}
Provides:       tex(plsiunitx.sty) = %{tl_version}
Provides:       tex(pxpgfrcs.sty) = %{tl_version}
Provides:       tex(pxstfloats.sty) = %{tl_version}

%description -n texlive-plautopatch
Japanese pLaTeX/upLaTeX formats and packages often conflict with other LaTeX
packages which are unaware of pLaTeX/upLaTeX. In the worst case, such packages
throw a fatal error or end up with a wrong output. The goal of this package is
that there should be no need to worry about such incompatibilities, because
specific patches are loaded automatically whenever necessary. This helps not
only to simplify source files, but also to make the appearance of working
pLaTeX/upLaTeX sources similar to those of ordinary LaTeX ones.

%package -n texlive-ptex-base
Summary:        Plain TeX format for pTeX and e-pTeX
Version:        svn64072
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ascii-jplain.tex) = %{tl_version}
Provides:       tex(kinsoku.tex) = %{tl_version}
Provides:       tex(ptex.tex) = %{tl_version}

%description -n texlive-ptex-base
The bundle contains the plain TeX format for pTeX and e-pTeX.

%package -n texlive-ptex-fonts
Summary:        Fonts for use with pTeX
Version:        svn64330
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ptex-fonts
The bundle contains fonts for use with pTeX and the documents for the makejvf
program. This is a redistribution derived from the ptex-texmf distribution by
ASCII MEDIA WORKS.

%package -n texlive-ptex-manual
Summary:        Japanese pTeX manual
Version:        svn75173
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ptex-manual-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ptex-manual-doc <= 11:%{version}

%description -n texlive-ptex-manual
This package contains the Japanese pTeX manual. Feedback is welcome!

%package -n texlive-pxbase
Summary:        Tools for use with (u)pLaTeX
Version:        svn66187
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(ifptex.sty)
Requires:       tex(ifuptex.sty)
Provides:       tex(pxbabel.sty) = %{tl_version}
Provides:       tex(pxbase.def) = %{tl_version}
Provides:       tex(pxbase.sty) = %{tl_version}
Provides:       tex(pxbasenc.def) = %{tl_version}
Provides:       tex(pxbsjc.def) = %{tl_version}
Provides:       tex(pxbsjc1.def) = %{tl_version}
Provides:       tex(pxjsfenc.def) = %{tl_version}
Provides:       tex(upkcat.sty) = %{tl_version}

%description -n texlive-pxbase
The main purpose of this package is to provide auxiliary functions which are
utilized by other packages created by the same author. It also provides a few
user commands to assist in creating Japanese documents using (u)pLaTeX.

%package -n texlive-pxchfon
Summary:        Japanese font setup for pLaTeX and upLaTeX
Version:        svn72097
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pxufont-ruby.sty)
Requires:       tex(pxufont.sty)
Provides:       tex(pxchfon.sty) = %{tl_version}
Provides:       tex(pxchfon0.def) = %{tl_version}

%description -n texlive-pxchfon
This package enables users to declare in their document which physical fonts
should be used for the standard Japanese (logical) fonts of pLaTeX and upLaTeX.
Font setup is realized by changing the font mapping of dvipdfmx, and thus users
can use any (monospaced) physical fonts they like, once they properly install
this package, without creating helper files for each new font. This package
also supports setup for the fonts used in the japanese-otf package. System
requirements: TeX format: LaTeX. TeX engine: pTeX or upTeX. DVIware: dvipdfmx.
Prerequisite packages: atbegshi.

%package -n texlive-pxcjkcat
Summary:        LaTeX interface for the CJK category codes of upTeX
Version:        svn74144
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(pxcjkcat.sty) = %{tl_version}

%description -n texlive-pxcjkcat
The package provides management of the CJK category code ('kcatcode'> table of
the upTeX extended TeX engine. Package options are available for tailored use
in the cases of documents that are principally written in Japanese, or
principally written in English or other Western languages.

%package -n texlive-pxjahyper
Summary:        Hyperref support for pLaTeX
Version:        svn72114
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(atbegshi.sty)
Requires:       tex(bxjatoucs.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(ltxcmds.sty)
Provides:       tex(pxjahyper-ajm.def) = %{tl_version}
Provides:       tex(pxjahyper-enc.sty) = %{tl_version}
Provides:       tex(pxjahyper-uni.def) = %{tl_version}
Provides:       tex(pxjahyper.sty) = %{tl_version}

%description -n texlive-pxjahyper
This package adjusts the behavior of hyperref on (u)pLaTeX so that authors can
properly create PDF documents that contain document information in Japanese.

%package -n texlive-pxjodel
Summary:        Help change metrics of fonts from japanese-otf
Version:        svn76323
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifuptex.sty)
Requires:       tex(otf.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(pxjodel.sty) = %{tl_version}

%description -n texlive-pxjodel
This package changes the setup of the japanese-otf package so that the TFMs for
direct input are all replaced by new ones with prefixed names; for example,
nmlminr-h will be replaced by foo--nmlminr-h, where foo is a prefix specified
by the user. This function will assist users who want to use the japanese-otf
package together with tailored TFMs of Japanese fonts. The "jodel" part of the
package name stands for "japanese-otf deluxe". Here "deluxe" is the name of
japanese-otf's option for employing multi-weight Japanese font families. This
option is probably the most likely reason for using japanese-otf. So pxjodel is
really about japanese-otf's "deluxe" option, hence the name. It is not related
to yodel singing, although some sense of word-play is intended.

%package -n texlive-pxrubrica
Summary:        Ruby annotations according to JIS X 4051
Version:        svn66298
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(pxrubrica.sty) = %{tl_version}

%description -n texlive-pxrubrica
This package provides a function to add ruby annotations (furigana) that follow
the style conventional in Japanese typography as described in the W3C technical
note "Requirements for Japanese Text Layout" ([JLREQ]) and the JIS
specification JIS X 4051. Starting with version 1.3, this package also provides
a function to add kenten (emphasis marks) to Japanese text.

%package -n texlive-pxufont
Summary:        Emulate non-Unicode Japanese fonts using Unicode fonts
Version:        svn67573
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifuptex.sty)
Provides:       tex(pxufont-ruby.sty) = %{tl_version}
Provides:       tex(pxufont.sty) = %{tl_version}

%description -n texlive-pxufont
The set of the Japanese logical fonts (JFMs) that are used as standard fonts in
pTeX and upTeX contains both Unicode JFMs and non-Unicode JFMs. This bundle
provides an alternative set of non-Unicode JFMs that are tied to the virtual
fonts (VFs) that refer to the glyphs in the Unicode JFMs. Moreover it provides
a LaTeX package that redefines the NFSS settings of the Japanese fonts of
(u)pLaTeX so that the new set of non-Unicode JFMs will be employed. As a whole,
this bundle allows users to dispense with the mapping setup on non-Unicode
JFMs. Such a setup is useful in particular when users want to use OpenType
fonts (such as Source Han Serif) that have a glyph encoding different from
Adobe-Japan1, because mapping setups from non-Unicode JFMs to such physical
fonts are difficult to prepare.

%package -n texlive-texlive-ja
Summary:        TeX Live manual (Japanese)
Version:        svn74739
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-ja-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-ja-doc <= 11:%{version}

%description -n texlive-texlive-ja
TeX Live manual (Japanese)

%package -n texlive-uptex-base
Summary:        Plain TeX formats and documents for upTeX
Version:        svn76790
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ukinsoku.tex) = %{tl_version}
Provides:       tex(uptex.tex) = %{tl_version}

%description -n texlive-uptex-base
The bundle contains plain TeX format files and documents for upTeX and e-upTeX.

%package -n texlive-uptex-fonts
Summary:        Fonts for use with upTeX
Version:        svn74119
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-uptex-fonts
The bundle contains fonts (TFM and VF) for use with upTeX. This is a
redistribution derived from the upTeX distribution by Takuji Tanaka.

%package -n texlive-wadalab
Summary:        Wadalab (Japanese) font packages
Version:        svn42428
License:        LicenseRef-Wadalab
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-wadalab
These are font bundles for the Japanese Wadalab fonts which work with the CJK
package. All subfonts now have glyph names compliant to the Adobe Glyph List,
making ToUnicode CMaps in PDF documents (created automatically by dvipdfmx)
work correctly. All font bundles now contain virtual Unicode subfonts.

%package -n texlive-zxjafbfont
Summary:        Fallback CJK font support for xeCJK
Version:        svn28539
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xeCJK.sty)
Provides:       tex(zxjafbfont.sty) = %{tl_version}

%description -n texlive-zxjafbfont
Fallback CJK font support for xeCJK

%package -n texlive-zxjatype
Summary:        Standard conforming typesetting of Japanese, for XeLaTeX
Version:        svn53500
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xeCJK.sty)
Requires:       tex(xparse.sty)
Provides:       tex(zxjatype.sty) = %{tl_version}

%description -n texlive-zxjatype
Standard conforming typesetting of Japanese, for XeLaTeX


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
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main} --strip-components=1
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main} --strip-components=1
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
tar -xf %{SOURCE86} -C %{buildroot}%{_texmf_main} --strip-components=1
tar -xf %{SOURCE87} -C %{buildroot}%{_texmf_main} --strip-components=1
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

# Install AppStream metadata for font components
cp %{SOURCE126} %{buildroot}%{_datadir}/appdata/
cp %{SOURCE127} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Remove tlp* files from special install components
rm -rf %{buildroot}%{_texmf_main}/tlp*

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/haranoaji %{buildroot}%{_datadir}/fonts/haranoaji
ln -sf %{_texmf_main}/fonts/opentype/public/haranoaji-extra %{buildroot}%{_datadir}/fonts/haranoaji-extra

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-ascmac
%license bsd.txt
%{_texmf_main}/fonts/map/dvips/ascmac/
%{_texmf_main}/fonts/source/public/ascmac/
%{_texmf_main}/fonts/tfm/public/ascmac/
%{_texmf_main}/fonts/type1/public/ascmac/
%{_texmf_main}/tex/latex/ascmac/
%doc %{_texmf_main}/doc/latex/ascmac/

%files -n texlive-asternote
%license mit.txt
%{_texmf_main}/tex/latex/asternote/
%doc %{_texmf_main}/doc/latex/asternote/

%files -n texlive-babel-japanese
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-japanese/
%doc %{_texmf_main}/doc/generic/babel-japanese/

%files -n texlive-bxbase
%license mit.txt
%{_texmf_main}/tex/latex/bxbase/
%doc %{_texmf_main}/doc/latex/bxbase/

%files -n texlive-bxcjkjatype
%license mit.txt
%{_texmf_main}/tex/latex/bxcjkjatype/
%doc %{_texmf_main}/doc/latex/bxcjkjatype/

%files -n texlive-bxcoloremoji
%license mit.txt
%{_texmf_main}/tex/latex/bxcoloremoji/
%doc %{_texmf_main}/doc/latex/bxcoloremoji/

%files -n texlive-bxghost
%license mit.txt
%{_texmf_main}/tex/latex/bxghost/
%doc %{_texmf_main}/doc/latex/bxghost/

%files -n texlive-bxjaholiday
%license mit.txt
%{_texmf_main}/tex/latex/bxjaholiday/
%doc %{_texmf_main}/doc/latex/bxjaholiday/

%files -n texlive-bxjalipsum
%license mit.txt
%{_texmf_main}/tex/latex/bxjalipsum/
%doc %{_texmf_main}/doc/latex/bxjalipsum/

%files -n texlive-bxjaprnind
%license mit.txt
%{_texmf_main}/tex/latex/bxjaprnind/
%doc %{_texmf_main}/doc/latex/bxjaprnind/

%files -n texlive-bxjatoucs
%license mit.txt
%{_texmf_main}/fonts/tfm/public/bxjatoucs/
%{_texmf_main}/tex/latex/bxjatoucs/
%doc %{_texmf_main}/doc/latex/bxjatoucs/

%files -n texlive-bxjscls
%license bsd2.txt
%{_texmf_main}/tex/latex/bxjscls/
%doc %{_texmf_main}/doc/latex/bxjscls/

%files -n texlive-bxorigcapt
%license mit.txt
%{_texmf_main}/tex/latex/bxorigcapt/
%doc %{_texmf_main}/doc/latex/bxorigcapt/

%files -n texlive-bxwareki
%license mit.txt
%{_texmf_main}/tex/latex/bxwareki/
%doc %{_texmf_main}/doc/latex/bxwareki/

%files -n texlive-chuushaku
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chuushaku/
%doc %{_texmf_main}/doc/latex/chuushaku/

%files -n texlive-convert-jpfonts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/convert-jpfonts/
%doc %{_texmf_main}/doc/latex/convert-jpfonts/

%files -n texlive-endnotesj
%license bsd.txt
%{_texmf_main}/tex/latex/endnotesj/
%doc %{_texmf_main}/doc/latex/endnotesj/

%files -n texlive-gckanbun
%license mit.txt
%{_texmf_main}/tex/latex/gckanbun/
%doc %{_texmf_main}/doc/latex/gckanbun/

%files -n texlive-gentombow
%license bsd.txt
%{_texmf_main}/tex/latex/gentombow/
%doc %{_texmf_main}/doc/latex/gentombow/

%files -n texlive-haranoaji
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/haranoaji/
%{_texmf_main}/tex/latex/haranoaji/
%doc %{_texmf_main}/doc/fonts/haranoaji/
%{_datadir}/fonts/haranoaji
%{_datadir}/appdata/haranoaji.metainfo.xml

%files -n texlive-haranoaji-extra
%license ofl.txt
%{_texmf_main}/fonts/opentype/public/haranoaji-extra/
%doc %{_texmf_main}/doc/fonts/haranoaji-extra/
%{_datadir}/fonts/haranoaji-extra
%{_datadir}/appdata/haranoaji-extra.metainfo.xml

%files -n texlive-ieejtran
%license mit.txt
%{_texmf_main}/bibtex/bst/ieejtran/
%doc %{_texmf_main}/doc/bibtex/ieejtran/

%files -n texlive-ifptex
%license mit.txt
%{_texmf_main}/tex/generic/ifptex/
%doc %{_texmf_main}/doc/generic/ifptex/

%files -n texlive-ifxptex
%license knuth.txt
%{_texmf_main}/tex/generic/ifxptex/
%doc %{_texmf_main}/doc/generic/ifxptex/

%files -n texlive-ipaex
%license other-free.txt
%{_texmf_main}/fonts/truetype/public/ipaex/
%doc %{_texmf_main}/doc/fonts/ipaex/

%files -n texlive-japanese-mathformulas
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/japanese-mathformulas/
%doc %{_texmf_main}/doc/lualatex/japanese-mathformulas/

%files -n texlive-japanese-otf
%license bsd.txt
%{_texmf_main}/fonts/tfm/public/japanese-otf/
%{_texmf_main}/fonts/vf/public/japanese-otf/
%{_texmf_main}/tex/platex/japanese-otf/
%doc %{_texmf_main}/doc/fonts/japanese-otf/

%files -n texlive-jieeetran
%license mit.txt
%{_texmf_main}/bibtex/bst/jieeetran/
%doc %{_texmf_main}/doc/bibtex/jieeetran/

%files -n texlive-jlreq
%license bsd2.txt
%{_texmf_main}/fonts/tfm/public/jlreq/
%{_texmf_main}/fonts/vf/public/jlreq/
%{_texmf_main}/tex/latex/jlreq/
%{_texmf_main}/tex/luatex/jlreq/
%doc %{_texmf_main}/doc/latex/jlreq/

%files -n texlive-jlreq-deluxe
%license mit.txt
%{_texmf_main}/fonts/tfm/public/jlreq-deluxe/
%{_texmf_main}/fonts/vf/public/jlreq-deluxe/
%{_texmf_main}/tex/platex/jlreq-deluxe/
%doc %{_texmf_main}/doc/platex/jlreq-deluxe/

%files -n texlive-jpneduenumerate
%license mit.txt
%{_texmf_main}/tex/latex/jpneduenumerate/
%doc %{_texmf_main}/doc/latex/jpneduenumerate/

%files -n texlive-jpnedumathsymbols
%license mit.txt
%{_texmf_main}/tex/latex/jpnedumathsymbols/
%doc %{_texmf_main}/doc/latex/jpnedumathsymbols/

%files -n texlive-jsclasses
%license bsd.txt
%{_texmf_main}/tex/platex/jsclasses/
%doc %{_texmf_main}/doc/platex/jsclasses/

%files -n texlive-kanbun
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/kanbun/
%doc %{_texmf_main}/doc/latex/kanbun/

%files -n texlive-lshort-japanese
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-japanese/

%files -n texlive-luatexja
%license bsd.txt
%{_texmf_main}/tex/luatex/luatexja/
%doc %{_texmf_main}/doc/luatex/luatexja/

%files -n texlive-luwa-ul
%license mit.txt
%{_texmf_main}/tex/lualatex/luwa-ul/
%doc %{_texmf_main}/doc/lualatex/luwa-ul/

%files -n texlive-mendex-doc
%license bsd.txt
%{_texmf_main}/makeindex/mendex-doc/
%doc %{_texmf_main}/doc/support/mendex-doc/

%files -n texlive-morisawa
%license bsd.txt
%{_texmf_main}/fonts/map/dvipdfmx/morisawa/
%{_texmf_main}/fonts/tfm/public/morisawa/
%{_texmf_main}/fonts/vf/public/morisawa/
%{_texmf_main}/tex/latex/morisawa/
%doc %{_texmf_main}/doc/fonts/morisawa/

%files -n texlive-outoruby
%license gpl3.txt
%{_texmf_main}/tex/latex/outoruby/
%doc %{_texmf_main}/doc/latex/outoruby/

%files -n texlive-pbibtex-base
%license bsd.txt
%{_texmf_main}/pbibtex/bib/
%{_texmf_main}/pbibtex/bst/
%doc %{_texmf_main}/doc/ptex/pbibtex/

%files -n texlive-pbibtex-manual
%license bsd.txt
%doc %{_texmf_main}/doc/latex/pbibtex-manual/

%files -n texlive-platex
%license bsd.txt
%{_texmf_main}/tex/platex/base/
%{_texmf_main}/tex/platex/config/
%doc %{_texmf_main}/doc/man/man1/
%doc %{_texmf_main}/doc/platex/base/

%files -n texlive-platex-tools
%license bsd.txt
%{_texmf_main}/tex/latex/platex-tools/
%doc %{_texmf_main}/doc/latex/platex-tools/

%files -n texlive-platexcheat
%license mit.txt
%doc %{_texmf_main}/doc/latex/platexcheat/

%files -n texlive-plautopatch
%license bsd.txt
%{_texmf_main}/tex/latex/plautopatch/
%doc %{_texmf_main}/doc/latex/plautopatch/

%files -n texlive-ptex-base
%license bsd.txt
%{_texmf_main}/tex/ptex/ptex-base/
%doc %{_texmf_main}/doc/ptex/ptex-base/

%files -n texlive-ptex-fonts
%license bsd.txt
%{_texmf_main}/fonts/source/ptex-fonts/jis/
%{_texmf_main}/fonts/source/ptex-fonts/nmin-ngoth/
%{_texmf_main}/fonts/source/ptex-fonts/standard/
%{_texmf_main}/fonts/tfm/ptex-fonts/dvips/
%{_texmf_main}/fonts/tfm/ptex-fonts/jis/
%{_texmf_main}/fonts/tfm/ptex-fonts/nmin-ngoth/
%{_texmf_main}/fonts/tfm/ptex-fonts/standard/
%{_texmf_main}/fonts/vf/ptex-fonts/jis/
%{_texmf_main}/fonts/vf/ptex-fonts/nmin-ngoth/
%{_texmf_main}/fonts/vf/ptex-fonts/standard/
%doc %{_texmf_main}/doc/fonts/ptex-fonts/

%files -n texlive-ptex-manual
%license bsd.txt
%doc %{_texmf_main}/doc/ptex/ptex-manual/

%files -n texlive-pxbase
%license mit.txt
%{_texmf_main}/tex/platex/pxbase/
%doc %{_texmf_main}/doc/platex/pxbase/

%files -n texlive-pxchfon
%license mit.txt
%{_texmf_main}/fonts/sfd/pxchfon/
%{_texmf_main}/fonts/tfm/public/pxchfon/
%{_texmf_main}/fonts/vf/public/pxchfon/
%{_texmf_main}/tex/platex/pxchfon/
%doc %{_texmf_main}/doc/platex/pxchfon/

%files -n texlive-pxcjkcat
%license mit.txt
%{_texmf_main}/tex/latex/pxcjkcat/
%doc %{_texmf_main}/doc/latex/pxcjkcat/

%files -n texlive-pxjahyper
%license mit.txt
%{_texmf_main}/tex/platex/pxjahyper/
%doc %{_texmf_main}/doc/platex/pxjahyper/

%files -n texlive-pxjodel
%license mit.txt
%{_texmf_main}/fonts/tfm/public/pxjodel/
%{_texmf_main}/fonts/vf/public/pxjodel/
%{_texmf_main}/tex/latex/pxjodel/
%doc %{_texmf_main}/doc/latex/pxjodel/

%files -n texlive-pxrubrica
%license mit.txt
%{_texmf_main}/tex/platex/pxrubrica/
%doc %{_texmf_main}/doc/platex/pxrubrica/

%files -n texlive-pxufont
%license mit.txt
%{_texmf_main}/fonts/tfm/public/pxufont/
%{_texmf_main}/fonts/vf/public/pxufont/
%{_texmf_main}/tex/latex/pxufont/
%doc %{_texmf_main}/doc/latex/pxufont/

%files -n texlive-texlive-ja
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-ja/

%files -n texlive-uptex-base
%license bsd.txt
%{_texmf_main}/tex/uptex/uptex-base/
%doc %{_texmf_main}/doc/uptex/uptex-base/

%files -n texlive-uptex-fonts
%license bsd.txt
%{_texmf_main}/fonts/cmap/uptex-fonts/
%{_texmf_main}/fonts/source/uptex-fonts/
%{_texmf_main}/fonts/tfm/uptex-fonts/jis/
%{_texmf_main}/fonts/tfm/uptex-fonts/min/
%{_texmf_main}/fonts/vf/uptex-fonts/jis/
%{_texmf_main}/fonts/vf/uptex-fonts/min/
%doc %{_texmf_main}/doc/fonts/uptex-fonts/

%files -n texlive-wadalab
%license other-free.txt
%{_texmf_main}/fonts/afm/wadalab/dgj/
%{_texmf_main}/fonts/afm/wadalab/dmj/
%{_texmf_main}/fonts/afm/wadalab/mc2j/
%{_texmf_main}/fonts/afm/wadalab/mcj/
%{_texmf_main}/fonts/afm/wadalab/mr2j/
%{_texmf_main}/fonts/afm/wadalab/mrj/
%{_texmf_main}/fonts/map/dvips/wadalab/
%{_texmf_main}/fonts/tfm/wadalab/dgj/
%{_texmf_main}/fonts/tfm/wadalab/dmj/
%{_texmf_main}/fonts/tfm/wadalab/mc2j/
%{_texmf_main}/fonts/tfm/wadalab/mcj/
%{_texmf_main}/fonts/tfm/wadalab/mr2j/
%{_texmf_main}/fonts/tfm/wadalab/mrj/
%{_texmf_main}/fonts/tfm/wadalab/udgj/
%{_texmf_main}/fonts/tfm/wadalab/udmj/
%{_texmf_main}/fonts/tfm/wadalab/umcj/
%{_texmf_main}/fonts/tfm/wadalab/umrj/
%{_texmf_main}/fonts/type1/wadalab/dgj/
%{_texmf_main}/fonts/type1/wadalab/dmj/
%{_texmf_main}/fonts/type1/wadalab/mc2j/
%{_texmf_main}/fonts/type1/wadalab/mcj/
%{_texmf_main}/fonts/type1/wadalab/mr2j/
%{_texmf_main}/fonts/type1/wadalab/mrj/
%{_texmf_main}/fonts/vf/wadalab/udgj/
%{_texmf_main}/fonts/vf/wadalab/udmj/
%{_texmf_main}/fonts/vf/wadalab/umcj/
%{_texmf_main}/fonts/vf/wadalab/umrj/
%doc %{_texmf_main}/doc/fonts/wadalab/

%files -n texlive-zxjafbfont
%license mit.txt
%{_texmf_main}/tex/latex/zxjafbfont/
%doc %{_texmf_main}/doc/latex/zxjafbfont/

%files -n texlive-zxjatype
%license mit.txt
%{_texmf_main}/tex/latex/zxjatype/
%doc %{_texmf_main}/doc/latex/zxjatype/

%changelog
* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76651-2
- Update luatexja luwa-ul

* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76651-1
- update to svn76651, fix descriptions, update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74394-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74394-1
- Update to TeX Live 2025
