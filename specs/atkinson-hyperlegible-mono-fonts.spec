# SPDX-License-Identifier: MIT

%global commit           154d50362016cc3e873eb21d242cd0772384c8f9
%global shortcommit      %{sub %{commit} 1 7}
%global commitdate       20241120
%global fontname         atkinson-hyperlegible-mono

%global fontdescription %{expand:
Atkinson Hyperlegible Mono is an entirely new typeface inspired by the Atkinson
Hyperlegible font. The monospaced font features characters that each occupy the
same amount of horizontal space, allowing for them to be scanned quickly in
table-based and coding environments.
}


Version:        2.100
Release:        %autorelease
URL:            https://www.brailleinstitute.org/freefont/

Source0:        https://github.com/googlefonts/atkinson-hyperlegible-mono/archive/%{shortcommit}.tar.gz
Source1:        64-%{fontname}.xml

BuildRequires:  fontpackages-devel

%global fontfamily      Atkinson Hyperlegible Mono
%global fontsummary     Monospace typeface made for low-vision legibility
%global fontlicense     OFL-1.1
%global fontlicenses    OFL.txt
%global fontdocs        DESCRIPTION.en_us.html
%global fonts           fonts/otf/*.otf
%global fontconfs       %{SOURCE1}

%fontpkg


%prep
%setup -n atkinson-hyperlegible-next-mono-%{commit}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
