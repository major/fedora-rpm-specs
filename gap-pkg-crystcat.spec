%global pkgname crystcat

Name:           gap-pkg-%{pkgname}
Version:        1.1.10
Release:        1%{?dist}
Summary:        Crystallographic groups catalog

License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap45/packages.php
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap45/CrystCat/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-cryst-doc
BuildRequires:  tth

Requires:       gap-pkg-cryst

%description
The GAP 4 package CrystCat provides a catalog of crystallographic groups
of dimensions 2, 3, and 4 which covers most of the data contained in the
book "Crystallographic groups of four-dimensional space" by H. Brown, R.
Bülow, J. Neubüser, H. Wondratschek, and H. Zassenhaus (John Wiley, New
York, 1978).  This catalog was previously available in the library of
GAP 3.  The present version for GAP 4 has been moved into a separate
package, because it requires the package Cryst, which is loaded
automatically by CrystCat.  The benefit of this is that space groups
extracted from the catalog now have the rich set of methods provided by
Cryst at their disposal, and are no longer dumb lists of generators.
Moreover, space groups are now fully supported in both the
representation acting from the left and the representation acting from
the right.

%package doc
Summary:        CrystCat documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-cryst-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
ln -s %{_gap_dir}/pkg/cryst ..
pushd doc
./make_doc
popd
rm -f ../../{doc,etc} ../cryst

# Compress large group files
gzip --best grp/crystcat.grp

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/make_doc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{Changelog,GPL,README}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" tst/testall.g

%files
%doc Changelog README
%license GPL
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}/htm/
%{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/htm/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.1.10-1
- Convert License tag to SPDX

* Fri Jul 29 2022 Jerry James <loganjerry@gmail.com> - 1.1.10-1
- Version 1.1.10

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.1.9-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.1.8-4
- Rebuild for gap 4.10.0
- Add -doc subpackage
- Add check script

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Jerry James <loganjerry@gmail.com> - 1.1.8-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.1.6-4
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.1.6-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Fri Jun 19 2015 Jerry James <loganjerry@gmail.com> - 1.1.6-1
- Initial RPM
