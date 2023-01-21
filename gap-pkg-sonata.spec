%global pkgname sonata

Name:           gap-pkg-%{pkgname}
Version:        2.9.6
Release:        3%{?dist}
Summary:        GAP package for systems of nearrings

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/sonata/
Source0:        https://github.com/gap-packages/sonata/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  parallel
BuildRequires:  tth

Requires:       gap-core

Suggests:       xgap

%description
SONATA stands for "systems of nearrings and their applications".  It
provides methods for the construction and the analysis of finite
nearrings.  A left nearring is an algebra (N;+,*), where (N,+) is a (not
necessarily abelian) group, (N,*) is a semigroup, and x*(y+z) = x*y + x*z
holds for all x,y,z in N.

As a typical example of a nearring, we may consider the set of all
mappings from a group G into G, where the addition is the pointwise
addition of mappings in G, and the multiplication is composition of
functions.  If functions are written on the right of their arguments,
then the left distributive law holds, while the right distributive law
is not satisfied for non-trivial G.

The SONATA package provides methods for the construction and analysis of
finite nearrings.
1. Methods for constructing all endomorphisms and all fixed-point-free
   automorphisms of a given group.
2. Methods for constructing the following nearrings of functions on a
   group G:
   - the nearring of polynomial functions of G (in the sense of
     Lausch-Nöbauer);
   - the nearring of compatible functions of G;
   - distributively generated nearrings such as I(G), A(G), E(G);
   - centralizer nearrings.
3. A library of all small nearrings (up to order 15) and all small
   nearrings with identity (up to order 31).
4. Functions to obtain solvable fixed-point-free automorphism groups on
   abelian groups, nearfields, planar nearrings, as well as designs from
   those.
5. Various functions to study the structure (size, ideals, N-groups, ...)
   of nearrings, to determine properties of nearring elements, and to
   decide whether two nearrings are isomorphic.
6. If the package XGAP is installed, the lattices of one- and two-sided
   ideals of a nearring can be studied interactively using a graphical
   representation.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        SONATA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Use the main gap package's macro file
rm -f doc/gapmacro.tex
ln -s %{gap_libdir}/doc/gapmacro.tex doc/gapmacro.tex

# Fix the documentation build script
sed -e 's,\.\./\.\./\.\./\.\./etc/convert\.pl,%{gap_libdir}/etc/convert.pl,' \
    -e 's,\.\./\.\./\.\./\.\./doc/manualindex,%{gap_libdir}/doc/manualindex,' \
    -i doc/make_doc

%build
# Build the documentation
export LC_ALL=C.UTF-8
pushd doc
./make_doc
popd

# Compress large data files
parallel %{?_smp_mflags} --no-notice gzip --best ::: nr/*.nr nri/*.nr

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc/{ref,tut}
cp -a *.g grp lib nr nri tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs -d doc/ref
%gap_copy_docs -d doc/tut
cp -a doc/htm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc README
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.9.6-2
- Update for split GAP directories

* Tue Dec  6 2022 Jerry James <loganjerry@gmail.com> - 2.9.6-1
- Version 2.9.6

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.9.5-1
- Clarify license of the doc subpackage

* Tue Oct 25 2022 Jerry James <loganjerry@gmail.com> - 2.9.5-1
- Version 2.9.5

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.9.4-3
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 21 2022 Jerry James <loganjerry@gmail.com> - 2.9.4-1
- Version 2.9.4

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 2.9.3-1
- Version 2.9.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 2.9.1-1
- New upstream version
- New URLs
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 2.8-4
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 2.8-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Compress files in parallel

* Thu Oct  8 2015 Jerry James <loganjerry@gmail.com> - 2.8-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 2.6-4
- Initial RPM
