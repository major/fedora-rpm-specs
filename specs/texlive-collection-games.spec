%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-games
Epoch:          12
Version:        svn76381
Release:        2%{?dist}
Summary:        Games typesetting

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-games.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bartel-chess-fonts.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bartel-chess-fonts.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess-problem-diagrams.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chess-problem-diagrams.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessboard.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessboard.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessfss.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chessfss.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chinesechess.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chinesechess.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossword.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossword.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crosswrd.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crosswrd.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/customdice.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/customdice.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/egameps.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/egameps.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eigo.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eigo.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebook.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebook.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebooklib.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gamebooklib.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/go.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/go.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hanoi.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/havannah.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/havannah.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexboard.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexboard.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexgame.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hexgame.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hmtrump.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hmtrump.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/horoscop.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/horoscop.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jeuxcartes.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jeuxcartes.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jigsaw.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jigsaw.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/labyrinth.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/labyrinth.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logicpuzzle.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/logicpuzzle.doc.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mahjong.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mahjong.doc.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathador.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathador.doc.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maze.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maze.doc.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multi-sudoku.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multi-sudoku.doc.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musikui.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musikui.doc.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nimsticks.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nimsticks.doc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/onedown.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/onedown.doc.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othello.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othello.doc.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othelloboard.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/othelloboard.doc.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pas-crosswords.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pas-crosswords.doc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-go.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgf-go.doc.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/playcards.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/playcards.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psgo.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psgo.doc.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quizztex.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quizztex.doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realtranspose.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/realtranspose.doc.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reverxii.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/reverxii.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rouequestions.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rouequestions.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rpgicons.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rpgicons.doc.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schwalbe-chess.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/schwalbe-chess.doc.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scrabble.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/scrabble.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sgame.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sgame.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skak.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skak.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skaknew.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/skaknew.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soup.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/soup.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudoku.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudoku.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudokubundle.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sudokubundle.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tangramtikz.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tangramtikz.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thematicpuzzle.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thematicpuzzle.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tictactoe.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tictactoe.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-triminos.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikz-triminos.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trivialpursuit.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/trivialpursuit.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twoxtwogame.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/twoxtwogame.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wargame.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wargame.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/weiqi.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/weiqi.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordle.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordle.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xq.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xq.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xskak.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xskak.doc.tar.xz

# AppStream metadata for font components
Source123:        skaknew.metainfo.xml
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-bartel-chess-fonts
Requires:       texlive-chess
Requires:       texlive-chess-problem-diagrams
Requires:       texlive-chessboard
Requires:       texlive-chessfss
Requires:       texlive-chinesechess
Requires:       texlive-collection-latex
Requires:       texlive-crossword
Requires:       texlive-crosswrd
Requires:       texlive-customdice
Requires:       texlive-egameps
Requires:       texlive-eigo
Requires:       texlive-gamebook
Requires:       texlive-gamebooklib
Requires:       texlive-go
Requires:       texlive-hanoi
Requires:       texlive-havannah
Requires:       texlive-hexboard
Requires:       texlive-hexgame
Requires:       texlive-hmtrump
Requires:       texlive-horoscop
Requires:       texlive-jeuxcartes
Requires:       texlive-jigsaw
Requires:       texlive-labyrinth
Requires:       texlive-logicpuzzle
Requires:       texlive-mahjong
Requires:       texlive-mathador
Requires:       texlive-maze
Requires:       texlive-multi-sudoku
Requires:       texlive-musikui
Requires:       texlive-nimsticks
Requires:       texlive-onedown
Requires:       texlive-othello
Requires:       texlive-othelloboard
Requires:       texlive-pas-crosswords
Requires:       texlive-pgf-go
Requires:       texlive-playcards
Requires:       texlive-psgo
Requires:       texlive-quizztex
Requires:       texlive-realtranspose
Requires:       texlive-reverxii
Requires:       texlive-rouequestions
Requires:       texlive-rpgicons
Requires:       texlive-rubik
Requires:       texlive-schwalbe-chess
Requires:       texlive-scrabble
Requires:       texlive-sgame
Requires:       texlive-skak
Requires:       texlive-skaknew
Requires:       texlive-soup
Requires:       texlive-sudoku
Requires:       texlive-sudokubundle
Requires:       texlive-tangramtikz
Requires:       texlive-thematicpuzzle
Requires:       texlive-tictactoe
Requires:       texlive-tikz-triminos
Requires:       texlive-trivialpursuit
Requires:       texlive-twoxtwogame
Requires:       texlive-wargame
Requires:       texlive-weiqi
Requires:       texlive-wordle
Requires:       texlive-xq
Requires:       texlive-xskak

%description
Setups for typesetting various games, including chess.


%package -n texlive-bartel-chess-fonts
Summary:        A set of fonts supporting chess diagrams
Version:        svn20619
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bartel-chess-fonts
The fonts are provided as Metafont source.

%package -n texlive-chess
Summary:        Fonts for typesetting chess boards
Version:        svn20582
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chess.sty) = %{tl_version}

%description -n texlive-chess
The original (and now somewhat dated) TeX chess font package. Potential users
should consider skak (for alternative fonts, and notation support), texmate
(for alternative notation support), or chessfss (for flexible font choices).

%package -n texlive-chess-problem-diagrams
Summary:        A package for typesetting chess problem diagrams
Version:        svn74591
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cpdparse.sty) = %{tl_version}
Provides:       tex(diagram.sty) = %{tl_version}

%description -n texlive-chess-problem-diagrams
This package provides macros to typeset chess problem diagrams including fairy
chess problems (mostly using rotated images of pieces) and other boards.

