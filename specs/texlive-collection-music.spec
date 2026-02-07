%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-music
Epoch:          12
Version:        svn76267
Release:        1%{?dist}
Summary:        Music packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-music.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abc.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/abc.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bagpipe.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bagpipe.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbars.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbars.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbox.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chordbox.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ddphonism.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ddphonism.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figbas.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/figbas.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fretplot.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fretplot.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gchords.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gchords.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtrcrd.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gtrcrd.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitar.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitar.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitarchordschemes.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitarchordschemes.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitartabs.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guitartabs.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harmony.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/harmony.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4musicians.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4musicians.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/leadsheets.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/leadsheets.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liederbuch.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/liederbuch.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musical.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musical.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musicography.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musicography.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixguit.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixguit.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtex-fonts.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtex-fonts.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/octave.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/octave.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piano.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piano.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/recorder-fingering.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/recorder-fingering.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songbook.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songbook.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songproj.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songproj.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songs.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/songs.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undar-digitacion.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undar-digitacion.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpiano.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpiano.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-abc
Requires:       texlive-autosp
Requires:       texlive-bagpipe
Requires:       texlive-chordbars
Requires:       texlive-chordbox
Requires:       texlive-collection-latex
Requires:       texlive-ddphonism
Requires:       texlive-figbas
Requires:       texlive-fretplot
Requires:       texlive-gchords
Requires:       texlive-gregoriotex
Requires:       texlive-gtrcrd
Requires:       texlive-guitar
Requires:       texlive-guitarchordschemes
Requires:       texlive-guitartabs
Requires:       texlive-harmony
Requires:       texlive-latex4musicians
Requires:       texlive-leadsheets
Requires:       texlive-liederbuch
Requires:       texlive-lilyglyphs
Requires:       texlive-lyluatex
Requires:       texlive-m-tx
Requires:       texlive-musical
Requires:       texlive-musicography
Requires:       texlive-musixguit
Requires:       texlive-musixtex
Requires:       texlive-musixtex-fonts
Requires:       texlive-musixtnt
Requires:       texlive-octave
Requires:       texlive-piano
Requires:       texlive-pmx
Requires:       texlive-pmxchords
Requires:       texlive-recorder-fingering
Requires:       texlive-songbook
Requires:       texlive-songproj
Requires:       texlive-songs
Requires:       texlive-undar-digitacion
Requires:       texlive-xml2pmx
Requires:       texlive-xpiano

%description
Music-related fonts and packages.


%package -n texlive-abc
Summary:        Support ABC music notation in LaTeX
Version:        svn41157
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(abc.sty) = %{tl_version}
Provides:       tex(mup.sty) = %{tl_version}

%description -n texlive-abc
The abc package lets you include lines of music written in the ABC Plus
language. The package will then employ the \write18 facility to convert your
notation to PostScript (using the established utility abcm2ps) and hence to the
format needed for inclusion in your document.

%package -n texlive-bagpipe
Summary:        Support for typesetting bagpipe music
Version:        svn34393
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bagpipe.tex) = %{tl_version}

%description -n texlive-bagpipe
Typesetting bagpipe music in MusixTeX is needlessly tedious. This package
provides specialized and re-defined macros to simplify this task.

%package -n texlive-chordbars
Summary:        Print chord grids for pop/jazz tunes
Version:        svn70392
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(relsize.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-euclide.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(chordbars.sty) = %{tl_version}

%description -n texlive-chordbars
This Tikz-based music-related package is targeted at pop/jazz guitar/bass/piano
musicians. They usually need only the chords and the song structure. This
package produces rectangular song patterns with "one square per bar", with the
chord shown inside the square. It also handles the song structure by showing
the bar count and the repetitions of the patterns.

%package -n texlive-chordbox
Summary:        Draw chord diagrams
Version:        svn51000
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xstring.sty)
Provides:       tex(chordbox.sty) = %{tl_version}

%description -n texlive-chordbox
This package provides two macros for drawing chord diagrams, as may be found
for example in chord charts/books and educational materials. They are composed
as TikZ pictures and have several options to modify their appearance.

%package -n texlive-ddphonism
Summary:        Dodecaphonic diagrams: twelve-tone matrices, clock diagrams, etc.
Version:        svn75201
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(ddphonism.sty) = %{tl_version}

