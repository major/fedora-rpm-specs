%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langenglish
Epoch:          12
Version:        svn74022
Release:        3%{?dist}
Summary:        US and UK English

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langenglish.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amiweb2c-guide.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amiweb2c-guide.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscls-doc.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amscls-doc.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amslatex-primer.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amslatex-primer.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/around-the-bend.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/around-the-bend.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascii-chart.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ascii-chart.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asy-overview.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asy-overview.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-cheatsheet.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/biblatex-cheatsheet.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/components.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/components.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/comprehensive.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/comprehensive.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dickimaw.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dickimaw.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/docsurvey.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/docsurvey.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtxtut.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtxtut.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/first-latex-doc.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/first-latex-doc.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontinstallationguide.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontinstallationguide.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forest-quickstart.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/forest-quickstart.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guide-to-latex.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/guide-to-latex.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/happy4th.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/happy4th.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-english.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intro-scientific.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/intro-scientific.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-errata.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-errata.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-hint.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-hint.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-pdf.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-pdf.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-english.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-english.doc.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-brochure.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-brochure.doc.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-course.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-course.doc.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-doc-ptr.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-doc-ptr.doc.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-for-undergraduates.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-for-undergraduates.doc.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-graphics-companion.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-graphics-companion.doc.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-refsheet.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-refsheet.doc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-veryshortguide.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-veryshortguide.doc.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-web-companion.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-web-companion.doc.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo.doc.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4wp.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex4wp.doc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcheat.doc.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcourse-rug.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexcourse-rug.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexfileinfo-pkgs.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexfileinfo-pkgs.doc.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-english.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-english.doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/macros2e.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/macros2e.doc.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/math-into-latex-4.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/math-into-latex-4.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maths-symbols.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/maths-symbols.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memdesign.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memdesign.doc.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memoirchapterstyles.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/memoirchapterstyles.doc.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metafont-beginners.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metafont-beginners.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost-examples.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost-examples.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/patgen2-tutorial.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/patgen2-tutorial.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictexsum.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pictexsum.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plain-doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plain-doc.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-en.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-en.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/short-math-guide.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/short-math-guide.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplified-latex.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/simplified-latex.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svg-inkscape.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svg-inkscape.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tamethebeast.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tamethebeast.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tds.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tds.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-font-errors-cheatsheet.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-font-errors-cheatsheet.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-nutshell.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-nutshell.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-overview.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-overview.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-vpat.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-vpat.doc.tar.xz
Source117:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texbytopic.tar.xz
Source118:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texbytopic.doc.tar.xz
Source119:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texonly.tar.xz
Source120:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texonly.doc.tar.xz
Source121:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/titlepages.tar.xz
Source122:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/titlepages.doc.tar.xz
Source123:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlc2.tar.xz
Source124:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlc2.doc.tar.xz
Source125:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlc3-examples.tar.xz
Source126:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlc3-examples.doc.tar.xz
Source127:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlmgrbasics.tar.xz
Source128:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlmgrbasics.doc.tar.xz
Source129:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typstfun.tar.xz
Source130:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typstfun.doc.tar.xz
Source131:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undergradmath.tar.xz
Source132:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/undergradmath.doc.tar.xz
Source133:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualfaq.tar.xz
Source134:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualfaq.doc.tar.xz
Source135:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/webguide.tar.xz
Source136:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/webguide.doc.tar.xz
Source137:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wrapstuff-doc-en.tar.xz
Source138:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wrapstuff-doc-en.doc.tar.xz
Source139:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexref.tar.xz
Source140:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetexref.doc.tar.xz
Source141:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yet-another-guide-latex2e.tar.xz
Source142:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yet-another-guide-latex2e.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-amiweb2c-guide
Requires:       texlive-amscls-doc
Requires:       texlive-amslatex-primer
Requires:       texlive-around-the-bend
Requires:       texlive-ascii-chart
Requires:       texlive-asy-overview
Requires:       texlive-biblatex-cheatsheet
Requires:       texlive-collection-basic
Requires:       texlive-components
Requires:       texlive-comprehensive
Requires:       texlive-dickimaw
Requires:       texlive-docsurvey
Requires:       texlive-dtxtut
Requires:       texlive-first-latex-doc
Requires:       texlive-fontinstallationguide
Requires:       texlive-forest-quickstart
Requires:       texlive-guide-to-latex
Requires:       texlive-happy4th
Requires:       texlive-hyphen-english
Requires:       texlive-impatient
Requires:       texlive-intro-scientific
Requires:       texlive-knuth-errata
Requires:       texlive-knuth-hint
Requires:       texlive-knuth-pdf
Requires:       texlive-l2tabu-english
Requires:       texlive-latex-brochure
Requires:       texlive-latex-course
Requires:       texlive-latex-doc-ptr
Requires:       texlive-latex-for-undergraduates
Requires:       texlive-latex-graphics-companion
Requires:       texlive-latex-refsheet
Requires:       texlive-latex-veryshortguide
Requires:       texlive-latex-web-companion
Requires:       texlive-latex2e-help-texinfo
Requires:       texlive-latex4wp
Requires:       texlive-latexcheat
Requires:       texlive-latexcourse-rug
Requires:       texlive-latexfileinfo-pkgs
Requires:       texlive-lshort-english
Requires:       texlive-macros2e
Requires:       texlive-math-into-latex-4
Requires:       texlive-maths-symbols
Requires:       texlive-memdesign
Requires:       texlive-memoirchapterstyles
Requires:       texlive-metafont-beginners
Requires:       texlive-metapost-examples
Requires:       texlive-patgen2-tutorial
Requires:       texlive-pictexsum
Requires:       texlive-plain-doc
Requires:       texlive-quran-en
Requires:       texlive-short-math-guide
Requires:       texlive-simplified-latex
Requires:       texlive-svg-inkscape
Requires:       texlive-tamethebeast
Requires:       texlive-tds
Requires:       texlive-tex-font-errors-cheatsheet
Requires:       texlive-tex-nutshell
Requires:       texlive-tex-overview
Requires:       texlive-tex-vpat
Requires:       texlive-texbytopic
Requires:       texlive-texonly
Requires:       texlive-titlepages
Requires:       texlive-tlc2
Requires:       texlive-tlc3-examples
Requires:       texlive-tlmgrbasics
Requires:       texlive-typstfun
Requires:       texlive-undergradmath
Requires:       texlive-visualfaq
Requires:       texlive-webguide
Requires:       texlive-wrapstuff-doc-en
Requires:       texlive-xetexref
Requires:       texlive-yet-another-guide-latex2e

