%global pkgname crisp

Name:           gap-pkg-%{pkgname}
Version:        1.4.5
Release:        7%{?dist}
Summary:        Computing subgroups of finite soluble groups

License:        BSD-2-Clause
URL:            http://www.icm.tu-bs.de/~bhoeflin/crisp/
Source0:        http://www.icm.tu-bs.de/~bhoeflin/crisp/%{pkgname}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  tth

Requires:       gap-core

%description
CRISP (Computing with Radicals, Injectors, Schunck classes and
Projectors) provides algorithms for computing subgroups of finite
soluble groups related to group classes.  In particular, it allows
computing F-radicals and F-injectors for Fitting classes (and Fitting
sets) F, F-residuals for formations F, and X-projectors for Schunck
classes X.  In order to carry out these computations, the group classes
F and X must be given by an algorithm which decides membership in the
group class.

Moreover, CRISP contains algorithms for the computation of normal
subgroups invariant under a prescribed set of automorphisms and
belonging to a given group class.  This includes an improved method to
compute the set of all normal subgroups of a finite soluble group, its
characteristic subgroups, and the socle and p-socles for given primes p.

%package doc
Summary:        CRISP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc

pushd doc
pdftex manual
makeindex -s manual.mst manual
pdftex manual
pdftex manual
popd

rm -fr htm
mkdir htm
perl %{_gap_dir}/etc/convert.pl -n CRISP -c -i -t doc htm

rm ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.4.5-7
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 1.4.5-1
- Version 1.4.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.4.4-8
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Jerry James <loganjerry@gmail.com> - 1.4.4-2
- Correct the license field

* Wed May  4 2016 Jerry James <loganjerry@gmail.com> - 1.4.4-1
- Initial RPM
