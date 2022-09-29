%global pkgname polycyclic

# When bootstrapping a new architecture, the alnuth package is not yet
# available.  Therefore:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-alnuth in bootstrap mode.
# 3. Build gap-pkg-radiroot
# 4. Build gap-pkg-alnuth in non-bootstrap mode.
# 5. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        2.16
Release:        7%{?dist}
Summary:        Algorithms on polycylic groups for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/polycyclic/
Source0:        https://github.com/gap-packages/polycyclic/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

## Post-release bug fixes from upstream

# Update AbelianPcpGroup, support infinity
# https://github.com/gap-packages/polycyclic/commit/37af5a8832b9f0872f058fd66572d423e270a2f7
Patch0:         %{name}-abelianpcpgroup-infinity.patch
# Support infinity in AbelianPcpGroup and AbelianGroupCons
# https://github.com/gap-packages/polycyclic/commit/929755ef354319268a7cd8cf574fad92543f38f6
Patch1:         %{name}-infinity.patch
# Fix a bug in ConjugacyElementsBySeries
# https://github.com/gap-packages/polycyclic/commit/e9312334e0be52f6aebb04d76feff4ac06a0b766
Patch2:         %{name}-conjugacyelementsbyseries.patch
# Fix Random not working for the trivial group
# https://github.com/gap-packages/polycyclic/commit/f3bdcbd90f729cf9e231614ae37bfcfe49abfca6
Patch3:         %{name}-random-trivial.patch
# Fix IsNormal, uprank FittingSubgroup method
# https://github.com/gap-packages/polycyclic/commit/3f385e49fca33917bfcf5f6d61828bdd97c4468a
Patch4:         %{name}-isnormal.patch
# Replace INV by its official name InverseMutable
# https://github.com/gap-packages/polycyclic/commit/237ed84786fd8477805241ec55e0955847717cae
Patch5:         %{name}-inverse-mutable.patch
# Fix a cohomology example
# https://github.com/gap-packages/polycyclic/commit/2d4c8d475f51075f2692e29f2b50e008d30f67eb
Patch6:         %{name}-cohom-example.patch
# Remove a duplicate SubsWord definition
# https://github.com/gap-packages/polycyclic/commit/7455d890b97b77cdede6d34d4edbf0a2a9ed2a6b
Patch7:         %{name}-subsword-dup.patch
# Fix a bug in IsSingleValued
# https://github.com/gap-packages/polycyclic/commit/02ebcc4f22d165e4f823a912e7cb2ed703d9416a
Patch8:         %{name}-issinglevalued.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
%if %{without bootstrap}
BuildRequires:  gap-pkg-alnuth
%endif
BuildRequires:  gap-pkg-autpgrp

%if %{without bootstrap}
Requires:       gap-pkg-alnuth
%endif
Requires:       gap-pkg-autpgrp

%description
This package provides algorithms for working with polycyclic groups.
The features of this package include:
- creating a polycyclic group from a polycyclic presentation
- arithmetic in a polycyclic group
- computation with subgroups and factor groups of a polycyclic group
- computation of standard subgroup series such as the derived series,
  the lower central series
- computation of the first and second cohomology
- computation of group extensions
- computation of normalizers and centralizers
- solutions to the conjugacy problems for elements and subgroups
- computation of Torsion and various finite subgroups
- computation of various subgroups of finite index
- computation of the Schur multiplicator, the non-abelian exterior
  square and the non-abelian tensor square

%package doc
Summary:        Polycyclic groups documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p0

# Fix character encodings
for fil in gap/basic/colcom.gi; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g gap tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g
%endif

%files
%doc CHANGES.md README.md
%license LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.16-7
- Update for gap 4.12.0
- Add post-release bug fix patches from upstream
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Jerry James <loganjerry@gmail.com> - 2.16-1
- Version 2.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Jerry James <loganjerry@gmail.com> - 2.15.1-1
- New upstream version

* Fri Sep 27 2019 Jerry James <loganjerry@gmail.com> - 2.15-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 2.14-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Jerry James <loganjerry@gmail.com> - 2.14-1
- New upstream version

* Tue Mar 20 2018 Jerry James <loganjerry@gmail.com> - 2.12-1
- New upstream version
- New URLs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 2.11-6
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 2.11-4
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  1 2015 Jerry James <loganjerry@gmail.com> - 2.11-2
- Rebuild with alnuth support

* Wed Mar 25 2015 Jerry James <loganjerry@gmail.com> - 2.11-1
- Initial RPM
