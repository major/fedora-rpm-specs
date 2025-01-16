%global pkgname irredsol
%global giturl  https://github.com/bh11/irredsol

Name:           gap-pkg-%{pkgname}
Version:        1.4.4
Release:        %autorelease
Summary:        Irreducible soluble linear groups over finite fields

License:        BSD-2-Clause
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            http://www.icm.tu-bs.de/~bhoeflin/irredsol/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/IRREDSOL-%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-crisp-doc
BuildRequires:  gap-pkg-primgrp-doc
BuildRequires:  perl-interpreter
BuildRequires:  tth

Requires:       gap-core

Recommends:     gap-pkg-crisp

%description
IRREDSOL is a GAP package which provides a library of all irreducible
soluble subgroups of GL(n, q), up to conjugacy, where n is a positive
integer and q a prime power satisfying q^n <= 2000000, and a library
of all primitive soluble groups of degree at most 2000000.

%package doc
# The content is BSD-2-Clause.  The remaining licenses cover the various fonts
# embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        BSD-2-Clause AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        IRREDSOL documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-crisp-doc
Requires:       gap-pkg-primgrp-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation and CRISP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg ../../pkg
ln -s %{gap_libdir}/pkg/crisp ..
ln -s %{gap_libdir}/pkg/primgrp ..
pushd doc
pdftex manual
makeindex manual
pdftex manual
pdftex manual
rm -f ../htm/*
perl %{gap_libdir}/etc/convert.pl -t -c -n IRREDSOL . ../htm
popd
rm -f ../../{doc,etc,pkg} ../crisp

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g data fp htm lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.txt
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/data/
%{gap_libdir}/pkg/%{pkgname}/fp/
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
