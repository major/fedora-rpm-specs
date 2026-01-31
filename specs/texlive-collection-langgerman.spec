%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langgerman
Epoch:          12
Version:        svn74675
Release:        4%{?dist}
Summary:        German

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langgerman.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apalike-german.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apalike-german.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autotype.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autotype.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-german.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-german.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-german.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-german.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/booktabs-de.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/booktabs-de.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csquotes-de.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csquotes-de.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dehyph.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dehyph-exptl.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dehyph-exptl.doc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dhua.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dhua.doc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtk-bibliography.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtk-bibliography.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etdipa.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etdipa.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox-de.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etoolbox-de.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fifinddo-info.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fifinddo-info.doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fragoli.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fragoli.doc.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/german.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/german.doc.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/germbib.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/germbib.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/germkorr.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/germkorr.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hausarbeit-jura.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hausarbeit-jura.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-german.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/koma-script-examples.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/koma-script-examples.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2picfaq.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2picfaq.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-de.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-de.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-doc-de.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-doc-de.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/microtype-de.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/microtype-de.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/milog.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/milog.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-de.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-de.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/r_und_s.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/r_und_s.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schulmathematik.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schulmathematik.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/templates-fenn.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/templates-fenn.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/templates-sommer.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/templates-sommer.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/termcal-de.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/termcal-de.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-de.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-de.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipa-de.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tipa-de.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-arsclassica-de.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-arsclassica-de.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-biblatex-de.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-biblatex-de.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-chemsym-de.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-chemsym-de.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-ecv-de.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-ecv-de.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-enumitem-de.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-enumitem-de.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-europecv-de.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-europecv-de.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-filecontents-de.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-filecontents-de.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-moreverb-de.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-moreverb-de.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udesoftec.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/udesoftec.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhrzeit.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uhrzeit.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umlaute.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/umlaute.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/voss-mathcol.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/voss-mathcol.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-apalike-german
Requires:       texlive-autotype
Requires:       texlive-babel-german
Requires:       texlive-bibleref-german
Requires:       texlive-booktabs-de
Requires:       texlive-collection-basic
Requires:       texlive-csquotes-de
Requires:       texlive-dehyph
Requires:       texlive-dehyph-exptl
Requires:       texlive-dhua
Requires:       texlive-dtk-bibliography
Requires:       texlive-etdipa
Requires:       texlive-etoolbox-de
Requires:       texlive-fifinddo-info
Requires:       texlive-fragoli
Requires:       texlive-german
Requires:       texlive-germbib
Requires:       texlive-germkorr
Requires:       texlive-hausarbeit-jura
Requires:       texlive-hyphen-german
Requires:       texlive-koma-script-examples
Requires:       texlive-l2picfaq
Requires:       texlive-latexcheat-de
Requires:       texlive-lualatex-doc-de
Requires:       texlive-microtype-de
Requires:       texlive-milog
Requires:       texlive-quran-de
Requires:       texlive-r_und_s
Requires:       texlive-schulmathematik
Requires:       texlive-templates-fenn
Requires:       texlive-templates-sommer
Requires:       texlive-termcal-de
Requires:       texlive-texlive-de
Requires:       texlive-tipa-de
Requires:       texlive-translation-arsclassica-de
Requires:       texlive-translation-biblatex-de
Requires:       texlive-translation-chemsym-de
Requires:       texlive-translation-ecv-de
Requires:       texlive-translation-enumitem-de
Requires:       texlive-translation-europecv-de
Requires:       texlive-translation-filecontents-de
Requires:       texlive-translation-moreverb-de
Requires:       texlive-udesoftec
Requires:       texlive-uhrzeit
Requires:       texlive-umlaute
Requires:       texlive-voss-mathcol

%description
Support for German.


%package -n texlive-apalike-german
Summary:        A copy of apalike.bst with German localization
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-apalike-german
A copy of apalike.bst (which is part of the base BibTeX distribution) with
German localization.

%package -n texlive-autotype
Summary:        A LuaLaTeX package for automatic language-specific typography
Version:        svn76924
License:        AGPL-3.0-or-later AND LPPL-1.3c AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(autotype.sty) = %{tl_version}

