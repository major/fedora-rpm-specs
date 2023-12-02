%global commit		2a87ac6f6ea3495150bfa00d0c0fb53dd0a2f11b
%global shortcommit 	%(c=%{commit}; echo ${c:0:7})
%global date		20210729
Version:        3.105
Release:        %autorelease %{?shortcommit: -p -s %{date}git%{shortcommit}}
URL:            https://www.deviantart.com/aajohan

%global foundry           Aajohan
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt DESCRIPTION.en_us.html README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Comfortaa
%global fontsummary       Modern style true type font
%global fonts             fonts/OTF/*.otf fonts/otf/*otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Comfortaa is a sans-serif font comfortable in every aspect with
Bold, Regular, and Thin variants.
It has very good European language coverage and decent Cyrillic coverage.}

%{?shortcommit:
Source0:        https://github.com/googlefonts/comfortaa/archive/%{shortcommit}/comfortaa-%{shortcommit}.tar.gz}
%{!?shortcommit:
Source0:        https://github.com/googlefonts/comfortaa/archive/%{version}/comfortaa-%{version}.tar.gz}
Source1:        61-%{fontpkgname}.conf

%fontpkg

%prep
%{?shortcommit:
%autosetup -n comfortaa-%{commit} }
%{!?shortcommit:
%autosetup -n comfortaa-%{version}
}
%linuxtext OFL.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
