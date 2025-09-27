%global gap_pkgname numericalsgps
%global gap_upname  NumericalSgps
%global giturl      https://github.com/gap-packages/numericalsgps

Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.0
Release:        %autorelease
Summary:        Compute with numerical semigroups and affine semigroups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/numericalsgps/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data gap tst version
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-normalizinterface
BuildRequires:  gap-pkg-singular

Requires:       gap-core

Recommends:     gap-pkg-normalizinterface
Recommends:     gap-pkg-singular

%description
NumericalSgps is a GAP package for computing with Numerical Semigroups.
Features include:

- defining numerical semigroups;
- computing several properties of numerical semigroups, namely: multiplicity,
  Frobenius number, (minimal) system of generators, Apéry set, gaps,
  fundamental gaps, etc.;
- perform several operations on numerical semigroups and ideals, namely:
  intersection, quotient by an integer, decompose into irreducible semigroups,
  add a special gap, ...;
- computing and testing membership to relevant families of numerical
  semigroups.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Documentation for the GAP NumericalSgps package
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES EXAMPLES README.md
%license GPL LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/data/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/
%{gap_libdir}/pkg/%{gap_upname}/version

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