%package -n texlive-chessboard
Summary:        Print chess boards
Version:        svn72795
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(animate.sty)
Requires:       tex(array.sty)
Requires:       tex(attachfile.sty)
Requires:       tex(babel.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(chessfss.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(doc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fourier.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
# LuxiMono Requires filtered - non-free font
Requires:       tex(makeidx.sty)
Requires:       tex(microtype.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
Provides:       tex(UF-chessboard-documentation.sty) = %{tl_version}
Provides:       tex(chessboard-keys-main.sty) = %{tl_version}
Provides:       tex(chessboard-keys-pgf.sty) = %{tl_version}
Provides:       tex(chessboard-pgf.sty) = %{tl_version}
Provides:       tex(chessboard.sty) = %{tl_version}

%description -n texlive-chessboard
This package offers commands to print chessboards. It can print partial boards,
hide pieces and fields, color the boards and put various marks on the board. It
has a lot of options to place pieces on the board. Using exotic pieces (e.g.,
for fairy chess) is possible. The documentation includes an example of an
animated chessboard, for those whose PDF viewer can display animations.

%package -n texlive-chessfss
Summary:        A package to handle chess fonts
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(chessfss.sty) = %{tl_version}
Provides:       tex(lsb1enc.def) = %{tl_version}
Provides:       tex(lsb2enc.def) = %{tl_version}
Provides:       tex(lsb3enc.def) = %{tl_version}
Provides:       tex(lsbc1enc.def) = %{tl_version}
Provides:       tex(lsbc2enc.def) = %{tl_version}
Provides:       tex(lsbc3enc.def) = %{tl_version}
Provides:       tex(lsbc4enc.def) = %{tl_version}
Provides:       tex(lsbc5enc.def) = %{tl_version}
Provides:       tex(lsbenc.def) = %{tl_version}
Provides:       tex(lsfenc.def) = %{tl_version}
Provides:       tex(lsienc.def) = %{tl_version}

%description -n texlive-chessfss
This package offers commands to use and switch between chess fonts. It uses the
LaTeX font selection scheme (nfss). The package doesn't parse, format and print
PGN input like e.g. the packages skak or texmate; the aim of the package is to
offer writers of chess packages a bundle of commands for fonts, so that they
don't have to implement all these commands for themselves. A normal user can
use the package to print e.g. single chess symbols and simple diagrams. The
documentation contains also a section about installation of chess fonts.

%package -n texlive-chinesechess
Summary:        Typeset Chinese chess with l3draw
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(chinesechess.sty) = %{tl_version}

%description -n texlive-chinesechess
This LaTeX3 package based on l3draw provides macros and an environment for
Chinese chess manual writing.

%package -n texlive-crossword
Summary:        Typeset crossword puzzles
Version:        svn73579
License:        Crossword
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Provides:       tex(cwpuzzle.sty) = %{tl_version}

%description -n texlive-crossword
An extended grid-based puzzle package, designed to take all input (both grid
and clues) from the same file. The package can typeset grids with holes in them
(for advertisements, or other sorts of stuff), and can deal with several sorts
of puzzle: The classical puzzle contains numbers for the words and clues for
the words to be filled in. The numbered puzzle contains numbers in each cell
where identical numbers represent identical letters. The goal is to find out
which number corresponds to which letter. The fill-in type of puzzle consists
of a grid and a list of words. The goal is to place all words in the grid.
Sudoku and Kakuro puzzles involve filling in grids of numbers according to
their own rules. Format may be block-separated, or separated by thick lines.
Input to the package is somewhat redundant: specification of the grid is
separate from specification of the clues (if they're necessary). The author
considers this style both 'natural' and robust.

%package -n texlive-crosswrd
Summary:        Macros for typesetting crossword puzzles
Version:        svn16896
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(crosswrd.sty) = %{tl_version}

%description -n texlive-crosswrd
The package provides a LaTeX method of typesetting crosswords, and assists the
composer ensure that the grid all goes together properly. Brian Hamilton
Kelly's original was written for LaTeX 2.09, and needed to be updated to run
with current LaTeX.

%package -n texlive-customdice
Summary:        Simple commands for drawing customisable dice
Version:        svn64089
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Provides:       tex(customdice.sty) = %{tl_version}

%description -n texlive-customdice
The customdice package for LaTeX, LuaLaTeX and XeTeX that provides
functionality for drawing dice. The aim is to provide highly-customisable but
simple-to-use commands, allowing: adding custom text to dice faces; control
over colouring; control over sizing.

%package -n texlive-egameps
Summary:        LaTeX package for typesetting extensive games
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(egameps.sty) = %{tl_version}

%description -n texlive-egameps
The style is intended to have enough features to draw any extensive game with
relative ease. The facilities of PSTricks are used for graphics. (An older
version of the package, which uses the LaTeX picture environment rather than
PSTricks and consequently has many fewer features is available on the package
home page.)

%package -n texlive-eigo
Summary:        Comprehensive tools for creating Go (Weiqi/Baduk) game diagrams in LaTeX
Version:        svn76251
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(eigo.sty) = %{tl_version}

%description -n texlive-eigo
The eigo package provides comprehensive tools for creating Go (Weiqi/Baduk)
game diagrams in LaTeX documents. Developed with AI assistance, it offers
multiple stone colors with full RGB customization, automatic numbering systems
with alternating colors, geometric transformations (rotations, mirrors),
flexible board display options with enhanced 2pt borders for publication
quality, symbol placement, and full LuaLaTeX compatibility. The package
supports seven stone colors, border display, extended size presets with
validation, and advanced features for game analysis and problem presentation.

%package -n texlive-gamebook
Summary:        Typeset gamebooks and other interactive novels
Version:        svn24714
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(draftwatermark.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(extramarks.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(scrtime.sty)
Requires:       tex(titlesec.sty)
Provides:       tex(gamebook.sty) = %{tl_version}

%description -n texlive-gamebook
This package provides the means in order to lay-out gamebooks with LaTeX. A
simple gamebook example is included with the package, and acts as a tutorial.

%package -n texlive-gamebooklib
Summary:        Macros for setting numbered entries in shuffled order
Version:        svn67772
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lcg.sty)
Requires:       tex(macroswap.sty)
Requires:       tex(silence.sty)
Provides:       tex(gamebooklib.sty) = %{tl_version}

%description -n texlive-gamebooklib
This package provides macros and environments to allow the user to typeset a
series of cross-referenced, numbered "entries", shuffled into random order, to
produce an interactive novel or "gamebook". This allows entries to be written
in natural order and shuffled automatically into a repeatable non-linear order.
Limited support is provided for footnotes to appear at the natural position:
the end of each entry, or the end of each page, whichever is closest to the
footnote mark. This is unrelated to the gamebook package which is more
concerned with the formatting of entries rather than their order. The two
packages can be used together or separately.

%package -n texlive-go
Summary:        Fonts and macros for typesetting go games
Version:        svn28628
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(go.sty) = %{tl_version}

%description -n texlive-go
The macros provide for nothing more complicated than the standard 19x19 board;
the fonts are written in Metafont.

%package -n texlive-hanoi
Summary:        Tower of Hanoi in TeX
Version:        svn25019
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hanoi.tex) = %{tl_version}

%description -n texlive-hanoi
The Plain TeX program (typed in the shape of the towers of Hanoi) serves both
as a game and as a TeX programming exercise. As a game it will solve the towers
with (up to) 15 discs (with 15 discs, 32767 moves are needed).

%package -n texlive-havannah
Summary:        Diagrams of board positions in the games of Havannah and Hex
Version:        svn36348
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(havannah.sty) = %{tl_version}

%description -n texlive-havannah
This package defines macros for typesetting diagrams of board positions in the
games of Havannah and Hex.

%package -n texlive-hexboard
Summary:        For drawing Hex boards and games
Version:        svn62102
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(hexboard.sty) = %{tl_version}

%description -n texlive-hexboard
hexboard is a package for LaTeX that should also work with LuaTeX and XeTeX,
that provides functionality for drawing Hex boards and games. The aim is a
clean, clear design with flexibility for drawing different sorts of Hex
diagrams.

%package -n texlive-hexgame
Summary:        Provide an environment to draw a hexgame-board
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-poly.sty)
Requires:       tex(pstcol.sty)
Provides:       tex(hexgame.sty) = %{tl_version}

%description -n texlive-hexgame
Hex is a mathematical game invented by the Danish mathematician Piet Hein and
independently by the mathematician John Nash. This package defines an
environment that enables the user to draw such a game in a trivial way.

%package -n texlive-hmtrump
Summary:        Describe card games
Version:        svn54512
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(hmtrump.sty) = %{tl_version}

%description -n texlive-hmtrump
This package provides a font with LuaLaTeX support for describing card games.

%package -n texlive-horoscop
Summary:        Generate astrological charts in LaTeX
Version:        svn56021
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(starfont.sty)
Requires:       tex(trig.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(horoscop.sty) = %{tl_version}

%description -n texlive-horoscop
The horoscop package provides a unified interface for astrological font
packages; typesetting with pict2e of standard wheel charts and some variations,
in PostScript- and PDF-generating TeX engines; and access to external
calculation software (Astrolog and Swiss Ephemeris) for computing object
positions.

%package -n texlive-jeuxcartes
Summary:        Macros to insert playing cards
Version:        svn76966
License:        LPPL-1.3c AND LGPL-2.1-only AND LicenseRef-Fedora-Public-Domain AND CC-BY-SA-4.0 AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(pifont.sty)
Requires:       tex(randomlist.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xstring.sty)
Provides:       tex(JeuxCartes.sty) = %{tl_version}

%description -n texlive-jeuxcartes
This package provides macros to insert playing cards, single, or hand, or
random-hand, Poker or French Tarot or Uno, from png files.

%package -n texlive-jigsaw
Summary:        Draw jigsaw pieces with TikZ
Version:        svn71923
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-epstopdf-pkg
Requires:       texlive-iftex
Requires:       texlive-pgf
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(tikz.sty)
Provides:       tex(jigsaw.sty) = %{tl_version}

%description -n texlive-jigsaw
This is a small LaTeX package to draw jigsaw pieces with TikZ. It is possible
to draw individual pieces and adjust their shape, create tile patterns or
automatically generate complete jigsaws.

%package -n texlive-labyrinth
Summary:        Draw labyrinths and solution paths
Version:        svn33454
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(picture.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(labyrinth.sty) = %{tl_version}

%description -n texlive-labyrinth
The labyrinth package provides code and an environment for typesetting simple
labyrinths with LaTeX, and generating an automatic or manual solution path.

%package -n texlive-logicpuzzle
Summary:        Typeset (grid-based) logic puzzles
Version:        svn34491
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(logicpuzzle.sty) = %{tl_version}
Provides:       tex(lpenv.sty) = %{tl_version}

%description -n texlive-logicpuzzle
The package allows the user to typeset various logic puzzles. At the moment the
following puzzles are supported: 2D-Sudoku (aka Magiequadrat, Diagon, ...),
Battleship (aka Bimaru, Marinespiel, Batalla Naval, ...), Bokkusu (aka
Kakurasu, Feldersummenratsel, ...), Bridges (akak Bruckenbau, Hashi, ...),
Chaos Sudoku, Four Winds (aka Eminent Domain, Lichtstrahl, ...), Hakyuu (aka
Seismic, Ripple Effect, ...), Hitori, Kakuro, Kendoku (aka Mathdoku, Calcudoku,
Basic, MiniPlu, Ken Ken, Square Wisdom, Sukendo, Caldoku, ..., Killer Sudoku
(aka Samunapure, Sum Number Place, Sumdoku, Gebietssummen, ...), Laser Beam
(aka Laserstrahl, ...), Magic Labyrinth (aka Magic Spiral, Magisches Labyrinth,
...), Magnets (aka Magnetplatte, Magnetfeld, ...), Masyu (aka Mashi,
{White|Black} Pearls, ...), Minesweeper (aka Minensuche, ...), Nonogram (aka
Griddlers, Hanjie, Tsunami, Logic Art, Logimage, ...), Number Link (aka
Alphabet Link, Arukone, Buchstabenbund, ...), Resuko, Schatzsuche, Skyline (aka
Skycrapers, Wolkenkratzer, Hochhauser, ...), including Skyline Sudoku and
Skyline Sudoku (N*N) variants, Slitherlink (aka Fences, Number Line, Dotty
Dilemma, Sli-Lin, Takegaki, Great Wall of China, Loop the Loop, Rundweg,
Gartenzaun, ...), Star Battle (aka Sternenschlacht, ...), Stars and Arrows (aka
Sternenhimmel, ...), Sudoku, Sun and Moon (aka Sternenhaufen, Munraito, ...),
Tents and Trees (aka Zeltlager, Zeltplatz, Camping, ...), and Tunnel.

%package -n texlive-mahjong
Summary:        Typeset Mahjong Tiles using MPSZ Notation
Version:        svn76924
License:        MIT AND LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(xparse.sty)
Provides:       tex(mahjong.sty) = %{tl_version}

%description -n texlive-mahjong
The mahjong package provides a LaTeX2e and LaTeX3 interface for typesetting
mahjong tiles using an extended version of MPSZ algebraic notation. Features
include spaces, rotated, blank, and concealed tiles, as well as red fives. The
size of the mahjong tiles can be controlled using a package option and an
optional argument of \mahjong. It is primarily aimed at Riichi (aka. Japanese)
Mahjong but can be used to typeset any style of mahjong.

%package -n texlive-mathador
Summary:        LaTeX commands for the French game "Mathador"
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bm.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(mathador.sty) = %{tl_version}

%description -n texlive-mathador
This is a LaTeX package with graphic commands for the French game MATHADOR (by
author Eric Trouillot and Reseau CANOPE). The principle of the game is like
this: Roll the dice! They give you one target number (between 0 and 99) and
five numbers to use to reach it. You can use the four arithmetic operations to
get there.

%package -n texlive-maze
Summary:        Generate random mazes
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(maze.sty) = %{tl_version}

%description -n texlive-maze
This package can generate random square mazes of a specified size. The mazes
generated by this package are natural and their solution is not too obvious.
The output it based on the picture environment.

%package -n texlive-multi-sudoku
Summary:        Create and customise Sudoku grids of various sizes
Version:        svn75941
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(xparse.sty)
Provides:       tex(multi-sudoku.sty) = %{tl_version}

%description -n texlive-multi-sudoku
This package provides tools for typesetting Sudoku grids of various sizes in
LaTeX. Unlike other Sudoku packages which are typically limited to the standard
9x9 layout, this package supports a broad range of grid sizes - from trivial
1x1 puzzles to extended 49x49 Sudokus - that's the limit for now! Grids are
drawn with our sudoku environment, which is based on using LaTeX's native
tabular environment. We include intuitive options to control dimensions, font
size, and grid thickness. Entries in the grid are inserted as in a regular
table, thus making it simple to create, customise, and fill Sudoku puzzles
manually.

%package -n texlive-musikui
Summary:        Easy creation of "arithmetical restoration" puzzles
Version:        svn47472
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(musikui.sty) = %{tl_version}

%description -n texlive-musikui
This package permits to easily typeset arithmetical restorations using LaTeX.
This package requires the graphicx package.

%package -n texlive-nimsticks
Summary:        Draws sticks for games of multi-pile Nim
Version:        svn64118
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(lcg.sty)
Requires:       tex(tikz.sty)
Provides:       tex(nimsticks.sty) = %{tl_version}

%description -n texlive-nimsticks
This LaTeX package provides commands \drawnimstick to draw a single nim stick
and \nimgame which represents games of multi-pile Nim. Nim sticks are drawn
with a little random wobble so they look 'thrown together' and not too regular.
The package also provides options to customise the size and colour of the
sticks, and flexibility to draw heaps of different objects.

%package -n texlive-onedown
Summary:        Typeset Bridge Diagrams
Version:        svn69067
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(adjustbox.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(collcell.sty)
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(makecmds.sty)
Requires:       tex(moresize.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(relsize.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tracklang.sty)
Requires:       tex(translator.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(onedown.sty) = %{tl_version}

%description -n texlive-onedown
This is a comprehensive package to draw all sorts of bridge diagrams, including
hands (stand alone or arround a compass), bidding tables (stand alone or in
connection with hands/compass), trick tables, and expert quizzes. Features:
Works for all fontsizes from \ssmall to \HUGE. Different fonts for hands,
bidding diagrams, compass, etc. are possible. Annotations to card and bidding
diagrams. Automated check on consistency of suit and hands. Multilingual output
of bridge terms. Extensive documentation: User manual, Reference manual, and
Examples.

%package -n texlive-othello
Summary:        Modification of a Go package to create othello boards
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(othello.sty) = %{tl_version}

%description -n texlive-othello
A package (based on Kolodziejska's go), and fonts (as Metafont source) are
provided.

%package -n texlive-othelloboard
Summary:        Typeset Othello (Reversi) diagrams of any size, with annotations
Version:        svn23714
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xstring.sty)
Provides:       tex(othelloboard.sty) = %{tl_version}

%description -n texlive-othelloboard
The package enables the user to generate high-quality Othello (also known as
Reversi) board diagrams of any size. The diagrams support annotations,
including full game transcripts. Automated board or transcript creation, from
plain text formats standard to WZebra (and other programs) is also supported.

%package -n texlive-pas-crosswords
Summary:        Creating crossword grids, using TikZ
Version:        svn32313
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fp.sty)
Requires:       tex(multido.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(pas-crosswords.sty) = %{tl_version}

%description -n texlive-pas-crosswords
The package produces crossword grids, using a wide variety of colours and
decorations of the grids and the text in them. The package uses TikZ for its
graphical output.

%package -n texlive-pgf-go
Summary:        Diagramming and commenting on Go games
Version:        svn74578
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(pgf-go-coordinate-parser.sty) = %{tl_version}
Provides:       tex(pgf-go-goban.sty) = %{tl_version}
Provides:       tex(pgf-go-marks.sty) = %{tl_version}
Provides:       tex(pgf-go-players.sty) = %{tl_version}
Provides:       tex(pgf-go-profiles.sty) = %{tl_version}
Provides:       tex(pgf-go-remember.sty) = %{tl_version}
Provides:       tex(pgf-go-stones.sty) = %{tl_version}
Provides:       tex(pgf-go.sty) = %{tl_version}

%description -n texlive-pgf-go
A LaTeX package for creating Go (Baduk) diagrams with ease. It features an
efficient coordinate-loading syntax to streamline workflows and offers flexible
profile manipulation, allowing users to customize board layouts, stones, and
annotations effortlessly.

%package -n texlive-playcards
Summary:        A simple template for drawing playcards
Version:        svn67342
License:        LGPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(contour.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(playcards.sty) = %{tl_version}

%description -n texlive-playcards
This small package provides commands for drawing customized playcards with
width 59mm and height 89mm, which are typical card dimensions.

%package -n texlive-psgo
Summary:        Typeset go diagrams with PSTricks
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Provides:       tex(psgo.sty) = %{tl_version}

%description -n texlive-psgo
Typeset go diagrams with PSTricks

%package -n texlive-quizztex
Summary:        Create quizzes like in TV shows
Version:        svn75977
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quizztex.sty) = %{tl_version}

%description -n texlive-quizztex
This LaTeX package permits to create quizzes in the style of the TV shows <<
Qui veut gagner des millions ? >> ("Who Wants to Be a Millionaire?") or << Tout
le monde veut prendre sa place ! >>.

%package -n texlive-realtranspose
Summary:        The "real" way to transpose a Matrix
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(realtranspose.sty) = %{tl_version}

%description -n texlive-realtranspose
With realtranspose you can notate the transposition of a matrix by rotating the
symbols 90 degrees. This is an homage to the realhats package.

%package -n texlive-reverxii
Summary:        Playing Reversi in TeX
Version:        svn63753
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(reverxii.tex) = %{tl_version}

%description -n texlive-reverxii
Following the lead of xii.tex, this little (938 characters) program that plays
Reversi. (The program incorporates some primitive AI.)

%package -n texlive-rouequestions
Summary:        Draw a "question wheel" (roue de questions)
Version:        svn67670
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-euclide.sty)
Provides:       tex(RoueQuestions.sty) = %{tl_version}

%description -n texlive-rouequestions
This package helps to produce a game for students: It is a wheel displaying
questions, with hidden answers inside.

%package -n texlive-rpgicons
Summary:        Icons for tabletop role-playing games
Version:        svn77109
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(rpgicons-l3.sty) = %{tl_version}
Provides:       tex(rpgicons-pgf.sty) = %{tl_version}
Provides:       tex(rpgicons.sty) = %{tl_version}

%description -n texlive-rpgicons
This package provides a set of high-quality icons for use in notes for tabletop
role-playing games. The icons are meant to be used in the body text, but they
can also be used in other contexts such as graphics or diagrams. The package
comes in two variants, one based on the l3draw package, and the other on
PGF/TikZ.

%package -n texlive-schwalbe-chess
Summary:        Typeset the German chess magazine "Die Schwalbe"
Version:        svn73582
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(diagram.sty)
Provides:       tex(schwalbe.sty) = %{tl_version}
Provides:       tex(swruler.sty) = %{tl_version}

%description -n texlive-schwalbe-chess
The package is based on chess-problem-diagrams, which in its turn has a
dependency on the bartel-chess-fonts.

%package -n texlive-scrabble
Summary:        Commands for Scrabble boards
Version:        svn77114
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(randintlist.sty)
Requires:       tex(tikz.sty)
Provides:       tex(Scrabble.sty) = %{tl_version}

%description -n texlive-scrabble
This package provides some commands (in English and in French) to work with a
Scrabble Board : \ScrabbleBoard and \begin{EnvScrabble} and \ScrabblePutWord
for the English version, \PlateauScrabble and \begin{EnvScrabble} and
\ScrabblePlaceMot for the French version.

%package -n texlive-sgame
Summary:        LaTeX style for typesetting strategic games
Version:        svn30959
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Provides:       tex(sgame.sty) = %{tl_version}
Provides:       tex(sgamevar.sty) = %{tl_version}

%description -n texlive-sgame
Formats strategic games. For a 2x2 game, for example, the input:
\begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$ &$3,0$ &$0,9$ \end{game}
produces output with (a) boxes around the payoffs, (b) payoff columns of equal
width, and (c) payoffs vertically centered within the boxes. Note that the game
environment will not work in the argument of another command.

%package -n texlive-skak
Summary:        Fonts and macros for typesetting chess games
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(chessfss.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lambda.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(skak.sty) = %{tl_version}

%description -n texlive-skak
This package provides macros and fonts in Metafont format which can be used to
typeset chess games using PGN, and to show diagrams of the current board in a
document. The package builds on work by Piet Tutelaers -- the main novelty is
the use of PGN for input instead of the more cumbersome coordinate notation
(g1f3 becomes the more readable Nf3 in PGN). An Adobe Type 1 implementation of
skak's fonts is available as package skaknew; an alternative chess notational
scheme is available in package texmate, and a general mechanism for selecting
chess fonts is provided in chessfss.

%package -n texlive-skaknew
Summary:        The skak chess fonts redone in Adobe Type 1
Version:        svn20031
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-skaknew
This package offers Adobe Type 1 versions of the fonts provided as Metafont
source by the skak bundle.

%package -n texlive-soup
Summary:        Generate alphabet soup puzzles
Version:        svn50815
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Provides:       tex(soup.sty) = %{tl_version}

%description -n texlive-soup
Generate alphabet soup puzzles (aka word search puzzles), and variations using
numbers or other symbols. Provides macros to generate an alphabet soup style
puzzle (also known as word search puzzles or "find-the-word" puzzles). Allow
creating numbersoup and soups with custom symbol sets.

%package -n texlive-sudoku
Summary:        Create sudoku grids
Version:        svn67189
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sudoku.sty) = %{tl_version}

%description -n texlive-sudoku
The sudoku package provides an environment for typesetting sudoku grids. A
sudoku puzzle is a 9x9 grid where some of the squares in the grid contain
numbers. The rules are simple: every column can only contain the digits 1 to 9,
every row can only contain the digits 1 to 9 and every 3x3 box can only contain
the digits 1 to 9. More information, including help and example puzzles, can be
found at sudoku.org.uk. This site also has blank sudoku grids (or worksheets),
but you will not need to print them from there if you have this package
installed.

%package -n texlive-sudokubundle
Summary:        A set of sudoku-related packages
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(createsudoku.sty) = %{tl_version}
Provides:       tex(printsudoku.sty) = %{tl_version}
Provides:       tex(solvesudoku.sty) = %{tl_version}

%description -n texlive-sudokubundle
The bundle provides three packages: printsudoku, which provides a command
\sudoku whose argument is the name of a file containing a puzzle specification;
solvesudoku, which attempts to find a solution to the puzzle in the file named
in the argument; and createsudoku, which uses the random package to generate a
puzzle according to a bunch of parameters that the user sets via macros. The
bundle comes with a set of ready-prepared puzzle files.

%package -n texlive-tangramtikz
Summary:        Tangram puzzles, with TikZ
Version:        svn75123
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
Provides:       tex(TangramTikz.sty) = %{tl_version}

%description -n texlive-tangramtikz
This package provides some commands (with English and French keys) to work with
tangram puzzles: \begin{EnvTangramTikz} and \PieceTangram to position a piece,
\TangramTikz to display a predefined Tangram.

%package -n texlive-thematicpuzzle
Summary:        Horizontal banners in a puzzle style
Version:        svn75984
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xstring.sty)
Provides:       tex(thematicpuzzle.sty) = %{tl_version}

%description -n texlive-thematicpuzzle
With this package it is possible to create a horizontal banner in the form of a
puzzle. There are some predefined themes.

%package -n texlive-tictactoe
Summary:        Drawing tic-tac-toe or Noughts and Crosses games
Version:        svn75712
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xspace.sty)
Provides:       tex(tictactoe.sty) = %{tl_version}

%description -n texlive-tictactoe
This package which provides commands for drawing grids for the game known
variously as tic-tac-toe (and variants), Noughts and Crosses, Naughts and
Crosses, Xs and Os, and so on.

%package -n texlive-tikz-triminos
Summary:        Create triminos, made with TikZ
Version:        svn73533
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tikz-triminos.sty) = %{tl_version}

%description -n texlive-tikz-triminos
Create (1 or 9 or 12) TriMinos with some customizations: size, font, logo,
colors; automatic texts adjustment; full version, or joker usage. Inspiration
from Paul Matthies

%package -n texlive-trivialpursuit
Summary:        Insert Trivial Pursuit board game
Version:        svn76152
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintexpr.sty)
Provides:       tex(TrivialPursuit.sty) = %{tl_version}

%description -n texlive-trivialpursuit
This is a package to display a Trivial Pursuit board game, with customization.

%package -n texlive-twoxtwogame
Summary:        Visualize 2x2 normal-form games
Version:        svn70423
License:        Apache-2.0 AND CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfmath-xfp.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(tikz-3dplot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzscale.sty)
Provides:       tex(twoxtwogame.sty) = %{tl_version}

%description -n texlive-twoxtwogame
This is a package for the visualization of 2x2 normal form games. The package
is based on PGF/TikZ and produces beautiful vector graphics that are intended
for use in scientific publications. The commands include the creation of
graphical representations of 2x2 games, the visualization of equilibria in 2x2
games and game embeddings for 2x2 games.

%package -n texlive-wargame
Summary:        A LaTeX package to prepare hex'n'counter wargames
Version:        svn72903
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(tikzlibrarywargame.chit.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarywargame.hex.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarywargame.natoapp6c.code.tex) = %{tl_version}
Provides:       tex(tikzlibrarywargame.util.code.tex) = %{tl_version}
Provides:       tex(wargame.sty) = %{tl_version}

%description -n texlive-wargame
This package can help make classic Hex'n'Counter wargames using LaTeX. The
package provides tools for generating Hex maps and boards Counters for units,
markers, and so on Counter sheets Order of Battle charts Illustrations in the
rules using the defined maps and counters The result will often be a PDF (or
set of PDFs) that contains everything one will need for a game (rules, charts,
boards, counter sheets). The package uses NATO App6 symbology for units. The
package uses NATO App6 symbology for units. The package uses TikZ for most
things. The package supports exporting the game to a VASSAL module See also the
README.md file for more, and of course the documentation (including the
tutorial in tutorial/game.pdf).

%package -n texlive-weiqi
Summary:        Use LaTeX3 to typeset Weiqi (Go)
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(weiqi.sty) = %{tl_version}

%description -n texlive-weiqi
This package uses LaTeX3 to typeset Weiqi (Go). Shi Yong LaTeX3 Chuang Jian Yi
Ge Pai Ban Wei Qi Qi Pu De Hong Bao .

%package -n texlive-wordle
Summary:        Create wordle grids
Version:        svn72059
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(wordle.sty) = %{tl_version}

%description -n texlive-wordle
This package provides environments (in French or English) to display wordle
grids: \begin{WordleGrid} for the English version, \begin{GrilleSutom} for the
French version.

%package -n texlive-xq
Summary:        Support for writing about xiangqi
Version:        svn35211
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xq.sty) = %{tl_version}

%description -n texlive-xq
The package is for writing about xiangqi or chinese chess. You can write games
or parts of games and show diagrams with special positions.

%package -n texlive-xskak
Summary:        An extension to the skak package for chess typesetting
Version:        svn51432
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(chessboard.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xifthen.sty)
Provides:       tex(xskak-keys.sty) = %{tl_version}
Provides:       tex(xskak-nagdef.sty) = %{tl_version}
Provides:       tex(xskak.sty) = %{tl_version}

%description -n texlive-xskak
Xskak, as its prime function, saves information about a chess game for later
use (e.g., to loop through a game to make an animated board). The package also
extends the input that the parsing commands can handle and offers an interface
to define and switch between indefinite levels of styles.


%prep
# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

mkdir -p %{buildroot}%{_datadir}/fonts
mkdir -p %{buildroot}%{_datadir}/appdata

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
tar -xf %{SOURCE58} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE59} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE60} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE61} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE62} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE63} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE64} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE65} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE66} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE67} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE68} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE69} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE70} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE71} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE72} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE73} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE74} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE75} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE76} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE77} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE78} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE79} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE80} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE81} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE82} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE83} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE84} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE85} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE86} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE87} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE88} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE89} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE90} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE91} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE92} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE93} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE94} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE95} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE96} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE97} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE98} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE99} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE100} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE101} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE102} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE103} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE104} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE105} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE106} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE107} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE108} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE109} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE110} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE111} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE112} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE113} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE114} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE115} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE116} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE117} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE118} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE119} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE120} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE121} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE122} -C %{buildroot}%{_texmf_main}

