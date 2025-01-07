# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/huertatipografica/Alegreya
Version: 2.008
%forgemeta

Release: 15%{?dist}
URL:     https://www.huertatipografica.com/en/fonts/alegreya-ht-pro

%global foundry           HT
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alegreya
%global fontsummary       Alegreya, a dynamic and varied serif font family
%global fontpkgheader     %{expand:
# Small Caps are accessible in the main family using OpenType features
Obsoletes: ht-alegreya-smallcaps-fonts < %{version}-%{release}
}
%global fonts             fonts/otf/*otf
%global fontsex           fonts/otf/*SC*otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Alegreya is a font family originally intended for literature. Among its
crowning characteristics, it conveys a dynamic and varied rhythm which
facilitates the reading of long texts. Also, it provides freshness to the page
while referring to the calligraphic letter, not as a literal interpretation,
but rather in a contemporary typographic language.

The italic has just as much care and attention to detail in the design as the
roman. The bold weights are strong, and the Black weights are really
experimental for the genre.

Not only does Alegreya provide great performance, but also achieves a strong
and harmonious text by means of elements designed in an atmosphere of
diversity.

Alegreya was chosen as one of 53 “Fonts of the Decade” at the ATypI Letter2
competition in September 2011, and one of the top 14 text type systems. It was
also selected in the 2nd Bienal Iberoamericana de Diseño, competition held in
Madrid in 2010.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.conf

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
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.008-6
- Fix fontconfig DTD id

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar  7 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-3
✅ Use traditional fontconfig syntax, upstream is clean enough the project does
   not need complex rules

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-1
✅ Convert to fonts-rpm-macros use
✅ Drop Small Caps: they are included in the main family as an OpenType feature

* Fri Sep 14 2012 Tom Callaway <spot@fedoraproject.org> - 1.004-1
- initial package
