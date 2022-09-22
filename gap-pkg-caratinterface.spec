%global pkgname caratinterface
%global upname  CaratInterface

Name:           gap-pkg-%{pkgname}
Version:        2.3.4
Release:        1%{?dist}
Summary:        GAP interface to CARAT

License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap/%{upname}/%{upname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  carat
BuildRequires:  gap-devel
BuildRequires:  tth

Requires:       carat
Requires:       gap-core

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
Summary:        CARAT documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
BuildArch:      noarch

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{upname}

# Don't use the bundled version of CARAT
rm -f carat*.tgz

%build
# Look for the CARAT binaries where they exist in Fedora
for f in read.g PackageInfo.g; do
  sed -i.orig 's,DirectoriesPackagePrograms( "%{upname}" ),Directory( "%{_libexecdir}/carat" ),' $f
  touch -r ${f}.orig $f
  rm -f ${f}.orig
done

# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{upname} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{upname}/{Changelog,configure,GPL,INSTALL,Makefile,README,src}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}/doc/make_doc
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc Changelog README
%license GPL
%{_gap_dir}/pkg/%{upname}/
%exclude %{_gap_dir}/pkg/%{upname}/doc/
%exclude %{_gap_dir}/pkg/%{upname}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}/doc/
%docdir %{_gap_dir}/pkg/%{upname}/htm/
%{_gap_dir}/pkg/%{upname}/doc/
%{_gap_dir}/pkg/%{upname}/htm/

%changelog
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
