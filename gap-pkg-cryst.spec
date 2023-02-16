%global pkgname cryst

# When bootstrapping a new architecture, there is no gap-pkg-crystcat yet.  That
# package is only needed for testing this one, but it needs this package to
# function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-crystcat
# 3. Build this package in non-bootstrap mode
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        4.1.25
Release:        4%{?dist}
Summary:        GAP support for crystallographic groups

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap/Cryst/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  tth

# For testing only
%if %{without bootstrap}
BuildRequires:  gap-pkg-crystcat
%endif

Requires:       gap-core
Requires:       gap-pkg-caratinterface
Requires:       gap-pkg-polycyclic

Suggests:       gap-pkg-crystcat
Suggests:       xgap

%description
The GAP 4 package Cryst, previously known as CrystGAP, is the successor
of the CrystGAP package for GAP 3.  During the porting process to GAP 4,
large parts of the code have been rewritten, and the functionality has
been extended considerably.  Cryst provides a rich set of methods to
compute with affine crystallographic groups, in particular space groups.
In contrast to the GAP 3 version, affine crystallographic groups are now
fully supported both in the representation acting from the right and in
the representation acting from the left.  The latter representation is
the one preferred by crystallographers.  There are also functions to
determine representatives of all space group types of a given dimension.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Cryst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap grp htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g
%endif

%files
%doc Changelog README
%license COPYING
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 4.1.25-3
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 4.1.25-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 4.1.25-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 4.1.25-1
- Convert License tag to SPDX

* Fri Jul 29 2022 Jerry James <loganjerry@gmail.com> - 4.1.25-1
- Version 4.1.25

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Jerry James <loganjerry@gmail.com> - 4.1.24-1
- Version 4.1.24

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 4.1.23-3
- Change gap-pkg-carat dependency to gap-pkg-caratinterface

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Jerry James <loganjerry@gmail.com> - 4.1.23-1
- Version 4.1.23

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 4.1.21-1
- New upstream version

* Thu Aug 29 2019 Jerry James <loganjerry@gmail.com> - 4.1.20-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 4.1.19-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 4.1.18-3
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 4.1.18-1
- New upstream version
- Add check script

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Jerry James <loganjerry@gmail.com> - 4.1.17-1
- New upstream version

* Sat Mar 17 2018 Jerry James <loganjerry@gmail.com> - 4.1.16-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb  3 2018 Jerry James <loganjerry@gmail.com> - 4.1.13-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.1.12-4
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 4.1.12-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Fri Jun 19 2015 Jerry James <loganjerry@gmail.com> - 4.1.12-1
- Initial RPM