%description -n texlive-autotype
autotype is a LuaLaTeX package for automatic language-specific typography.
Currently, it supports ligature suppression at word boundaries, long s
insertion for blackletter typesetting, and weighted hyphenation, but only for
German (old and new orthography).

%package -n texlive-babel-german
Summary:        Babel support for documents written in German
Version:        svn77469
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(austrian.ldf) = %{tl_version}
Provides:       tex(babel-german.def) = %{tl_version}
Provides:       tex(german-at-1901.ldf) = %{tl_version}
Provides:       tex(german-at.ldf) = %{tl_version}
Provides:       tex(german-austria-1901.ldf) = %{tl_version}
Provides:       tex(german-austria.ldf) = %{tl_version}
Provides:       tex(german-ch-1901.ldf) = %{tl_version}
Provides:       tex(german-ch.ldf) = %{tl_version}
Provides:       tex(german-de-1901.ldf) = %{tl_version}
Provides:       tex(german-de.ldf) = %{tl_version}
Provides:       tex(german-germany-1901.ldf) = %{tl_version}
Provides:       tex(german-germany.ldf) = %{tl_version}
Provides:       tex(german-switzerland-1901.ldf) = %{tl_version}
Provides:       tex(german-switzerland.ldf) = %{tl_version}
Provides:       tex(german.ldf) = %{tl_version}
Provides:       tex(germanb.ldf) = %{tl_version}
Provides:       tex(naustrian.ldf) = %{tl_version}
Provides:       tex(ngerman.ldf) = %{tl_version}
Provides:       tex(ngermanb.ldf) = %{tl_version}
Provides:       tex(nswissgerman.ldf) = %{tl_version}
Provides:       tex(swissgerman.ldf) = %{tl_version}

%description -n texlive-babel-german
This bundle is an extension to the babel package for multilingual typesetting.
It provides all the necessary macros, definitions and settings to typeset
German documents. The bundle includes support for the traditional and reformed
German orthography as well as for the Austrian and Swiss varieties of German.

%package -n texlive-bibleref-german
Summary:        German adaptation of bibleref
Version:        svn21923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
Provides:       tex(bibleref-german.sty) = %{tl_version}

%description -n texlive-bibleref-german
The package provides translations and various formats for the use of bibleref
in German documents. The German naming of the bible books complies with the
'Loccumer Richtlinien' (Locum guidelines). In addition, the Vulgate (Latin
bible) is supported.

%package -n texlive-booktabs-de
Summary:        German version of booktabs
Version:        svn21907
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-booktabs-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-booktabs-de-doc <= 11:%{version}

%description -n texlive-booktabs-de
This is a "translation" of the booktabs.

%package -n texlive-csquotes-de
Summary:        German translation of csquotes documentation
Version:        svn23371
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-csquotes-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-csquotes-de-doc <= 11:%{version}

%description -n texlive-csquotes-de
This is a translation of the documentation of csquotes version 5.1.

%package -n texlive-dehyph
Summary:        German hyphenation patterns for traditional orthography
Version:        svn48599
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dehyphn.tex) = %{tl_version}
Provides:       tex(dehypht.tex) = %{tl_version}
Provides:       tex(dehyphtex.tex) = %{tl_version}

%description -n texlive-dehyph
The package provides older hyphenation patterns for the German language. Please
note that by default only pdfLaTeX uses these patterns (mainly for backwards
compatibility). The older packages ghyphen and gnhyph are now bundled together
with dehyph, and are no longer be updated. Both XeLaTeX and LuaLaTeX use the
current German hyphenation patterns taken from Hyphenation patterns in UTF-8,
and using the Experimental hyphenation patterns for the German language package
it is possible to make pdfLaTeX use the new German patterns as well.

%package -n texlive-dehyph-exptl
Summary:        Experimental hyphenation patterns for the German language
Version:        svn72949
License:        MIT AND LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(dehyphn-x-2024-02-28.tex) = %{tl_version}
Provides:       tex(dehypht-x-2024-02-28.tex) = %{tl_version}
Provides:       tex(dehyphts-x-2024-02-28.tex) = %{tl_version}

