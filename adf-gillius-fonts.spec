# SPDX-License-Identifier: MIT
Version: 1.009
Release: 5%{?dist}
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0
%global fontlicenses      OTF/COPYING
%global fontdocs          NOTICE

%global common_description %{expand:
The Gillius family from the Arkandis Digital Foundry is a set of sans-serif
typefaces intended as an alternative to Gill Sans. Its two widths, regular and
condensed, both feature a roman and an italic, and each includes a regular and
bold weight.
}

%global fontfamily0       Gillius
%global fontsummary0      ADF Gillius sans-serif typeface family, a GillSans alternative
%global fontpkgheader0    %{expand:
Obsoletes: adf-gillius-fonts-common < %{version}-%{release}
}
%global fonts0            OTF/GilliusADF-*
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This is the base variant.}

%global fontfamily2       Gillius-2
%global fontsummary2      ADF Gillius No2 sans-serif typeface family. a GillSans alternative
%global fonts2            OTF/GilliusADFNo2-*
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

A slightly rounder variant, which features the same set of weights,
widths, and slopes.}


%global archivename Gillius-Collection-20110312

Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/%{fontfamily}-cat.pdf
Source10:  69-%{fontpkgname}.conf
Source12:  69-%{fontpkgname2}.conf



%fontpkg -a

%fontmetapkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE OTF/COPYING

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license OTF/COPYING
%doc *.pdf 


%changelog
* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.009-5
- SPDX migration

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 13 2021 Michael J. Gruber <mjg@fedoraproject.org> - 1.009-1
- rebase with upstream 1.009
- switch to current fonts rpm macros

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.008-10
- Add metainfo file to show this font in gnome-software
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Michael J Gruber <mjg at fedoraproject.org> - 1.008-3
- split into subpackages

* Mon Nov 15 2010 Michael J Gruber <mjg at fedoraproject.org> - 1.008-2
- Add fontconfig rules for Gillius ADF No2

* Sun Nov 14 2010 Michael J Gruber <mjg at fedoraproject.org> - 1.008-1
- Initial packaging for Fedora
