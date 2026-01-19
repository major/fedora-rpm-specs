%global tl_version 2025

Name:           texlive-scheme-minimal
Epoch:          12
Version:        svn54191
Release:        2%{?dist}
Summary:        minimal scheme (plain only)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic

%description
minimal scheme (plain only) This is the minimal TeX Live scheme, with support
for only plain TeX. (No LaTeX macros.) LuaTeX is included because Lua scripts
are used in TeX Live infrastructure. This scheme corresponds exactly to
collection-basic.



%build
# Nothing to build

%install
# Nothing to install

# Main scheme metapackage (empty)
%files


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn54191-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 15 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn54191-1
- Update to TeX Live 2025