# Install AppStream metadata for font components
cp %{SOURCE123} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/skaknew %{buildroot}%{_datadir}/fonts/skaknew

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-bartel-chess-fonts
%license gpl2.txt
%{_texmf_main}/fonts/source/public/bartel-chess-fonts/
%{_texmf_main}/fonts/tfm/public/bartel-chess-fonts/
%doc %{_texmf_main}/doc/fonts/bartel-chess-fonts/

%files -n texlive-chess
%license pd.txt
%{_texmf_main}/fonts/source/public/chess/
%{_texmf_main}/fonts/tfm/public/chess/
%{_texmf_main}/tex/latex/chess/
%doc %{_texmf_main}/doc/fonts/chess/

%files -n texlive-chess-problem-diagrams
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chess-problem-diagrams/
%doc %{_texmf_main}/doc/latex/chess-problem-diagrams/

%files -n texlive-chessboard
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chessboard/
%doc %{_texmf_main}/doc/latex/chessboard/

%files -n texlive-chessfss
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/chessfss/
%{_texmf_main}/tex/latex/chessfss/
%doc %{_texmf_main}/doc/latex/chessfss/

%files -n texlive-chinesechess
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/chinesechess/
%doc %{_texmf_main}/doc/latex/chinesechess/

%files -n texlive-crossword
%license other-free.txt
%{_texmf_main}/tex/latex/crossword/
%doc %{_texmf_main}/doc/latex/crossword/

