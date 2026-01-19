%global tl_version 2025

Name:           texlive-scheme-full
Epoch:          12
Version:        svn54074
Release:        2%{?dist}
Summary:        full scheme (everything)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-bibtexextra
Requires:       texlive-collection-binextra
Requires:       texlive-collection-context
Requires:       texlive-collection-fontsextra
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-collection-formatsextra
Requires:       texlive-collection-fontutils
Requires:       texlive-collection-games
Requires:       texlive-collection-humanities
Requires:       texlive-collection-langarabic
Requires:       texlive-collection-langchinese
Requires:       texlive-collection-langcjk
Requires:       texlive-collection-langcyrillic
Requires:       texlive-collection-langczechslovak
Requires:       texlive-collection-langenglish
Requires:       texlive-collection-langeuropean
Requires:       texlive-collection-langfrench
Requires:       texlive-collection-langgerman
Requires:       texlive-collection-langgreek
Requires:       texlive-collection-langitalian
Requires:       texlive-collection-langjapanese
Requires:       texlive-collection-langkorean
Requires:       texlive-collection-langother
Requires:       texlive-collection-langpolish
Requires:       texlive-collection-langportuguese
Requires:       texlive-collection-langspanish
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexextra
Requires:       texlive-collection-latexrecommended
Requires:       texlive-collection-luatex
Requires:       texlive-collection-mathscience
Requires:       texlive-collection-metapost
Requires:       texlive-collection-music
Requires:       texlive-collection-pictures
Requires:       texlive-collection-plaingeneric
Requires:       texlive-collection-pstricks
Requires:       texlive-collection-publishers
Requires:       texlive-collection-texworks
Requires:       texlive-collection-xetex

%description
full scheme (everything) This is the full TeX Live scheme: it installs
everything available.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn54074-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54074-1
- Update to TeX Live 2025