# SPDX-License-Identifier: MIT

Version: 2.004
Release: 10%{?dist}
URL:     https://github.com/adobe-fonts/source-han-sans/

%global foundry           Adobe
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      LICENSE.txt

%global fontfamily        Source Han Sans TW
%global fontsummary       Adobe OpenType Pan-CJK font family for Traditional Chinese
%global fonts             SubsetOTF/TW/SourceHanSansTW*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Sans is a sans serif Pan-CJK font family 
that is offered in seven weights—ExtraLight, Light, 
Normal, Regular, Medium, Bold, and Heavy—and 
in several OpenType/CFF-based deployment configurations
to accommodate various system requirements or limitations.

As the name suggests, Pan-CJK fonts are intended to
support the characters necessary to render or
display text in Simplified Chinese, Traditional Chinese,
Japanese, and Korean.
}

Source0:  https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/SourceHanSansTW.zip
Source10: 65-2-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 Peng Wu <pwu@redhat.com> - 2.004-5
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  2 2021 Peng Wu <pwu@redhat.com> - 2.004-1
- Update to 2.004

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 2020 Peng Wu <pwu@redhat.com> - 2.002-1
- Update to 2.002

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peng Wu <pwu@redhat.com> - 2.001-1
- Update to 2.001

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Peng Wu <pwu@redhat.com> - 2.000-1
- Update to 2.000

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 1.004-9
- Update the fontconfig priority to ensure this as default for upgrading.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb  1 2018 Peng Wu <pwu@redhat.com> - 1.004-7
- Update the priority to change the default font to Noto

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Peng Wu <pwu@redhat.com> - 1.004-5
- Use Source Han Sans for Mono and Sans
- Use Source Han Serif for Serif

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Peng Wu <pwu@redhat.com> - 1.004-2
- Fixes Obsoletes

* Fri Aug  7 2015 Peng Wu <pwu@redhat.com> - 1.004-1
- Update to 1.004

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Peng Wu <pwu@redhat.com> - 1.002-1
- Update to 1.002

* Mon Apr 13 2015 Peng Wu <pwu@redhat.com> - 1.001-2
- Update spec according to review feedback.

* Mon Mar 30 2015 Peng Wu <pwu@redhat.com> - 1.001-1
- Renamed from adobe-source-han-sans-twhk-fonts

