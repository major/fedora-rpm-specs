%global tl_version 2025

Name:           texlive-scheme-basic
Epoch:          12
Version:        svn54191
Release:        1%{?dist}
Summary:        basic scheme (plain and latex)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex

%description
basic scheme (plain and latex) This is the basic TeX Live scheme: it is a small
set of files sufficient to typeset plain TeX or LaTeX documents in PostScript
or PDF, using the Computer Modern fonts. This scheme corresponds to
collection-basic and collection-latex.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54191-1
- Update to TeX Live 2025