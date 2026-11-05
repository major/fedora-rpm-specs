# SPDX-License-Identifier: MIT
%global  forgeurl https://github.com/SorkinType/Agbalumo/
%global  commit       261ad51ef2291821685c1bebf10cf0fb9f7e08f9
%global  shortcommit  261ad51
%global  commitdate   20250605
%global  version0     1.00


Version: %{version0}
Release: %{autorelease}
URL: %{forgeurl}
VCS: git:%{url}.git
 
%global foundry       columntype
%global fontlicense   OFL-1.1
%global fontlicenses  OFL.txt
%global fontdocs      DESCRIPTION.en_us.html
%global fontdocsex    %{fontlicenses}
 
%global common_description  %{expand:
Curvy, chunky, and compact. The Agbalumo display typeface has been designed to
represent and capture the beauty of African languages. Primarily taking shape
from the use of a brush pen, it's charming, playful, and cute look lends
itself to a variety of commercial and cultural use cases.

Agbalumo is a single weight multilingual font. The glyph set includes standard
opentype features and an assortment of stylistic alternates. Agbalumo can be
used for African languages that make use of the Latin script, the Ge'ez script,
European languages, and Vietnamese.}

%global fontfamily       Agbalumo
%global fontsummary      Agbalumo regular display typeface
%global fonts            fonts/ttf/Agbalumo-Regular.ttf
%global fontconfs        %{SOURCE10}
%global fontdescription  %{expand:
%{common_description}
Regular fonts.}

Source0:  %{forgeurl}/archive/%{commit}/agbalumo-%{commit}.tar.gz
Source10: 67-%{fontpkgname}.conf


%fontpkg

 
%prep
%autosetup -n Agbalumo-%{commit}

%build
%fontbuild
 
%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
