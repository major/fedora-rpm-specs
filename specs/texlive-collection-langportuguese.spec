%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langportuguese
Epoch:          12
Version:        svn73303
Release:        3%{?dist}
Summary:        Portuguese

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langportuguese.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-portuges.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-portuges.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-tut-pt.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/beamer-tut-pt.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cursolatex.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cursolatex.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feupphdteses.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feupphdteses.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-portuguese.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-via-exemplos.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-via-exemplos.doc.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-ptbr.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-ptbr.doc.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-portuguese.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-portuguese.doc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numberpt.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/numberpt.doc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ordinalpt.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ordinalpt.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptlatexcommands.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptlatexcommands.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabularray-abnt.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabularray-abnt.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xypic-tut-pt.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xypic-tut-pt.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-portuges
Requires:       texlive-beamer-tut-pt
Requires:       texlive-collection-basic
Requires:       texlive-cursolatex
Requires:       texlive-feupphdteses
Requires:       texlive-hyphen-portuguese
Requires:       texlive-latex-via-exemplos
Requires:       texlive-latexcheat-ptbr
Requires:       texlive-lshort-portuguese
Requires:       texlive-numberpt
Requires:       texlive-ordinalpt
Requires:       texlive-ptlatexcommands
Requires:       texlive-tabularray-abnt
Requires:       texlive-xypic-tut-pt

%description
Support for Portuguese and Brazilian Portuguese.


%package -n texlive-babel-portuges
Summary:        Babel support for Portuges
Version:        svn77468
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(brazil.ldf) = %{tl_version}
Provides:       tex(brazilian.ldf) = %{tl_version}
Provides:       tex(portuges.ldf) = %{tl_version}
Provides:       tex(portuguese.ldf) = %{tl_version}

%description -n texlive-babel-portuges
The package provides the language definition file for support of Portuguese and
Brazilian Portuguese in babel. Some shortcuts are defined, as well as
translations to Portuguese of standard "LaTeX names".

%package -n texlive-beamer-tut-pt
Summary:        An introduction to the Beamer class, in Portuguese
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-beamer-tut-pt-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-beamer-tut-pt-doc <= 11:%{version}

%description -n texlive-beamer-tut-pt
An introduction to the Beamer class, in Portuguese

%package -n texlive-cursolatex
Summary:        A LaTeX tutorial
Version:        svn24139
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cursolatex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cursolatex-doc <= 11:%{version}

%description -n texlive-cursolatex
The tutorial is presented as a set of slides (in Portuguese).

