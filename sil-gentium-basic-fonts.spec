# SPDX-License-Identifier: MIT
Version: 1.102
Release: 5%{?dist}
URL:     https://software.sil.org/gentium/

%global foundry           SIL
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt

%global common_description %{expand:
Gentium Basic and Gentium Book Basic are font families based on the
original Gentium design, but with additional weights. Both families come
with a complete regular, bold, italic and bold italic set of fonts.
These "Basic" fonts support only the Basic Latin and Latin-1 Supplement
Unicode ranges, plus a selection of the more commonly used extended Latin
characters, with miscellaneous diacritical marks, symbols and punctuation.
}

%global fontfamily0       Gentium Basic
%global fontsummary0      SIL Gentium Basic font family
%global fontpkgheader0    %{expand:
Obsoletes: sil-gentium-basic-fonts-common < %{version}-%{release}
}
%global fonts0            GenBas*
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This is the base variant.}

%global fontfamily2       Gentium Basic Book
%global fontsummary2      SIL Gentium Book Basic font family
%global fonts2            GenBkBas*
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%global fontpkgname2       sil-gentium-basic-book-fonts
%{common_description}

The "Book" family is slightly heavier.}


%global archivename GentiumBasic_1102

Source0:   https://software.sil.org/downloads/r/gentium/%{archivename}.zip
Source10:  59-%{fontpkgname}.conf
Source12:  59-%{fontpkgname2}.conf


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
%doc FONTLOG.txt GENTIUM-FAQ.txt OFL-FAQ.txt

%changelog
* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.102-5
- SPDX migration

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 13 2021 Michael J. Gruber <mjg@fedoraproject.org> - 1.102-1
- rebase with upstream 1.102
- switch to current fonts rpm macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 21 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.1-12
- Add metainfo file to show this font in gnome-software
- Remove duplicate dir %%{_fontdir}
- Clean the spec to follow current packaging guidelines

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Michael J Gruber <mjg@fedoraproject.org> - 1.1-7
- spec file clean up.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 <b.rahul.pm@gmail.com> - 1.1-3.fc11
- Changed the naming for srpm.

* Wed Jan 28 2009 <b.rahul.pm@gmail.com> - 1.1-2.fc11
- Changes according to package naming guidelines post-1.13  fontpackages.

* Tue Jan 06 2009 <b.rahul.pm@gmail.com> - 1.1-1.fc11
- Following new packaging guidelines.
