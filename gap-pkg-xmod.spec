%global pkgname XMod

Name:           gap-pkg-xmod
Version:        2.89
Release:        1%{?dist}
Summary:        Crossed Modules and Cat1-Groups for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/xmod/
Source0:        https://github.com/gap-packages/xmod/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-crisp
BuildRequires:  gap-pkg-groupoids
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-crisp
Requires:       gap-pkg-groupoids
Requires:       gap-pkg-hap
Requires:       gap-pkg-smallgrp
Requires:       gap-pkg-utils

%description
This package allows for computation with crossed modules, cat1-groups,
morphisms of these structures, derivations of crossed modules and the
corresponding sections of cat1-groups.  Experimental functions for
crossed squares are now included.  In October 2015 a new section on
isoclinism of crossed modules was added.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
# XY: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        XMod documentation
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
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
* Sun Feb  5 2023 Jerry James <loganjerry@gmail.com> - 2.89-1
- Version 2.89

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.88-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.88-4
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.88-3
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.88-3
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 2.88-1
- Do not build on i386 due to unavailability of polymake

* Thu Apr 28 2022 Jerry James <loganjerry@gmail.com> - 2.88-1
- Version 2.88

* Thu Mar 17 2022 Jerry James <loganjerry@gmail.com> - 2.86-1
- Version 2.86

* Sun Mar 13 2022 Jerry James <loganjerry@gmail.com> - 2.85-1
- Version 2.85

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Jerry James <loganjerry@gmail.com> - 2.84-1
- Version 2.84

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 18 2021 Jerry James <loganjerry@gmail.com> - 2.83-1
- Version 2.83

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Jerry James <loganjerry@gmail.com> - 2.82-1
- Version 2.82

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jerry James <loganjerry@gmail.com> - 2.81-1
- Version 2.81

* Tue May  5 2020 Jerry James <loganjerry@gmail.com> - 2.79-1
- Version 2.79

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.77-1
- Version 2.77
- Add gap-pkg-crisp BR and R to avoid incorrect test results

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 2.73-1
- New upstream version

* Wed Feb 13 2019 Jerry James <loganjerry@gmail.com> - 2.72-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Jerry James <loganjerry@gmail.com> - 2.64-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Jerry James <loganjerry@gmail.com> - 2.59-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec  3 2016 Jerry James <loganjerry@gmail.com> - 2.58-1
- New upstream version
- New URLs

* Fri Sep 30 2016 Jerry James <loganjerry@gmail.com> - 2.56-1
- Initial RPM
