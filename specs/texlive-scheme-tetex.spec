%global tl_version 2025

Name:           texlive-scheme-tetex
Epoch:          12
Version:        svn74022
Release:        2%{?dist}
Summary:        teTeX scheme (more than medium, but nowhere near full)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-acronym
Requires:       texlive-amslatex-primer
Requires:       texlive-bbm
Requires:       texlive-bbm-macros
Requires:       texlive-bbold
Requires:       texlive-bibtex8
Requires:       texlive-cmbright
Requires:       texlive-collection-basic
Requires:       texlive-collection-context
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-collection-fontutils
Requires:       texlive-collection-formatsextra
Requires:       texlive-collection-langcjk
Requires:       texlive-collection-langcyrillic
Requires:       texlive-collection-langczechslovak
Requires:       texlive-collection-langenglish
Requires:       texlive-collection-langeuropean
Requires:       texlive-collection-langfrench
Requires:       texlive-collection-langgerman
Requires:       texlive-collection-langgreek
Requires:       texlive-collection-langitalian
Requires:       texlive-collection-langother
Requires:       texlive-collection-langpolish
Requires:       texlive-collection-langportuguese
Requires:       texlive-collection-langspanish
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
Requires:       texlive-collection-mathscience
Requires:       texlive-collection-metapost
Requires:       texlive-collection-pictures
Requires:       texlive-collection-plaingeneric
Requires:       texlive-collection-pstricks
Requires:       texlive-ctie
Requires:       texlive-cweb
Requires:       texlive-detex
Requires:       texlive-dtl
Requires:       texlive-dvi2tty
Requires:       texlive-dvicopy
Requires:       texlive-dvidvi
Requires:       texlive-dviljk
Requires:       texlive-eplain
Requires:       texlive-eulervm
Requires:       texlive-gentle
Requires:       texlive-lshort-english
Requires:       texlive-mltex
Requires:       texlive-multirow
Requires:       texlive-nomencl
Requires:       texlive-patgen
Requires:       texlive-pst-pdf
Requires:       texlive-rsfs
Requires:       texlive-seetexk
Requires:       texlive-siunits
Requires:       texlive-subfigure
Requires:       texlive-supertabular
Requires:       texlive-tamethebeast
Requires:       texlive-tds
Requires:       texlive-tie
Requires:       texlive-web
Requires:       texlive-xpdfopen

%description
teTeX scheme (more than medium, but nowhere near full) TeX Live scheme nearly
equivalent to the teTeX distribution that was maintained by Thomas Esser.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn74022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74022-1
- Update to TeX Live 2025