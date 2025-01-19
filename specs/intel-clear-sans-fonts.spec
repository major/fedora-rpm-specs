# SPDX-License-Identifier: MIT
Version: 1.00
Release: 19%{?dist}
%global  projectname clear-sans
URL:     https://01.org/%{projectname}

%global foundry           Intel
%global fontlicense       Apache-2.0
%global fontlicenses      LICENSE-2.0.txt

%global fontfamily        Clear Sans
%global fontsummary       Clear Sans, a versatile font family for screen, print, and Web
%global fonts             TTF/*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription  %{expand:
Clear Sans has been recognized as a versatile font for screen, print, and Web.
Its minimized, unambiguous characters and slightly narrow proportions, make it
ideal for UI design.

Clear Sans was designed with on-screen legibility in mind. It strikes a balance
between contemporary, professional, and stylish expression and thoroughly
functional purpose. It has a sophisticated and elegant personality at all
sizes, and its thoughtful design becomes even more evident at the thin weight.}

Source0:  https://01.org/sites/default/files/downloads/%{projectname}/clearsans-%{version}.zip
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%setup -q -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 1.00-12
- Fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-7
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-6
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Sat Mar  7 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-3
✅ Initial packaging
