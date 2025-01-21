Version:        1.100
Release:        8%{?dist}
URL:            https://software.sil.org/mingzat/
BuildRequires:  fonts-rpm-macros

%global foundry         SIL
%global fontlicense     OFL-1.1
%global fontlicenses    OFL.txt OFL-FAQ.txt
%global fontdocs        *.txt
%global fontdocsex      %{fontlicenses}

%global fontfamily      Mingzat
%global fontsummary     A font for Lepcha script
%global fonts           *.ttf
%global fontconfs       %{SOURCE10}
%global fontdescription %{expand:
Mingzat is based on Jason Glavy's JG Lepcha font which was a custom-encoded
font. The goal for this product was to provide a single Unicode-based font
that would contain all Lepcha characters. In addition, there is provision for
other Latin characters and symbols. This font makes use of state-of-the-art
font technologies (Graphite and OpenType) to support the need for conjuncts
and to position arbitrary combinations of Lepcha glyphs and combining marks
optimally.}

# Licenses
# Mingzat-Regular.ttf:  OFL
# OFL.txt:      OFL and OFL text
# OFL-FAQ.txt:  No-modification. Handle it as an extension of OFL text so that
#               we can distribute it.
# org.fedoraproject.sil-mingzat-fonts.metainfo.xml: MIT # bug #2089366
# README.txt:   OFL
## Not in any binary package
# web/Mingzat-Regular.woff:         OFL
# web/Mingzat-Regular.woff2:        OFL
# web/Mingzat-webfont-example.css:  OFL
Source0:    https://software.sil.org/downloads/r/mingzat/%{fontfamily}-%{version}.zip
Source10:   65-sil-mingzat.conf

%fontpkg

%prep
%setup -q -n %{fontfamily}-%{version}
%linuxtext -n *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Akira TAGOH <tagoh@redhat.com> - 1.100-6
- Update License field to SPDX.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Petr Pisar <ppisar@redhat.com> - 1.100-1
- 1.100 bump

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-1
- 1.000 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.100-3
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Petr Pisar <ppisar@redhat.com> - 0.100-1
- 0.100 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Petr Pisar <ppisar@redhat.com> - 0.020-1
- Initial package
