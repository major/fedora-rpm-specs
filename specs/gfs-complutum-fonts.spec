# SPDX-License-Identifier: MIT
Version: 20070413
Release: 47%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/16th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Complutum
%global fontsummary       GFS Complutum, a 16th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The ancient Greek alphabet evolved during the millennium of the Byzantine era
from majuscule to minuscule form and gradually incorporated a wide array of
ligatures, flourishes and other decorative nuances which defined its
extravagant cursive character. Until the late 15th century, typographers who
had to deal with Greek text avoided emulating this complicated hand; instead
they would use only the twenty four letters of the alphabet separately, often
without accents and other diacritics.

A celebrated example is the type cut and cast for the typesetting of the New
Testament in the so-called Complutensian Polyglot Bible (1512), edited by the
Greek scholar, Demetrios Doukas. The type was cut by Arnaldo Guillén de Brocar
and the whole edition was a commission by cardinal Francisco Ximénez, in the
University of Alcalá (Complutum), Spain. It is one of the best and most
representative models of this early tradition in Greek typography which was
revived in the early 20th century by the eminent bibliographer of the British
Library, Richard Proctor. A font named Otter Greek was cut in 1903 and a book
was printed using the new type. The original type had no capitals so Proctor
added his own, which were rather large and ill-fitted. The early death of
Proctor, the big size of the font and the different aesthetic notions of the
time were the reasons that Otter Greek was destined to oblivion, as a
curiosity.

Greek Font Society incorporated Brocar’s famous and distinctive type in the
commemorative edition of Pindar’s Odes for the Athens Olympics (2004) and the
type with a new set of capitals, revived digitally by George D. Matthiopoulos,
is now available for general use.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

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
%doc *.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 20070413-40
- Fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-35
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-34
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-33
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-32
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-31
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-30
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20070413-2
✅ Initial packaging
