%global gap_pkgname sophus
%global giturl      https://github.com/gap-packages/sophus

Name:           gap-pkg-%{gap_pkgname}
Version:        1.27
Release:        %autorelease
Summary:        Computing in nilpotent Lie algebras

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/sophus/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp

Requires:       gap-pkg-autpgrp

%description
The Sophus package is written to compute with nilpotent Lie algebras over
finite prime fields.  Using this package, you can compute the cover, the list
of immediate descendants, and the automorphism group of such Lie algebras.
You can also test if two such Lie algebras are isomorphic.

The immediate descendant function of the package can be used to classify
small-dimensional nilpotent Lie algebras over a given field.  For instance,
the package author obtained a classification of nilpotent Lie algebras with
dimension at most 9 over F_2; see
http://www.sztaki.hu/~schneider/Research/SmallLie.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Sophus documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README CHANGES.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
