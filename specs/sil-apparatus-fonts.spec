# SPDX-License-Identifier: MIT
Version: 1.0
Release: 17%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Apparatus SIL
%global fontsummary       Apparatus SIL, a font family for rendering Greek & Hebrew biblical texts
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", "");print(t)}
%global projectname       %{archivename}
URL:                      https://scripts.sil.org/ApparatusSIL
%global fonts             *.ttf *.TTF
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The Apparatus SIL font family was designed to provide most of the symbols
needed to reproduce the textual apparatus found in major editions of Greek &
Hebrew biblical texts. It is based on SIL Charis, a font family designed for
optimum clarity and compactness when printed at small point sizes. This assures
that both Charis SIL and Apparatus SIL can be used together in documents with a
consistency of style.

Most lines of text in the apparatus can be reproduced by combining the Greek
and Hebrew fonts, transliteration (using a font such as Charis SIL), and the
Apparatus SIL font.}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=AppSIL%{version}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%setup -q -c -T
unzip -j -q %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 1.0-11
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
- 1.0-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sun Feb 23 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-3
✅ Fix source URL

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-1
✅ Initial packaging
