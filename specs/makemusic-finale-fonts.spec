# The collection as a whole has no version number.  The individual fonts carry
# different version numbers.  Run `otfinfo -v` to see the version numbers.

Name:           makemusic-finale-fonts
Summary:        MakeMusic Finale fonts
License:        OFL-1.1
Version:        0
Release:        %autorelease
URL:            https://makemusic.zendesk.com/hc/en-us/articles/1500013053461-MakeMusic-Fonts-and-Licensing-Information

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

%global fontorg         com.makemusic

%global fontfamily1     Finale Ash
%global fontsummary1    Update of the handwritten Ash font
%global fontlicense1    OFL-1.1-RFN
%global fonts1          FinaleAsh.otf
%global fontconfs1      %{SOURCE2}
%global fontpkgheader1  %{expand:
Version:        1.7
}
%global fontdescription1 %{expand:
The Finale Ash font is a SMuFL-compliant, modern update to the
legendary, long-unavailable handwritten Ash font.  This font is artfully
crafted to represent the classic AshMusic font developed in 1996 for
Express Music Services, Inc. by Ashley Wells.}

%global fontfamily2     Finale Ash Text
%global fontsummary2    Text font designed to complement the Finale Ash font
%global fontlicense2    OFL-1.1-RFN
%global fonts2          FinaleAshText.otf
%global fontconfs2      %{SOURCE3}
%global fontpkgheader2  %{expand:
Version:        1.3
}
%global fontdescription2 %{expand:
The Finale Ash Text font is a SMuFL-compliant text font designed to
complement the Finale Ash music font.}

%global fontfamily3     Finale Broadway
%global fontsummary3    Update of the handwritten Broadway Copyist font
%global fontlicense3    OFL-1.1-RFN
%global fonts3          FinaleBroadway.otf
%global fontconfs3      %{SOURCE4}
%global fontpkgheader3  %{expand:
Version:        1.4
}
%global fontdescription3 %{expand:
The Finale Broadway font is the SMuFL-compliant version of Finale's
premiere handwritten Broadway Copyist legacy font.  In addition to the
characters from the Broadway Copyist font, this font also contains
Broadway Copyist Perc characters.}

%global fontfamily4     Finale Broadway Legacy Text
%global fontsummary4    Broadway Copyist Text and Text Ext fonts
%global fontlicense4    OFL-1.1-RFN
%global fonts4          FinaleBroadwayLegacyText.otf
%global fontconfs4      %{SOURCE5}
%global fontpkgheader4  %{expand:
Version:        1.1
}
%global fontdescription4 %{expand:
The Finale Broadway Legacy Text font is the SMuFL-compliant version of
the handwritten Broadway Copyist Text and Broadway Copyist Text Ext
fonts.  It emulates the look and feel of natural felt-tip print
handwriting.}

%global fontfamily5     Finale Broadway Text
%global fontsummary5    Finale Copyist Text and Text Ext fonts
%global fontlicense5    OFL-1.1-RFN
%global fonts5          FinaleBroadwayText.otf
%global fontconfs5      %{SOURCE6}
%global fontpkgheader5  %{expand:
Version:        1.1
}
%global fontdescription5 %{expand:
The Finale Broadway Text font is the SMuFL-compliant version of the
handwritten Finale Copyist Text and Finale Copyist Text Ext fonts.  This
font includes enclosures and basic notes and accidentals for creating
chord suffixes.}

%global fontfamily6     Finale Engraver
%global fontsummary6    Update of Bruce Nelson's Engraver font
%global fontlicense6    OFL-1.1-RFN
%global fonts6          FinaleEngraver.otf
%global fontconfs6      %{SOURCE7}
%global fontpkgheader6  %{expand:
Version:        1.4
}
%global fontdescription6 %{expand:
The Finale Engraver font is a SMuFL-compliant version of Bruce Nelson's
Engraver, EngraverFontExtras, and EngraverTime fonts.  This font set was
developed to meet the Music Publisher Association's music font design
specifications.  It includes a larger notehead with a different notehead
angle.  It also includes “Let Ring” noteheads, “Double-stopped unison”
noteheads, “Trill to” noteheads, “Tone-cluster” noteheads, variations on
dynamics and articulations, tempo markings, and harp pedaling symbols.}

