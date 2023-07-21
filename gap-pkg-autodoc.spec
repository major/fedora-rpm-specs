%global pkgname AutoDoc

# When bootstrapping a new architecture, there is no gap-pkg-io package yet,
# since it requires this package to build.  We only need it for testing this
# package, not for building it, so use the following procedure:
# 1. Do a bootstrap build of this package.
# 2. Build gap-pkg-io.
# 3. Do a normal build of this packages, which includes running the tests.
%bcond_with bootstrap

Name:           gap-pkg-autodoc
Version:        2023.06.19
Release:        2%{?dist}
Summary:        Generate documentation from GAP source code

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/AutoDoc/
Source0:        https://github.com/gap-packages/AutoDoc/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
%if %{without bootstrap}
BuildRequires:  gap-pkg-io
%endif
BuildRequires:  tex(a4wide.sty)

# AUTODOC_CurrentDirectory invokes pwd
Requires:       coreutils
Requires:       gap-core
Requires:       GAPDoc-latex

%description
This package is an add-on to GAPDoc that enables generating
documentation from GAP source code.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        AutoDoc documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../AutoDoc-%{version} ../pkg
gap -l "$PWD/..;" --bare -c 'LoadPackage("GAPDoc");' makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap makefile tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs
cp -p doc/*.xml %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" --bare -c 'LoadPackage("GAPDoc");' tst/testall.g
%endif

%files
%doc CHANGES README.md
%license COPYRIGHT LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.06.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Jerry James <loganjerry@gmail.com> - 2023.06.19-1
- Version 2023.06.19

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2022.10.20-2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2022.10.20-1
- Use upstream's method of bootstrapping
- Clarify license of the doc subpackage

* Thu Oct 20 2022 Jerry James <loganjerry@gmail.com> - 2022.10.20-1
- Version 2022.10.20

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 2022.07.10-3
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2022.07.10-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.07.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 2022.07.10-1
- Version 2022.07.10

* Thu Mar 10 2022 Jerry James <loganjerry@gmail.com> - 2022.03.10-1
- Version 2022.03.10

* Thu Feb 24 2022 Jerry James <loganjerry@gmail.com> - 2022.02.24-1
- Version 2022.02.24

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.08.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.08.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.08.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Jerry James <loganjerry@gmail.com> - 2020.08.11-1
- Version 2020.08.11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.09.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.09.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep  4 2019 Jerry James <loganjerry@gmail.com> - 2019.09.04-1
- New upstream version

* Fri Aug 16 2019 Jerry James <loganjerry@gmail.com> - 2019.07.24-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 2019.07.17-1
- New upstream version

* Wed Jul  3 2019 Jerry James <loganjerry@gmail.com> - 2019.07.03-1
- New upstream version

* Tue May 21 2019 Jerry James <loganjerry@gmail.com> - 2019.05.20-1
- New upstream version
- Drop upstreamed -ref patch

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 2019.04.10-1
- New upstream version
- Add -ref patch

* Fri Feb 22 2019 Jerry James <loganjerry@gmail.com> - 2019.02.22-1
- New upstream version

* Thu Feb 21 2019 Jerry James <loganjerry@gmail.com> - 2019.02.21-1
- New upstream version

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 2018.09.20-4
- Rebuild in non-bootstrap mode

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 2018.09.20-3
- Rebuild for gap 4.10.0
- Drop -test patch, only needed for gap <= 4.8
- Add bootstrap option
- Do a bootstrap build since gap-pkg-io hasn't been built for gap 4.10.0 yet
- Add a -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.09.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Jerry James <loganjerry@gmail.com> - 2018.09.20-1
- New upstream version
- Add check script

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Jerry James <loganjerry@gmail.com> - 2018.02.14-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.09.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep  9 2017 Jerry James <loganjerry@gmail.com> - 2017.09.08-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Jerry James <loganjerry@gmail.com> - 2016.12.04-1
- New upstream version

* Wed Nov 30 2016 Jerry James <loganjerry@gmail.com> - 2016.11.26-1
- New upstream version (bz 1400110)

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 2016.03.08-1
- New upstream version (bz 1314938)

* Thu Feb 18 2016 Jerry James <loganjerry@gmail.com> - 2016.02.16-1
- New upstream version (bz 1309144)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2016.01.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 2016.01.31-1
- New upstream version (bz 1303471)

* Thu Jan 21 2016 Jerry James <loganjerry@gmail.com> - 2016.01.21-1
- New upstream version (bz 1300867)

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 2015.09.30-1
- New upstream version
- Update URLs
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Mon Jun 22 2015 Jerry James <loganjerry@gmail.com> - 2015.04.29-2
- Remove erroneous isa tags
- Do not package 0-byte files

* Fri Jun 19 2015 Jerry James <loganjerry@gmail.com> - 2015.04.29-1
- Initial RPM (bz 1233984)
