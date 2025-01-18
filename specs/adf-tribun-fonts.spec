# SPDX-License-Identifier: MIT
Version: 1.17
Release: 18%{?dist}
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      OTF/COPYING
%global fontdocs          *.txt

%global fontfamily        Tribun
%global fontsummary       ADF Tribun, a newsprint-like serif font family
%global fonts             OTF/*.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Hirwen Harendal started in 1999 the realization of a first font family, aiming
to create another “Times New Roman”… He does not consider this endeavor a huge
success. However, he transformed Tribun progressively since then to give it its
own character.

The idea was to achieve newsprint-like rendering. To this effect, the glyph
bodies, serifs, or even extenders are not normalized and use irregular strokes.
This is most visible in italics though those variations stay imperceptible at
small sizes.

Italics proved time-consuming. They are never an easy thing to draw.
Nevertheless, the designer considers them very close to those of “Times”, with
some variations.

The medium weight uses a stronger stroke. It can be used for emphasis, or for
effects in titles. That being said it has also been used for body copy. It is
also slightly expanded to complete the face offerings.

The condensed version is a bit unusual, since it stands in for both normal and
medium condensed. After several trials, Hirwen decided an intermediate weight
rendered much better both for document display and in print. Secondly, he took
great care to keep readability excellent, and this even for italics.

This font family is particularly well suited for text, display, or
presentations. It is also ideal for all Web publications. It can serve as
alternative to “Times New Roman” and other similar fonts.}

%global archivename Tribun-Std-20120228

Source0:  http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:  http://arkandis.tuxfamily.org/docs/Tribun-Cat.pdf
Source10: 60-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE.txt OTF/COPYING

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OTF/COPYING
%doc *.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 1.17-11
- Fix FTBFS

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.17-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.17-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.17-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.17-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.17-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.17-1
✅ Convert to fonts-rpm-macros use

* Sat Oct 10 2009 Nicolas Mailhot <nim@fedoraproject.org>
- 1.13-1
— Initial release
