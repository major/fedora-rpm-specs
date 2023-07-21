%global pkgname polenta

Name:           gap-pkg-%{pkgname}
Version:        1.3.10
Release:        6%{?dist}
Summary:        Polycyclic presentations for matrix groups

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/polenta/
Source0:        https://github.com/gap-packages/polenta/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-alnuth-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-radiroot

Requires:       gap-pkg-alnuth
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-radiroot

Recommends:     gap-pkg-aclib

%description
The Polenta package provides methods to compute polycyclic presentations
of matrix groups (finite or infinite).  As a by-product, this package
gives some functionality to compute certain module series for modules of
solvable groups.  For example, if G is a rational polycyclic matrix
group, then we can compute the radical series of the natural Q[G]-module
Q^d.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polenta documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-alnuth-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g exam lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# POLENTA.tst and POLENTA2.tst require more memory than some koji builders have
# available, so we disable them.  The maintainer should run them on a machine
# with a minimum of 16 GB of RAM prior to updating to a new version.
sed -i 's/"POLENTA\.tst"/#&/;/POLENTA2/s/Add/;#&/' tst/testall.g

gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES README.md TODO
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.3.10-4
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.3.10-3
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.3.10-3
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 29 2022 Jerry James <loganjerry@gmail.com> - 1.3.10-1
- Version 1.3.10

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 1.3.9-2
- Fix -doc subpackage dependency on alnuth

* Sat Oct  5 2019 Jerry James <loganjerry@gmail.com> - 1.3.9-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.3.8-5
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  8 2018 Jerry James <loganjerry@gmail.com> - 1.3.8-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec  9 2016 Jerry James <loganjerry@gmail.com> - 1.3.7-1
- New upstream version (bz 1403107)

* Fri May  6 2016 Jerry James <loganjerry@gmail.com> - 1.3.6-1
- Initial RPM
