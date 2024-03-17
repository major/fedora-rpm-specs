%global pkgname automata

Name:           gap-pkg-%{pkgname}
Version:        1.15
Release:        %autorelease
Summary:        Finite automata algorithms

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/automata/
VCS:            https://github.com/gap-packages/automata
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

# Splash invokes tools from these packages
Recommends:     coreutils
Recommends:     graphviz
Recommends:     xdg-utils

%description
This package contains algorithms for working with finite automata in
GAP.  It can do the following:
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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap tst version %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES EXAMPLES README.md
%license GPL LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
