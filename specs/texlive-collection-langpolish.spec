%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langpolish
Epoch:          12
Version:        svn54074
Release:        3%{?dist}
Summary:        Polish

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langpolish.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-polish.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-polish.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bredzenie.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bredzenie.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cc-pl.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cc-pl.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gustlib.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gustlib.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-polish.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-polish.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-polish.doc.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mwcls.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mwcls.doc.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pl.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pl.doc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polski.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/polski.doc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/przechlewski-book.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/przechlewski-book.doc.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qpxqtx.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qpxqtx.doc.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tap.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tap.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-virtual-academy-pl.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-virtual-academy-pl.doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-pl.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-pl.doc.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utf8mex.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/utf8mex.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-latex
Requires:       texlive-collection-basic
Requires:       texlive-babel-polish
Requires:       texlive-bredzenie
Requires:       texlive-cc-pl
Requires:       texlive-gustlib
Requires:       texlive-hyphen-polish
Requires:       texlive-lshort-polish
Requires:       texlive-mex
Requires:       texlive-mwcls
Requires:       texlive-pl
Requires:       texlive-polski
Requires:       texlive-przechlewski-book
Requires:       texlive-qpxqtx
Requires:       texlive-tap
Requires:       texlive-tex-virtual-academy-pl
Requires:       texlive-texlive-pl
Requires:       texlive-utf8mex

%description
Support for Polish.


%package -n texlive-babel-polish
Summary:        Babel support for Polish
Version:        svn62680
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(polish-compat.ldf) = %{tl_version}
Provides:       tex(polish.ldf) = %{tl_version}

%description -n texlive-babel-polish
The package provides the language definition file for support of Polish in
babel. Some shortcuts are defined, as well as translations to Polish of
standard "LaTeX names".

%package -n texlive-bredzenie
Summary:        A Polish version of "lorem ipsum..." in the form of a LaTeX package
Version:        svn44371
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bredzenie.sty) = %{tl_version}

%description -n texlive-bredzenie
This is a polish version of the classic pseudo-Latin "lorem ipsum dolor sit
amet...". It provides access to several paragraphs of pseudo-Polish generated
with Hidden Markov Models and Recurrent Neural Networks trained on a corpus of
Polish.

%package -n texlive-cc-pl
Summary:        Polish extension of Computer Concrete fonts
Version:        svn58602
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cc-pl
These Metafont sources rely on the availability of the Metafont 'Polish' fonts
and of the Metafont sources of the original Concrete fonts. Adobe Type 1
versions of the fonts are included.

%package -n texlive-gustlib
Summary:        Plain macros for much core and extra functionality, from GUST
Version:        svn54074
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(biblotex.tex) = %{tl_version}
Provides:       tex(infr-ex.tex) = %{tl_version}
Provides:       tex(infram.tex) = %{tl_version}
Provides:       tex(map.tex) = %{tl_version}
Provides:       tex(mcol-ex.tex) = %{tl_version}
Provides:       tex(meashor.tex) = %{tl_version}
Provides:       tex(mimulcol.tex) = %{tl_version}
Provides:       tex(plidxmac.tex) = %{tl_version}
Provides:       tex(przyklad.tex) = %{tl_version}
Provides:       tex(rbox-ex.tex) = %{tl_version}
Provides:       tex(roundbox.tex) = %{tl_version}
Provides:       tex(split.tex) = %{tl_version}
Provides:       tex(tp-crf.tex) = %{tl_version}
Provides:       tex(tsp.tex) = %{tl_version}
Provides:       tex(tun.tex) = %{tl_version}
Provides:       tex(verbatim-dek.tex) = %{tl_version}

%description -n texlive-gustlib
Includes bibliography support, token manipulation, cross-references, verbatim,
determining length of a paragraph's last line, multicolumn output, Polish
bibliography and index styles, prepress and color separation, graphics
manipulation, tables.

%package -n texlive-hyphen-polish
Summary:        Polish hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-pl.qx.tex) = %{tl_version}
Provides:       tex(hyph-pl.tex) = %{tl_version}
Provides:       tex(loadhyph-pl.tex) = %{tl_version}

