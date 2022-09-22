%global pkgname aclib

Name:           gap-pkg-%{pkgname}
Version:        1.3.2
Release:        6%{?dist}
Summary:        Almost Crystallographic groups library for GAP

License:        Artistic-2.0
URL:            https://gap-packages.github.io/aclib/
Source0:        https://github.com/gap-packages/aclib/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  tth

Requires:       gap-core
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
Summary:        AClib documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix end-of-line encoding
sed -i.orig 's/\r//' doc/algos.tex
touch -r doc/algos.tex.orig doc/algos.tex
rm -f doc/algos.tex.orig

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
cd doc
./make_doc %{_gap_dir}
cd -
rm -f ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/make_doc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{.release,LICENSE,README}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" tst/testall.g

%files
%doc README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}/htm/
%{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/htm/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.3.2-6
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Version 1.3.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.3.1-3
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Jerry James <loganjerry@gmail.com> - 1.3-1
- New upstream version
- New URLs
- Add check script

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.2-5
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.2-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Mon Jul 20 2015 Jerry James <loganjerry@gmail.com> - 1.2-2
- Do not package version control files
- Fix end-of-line encodings

* Fri Jun 19 2015 Jerry James <loganjerry@gmail.com> - 1.2-1
- Initial RPM
