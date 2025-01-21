# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/weiweihuanghuang/Work-Sans
%global commit      dcd044c29b6f92f101a94777f744fa0f051da14b
%forgemeta

Version: 2.07
Release: 21%{?dist}
URL:     %{forgeurl}

%global foundry           weiweihuanghuang
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Work Sans
%global fontsummary       Work Sans, a font family in the early grotesque style
%global fonts             fonts/variable/*ttf fonts/static/OTF/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Work Sans is a font family based loosely on early Grotesques — i.e. Stephenson
Blake, Miller & Richard and Bauersche Gießerei. The core of the fonts are
optimized for on-screen medium-sized text usage,  but can still be used in
print. The fonts at the extreme weights are designed more for display use.
Overall, features are simplified and optimized for screen resolutions – for
example, diacritic marks are larger than how they would be in print.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

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

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc documentation/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Akira TAGOH <tagoh@redhat.com>
- 2.07-15.20200215gitdcd044c
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
- 2.07-10.20200215gitdcd044c
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-9.20200215gitdcd044c
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-8.20200215gitdcd044c
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-7
✅ Rebuild to workaround broken F31 build

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-6
✅ Lint, lint, lint and lint again

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-5
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-4
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.07-1.20191208gitdcd044c
✅ Initial packaging
