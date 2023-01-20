Version:        1.000
Release:        17%{?dist}
URL:            http://www.astigmatic.com/

%global foundry           Astigmatic
%global fontlicense       OFL
%global fontlicenses      "SIL Open Font License.txt"

%global fontfamily        Grand Hotel
%global fontsummary       Script retro style fonts
%global fonts             *.otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Grand Hotel finds its inspiration from the title screen of the 1937 film “Cafe 
Metropole” starring Tyrone Power. This condensed upright connecting script has 
a classic vibe to it.

It has a wonderful weight to it that feels subtly tied to Holiday and Bakery 
themed designs, even though it can work outside that genre.}

Source0:        https://www.fontsquirrel.com/fonts/download/grand-hotel/grand-hotel.zip
Source1:        61-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Parag Nemade <pnemade@fedoraproject.org> - 1.000-14
- Convert this package to new fonts packaging guidelines

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-3
- Fix appdata file

* Sat Aug 20 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-2
- Remove legacy install code line "rm -fr %%{buildroot}"

* Fri Aug 19 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-1
- Initial build
