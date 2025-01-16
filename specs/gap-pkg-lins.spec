%global pkgname lins
%global upname  LINS
%global giturl  https://github.com/gap-packages/LINS

Name:           gap-pkg-%{pkgname}
Version:        0.9
Release:        %autorelease
Summary:        Compute the normal subgroups of a finitely presented group

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/LINS/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-cohomolo
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-polycyclic-doc
BuildRequires:  gap-pkg-recog

Requires:       gap-core

%description
This package provides an algorithm for computing the normal subgroups of
a finitely presented group up to some given index bound.

This algorithm is based on work of Derek Holt and David Firth.  Derek
Holt and David Firth implemented this algorithm in the algebra software
MAGMA.

The current implementation in GAP uses a table of groups that was
computed by the code in `createTables.gi`.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a gap tst *.g  %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testquick.g

%files
%doc README.md
%license COPYRIGHT LICENSE
%dir %{gap_libdir}/pkg/%{upname}/
%{gap_libdir}/pkg/%{upname}/*.g
%{gap_libdir}/pkg/%{upname}/gap/
%{gap_libdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