%description -n texlive-dehyph-exptl
The package provides experimental hyphenation patterns for the German language,
covering both traditional and reformed orthography. The patterns can be used
with packages Babel and hyphsubst from the Oberdiek bundle. Dieses Paket
enthalt experimentelle Trennmuster fur die deutsche Sprache. Die Trennmuster
decken das in Deutschland, Osterreich und der Schweiz gebrauchliche
Standarddeutsch in der traditionellen und reformierten Rechtschreibung ab und
konnen mit den Paketen Babel und hyphsubst aus dem Oberdiek-Bundel verwendet
werden.

%package -n texlive-dhua
Summary:        German abbreviations using thin space
Version:        svn24035
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(dhua.sty) = %{tl_version}

%description -n texlive-dhua
The package provides commands for those abbreviations of German phrases for
which the use of thin space is recommended. Setup commands \newdhua and
\newtwopartdhua are provided, as well as commands for single cases (such as \zB
for 'z. B.', saving the user from typing such as 'z.\,B.'). To typeset the
documentation, the niceverb package, version 0.44, or later, is required. Das
Paket `dhua' stellt Befehle fur sog. mehrgliedrige Abkurzungen bereit, fur die
schmale Leerzeichen (Festabstande) empfohlen werden (Duden, Wikipedia). In die
englische Paketdokumentation sind deutsche Erlauterungen eingestreut.

%package -n texlive-dtk-bibliography
Summary:        Bibliography of "Die TeXnische Komodie"
Version:        svn76870
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(authoryear.bbx)
Requires:       tex(dantelogo.sty)
Requires:       tex(fetamont.sty)
Requires:       tex(hologo.sty)
Requires:       tex(iftex.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xspace.sty)
Provides:       tex(dtk-authoryear.bbx) = %{tl_version}
Provides:       tex(dtk-logos.sty) = %{tl_version}

%description -n texlive-dtk-bibliography
This package contains the bibliography for "Die TeXnische Komodie", the journal
of the German-speaking TeX User Group. It is updated on a quarterly basis.

%package -n texlive-etdipa
Summary:        Simple, lightweight template for scientific documents
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-etdipa-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-etdipa-doc <= 11:%{version}

%description -n texlive-etdipa
This package provides a complete working directory for the scientific
documentation of arbitrary projects. It was originally developed to provide a
template for Austrian "Diplomarbeiten" or "Vorwissenschaftliche Arbeiten",
which are scientific projects of students at a secondary school.

%package -n texlive-etoolbox-de
Summary:        German translation of documentation of etoolbox
Version:        svn21906
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-etoolbox-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-etoolbox-de-doc <= 11:%{version}

%description -n texlive-etoolbox-de
The version translated is 2.1 or 2011-01-03.

%package -n texlive-fifinddo-info
Summary:        German HTML beamer presentation on nicetext and morehype
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fifinddo-info-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fifinddo-info-doc <= 11:%{version}

%description -n texlive-fifinddo-info
The bundle: exhibits the process of making an "HTML beamer presentation" with
the blogdot package from the morehype bundle, and HTML generation based on the
fifinddo package.

%package -n texlive-fragoli
Summary:        Macros for constructing complex semantic derivations
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(comment.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(nicefrac.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(ulem.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(fragoli.sty) = %{tl_version}

%description -n texlive-fragoli
The primary goal of this package is to provide a minimal and user-friendly
syntax for constructing large and complex semantic derivations, following the
specific notational style used at Goethe University Frankfurt. It includes a
comprehensive set of commands for text formatting and various types of
bracketing, ensuring a consistent style -- particularly when distinguishing
between meta-language and object-language within a single derivation or
formula. The formula style is loosely based on the accompanying material to an
introductory course to linguistic semantics by Prof. Dr. Thomas Ede Zimmermann.
The package brings together and refines a collection of LaTeX commands and
concepts developed over the years within the Department of Linguistics at the
Goethe-Universitat at Frankfurt am Main. In the process of preparing research
papers, assignments, and examinations, numerous custom LaTeX headers and
commands were shared within the department -- some mutually compatible, others
not. Note: The package name is an abbreviation of "Frankfurt Goethe
Linguistic".

%package -n texlive-german
Summary:        Support for German typography
Version:        svn42428
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(german.sty) = %{tl_version}
Provides:       tex(ngerman.sty) = %{tl_version}

%description -n texlive-german
Supports the old German orthography (alte deutsche Rechtschreibung).

%package -n texlive-germbib
Summary:        German variants of standard BibTeX styles
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(german.sty)
Provides:       tex(bibgerm.sty) = %{tl_version}
Provides:       tex(mynormal.sty) = %{tl_version}

%description -n texlive-germbib
A development of the (old) german.sty, this bundle provides German packages,
BibTeX styles and documentary examples, for writing documents with
bibliographies. The author has since developed the babelbib bundle, which (he
asserts) supersedes germbib.

%package -n texlive-germkorr
Summary:        Change kerning for German quotation marks
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(germkorr.sty) = %{tl_version}

%description -n texlive-germkorr
The package germcorr has to be loaded after the package german. It brings some
letters like T nearer to german single and double quotes even when that letter
wears a standard accent like "`\.T"'.