%description
Support for, and documentation in, English.


%package -n texlive-amiweb2c-guide
Summary:        How to install AmiWeb2c
Version:        svn56878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amiweb2c-guide-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amiweb2c-guide-doc <= 11:%{version}

%description -n texlive-amiweb2c-guide
This is a guide for the installation of (La)TeX with the Amiga port of Web2C
named AmiWeb2C in the version 2.1 on an emulated Amiga 4000 computer running
Workbench 3.1. Furthermore the installation of an ARexx server for calling
LaTeX from an editor is described and some tips for the installation of new
fonts are given.

%package -n texlive-amscls-doc
Summary:        User documentation for AMS document classes
Version:        svn46110
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amscls-doc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amscls-doc-doc <= 11:%{version}

%description -n texlive-amscls-doc
This collection comprises a set of four manuals, or Author Handbooks, each
documenting the use of a class of publications based on one of the AMS document
classes amsart, amsbook, amsproc and one "hybrid", as well as a guide to the
generation of the four manuals from a coordinated set of LaTeX source files.
The Handbooks comprise the user documentation for the pertinent document
classes. As the source for the Handbooks consists of a large number of files,
and the intended output is multiple different documents, the principles
underlying this collection can be used as a model for similar projects. The
manual "Compiling the AMS Author Handbooks" provides information about the
structure of and interaction between the various components.

%package -n texlive-amslatex-primer
Summary:        Getting up and running with AMS-LaTeX
Version:        svn28980
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amslatex-primer-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amslatex-primer-doc <= 11:%{version}

%description -n texlive-amslatex-primer
The document aims to get you up and running with AMS-LaTeX as quickly as
possible. These instructions (along with a template file template.tex) are not
a substitute for the full documentation, but they may get you started quickly
enough so that you will only need to refer to the main documentation
occasionally. In addition to 'AMS-LaTeX out of the box', the document contains:
a section describing how to draw commutative diagrams using Xy-pic; and a
section describing how to use amsrefs to create a bibliography.

%package -n texlive-around-the-bend
Summary:        Typeset exercises in TeX, with answers
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-around-the-bend-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-around-the-bend-doc <= 11:%{version}

%description -n texlive-around-the-bend
This is a typeset version of the files of the aro-bend, plus three extra
questions (with their answers) that Michael Downes didn't manage to get onto
CTAN.

%package -n texlive-ascii-chart
Summary:        An ASCII wall chart
Version:        svn20536
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ascii-chart-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ascii-chart-doc <= 11:%{version}

%description -n texlive-ascii-chart
The document may be converted between Plain TeX and LaTeX (2.09) by a simple
editing action.

%package -n texlive-asy-overview
Summary:        A brief overview of the Asymptote language for drawing mathematical graphics
Version:        svn72484
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asy-overview-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asy-overview-doc <= 11:%{version}

%description -n texlive-asy-overview
Asymptote is a programming language for creating mathematical graphics. This
document gives you a quick overview, illustrating with a few familiar Calculus
examples. Readers can work through it in a couple of hours to get a feel for
the system's strengths, and if they are interested then go on to a full
tutorial or the official reference.

%package -n texlive-biblatex-cheatsheet
Summary:        BibLaTeX/Biber 'cheat sheet'
Version:        svn44685
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-biblatex-cheatsheet-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-biblatex-cheatsheet-doc <= 11:%{version}

%description -n texlive-biblatex-cheatsheet
A BibLaTeX/Biber 'cheat sheet' which I wrote because I wanted one to distribute
to students, but couldn't find an existing one.

%package -n texlive-components
Summary:        Components of TeX
Version:        svn63184
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-components-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-components-doc <= 11:%{version}

%description -n texlive-components
An introduction to the components and files users of TeX may encounter.

%package -n texlive-comprehensive
Summary:        Symbols accessible from LaTeX
Version:        svn69619
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-comprehensive-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-comprehensive-doc <= 11:%{version}

%description -n texlive-comprehensive
Over 20000 symbols accessible from LaTeX are listed in a set of tables
organized by topic and package. The aim is to make it easy to find symbols and
learn how to incorporate them into a LaTeX document. An index further helps
locate symbols of interest.

%package -n texlive-dickimaw
Summary:        Books and tutorials from the "Dickimaw LaTeX Series"
Version:        svn32925
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-dickimaw-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-dickimaw-doc <= 11:%{version}

%description -n texlive-dickimaw
The package provides some of the books and tutorials that form part of the
"Dickimaw LaTeX Series". Only the A4 PDF of each book is detailed here. Other
formats, such as HTML or screen optimized PDF, are available from the package
home page. Books included are: "LaTeX for Complete Novices": an introductory
guide to LaTeX. "Using LaTeX to Write a PhD Thesis": a follow-on from "LaTeX
for Complete Novices" geared towards students who want to use LaTeX to write
their PhD thesis. "Creating a LaTeX minimal example": describes how to create a
minimal example, which can be used as a debugging aid when you encounter errors
in your LaTeX documents.

