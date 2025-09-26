%global gap_pkgname automata
%global giturl      https://github.com/gap-packages/automata

Name:           gap-pkg-%{gap_pkgname}
Version:        1.16
Release:        %autorelease
Summary:        Finite automata algorithms

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/automata/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst version
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

# Splash invokes tools from these packages
Recommends:     coreutils
Recommends:     graphviz
Recommends:     xdg-utils

%description
This package contains algorithms for working with finite automata in GAP.  It
can do the following:
- compute a rational expression for the language recognized by a finite
  automaton;
- compute an automaton for the language given by a rational expression;
- minimalize a finite automaton;
- visualize automata.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Finite automata documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES EXAMPLES README.md
%license GPL LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/
%{gap_libdir}/pkg/%{gap_upname}/version

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
