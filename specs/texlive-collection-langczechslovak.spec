%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langczechslovak
Epoch:          12
Version:        svn54074
Release:        4%{?dist}
Summary:        Czech/Slovak

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langczechslovak.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-czech.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-czech.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovak.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovak.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cnbwp.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cnbwp.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cs.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csbulletin.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csbulletin.doc.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cstex.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cstex.doc.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-czech.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-slovak.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-czech.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-czech.doc.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovak.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovak.doc.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-cz.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-cz.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-babel-czech
Requires:       texlive-babel-slovak
Requires:       texlive-cnbwp
Requires:       texlive-cs
Requires:       texlive-csbulletin
Requires:       texlive-cslatex
Requires:       texlive-csplain
Requires:       texlive-cstex
Requires:       texlive-hyphen-czech
Requires:       texlive-hyphen-slovak
Requires:       texlive-vlna
Requires:       texlive-lshort-czech
Requires:       texlive-lshort-slovak
Requires:       texlive-texlive-cz

%description
Support for Czech/Slovak.


%package -n texlive-babel-czech
Summary:        Babel support for Czech
Version:        svn30261
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(czech.ldf) = %{tl_version}

%description -n texlive-babel-czech
The package provides the language definition file for support of Czech in
babel. Some shortcuts are defined, as well as translations to Czech of standard
"LaTeX names".

%package -n texlive-babel-slovak
Summary:        Babel support for typesetting Slovak
Version:        svn30292
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(slovak.ldf) = %{tl_version}

%description -n texlive-babel-slovak
The package provides the language definition file for support of Slovak in
babel, including Slovak variants of LaTeX built-in-names. Shortcuts are also
defined.

%package -n texlive-cnbwp
Summary:        Typeset working papers of the Czech National Bank
Version:        svn69910
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(multicol.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(rotating.sty)
Requires:       tex(url.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xevlna.sty)
Requires:       tex(zwpagelayout.sty)
Provides:       tex(cnbwp-manual.sty) = %{tl_version}

%description -n texlive-cnbwp
The package supports proper formatting of Working Papers of the Czech National
Bank (WP CNB). The package was developed for CNB but it is also intended for
authors from outside CNB.

%package -n texlive-cs
Summary:        Czech/Slovak-tuned Computer Modern fonts
Version:        svn41553
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-cmexb

%description -n texlive-cs
The fonts are provided as Metafont source; Type 1 format versions (csfonts-t1)
are also available.

%package -n texlive-csbulletin
Summary:        LaTeX class for articles submitted to the CSTUG Bulletin (Zpravodaj)
Version:        svn77112
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(csbulacronym.sty) = %{tl_version}
Provides:       tex(csbulobalka.sty) = %{tl_version}

%description -n texlive-csbulletin
The package provides the class for articles for the CSTUG Bulletin (Zpravodaj
Ceskoslovenskeho sdruzeni uzivatelu TeXu). You can see the structure of a
document by looking at the source file of the manual.

%package -n texlive-cstex
Summary:        Support for Czech/Slovak languages
Version:        svn64149
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cstex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cstex-doc <= 11:%{version}

%description -n texlive-cstex
This package mirrors the macros part of the home site's distribution of CSTeX.
The licence (modified GPL) applies to some of the additions that make it a
Czech/Slovak language distribution, rather than the distribution of a basic
Plain/LaTeX distribution.

%package -n texlive-hyphen-czech
Summary:        Czech hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-cs.ec.tex) = %{tl_version}
Provides:       tex(hyph-cs.tex) = %{tl_version}
Provides:       tex(loadhyph-cs.tex) = %{tl_version}

%description -n texlive-hyphen-czech
Hyphenation patterns for Czech in T1/EC and UTF-8 encodings. Original patterns
'czhyphen' are still distributed in the 'csplain' package and loaded with ISO
Latin 2 encoding (IL2).

%package -n texlive-hyphen-slovak
Summary:        Slovak hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sk.ec.tex) = %{tl_version}
Provides:       tex(hyph-sk.tex) = %{tl_version}
Provides:       tex(loadhyph-sk.tex) = %{tl_version}

%description -n texlive-hyphen-slovak
Hyphenation patterns for Slovak in T1/EC and UTF-8 encodings. Original patterns
'skhyphen' are still distributed in the 'csplain' package and loaded with ISO
Latin 2 encoding (IL2).

%package -n texlive-lshort-czech
Summary:        Czech translation of the "Short Introduction to LaTeX2e"
Version:        svn55643
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-czech-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-czech-doc <= 11:%{version}

%description -n texlive-lshort-czech
This is the Czech translation of "A Short Introduction to LaTeX2e".

%package -n texlive-lshort-slovak
Summary:        Slovak introduction to LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-slovak-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-slovak-doc <= 11:%{version}

%description -n texlive-lshort-slovak
A Slovak translation of Oetiker's (not so) short introduction.

%package -n texlive-texlive-cz
Summary:        TeX Live manual (Czech/Slovak)
Version:        svn77067
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-cz-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-cz-doc <= 11:%{version}

%description -n texlive-texlive-cz
TeX Live manual (Czech/Slovak)

%post -n texlive-hyphen-czech
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/czech.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "czech loadhyph-cs.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{czech}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{czech}{loadhyph-cs.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-czech
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/czech.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{czech}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-slovak
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/slovak.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "slovak loadhyph-sk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{slovak}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{slovak}{loadhyph-sk.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-slovak
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/slovak.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{slovak}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-babel-czech
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-czech/
%doc %{_texmf_main}/doc/generic/babel-czech/

%files -n texlive-babel-slovak
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-slovak/
%doc %{_texmf_main}/doc/generic/babel-slovak/

%files -n texlive-cnbwp
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/cnbwp/
%{_texmf_main}/makeindex/cnbwp/
%{_texmf_main}/tex/latex/cnbwp/
%doc %{_texmf_main}/doc/latex/cnbwp/

%files -n texlive-cs
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/cs/
%{_texmf_main}/fonts/map/dvips/cs/
%{_texmf_main}/fonts/source/public/cs/
%{_texmf_main}/fonts/tfm/cs/cs-a35/
%{_texmf_main}/fonts/tfm/cs/cs-charter/
%{_texmf_main}/fonts/tfm/public/cs/
%{_texmf_main}/fonts/type1/public/cs/
%{_texmf_main}/fonts/vf/cs/cs-a35/
%{_texmf_main}/fonts/vf/cs/cs-charter/

%files -n texlive-csbulletin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/csbulletin/
%doc %{_texmf_main}/doc/latex/csbulletin/

%files -n texlive-cstex
%license pd.txt
%doc %{_texmf_main}/doc/cstex/

%files -n texlive-hyphen-czech
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-slovak
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-lshort-czech
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-czech/

%files -n texlive-lshort-slovak
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/lshort-slovak/

%files -n texlive-texlive-cz
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-cz/

%changelog
* Sun Feb  8 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-4
- bump for rebuild

* Thu Jan 15 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-3
- fix descriptions, update to latest components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-1
- Update to TeX Live 2025
