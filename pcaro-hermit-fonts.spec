# SPDX-License-Identifier: MIT
Version:        2.0
Release:        %autorelease
URL:            https://pcaro.es/p/hermit

%global foundry		pcaro	
%global	fontlicense	OFL

%global	fontfamily	Hermit
%global	fontsummary	Hermit monospace fonts
%global	fonts		*.otf
%global	fontconfngs	%{SOURCE10}
%global fontdescription	%{expand:
Hermit is a monospace font designed to be clear, pragmatic and very readable.
Its creation has been focused on programming. Every glyph was carefully planned
and calculated, according to defined principles and rules. For this reason,
Hermit is coherent and regular.}

Source0:	https://pcaro.es/d/otf-hermit-%{version}.tar.gz
Source10:	60-%{fontpkgname}.xml

%fontpkg

%prep
%setup -q -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