%description -n texlive-ddphonism
This music-related package focuses on notation from the Twelve-Tone System,
also called Dodecaphonism. It provides LaTeX algorithms to generate common
dodecaphonic diagrams based off a musical series, or row sequence, of arbitrary
length. The package requires TikZ.

%package -n texlive-figbas
Summary:        Mini-fonts for figured-bass notation in music
Version:        svn28943
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-figbas
This package consists of three mini-fonts (and associated metrics) of
conventional ligatures for the figured-bass notations 2+, 4+, 5+, 6+ and 9+ in
music manuscripts. The fonts are usable with Computer Modern Roman and Sans,
and Palatino/Palladio, respectively.

%package -n texlive-fretplot
Summary:        Create scale and chord diagrams for guitar-like instruments
Version:        svn76337
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(fretplot.sty) = %{tl_version}

%description -n texlive-fretplot
This LuaLaTeX package provides batch generation of scale and chord diagrams for
plucked string instruments, such as the guitar. Flexible and Automated: Highly
customizable and automatable via simple, powerful file formats for describing
fretboard diagrams. Easily generate batches of diagrams. Attractive Defaults:
Comes with sensible, visually appealing default settings. Music Theory Aware:
Includes easy-to-use LaTeX macros that understand music theory. Render guitar
scale diagrams by specifying the musical scale or scale type via built-in
macros or directly via degree, pitch class, or interval formulae.

%package -n texlive-gchords
Summary:        Typeset guitar chords
Version:        svn29803
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gchords.sty) = %{tl_version}

%description -n texlive-gchords
A LaTeX package for typesetting of guitar chord diagrams, including options for
chord names, finger numbers and typesetting above lyrics. The bundle also
includes a TCL script (chordbox.tcl) that provides a graphical application
which creates LaTeX files that use gchords.sty.

%package -n texlive-gtrcrd
Summary:        Add chords to lyrics
Version:        svn32484
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(gtrcrd.sty) = %{tl_version}

%description -n texlive-gtrcrd
The package provides the means to specify guitar chords to be played with each
part of the lyrics of a song. The syntax of the macros reduces the chance of
failing to provide a chord where one is needed, and the structure of the macros
ensures that the chord specification appears immediately above the start of the
lyric.

%package -n texlive-guitar
Summary:        Guitar chords and song texts
Version:        svn32258
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(toolbox.sty)
Provides:       tex(guitar.sty) = %{tl_version}

%description -n texlive-guitar
(La)TeX macros for typesetting guitar chords over song texts. The toolbox
package is required. Note that this package only places arbitrary TeX code over
the lyrics. To typeset the chords graphically (and not only by name), the
author recommends use of an additional package such as gchords by K. Peeters.

%package -n texlive-guitarchordschemes
Summary:        Guitar Chord and Scale Tablatures
Version:        svn54512
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cnltx-base.sty)
Requires:       tex(tikz.sty)
Provides:       tex(guitarchordschemes.sty) = %{tl_version}

%description -n texlive-guitarchordschemes
This package provides two commands (\chordscheme and \scales). With those
commands it is possible to draw schematic diagrams of guitar chord tablatures
and scale tablatures. Both commands know a range of options that allow wide
customization of the output. The package's drawing is done with the help of
TikZ.

%package -n texlive-guitartabs
Summary:        A class for drawing guitar tablatures easily
Version:        svn48102
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-guitartabs
This package provides is a simple LaTeX2e class that allows guitarists to
create basic guitar tablatures using LaTeX. Create music and do not be bothered
with macro programming. The class depends on the LaTeX packages geometry,
harmony, inputenc, intcalc, musixtex, tikz, and xifthen, as well as the article
class.

%package -n texlive-harmony
Summary:        Typeset harmony symbols, etc., for musicology
Version:        svn72045
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Provides:       tex(harmony.sty) = %{tl_version}

%description -n texlive-harmony
The package harmony.sty uses the packages ifthen and amssymb from the amsfonts
bundle, together with the LaTeX font lcirclew10 and the font musix13 from
musixtex.

%package -n texlive-latex4musicians
Summary:        A guide for combining LaTeX and music
Version:        svn49759
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex4musicians-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex4musicians-doc <= 11:%{version}

%description -n texlive-latex4musicians
This guide, "LaTeX for Musicians", explains how to create LaTeX documents that
include several kinds of music elements: music symbols, song lyrics, guitar
chords diagrams, lead sheets, music excerpts, guitar tablatures, multi-page
scores.