%description -n texlive-hyphen-polish
Hyphenation patterns for Polish in QX and UTF-8 encodings. These patterns are
also used by Polish TeX formats MeX and LaMeX.

%package -n texlive-lshort-polish
Summary:        Introduction to LaTeX in Polish
Version:        svn63289
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-polish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-polish-doc <= 11:%{version}

%description -n texlive-lshort-polish
This is the Polish translation of A Short Introduction to LaTeX2e.

%package -n texlive-mwcls
Summary:        Polish-oriented document classes
Version:        svn77050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mwcls
mwcls is a set of document classes for LaTeX2e designed with Polish
typographical tradition in mind. Classes include: 'mwart' (which is a
replacement for 'article'), 'mwrep' (replacing 'report'), and 'mwbk' (replacing
'book'). Most features present in standard classes work with mwcls classes.
Some extensions/exceptions include: sectioning commands allow for second
optional argument (it is possible to state different texts for running head and
for TOC), new environments 'itemize*' and 'enumerate*' for lists with long
items, page styles have variants for normal, opening, closing, and blank pages.

%package -n texlive-pl
Summary:        Polish extension of Computer Modern fonts
Version:        svn58661
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-pl
The Polish extension of the Computer Modern fonts (compatible with CM itself)
for use with Polish TeX formats. The fonts were originally a part of the MeX
distribution (and they are still available that way).

%package -n texlive-polski
Summary:        Typeset Polish documents with LaTeX and Polish fonts
Version:        svn60322
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyphen-polish
Requires:       texlive-pl
Provides:       tex(amigapl.def) = %{tl_version}
Provides:       tex(mazovia.def) = %{tl_version}
Provides:       tex(ot1patch.sty) = %{tl_version}
Provides:       tex(plprefix.sty) = %{tl_version}
Provides:       tex(polski.sty) = %{tl_version}
Provides:       tex(qxenc.def) = %{tl_version}

%description -n texlive-polski
Tools to typeset monolingual Polish documents in LaTeX2e without babel or
polyglossia. The package loads Polish hyphenation patterns, ensures that a font
encoding suitable for Polish is used; in particular it enables Polish
adaptation of Computer Modern fonts (the so-called PL fonts), provides
translations of \today and names like "Bibliography" or "Chapter", redefines
math symbols according to Polish typographical tradition, provides macros for
dashes according to Polish orthography, provides a historical input method for
"Polish characters", works with traditional TeX as well as with Unicode aware
variants. (This package was previously known as platex, but has been renamed to
resolve a name clash.)

%package -n texlive-przechlewski-book
Summary:        Examples from Przechlewski's LaTeX book
Version:        svn23552
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-przechlewski-book
The bundle provides machine-readable copies of the examples from the book
"Praca magisterska i dyplomowa z programem LaTeX".

%package -n texlive-qpxqtx
Summary:        Polish macros and fonts supporting Pagella/pxfonts and Termes/txfonts
Version:        svn45797
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(amspbold.tex) = %{tl_version}
Provides:       tex(amsqpx.def) = %{tl_version}
Provides:       tex(amsqpx.tex) = %{tl_version}
Provides:       tex(amsqtx.def) = %{tl_version}
Provides:       tex(amsqtx.tex) = %{tl_version}
Provides:       tex(amstbold.tex) = %{tl_version}
Provides:       tex(qpxmath.sty) = %{tl_version}
Provides:       tex(qpxmath.tex) = %{tl_version}
Provides:       tex(qtxmath.sty) = %{tl_version}
Provides:       tex(qtxmath.tex) = %{tl_version}

%description -n texlive-qpxqtx
Polish macros and fonts supporting Pagella/pxfonts and Termes/txfonts

%package -n texlive-tap
Summary:        TeX macros for typesetting complex tables
Version:        svn31731
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(tap.tex) = %{tl_version}

