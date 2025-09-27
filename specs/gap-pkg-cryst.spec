# When bootstrapping a new architecture, there is no gap-pkg-crystcat yet.  That
# package is only needed for testing this one, but it needs this package to
# function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-crystcat
# 3. Build this package in non-bootstrap mode
%bcond bootstrap 0

%global gap_pkgname    cryst
%global gap_skip_check %{?with_bootstrap}

Name:           gap-pkg-%{gap_pkgname}
Version:        4.1.30
Release:        %autorelease
Summary:        GAP support for crystallographic groups

License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/cryst.git
Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/Cryst/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap grp htm tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-polenta
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  tth

# For testing only
%if %{without bootstrap}
BuildRequires:  gap-pkg-crystcat
%endif

Requires:       gap-pkg-caratinterface
Requires:       gap-pkg-polenta
Requires:       gap-pkg-polycyclic

Suggests:       xgap

%description
The GAP 4 package Cryst, previously known as CrystGAP, is the successor of the
CrystGAP package for GAP 3.  During the porting process to GAP 4, large parts
of the code have been rewritten, and the functionality has been extended
considerably.  Cryst provides a rich set of methods to compute with affine
crystallographic groups, in particular space groups.  In contrast to the GAP 3
version, affine crystallographic groups are now fully supported both in the
representation acting from the right and in the representation acting from the
left.  The latter representation is the one preferred by crystallographers.
There are also functions to determine representatives of all space group types
of a given dimension.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Cryst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%files
%doc Changelog README
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/grp/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
