%global pkgname aclib
%global giturl  https://github.com/gap-packages/aclib

Name:           gap-pkg-%{pkgname}
Version:        1.3.2
Release:        %autorelease
Summary:        Almost Crystallographic groups library for GAP

License:        Artistic-2.0
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/aclib/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  tth

Requires:       gap-pkg-polycyclic

Recommends:     gap-pkg-crystcat

%description
The AClib package contains a library of almost crystallographic groups
and some algorithms to compute with these groups.  A group is called
almost crystallographic if it is finitely generated nilpotent-by-finite
and has no nontrivial finite normal subgroups.  Further, an almost
crystallographic group is called almost Bieberbach if it is
torsion-free.  The almost crystallographic groups of Hirsch length 3 and
a part of the almost crystallographic groups of Hirsch length 4 have
been classified by Dekimpe.  This classification includes all almost
Bieberbach groups of Hirsch lengths 3 or 4.  The AClib package gives
access to this classification; that is, the package contains this
library of groups in a computationally useful form.  The groups in this
library are available in two different representations.  First, each of
the groups of Hirsch length 3 or 4 has a rational matrix representation
of dimension 4 or 5, respectively, and such representations are
available in this package.  Secondly, all the groups in this library
are (infinite) polycyclic groups and the package also incorporates
polycyclic presentations for them.  The polycyclic presentations can be
used to compute with the given groups using the methods of the
Polycyclic package.

%package doc
# The content is Artistic-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        Artistic-2.0 AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        AClib documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
# Fix end-of-line encoding
sed -i.orig 's/\r//' doc/algos.tex
touch -r doc/algos.tex.orig doc/algos.tex
rm -f doc/algos.tex.orig

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc %{gap_libdir}
cd -
rm -f ../../doc

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap
%{gap_libdir}/pkg/%{pkgname}/tst

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
