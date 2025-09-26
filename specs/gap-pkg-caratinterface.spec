%global gap_pkgname caratinterface
%global gap_upname  CaratInterface

Name:           gap-pkg-%{gap_pkgname}
Version:        2.3.7
Release:        %autorelease
Summary:        GAP interface to CARAT

License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/CaratInterface.git
Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/%{gap_upname}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap htm tst
BuildOption(check): tst/testall.g

BuildRequires:  carat
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io
BuildRequires:  tth

Requires:       carat
Requires:       gap-pkg-io

Suggests:       gap-pkg-cryst

%description
This package provides GAP interface routines to some of the standalone
programs of the package CARAT, developed by J. Opgenorth, W. Plesken, and T.
Schulz at Lehrstuhl B für Mathematik, RWTH Aachen.  CARAT is a package for
computation with crystallographic groups.

CARAT is to a large extent complementary to the GAP 4 package Cryst.  In
particular, it provides routines for the computation of normalizers and
conjugators of finite unimodular groups in GL(n,Z), and routines for the
computation of Bravais groups, which are all missing in Cryst.  Furthermore,
it provides a catalog of Bravais groups up to dimension 6.  Cryst
automatically loads Carat when it is available, and makes use of its functions
where necessary.  The Carat package thereby extends the functionality of the
package Cryst considerably.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        CARAT documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}

%build
# Don't use the bundled version of CARAT
rm -f carat*.tgz

# Look for the CARAT binaries where they exist in Fedora
for f in read.g PackageInfo.g; do
  sed -i.orig 's,DirectoriesPackagePrograms( "%{gap_upname}" ),Directory( "%{_libexecdir}/carat" ),' $f
  touch -r ${f}.orig $f
  rm -f ${f}.orig
done

# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%files
%doc Changelog README
%license GPL
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
