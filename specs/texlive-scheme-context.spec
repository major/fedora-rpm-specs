%global tl_version 2025

Name:           texlive-scheme-context
Epoch:          12
Version:        svn75426
Release:        2%{?dist}
Summary:        ConTeXt scheme

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-almfixed
Requires:       texlive-antt
Requires:       texlive-circuitikz
Requires:       texlive-cm-unicode
Requires:       texlive-collection-context
Requires:       texlive-collection-metapost
Requires:       texlive-concmath-otf
Requires:       texlive-context-animation
Requires:       texlive-context-calendar-examples
Requires:       texlive-context-collating-marks
Requires:       texlive-context-cyrillicnumbers
Requires:       texlive-context-filter
Requires:       texlive-context-gnuplot
Requires:       texlive-context-handlecsv
Requires:       texlive-context-letter
Requires:       texlive-context-mathsets
Requires:       texlive-context-pocketdiary
Requires:       texlive-context-simpleslides
Requires:       texlive-context-squares
Requires:       texlive-context-sudoku
Requires:       texlive-context-transliterator
Requires:       texlive-context-vim
Requires:       texlive-context-visualcounter
Requires:       texlive-dejavu
Requires:       texlive-ebgaramond
Requires:       texlive-erewhon
Requires:       texlive-erewhon-math
Requires:       texlive-euler-math
Requires:       texlive-fontawesome
Requires:       texlive-garamond-math
Requires:       texlive-gentium-sil
Requires:       texlive-iwona
Requires:       texlive-kpfonts-otf
Requires:       texlive-kurier
Requires:       texlive-libertinus-fonts
Requires:       texlive-lm
Requires:       texlive-lm-math
Requires:       texlive-lua-widow-control
Requires:       texlive-marvosym
Requires:       texlive-oldstandard
Requires:       texlive-pgf
Requires:       texlive-pgfplots
Requires:       texlive-plex
Requires:       texlive-poltawski
Requires:       texlive-tex-gyre
Requires:       texlive-tex-gyre-math
Requires:       texlive-xcharter
Requires:       texlive-xcharter-math
Requires:       texlive-xits

%description
ConTeXt scheme This is the TeX Live scheme for installing ConTeXt. It's
intended to give essentially the same results as the ConTeXt standalone
distribution. In addition to collection-context, includes fonts and other
packages commonly used with ConTeXt. TeX Live uses the ConTeXt repackaging as
distributed from https://github.com/gucci-on-fleek/context-packaging. See
https://contextgarden.net and https://pragma-ade.com for information about
ConTeXt.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn75426-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75426-1
- Update to TeX Live 2025