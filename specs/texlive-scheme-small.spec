%global tl_version 2025

Name:           texlive-scheme-small
Epoch:          12
Version:        svn71080
Release:        1%{?dist}
Summary:        small scheme (basic + xetex, metapost, a few languages)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-babel-basque
Requires:       texlive-babel-czech
Requires:       texlive-babel-danish
Requires:       texlive-babel-dutch
Requires:       texlive-babel-english
Requires:       texlive-babel-finnish
Requires:       texlive-babel-french
Requires:       texlive-babel-german
Requires:       texlive-babel-hungarian
Requires:       texlive-babel-italian
Requires:       texlive-babel-norsk
Requires:       texlive-babel-polish
Requires:       texlive-babel-portuges
Requires:       texlive-babel-spanish
Requires:       texlive-babel-swedish
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-collection-latexrecommended
Requires:       texlive-collection-metapost
Requires:       texlive-collection-xetex
Requires:       texlive-ec
Requires:       texlive-epstopdf
Requires:       texlive-eurosym
Requires:       texlive-hyphen-basque
Requires:       texlive-hyphen-czech
Requires:       texlive-hyphen-danish
Requires:       texlive-hyphen-dutch
Requires:       texlive-hyphen-english
Requires:       texlive-hyphen-finnish
Requires:       texlive-hyphen-french
Requires:       texlive-hyphen-german
Requires:       texlive-hyphen-hungarian
Requires:       texlive-hyphen-italian
Requires:       texlive-hyphen-norwegian
Requires:       texlive-hyphen-polish
Requires:       texlive-hyphen-portuguese
Requires:       texlive-hyphen-spanish
Requires:       texlive-hyphen-swedish
Requires:       texlive-lm
Requires:       texlive-lualibs
Requires:       texlive-luaotfload
Requires:       texlive-luatexbase
Requires:       texlive-revtex
Requires:       texlive-synctex
Requires:       texlive-times
Requires:       texlive-tipa
Requires:       texlive-ulem
Requires:       texlive-upquote
Requires:       texlive-zapfding

%description
small scheme (basic + xetex, metapost, a few languages) This is a small TeX
Live scheme, corresponding to MacTeX's BasicTeX variant. It adds XeTeX,
MetaPost, various hyphenations, and some recommended packages to scheme-basic.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn71080-1
- Update to TeX Live 2025