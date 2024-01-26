%global pkgname hapcryst

Name:           gap-pkg-%{pkgname}
Version:        0.1.15
Release:        7%{?dist}
Summary:        Integral cohomology computations of Bieberbach groups

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/hapcryst/
Source0:        https://github.com/gap-packages/hapcryst/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Fix documentation bugs
Patch0:         %{name}-doc.patch
# Adapt to Carat -> CaratInterface name change
Patch1:         %{name}-carat.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-cryst
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-polymaking-doc

Requires:       gap-pkg-aclib
Requires:       gap-pkg-cryst
Requires:       gap-pkg-hap
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-polymaking

Recommends:     gap-pkg-caratinterface
Recommends:     gap-pkg-crystcat

%description
This package is an add-on for Graham Ellis' HAP package.  HAPcryst
implements some functions for crystallographic groups (namely
OrbitStabilizer-type methods).  It is also capable of calculating free
resolutions for Bieberbach groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        HAPcryst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

# Fix up broken HTML links between the two books
sed -i "s,\./lib,.&,g" doc/*.html

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
rm -fr %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc
%gap_copy_docs
%gap_copy_docs -d lib/datatypes/doc

%check
export LC_ALL=C.UTF-8

# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Run the actual tests
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES README
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/examples/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc/

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 0.1.15-3
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 0.1.15-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 0.1.15-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 0.1.15-1
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 0.1.15-1
- Version 0.1.15

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.1.14-1
- Do not build on i386 due to unavailability of polymake

* Thu Mar 10 2022 Jerry James <loganjerry@gmail.com> - 0.1.14-1
- Version 0.1.14
- Drop upstreamed -test patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Jerry James <loganjerry@gmail.com> - 0.1.13-1
- Version 0.1.13

* Mon Feb  3 2020 Jerry James <loganjerry@gmail.com> - 0.1.12-1
- Version 0.1.12
- Drop upstreamed -dims patch
- Actually put some files into the -doc subpackage

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Jerry James <loganjerry@gmail.com> - 0.1.11-9
- Add -carat patch due to package name change

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 0.1.11-7
- Rebuild for gap 4.10.0
- Add -doc subpackage
- Add -dims patch due to changes in polymake

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Jerry James <loganjerry@gmail.com> - 0.1.11-1
- Initial RPM
