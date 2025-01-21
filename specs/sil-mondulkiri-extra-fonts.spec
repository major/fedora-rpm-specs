# SPDX-License-Identifier: MIT
BuildArch: noarch

Version: 5.300
Release: 17%{?dist}
License: OFL-1.1-RFN
URL:     https://scripts.sil.org/Mondulkiri

%global source_name       sil-mondulkiri-extra-fonts

Name: %{source_name}

%global foundry           SIL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description %{expand: The Mondulkiri font families provide
Unicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the
names of two provinces in north-eastern Cambodia, Busra and Oureang are names
of places in Mondulkiri province.}

%global fontfamily1       Ratanakiri
%global fontsummary1      Khmer Ratanakiri, a Khmer Mool title font family
%global fonts1            RataV53.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

Khmer Ratanakiri is a Mool (or Muol or Muul) font family which is frequently
used for headings and signs. At this point of time most ligatures have not yet
been implemented. Some coengs of independent vowels and other features used
only infrequently in normal Khmer text are currently still implemented in a
different character style. This font does not support more than one
below‐coeng, i.e. words like លក្ស្មណៈ cannot be written in it.}

%global fontfamily2       Oureang
%global fontsummary2      Khmer Oureang, a very bold Khmer title font family
%global fontpkgheader2    %{expand:
Suggests: font(khmermondulkiri)
}
%global fonts2            Mo9V55.ttf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

Khmer Oureang is a very bold Khmer script font family, useful for headings. It
was formerly named “Khmer Mondulkiri ultra”.}

%global fontfamily3       Busra MOE
%global fontsummary3      Khmer Busra MOE, a special Khmer Busra variant
%global fontpkgheader3    %{expand:
Suggests: font(khmerbusra)
}
%global fonts3            Mo5V56MO.ttf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

Khmer Busra MOE drops a below‐vowel in a cluster containing a coeng‐Ro.}

%global fontfamily4       Busra dict
%global fontsummary4      Khmer Busra dict, a special Khmer Busra variant
%global fontpkgheader4    %{expand:
Suggests: font(khmerbusra)
}
%global fonts4            Mo5V56dc.ttf
%global fontconfngs4      %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

Khmer Busra dict has alternative shapes for four of the Khmer letters as they
are found in some dictionaries.}

%global fontfamily5       Busra high
%global fontsummary5      Khmer Busra high, a special Khmer Busra variant
%global fontpkgheader5    %{expand:
Suggests: font(khmerbusra)
}
%global fonts5            Mo5V56hi.ttf
%global fontconfngs5      %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

Khmer Busra high has a higher line height in order to accommodate some rare
Khmer words on screen.}

%global fontfamily6       Busra Bunong
%global fontsummary6      Khmer Busra Bunong, a special Khmer Busra variant
%global fontpkgheader6    %{expand:
Suggests: font(khmerbusra)
}
%global fonts6            Mo5V56Bu.ttf
%global fontconfngs6      %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

Khmer Busra Bunong has a lower line height. Some coengs or vowels under coengs
may not display on screen or touch the top character of the next line. If any
parts are clipped on the screen they should, however, be visible in print. It
will provide more lines of text on a given page.}

%global fontfamily7       Busra xspace
%global fontsummary7      Khmer Busra xspace, a special Khmer Busra variant
%global fontpkgheader7    %{expand:
Suggests: font(khmerbusra)
}
%global fonts7            Mo5V56xs.ttf
%global fontconfngs7      %{SOURCE17}
%global fontdescription7 %{expand:
%{common_description}

Khmer Busra xspace makes a number of otherwise invisible or not easily visible
characters visible. However, many word processors and editors take charge of
some or all of these characters and do not display them in the way they are
provided in the font.}

%global fontfamily8       Busra diagnostic
%global fontsummary8      Khmer Busra diagnostic, a special Khmer Busra variant
%global fontpkgheader8    %{expand:
Suggests: font(khmerbusra)
}
%global fonts8            Mo5V56di.ttf
%global fontconfngs8      %{SOURCE18}
%global fontdescription8  %{expand:
%{common_description}

Khmer Busra diagnostic does the same as Khmer Busra xspace, but also adds
dotted circles before coengs if they follow a vowel as well as in between
multiple above‐symbols. Both of these character sequences are permitted in
Windows, but the former is often a miss‐spelling and the latter is also usually
unintended and a miss‐spelling as well as not being permitted in other
operating systems. In this way the font helps to spot common typos.}

%global fontfamily9       Busra dot
%global fontsummary9      Khmer Busra dot, a special Khmer Busra variant
%global fontpkgheader9    %{expand:
Suggests: font(khmerbusra)
}
%global fonts9            Mo5V56do.ttf
%global fontconfngs9      %{SOURCE19}
%global fontdescription9 %{expand:
%{common_description}

This font does something that a Unicode font should not do and that is it does
not show the “correct” symbol for one particular Unicode code-point. It shows a
dotted circle in the place where a ក should be shown. It may be used for
didactic purposes.}

%global archivename Mondulkiri-%{version}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}&filename=%{archivename}.zip#/%{archivename}.zip
Source11: 66-%{fontpkgname1}.xml
Source12: 66-%{fontpkgname2}.xml
Source13: 66-%{fontpkgname3}.xml
Source14: 66-%{fontpkgname4}.xml
Source15: 66-%{fontpkgname5}.xml
Source16: 66-%{fontpkgname6}.xml
Source17: 66-%{fontpkgname7}.xml
Source18: 66-%{fontpkgname8}.xml
Source19: 66-%{fontpkgname9}.xml

Summary:  Extra Khmer script font families from the SIL Mondulkiri project
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%setup -q -n %{archivename}
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc documentation/*.pdf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.300-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.300-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.300-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.300-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.300-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 5.300-12
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
- 5.300-7
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.300-6
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.300-5
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.300-4
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.300-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.300-1
✅ Initial packaging
