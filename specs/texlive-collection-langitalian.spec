%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langitalian
Epoch:          12
Version:        svn72943
Release:        3%{?dist}
Summary:        Italian

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langitalian.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsldoc-it.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsldoc-it.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsmath-it.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsmath-it.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsthdoc-it.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsthdoc-it.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antanilipsum.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antanilipsum.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-italian.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-italian.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-accursius.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-accursius.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/codicefiscaleitaliano.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/codicefiscaleitaliano.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyhdr-it.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fancyhdr-it.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixltxhyph.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixltxhyph.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frontespizio.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frontespizio.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-italian.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/itnumpar.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/itnumpar.doc.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4wp-it.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4wp-it.doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/layaureo.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/layaureo.doc.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-italian.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-italian.doc.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psfrag-italian.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psfrag-italian.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-it.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-it.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/verifica.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/verifica.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-amsldoc-it
Requires:       texlive-amsmath-it
Requires:       texlive-amsthdoc-it
Requires:       texlive-antanilipsum
Requires:       texlive-babel-italian
Requires:       texlive-biblatex-accursius
Requires:       texlive-codicefiscaleitaliano
Requires:       texlive-collection-basic
Requires:       texlive-fancyhdr-it
Requires:       texlive-fixltxhyph
Requires:       texlive-frontespizio
Requires:       texlive-hyphen-italian
Requires:       texlive-itnumpar
Requires:       texlive-latex4wp-it
Requires:       texlive-layaureo
Requires:       texlive-lshort-italian
Requires:       texlive-psfrag-italian
Requires:       texlive-texlive-it
Requires:       texlive-verifica

%description
Support for Italian.


%package -n texlive-amsldoc-it
Summary:        Italian translation of amsldoc
Version:        svn45662
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsldoc-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsldoc-it-doc <= 11:%{version}

%description -n texlive-amsldoc-it
Italian translation of amsldoc

%package -n texlive-amsmath-it
Summary:        Italian translations of some old amsmath documents
Version:        svn22930
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsmath-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsmath-it-doc <= 11:%{version}

%description -n texlive-amsmath-it
The documents are: diffs-m.txt of December 1999, and amsmath.faq of March 2000.

%package -n texlive-amsthdoc-it
Summary:        Italian translation of amsthdoc: Using the amsthm package
Version:        svn45662
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsthdoc-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsthdoc-it-doc <= 11:%{version}

%description -n texlive-amsthdoc-it
Italian translation of amsthdoc: Using the amsthm package

%package -n texlive-antanilipsum
Summary:        Generate sentences in the style of "Amici miei"
Version:        svn77161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(antanilipsum.sty) = %{tl_version}

%description -n texlive-antanilipsum
This package is an italian blind text generator that outputs supercazzole,
mocking nonsense phrases from the movie series Amici Miei ("My friends"),
directed by Mario Monicelli.

%package -n texlive-babel-italian
Summary:        Babel support for Italian text
Version:        svn77371
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(italian.ldf) = %{tl_version}

%description -n texlive-babel-italian
The package provides language definitions for use in babel.

%package -n texlive-biblatex-accursius
Summary:        Citing features for Italian jurists
Version:        svn72942
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(ext-verbose-trad1.bbx)
Requires:       tex(verbose-trad1.cbx)
Provides:       tex(accursius.bbx) = %{tl_version}
Provides:       tex(accursius.cbx) = %{tl_version}

%description -n texlive-biblatex-accursius
This style is primarily aimed at Italian legal jurists and provides them with
the ability to cite legal materials, such as legislative acts, regulations,
soft law, treaties and case law. Additionally, the style codifies the most
prevalent citation practices amongst Italian legal scholars. Specifically, with
regard to the citation of legal materials, this style, instead of developing
the entry types @jurisdiction, @legal, and @legislation, creates a new one:
@itprov, which can describe a wide range of legal sources. Furthermore, it
creates a second new entry type: @notetoprov, which is used specifically to
cite so-called "note a sentenza" (notes to judgement), which closely mirrors
@itprov, but is literature and, therefore, is intended to have the same
treatment as standard entry types. The citation commands are the standard ones.
The @itprov entry type comprises the list institution to indicate which
authority adopted the cited act; the kindprov, nprov, provtitle (or
titleparties) fields to indicate the minimal 'ID' of the act and many others.
Finally, the entry type allows to specify where the cited act was consulted,
whether from an official bulletin (the ofbull field), an official portal or a
private database (the ofportal field), or a journal or collection.

%package -n texlive-codicefiscaleitaliano
Summary:        Test the consistency of the Italian personal Fiscal Code
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(codicefiscaleitaliano.sty) = %{tl_version}

%description -n texlive-codicefiscaleitaliano
The alphanumeric string that forms the Italian personal Fiscal Code is prone to
be misspelled thus rendering a legal document invalid. The package quickly
verifies the consistency of the fiscal code string, and can therefore be useful
for lawyers and accountants that use fiscal codes very frequently.

%package -n texlive-fancyhdr-it
Summary:        Italian translation of fancyhdr documentation
Version:        svn21912
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancyhdr-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancyhdr-it-doc <= 11:%{version}

%description -n texlive-fancyhdr-it
The translation is of documentation provided with the fancyhdr package.

%package -n texlive-fixltxhyph
Summary:        Allow hyphenation of partially-emphasised substrings
Version:        svn73227
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(fixltxhyph.sty) = %{tl_version}