%files -n texlive-crosswrd
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/crosswrd/
%doc %{_texmf_main}/doc/latex/crosswrd/

%files -n texlive-customdice
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/customdice/
%doc %{_texmf_main}/doc/latex/customdice/

%files -n texlive-egameps
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/egameps/
%doc %{_texmf_main}/doc/latex/egameps/

%files -n texlive-eigo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/eigo/
%doc %{_texmf_main}/doc/latex/eigo/

%files -n texlive-gamebook
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gamebook/
%doc %{_texmf_main}/doc/latex/gamebook/

%files -n texlive-gamebooklib
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gamebooklib/
%doc %{_texmf_main}/doc/latex/gamebooklib/

%files -n texlive-go
%license pd.txt
%{_texmf_main}/fonts/source/public/go/
%{_texmf_main}/fonts/tfm/public/go/
%{_texmf_main}/tex/latex/go/
%doc %{_texmf_main}/doc/fonts/go/

%files -n texlive-hanoi
%license pd.txt
%{_texmf_main}/tex/plain/hanoi/

%files -n texlive-havannah
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/havannah/
%doc %{_texmf_main}/doc/latex/havannah/

%files -n texlive-hexboard
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/hexboard/
%doc %{_texmf_main}/doc/latex/hexboard/

%files -n texlive-hexgame
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hexgame/
%doc %{_texmf_main}/doc/latex/hexgame/

