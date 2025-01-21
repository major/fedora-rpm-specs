# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather-Sans
%global commit      f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
%forgemeta

Version: 1.008
Release: 12%{?dist}
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather Sans
%global fontsummary       Merriweather Sans, a low-contrast semi-condensed sans-serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Merriweather Sans is a low-contrast semi-condensed sans-serif font family
designed to be readable at very small sizes. Merriweather Sans is traditional
in feeling despite the modern shapes it has adopted for screens. It is a
companion to the serif font family Merriweather.}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-1.20191208gitf36d6e1
✅ Initial packaging