%package -n texlive-leadsheets
Summary:        Typesetting leadsheets and songbooks
Version:        svn61504
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(translations.sty)
Requires:       tex(xparse.sty)
Provides:       tex(leadsheets.library.chordnames.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.chords.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.external.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.musejazz.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.musicsymbols.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.properties.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.shorthands.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.songs.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.templates.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.translations.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.transposing.code.tex) = %{tl_version}
Provides:       tex(leadsheets.sty) = %{tl_version}

%description -n texlive-leadsheets
This LaTeX package offers support for typesetting simple leadsheets of songs,
i.e. song lyrics and the corresponding chords.

%package -n texlive-liederbuch
Summary:        A LaTeX package for storing songs or other content, and repeated reuse in documents
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(xparse.sty)
Provides:       tex(liederbuch-babel.sty) = %{tl_version}
Provides:       tex(liederbuch-listofsongs.sty) = %{tl_version}
Provides:       tex(liederbuch.sty) = %{tl_version}
Provides:       tex(printliederbuch.sty) = %{tl_version}

%description -n texlive-liederbuch
This package is meant for content which you reuse regularly, like songs in
small booklets. For example the booklets used at church, weddings or similar
events. It has two major parts: You typeset your content once (most likely a
song), garnish it with some meta data and put it into a sty-file. From there
you can insert this content into your document with one single line. The
inserted content can have header and footer that use the meta data (i.e. title,
composer, lyricist). Inside these content fragments, you can use the
\notenzeile (stave line) command to combine an image of a stave line with song
lyrics. If correctly used, the lyrics are placed correctly below the notes and
need most often no or only minor adjustments. With that you can combine any
stave image with LaTeX fonts. You can find resources and inspiration in a demo
project.

%package -n texlive-musical
Summary:        Typeset (musical) theatre scripts
Version:        svn54758
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xspace.sty)
Provides:       tex(musical.sty) = %{tl_version}

%description -n texlive-musical
This package is designed to simplify the development and distribution of
scripts for theatrical musicals, especially ones under development. The output
is formatted to follow generally accepted script style[1] while also
maintaining a high level of typographic integrity, and includes commands for
dialog, lyrics, stage directions, music and dance cues, rehearsal marks, and
more. It gracefully handles dialog that crosses page breaks, and can generate
lists of songs and lists of dances in the show. [1] There are lots of
references for the One True Way to format a script. Naturally, none of them
agree.

%package -n texlive-musicography
Summary:        Accessing symbols for music writing with pdfLaTeX
Version:        svn68220
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(setspace.sty)
Requires:       tex(stackengine.sty)
Provides:       tex(musicography.sty) = %{tl_version}

%description -n texlive-musicography
This package makes available the most commonly used symbols in writing about
music in a way that can be used with pdfLaTeX and looks consistent and
attractive. It includes accidentals, meters, and notes of different rhythmic
values. The package builds on the approach used in the harmony package, where
the symbols are taken from the MusiXTeX fonts. But it provides a larger range
of symbols and a more flexible, user-friendly interface written using xparse
and stackengine.

%package -n texlive-musixguit
Summary:        Easy notation for guitar music, in MusixTeX
Version:        svn21649
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(musixtex.sty)
Requires:       tex(setspace.sty)
Provides:       tex(musixguit.sty) = %{tl_version}

%description -n texlive-musixguit
The package provides commands for typesetting notes for guitar, especially for
simplifying guitar notation with MusixTeX.

%package -n texlive-musixtex-fonts
Summary:        Fonts used by MusixTeX
Version:        svn65517
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-musixtex-fonts
These are fonts for use with MusixTeX; they are provided both as original
Metafont source, and as converted Adobe Type 1. The bundle renders the older
(Type 1 fonts only) bundle musixtex-t1fonts obsolete.

%package -n texlive-octave
Summary:        Typeset musical pitches with octave designations
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(octave.sty) = %{tl_version}

%description -n texlive-octave
This package typesets musical pitch names with designation for the octave in
either the Helmholtz system (with octave numbers), or the traditional system
(with prime symbols). Authors can just write \pitch{C}{4} and the pitches will
be rendered correctly depending on which package option was selected. The
system can also be changed mid-document.

%package -n texlive-piano
Summary:        Typeset a basic 2-octave piano diagram
Version:        svn21574
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xargs.sty)
Provides:       tex(piano.sty) = %{tl_version}