%files -n texlive-hmtrump
%license cc-by-sa-4.txt
%{_texmf_main}/fonts/truetype/public/hmtrump/
%{_texmf_main}/tex/lualatex/hmtrump/
%doc %{_texmf_main}/doc/lualatex/hmtrump/

%files -n texlive-horoscop
%license pd.txt
%{_texmf_main}/tex/latex/horoscop/
%doc %{_texmf_main}/doc/latex/horoscop/

%files -n texlive-jeuxcartes
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jeuxcartes/
%doc %{_texmf_main}/doc/latex/jeuxcartes/

%files -n texlive-jigsaw
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/jigsaw/
%doc %{_texmf_main}/doc/latex/jigsaw/

%files -n texlive-labyrinth
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/labyrinth/
%doc %{_texmf_main}/doc/latex/labyrinth/

%files -n texlive-logicpuzzle
%license lppl1.3c.txt
%{_texmf_main}/scripts/logicpuzzle/
%{_texmf_main}/tex/latex/logicpuzzle/
%doc %{_texmf_main}/doc/latex/logicpuzzle/

%files -n texlive-mahjong
%license mit.txt
%{_texmf_main}/tex/latex/mahjong/
%doc %{_texmf_main}/doc/latex/mahjong/

%files -n texlive-mathador
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mathador/
%doc %{_texmf_main}/doc/latex/mathador/

