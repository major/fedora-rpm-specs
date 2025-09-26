%global gap_pkgname primgrp
%global giturl      https://github.com/gap-packages/primgrp

Name:           gap-pkg-%{gap_pkgname}
Version:        4.0.1
Release:        %autorelease
Summary:        Primitive permutation groups library

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/primgrp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --bare
BuildOption(install): data lib tst
BuildOption(check): --bare tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
The PrimGrp package provides the library of primitive permutation groups which
includes, up to permutation isomorphism (i.e., up to conjugacy in the
corresponding symmetric group), all primitive permutation groups of degree
less than 4096.  Groups of degree 4096 to 8191 must be downloaded separately
from https://doi.org/10.5281/zenodo.10411366 and then installed by following
the instructions given there.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Primitive permutation groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/data/
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
