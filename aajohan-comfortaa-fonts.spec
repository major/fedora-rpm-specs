Version:        3.101
Release:        5%{?dist}
URL:            https://www.deviantart.com/aajohan

%global foundry           Aajohan
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt DESCRIPTION.en_us.html README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Comfortaa
%global fontsummary       Modern style true type font
%global fonts             fonts/OTF/*.otf fonts/TTF/*.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Comfortaa is a sans-serif font comfortable in every aspect with
Bold, Regular, and Thin variants.
It has very good European language coverage and decent Cyrillic coverage.}

Source0:        https://github.com/googlefonts/comfortaa/archive/%{version}%{?prerelease}/%{name}-%{version}%{?prerelease}.tar.gz
Source1:        61-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -n comfortaa-%{version}
chmod 644 AUTHORS.txt CONTRIBUTORS.txt
%linuxtext FONTLOG.txt OFL.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Parag Nemade <pnemade@fedoraproject.org> - 3.101-3
- Convert this package to new fonts packaging guidelines

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 1 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.101-1
- Update to 3.101
- New source url
- Resolves rhbz#1966444
- Resolves rhbz#1966659

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 3.001-1
- Update to 3.001

- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.004-4
- Add metainfo file to show this font in gnome-software

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 2.004-1
- Latest upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Luya Tshimbalanga <luya@fedoraproject.org> - 2.003-1
- Upstream update (rhbz#786442)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Luya Tshimbalanga <luya@fedoraproject.org> - 2.002-5
- Upstream update (rhbz#771541)
- Spec cleaned up
- updated filename documentation

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 3 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.004-1
- Upstream update rhbz#658745

* Thu Sep 23 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-5.1
- Changed to the correct description rhbz#636987

* Tue Aug 3 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-4
- Set the right close tag inside 61 conf file

* Fri Jul 30 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-3
- Added missing documentations
- Switched to the right versioning
- Addressed wrong-file-end-of-line-encoding issue

* Thu Jul 29 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-2
- Set prefix to 61 for fontconfig.conf
- Shortened description
- Some fixes

* Tue Jul 27 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-1
- Initial RPM release.
