%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-context
Epoch:          12
Version:        svn75426
Release:        3%{?dist}
Summary:        ConTeXt and packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-context.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-animation.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-animation.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-calendar-examples.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-calendar-examples.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-chat.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-chat.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-collating-marks.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-collating-marks.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-cyrillicnumbers.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-cyrillicnumbers.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-filter.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-filter.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-gnuplot.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-gnuplot.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-handlecsv.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-handlecsv.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-letter.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-letter.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-mathsets.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-mathsets.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-notes-zh-cn.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-notes-zh-cn.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-pocketdiary.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-pocketdiary.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-simpleslides.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-simpleslides.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-squares.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-squares.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-sudoku.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-sudoku.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-transliterator.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-transliterator.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-typescripts.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-typescripts.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-vim.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-vim.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-visualcounter.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-visualcounter.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jmn.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-context
Requires:       texlive-context-animation
Requires:       texlive-context-calendar-examples
Requires:       texlive-context-chat
Requires:       texlive-context-collating-marks
Requires:       texlive-context-cyrillicnumbers
Requires:       texlive-context-filter
Requires:       texlive-context-gnuplot
Requires:       texlive-context-handlecsv
Requires:       texlive-context-legacy
Requires:       texlive-context-letter
Requires:       texlive-context-mathsets
Requires:       texlive-context-notes-zh-cn
Requires:       texlive-context-pocketdiary
Requires:       texlive-context-simpleslides
Requires:       texlive-context-squares
Requires:       texlive-context-sudoku
Requires:       texlive-context-transliterator
Requires:       texlive-context-typescripts
Requires:       texlive-context-vim
Requires:       texlive-context-visualcounter
Requires:       texlive-jmn
Requires:       texlive-luajittex

%description
Hans Hagen's powerful ConTeXt system, https://pragma-ade.com. Also includes
third-party ConTeXt packages. TeX Live uses the ConTeXt repackaging as
distributed from https://github.com/gucci-on-fleek/context-packaging. See
https://contextgarden.net and https://pragma-ade.com for information about
ConTeXt.#


%package -n texlive-context-animation
Summary:        Generate fieldstack based animation with ConTeXt
Version:        svn75386
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-animation
The package is a port, to Context (mkvi), of the corresponding LaTeX package.

%package -n texlive-context-calendar-examples
Summary:        Collection of calendars based on the PocketDiary-module
Version:        svn66947
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-calendar-examples
The module contains examples for creating calendars based on the
PocketDiary-module in various page sizes. In this collection there are the
following examples: Year calendar with 1 day per page Year calendar with 1 week
per two facing pages Menu-Calendar for each week of the year Sun data and moon
data calendar for the whole year Photo calendar

%package -n texlive-context-chat
Summary:        Typeset messenger chats with ConTEXt
Version:        svn72010
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-chat
A simplified way to typeset a digital chat between characters.

%package -n texlive-context-collating-marks
Summary:        Environment to place collating marks on the spine of a section
Version:        svn68696
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-collating-marks
This module provides a possibility to place collating marks on the spines of
sections when using imposition. Placing collating marks is a method to make the
correct sequence of sections of a book block visible.

%package -n texlive-context-cyrillicnumbers
Summary:        Write numbers as cyrillic glyphs
Version:        svn47085
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-cyrillicnumbers
The package extends ConTeXt's system of number conversion, by adding numeration
using cyrillic letters.

%package -n texlive-context-filter
Summary:        Run external programs on the contents of a start-stop environment
Version:        svn62070
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-filter
The filter module provides a simple interface to run external programs on the
contents of a start-stop environment. Options are available to run the external
program only if the content of the environment has changed, to specify how the
program output should be read back, and to choose the name of the temporary
files that are created. The module is compatible with both MkII and MkIV.

%package -n texlive-context-gnuplot
Summary:        Inclusion of Gnuplot graphs in ConTeXt
Version:        svn75301
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-gnuplot
Enables simple creation and inclusion of graphs with Gnuplot. The package
writes a script into temporary file, runs Gnuplot and includes the resulting
graphic directly into the document. See the ConTeXt Garden package page for
further details.

%package -n texlive-context-handlecsv
Summary:        Data merging for automatic document creation
Version:        svn76721
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(t-handlecsv.tex) = %{tl_version}

%description -n texlive-context-handlecsv
The package handles csv data merging for automatic document creation.

%package -n texlive-context-letter
Summary:        ConTeXt package for writing letters
Version:        svn60787
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-letter
A means of writing 'vanilla' letters and memos is provided, with support
covering ConTeXt Mkii and Mkiv. The design of letters may be amended by a wide
range of style specifications.

%package -n texlive-context-mathsets
Summary:        Set notation in ConTeXt
Version:        svn47085
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(t-mathsets.tex) = %{tl_version}

%description -n texlive-context-mathsets
Typeset good-looking set notation (e.g., {x|x \in Y}), as well as similar
things such as Dirac bra-ket notation, conditional probabilities, etc. The
package is at least inspired by braket.

%package -n texlive-context-notes-zh-cn
Summary:        A ConTeXt LMTX introduction for Chinese users
Version:        svn76286
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-context-notes-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-context-notes-zh-cn-doc <= 11:%{version}
Requires:       texlive-context