%global fontfamily7     Finale Jazz
%global fontsummary7    Handwritten Jazz, JazzPerc, and JazzCord fonts
%global fontlicense7    OFL-1.1-RFN
%global fonts7          FinaleJazz.otf
%global fontconfs7      %{SOURCE8}
%global fontpkgheader7  %{expand:
Version:        1.9
}
%global fontdescription7 %{expand:
The Finale Jazz font is the SMuFL-compliant version of the handwritten
Jazz legacy font and also includes the legacy JazzPerc and JazzCord
fonts.}

%global fontfamily8     Finale Jazz Text
%global fontsummary8    Handwritten Jazz Text and Jazz Text Ext fonts
%global fontlicense8    OFL-1.1-RFN
%global fonts8          FinaleJazzText.otf
%global fontconfs8      %{SOURCE9}
%global fontpkgheader8  %{expand:
Version:        1.3
}
%global fontdescription8 %{expand:
The Finale Jazz Text font is the SMuFL-compliant version of the
handwritten Jazz Text and Jazz Text Ext legacy fonts.  This font
contains a full set of text and enclosures.}

%global fontfamily9     Finale Jazz Text Lowercase
%global fontsummary9    Lowercase versions of Finale Jazz Text
%global fontlicense9    OFL-1.1-RFN
%global fonts9          FinaleJazzTextLowercase.otf
%global fontconfs9      %{SOURCE10}
%global fontpkgheader9  %{expand:
Version:        1.4
}
%global fontdescription9 %{expand:
The Finale Jazz Text Lowercase font is a text font designed as an
extension to Finale Jazz Text and contains lowercase versions of the
alphabet characters, as opposed to the small caps characters contained
in Finale Jazz Text.}

%global fontfamily10    Finale Legacy
%global fontsummary10   The Petrucci, Seville and Tamburo fonts
%global fontlicense10   OFL-1.1-RFN
%global fonts10         FinaleLegacy.otf
%global fontconfs10     %{SOURCE11}
%global fontpkgheader10 %{expand:
Version:        1.6
}
%global fontdescription10 %{expand:
The Finale Legacy font is the SMuFL-compliant version of the Petrucci,
Seville and Tamburo fonts.

Named for the sixteenth-century Italian who first used movable type for
printing polyphonic music, Petrucci was the default music font for
Finale products for years but is now shipped for compatibility.

Seville was formerly the default font used for selecting fretboard
diagrams in Finale.

Named for the Italian term for drum, Tamburo is a font primarily
comprised of noteheads.  It contains a variety of symbols particularly
useful for percussion notation, including instrument noteheads and
several articulation marks.  Tamburo also includes a full set of symbols
for use in hymnal shape note music, where each note of the scale is
displayed with a unique notehead.  Moreover, Tamburo expands your
choice of accidentals for quarter-tone music.}

%global fontfamily11    Finale Lyrics
%global fontsummary11   Text font designed for optimal lyric spacing
%global fontlicense11   OFL-1.1
%global fonts11         FinaleLyrics*.otf
%global fontconfs11     %{SOURCE12}
%global fontpkgheader11 %{expand:
Version:        2.3
}
%global fontdescription11 %{expand:
The Finale Lyrics font contains standard text characters.  It was
designed specifically for optimal lyric spacing.}

%global fontfamily12    Finale Maestro
%global fontsummary12   Engraved music font
%global fontlicense12   OFL-1.1-RFN
%global fonts12         FinaleMaestro.otf
%global fontconfs12     %{SOURCE13}
%global fontpkgheader12 %{expand:
Version:        2.7
}
%global fontdescription12 %{expand:
The Finale Maestro font is a SMuFL-compliant update to Finale's classic
engraved default music font, Maestro.  This update looks similar to the
legacy Maestro font with the characters now mapped to the SMuFL
specification and minor updates added to some glyphs.  Additionally,
this single font now incorporates the characters from the Finale
AlphaNotes, Finale Mallets, Finale Percussion, Finale Numerics, Maestro
Percussion and Maestro Wide fonts.

The elegant Maestro font is more robust than the older Petrucci, and
more accurately represents the look of engraved music.

Created for use with beginning music students, the Finale AlphaNotes
font places note names inside noteheads.

The Finale Percussion font consists of pictogram glyphs that you can use
in your score to visually indicate individual percussion instruments.

The Finale Mallets font includes icons to represent any variety of
mallet usages, including the ability to create a cross-mallet symbol.
For example, you could use two 'zero-width' characters to indicate that
the performer should use two different mallets in one hand.

The Finale Numerics font includes all the characters you need to create
harmonic analysis and figured bass.  Zero-width characters allow you to
stack characters easily.}