%package -n texlive-hausarbeit-jura
Summary:        Class for writing "juristische Hausarbeiten" at German Universities
Version:        svn56070
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hausarbeit-jura
The class was developed for use by students writing legal essays ("juristische
Hausarbeit") at German Universities. It is based on jurabook and jurabib and
makes it easy for LaTeX beginners to get a correct and nicely formatted paper.

%package -n texlive-hyphen-german
Summary:        German hyphenation patterns.
Version:        svn74203
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-dehyph
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-de-1901.ec.tex) = %{tl_version}
Provides:       tex(hyph-de-1901.tex) = %{tl_version}
Provides:       tex(hyph-de-1996.ec.tex) = %{tl_version}
Provides:       tex(hyph-de-1996.tex) = %{tl_version}
Provides:       tex(hyph-de-ch-1901.ec.tex) = %{tl_version}
Provides:       tex(hyph-de-ch-1901.tex) = %{tl_version}
Provides:       tex(loadhyph-de-1901.tex) = %{tl_version}
Provides:       tex(loadhyph-de-1996.tex) = %{tl_version}
Provides:       tex(loadhyph-de-ch-1901.tex) = %{tl_version}

%description -n texlive-hyphen-german
Hyphenation patterns for German in T1/EC and UTF-8 encodings, for traditional
and reformed spelling, including Swiss German. The package includes the latest
patterns from dehyph-exptl (known to TeX under names 'german', 'ngerman' and
'swissgerman'), however 8-bit engines still load old versions of patterns for
'german' and 'ngerman' for backward-compatibility reasons. Swiss German
patterns are suitable for Swiss Standard German (Hochdeutsch) not the Alemannic
dialects spoken in Switzerland (Schwyzerduetsch). There are no known patterns
for written Schwyzerduetsch.

%package -n texlive-koma-script-examples
Summary:        Examples from the KOMA-Script book
Version:        svn63833
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-koma-script-examples-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-koma-script-examples-doc <= 11:%{version}

%description -n texlive-koma-script-examples
This package contains some examples from the 6th edition of the book
>>KOMA-Script<<, >>Eine Sammlung von Klassen und Paketen fur LaTeX2e<< by
Markus Kohm, published by Lehmanns Media. There are no further descriptions of
these examples.

%package -n texlive-l2picfaq
Summary:        LaTeX pictures "how-to" (German)
Version:        svn19601
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l2picfaq-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l2picfaq-doc <= 11:%{version}

%description -n texlive-l2picfaq
The document (in German) is a collection of "how-to" notes about LaTeX and
pictures. The aim of the document is to provide a solution, in the form of some
sample code, for every problem.

%package -n texlive-latexcheat-de
Summary:        A LaTeX cheat sheet, in German
Version:        svn35702
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcheat-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcheat-de-doc <= 11:%{version}

%description -n texlive-latexcheat-de
This is a translation to German of Winston Chang's LaTeX cheat sheet (a
reference sheet for writing scientific papers). It has been adapted to German
standards using the KOMA script document classes.

%package -n texlive-lualatex-doc-de
Summary:        Guide to LuaLaTeX (German translation)
Version:        svn30474
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lualatex-doc-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lualatex-doc-de-doc <= 11:%{version}

