%global giturl  https://github.com/MuseScoreFonts/Edwin

Version:        0.54
Release:        %autorelease
URL:            https://musescore.org/
VCS:            git:%{giturl}.git

%global fontorg         org.musescore
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    LICENSE.txt OFL-FAQ.txt
%global fontdocs        FONTLOG.txt README.md
%global fontfamily      Edwin
%global fontsummary     A text font for musical scores
%global fonts           *.otf
%global fontconfs       %{SOURCE1}
%global fontdescription %{expand:In 1999-2000, URW++ Design and Development GmbH released Type 1
implementations of the Core 35 fonts under the GNU General Public License
(GPL) and the Aladdin Ghostscript Free Public License (AFPL).  In 2009, URW++
additionally released the same fonts under the LaTeX Project Public License
(LPPL).

In 2016, URW++ released a major Version 2.0 upgrade to the Core 35 fonts.
This version is an extensive reworking of the original Core 35 fonts, with
improved font outlines, and greatly extended character sets, including
Cyrillic and Greek.  Also, some font names were changed.  Version 2.0 was
released in Type 1, OpenType-CFF and OpenType-TTF formats.  URW++ released
Version 2.0 of the fonts under the GNU Affero General Public License, Version
3 (AGPL) with an exemption.

In 2017, URW++ additionally released the same Version 2.0 fonts under the
LaTeX Project Public License (LPPL) Version 1.3c, and under the SIL Open Font
License (OFL), Version 1.1, without a "Reserved Font Name" clause.

In 2020, MuseScore BVBA released the Edwin font family, a renamed version of
the C059 font family (Roman, Italic, Bold & Bold Italic) from the Core 35 font
set.  This was done in order to make modifications that suit the requirements
of the open source notation software, MuseScore.  It is released under the SIL
Open Font License (OFL) only.}
%global fontpkgheader   %{expand:
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-edwin-fonts < 4.0
Provides:       mscore-edwin-fonts = 1:%{version}-%{release}
}

Source0:        %{giturl}/archive/v%{version}/Edwin-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  fonts-rpm-macros

%fontpkg

%prep
%autosetup -n Edwin-%{version}

%build
%fontbuild

%install
%fontinstall

# Fix the metainfo; see bz 1943727
sed -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -e 's,&,&amp;,' \
    -i %{buildroot}%{_metainfodir}/%{fontorg}.edwin-fonts.metainfo.xml

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
