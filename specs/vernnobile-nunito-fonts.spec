# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/nunito
%global commit      6d8a4e1c00df8b361e59656eee7c2b458d663191
%forgemeta

Version: 3.504
Release: 18%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Nunito
%global fontsummary       Nunito, a sans serif font family with rounded terminals
%global fonts             fonts/TTF-unhinted/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Nunito is a well balanced sans serif with rounded terminals. Nunito has been
designed mainly to be used as a display font but is usable as a text font too.
Nunito has been designed to be used freely across the internet by web browsers
on desktop computers, laptops and mobile devices.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.504-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.504-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.504-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.504-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.504-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.504-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 3.504-12.20200215git6d8a4e1
- fix FTBFS

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-7.20200215git6d8a4e1
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-6.20200215git6d8a4e1
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-5.20200215git6d8a4e1
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-4
✅ Rebuild to workaround broken F31 build

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-3
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-1.20191208git6d8a4e1
✅ Initial packaging