%description -n texlive-lualatex-doc-de
The document is a German translation of the map/guide to the world of LuaLaTeX.
Coverage supports both new users and package developers. Apart from the
introductory material, the document gathers information from several sources,
and offers links to others.

%package -n texlive-microtype-de
Summary:        Translation into German of the documentation of microtype
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-microtype-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-microtype-de-doc <= 11:%{version}

%description -n texlive-microtype-de
Translation into German of the documentation of microtype

%package -n texlive-milog
Summary:        A LaTeX class for fulfilling the documentation duties according to the German minimum wage law MiLoG
Version:        svn75447
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-milog
Seit dem 1. Januar 2015 gilt in Deutschland grundsatzlich fur alle Arbeitnehmer
ein flachendeckender gesetzlicher Mindestlohn in Hohe von derzeit 8,50EUR pro
Stunde. Mit Wirkung ab 1. August 2015 wurden die Dokumentations- und
Aufzeichnungspflichten gelockert. Nach SS17 MiLoG, muss Beginn, Ende und Dauer
der taglichen Arbeitszeit der in SS22 MiLoG definierten Arbeitnehmern (formlos)
aufgezeichnet werden. Zusatzlich ermoglicht milog.cls aus praktischen Grunden
die Aufzeichnug von unbezahlten Pausen und Bemerkungen (Ruhetag, Urlaub, krank,
...). Die Erfassung der Arbeitszeiten erfolgt in einer simplen CSV-Datei, aus
der die Klasse automatisch einen Arbeitszeitnachweis erstellt. Alternativ
konnen die Daten auch durch einen CSV-Export - mit eventueller Nachbearbeitung
- einer geeigneteten App erhoben werden. The milog.cls class provides means to
fulfill the documentation duties by the German minimum wage law MiLoG. The
recording of working hours is carried out in a simple CSV file from which the
class will automatically create a time sheet. Alternatively, data can also be
collected by a CSV export of a suitable app.

%package -n texlive-quran-de
Summary:        German translations to the quran package
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-de.sty) = %{tl_version}
Provides:       tex(qurantext-deii.translation.def) = %{tl_version}
Provides:       tex(qurantext-deiii.translation.def) = %{tl_version}
Provides:       tex(qurantext-deiv.translation.def) = %{tl_version}

%description -n texlive-quran-de
The package is prepared for typesetting some German translations of the Holy
Quran. It adds three more German translations to the quran package.

%package -n texlive-r_und_s
Summary:        Chemical hazard codes
Version:        svn15878
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(eng_rs.sty) = %{tl_version}
Provides:       tex(eng_rs.tex) = %{tl_version}
Provides:       tex(fr_rs.sty) = %{tl_version}
Provides:       tex(fr_rs.tex) = %{tl_version}
Provides:       tex(nl_rs.sty) = %{tl_version}
Provides:       tex(nl_rs.tex) = %{tl_version}
Provides:       tex(r_und_s.sty) = %{tl_version}
Provides:       tex(r_und_s.tex) = %{tl_version}

%description -n texlive-r_und_s
The r_und_s package decodes the german 'R- und S-Satze', which are numerically
coded security advice for chemical substances into plain text. This is, e.g.,
used to compose security sheets or lab protocols and especially useful for
students of chemistry. There are four packages, giving texts in German,
English, French and Dutch.

%package -n texlive-schulmathematik
Summary:        Commands and document classes for German-speaking teachers of mathematics and physics
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(circuitikz.sty)
Provides:       tex(schulma-physik.sty) = %{tl_version}
Provides:       tex(schulma.sty) = %{tl_version}

%description -n texlive-schulmathematik
The schulmathematik bundle provides two LaTeX packages and six document classes
for German-speaking teachers of mathematics and physics.

%package -n texlive-templates-fenn
Summary:        Templates for TeX usage
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-templates-fenn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-templates-fenn-doc <= 11:%{version}

