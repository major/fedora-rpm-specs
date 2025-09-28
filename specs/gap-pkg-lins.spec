%global gap_pkgname lins
%global gap_upname  LINS
%global giturl      https://github.com/gap-packages/LINS

Name:           gap-pkg-%{gap_pkgname}
Version:        0.9
Release:        %autorelease
Summary:        Compute the normal subgroups of a finitely presented group

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/LINS/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testquick.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-cohomolo
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-polycyclic-doc
BuildRequires:  gap-pkg-recog

Requires:       gap-core

%description
This package provides an algorithm for computing the normal subgroups of a
finitely presented group up to some given index bound.

This algorithm is based on work of Derek Holt and David Firth.  Derek Holt and
David Firth implemented this algorithm in the algebra software MAGMA.

The current implementation in GAP uses a table of groups that was computed by
the code in `createTables.gi`.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only AND OFL-1.1-RFN
Summary:        Documentation for the GAP LINS package
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-polycyclic-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
%license COPYRIGHT LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
