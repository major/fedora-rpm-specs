%global pkgname polymaking

Name:           gap-pkg-%{pkgname}
Version:        0.8.7
Release:        2%{?dist}
Summary:        GAP interface to polymake

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/polymaking/
Source0:        https://github.com/gap-packages/polymaking/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  polymake

Requires:       gap-core
Requires:       polymake

%description
This package provides a very basic GAP interface to polymake.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polymaking documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

# Fix an undefined LaTeX command in the BibTeX file
sed -i 's/URL/url/' doc/polymaking.bib

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Now we can run the actual test.
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov  7 2023 Jerry James <loganjerry@gmail.com> - 0.8.7-1
- Version 0.8.7
- Drop upstreamed doc patch

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 0.8.6-6
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 0.8.6-5
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 0.8.6-5
- Update for gap 4.12.0
- Add -doc patch
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.8.6-3
- Do not build on i386 due to unavailability of polymake

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.8.6-1
- Version 0.8.6

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 0.8.5-1
- Version 0.8.5

* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 0.8.4-1
- Version 0.8.4

* Mon Apr 12 2021 Jerry James <loganjerry@gmail.com> - 0.8.3-1
- Version 0.8.3
- Drop all patches; all have been upstreamed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Jerry James <loganjerry@gmail.com> - 0.8.2-5
- Rebuild for gap 4.11.0

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.8.2-4
- Add -polymake4 patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 0.8.2-1
- New upstream version
- New URLs
- Drop upstreamed -output and -test patches

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 0.8.1-11
- Rebuild for gap 4.10.0
- Add a -doc subpackage
- Add the -test patch to use a more modern test method
- Add the -dims patch to adapt to recent versions of polymake

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-5
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 0.8.1-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Add -output patch to fix misparsed polymake output

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- Initial RPM