%description -n texlive-templates-fenn
A set of templates for using LaTeX packages that the author uses, comprising: -
scrlttr2.tex: a letter, written with scrlttr2.cls from the KOMA-Script bundle;
- dinbrief.tex: a letter according to the German (DIN) standards, written with
dinbrief.cls; - kbrief.tex: a brief memo ('Kurzbrief') to accompany enclosures,
as used in German offices, again based on dinbrief; - vermerk.tex: a general
form for taking down notes on events in the office; and - diabetes.tex: a diary
for the basis-bolus insulin therapy of diabetes mellitus, using scrartcl.cls
from the KOMA-Script bundle.

%package -n texlive-templates-sommer
Summary:        Templates for TeX usage
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-templates-sommer-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-templates-sommer-doc <= 11:%{version}

%description -n texlive-templates-sommer
A set of templates for using LaTeX packages that the author uses, comprising: -
Hausarbeit.tex: for students of the Lehrstuhl Volkskunde an der
Friedrich-Schiller-Universitat Jena; - Psycho-Dipl.tex: for diploma theses in
psychology.

%package -n texlive-termcal-de
Summary:        German localization for termcal
Version:        svn47111
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(termcal.sty)
Provides:       tex(termcal-de.sty) = %{tl_version}

%description -n texlive-termcal-de
This package provides a German localization to the termcal package written by
Bill Mitchell, which is intended to print a term calendar for use in planning a
class. termcal-de depends on the following other packages: termcal, pgfkeys,
pgfopts, datetime2, and datetime2-german.

%package -n texlive-texlive-de
Summary:        TeX Live manual (German)
Version:        svn74226
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-de-doc <= 11:%{version}

%description -n texlive-texlive-de
TeX Live manual (German)

%package -n texlive-tipa-de
Summary:        German translation of tipa documentation
Version:        svn22005
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tipa-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tipa-de-doc <= 11:%{version}

%description -n texlive-tipa-de
This is a translation of Fukui Rei's tipaman from the tipa bundle.

%package -n texlive-translation-arsclassica-de
Summary:        German version of arsclassica
Version:        svn23803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-arsclassica-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-arsclassica-de-doc <= 11:%{version}

%description -n texlive-translation-arsclassica-de
This is a "translation" of the arsclassica documentation.

%package -n texlive-translation-biblatex-de
Summary:        German translation of the User Guide for BibLaTeX
Version:        svn59382
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-biblatex-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-biblatex-de-doc <= 11:%{version}

%description -n texlive-translation-biblatex-de
A German translation of the User Guide for BibLaTeX.

%package -n texlive-translation-chemsym-de
Summary:        German version of chemsym
Version:        svn23804
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-chemsym-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-chemsym-de-doc <= 11:%{version}

%description -n texlive-translation-chemsym-de
This is a "translation" of the chemsym documentation.

%package -n texlive-translation-ecv-de
Summary:        Ecv documentation, in German
Version:        svn24754
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-ecv-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-ecv-de-doc <= 11:%{version}

%description -n texlive-translation-ecv-de
This is a "translation" of the ecv documentation.

%package -n texlive-translation-enumitem-de
Summary:        Enumitem documentation, in German
Version:        svn24196
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-enumitem-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-enumitem-de-doc <= 11:%{version}

%description -n texlive-translation-enumitem-de
This is a translation of the manual for enumitem.

%package -n texlive-translation-europecv-de
Summary:        German version of europecv
Version:        svn23840
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-europecv-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-europecv-de-doc <= 11:%{version}

%description -n texlive-translation-europecv-de
This is a "translation" of the europecv documentation.

%package -n texlive-translation-filecontents-de
Summary:        German version of filecontents
Version:        svn24010
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-filecontents-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-filecontents-de-doc <= 11:%{version}

%description -n texlive-translation-filecontents-de
This is a "translation" of the filecontents documentation.

%package -n texlive-translation-moreverb-de
Summary:        German version of moreverb
Version:        svn23957
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-moreverb-de-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-moreverb-de-doc <= 11:%{version}

%description -n texlive-translation-moreverb-de
This is a "translation" of the moreverb documentation.

%package -n texlive-udesoftec
Summary:        Thesis class for the University of Duisburg-Essen
Version:        svn57866
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyphenat.sty)
Requires:       tex(natbib.sty)
Requires:       tex(regexpatch.sty)
Requires:       tex(uri.sty)
Requires:       tex(xstring.sty)
Provides:       tex(udesoftec-bibcommon.sty) = %{tl_version}
Provides:       tex(udesoftec-biblatex.sty) = %{tl_version}
Provides:       tex(udesoftec-bst.sty) = %{tl_version}
Provides:       tex(udesoftec-extra.sty) = %{tl_version}

