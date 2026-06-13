%global gap_pkgname typeset
%global giturl      https://github.com/gap-packages/typeset

Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.4
Release:        %autorelease
Summary:        Automatic typesetting framework for common GAP objects

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/typeset/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): demo gap tst
BuildOption(check): tst/testall.g

BuildRequires:  dot2tex
BuildRequires:  gap(autodoc)
BuildRequires:  gap(ctbllib)
BuildRequires:  gap(digraphs) >= 1.5.0
BuildRequires:  gap-devel >= 4.11
BuildRequires:  gap-pkg-digraphs-doc >= 1.5.0
BuildRequires:  graphviz
BuildRequires:  tex(preview.sty)
BuildRequires:  tex(standalone.sty)
BuildRequires:  tex(tikz.sty)

Requires:       GAPDoc-latex
Requires:       dot2tex
Requires:       gap-core >= 4.11
Requires:       graphviz
Requires:       tex(preview.sty)
Requires:       tex(standalone.sty)
Requires:       tex(tikz.sty)

Recommends:     gap(digraphs) >= 1.5.0

Provides:       gap(typeset) = %{version}-%{release}

%description
This package implements a framework for automatic typesetting of common GAP
objects, for the purpose of embedding them nicely into research papers.
Currently, an example implementation has been written specifically for LaTeX.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP typeset package
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-digraphs-doc >= 1.5.0

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/demo/
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/demo/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
