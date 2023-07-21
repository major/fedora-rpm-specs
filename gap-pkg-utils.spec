%global pkgname utils

Name:           gap-pkg-%{pkgname}
Version:        0.82
Release:        2%{?dist}
Summary:        Utility functions for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/utils/
Source0:        https://github.com/gap-packages/utils/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-curlinterface-doc
BuildRequires:  gap-pkg-io-doc

Recommends:     gap-pkg-curlinterface

%description
The Utils package provides a collection of utility functions gleaned
from many packages.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        GAP utils documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-curlinterface-doc
Requires:       gap-pkg-io-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%build
export LC_ALL=C.UTF-8
gap -l "$PWD/..;" makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# The download test cannot be run on the koji builders, which provide no
# network access during a package build.
rm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst/download.tst
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g
cp -p tst/download.tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 10 2023 Jerry James <loganjerry@gmail.com> - 0.82-1
- Version 0.82

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 0.81-2
- Update for split GAP directories

* Mon Dec  5 2022 Jerry James <loganjerry@gmail.com> - 0.81-1
- Version 0.81

* Sat Nov 19 2022 Jerry James <loganjerry@gmail.com> - 0.78-1
- Version 0.78
- Drop dependency on gap-pkg-polycyclic

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 0.77-2
- Clarify license of the doc subpackage

* Wed Sep 28 2022 Jerry James <loganjerry@gmail.com> - 0.77-2
- Fix -doc subpackage Requires (rhbz#2130679)

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 0.77-1
- Version 0.77
- Convert License tag to SPDX
- Drop upstreamed -doc patch
- Update for gap 4.12.0

* Wed Aug  3 2022 Jerry James <loganjerry@gmail.com> - 0.75-1
- Version 0.75

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.74-1
- Version 0.74

* Wed Jul  6 2022 Jerry James <loganjerry@gmail.com> - 0.73-1
- Version 0.73

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Jerry James <loganjerry@gmail.com> - 0.72-1
- Version 0.72

* Mon Nov 15 2021 Jerry James <loganjerry@gmail.com> - 0.71-1
- Version 0.71

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Jerry James <loganjerry@gmail.com> - 0.69-1
- Version 0.69

* Fri Nov 22 2019 Jerry James <loganjerry@gmail.com> - 0.68-1
- Version 0.68

* Thu Sep  5 2019 Jerry James <loganjerry@gmail.com> - 0.67-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 0.64-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 0.61-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 0.53-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 0.49-1
- New upstream version

* Wed Nov  8 2017 Jerry James <loganjerry@gmail.com> - 0.48-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb  9 2017 Jerry James <loganjerry@gmail.com> - 0.46-1
- New upstream version, now needs polycyclic

* Wed Jan 18 2017 Jerry James <loganjerry@gmail.com> - 0.44-1
- New upstream version

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 0.43-1
- New upstream version

* Wed Oct 19 2016 Jerry James <loganjerry@gmail.com> - 0.42-1
- New upstream version

* Tue May  3 2016 Jerry James <loganjerry@gmail.com> - 0.40-1
- Initial RPM
