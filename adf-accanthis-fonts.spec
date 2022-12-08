# SPDX-License-Identifier: MIT
Version: 1.8
Release: 28%{?dist}
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0
%global fontlicenses      OTF/COPYING
%global fontdocs          NOTICE.txt

%global common_description %{expand:
A Latin font family published by Hirwen Harendal’s Arkandis Digital Foundry,
Accanthis was inspired from the “Cloister Oldstyle” font family found in the
“American Specimen Book of Typefaces Suplement”. Its medium contrast is
sufficient to be reader-friendly and deliver an elegant and refined experience.

Accanthis is a modernized garaldic font family and is well suited to book
typesetting and refined presentations.}

%global fontfamily0       Accanthis
%global fontsummary0      ADF Accanthis, a modernized garaldic serif font family, “Galliard” alternative
%global fontpkgheader0    %{expand:
Obsoletes: adf-accanthis-fonts-common < %{version}-%{release}
}
%global fonts0            OTF/AccanthisADFStd-*.otf
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This variant is intended to serve as alternative to the “Galliard” font family.}

%global fontfamily2       Accanthis-2
%global fontsummary2      ADF Accanthis Nᵒ2, a modernized garaldic serif, “Horley old style” alternative
%global fonts2            OTF/AccanthisADFStdNo2-*.otf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This variant is closer to the “Horley old style” font family than the original
version.}

%global fontfamily3       Accanthis-3
%global fontsummary3      ADF Accanthis Nᵒ3, a modernized garaldic serif font family
%global fonts3            OTF/AccanthisADFStdNo3-*.otf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This variant remixes a slightly modified Accanthis №2 with elements from the
original Italic and changes to k, p, z and numbers.}

%global archivename Accanthis-Std-20101124

Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Accanthis-Cat.pdf
Source10:  60-%{fontpkgname}.xml
Source12:  60-%{fontpkgname2}.xml
Source13:  60-%{fontpkgname3}.xml


%fontpkg -a

%fontmetapkg

%package   doc
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
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license OTF/COPYING
%doc *.pdf

%changelog
* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.8-28
- SPDX migration

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Michael J Gruber <mjg@fedoraproject.org> - 1.8-24
- fix FTBFS due to premature spec update

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.8-21
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.8-20
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.8-19
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.8-18
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.8-17
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.8-16
✅ Convert to fonts-rpm-macros use

* Sun Jul 12 2009 Nicolas Mailhot <nim@fedoraproject.org>
- 1.6-1
✅ Initial packaging
