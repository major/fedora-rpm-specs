# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/GreatVibesFont
%global commit      a82e16d27e13b0d1337abeab05fdfd99a51d044c
%forgemeta

Version: 1.101
Release: 13%{?dist}
URL:     %{forgeurl}

%global foundry           TypeSETit
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Great Vibes
%global fontsummary       Great Vibes, a beautifully flowing cursive font family
%global fonts             fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Great Vibes is a beautifully flowing connecting cursive font family. It has
cleanly looping ascenders and descenders as well as elegant uppercase forms.}

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
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.101-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.101-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.101-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Akira TAGOH <tagoh@redhat.com>
- 1.101-10.20200215gita82e16d
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
- 1.101-5.20200215gita82e16d
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-4.20200215gita82e16d
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-3.20200215gita82e16d
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-1.20191208gita82e16d
✅ Initial packaging
