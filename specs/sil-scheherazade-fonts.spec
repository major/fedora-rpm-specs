%global projectname       scheherazade
BuildArch: noarch

Version:    3.300
Release:    6%{?dist}
URL:        https://software.sil.org/%{projectname}/

%global foundry           SIL
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          FONTLOG.txt README.txt OFL-FAQ.txt documentation/*
%global fontdocsex        %{fontlicenses}

%global fontfamily1        Scheherazade New
%global fontsummary1       An Arabic script unicode font
%global fontpkgheader1    %{expand:
Provides: sil-scheherazade-fonts = %{version}-%{release}
Obsoletes: sil-scheherazade-fonts < %{version}-%{release}
}
%global fonts1             *.ttf
%global fontconfs1         %{SOURCE1}
%global fontdescription1   %{expand:
Scheherazade, named after the heroine of the classic Arabian Nights tale, is
designed in a similar style to traditional typefaces such as Monotype Naskh,
extended to cover the full Unicode Arabic repertoire.
}

Source0:    https://software.sil.org/downloads/r/scheherazade/ScheherazadeNew-%{version}.zip
Source1:    65-%{fontpkgname1}.conf

Name:       sil-scheherazade-fonts
Summary:    An Arabic script unicode font 
License:    OFL-1.1

%description
%wordwrap -v common_description

%fontpkg -a

%prep
%setup -q -n ScheherazadeNew-%{version}
rm -rf documentation/source documentation/pdf
%linuxtext FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt documentation/DOCUMENTATION.txt documentation/assets/css/*

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.300-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.300-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.300-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.300-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Paul Whalen <pwhalen@fedoraproject.org> - 3.300-2
- Fix Obsoletes, add Provides

* Sat Sep 03 2022 Parag Nemade <pnemade AT redhat DOT com> - 3.300-1
- Convert spec to new fonts packaging guidelines
- Update to new upstream release 3.300
- Upstream renamed font family to "Scheherazade New"

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Akira TAGOH <tagoh@redhat.com> - 2.100-7
- Update URL.
- Modernize the spec file.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 10 2015 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.100-1
- Update to upstream version 2.100

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.020-3
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.020-1
- Update to 2.020 upstream release with bug fixes

* Mon Sep 16 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.010-1
- Update to upstream bugfix release 010

* Sun Aug 18 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.000-1
- Update to version 2.000

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 16 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.005-3
- Fix fontconfig test tag to use 'compare' rather than 'mode' which is the
  correct keyword

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.005-1
- Updated to 1.005 upstream version
- Removed some deprecated entries (like cleaning buildroot)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 01 2010 Hedayat Vatankhah <hedayat@grad.com> - 1.001-3
- Scaled the font (1.2 times bigger) to make it more like other fonts

* Sat Oct 03 2009 Hedayat Vatankhah <hedayat@grad.com> - 1.001-2
- Fixed summary to not include font name
- Removed some parts of the description
- Added fontconfig rules

* Mon Sep 28 2009 Hedayat Vatankhah <hedayat@grad.com> - 1.001-1
- Initial version
