%global pkgname polycyclic
%global giturl  https://github.com/gap-packages/polycyclic

# When bootstrapping a new architecture, the alnuth package is not yet
# available.  Therefore:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-alnuth in bootstrap mode.
# 3. Build gap-pkg-radiroot
# 4. Build gap-pkg-alnuth in non-bootstrap mode.
# 5. Build this package in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        2.16
Release:        %autorelease
Summary:        Algorithms on polycylic groups for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/polycyclic/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
%if %{without bootstrap}
BuildRequires:  gap-pkg-alnuth
%endif
BuildRequires:  gap-pkg-autpgrp

%if %{without bootstrap}
Requires:       gap-pkg-alnuth
%endif
Requires:       gap-pkg-autpgrp

%description
This package provides algorithms for working with polycyclic groups.
The features of this package include:
- creating a polycyclic group from a polycyclic presentation
- arithmetic in a polycyclic group
- computation with subgroups and factor groups of a polycyclic group
- computation of standard subgroup series such as the derived series,
  the lower central series
- computation of the first and second cohomology
- computation of group extensions
- computation of normalizers and centralizers
- solutions to the conjugacy problems for elements and subgroups
- computation of Torsion and various finite subgroups
- computation of various subgroups of finite index
- computation of the Schur multiplicator, the non-abelian exterior
  square and the non-abelian tensor square

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polycyclic groups documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p0

%conf
# Fix character encodings
for fil in gap/basic/colcom.gi; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

# Tests disabled until upstream can fix a test hang:
# https://github.com/gap-packages/polycyclic/issues/46
#%%if %%{without bootstrap}
#%%check
#gap -l '%%{buildroot}%%{gap_libdir};' tst/testall.g
#%%endif

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