%files -n texlive-maze
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/maze/
%doc %{_texmf_main}/doc/latex/maze/

%files -n texlive-multi-sudoku
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/multi-sudoku/
%doc %{_texmf_main}/doc/latex/multi-sudoku/

%files -n texlive-musikui
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/musikui/
%doc %{_texmf_main}/doc/latex/musikui/

%files -n texlive-nimsticks
%license mit.txt
%{_texmf_main}/tex/latex/nimsticks/
%doc %{_texmf_main}/doc/latex/nimsticks/

%files -n texlive-onedown
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/onedown/
%doc %{_texmf_main}/doc/latex/onedown/

%files -n texlive-othello
%license gpl2.txt
%{_texmf_main}/fonts/source/public/othello/
%{_texmf_main}/fonts/tfm/public/othello/
%{_texmf_main}/tex/latex/othello/
%doc %{_texmf_main}/doc/latex/othello/

%files -n texlive-othelloboard
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/othelloboard/
%doc %{_texmf_main}/doc/latex/othelloboard/

%files -n texlive-pas-crosswords
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pas-crosswords/
%doc %{_texmf_main}/doc/latex/pas-crosswords/

%files -n texlive-pgf-go
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgf-go/
%doc %{_texmf_main}/doc/latex/pgf-go/