%description -n texlive-fixltxhyph
The package fixes the problem of TeX failing to hyphenate letter strings that
seem (to TeX) to be words, but which are followed by an apostrophe and then an
emphasis command. The cause of the problem is not the apostrophe, but the font
change in the middle of the string. The problem arises in Catalan, French,
Italian and Romansh.

%package -n texlive-frontespizio
Summary:        Create a frontispiece for Italian theses
Version:        svn24054
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(afterpage.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(environ.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(frontespizio.sty) = %{tl_version}

%description -n texlive-frontespizio
Typesetting a frontispiece independently of the layout of the main document is
difficult. This package provides a solution by producing an auxiliary TeX file
to be typeset on its own and the result is automatically included at the next
run. The markup necessary for the frontispiece is written in the main document
in a frontespizio environment. Documentation is mainly in Italian, as the style
is probably apt only to theses in Italy.

%package -n texlive-hyphen-italian
Summary:        Italian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-it.tex) = %{tl_version}
Provides:       tex(hyph-quote-it.tex) = %{tl_version}
Provides:       tex(loadhyph-it.tex) = %{tl_version}

%description -n texlive-hyphen-italian
Hyphenation patterns for Italian in ASCII encoding. Compliant with the
Recommendation UNI 6461 on hyphenation issued by the Italian Standards
Institution (Ente Nazionale di Unificazione UNI).

%package -n texlive-itnumpar
Summary:        Spell numbers in words (Italian)
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(itnumpar.sty) = %{tl_version}

%description -n texlive-itnumpar
Sometimes we need to say "Capitolo primo" or "Capitolo uno" instead of
"Capitolo 1", that is, spelling the number in words instead of the usual digit
form. This package provides support for spelling out numbers in Italian words,
both in cardinal and in ordinal form.

%package -n texlive-latex4wp-it
Summary:        LaTeX guide for word processor users, in Italian
Version:        svn36000
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex4wp-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex4wp-it-doc <= 11:%{version}

%description -n texlive-latex4wp-it
The package provides a version of the document in Italian

%package -n texlive-layaureo
Summary:        A package to improve the A4 page layout
Version:        svn19087
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(keyval.sty)
Provides:       tex(layaureo.sty) = %{tl_version}

%description -n texlive-layaureo
This package produces a wide page layout for documents that use A4 paper size.
Moreover, LayAureo provides both a simple hook for leaving an empty space which
is required if pages are bundled by a press binding (use option
binding=length), and an option called big which it forces typearea to become
maximum.

%package -n texlive-lshort-italian
Summary:        Introduction to LaTeX in Italian
Version:        svn57038
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-italian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-italian-doc <= 11:%{version}

%description -n texlive-lshort-italian
This is the Italian translation of the Short Introduction to LaTeX2e.

%package -n texlive-psfrag-italian
Summary:        PSfrag documentation in Italian
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-psfrag-italian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-psfrag-italian-doc <= 11:%{version}

%description -n texlive-psfrag-italian
This is a translation of the documentation that comes with the psfrag
documentation.

%package -n texlive-texlive-it
Summary:        TeX Live manual (Italian)
Version:        svn58653
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-it-doc <= 11:%{version}

%description -n texlive-texlive-it
TeX Live manual (Italian)

%package -n texlive-verifica
Summary:        Typeset (Italian high school) exercises
Version:        svn75682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-verifica
This class provides various environments and commands to produce the typical
exercises contained in a test. It is mainly intended for Italian high school
teachers, as the style is probably more in line with Italian high school tests.

%post -n texlive-hyphen-italian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/italian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "italian loadhyph-it.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{italian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{italian}{loadhyph-it.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-italian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/italian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{italian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-amsldoc-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsldoc-it/

%files -n texlive-amsmath-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsmath-it/

%files -n texlive-amsthdoc-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsthdoc-it/

%files -n texlive-antanilipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/antanilipsum/
%doc %{_texmf_main}/doc/latex/antanilipsum/

%files -n texlive-babel-italian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-italian/
%doc %{_texmf_main}/doc/generic/babel-italian/

%files -n texlive-biblatex-accursius
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-accursius/
%doc %{_texmf_main}/doc/latex/biblatex-accursius/

%files -n texlive-codicefiscaleitaliano
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/codicefiscaleitaliano/
%doc %{_texmf_main}/doc/latex/codicefiscaleitaliano/

%files -n texlive-fancyhdr-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/fancyhdr-it/

%files -n texlive-fixltxhyph
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fixltxhyph/
%doc %{_texmf_main}/doc/latex/fixltxhyph/

%files -n texlive-frontespizio
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/frontespizio/
%doc %{_texmf_main}/doc/latex/frontespizio/

%files -n texlive-hyphen-italian
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-itnumpar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/itnumpar/
%doc %{_texmf_main}/doc/latex/itnumpar/

%files -n texlive-latex4wp-it
%license fdl.txt
%doc %{_texmf_main}/doc/latex/latex4wp-it/

%files -n texlive-layaureo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/layaureo/
%doc %{_texmf_main}/doc/latex/layaureo/

%files -n texlive-lshort-italian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-italian/

%files -n texlive-psfrag-italian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/psfrag-italian/

%files -n texlive-texlive-it
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-it/

%files -n texlive-verifica
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/verifica/
%doc %{_texmf_main}/doc/latex/verifica/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72943-3
- fix descriptions, licensing
- drop l2tabu-italian (non-free)

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72943-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72943-1
- Update to TeX Live 2025
