%global pkgname ctbllib

# When bootstrapping a new architecture, there is no gap-pkg-spinsym package
# yet.  We need it to run tests, but it needs this package to function at all.
# Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-spinsym
# 4. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        1.3.7
Release:        3%{?dist}
Summary:        GAP Character Table Library

License:        GPL-3.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/
Source0:        %{url}%{pkgname}-%{version}.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

# The makedocrel script determines that the package being built is outside of
# the normal GAP install directories and refuses to do anything with it.
Patch0:         %{name}-makedocrel.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-browse-doc
BuildRequires:  gap-pkg-cohomolo
BuildRequires:  gap-pkg-grpconst
BuildRequires:  gap-pkg-smallgrp-doc
%if %{without bootstrap}
BuildRequires:  gap-pkg-spinsym
%endif
BuildRequires:  gap-pkg-tomlib-doc
BuildRequires:  netpbm-progs
BuildRequires:  parallel
BuildRequires:  tex(epic.sty)

Requires:       gap-pkg-atlasrep

Recommends:     gap-pkg-browse
Recommends:     gap-pkg-primgrp
Recommends:     gap-pkg-smallgrp
Recommends:     gap-pkg-spinsym
Recommends:     gap-pkg-tomlib
Recommends:     gap-pkg-transgrp

%description
This package provides the Character Table Library by Thomas Breuer.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# LaTeX: LPPL-1.3a
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Character Table Library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-browse-doc
Requires:       gap-pkg-smallgrp-doc
Requires:       gap-pkg-tomlib-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b1 -p1

# Remove spurious executable bit
chmod a-x doc/utils.xml

%build
# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tbl

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}
cp -a *.g data dlnames gap4 htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}

# Building documentation has to be done after installation, because otherwise
# GAP sees an old version of ctbllib in the buildroot rather than this version,
# and the ctbllib version check kills the build.
export LC_ALL=C.UTF-8
cp -a doc doc2 %{buildroot}%{gap_libdir}/pkg/%{pkgname}
gap -l "%{buildroot}%{gap_libdir};" < makedocrel.g
rm -fr doc doc2
mv %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc{,2} .
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc{,2}
%gap_copy_docs
%gap_copy_docs -d doc2

%check
export LC_ALL=C.UTF-8

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

# Basic installation test
gap -l "%{buildroot}%{gap_libdir};" << EOF
ReadPackage( "ctbllib", "tst/testinst.g" );
EOF

%if %{without bootstrap}
# Somewhat less basic test.  Skip the interactive tests.
# Do not run testall.g.  It takes a long time to run.
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
sed -i '/BrowseCTblLibInfo();/d' gap4/ctbltocb.g tst/docxpl.tst
gap -l "$PWD/..;" tst/testauto.g
rm -fr ../pkg
%endif

%files
%doc README.md
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc2/
%exclude %{gap_libdir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/doc2/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc2/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  9 2024 Jerry James <loganjerry@gmail.com> - 1.3.7-1
- Version 1.3.7

* Fri Sep 15 2023 Jerry James <loganjerry@gmail.com> - 1.3.6-1
- Version 1.3.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar  7 2023 Jerry James <loganjerry@gmail.com> - 1.3.5-1
- Version 1.3.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.3.4-4
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.3.4-3
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.3.4-3
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.3.4-2
- License change from GPLv2+ to GPL-3.0-or-later

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Jerry James <loganjerry@gmail.com> - 1.3.4-1
- Version 1.3.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- Version 1.3.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 29 2021 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Version 1.3.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Version 1.3.1

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0
- Drop all patches
- Add bootstrap mode to guard test that needs spinsym

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.2.2-13
- Rebuild for gap 4.10.0
- Add -generators patch to work around incompatibility with gap 4.10.0
- Add -test patch to fix problems with the tests
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-7
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-5
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-3
- Use redirection to force check script to terminate

* Thu Jan 29 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-2
- Use _smp_mflags when compressing

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- Initial RPM
