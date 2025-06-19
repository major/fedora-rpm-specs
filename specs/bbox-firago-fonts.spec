Version: 1.001
Release: 3%{?dist}
URL:     https://carrois.com/fira/

%global version_nodots %{gsub %{version} %. %{quote:}}

%global foundry           BBOX
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt

%global fontfamily        FiraGO
%global fontsummary       An independent Open Source typeface

%global fonts             Fonts/FiraGO_OTF_%{version_nodots}/*/*.otf
%global fontconfs         %{SOURCE2}

%global fontdescription   %{expand:
Based on the Fira Sans 4.3 glyph set, FiraGO now supports Arabic, Devanagari,
Georgian, Hebrew and Thai. With this script support, FiraGO catches up with
other globally extended and free typefaces such as Noto.
}

Source0:  https://carrois.com/downloads/FiraGO/Download_Folder_FiraGO_%{version_nodots}.zip
Source1:  https://carrois.com/downloads/FiraGO/OFL.txt
Source2:  60-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -n Download_Folder_FiraGO_%{version_nodots} -a 0
cp %{SOURCE1} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sat Jun 14 2025 Mateus Rodrigues Costa <mateusrodcosta@gmail.com> - 1.001-3
- Rename package with foundry prefix: bbox-firago-fonts
- Change URLs to point to new foundry website: https://carrois.com/

* Sun May 11 2025 Mateus Rodrigues Costa <mateusrodcosta@gmail.com> - 1.001-2
- Package license file
- Tweak fontconfig ruleset prefix

* Thu Apr 17 2025 Mateus Rodrigues Costa <mateusrodcosta@gmail.com> - 1.001-1
- Initial packaging attempt
