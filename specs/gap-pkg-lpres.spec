%global pkgname lpres
%global giturl  https://github.com/gap-packages/lpres

Name:           gap-pkg-%{pkgname}
Version:        1.1.1
Release:        %autorelease
Summary:        Nilpotent quotients of L-presented groups

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/lpres/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ace-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-nq-doc
BuildRequires:  gap-pkg-polycyclic-doc

Requires:       gap-pkg-fga
Requires:       gap-pkg-polycyclic

Recommends:     gap-pkg-ace
Recommends:     gap-pkg-autpgrp
Recommends:     gap-pkg-nq

%description
The lpres package provides a first construction of finitely L-presented
groups and a nilpotent quotient algorithm for L-presented groups.  The
features of this package include:
- creating an L-presented group as a new gap object,
- computing nilpotent quotients of L-presented groups and epimorphisms
  from the L-presented group onto its nilpotent quotients,
- computing the abelian invariants of an L-presented group,
- computing finite-index subgroups and if possible their L-presentation,
- approximating the Schur multiplier of L-presented groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        LPRES documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-polycyclic-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
gap makedoc.g

# A second BiBTeX run is needed to resolve \cite within a reference
cd doc
bibtex lpres
pdflatex lpres
pdflatex lpres
mv lpres.pdf manual.pdf
cd -

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