%package -n texlive-docsurvey
Summary:        A survey of LaTeX documentation
Version:        svn70729
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-docsurvey-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-docsurvey-doc <= 11:%{version}

%description -n texlive-docsurvey
A survey of programming-related documentation for LaTeX. Included are
references to printed and electronic books and manuals, symbol lists, FAQs, the
LaTeX source code, CTAN and distributions, programming-related packages, users
groups and online communities, and information on creating packages and
documentation.

%package -n texlive-dtxtut
Summary:        Tutorial on writing .dtx and .ins files
Version:        svn69587
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-dtxtut-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-dtxtut-doc <= 11:%{version}

%description -n texlive-dtxtut
This tutorial is intended for advanced LaTeX2e users who want to learn how to
create .ins and .dtx files for distributing their homebrewed classes and
package files.

%package -n texlive-first-latex-doc
Summary:        A document for absolute LaTeX beginners
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-first-latex-doc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-first-latex-doc-doc <= 11:%{version}

%description -n texlive-first-latex-doc
The document leads a reader, who knows nothing about LaTeX, through the
production of a two page document. The user who has completed that first
document, and wants to carry on, will find recommendations for tutorials.

%package -n texlive-fontinstallationguide
Summary:        Font installation guide
Version:        svn59755
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fontinstallationguide-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fontinstallationguide-doc <= 11:%{version}

%description -n texlive-fontinstallationguide
This guide discusses the most common scenarios you are likely to encounter when
installing Type 1 PostScript fonts. While the individual tools employed in the
installation process are documented well, the actual difficulty most users are
facing when trying to install new fonts is understanding how to put all the
pieces together. This is what this guide is about.

%package -n texlive-forest-quickstart
Summary:        Quickstart Guide for Linguists package "forest"
Version:        svn55688
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-forest-quickstart-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-forest-quickstart-doc <= 11:%{version}

%description -n texlive-forest-quickstart
forest is a PGF/TikZ-based package for drawing linguistic (and other kinds of)
trees. This manual provides a quickstart guide for linguists with just the
essential things that you need to get started.

%package -n texlive-guide-to-latex
Summary:        Examples and more from Guide to LaTeX, by Kopka and Daly
Version:        svn45712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-guide-to-latex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-guide-to-latex-doc <= 11:%{version}

%description -n texlive-guide-to-latex
examples and more from Guide to LaTeX, by Kopka and Daly

%package -n texlive-happy4th
Summary:        A firework display in obfuscated TeX
Version:        svn25020
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-happy4th-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-happy4th-doc <= 11:%{version}

%description -n texlive-happy4th
The output PDF file gives an amusing display, as the reader pages through it.

%package -n texlive-hyphen-english
Summary:        English hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-en-gb.tex) = %{tl_version}
Provides:       tex(hyph-en-us.tex) = %{tl_version}
Provides:       tex(loadhyph-en-gb.tex) = %{tl_version}
Provides:       tex(loadhyph-en-us.tex) = %{tl_version}

%description -n texlive-hyphen-english
Additional hyphenation patterns for American and British English in ASCII
encoding. The American English patterns (usenglishmax) greatly extend the
standard patterns from Knuth to find many additional hyphenation points.
British English hyphenation is completely different from US English, so has its
own set of patterns.

%package -n texlive-impatient
Summary:        Free edition of the book "TeX for the Impatient"
Version:        svn54080
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-impatient-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-impatient-doc <= 11:%{version}

%description -n texlive-impatient
"TeX for the Impatient" is a book (of around 350 pages) on TeX, Plain TeX and
Eplain. The book is also available in French and Chinese translations.

%package -n texlive-intro-scientific
Summary:        Introducing scientific/mathematical documents using LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-intro-scientific-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-intro-scientific-doc <= 11:%{version}

%description -n texlive-intro-scientific
"Writing Scientific Documents Using LaTeX" is an article introducing the use of
LaTeX in typesetting scientific documents. It covers the basics of creating a
new LaTeX document, special typesetting considerations, mathematical
typesetting and graphics. It also touches on bibliographic data and BibTeX.

%package -n texlive-knuth-errata
Summary:        Knuth's published errata
Version:        svn58682
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-knuth-errata-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-knuth-errata-doc <= 11:%{version}

%description -n texlive-knuth-errata
These files record details of problems reported in Knuth's 'Computers and
Typesetting' series of books, for the Computer Modern fonts, and for TeX,
Metafont and related programs.

%package -n texlive-knuth-hint
Summary:        HINT collection of typeset C/WEB sources in TeX Live
Version:        svn74654
License:        LicenseRef-Fedora-Public-Domain AND Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-knuth-hint-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-knuth-hint-doc <= 11:%{version}

%description -n texlive-knuth-hint
The knuth-hint package contains the large collection of HINT documents for many
of the CWEB amd WEB sources of programs in the TeX Live distribution (and, for
technical reasons, a PDF document for XeTeX). Each program is presented in its
original form as written by the respective authors, and in the "changed" form
as used in TeX Live. Care has been taken to keep the section numbering intact,
so that you can study the codes and the changes in parallel. Also included are
the "errata" for Donald Knuth's "Computers & Typesetting". HINT is the dynamic
document format created by Martin Ruckert's HiTeX engine that was added to TeX
Live 2022. The HINT files can be viewed on Linux, Windows, and Android with the
hintview application. The knuth-hint package is a showcase of HiTeX's
capabilities.

%package -n texlive-knuth-pdf
Summary:        PDF collection of typeset C/WEB sources in TeX Live
Version:        svn74653
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-knuth-pdf-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-knuth-pdf-doc <= 11:%{version}

