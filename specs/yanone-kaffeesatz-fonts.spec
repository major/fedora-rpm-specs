# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/alexeiva/yanone-kaffeesatz/
%global commit      1da49356a388c67da5b51d54fd6ad5a686d96c46
%forgemeta

Epoch:   1
Version: 2.001
Release: 18%{?dist}
URL:     http://www.yanone.de/typedesign/kaffeesatz/

%global foundry           Yanone
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Kaffeesatz
%global fontsummary       Yanone Kaffeesatz, a decorative font family
%global fonts             fonts/ttf/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Yanone Kaffeesatz is a sans-serif decorative Latin font family by Jan Gerner,
suitable for titles and short runs of text.

Its Bold is reminiscent of 1920s coffee house typography, while the rather thin
fonts bridge the gap to present times.

You can witness Kaffeesatz use on German fresh-water gyms, Dubai mall promos
and New Zealand McDonalds ads. And of course on coffee and foodstuff packaging
and café design around the globe.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Akira TAGOH <tagoh@redhat.com>
- 2.001-12.20200215git1da4935
- Fix FTBFS.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-7.20200215git1da4935
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-6.20200215git1da4935
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-5.20200215git1da4935
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1:2.001-4
✅ Lint, lint, lint and lint again

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1:2.001-3
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1:2.001-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1:2.001-1.20191209git1da4935
✅ Convert to fonts-rpm-macros use
✅ Package the Google Fonts extended version

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20061120-3
✅ Initial packaging
