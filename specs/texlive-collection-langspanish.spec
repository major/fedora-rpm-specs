%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langspanish
Epoch:          12
Version:        svn72203
Release:        3%{?dist}
Summary:        Spanish

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langspanish.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antique-spanish-units.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antique-spanish-units.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-catalan.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-catalan.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-galician.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-galician.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-spanish.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-spanish.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/es-tex-faq.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/es-tex-faq.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-catalan.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-galician.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-spanish.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-spanish.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-spanish.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-spanish.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo-spanish.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo-spanish.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-esmx.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat-esmx.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-spanish.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-spanish.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-es.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-es.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-es.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-es.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-antique-spanish-units
Requires:       texlive-babel-catalan
Requires:       texlive-babel-galician
Requires:       texlive-babel-spanish
Requires:       texlive-collection-basic
Requires:       texlive-es-tex-faq
Requires:       texlive-hyphen-catalan
Requires:       texlive-hyphen-galician
Requires:       texlive-hyphen-spanish
Requires:       texlive-l2tabu-spanish
Requires:       texlive-latex2e-help-texinfo-spanish
Requires:       texlive-latexcheat-esmx
Requires:       texlive-lshort-spanish
Requires:       texlive-quran-es
Requires:       texlive-texlive-es

%description
Support for Spanish.


%package -n texlive-antique-spanish-units
Summary:        A short document about antique spanish units
Version:        svn69568
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-antique-spanish-units-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-antique-spanish-units-doc <= 11:%{version}

%description -n texlive-antique-spanish-units
This short document is about antique spanish units used in Spain and their
colonies between the sixteenth and nineteenth centuries. The next step will be
to develop a LaTeX package similar to siunitx. The document could be
interesting for historians, economists, metrologists and others, as a reference
and detailed compendium about this old system of units.

%package -n texlive-babel-catalan
Summary:        Babel contributed support for Catalan
Version:        svn30259
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(catalan.ldf) = %{tl_version}

%description -n texlive-babel-catalan
The package establishes Catalan conventions in a document (or a subset of the
conventions, if Catalan is not the main language of the document).

%package -n texlive-babel-galician
Summary:        Babel/Polyglossia support for Galician
Version:        svn30270
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(galician.ldf) = %{tl_version}

%description -n texlive-babel-galician
The package provides a language description file that enables support of
Galician either with babel or with polyglossia.

%package -n texlive-babel-spanish
Summary:        Babel support for Spanish
Version:        svn59367
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(romanidx.sty) = %{tl_version}
Provides:       tex(spanish.ldf) = %{tl_version}

%description -n texlive-babel-spanish
This bundle provides the means to typeset Spanish text, with the support
provided by the LaTeX standard package babel. Note that separate support is
provided for those who wish to typeset Spanish as written in Mexico.

%package -n texlive-es-tex-faq
Summary:        CervanTeX (Spanish TeX Group) FAQ
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-es-tex-faq-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-es-tex-faq-doc <= 11:%{version}

%description -n texlive-es-tex-faq
SGML source, converted LaTeX version, and readable copies of the FAQ from the
Spanish TeX users group.

%package -n texlive-hyphen-catalan
Summary:        Catalan hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ca.ec.tex) = %{tl_version}
Provides:       tex(hyph-ca.tex) = %{tl_version}
Provides:       tex(loadhyph-ca.tex) = %{tl_version}

%description -n texlive-hyphen-catalan
Hyphenation patterns for Catalan in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-galician
Summary:        Galician hyphenation patterns.
Version:        svn73410
License:        Unlicense
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-gl.ec.tex) = %{tl_version}
Provides:       tex(hyph-gl.tex) = %{tl_version}
Provides:       tex(loadhyph-gl.tex) = %{tl_version}

%description -n texlive-hyphen-galician
Hyphenation patterns for Galician in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-spanish
Summary:        Spanish hyphenation patterns.
Version:        svn75447
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-es.ec.tex) = %{tl_version}
Provides:       tex(hyph-es.tex) = %{tl_version}
Provides:       tex(loadhyph-es.tex) = %{tl_version}

%description -n texlive-hyphen-spanish
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.

%package -n texlive-l2tabu-spanish
Summary:        Spanish translation of "Obsolete packages and commands"
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l2tabu-spanish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l2tabu-spanish-doc <= 11:%{version}

