Version:        3.101
Release:        %autorelease
URL:            https://www.deviantart.com/aajohan

%global foundry           Aajohan
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt DESCRIPTION.en_us.html README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Comfortaa
%global fontsummary       Modern style true type font
%global fonts             fonts/OTF/*.otf
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
%autochangelog
