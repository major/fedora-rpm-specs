%global gap_pkgname lpres
%global giturl      https://github.com/gap-packages/lpres

Name:           gap-pkg-%{gap_pkgname}
Version:        1.1.2
Release:        %autorelease
Summary:        Nilpotent quotients of L-presented groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/lpres/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(ace) >= 5.0
BuildRequires:  gap(autodoc)
BuildRequires:  gap(autpgrp) >= 1.4
BuildRequires:  gap(fga) >= 1.1.0.1
BuildRequires:  gap(polycyclic) >= 2.5
BuildRequires:  gap-devel >= 4.9
BuildRequires:  gap-pkg-nq-doc
BuildRequires:  gap-pkg-polycyclic-doc >= 2.5

Requires:       gap(fga) >= 1.1.0.1
Requires:       gap(polycyclic) >= 2.5
Requires:       gap-core >= 4.9

Recommends:     gap(ace) >= 5.0
Recommends:     gap(autpgrp) >= 1.4
Recommends:     gap(nq)

Provides:       gap(lpres) = %{version}-%{release}

%description
The lpres package provides a first construction of finitely L-presented groups
and a nilpotent quotient algorithm for L-presented groups.  The features of
this package include:
- creating an L-presented group as a new gap object,
- computing nilpotent quotients of L-presented groups and epimorphisms from
  the L-presented group onto its nilpotent quotients,
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
Requires:       gap-online-help
Requires:       gap-pkg-polycyclic-doc >= 2.5

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
