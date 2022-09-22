# SPDX-License-Identifier: MIT
Version: 5.000
Release: 12%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika Compact
%global fontsummary       SIL Andika Compact, a font family for literacy and beginning readers
%global projectname       andika
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Suggests: font(andika)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Andika is a sans serif, Unicode-compliant font family designed especially for
literacy use, taking into account the needs of beginning readers. The focus is
on clear, easy-to-perceive letter-forms that will not be readily confused with
one another.

A sans serif font is preferred by some literacy personnel for teaching people
to read. Its forms are simpler and less cluttered than those of most serif
fonts. For years, literacy workers have had to make do with fonts that were
not really suitable for beginning readers and writers. In some cases, literacy
specialists have had to tediously assemble letters from a variety of fonts in
order to get all of the characters they need for their particular language
project, resulting in confusing and unattractive publications. Andika
addresses those issues.

The Andika Compact font family was derived from Andika using SIL TypeTuner,
by setting the “Line spacing” feature to “Tight”, and it cannot be TypeTuned
again. It may exhibit some diacritics clipping on screen (but should print
fine).}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 62-%{fontpkgname}.xml

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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Akira TAGOH <tagoh@redhat.com>
- 5.000-11
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
- 5.000-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-1
✅ Initial packaging
