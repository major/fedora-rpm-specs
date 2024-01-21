%global pkgname crisp

Name:           gap-pkg-%{pkgname}
Version:        1.4.6
Release:        5%{?dist}
Summary:        Computing subgroups of finite soluble groups

License:        BSD-2-Clause
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            http://www.icm.tu-bs.de/~bhoeflin/crisp/
Source0:        %{url}%{pkgname}-%{version}.tar.bz2

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
# The content is BSD-2-Clause.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        BSD-2-Clause AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        CRISP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc

pushd doc
pdftex manual
makeindex -s manual.mst manual
pdftex manual
pdftex manual
popd

rm -fr htm
mkdir htm
perl %{gap_libdir}/etc/convert.pl -n CRISP -c -i -t doc htm

rm ../../doc

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g htm lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc README.txt
%license LICENSE.txt
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.4.6-2
- Update for split GAP directories

* Fri Dec 16 2022 Jerry James <loganjerry@gmail.com> - 1.4.6-1
- Version 1.4.6

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.4.5-8
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.4.5-8
- Update for gap 4.12.0

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