%description -n texlive-knuth-pdf
Here you find a large collection of PDF documents for many C/WEB programs in
TeX Live, both in their original form as written by their respective authors,
and in the changed form as they are actually used in the TeX Live system. Care
has been taken to keep the section numbering intact, so that you can study the
sources and their changes in parallel. Also included is the collection of
"errata" for Donald Knuth's "Computers & Typesetting series". Although not all
the texts here are written or maintained by Donald Knuth, it is more convenient
for everything to be collected in one place for reading and searching. They all
stem from the system that Knuth created. The central entry point is the "index"
file, with links to the individual documents, either in HTML or in PDF format.

%package -n texlive-l2tabu-english
Summary:        English translation of "Obsolete packages and commands"
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l2tabu-english-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l2tabu-english-doc <= 11:%{version}

%description -n texlive-l2tabu-english
English translation of the l2tabu practical guide to LaTeX2e by Mark Trettin. A
list of obsolete packages and commands.

%package -n texlive-latex-brochure
Summary:        A publicity flyer for LaTeX
Version:        svn40612
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-brochure-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-brochure-doc <= 11:%{version}

%description -n texlive-latex-brochure
The document is designed as a publicity flyer for LaTeX, but also serves as an
interesting showcase of what LaTeX can do. The flyer is designed for printing,
double-sided, on A3 paper, which would then be folded once.

%package -n texlive-latex-course
Summary:        A LaTeX course as a projected presentation
Version:        svn68681
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-course-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-course-doc <= 11:%{version}

%description -n texlive-latex-course
A brief Beamer-based slide presentation on LaTeX, based on Rupprecht's LaTeX
2.09 course, which the author has translated to English and taken to
LaTeX2e/Beamer. Additional material was taken from the Short Introduction to
LaTeX.

%package -n texlive-latex-doc-ptr
Summary:        A direction-finder for LaTeX resources available online
Version:        svn77050
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-doc-ptr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-doc-ptr-doc <= 11:%{version}

%description -n texlive-latex-doc-ptr
A brief set of recommendations for users who need online documentation of
LaTeX. The document supports the need for documentation of LaTeX itself, in
distributions. For example, it could be used in the command texdoc latex, in
the TeX Live distribution.

%package -n texlive-latex-for-undergraduates
Summary:        A tutorial aimed at introducing undergraduate students to LaTeX
Version:        svn70199
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-for-undergraduates-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-for-undergraduates-doc <= 11:%{version}

%description -n texlive-latex-for-undergraduates
A tutorial aimed at introducing undergraduate students to LaTeX, including an
introduction to LaTeX Workshop in Visual Studio Code and an example package of
user-defined LaTeX commands.

%package -n texlive-latex-graphics-companion
Summary:        Examples from The LaTeX Graphics Companion
Version:        svn29235
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-graphics-companion-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-graphics-companion-doc <= 11:%{version}

%description -n texlive-latex-graphics-companion
The source of the examples printed in the book, together with necessary
supporting files.

%package -n texlive-latex-refsheet
Summary:        LaTeX Reference Sheet for a thesis with KOMA-Script
Version:        svn45076
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-refsheet-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-refsheet-doc <= 11:%{version}

%description -n texlive-latex-refsheet
This LaTeX Reference Sheet is for writing a thesis using the KOMA-Script
document classes (scrartcl, scrreprt, scrbook) and all the packages needed for
a thesis in natural sciences.

%package -n texlive-latex-veryshortguide
Summary:        The Very Short Guide to LaTeX
Version:        svn55228
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-veryshortguide-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-veryshortguide-doc <= 11:%{version}

%description -n texlive-latex-veryshortguide
This is a 4-page reminder of what LaTeX does. It is designed for printing on A4
paper, double-sided, and folding once to A5. Such an 'imposed' version of the
document is provided in the distribution, as PDF. An analogous version is
provided in 'legal' format.

%package -n texlive-latex-web-companion
Summary:        Examples from The LaTeX Web Companion
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-web-companion-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-web-companion-doc <= 11:%{version}

%description -n texlive-latex-web-companion
The source of the examples printed in the book, together with necessary
supporting files.

%package -n texlive-latex2e-help-texinfo
Summary:        Unofficial reference manual covering LaTeX2e
Version:        svn71252
License:        Latex2e
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex2e-help-texinfo-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex2e-help-texinfo-doc <= 11:%{version}

%description -n texlive-latex2e-help-texinfo
The manual is provided as Texinfo source (which was originally derived from the
VMS help file in the DECUS TeX distribution of 1990, with many subsequent
changes). This is a collaborative development, and details of getting involved
are to be found on the package home page. A Spanish translation is included
here, and a French translation is available as a separate package. All the
other formats in the distribution are derived from the Texinfo source, as
usual.

%package -n texlive-latex4wp
Summary:        A LaTeX guide specifically designed for word processor users
Version:        svn68096
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex4wp-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex4wp-doc <= 11:%{version}

%description -n texlive-latex4wp
"LaTeX for Word Processor Users" is a guide that helps converting knowledge and
techniques of word processing into the LaTeX typesetting environment. It aims
at helping WP users use LaTeX instead.

%package -n texlive-latexcheat
Summary:        A LaTeX cheat sheet
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcheat-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcheat-doc <= 11:%{version}

%description -n texlive-latexcheat
A LaTeX reference sheet for writing scientific papers. Unlike many other such
sheets, this sheet does not focus on typesetting mathematics (though it does
list some symbols).

%package -n texlive-latexcourse-rug
Summary:        A LaTeX course book
Version:        svn39026
License:        FSFAP
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latexcourse-rug-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latexcourse-rug-doc <= 11:%{version}

