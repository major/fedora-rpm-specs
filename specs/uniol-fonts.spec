# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/font-uniol
Version:   2.001
Release:   1%{?dist}
%forgemeta
URL: %{forgeurl}
%global fontfamily    uniol
%global fontlicense       OFL
%global fontlicenses      Licence
%global fontdocs       README.md
%global fontdocsex        %{fontlicenses}
%global fontsummary       Unicode compliant Open source Ol Chiki font
%global fonts            *.ttf
%global fontconfs        66-0-%{fontpkgname}.conf
BuildRequires: fontforge

%global fontdescription  %{expand:
 This is an Unicode compliant OlChiki or OlCemet font.
 OlChiki is a modern alphabetic script used to write Santhali
  language used in various states of India.
}

Source0: %{forgesource}

%fontpkg

%prep
%forgesetup

%build
chmod 755 generate.pe
./generate.pe *.sfd

%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Jun 13 2025 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 2.001-2
- updated Licence file details
* Fri Jun 13 2025 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 2.001-1
- Added Bold, Italic and Bold Italic
- Added GPOS table
- Modified punctuation characters

