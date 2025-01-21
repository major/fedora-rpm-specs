# SPDX-License-Identifier: MIT
Version: 6.200
Release: 5%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Charis SIL
%global fontsummary       Charis SIL, a font family similar to Bitstream Charter
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Charis SIL provides glyphs for a wide range of Latin and Cyrillic characters.
Charis is similar to Bitstream Charter, one of the first fonts designed
specifically for laser printers. It is highly readable and holds up well in
less-than-ideal reproduction environments. It also has a full set of styles
— regular, italic, bold, bold italic — and so is more useful in general
publishing than Doulos SIL. Charis is a serif proportionally spaced font
optimized for readability in long printed documents.}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%setup -q -n %{archivename}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Parag Nemade <pnemade AT redhat DOT com> - 6.200-1
- Update to 6.200 version (#2166353)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 10 2022 Parag Nemade <pnemade@fedoraproject.org> - 6.101-1
- new version 6.101 (rh#2055204)

* Wed Feb 02 2022 Parag Nemade <pnemade@fedoraproject.org> - 6.001-1
- Update to new upstream release

* Wed Feb 02 2022 Parag Nemade <pnemade@fedoraproject.org> - 5.000-20
- Fix packaging issue

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-15
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-14
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-13
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-12
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-11
✅ Convert to fonts-rpm-macros use

* Sat Feb 18 2006 Roozbeh Pournader <roozbeh@farsiweb.info>
- 4.0.02-1
✅ Initial packaging, based on gentium-fonts
