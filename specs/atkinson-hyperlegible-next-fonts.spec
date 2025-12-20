# SPDX-License-Identifier: MIT

%global commit           7925f50f649b3813257faf2f4c0b381011f434f1
%global shortcommit      %{sub %{commit} 1 7}
%global commitdate       20250222
%global fontname         atkinson-hyperlegible-next

%global fontdescription %{expand:
Atkinson Hyperlegible is a uniquely accessible typeface created by Braille
Institute of America. It has been developed specifically to increase legibility
for readers with low vision, and to improve comprehension.

Atkinson Hyperlegible Next, a refined version of Atkinson Hyperlegible,
improves on the original in every way. It features new weights, improved
kerning, refined curves, added symbols, and additional language support.
}


Version:        2.100
Release:        %autorelease
URL:            https://www.brailleinstitute.org/freefont/

Source0:        https://github.com/googlefonts/%{fontname}/archive/%{shortcommit}.tar.gz
Source1:        64-%{fontname}.xml

BuildRequires:  fontpackages-devel

%global fontfamily      Atkinson Hyperlegible Next
%global fontsummary     Second-gen font family made for low-vision legibility
%global fontlicense     OFL-1.1
%global fontlicenses    OFL.txt
%global fontdocs        DESCRIPTION.en_us.html
%global fonts           fonts/otf/*.otf
%global fontconfs       %{SOURCE1}

%fontpkg


%prep
%setup -n %{fontname}-%{commit}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
