Version: 1.00
Release: 17%{?dist}
URL:     https://www.businesswire.com/news/home/20100608005491/en/Monotype-Imaging-Contributes-Simplified-Chinese-Font-%E2%80%9CMYuppy%E2%80%9D

%global foundry           Symbian
%global fontlicense       EPL-1.0

%global fontlicenses      *.TXT

%global fontfamily        M Yuppy GB
%global fontsummary       M Yuppy GB, a Chinese font family with a unique, modern feel
%global fonts             %{SOURCE0}
%global fontconfngs       %{SOURCE2}

%global fontdescription   %{expand:
Designed to appeal to young urban professionals, M Yuppy is a font family with
a unique, modern feel. The design combines elements of handwriting with classic
letter-form characteristics, such as open shapes and proper proportions that
help the typeface retain legibility.}

Source0: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium.ttf
Source1: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium_README.TXT
Source2: 65-%{fontpkgname}.xml

%fontpkg

%prep
%setup -q -c -T
cp %{SOURCE1} .
%linuxtext *TXT

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 1.00-11
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
- 1.00-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-1
✅ Initial packaging
