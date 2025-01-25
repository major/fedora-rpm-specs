# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/fonts-mukti

Version:   3.4.3
Release:   3%{?dist}

%forgemeta

URL: %{forgeurl}

Source0: %{forgesource}
Source1: https://github.com/mitradranirban/fbf-mukti-fonts/raw/main/SOURCES/66-0-fbf-mukti-fonts.conf

%global foundry fbf 
%global fontfamily    mukti         
%global fontlicense       GPL-3.0-or-later WITH Font-exception-2.0
%global fontlicenses      LICENCE 
%global fontdocs          README.md changelog
%global fontdocsex        %{fontlicenses}
%global fontsummary       Bangla open source Opentype font
%global fonts            *.otf
%global fontconfs        %{SOURCE1}
BuildRequires: fontforge 

%global fontdescription  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font 
made for Mukta Bangla Font project. It was  made by using good quality glyphs
 of GPLed font bng2-n from Cyberscape Multimedia
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>.
}

%fontpkg 

%prep
%forgesetup -v
chmod 755 generate.pe
./generate.pe *.sfd

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jan 23 2025 Akira TAGOH <tagoh@redhat.com> - 3.4.3-3
- Fix FTBFS issue
  Resolves: rhbz#2340152

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 3.4.3-1
- minor bugfix - correction of typo in conjunct lookup 

* Tue Nov 26 2024 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 3.4.2-1
- Added Missing .notdef glyf
- Added stylistic alternate of i-matra and ii-matra
- reinstated vertical fraction lookup mistakenly deleted from previous version

* Sun Jul 07 2024 13:01:00 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 3.1.0-1
- new upstream release 3.1.0
- family added italic and bold italic version 

* Tue Feb 13 2024 11:30:30 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.3-2
- changed global licence to SPDX license identifier - GPL-3.0-or-later WITH Font-exception-2.0

* Fri Feb 09 2024 21:22:41 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.3-1
- New upstream release 3.0.3
- Added few Bengali and Ahamiya Conjuncts 
- Few Minor Bugfixes 


* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild


* Sun Feb 06 2022 21:22:41 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.2-4
- corrected distag entry 
* Sun Feb 06 2022 14:42:41 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.2-3
- forgesource macro usage with updated source 

* Sun Feb 06 2022 06:10:33 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.2-2
- corrected typos

* Sat Feb 05 2022 22:56:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.2-1 
- bumped upstream to version 3.0.2 
- change docs and licence to match upstream
- removed forgemeta references 

* Fri Feb 04 2022 19:36:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-4
- Modified fontconfig 
- removed excess white spaces and tabs in spec file
- modified source line and fontcofig lines in spec 

* Thu Feb 03 2022 15:30:00 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-3
- Preparing fonts from source sfd files using fontforge as required in gpl
- collecting source from remote 

* Wed Feb 02 2022 21:30:16 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-2
- modification of spec file to remove unecessary elements 

* Fri Jan 28 2022 21:42:16 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-1
- Change in EM square from 2048 to 1000
- Upgrade fto Unicode 14.0 standard for Bengali
- shift from version 1 to version 2 of Bengali OpenType specification
- support for Assamese language
- support for both traditional and modern form of conjunts 
- addition of vedic stress marks
- removal of Latin glyphs
- removal of references and over lapping 
- addition of missing conjuncts 
- various bugfixes 
- Removed Bengali namespace error of double utf-8 encoding
- Created Mukti from MuktiNarrow 
- Converted splines from quadratic to cubic
- saved source in fontforge sfd format 
- removed microsoft volt tables from font

