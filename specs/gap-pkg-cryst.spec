%global pkgname cryst

# When bootstrapping a new architecture, there is no gap-pkg-crystcat yet.  That
# package is only needed for testing this one, but it needs this package to
# function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-crystcat
# 3. Build this package in non-bootstrap mode
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        4.1.27
Release:        %autorelease
Summary:        GAP support for crystallographic groups

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/cryst.git
Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/Cryst/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  tth

# For testing only
%if %{without bootstrap}
BuildRequires:  gap-pkg-crystcat
%endif

Requires:       gap-pkg-caratinterface
Requires:       gap-pkg-polycyclic

Suggests:       gap-pkg-crystcat
Suggests:       xgap

%description
The GAP 4 package Cryst, previously known as CrystGAP, is the successor
of the CrystGAP package for GAP 3.  During the porting process to GAP 4,
large parts of the code have been rewritten, and the functionality has
been extended considerably.  Cryst provides a rich set of methods to
compute with affine crystallographic groups, in particular space groups.
In contrast to the GAP 3 version, affine crystallographic groups are now
fully supported both in the representation acting from the right and in
the representation acting from the left.  The latter representation is
the one preferred by crystallographers.  There are also functions to
determine representatives of all space group types of a given dimension.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap grp htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g
%endif

%files
%doc Changelog README
%license COPYING
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/grp/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
