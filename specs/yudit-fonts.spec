# SPDX-License-Identifqier: MIT
%global forgeurl https://gitlab.com/mitradranirban/yudit-fonts
Version: 1.4
Release: %autorelease

%global fontfamily yudit
%global fontsummary   A Latin and Old Hungarian Rovasiras Font
%global fontlicense       GPL-2.0-only
%global fontlicenses      LICENCE
%global fontdocs          *.TXT *.txt
%global fonts                      *.ttf
%global fontconfs          61-1-yudit-fonts.conf
%forgemeta 
URL:  %forgeurl
VCS: git:%{forgeurl}.git
BuildRequires: fontforge
BuildRequires: fonts-rpm-macros  
%global fontdescription  %{expand:
Yudit is the default font bundled with Yudit Unicode editor. It contains 
Latin with Old Hungarian Rovasiras glyphs with custom encodings. 
}
Source0: %forgesource

%fontpkg

%prep
%forgesetup 
%linuxtext -n README.TXT

%build
./generate.pe *.sfd
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog

%autochangelog 