%description -n texlive-piano
This package adds the \keyboard[1][2]..[7] command to your project. When used,
it draws a small 2 octaves piano keyboard on your document, with up to 7 keys
highlighted. Keys go : Co, Cso, Do, Dso, Eo, Fo, Fso, Go, Gso, Ao, Aso, Bo, Ct,
Cst, Dt, Dst, Et, Ft, Fst, Gt, Gst, At, Ast and Bt. (A working example is
included in the README file.)

%package -n texlive-recorder-fingering
Summary:        Package to display recorder fingering diagrams
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Provides:       tex(recorder-fingering.sty) = %{tl_version}

%description -n texlive-recorder-fingering
This package provides support for generating and displaying fingering diagrams
for baroque fingering recorders and the tin whistle. Standard fingerings are
provided for recorders in both C and F, and the tin whistle in D, along with
methods to create and display alternate fingerings for trills, etc.

%package -n texlive-songbook
Summary:        Package for typesetting song lyrics and chord books
Version:        svn18136
License:        LGPL-2.1-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multicol.sty)
Requires:       tex(xstring.sty)
Provides:       tex(conditionals.sty) = %{tl_version}
Provides:       tex(songbook.sty) = %{tl_version}

%description -n texlive-songbook
The package provides an all purpose songbook style. Three types of output may
be created from a single input file: "words and chords" books for the musicians
to play from, "words only" songbooks for the congregation to sing from, and
overhead transparency masters for congregational use. The package will also
print a table of contents, an index sorted by title and first line, and an
index sorted by key, or by artist/composer. The package attempts to handle
songs in multiple keys, as well as songs in multiple languages.

%package -n texlive-songproj
Summary:        Generate Beamer slideshows with song lyrics
Version:        svn76924
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(verse.sty)
Requires:       tex(xparse.sty)
Provides:       tex(songproj.sty) = %{tl_version}

%description -n texlive-songproj
This package, together with the Beamer class, is used to generate slideshows
with song lyrics. This is typically used in religious services in churches
equipped with a projector, for which this package has been written, but it can
be useful for any type of singing assembly. It provides environments to
describe a song in a natural way, and formatting it into slides with overlays.
The package comes with an additional Python script that can be used to convert
plain-text song lyrics to the expected LaTeX markup.

