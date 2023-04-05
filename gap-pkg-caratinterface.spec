%global pkgname caratinterface
%global upname  CaratInterface

Name:           gap-pkg-%{pkgname}
Version:        2.3.5
Release:        1%{?dist}
Summary:        GAP interface to CARAT

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap/%{upname}/%{upname}-%{version}.tar.gz

BuildRequires:  carat
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io
BuildRequires:  tth

Requires:       carat
Requires:       gap-pkg-io

Suggests:       gap-pkg-cryst

%description
This package provides GAP interface routines to some of the standalone
programs of the package CARAT, developed by J. Opgenorth, W. Plesken,
and T. Schulz at Lehrstuhl B für Mathematik, RWTH Aachen.  CARAT is a
package for computation with crystallographic groups.

CARAT is to a large extent complementary to the GAP 4 package Cryst.  In
particular, it provides routines for the computation of normalizers and
conjugators of finite unimodular groups in GL(n,Z), and routines for the
computation of Bravais groups, which are all missing in Cryst.
Furthermore, it provides a catalog of Bravais groups up to dimension 6.
Cryst automatically loads Carat when it is available, and makes use of
its functions where necessary.  The Carat package thereby extends the
functionality of the package Cryst considerably.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}

# Don't use the bundled version of CARAT
rm -f carat*.tgz

%build
export LC_ALL=C.UTF-8

# Look for the CARAT binaries where they exist in Fedora
for f in read.g PackageInfo.g; do
  sed -i.orig 's,DirectoriesPackagePrograms( "%{upname}" ),Directory( "%{_libexecdir}/carat" ),' $f
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

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g gap htm tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc Changelog README
%license GPL
%{gap_libdir}/pkg/%{upname}/
%exclude %{gap_libdir}/pkg/%{upname}/doc/
%exclude %{gap_libdir}/pkg/%{upname}/htm/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%docdir %{gap_libdir}/pkg/%{upname}/htm/
%{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/htm/

%changelog
* Mon Apr  3 2023 Jerry James <loganjerry@gmail.com> - 2.3.5-1
- Version 2.3.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.3.4-3
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.3.4-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.3.4-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.3.4-1
- Convert License tag to SPDX

* Fri Jul 29 2022 Jerry James <loganjerry@gmail.com> - 2.3.4-1
- Version 2.3.4

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 2.3.3-8
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Jerry James <loganjerry@gmail.com> - 2.3.3-1
- Initial RPM, rename from gap-pkg-carat
