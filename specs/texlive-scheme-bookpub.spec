%global tl_version 2025

Name:           texlive-scheme-bookpub
Epoch:          12
Version:        svn63547
Release:        1%{?dist}
Summary:        book publishing scheme (core LaTeX and add-ons)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-barcodes
Requires:       biber
Requires:       texlive-biblatex
Requires:       texlive-bookcover
Requires:       texlive-caption
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-enumitem
Requires:       texlive-fontspec
Requires:       latexmk
Requires:       texlive-lipsum
Requires:       texlive-listings
Requires:       texlive-markdown
Requires:       texlive-memoir
Requires:       texlive-microtype
Requires:       texlive-minted
Requires:       texlive-novel
Requires:       texlive-octavo
Requires:       texlive-pdfpages
Requires:       texlive-pgf
Requires:       texlive-qrcode
Requires:       texlive-shapes
Requires:       texlive-titlesec
Requires:       texlive-tocloft
Requires:       texlive-tufte-latex
Requires:       texlive-willowtreebook

%description
book publishing scheme (core LaTeX and add-ons) This is a book publishing
scheme, containing core (Lua)LaTeX and selected additional packages likely to
be useful for non-technical book publication. It does not contain additional
fonts (different books need different fonts, and the packages are large), nor
does it contain additional mathematical or other technical packages.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn63547-1
- Update to TeX Live 2025