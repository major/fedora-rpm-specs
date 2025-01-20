# SPDX-License-Identifier: MIT
Version: 20141121
Release: 30%{?dist}
# https://company.paratype.com/pt-sans-pt-serif
URL:     http://www.paratype.com/public/

%global foundry           PT
%global fontlicense       OFL-1.1
%global fontlicenses      PTSSM_OFL.txt

%global fontfamily        PT Sans
%global fontsummary       PT Sans, a grotesque pan-Cyrillic font family
%global fontpkgheader     %{expand:
Obsoletes: paratype-pt-sans-fonts         <= %{version}-%{release}
Obsoletes: paratype-pt-sans-caption-fonts <= %{version}-%{release}
}
%global fonts             PTS*.ttf PTN*.ttf PTC*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The PT Sans family was developed as part of the “Public Types of Russian
Federation” project. This project aims at enabling the peoples of Russia to
read and write their native languages, using free/libre fonts. It is
dedicated to the 300-year anniversary of the Russian civil type invented by
Peter the Great from 1708 to 1710, and was realized with financial support
from the Russian Federal Agency for Press and Mass Communications.

The fonts include support for all 54 ethnic languages of the Russian
Federation as well as more common Western, Central European and Cyrillic
blocks making them unique and a very important tool for modern digital
communications.

PT Sans is a grotesque font family based on Russian type designs of the second
part of the 20th century. However, it also includes very distinctive features
of modern humanistic design, fulfilling present day aesthetic and functional
requirements.

It was designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov
and released by ParaType.}

# This is now dead and ParaType still publishes an older version on its website
Source0:  http://www.fontstock.com/public/PTSansOFL.zip
Source10: 58-%{fontpkgname}.xml
Source20: http://rus.paratype.ru/system/attachments/647/original/ptsans55reg.pdf
Source21: http://rus.paratype.ru/system/attachments/650/original/ptsans75bold.pdf
Source22: http://rus.paratype.ru/system/attachments/648/original/ptsans56it.pdf
Source23: http://rus.paratype.ru/system/attachments/651/original/ptsans76bit.pdf
Source24: http://rus.paratype.ru/system/attachments/652/original/ptsanscaption55.pdf
Source25: http://rus.paratype.ru/system/attachments/653/original/ptsanscaption57bold.pdf
Source26: http://rus.paratype.ru/system/attachments/649/original/ptsans57narrow.pdf
Source27: http://rus.paratype.ru/system/attachments/655/original/ptsans77narrowbold.pdf

%fontpkg

%package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.


%prep
%setup -q -c
%linuxtext *.txt
install -m 0644 -vp %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} \
                    %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license PTSSM_OFL.txt
%doc *.pdf

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 27 2024 Parag Nemade <pnemade AT redhat DOT com> - 20141121-28
- Migrate to SPDX license expression

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Jens Petersen <petersen@redhat.com> - 20141121-25
- drop the legacy compat package (#2054527)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Parag Nemade <pnemade AT redhat DOT com>
- 20141121-18
- Fix this spec file to build for F33+

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20141121-16
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20141121-15
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20141121-14
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Thu Mar 26 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20141121-13
✅ Add compatibility packages

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20141121-12
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20141121-11
✅ Convert to fonts-rpm-macros use
✅ Include caption in sans: it's an optical sizing variant
✅ PT is the foundry identifier; drop it

* Sun Jan 17 2010 Nicolas Mailhot <nim@fedoraproject.org>
- 20100112-1
✅ Initial packaging