%description -n texlive-context-notes-zh-cn
An introductory tutorial on ConTeXt, in Chinese. The document covers ConTeXt
installation, fonts, layout design, cross-reference, project structure, metafun
and presentation design.

%package -n texlive-context-pocketdiary
Summary:        A personal organiser
Version:        svn73164
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-pocketdiary
PocketDiary is a calendar module, enabling to prepare various calendars from
day- to week, month- and year-calendars based on the ideas contained in
PocketMods, having 8 pages arranged on a A4 single-sided printed sheet of
paper. The module comes with different templates for notes etc. The module
provides sun and moon data calculations

%package -n texlive-context-simpleslides
Summary:        A module for preparing presentations
Version:        svn67070
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(s-simpleslides-BigNumber.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BlackBoard.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BottomSquares.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Boxed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BoxedTitle.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Ellipse.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Embossed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Framed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FramedTitle.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FuzzyFrame.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FuzzyTopic.tex) = %{tl_version}
Provides:       tex(s-simpleslides-HorizontalStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-NarrowStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-PlainCounter.tex) = %{tl_version}
Provides:       tex(s-simpleslides-RainbowStripe.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Rounded.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Shaded.tex) = %{tl_version}
Provides:       tex(s-simpleslides-SideSquares.tex) = %{tl_version}
Provides:       tex(s-simpleslides-SideToc.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Split.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Sunrise.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Swoosh.tex) = %{tl_version}
Provides:       tex(s-simpleslides-ThickStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-default.tex) = %{tl_version}

%description -n texlive-context-simpleslides
This ConTeXt module provides an easy-to-use interface for creating
presentations for use with a digital projector. The presentations are not
interactive (no buttons, hyperlinks or navigational tools such as tables of
contents). Graphics may be mixed with the text of slides. The module provides
several predefined styles, designed for academic presentation. Most styles are
configurable, and it is easy to design new styles.

%package -n texlive-context-squares
Summary:        Typesetting Magic and Latin squares
Version:        svn70128
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-squares
The package provides typesetting of magic and latin squares.

%package -n texlive-context-sudoku
Summary:        Sudokus for ConTeXt
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-sudoku
A port of Peter Norvig's sudoku solver to Lua/ConTeXt. It provides four basic
commands for typesetting sudokus, as well as a command handler.

%package -n texlive-context-transliterator
Summary:        Transliterate text from 'other' alphabets
Version:        svn61127
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(t-transliterator.tex) = %{tl_version}

%description -n texlive-context-transliterator
The package will read text in one alphabet, and provide a transliterated
version in another; this is useful for readers who cannot read the original
alphabet. The package can make allowance for hyphenation.

%package -n texlive-context-typescripts
Summary:        Small modules to load various fonts for use in ConTeXt
Version:        svn76524
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-typescripts
The package provides files offering interfaces to 33 publicly available fonts
(or collections of fonts from the same foundry); each is available in a .mkii
and a .mkiv version.

%package -n texlive-context-vim
Summary:        Generate ConTeXt syntax highlighting code from vim
Version:        svn62071
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Requires:       texlive-context-filter
Provides:       tex(t-vim.tex) = %{tl_version}

%description -n texlive-context-vim
ConTeXt has excellent pretty printing capabilities for many languages. The code
for pretty printing is written in TeX, and due to catcode juggling, such
verbatim typesetting is perhaps the trickiest part of TeX. This makes it
difficult for a "normal" user to define syntax highlighting rules for a new
language. This module takes the onus of defining syntax highlighting rules away
from the user and uses ViM editor to generate the syntax highlighting. There is
a helper 2context.vim script to do the syntax parsing in ViM.

%package -n texlive-context-visualcounter
Summary:        Visual display of ConTeXt counters
Version:        svn47085
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-visualcounter
A typical document usually contains many counters: page numbers, section
numbers, itemizations, enumerations, theorems, and so on. This module provides
a visual display for such counters.

%package -n texlive-jmn
Summary:        Special fonts for ConTeXt
Version:        svn45751
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jmn
special fonts for ConTeXt


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-context-animation
%license gpl3.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-calendar-examples
%license pd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-chat
%license gpl3.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-collating-marks
%license pd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-cyrillicnumbers
%license bsd.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-filter
%license bsd2.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-gnuplot
%license gpl2.txt
%{_texmf_main}/metapost/context/third/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-handlecsv
%license gpl3.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-letter
%license gpl2.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-mathsets
%license bsd2.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-notes-zh-cn
%license fdl.txt
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-pocketdiary
%license pd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-simpleslides
%license gpl2.txt
%{_texmf_main}/scripts/context/lua/
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-squares
%license mit.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-sudoku
%license mit.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-transliterator
%license bsd.txt
%{_texmf_main}/scripts/context/lua/
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-typescripts
%license gpl3.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-vim
%license bsd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-visualcounter
%license bsd2.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-jmn
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/jmn/hans/
%{_texmf_main}/fonts/enc/dvips/jmn/
%{_texmf_main}/fonts/map/dvips/jmn/
%{_texmf_main}/fonts/tfm/jmn/hans/
%{_texmf_main}/fonts/type1/jmn/hans/

%changelog
* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75426-3
- fix descriptions, uncapitalized summaries, licensing
- update to latest component versions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75426-2
- regenerated, no longer get deps from docs

* Thu Sep 18 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75426-1
- Update to TeX Live 2025