%package -n texlive-songs
Summary:        Produce song books for church or fellowship
Version:        svn51494
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(etex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Provides:       tex(songs.sty) = %{tl_version}

%description -n texlive-songs
The package provides a means of producing beautiful song books for church or
fellowship. It offers: a very easy chord-entry syntax; multiple modes
(words-only; words+chords; slides; handouts); measure bars; guitar tablatures;
automatic transposition; scripture quotations; multiple indexes (sorted by
title, author, important lyrics, or scripture references); and projector-style
output generation, for interactive use. A set of example documents is provided.

%package -n texlive-undar-digitacion
Summary:        Musical fingering diagrams of Pinkullo Huanuqueno, Flute (Recorder), Quena and Saxophone
Version:        svn69742
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(musicography.sty)
Requires:       tex(musixtex.sty)
Requires:       tex(recorder-fingering.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(undar-digitacion.sty) = %{tl_version}

%description -n texlive-undar-digitacion
The package provides tools for generating: Pinkullo Huanuqueno Flute Quena
Saxophone The result will often be a PDF (or set of PDFs) that contain
everything one will need for musical fingering diagrams of the Pinkullo
Huanuqueno, Flute, Quena and Saxophone. The package uses TikZ for most things
and MusixTeX for music symbols.

%package -n texlive-xpiano
Summary:        An extension of the piano package
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(xpiano.sty) = %{tl_version}

%description -n texlive-xpiano
This package provides macros for typesetting virtual keyboards limited to two
octaves for showing notes represented by a colored circle. Optionally, the
number used for pitch analysis can be shown. It is an extension of piano.sty by
Emile Daneault, written in expl3 in answer to a couple of questions on
TeX.StackExchange: https://tex.stackexchange.com/questions/162184/
https://tex.stackexchange.com/questions/246276/. It features extended syntax
and several options, like setting the color, adding numbers for pitch analysis,
one or two octaves, and others.


%prep
# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE3} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE4} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE5} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE6} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE7} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE8} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE9} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE10} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE11} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE12} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE13} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE14} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE15} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE16} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE17} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE18} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE19} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE20} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE21} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE22} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE23} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE24} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE25} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE26} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE27} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE28} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE29} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE30} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE31} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE32} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE33} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE34} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE35} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE36} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE37} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE38} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE39} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE42} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE43} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE44} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE45} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE46} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE47} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE48} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE49} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE50} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE51} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE52} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE53} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE54} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE55} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE56} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE57} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-abc
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/abc/
%doc %{_texmf_main}/doc/latex/abc/

%files -n texlive-bagpipe
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/bagpipe/
%doc %{_texmf_main}/doc/generic/bagpipe/

%files -n texlive-chordbars
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chordbars/
%doc %{_texmf_main}/doc/latex/chordbars/

%files -n texlive-chordbox
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chordbox/
%doc %{_texmf_main}/doc/latex/chordbox/

%files -n texlive-ddphonism
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ddphonism/
%doc %{_texmf_main}/doc/latex/ddphonism/

%files -n texlive-figbas
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/figbas/
%{_texmf_main}/fonts/map/dvips/figbas/
%{_texmf_main}/fonts/tfm/public/figbas/
%{_texmf_main}/fonts/type1/public/figbas/
%doc %{_texmf_main}/doc/fonts/figbas/

%files -n texlive-fretplot
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fretplot/
%doc %{_texmf_main}/doc/latex/fretplot/

%files -n texlive-gchords
%license gpl2.txt
%{_texmf_main}/tex/latex/gchords/
%doc %{_texmf_main}/doc/latex/gchords/

%files -n texlive-gtrcrd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gtrcrd/
%doc %{_texmf_main}/doc/latex/gtrcrd/

%files -n texlive-guitar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/guitar/
%doc %{_texmf_main}/doc/latex/guitar/

%files -n texlive-guitarchordschemes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/guitarchordschemes/
%doc %{_texmf_main}/doc/latex/guitarchordschemes/

%files -n texlive-guitartabs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/guitartabs/
%doc %{_texmf_main}/doc/latex/guitartabs/

%files -n texlive-harmony
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/harmony/
%doc %{_texmf_main}/doc/latex/harmony/

%files -n texlive-latex4musicians
%license fdl.txt
%doc %{_texmf_main}/doc/latex/latex4musicians/

%files -n texlive-leadsheets
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/leadsheets/
%doc %{_texmf_main}/doc/latex/leadsheets/

%files -n texlive-liederbuch
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/liederbuch/
%doc %{_texmf_main}/doc/latex/liederbuch/

%files -n texlive-musical
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musical/
%doc %{_texmf_main}/doc/latex/musical/

%files -n texlive-musicography
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musicography/
%doc %{_texmf_main}/doc/latex/musicography/

%files -n texlive-musixguit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musixguit/
%doc %{_texmf_main}/doc/latex/musixguit/

%files -n texlive-musixtex-fonts
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/musixtex-fonts/
%{_texmf_main}/fonts/opentype/public/musixtex-fonts/
%{_texmf_main}/fonts/source/public/musixtex-fonts/
%{_texmf_main}/fonts/tfm/public/musixtex-fonts/
%{_texmf_main}/fonts/type1/public/musixtex-fonts/
%doc %{_texmf_main}/doc/fonts/musixtex-fonts/

%files -n texlive-octave
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/octave/
%doc %{_texmf_main}/doc/latex/octave/

%files -n texlive-piano
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/piano/
%doc %{_texmf_main}/doc/latex/piano/

%files -n texlive-recorder-fingering
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/recorder-fingering/
%doc %{_texmf_main}/doc/latex/recorder-fingering/

%files -n texlive-songbook
%license lgpl2.1.txt
%{_texmf_main}/makeindex/songbook/
%{_texmf_main}/tex/latex/songbook/
%doc %{_texmf_main}/doc/latex/songbook/

%files -n texlive-songproj
%license bsd.txt
%{_texmf_main}/tex/latex/songproj/
%doc %{_texmf_main}/doc/latex/songproj/

%files -n texlive-songs
%license gpl2.txt
%{_texmf_main}/tex/latex/songs/
%doc %{_texmf_main}/doc/latex/songs/

%files -n texlive-undar-digitacion
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/undar-digitacion/
%doc %{_texmf_main}/doc/latex/undar-digitacion/

%files -n texlive-xpiano
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xpiano/
%doc %{_texmf_main}/doc/latex/xpiano/

%changelog
* Wed Feb 04 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76267-1
- update to svn76267, fix licensing, descriptions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73288-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73288-1
- Update to TeX Live 2025
