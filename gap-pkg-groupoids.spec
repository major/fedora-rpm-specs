%global pkgname groupoids

Name:           gap-pkg-%{pkgname}
Version:        1.71
Release:        1%{?dist}
Summary:        Groupoids, group graphs, and groupoid graphs

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/groupoids/
Source0:        https://github.com/gap-packages/groupoids/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-semigroups
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-fga
Requires:       gap-pkg-utils

Recommends:     gap-pkg-semigroups

%description
The Groupoids package provides functions for computation with finite
groupoids and their morphisms.

The first part is concerned with the standard constructions for
connected groupoids, and for groupoids with more than one component.
Groupoid morphisms are also implemented, and recent work includes the
implementation of automorphisms of a finite, connected groupoid: by
permutation of the objects; by automorphism of the root group; and by
choice of rays to each object.  The automorphism group of such a
groupoid is also computed, together with an isomorphism of a quotient of
permutation groups.

The second part implements graphs of groups and graphs of groupoids.  A
graph of groups is a directed graph with a group at each vertex and with
isomorphisms between subgroups on each arc.  This construction enables
normal form computations for free products with amalgamation, and for
HNN extensions, when the vertex groups come with their own rewriting
systems.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Groupoids documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
# Skip tests that tend to get OOM killed
SKIP="manual/gpd.tst extra/rt-act.tst"
for test in $SKIP; do
  rm %{buildroot}%{gap_dir}/pkg/%{pkgname}/tst/$test
done
gap -l "%{buildroot}%{gap_dir};%{gap_dir}" tst/testall.g
for test in $SKIP; do
  cp -p tst/$test %{buildroot}%{gap_dir}/pkg/%{pkgname}/tst/$test
done

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.71-1
- Clarify license of the doc subpackage

* Tue Sep 13 2022 Jerry James <loganjerry@gmail.com> - 1.71-1
- Version 1.71
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.69-3
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Jerry James <loganjerry@gmail.com> - 1.69-1
- Version 1.69

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep  5 2019 Jerry James <loganjerry@gmail.com> - 1.68-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.67-1
- New upstream version

* Tue Apr 16 2019 Jerry James <loganjerry@gmail.com> - 1.65-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.63-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 1.55-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jerry James <loganjerry@gmail.com> - 1.54-1
- Name change from gap-pkg-gpd to gap-pkg-groupoids