%description -n texlive-udesoftec
The class is designed for typesetting theses in the Research Group for Business
Informatics and Software Engineering. (The class may also serve as a template
for such theses.) The class is designed for use with pdfLaTeX; input in UTF-8
encoding is assumed.

%package -n texlive-uhrzeit
Summary:        Time printing, in German
Version:        svn39570
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(soul.sty)
Provides:       tex(uhrzeit.sty) = %{tl_version}

%description -n texlive-uhrzeit
The primary goal of this package is to facilitate formats and ranges of times
as formerly used in Germany. A variety of printing formats are available.

%package -n texlive-umlaute
Summary:        German input encodings in LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(inputenc.sty)
Provides:       tex(atari.def) = %{tl_version}
Provides:       tex(isolatin.def) = %{tl_version}
Provides:       tex(mac.def) = %{tl_version}
Provides:       tex(pc850.def) = %{tl_version}
Provides:       tex(roman8.def) = %{tl_version}
Provides:       tex(umlaute.sty) = %{tl_version}

%description -n texlive-umlaute
An early package for using alternate input encodings. The author considers the
package mostly obsolete, since most of its functions are taken by the inputenc
package; however, inputenc doesn't support the roman8 and atari encodings, so
umlaute remains the sole source of that support.

%package -n texlive-voss-mathcol
Summary:        Typesetting mathematics in colour, in (La)TeX
Version:        svn32954
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-voss-mathcol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-voss-mathcol-doc <= 11:%{version}

%description -n texlive-voss-mathcol
This is a short paper from the TeXnische Komodie, in German. Since the body of
the paper is dominated by clear LaTeX coding examples, most LaTeX programmers
will understand how to achieve the results shown in the diagrams, even if they
don't understand German.

%post -n texlive-dehyph-exptl
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/german-x-2024-02-28.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "german-x-2024-02-28 dehypht-x-2024-02-28.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=german-x-latest.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=german-x-latest" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{german-x-2024-02-28}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{german-x-2024-02-28}{dehypht-x-2024-02-28.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{german-x-latest}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{german-x-latest}{dehypht-x-2024-02-28.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/ngerman-x-2024-02-28.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ngerman-x-2024-02-28 dehyphn-x-2024-02-28.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=ngerman-x-latest.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=ngerman-x-latest" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ngerman-x-2024-02-28}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ngerman-x-2024-02-28}{dehyphn-x-2024-02-28.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{ngerman-x-latest}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ngerman-x-latest}{dehyphn-x-2024-02-28.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-dehyph-exptl
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/german-x-2024-02-28.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=german-x-latest.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{german-x-2024-02-28}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{german-x-latest}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/ngerman-x-2024-02-28.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=ngerman-x-latest.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ngerman-x-2024-02-28}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ngerman-x-latest}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-german
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/german.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "german loadhyph-de-1901.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{german}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{german}{loadhyph-de-1901.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/ngerman.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ngerman loadhyph-de-1996.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ngerman}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ngerman}{loadhyph-de-1996.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/swissgerman.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "swissgerman loadhyph-de-ch-1901.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{swissgerman}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{swissgerman}{loadhyph-de-ch-1901.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-german
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/german.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{german}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/ngerman.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ngerman}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/swissgerman.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{swissgerman}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-apalike-german
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/apalike-german/
%doc %{_texmf_main}/doc/bibtex/apalike-german/

%files -n texlive-autotype
%license other-free.txt
%{_texmf_main}/tex/lualatex/autotype/
%doc %{_texmf_main}/doc/lualatex/autotype/

%files -n texlive-babel-german
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-german/
%doc %{_texmf_main}/doc/generic/babel-german/

%files -n texlive-bibleref-german
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-german/
%doc %{_texmf_main}/doc/latex/bibleref-german/

%files -n texlive-booktabs-de
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/booktabs-de/

%files -n texlive-csquotes-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/csquotes-de/

%files -n texlive-dehyph
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/dehyph/

