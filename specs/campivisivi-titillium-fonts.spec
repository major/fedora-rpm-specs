Version: 20120913
Release: 31%{?dist}
URL: http://www.campivisivi.net/titillium/

%global foundry           Campivisivi
%global fontlicense       OFL-1.1
%global fontlicenses      OFL-titillium.txt
%global fontdocs          OFL-FAQ.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Titillium
%global fontsummary       Sans-serif typeface from the Master of Visual Design Campi Visivi
%global fonts             *.otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Sans-serif typeface from the Master of Visual Design Campi Visivi.}

Source0: http://www.campivisivi.net/titillium/download/Titillium_roman_upright_italic_2_0_OT.zip
Source1: 61-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n "Titillium_roman_upright_italic_2_0_OT"
%linuxtext OFL-titillium.txt OFL-FAQ.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Parag Nemade <pnemade@fedoraproject.org> - 20120913-23
- Convert this package to new fonts packaging guidelines

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 20130913-12
- Bump

* Wed Mar 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 20130913-11
- Reverted name of metainfo file

* Wed Mar 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 20120913-10
- Updated metainfo to adhere to appstream guideline
- Fixed typo within metainfo file
- Bumped for rebuild (release 8 and 9)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120913-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 20120913-5
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120913-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120913-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 20120913-2
- Update spec based on fedora packaging review

* Mon Jul 22 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 20120913-1
- Initial release