%files -n texlive-playcards
%license lgpl.txt
%{_texmf_main}/tex/latex/playcards/
%doc %{_texmf_main}/doc/latex/playcards/

%files -n texlive-psgo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/psgo/
%doc %{_texmf_main}/doc/latex/psgo/

%files -n texlive-quizztex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quizztex/
%doc %{_texmf_main}/doc/latex/quizztex/

%files -n texlive-realtranspose
%license mit.txt
%{_texmf_main}/tex/latex/realtranspose/
%doc %{_texmf_main}/doc/latex/realtranspose/

%files -n texlive-reverxii
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/reverxii/
%doc %{_texmf_main}/doc/generic/reverxii/

%files -n texlive-rouequestions
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rouequestions/
%doc %{_texmf_main}/doc/latex/rouequestions/

%files -n texlive-rpgicons
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/rpgicons/
%doc %{_texmf_main}/doc/latex/rpgicons/

%files -n texlive-schwalbe-chess
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/schwalbe-chess/
%doc %{_texmf_main}/doc/latex/schwalbe-chess/

%files -n texlive-scrabble
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/scrabble/
%doc %{_texmf_main}/doc/latex/scrabble/

%files -n texlive-sgame
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sgame/
%doc %{_texmf_main}/doc/latex/sgame/

