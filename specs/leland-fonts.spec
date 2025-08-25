%global giturl  https://github.com/MuseScoreFonts/Leland

Version:        0.79
Release:        %autorelease
URL:            https://musescore.org/
VCS:            git:%{giturl}.git

%global fontorg         org.musescore
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    LICENSE.txt OFL-FAQ.txt
%global fontdocs        FONTLOG.txt README.md

%global _desc %{expand:
The Leland music fonts (Leland & Leland Text) were initially developed
for the MuseScore (https://www.musescore.org) music composition
software.

Leland is compliant with Standard Music Font Layout (SMuFL), which
provides a standard way of mapping the thousands of musical symbols
required by conventional music notation into the Private Use Area in
Unicode's Basic Multilingual Plane for a single (format-independent)
font.

The font is named after Leland Smith, creator of the SCORE music
notation software.}

%global fontfamily0     Leland
%global fontsummary0    SMuFL-compliant OpenType music font
%global fontpkgheader1  %{expand:
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-leland-fonts < 4.0
Provides:       mscore-leland-fonts = 1:%{version}-%{release}
}
%global fonts0          Leland.otf
%global fontconfs0      %{SOURCE1}
%global fontdescription0 %{expand:%_desc

This package contains the music font.}

%global fontfamily1     Leland Text
%global fontsummary1    Text font to complement Leland
%global fonts1          LelandText.otf
%global fontconfs1      %{SOURCE2}
%global fontdescription1 %{expand:%_desc

This package contains the text font.}

Source0:        %{giturl}/archive/v%{version}/Leland-%{version}.tar.gz
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  fonts-rpm-macros

%fontpkg -a
%fontmetapkg

%prep
%autosetup -n Leland-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

# Install SMuFL metadata
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/Leland
install -p -m 0644 leland_metadata.json \
  %{buildroot}%{_datadir}/SMuFL/Fonts/Leland/metadata.json
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/Leland/Leland.json

# Fix invalid metadata; see bz 1943727
for name in leland leland-text; do
  sed -e 's,updatecontact,update_contact,g' \
      -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
      -e 's,\(MuseScore\) (\(https://www.musescore.org\)),<a href="\2">\1</a>,' \
      -e 's,&,&amp;,' \
      -i %{buildroot}%{_metainfodir}/%{fontorg}.${name}-fonts.metainfo.xml
done

%check
%fontcheck -a

%fontfiles -z 0
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/Leland/

%fontfiles -z 1

%changelog
%autochangelog