%description -n texlive-tap
The package offers a simple notation for pretty complex tables (to Michael J.
Ferguson's credit). With PostScript, the package allows shaded/coloured tables,
diagonal rules, etc. The package is supposed to work with both Plain and LaTeX.
An AWK converter from ASCII semigraphic tables to TAP notation is included.

%package -n texlive-tex-virtual-academy-pl
Summary:        TeX usage web pages, in Polish
Version:        svn67718
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-virtual-academy-pl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-virtual-academy-pl-doc <= 11:%{version}

%description -n texlive-tex-virtual-academy-pl
TeX Virtual Academy is a bundle of Polish documentation in HTML format about
TeX and Co. It contains information for beginners, LaTeX packages,
descriptions, etc.

%package -n texlive-texlive-pl
Summary:        TeX Live manual (Polish)
Version:        svn74803
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-pl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-pl-doc <= 11:%{version}

%description -n texlive-texlive-pl
TeX Live manual (Polish)

%package -n texlive-utf8mex
Summary:        Tools to produce formats that read Polish language input
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(utf8-pl.tex) = %{tl_version}
Provides:       tex(utf8plsq.tex) = %{tl_version}

%description -n texlive-utf8mex
The bundle provides files for building formats to read input in Polish
encodings.

%post -n texlive-hyphen-polish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/polish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "polish loadhyph-pl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{polish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{polish}{loadhyph-pl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-polish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/polish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{polish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-polish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-polish/
%doc %{_texmf_main}/doc/generic/babel-polish/

%files -n texlive-bredzenie
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bredzenie/
%doc %{_texmf_main}/doc/latex/bredzenie/

%files -n texlive-cc-pl
%license pd.txt
%{_texmf_main}/fonts/map/dvips/cc-pl/
%{_texmf_main}/fonts/source/public/cc-pl/
%{_texmf_main}/fonts/tfm/public/cc-pl/
%{_texmf_main}/fonts/type1/public/cc-pl/
%doc %{_texmf_main}/doc/fonts/cc-pl/

%files -n texlive-gustlib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bib/gustlib/
%{_texmf_main}/bibtex/bst/gustlib/
%{_texmf_main}/tex/plain/gustlib/
%doc %{_texmf_main}/doc/plain/gustlib/

%files -n texlive-hyphen-polish
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-lshort-polish
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-polish/

%files -n texlive-mwcls
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mwcls/
%doc %{_texmf_main}/doc/latex/mwcls/

%files -n texlive-pl
%license pd.txt
%{_texmf_main}/dvips/pl/
%{_texmf_main}/fonts/afm/public/pl/
%{_texmf_main}/fonts/enc/dvips/pl/
%{_texmf_main}/fonts/map/dvips/pl/
%{_texmf_main}/fonts/source/public/pl/
%{_texmf_main}/fonts/tfm/public/pl/
%{_texmf_main}/fonts/type1/public/pl/
%doc %{_texmf_main}/doc/fonts/pl/

%files -n texlive-polski
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/polski/
%doc %{_texmf_main}/doc/latex/polski/

%files -n texlive-przechlewski-book
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/przechlewski-book/
%{_texmf_main}/tex/latex/przechlewski-book/
%doc %{_texmf_main}/doc/latex/przechlewski-book/

%files -n texlive-qpxqtx
%license pd.txt
%{_texmf_main}/fonts/tfm/public/qpxqtx/
%{_texmf_main}/fonts/vf/public/qpxqtx/
%{_texmf_main}/tex/generic/qpxqtx/
%doc %{_texmf_main}/doc/fonts/qpxqtx/

%files -n texlive-tap
%license pd.txt
%{_texmf_main}/tex/generic/tap/
%doc %{_texmf_main}/doc/generic/tap/

%files -n texlive-tex-virtual-academy-pl
%license fdl.txt
%doc %{_texmf_main}/doc/generic/tex-virtual-academy-pl/

%files -n texlive-texlive-pl
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-pl/

%files -n texlive-utf8mex
%license pd.txt
%{_texmf_main}/tex/mex/utf8mex/
%doc %{_texmf_main}/doc/mex/utf8mex/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-3
- fix licensing, descriptions
- update mwcls

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-1
- Update to TeX Live 2025