%description -n texlive-l2tabu-spanish
A Spanish translation of the l2tabu practical guide to LaTeX2e by Mark Trettin.
A list of obsolete packages, commands and usages.

%package -n texlive-latex2e-help-texinfo-spanish
Summary:        Unofficial reference manual covering LaTeX2e
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex2e-help-texinfo-spanish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex2e-help-texinfo-spanish-doc <= 11:%{version}

%description -n texlive-latex2e-help-texinfo-spanish
The manual is provided as Texinfo source (which was originally derived from the
VMS help file in the DECUS TeX distribution of 1990, with many subsequent
changes). This is a collaborative development, and details of getting involved
are to be found on the package home page. A Spanish translation is included
here, and a French translation is available as a separate package. All the
other formats in the distribution are derived from the Texinfo source, as
usual.

%package -n texlive-latexcheat-esmx
Summary:        A LaTeX cheat sheet, in Spanish
Version:        svn36866
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcheat-esmx-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcheat-esmx-doc <= 11:%{version}

%description -n texlive-latexcheat-esmx
This is a translation to Spanish (Castellano) of Winston Chang's LaTeX cheat
sheet (a reference sheet for writing scientific papers).

%package -n texlive-lshort-spanish
Summary:        Short introduction to LaTeX, Spanish translation
Version:        svn35050
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-spanish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-spanish-doc <= 11:%{version}

%description -n texlive-lshort-spanish
A Spanish translation of the Short Introduction to LaTeX2e, version 20.

%package -n texlive-quran-es
Summary:        Spanish Translations for the quran package
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-es.sty) = %{tl_version}
Provides:       tex(qurantext-esi.translation.def) = %{tl_version}
Provides:       tex(qurantext-esii.translation.def) = %{tl_version}
Provides:       tex(qurantext-esiii.translation.def) = %{tl_version}

%description -n texlive-quran-es
The package is designed for typesetting several Spanish translations of the
Holy Quran. It extends the quran package by adding three additional Spanish
translations.

%package -n texlive-texlive-es
Summary:        TeX Live manual (Spanish)
Version:        svn74997
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-es-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-es-doc <= 11:%{version}

%description -n texlive-texlive-es
TeX Live manual (Spanish)

%post -n texlive-hyphen-catalan
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/catalan.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "catalan loadhyph-ca.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{catalan}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{catalan}{loadhyph-ca.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-catalan
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/catalan.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{catalan}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-galician
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/galician.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "galician loadhyph-gl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{galician}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{galician}{loadhyph-gl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-galician
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/galician.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{galician}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-spanish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/spanish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "spanish loadhyph-es.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=espanol.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=espanol" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{spanish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{espanol}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{espanol}{loadhyph-es.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-spanish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/spanish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=espanol.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{spanish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{espanol}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-antique-spanish-units
%license cc-by-4.txt
%doc %{_texmf_main}/doc/generic/antique-spanish-units/

%files -n texlive-babel-catalan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-catalan/
%doc %{_texmf_main}/doc/generic/babel-catalan/

%files -n texlive-babel-galician
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-galician/
%doc %{_texmf_main}/doc/generic/babel-galician/

%files -n texlive-babel-spanish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-spanish/
%doc %{_texmf_main}/doc/generic/babel-spanish/

%files -n texlive-es-tex-faq
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/generic/es-tex-faq/

%files -n texlive-hyphen-catalan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-galician
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-spanish
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%doc %{_texmf_main}/doc/generic/hyph-utf8/

%files -n texlive-l2tabu-spanish
%license pd.txt
%doc %{_texmf_main}/doc/latex/l2tabu-spanish/

%files -n texlive-latex2e-help-texinfo-spanish
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/info/
%doc %{_texmf_main}/doc/latex/latex2e-help-texinfo-spanish/

%files -n texlive-latexcheat-esmx
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latexcheat-esmx/

%files -n texlive-lshort-spanish
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-spanish/

%files -n texlive-quran-es
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/quran-es/
%doc %{_texmf_main}/doc/xelatex/quran-es/

%files -n texlive-texlive-es
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-es/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72203-3
- fix licensing, descriptions, update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72203-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72203-1
- Update to TeX Live 2025