%package -n texlive-feupphdteses
Summary:        Typeset Engineering PhD theses at the University of Porto
Version:        svn30962
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(backref.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(couriers.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(grffile.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lineno.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pdflscape.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pgfgantt.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(placeins.sty)
Requires:       tex(setspace.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tabulary.sty)
Requires:       tex(tikz.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(feupphdteses.sty) = %{tl_version}

%description -n texlive-feupphdteses
A complete template for thesis/works of Faculdade de Engenharia da Universidade
do Porto (FEUP) Faculty of Engineering University of Porto.

%package -n texlive-hyphen-portuguese
Summary:        Portuguese hyphenation patterns.
Version:        svn74203
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-pt.ec.tex) = %{tl_version}
Provides:       tex(hyph-pt.tex) = %{tl_version}
Provides:       tex(loadhyph-pt.tex) = %{tl_version}

%description -n texlive-hyphen-portuguese
Hyphenation patterns for Portuguese in T1/EC and UTF-8 encodings.

%package -n texlive-latex-via-exemplos
Summary:        A LaTeX course written in Brazilian Portuguese language
Version:        svn77105
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-via-exemplos-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-via-exemplos-doc <= 11:%{version}

%description -n texlive-latex-via-exemplos
This is a LaTeX2e course written in Brazilian Portuguese language.

%package -n texlive-latexcheat-ptbr
Summary:        A LaTeX cheat sheet, in Brazilian Portuguese
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcheat-ptbr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcheat-ptbr-doc <= 11:%{version}

%description -n texlive-latexcheat-ptbr
This is a translation to Brazilian Portuguese of Winston Chang's LaTeX cheat
sheet

%package -n texlive-lshort-portuguese
Summary:        Introduction to LaTeX in Portuguese
Version:        svn55643
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-portuguese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-portuguese-doc <= 11:%{version}

%description -n texlive-lshort-portuguese
This is the Portuguese translation of A Short Introduction to LaTeX2e.

%package -n texlive-numberpt
Summary:        Counters spelled out in Portuguese
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(numberpt.sty) = %{tl_version}

%description -n texlive-numberpt
This packages defines commands to display counters spelled out in Portuguese.
The styles are \numberpt for "all lowercase" \Numberpt for "First word
capitalized" \NumberPt for "All Capitalized" \NUMBERPT for "ALL UPPERCASE" For
example, \renewcommand{\thechapter}{\NumberPt{chapter}} makes chapter titles to
be rendered as "Capitulo Um", "Capitulo Dois" etc. Options are offered to
select variations in the spelling of "14", or Brazilian vs. European Portuguese
forms in the spelling of "16", "17", and "19". The package requires expl3 and
xparse.

%package -n texlive-ordinalpt
Summary:        Counters as ordinal numbers in Portuguese
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ordinalpt.sty) = %{tl_version}

%description -n texlive-ordinalpt
The package provides a counter style (like \arabic, \alph and others) which
produces as output strings like "primeiro" ("first" in Portuguese), "segundo"
(second), and so on up to 1999th. Separate counter commands are provided for
different letter case variants, and for masculine and feminine gender
inflections.

%package -n texlive-ptlatexcommands
Summary:        LaTeX to commands in Portuguese
Version:        svn67125
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algorithm.sty)
Requires:       tex(algorithmic.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(PTLatexCommands.sty) = %{tl_version}

%description -n texlive-ptlatexcommands
This package transforms common commands used in LaTeX to commands in
Portuguese.

%package -n texlive-tabularray-abnt
Summary:        An ABNT (Brazilian standard) theme for tabularray
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(float.sty)
Requires:       tex(tabularray.sty)
Provides:       tex(tabularray-abnt-2025A.sty) = %{tl_version}
Provides:       tex(tabularray-abnt.sty) = %{tl_version}

%description -n texlive-tabularray-abnt
This is the abnt Brazilian standard style for tabularray. It provides the
themes abnt (for tables with numerical data) and quadro (for tables with text
information). Additional environments abnttblr, tallabnttblr, and longabnttblr
are wrappers to tblr, talltblr, and longtblr that apply the abnt theme
automatically and permit to set the table font using \SetAbntTblrFont{}
provided here.

%package -n texlive-xypic-tut-pt
Summary:        A tutorial for XY-pic, in Portuguese
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xypic-tut-pt-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xypic-tut-pt-doc <= 11:%{version}

%description -n texlive-xypic-tut-pt
A tutorial for XY-pic, in Portuguese

%post -n texlive-hyphen-portuguese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/portuguese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "portuguese loadhyph-pt.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=portuges.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=portuges" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{portuguese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{portuges}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-portuguese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/portuguese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=portuges.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{portuguese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{portuges}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-portuges
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-portuges/
%doc %{_texmf_main}/doc/generic/babel-portuges/

%files -n texlive-beamer-tut-pt
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/beamer-tut-pt/

%files -n texlive-cursolatex
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/cursolatex/

%files -n texlive-feupphdteses
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/feupphdteses/
%doc %{_texmf_main}/doc/latex/feupphdteses/

%files -n texlive-hyphen-portuguese
%license bsd.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-latex-via-exemplos
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-via-exemplos/

%files -n texlive-latexcheat-ptbr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latexcheat-ptbr/

%files -n texlive-lshort-portuguese
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-portuguese/

%files -n texlive-numberpt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/numberpt/
%doc %{_texmf_main}/doc/latex/numberpt/

%files -n texlive-ordinalpt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ordinalpt/
%doc %{_texmf_main}/doc/latex/ordinalpt/

%files -n texlive-ptlatexcommands
%license mit.txt
%{_texmf_main}/tex/latex/ptlatexcommands/
%doc %{_texmf_main}/doc/latex/ptlatexcommands/

%files -n texlive-tabularray-abnt
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tabularray-abnt/
%doc %{_texmf_main}/doc/latex/tabularray-abnt/

%files -n texlive-xypic-tut-pt
%license gpl2.txt
%doc %{_texmf_main}/doc/generic/xypic-tut-pt/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn73303-3
- fix licensing, descriptions
- update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73303-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73303-1
- Update to TeX Live 2025
