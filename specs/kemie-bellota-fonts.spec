# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/kemie/Bellota-Font/
Version:            4.1
%forgemeta

Release: 15%{?dist}
URL:     %{forgeurl}

%global foundry           kemie
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *TXT *md
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
The Bellota font families are ornamented, low contrast sans-serifs with text
and swash alternates. They’re just cute enough! They include stylistic
alternates (for swash and non-ornamented characters) and ligatures available
through OpenType features.}

%global fontfamily0       Bellota
%global fontsummary0      An ornamented, cute, low contrast sans-serif font family
%global fonts0            ttf/*ttf
%global fontsex0          %{fonts1}
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

Bellota, is the most exuberant variation published by the project.}

%global fontfamily1       Bellota Text
%global fontsummary1      An ornamented, slightly demure, cute, low contrast sans-serif font family
%global fontpkgheader1    %{expand:
Suggests: font(bellota)
}
%global fonts1            ttf/BellotaText*ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

Bellota Text is slightly more demure than Bellota itself.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname0}.xml
Source11: 60-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%prep
%forgesetup

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 4.1-9
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
- 4.1-4
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-3
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-2
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Thu Mar 26 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-1
✅ Initial packaging