%files -n texlive-skak
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/skak/
%{_texmf_main}/fonts/tfm/public/skak/
%{_texmf_main}/tex/latex/skak/
%doc %{_texmf_main}/doc/latex/skak/

%files -n texlive-skaknew
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/skaknew/
%{_texmf_main}/fonts/map/dvips/skaknew/
%{_texmf_main}/fonts/opentype/public/skaknew/
%{_texmf_main}/fonts/tfm/public/skaknew/
%{_texmf_main}/fonts/type1/public/skaknew/
%doc %{_texmf_main}/doc/fonts/skaknew/
%{_datadir}/fonts/skaknew
%{_datadir}/appdata/skaknew.metainfo.xml

%files -n texlive-soup
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/soup/
%doc %{_texmf_main}/doc/latex/soup/

%files -n texlive-sudoku
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sudoku/
%doc %{_texmf_main}/doc/latex/sudoku/

%files -n texlive-sudokubundle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sudokubundle/
%doc %{_texmf_main}/doc/latex/sudokubundle/

%files -n texlive-tangramtikz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tangramtikz/
%doc %{_texmf_main}/doc/latex/tangramtikz/

%files -n texlive-thematicpuzzle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thematicpuzzle/
%doc %{_texmf_main}/doc/latex/thematicpuzzle/

%files -n texlive-tictactoe
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/tictactoe/
%doc %{_texmf_main}/doc/latex/tictactoe/

%files -n texlive-tikz-triminos
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tikz-triminos/
%doc %{_texmf_main}/doc/latex/tikz-triminos/

%files -n texlive-trivialpursuit
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/trivialpursuit/
%doc %{_texmf_main}/doc/latex/trivialpursuit/

%files -n texlive-twoxtwogame
%license apache2.txt
%{_texmf_main}/tex/latex/twoxtwogame/
%doc %{_texmf_main}/doc/latex/twoxtwogame/

%files -n texlive-wargame
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/wargame/
%doc %{_texmf_main}/doc/latex/wargame/

%files -n texlive-weiqi
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/weiqi/
%doc %{_texmf_main}/doc/latex/weiqi/

%files -n texlive-wordle
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/wordle/
%doc %{_texmf_main}/doc/latex/wordle/

%files -n texlive-xq
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/xq/
%{_texmf_main}/fonts/tfm/public/xq/
%{_texmf_main}/tex/latex/xq/
%doc %{_texmf_main}/doc/fonts/xq/

%files -n texlive-xskak
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xskak/
%doc %{_texmf_main}/doc/latex/xskak/

%changelog
* Tue Jan 20 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76381-2
- fix licensing
- validate appdata

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76381-1
- Update to svn76381
- update components
- fix descriptions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75941-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75941-1
- Update to TeX Live 2025
