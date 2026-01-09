%global tl_version 2025

Name:           texlive-scheme-medium
Epoch:          12
Version:        svn54074
Release:        1%{?dist}
Summary:        medium scheme (small + more packages and languages)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-binextra
Requires:       texlive-collection-context
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-collection-fontutils
Requires:       texlive-collection-langczechslovak
Requires:       texlive-collection-langenglish
Requires:       texlive-collection-langeuropean
Requires:       texlive-collection-langfrench
Requires:       texlive-collection-langgerman
Requires:       texlive-collection-langitalian
Requires:       texlive-collection-langpolish
Requires:       texlive-collection-langportuguese
Requires:       texlive-collection-langspanish
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
Requires:       texlive-collection-luatex
Requires:       texlive-collection-mathscience
Requires:       texlive-collection-metapost
Requires:       texlive-collection-plaingeneric
Requires:       texlive-collection-texworks
Requires:       texlive-collection-xetex

%description
medium scheme (small + more packages and languages) This is the medium TeX Live
collection: it contains plain TeX, LaTeX, many recommended packages, and
support for most European languages.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-1
- Update to TeX Live 2025