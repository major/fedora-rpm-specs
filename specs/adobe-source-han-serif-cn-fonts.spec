# SPDX-License-Identifier: MIT

Version: 2.003
Release: 2%{?dist}
URL:     https://github.com/adobe-fonts/source-han-serif/

%global foundry           Adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt

%global fontfamily        Source Han Serif CN
%global fontsummary       Adobe OpenType Pan-CJK font family for Simplified Chinese
%global fonts             SourceHanSerifCN*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.
}

Source0:  https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/SourceHanSerifCN.zip
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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 15 2024 Peng Wu <pwu@redhat.com> - 2.003-1
- Update to 2.003
- Resolves: RHBZ#2302468

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 21 2023 Peng Wu <pwu@redhat.com> - 2.002-1
- Update to 2.002
- Resolves: RHBZ#2232879

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 15 2023 Peng Wu <pwu@redhat.com> - 2.001-4
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Peng Wu <pwu@redhat.com> - 2.001-1
- Update to 2.001

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Peng Wu <pwu@redhat.com> - 2.000-1
- Update to 2.000

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 1.001-6
- Update the fontconfig priority to ensure this as default for upgrading.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb  1 2018 Peng Wu <pwu@redhat.com> - 1.001-4
- Update the priority to change the default font to Noto

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Peng Wu <pwu@redhat.com> - 1.001-2
- Use Source Han Sans for Mono and Sans
- Use Source Han Serif for Serif

* Mon Jun 12 2017 Peng Wu <pwu@redhat.com> - 1.001-1
- Initial Version
