# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/MuliFont
%global commit      580b05e1f2ad319cd98a8de03fd2da7b36677954
%forgemeta

Version: 2.001
Release: 18%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Muli
%global fontsummary       Muli, a minimalist sans serif font family
%global fonts             fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Muli is a minimalist sans serif font family, designed for both display and text
typography.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Akira TAGOH <tagoh@redhat.com>
- 2.001-12.20200215git580b05e
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
- 2.001-7.20200215git580b05e
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-6.20200215git580b05e
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-5.20200215git580b05e
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

 Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-4
✅ Rebuild to workaround broken F31 build

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-3
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-1.20191208git580b05e
✅ Initial packaging
