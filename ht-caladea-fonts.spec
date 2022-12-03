%global forgeurl https://github.com/huertatipografica/Caladea
%global commit 336a529cfad3d103d6527752686f8331d13e820a
Epoch: 1
Version: 1.001
%forgemeta

Release:  8%{?dist}
URL:     https://github.com/huertatipografica/Caladea

%global foundry           HT
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Caladea
%global fontsummary       Caladea, a serif font family metric-compatible with Cambria font family
%global fontpkgheader     %{expand:
Obsoletes:      google-crosextra-caladea-fonts < 1.002-0.15.20130214
Provides:       google-crosextra-caladea-fonts = 1:%{version}-%{release}
}
%global fonts             fonts/otf/*otf
%global fontconfs         %{SOURCE1} %{SOURCE2}
%global fontdescription   %{expand:
Caladea is a free modern, friendly serif font family based on Cambo
(https://fonts.google.com/specimen/Cambo) Designed by Carolina Giovagnoli
and Andrés Torresi for Huerta Tipográfica in 2012.

Cambo is a modern Latin typeface inspired by the contrast, style and ornaments
of Khmer typefaces and writing styles. Its main objective is to be used to
write Latin texts in a Khmer context, but it is also an elegant choice for all
kinds of texts.

Caladea is metric-compatible with Cambria font.}

Source0:  %{forgesource}
Source1:  30-0-%{fontpkgname}.conf
Source2:  62-%{fontpkgname}.conf

%fontpkg

%prep
%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Dec 01 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:1.001-8
- Update license tag to SPDX format

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:1.001-2.20200401git336a529
- Update the DTD id in fontconfig files

* Tue Mar 17 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:1.001-1.20200401git336a529
- Initial Fedora release.
- Rename from google-crosextra-caladea-fonts