%global fontfamily13    Finale Maestro Text
%global fontsummary13   A Times font for lyrics
%global fontlicense13   OFL-1.1-RFN
%global fonts13         FinaleMaestroText*.otf
%global fontconfs13     %{SOURCE14}
%global fontpkgheader13 %{expand:
Version:        1.6
}
%global fontdescription13 %{expand:
The Finale Maestro Text font is the SMuFL-compliant version of the
MaestroTimes font.  This includes Regular, Italic, Bold and Bold
Italic.}

Source0:        https://makemusic.zendesk.com/hc/en-us/article_attachments/4586784089367/MMFonts.msi
Source1:        https://makemusic.zendesk.com/hc/en-us/article_attachments/4402710909975/OFL.txt
Source2:        65-%{fontpkgname1}.conf
Source3:        65-%{fontpkgname2}.conf
Source4:        65-%{fontpkgname3}.conf
Source5:        65-%{fontpkgname4}.conf
Source6:        65-%{fontpkgname5}.conf
Source7:        65-%{fontpkgname6}.conf
Source8:        65-%{fontpkgname7}.conf
Source9:        65-%{fontpkgname8}.conf
Source10:       65-%{fontpkgname9}.conf
Source11:       65-%{fontpkgname10}.conf
Source12:       65-%{fontpkgname11}.conf
Source13:       65-%{fontpkgname12}.conf
Source14:       65-%{fontpkgname13}.conf

BuildRequires:  msitools

%description
This package contains the OpenType fonts delivered with the Finale music
notation system.

%fontpkg -a

%prep
%setup -q -c -T

%conf
msiextract %{SOURCE0}
cp -p %{SOURCE1} .
%linuxtext -n OFL.txt

%build
%fontbuild -a

%install
%fontinstall -a -l OFL.txt

# Install SMuFL metadata
for font in 'Finale Ash' 'Finale Ash Text' 'Finale Broadway' \
    'Finale Broadway Legacy Text' 'Finale Broadway Text' 'Finale Engraver' \
    'Finale Jazz' 'Finale Jazz Text' 'Finale Jazz Text Lowercase' \
    'Finale Legacy' 'Finale Maestro' 'Finale Maestro Text' \
    'Finale Maestro Text Bold' 'Finale Maestro Text Bold Italic' \
    'Finale Maestro Text Italic'; do
  mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/"$font"
  install -p -m 0644 "SMuFL/Fonts/ $font/$font.json" \
    %{buildroot}%{_datadir}/SMuFL/Fonts/"$font"
  ln -s "$font.json" %{buildroot}%{_datadir}/SMuFL/Fonts/"$font"/metadata.json
done

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,updatecontact,update_contact,g;s,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -i $(ls -1d %{buildroot}%{_metainfodir}/%{fontorg}.*.xml)

%check
%fontcheck -a

%fontfiles -z 1
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Ash/"

%fontfiles -z 2
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Ash Text/"

%fontfiles -z 3
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Broadway/"

%fontfiles -z 4
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Broadway Legacy Text/"

%fontfiles -z 5
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Broadway Text/"

%fontfiles -z 6
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Engraver/"

%fontfiles -z 7
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Jazz/"

%fontfiles -z 8
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Jazz Text/"

%fontfiles -z 9
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Jazz Text Lowercase/"

%fontfiles -z 10
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Legacy/"

%fontfiles -z 11

%fontfiles -z 12
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Maestro/"

%fontfiles -z 13
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
"%{_datadir}/SMuFL/Fonts/Finale Maestro Text/"
"%{_datadir}/SMuFL/Fonts/Finale Maestro Text Bold/"
"%{_datadir}/SMuFL/Fonts/Finale Maestro Text Bold Italic/"
"%{_datadir}/SMuFL/Fonts/Finale Maestro Text Italic/"

%changelog
%autochangelog
