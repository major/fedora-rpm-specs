%global gap_pkgname liealgdb
%global giturl      https://github.com/gap-packages/liealgdb

Name:           gap-pkg-%{gap_pkgname}
Version:        2.3.0
Release:        %autorelease
Summary:        Database of Lie algebras

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/liealgdb/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
The package LieAlgDB provides access to several classifications of Lie
algebras.  In the mathematics literature many classifications of Lie algebras
of various types have been published (refer to the bibliography of the manual
for a few examples).  However, working with these classifications from paper
is not always easy.  This package aims at making a few classifications of
small dimensional Lie algebras that have appeared in recent years more
accessible.  For each classification that is contained in the package,
functions are provided that construct Lie algebras from that classification
inside GAP.  This allows the user to obtain easy access to the often rather
complicated data contained in a classification, and to directly interface the
Lie algebras to the functionality for Lie algebras which is already contained
in GAP.

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
Summary:        LieAlgDB documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES.md README
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
