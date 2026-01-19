%global tl_version 2025

Name:           texlive-scheme-gust
Epoch:          12
Version:        svn59755
Release:        2%{?dist}
Summary:        GUST TeX Live scheme

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-amslatex-primer
Requires:       texlive-amstex
Requires:       texlive-antt
Requires:       texlive-bibtex8
Requires:       texlive-collection-basic
Requires:       texlive-collection-context
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-collection-fontutils
Requires:       texlive-collection-langpolish
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
Requires:       texlive-collection-metapost
Requires:       texlive-collection-plaingeneric
Requires:       texlive-collection-texworks
Requires:       texlive-collection-xetex
Requires:       texlive-comment
Requires:       texlive-comprehensive
Requires:       texlive-concrete
Requires:       texlive-cyklop
Requires:       texlive-dvidvi
Requires:       texlive-dviljk
Requires:       texlive-fontinstallationguide
Requires:       texlive-gustprog
Requires:       texlive-impatient
Requires:       texlive-iwona
Requires:       texlive-metafont-beginners
Requires:       texlive-metapost-examples
Requires:       texlive-poltawski
Requires:       texlive-seetexk
Requires:       texlive-seminar
Requires:       texlive-tds
Requires:       texlive-tex4ht
Requires:       texlive-texdoc

%description
GUST TeX Live scheme This is the GUST TeX Live scheme: it is a set of files
sufficient to typeset Polish plain TeX, LaTeX and ConTeXt documents in
PostScript or PDF.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn59755-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn59755-1
- Update to TeX Live 2025