%files -n texlive-dehyph-exptl
%license mit.txt
%{_texmf_main}/tex/generic/dehyph-exptl/
%doc %{_texmf_main}/doc/generic/dehyph-exptl/

%files -n texlive-dhua
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/dhua/
%doc %{_texmf_main}/doc/latex/dhua/

%files -n texlive-dtk-bibliography
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/dtk-bibliography/
%{_texmf_main}/tex/latex/dtk-bibliography/
%doc %{_texmf_main}/doc/bibtex/dtk-bibliography/

%files -n texlive-etdipa
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/etdipa/

%files -n texlive-etoolbox-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/etoolbox-de/

%files -n texlive-fifinddo-info
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/fifinddo-info/

%files -n texlive-fragoli
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fragoli/
%doc %{_texmf_main}/doc/latex/fragoli/

%files -n texlive-german
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/german/
%doc %{_texmf_main}/doc/generic/german/

%files -n texlive-germbib
%license other-free.txt
%{_texmf_main}/bibtex/bst/germbib/
%{_texmf_main}/tex/latex/germbib/
%doc %{_texmf_main}/doc/bibtex/germbib/

%files -n texlive-germkorr
%license gpl2.txt
%{_texmf_main}/tex/latex/germkorr/
%doc %{_texmf_main}/doc/latex/germkorr/

%files -n texlive-hausarbeit-jura
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hausarbeit-jura/
%doc %{_texmf_main}/doc/latex/hausarbeit-jura/

%files -n texlive-hyphen-german
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-koma-script-examples
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/koma-script-examples/

%files -n texlive-l2picfaq
%license fdl.txt
%doc %{_texmf_main}/doc/latex/l2picfaq/

%files -n texlive-latexcheat-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latexcheat-de/

%files -n texlive-lualatex-doc-de
%license fdl.txt
%doc %{_texmf_main}/doc/latex/lualatex-doc-de/

%files -n texlive-microtype-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/microtype-de/

%files -n texlive-milog
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/milog/
%doc %{_texmf_main}/doc/latex/milog/

%files -n texlive-quran-de
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/quran-de/
%doc %{_texmf_main}/doc/xelatex/quran-de/

%files -n texlive-r_und_s
%license bsd.txt
%{_texmf_main}/tex/latex/r_und_s/
%doc %{_texmf_main}/doc/latex/r_und_s/

%files -n texlive-schulmathematik
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/schulmathematik/
%doc %{_texmf_main}/doc/latex/schulmathematik/

%files -n texlive-templates-fenn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/templates-fenn/

%files -n texlive-templates-sommer
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/templates-sommer/

%files -n texlive-termcal-de
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/termcal-de/
%doc %{_texmf_main}/doc/latex/termcal-de/

%files -n texlive-texlive-de
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-de/

%files -n texlive-tipa-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/tipa-de/

%files -n texlive-translation-arsclassica-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-arsclassica-de/

%files -n texlive-translation-biblatex-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-biblatex-de/

%files -n texlive-translation-chemsym-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-chemsym-de/

%files -n texlive-translation-ecv-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-ecv-de/

%files -n texlive-translation-enumitem-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-enumitem-de/

%files -n texlive-translation-europecv-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-europecv-de/

%files -n texlive-translation-filecontents-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-filecontents-de/

%files -n texlive-translation-moreverb-de
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-moreverb-de/

%files -n texlive-udesoftec
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/udesoftec/
%{_texmf_main}/tex/latex/udesoftec/
%doc %{_texmf_main}/doc/latex/udesoftec/

%files -n texlive-uhrzeit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/uhrzeit/
%doc %{_texmf_main}/doc/latex/uhrzeit/

%files -n texlive-umlaute
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/umlaute/
%doc %{_texmf_main}/doc/latex/umlaute/

%files -n texlive-voss-mathcol
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/voss-mathcol/

%changelog
* Mon Jan 26 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn74675-4
- remove l2tabu (OPL is non-free)
- update babel-german

* Sat Jan 24 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn74675-3
- remove lshort-german (OPL is non-free)
- update components
- fix licensing
- fix descriptions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74675-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74675-1
- Update to TeX Live 2025
