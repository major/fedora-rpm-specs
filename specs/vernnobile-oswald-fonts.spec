# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/OswaldFont
%global commit      5a5fff234687674f8531a8537455e626b08b3321
%forgemeta

Version: 4.101
Release: 20%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Oswald
%global fontsummary       Oswald, a reworked Gothic style font family
%global fonts             fonts/otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Oswald is a reworking of the classic Gothic typeface style historically
represented by designs such as “Alternate Gothic”. The characters of Oswald
have been re-drawn and reformed to better fit the pixel grid of standard
digital screens. Oswald is designed to be used freely across the internet by
web browsers on desktop computers, laptops and mobile devices.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup
%linuxtext %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.101-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.101-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.101-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.101-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.101-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.101-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 4.101-14.20200215git5a5fff2
- Fix FTBFS

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-9.20200215git5a5fff2
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-8.20200215git5a5fff2
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-7.20200215git5a5fff2
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-6
✅ Rebuild to workaround broken F31 build

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-5
✅ Lint, lint, lint and lint again

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-4
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.101-1.20191208git5a5fff2
✅ Initial packaging