%description -n texlive-latexcourse-rug
The package provides the book and practice files for a LaTeX course that the
author has give several times at the Rijksuniversiteit Groningen (Netherlands).

%package -n texlive-latexfileinfo-pkgs
Summary:        A comparison of packages showing LaTeX file information
Version:        svn26760
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-latexfileinfo-pkgs
The package provides an HTML file that lists and compares CTAN packages that
display LaTeX source file information from \ProvidesClass, \ProvidesFile, and
\ProvidesPackage commands in the LaTeX file. Five packages of the author's, and
several other packages are discussed; revision control systems are mentioned
briefly.

%package -n texlive-lshort-english
Summary:        A (Not So) Short Introduction to LaTeX2e
Version:        svn58309
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-english-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-english-doc <= 11:%{version}

%description -n texlive-lshort-english
The document derives from a German introduction ('lkurz'), which was translated
and updated; it continues to be updated. This translation has, in its turn,
been translated into several other languages; see the lshort catalogue entry
for the current list.

%package -n texlive-macros2e
Summary:        A list of internal LaTeX2e macros
Version:        svn77050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(hyperref.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(zref-abspos.sty)
Requires:       tex(zref-user.sty)
Provides:       tex(extlabels.sty) = %{tl_version}

%description -n texlive-macros2e
This document lists the internal macros defined by the LaTeX2e base files which
can also be useful to package authors. The macros are hyper-linked to their
description in source2e. For this to work both PDFs must be inside the same
directory. This document is not yet complete in content and format and may miss
some macros.

%package -n texlive-math-into-latex-4
Summary:        Samples from Math into LaTeX, 4th Edition
Version:        svn44131
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-math-into-latex-4-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-math-into-latex-4-doc <= 11:%{version}

%description -n texlive-math-into-latex-4
Samples for the book `(More) Math into LaTeX', 4th edition. In addition, there
are two excerpts from the book: A Short Course to help you get started quickly
with LaTeX, including detailed instructions on how to install LaTeX on a PC or
a Mac; Math and Text Symbol Tables.

%package -n texlive-maths-symbols
Summary:        Summary of mathematical symbols available in LaTeX
Version:        svn37763
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-maths-symbols-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-maths-symbols-doc <= 11:%{version}

%description -n texlive-maths-symbols
A predecessor of the comprehensive symbols list, covering mathematical symbols
available in standard LaTeX (including the AMS symbols, if available at compile
time).

%package -n texlive-memdesign
Summary:        Notes on book design
Version:        svn48664
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-memdesign-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-memdesign-doc <= 11:%{version}

%description -n texlive-memdesign
"A Few Notes on Book Design" provides an introduction to the business of book
design. It is an extended version of what used to be the first part of the
memoir users' manual. Please note that the compiled copy, supplied in the
package, uses commercial fonts; the README file contains instructions on how to
compile the document without these fonts.

%package -n texlive-memoirchapterstyles
Summary:        Chapter styles in memoir class
Version:        svn59766
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-memoirchapterstyles-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-memoirchapterstyles-doc <= 11:%{version}

%description -n texlive-memoirchapterstyles
A showcase of chapter styles available to users of memoir: the six provided in
the class itself, plus many from elsewhere (by the present author and others).
The package's resources apply only to memoir, but the package draws from a
number of sources relating to standard classes, including the fncychap package,
and Vincent Zoonekynd's tutorial on headings.

%package -n texlive-metafont-beginners
Summary:        An introductory tutorial for Metafont
Version:        svn29803
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-metafont-beginners-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-metafont-beginners-doc <= 11:%{version}

%description -n texlive-metafont-beginners
An old introduction to the use of Metafont, that has stood the test of time. It
focuses on using the program, rather than designing fonts, but does offer
advice about understanding errors in other people's fonts.

%package -n texlive-metapost-examples
Summary:        Example drawings using MetaPost
Version:        svn15878
License:        GPL-1.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-metapost-examples-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-metapost-examples-doc <= 11:%{version}

%description -n texlive-metapost-examples
These are a few (hundred) example pictures drawn with MetaPost, ranging from
very simple (lines and circles) to rather intricate (uncommon geometric
transformations, fractals, bitmap, etc).

%package -n texlive-patgen2-tutorial
Summary:        A tutorial on the use of Patgen 2
Version:        svn58841
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-patgen2-tutorial-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-patgen2-tutorial-doc <= 11:%{version}

%description -n texlive-patgen2-tutorial
This document describes the use of Patgen 2 to create hyphenation patterns for
wide ranges of languages.

%package -n texlive-pictexsum
Summary:        A summary of PicTeX commands
Version:        svn24965
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-pictexsum-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pictexsum-doc <= 11:%{version}

%description -n texlive-pictexsum
The document summarises the commands of PicTeX. While it is no substitute for
the PicTeX manual itself (available from Personal TeX inc.), the document is a
useful aide-memoire for those who have read the manual.

%package -n texlive-plain-doc
Summary:        A list of plain.tex cs names
Version:        svn28424
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-plain-doc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-plain-doc-doc <= 11:%{version}

%description -n texlive-plain-doc
The document constitutes a list of every control sequence name (csname)
described in the TeXbook, together with an indication of whether the csname is
a primitive TeX command, or is defined in plain.tex

%package -n texlive-quran-en
Summary:        English translation extension to the quran package
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-en.sty) = %{tl_version}
Provides:       tex(qurantext-enii.translation.def) = %{tl_version}
Provides:       tex(qurantext-eniii.translation.def) = %{tl_version}
Provides:       tex(qurantext-eniv.translation.def) = %{tl_version}
Provides:       tex(qurantext-enix.translation.def) = %{tl_version}
Provides:       tex(qurantext-env.translation.def) = %{tl_version}
Provides:       tex(qurantext-envi.translation.def) = %{tl_version}
Provides:       tex(qurantext-envii.translation.def) = %{tl_version}
Provides:       tex(qurantext-enviii.translation.def) = %{tl_version}
Provides:       tex(qurantext-enx.translation.def) = %{tl_version}
Provides:       tex(qurantext-enxi.translation.def) = %{tl_version}
Provides:       tex(qurantext-enxii.translation.def) = %{tl_version}
Provides:       tex(qurantext-enxiii.translation.def) = %{tl_version}
Provides:       tex(qurantext-enxiv.translation.def) = %{tl_version}
Provides:       tex(qurantext-enxv.translation.def) = %{tl_version}
Provides:       tex(qurantext-enxvi.translation.def) = %{tl_version}

%description -n texlive-quran-en
This package is designed for typesetting multiple English translations of the
Holy Quran. It adds 15 additional English translations to the quran package.

%package -n texlive-short-math-guide
Summary:        Guide to using amsmath and related packages to typeset mathematical notation with LaTeX
Version:        svn46126
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-short-math-guide-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-short-math-guide-doc <= 11:%{version}

%description -n texlive-short-math-guide
The Short Math Guide is intended to be a concise introduction to the use of the
facilities provided by amsmath and various other LaTeX packages for typesetting
mathematical notation. Originally created by Michael Downes of the American
Mathematical Society based only on amsmath, it has been brought up to date with
references to related packages and other useful information.

%package -n texlive-simplified-latex
Summary:        A Simplified Introduction to LaTeX
Version:        svn20620
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-simplified-latex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-simplified-latex-doc <= 11:%{version}

%description -n texlive-simplified-latex
An accessible introduction for the beginner.

%package -n texlive-svg-inkscape
Summary:        How to include an SVG image in LaTeX using Inkscape
Version:        svn32199
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-svg-inkscape-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-svg-inkscape-doc <= 11:%{version}

%description -n texlive-svg-inkscape
The document demonstrates the use of SVG images in LaTeX documents. Using the
"PDF+LaTeX output" option of Inkscape, it is possible to include SVG in
documents, in which LaTeX typesets the text. This results in uniform text style
throughout the document, including text in images; moreover, LaTeX commands may
be used in the image's text, providing such things as mathematics and
references. The document also describes how to automate the conversion from SVG
to PDF+LaTeX using Inkscape.

%package -n texlive-tamethebeast
Summary:        A manual about bibliographies and especially BibTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tamethebeast-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tamethebeast-doc <= 11:%{version}

%description -n texlive-tamethebeast
An (as-complete-as-possible) manual about bibliographies in LaTeX, and thus
mainly about BibTeX.

%package -n texlive-tds
Summary:        The TeX Directory Structure standard
Version:        svn64477
License:        Abstyles
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tds-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tds-doc <= 11:%{version}

%description -n texlive-tds
Defines a structure for placement of TeX-related files on an hierarchical file
system, in a way that is well-defined, and is readily implementable.

%package -n texlive-tex-font-errors-cheatsheet
Summary:        Cheat sheet outlining the most common TeX font errors
Version:        svn18314
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-font-errors-cheatsheet-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-font-errors-cheatsheet-doc <= 11:%{version}

%description -n texlive-tex-font-errors-cheatsheet
This is a compact three-pages document highlighting the TeX flow of integrating
fonts, and explains how some of the most common font-related error messages
occur. Also, hints are given on how to address those.

%package -n texlive-tex-nutshell
Summary:        A short document about TeX principles
Version:        svn70375
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-nutshell-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-nutshell-doc <= 11:%{version}

%description -n texlive-tex-nutshell
This document is meant for users who are looking for information about the
basics of TeX. Its main goal is its brevity. The pure TeX features are
described, no features provided by macro extensions. Only the last section
gives a summary of plain TeX macros.

%package -n texlive-tex-overview
Summary:        An overview of the development of TeX
Version:        svn41403
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-overview-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-overview-doc <= 11:%{version}

%description -n texlive-tex-overview
The document gives a short overview of TeX and its children, as well as the
macro packages LaTeX and ConTeXt.

%package -n texlive-tex-vpat
Summary:        TeX Accessibility Conformance Report
Version:        svn72067
License:        CC-BY-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-vpat-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-vpat-doc <= 11:%{version}

%description -n texlive-tex-vpat
TeX Accessibility Conformance Report based on ITI VPAT(R) guidelines. Currently
it covers TeX Live. Other distributions can be added if needed.

%package -n texlive-texbytopic
Summary:        Freed version of the book TeX by Topic
Version:        svn68950
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texbytopic-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texbytopic-doc <= 11:%{version}

%description -n texlive-texbytopic
An invaluable book, originally published by Addison-Wesley (who have released
their copyright -- their version of the book went out of print in the 1990s).
The book describes itself as "a TeXnician's reference", and covers the way TeX
(the engine) works in as much detail as most ordinary TeX programmers will ever
need to know. A printed copy of the book, slightly updated, may be had (for a
modest price) from DANTE. The original edition is available from Lulu. See the
package home page for details.

%package -n texlive-texonly
Summary:        A sample document in Plain TeX
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texonly-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texonly-doc <= 11:%{version}

%description -n texlive-texonly
A file written with TeX, not using any packages or sty-files, to be compiled
with TeX or pdfTeX only, not with LaTeX et al.

%package -n texlive-titlepages
Summary:        Sample titlepages, and how to code them
Version:        svn19457
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-titlepages-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-titlepages-doc <= 11:%{version}

%description -n texlive-titlepages
The document provides examples of over two dozen title page designs based on a
range of published books and theses, together with the LaTeX code used to
create them.

%package -n texlive-tlc2
Summary:        Examples from "The LaTeX Companion", second edition
Version:        svn26096
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tlc2-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tlc2-doc <= 11:%{version}

%description -n texlive-tlc2
The source of the examples printed in the book, together with necessary
supporting files. The book was published by Addison-Wesley, 2004, ISBN
0-201-36299-6.

%package -n texlive-tlc3-examples
Summary:        All examples from "The LaTeX Companion", third edition
Version:        svn65496
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tlc3-examples-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tlc3-examples-doc <= 11:%{version}

%description -n texlive-tlc3-examples
The PDFs (as used with spotcolor and trimming) and sources for all examples
from the third edition (Parts I+II), together with necessary supporting files.
The edition is published by Addison-Wesley, 2023, ISBN-13: 978-0-13-816648-9,
ISBN-10: 0-13-816648-X (bundle of Part I & II).

%package -n texlive-tlmgrbasics
Summary:        A simplified documentation for tlmgr
Version:        svn75236
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tlmgrbasics-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tlmgrbasics-doc <= 11:%{version}

%description -n texlive-tlmgrbasics
This package provides simplified documentation for tlmgr, the TeX Live Manager.
It describes the most commonly-used actions and options in a convenient format.

%package -n texlive-typstfun
Summary:        List of equivalent Typst function names of LaTeX commands
Version:        svn70018
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-typstfun-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-typstfun-doc <= 11:%{version}

%description -n texlive-typstfun
This documentation lists equivalent Typst function names of LaTeX commands.
Only math symbols provided by the LaTeX format or the amsmath bundle are
included.

%package -n texlive-undergradmath
Summary:        LaTeX Math for Undergraduates cheat sheet
Version:        svn57286
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-undergradmath-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-undergradmath-doc <= 11:%{version}

%description -n texlive-undergradmath
This is a cheat sheet for writing mathematics with LaTeX. It is aimed at US
undergraduates.

%package -n texlive-visualfaq
Summary:        A Visual LaTeX FAQ
Version:        svn61719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-visualfaq-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-visualfaq-doc <= 11:%{version}

%description -n texlive-visualfaq
Having trouble finding the answer to a LaTeX question? The Visual LaTeX FAQ is
an innovative new search interface that presents over a hundred typeset samples
of frequently requested document formatting. Simply click on a hyperlinked
piece of text and the Visual LaTeX FAQ will send your Web browser to the
appropriate page in the TeX FAQ.

%package -n texlive-webguide
Summary:        Brief guide to LaTeX tools for Web publishing
Version:        svn77050
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-webguide-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-webguide-doc <= 11:%{version}

%description -n texlive-webguide
The documentation constitutes an example of the package's own recommendations
(being presented both in PDF and HTML).

%package -n texlive-wrapstuff-doc-en
Summary:        English version of the wrapstuff package documentation
Version:        svn71835
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-wrapstuff-doc-en-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-wrapstuff-doc-en-doc <= 11:%{version}

%description -n texlive-wrapstuff-doc-en
This package provides an English translation of the documentation for the
wrapstuff package.

%package -n texlive-xetexref
Summary:        Reference documentation of XeTeX
Version:        svn73885
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-xetexref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xetexref-doc <= 11:%{version}

%description -n texlive-xetexref
The package comprises reference documentation for XeTeX detailing its extended
features.

%package -n texlive-yet-another-guide-latex2e
Summary:        A short guide to using LaTeX2e to typeset high quality documents
Version:        svn73469
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-yet-another-guide-latex2e-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-yet-another-guide-latex2e-doc <= 11:%{version}

%description -n texlive-yet-another-guide-latex2e
This document is a short guide to using LaTeX2e to typeset high quality
documents. It focuses on users of Windows and guides the reader through
installation, some of LaTeX's conventions, and creating the front matter, body
and end matter. The appendices contain a list of useful facilities not
otherwise covered in this document and a list of helpful resources.

%post -n texlive-hyphen-english
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ukenglish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ukenglish loadhyph-en-gb.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=british.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=british" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=UKenglish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=UKenglish" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ukenglish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ukenglish}{loadhyph-en-gb.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{british}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{british}{loadhyph-en-gb.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{UKenglish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{UKenglish}{loadhyph-en-gb.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/usenglishmax.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "usenglishmax loadhyph-en-us.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{usenglishmax}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{usenglishmax}{loadhyph-en-us.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-english
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ukenglish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=british.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=UKenglish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ukenglish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{british}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{UKenglish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/usenglishmax.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{usenglishmax}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

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
tar -xf %{SOURCE123} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE124} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE125} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE126} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE127} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE128} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE129} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE130} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE131} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE132} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE133} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE134} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE135} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE136} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE137} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE138} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE139} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE140} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE141} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE142} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-amiweb2c-guide
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amiweb2c-guide/

%files -n texlive-amscls-doc
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amscls-doc/

%files -n texlive-amslatex-primer
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amslatex-primer/

%files -n texlive-around-the-bend
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/generic/around-the-bend/

%files -n texlive-ascii-chart
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/support/ascii-chart/

%files -n texlive-asy-overview
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/asy-overview/

%files -n texlive-biblatex-cheatsheet
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/biblatex-cheatsheet/

%files -n texlive-components
%license gpl2.txt
%doc %{_texmf_main}/doc/generic/components/

%files -n texlive-comprehensive
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/comprehensive/

%files -n texlive-dickimaw
%license fdl.txt
%doc %{_texmf_main}/doc/latex/dickimaw/

%files -n texlive-docsurvey
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/docsurvey/

%files -n texlive-dtxtut
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/dtxtut/

%files -n texlive-first-latex-doc
%license pd.txt
%doc %{_texmf_main}/doc/latex/first-latex-doc/

%files -n texlive-fontinstallationguide
%license fdl.txt
%doc %{_texmf_main}/doc/fonts/fontinstallationguide/

%files -n texlive-forest-quickstart
%license fdl.txt
%doc %{_texmf_main}/doc/latex/forest-quickstart/

%files -n texlive-guide-to-latex
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/guide-to-latex/

%files -n texlive-happy4th
%license pd.txt
%doc %{_texmf_main}/doc/plain/happy4th/

%files -n texlive-hyphen-english
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-impatient
%license fdl.txt
%doc %{_texmf_main}/doc/plain/impatient/

%files -n texlive-intro-scientific
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/intro-scientific/

%files -n texlive-knuth-errata
%license knuth.txt
%doc %{_texmf_main}/doc/generic/knuth-errata/

%files -n texlive-knuth-hint
%license pd.txt
%doc %{_texmf_main}/doc/generic/knuth-hint/

%files -n texlive-knuth-pdf
%license pd.txt
%doc %{_texmf_main}/doc/generic/knuth-pdf/

%files -n texlive-l2tabu-english
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/l2tabu-english/

%files -n texlive-latex-brochure
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-brochure/

%files -n texlive-latex-course
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/latex-course/

%files -n texlive-latex-doc-ptr
%license pd.txt
%doc %{_texmf_main}/doc/latex/latex-doc-ptr/

%files -n texlive-latex-for-undergraduates
%license pd.txt
%doc %{_texmf_main}/doc/latex/latex-for-undergraduates/

%files -n texlive-latex-graphics-companion
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-graphics-companion/

%files -n texlive-latex-refsheet
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-refsheet/

%files -n texlive-latex-veryshortguide
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-veryshortguide/

%files -n texlive-latex-web-companion
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-web-companion/

%files -n texlive-latex2e-help-texinfo
%license other-free.txt
%doc %{_texmf_main}/doc/info/
%doc %{_texmf_main}/doc/latex/latex2e-help-texinfo/

%files -n texlive-latex4wp
%license fdl.txt
%doc %{_texmf_main}/doc/latex/latex4wp/

%files -n texlive-latexcheat
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latexcheat/

%files -n texlive-latexcourse-rug
%doc %{_texmf_main}/doc/latex/latexcourse-rug/

%files -n texlive-latexfileinfo-pkgs
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latexfileinfo-pkgs/
%doc %{_texmf_main}/doc/latex/latexfileinfo-pkgs/

%files -n texlive-lshort-english
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-english/

%files -n texlive-macros2e
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/macros2e/
%doc %{_texmf_main}/doc/latex/macros2e/

%files -n texlive-math-into-latex-4
%license pd.txt
%doc %{_texmf_main}/doc/latex/math-into-latex-4/

%files -n texlive-maths-symbols
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/maths-symbols/

%files -n texlive-memdesign
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/fonts/memdesign/

%files -n texlive-memoirchapterstyles
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/memoirchapterstyles/

%files -n texlive-metafont-beginners
%license pd.txt
%doc %{_texmf_main}/doc/fonts/metafont-beginners/

%files -n texlive-metapost-examples
%license gpl.txt
%doc %{_texmf_main}/doc/metapost/metapost-examples/

%files -n texlive-patgen2-tutorial
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/support/patgen2-tutorial/

%files -n texlive-pictexsum
%license bsd2.txt
%doc %{_texmf_main}/doc/latex/pictexsum/

%files -n texlive-plain-doc
%license pd.txt
%doc %{_texmf_main}/doc/plain/plain-doc/

%files -n texlive-quran-en
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/quran-en/
%doc %{_texmf_main}/doc/xelatex/quran-en/

%files -n texlive-short-math-guide
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/short-math-guide/

%files -n texlive-simplified-latex
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/simplified-latex/

%files -n texlive-svg-inkscape
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/svg-inkscape/

%files -n texlive-tamethebeast
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/bibtex/tamethebeast/

%files -n texlive-tds
%license other-free.txt
%doc %{_texmf_main}/doc/generic/tds/
%doc %{_texmf_main}/doc/info/

%files -n texlive-tex-font-errors-cheatsheet
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/tex-font-errors-cheatsheet/

%files -n texlive-tex-nutshell
%license pd.txt
%doc %{_texmf_main}/doc/plain/tex-nutshell/

%files -n texlive-tex-overview
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/tex-overview/

%files -n texlive-tex-vpat
%license cc-by-3.txt
%doc %{_texmf_main}/doc/latex/tex-vpat/

%files -n texlive-texbytopic
%license fdl.txt
%doc %{_texmf_main}/doc/plain/texbytopic/

%files -n texlive-texonly
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/plain/texonly/

%files -n texlive-titlepages
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/titlepages/

%files -n texlive-tlc2
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/tlc2/

%files -n texlive-tlc3-examples
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/tlc3-examples/

%files -n texlive-tlmgrbasics
%license gpl2.txt
%doc %{_texmf_main}/doc/support/tlmgrbasics/

%files -n texlive-typstfun
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/typstfun/

%files -n texlive-undergradmath
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/undergradmath/

%files -n texlive-visualfaq
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/visualfaq/

%files -n texlive-webguide
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/webguide/

%files -n texlive-wrapstuff-doc-en
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/wrapstuff-doc-en/

%files -n texlive-xetexref
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/xetex/xetexref/

%files -n texlive-yet-another-guide-latex2e
%license fdl.txt
%doc %{_texmf_main}/doc/latex/yet-another-guide-latex2e/

%changelog
* Tue Jan 20 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn74022-3
- drop drawing-with-metapost (license "OpenPublication" is non-free)
- fix summaries
- fix license tags

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74022-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74022-1
- Update to TeX Live 2025
