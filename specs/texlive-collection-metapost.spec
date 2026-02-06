%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-metapost
Epoch:          12
Version:        svn73627
Release:        3%{?dist}
Summary:        MetaPost and Metafont packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-metapost.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/automata.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/automata.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbcard.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bbcard.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blockdraw_mp.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/blockdraw_mp.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bpolynomial.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bpolynomial.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmarrows.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cmarrows.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drv.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/drv.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviincl.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviincl.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emp.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/emp.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsincl.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsincl.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expressg.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expressg.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exteps.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exteps.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/featpost.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/featpost.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmf.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmf.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmp-auto.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/feynmp-auto.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fiziko.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fiziko.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garrigues.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garrigues.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmp.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gmp.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hatching.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hatching.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hershey-mp.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hershey-mp.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huffman.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huffman.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexmp.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexmp.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mcf2graph.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mcf2graph.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metago.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metago.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaobj.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaobj.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaplot.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metaplot.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost-colorbrewer.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost-colorbrewer.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metauml.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metauml.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic4ode.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfpic4ode.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-hatching.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/minim-hatching.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-geom2d.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-geom2d.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-neuralnetwork.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp-neuralnetwork.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp3d.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mp3d.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mparrows.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mparrows.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpattern.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpattern.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpchess.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpchess.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpcolornames.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpcolornames.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpgraphics.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpgraphics.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpkiviat.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mpkiviat.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mptrees.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mptrees.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piechartmp.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/piechartmp.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/repere.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/repere.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roex.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roundrect.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/roundrect.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shapes.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/shapes.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/slideshow.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/slideshow.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splines.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splines.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textpath.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/textpath.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/threeddice.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/threeddice.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-automata
Requires:       texlive-bbcard
Requires:       texlive-blockdraw_mp
Requires:       texlive-bpolynomial
Requires:       texlive-cmarrows
Requires:       texlive-collection-basic
Requires:       texlive-drv
Requires:       texlive-dviincl
Requires:       texlive-emp
Requires:       texlive-epsincl
Requires:       texlive-expressg
Requires:       texlive-exteps
Requires:       texlive-featpost
Requires:       texlive-feynmf
Requires:       texlive-feynmp-auto
Requires:       texlive-fiziko
Requires:       texlive-garrigues
Requires:       texlive-gmp
Requires:       texlive-hatching
Requires:       texlive-hershey-mp
Requires:       texlive-huffman
Requires:       texlive-latexmp
Requires:       texlive-mcf2graph
Requires:       texlive-metago
Requires:       texlive-metaobj
Requires:       texlive-metaplot
Requires:       texlive-metapost
Requires:       texlive-metapost-colorbrewer
Requires:       texlive-metauml
Requires:       texlive-mfpic
Requires:       texlive-mfpic4ode
Requires:       texlive-minim-hatching
Requires:       texlive-mp-geom2d
Requires:       texlive-mp-neuralnetwork
Requires:       texlive-mp3d
Requires:       texlive-mparrows
Requires:       texlive-mpattern
Requires:       texlive-mpchess
Requires:       texlive-mpcolornames
Requires:       texlive-mpgraphics
Requires:       texlive-mpkiviat
Requires:       texlive-mptrees
Requires:       texlive-piechartmp
Requires:       texlive-repere
Requires:       texlive-roex
Requires:       texlive-roundrect
Requires:       texlive-shapes
Requires:       texlive-slideshow
Requires:       texlive-splines
Requires:       texlive-suanpan
Requires:       texlive-textpath
Requires:       texlive-threeddice

%description
MetaPost and Metafont packages


%package -n texlive-automata
Summary:        Finite state machines, graphs and trees in MetaPost
Version:        svn19717
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-automata
The package offers a collection of macros for MetaPost to make easier to draw
finite-state machines, automata, labelled graphs, etc. The user defines nodes,
which may be isolated or arranged into matrices or trees; edges connect pairs
of nodes through arbitrary paths. Parameters, that specify the shapes of nodes
and the styles of edges, may be adjusted.

%package -n texlive-bbcard
Summary:        BS bingo, calendar and baseball-score cards
Version:        svn19440
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bbcard
Three jiffy packages for creating cards of various sorts with MetaPost.

%package -n texlive-blockdraw_mp
Summary:        Block diagrams and bond graphs, with MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-blockdraw_mp
A set of simple MetaPost macros for the task. While the task is not itself
difficult to program, it is felt that many users will be happy to have a
library for the job..

%package -n texlive-bpolynomial
Summary:        Drawing polynomial functions of up to order 3
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bpolynomial
This MetaPost package helps plotting polynomial and root functions up to order
three. The package provides macros to calculate Bezier curves exactly matching
a given constant, linear, quadratic or cubic polynomial, or square or cubic
root function. In addition, tangents on all functions and derivatives of
polynomials can be calculated.

%package -n texlive-cmarrows
Summary:        MetaPost arrows and braces in the Computer Modern style
Version:        svn24378
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cmarrows
This MetaPost package contains macros to draw arrows and braces in the Computer
Modern style.

%package -n texlive-drv
Summary:        Derivation trees with MetaPost
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-drv
A set of MetaPost macros for typesetting derivation trees (such as used in
sequent calculus, type inference, programming language semantics...). No
MetaPost knowledge is needed to use these macros.

%package -n texlive-dviincl
Summary:        Include a DVI page into MetaPost output
Version:        svn29349
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dviincl
DVItoMP is one of the auxiliary programs available to any MetaPost package; it
converts a DVI file into a MetaPost file. Using it, one can envisage including
a DVI page into an EPS files generated by MetaPost. Such files allow pages to
include other pages.

%package -n texlive-emp
Summary:        "Encapsulate" MetaPost figures in a document
Version:        svn23483
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(emp.sty) = %{tl_version}

%description -n texlive-emp
Emp is a package for encapsulating MetaPost figures in LaTeX: the package
provides environments where you can place MetaPost commands, and means of using
that code as fragments for building up figures to include in your document. So,
with emp, the procedure is to run your document with LaTeX, run MetaPost, and
then complete running your document in the normal way. Emp is therefore useful
for keeping illustrations in synchrony with the text. It also frees you from
inventing descriptive names for PostScript files that fit into the confines of
file system conventions.

%package -n texlive-epsincl
Summary:        Include EPS in MetaPost figures
Version:        svn29349
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-epsincl
The package facilitates including EPS files in MetaPost figures; it makes use
of (G)AWK.

%package -n texlive-expressg
Summary:        Diagrams consisting of boxes, lines, and annotations
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-expressg
A MetaPost package providing facilities to assist in drawing diagrams that
consist of boxes, lines, and annotations. Particular support is provided for
creating EXPRESS-G diagrams, for example IDEF1X, OMT, Shlaer-Mellor, and NIAM
diagrams. The package may also be used to create UML and most other
Box-Line-Annotation charts, but not Gantt charts directly.

%package -n texlive-exteps
Summary:        Include EPS figures in MetaPost
Version:        svn19859
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-exteps
Exteps is a module for including external EPS figures into MetaPost figures. It
is written entirely in MetaPost, and does not therefore require any post
processing of the MetaPost output.

%package -n texlive-featpost
Summary:        MetaPost macros for 3D
Version:        svn35346
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-featpost
These macros allow the production of three-dimensional schemes containing:
angles, circles, cylinders, cones and spheres, among other things.

%package -n texlive-feynmf
Summary:        Macros and fonts for creating Feynman (and other) diagrams
Version:        svn17259
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(feynmf.sty) = %{tl_version}
Provides:       tex(feynmp.sty) = %{tl_version}

%description -n texlive-feynmf
The feynmf package provides an interface to Metafont (inspired by the
facilities of mfpic) to use simple structure specifications to produce
relatively complex diagrams. (The feynmp package, also part of this bundle,
uses MetaPost in the same way.) While the package was designed for Feynman
diagrams, it could in principle be used for diagrams in graph and similar
theories, where the structure is semi-algorithmically determined.

%package -n texlive-feynmp-auto
Summary:        Automatic processing of feynmp graphics
Version:        svn30223
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(feynmp.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(feynmp-auto.sty) = %{tl_version}

%description -n texlive-feynmp-auto
The package takes care of running Metapost on the output files produced by the
feynmp package, so that the compiled pictures will be available in the next run
of LaTeX. The package honours options that apply to feynmp.

%package -n texlive-fiziko
Summary:        A MetaPost library for physics textbook illustrations
Version:        svn61944
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fiziko
This MetaPost library was initially written to automate some elements of black
and white illustrations for a physics textbook. It provides functions to draw
things like lines of variable width, shaded spheres, and tubes of different
kinds, which can be used to produce images of a variety of objects. The library
also contains functions to draw some objects constructed from these primitives.

%package -n texlive-garrigues
Summary:        MetaPost macros for the reproduction of Garrigues' Easter nomogram
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-garrigues
MetaPost macros for the reproduction of Garrigues' Easter nomogram. These
macros are described in Denis Roegel: An introduction to nomography: Garrigues'
nomogram for the computation of Easter, TUGboat (volume 30, number 1, 2009,
pages 88-104)

%package -n texlive-gmp
Summary:        Enable integration between MetaPost pictures and LaTeX
Version:        svn21691
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(gmp.sty) = %{tl_version}

%description -n texlive-gmp
The package allows integration between MetaPost pictures and LaTeX. The main
feature is that passing parameters to the MetaPost pictures is possible and the
picture code can be put inside arguments to commands, including \newcommand.

%package -n texlive-hatching
Summary:        MetaPost macros for hatching interior of closed paths
Version:        svn23818
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hatching
The file hatching.mp contains a set of MetaPost macros for hatching interior of
closed paths. Examples of usage are included.

%package -n texlive-hershey-mp
Summary:        MetaPost support for the Hershey font file format
Version:        svn70885
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hershey-mp
This package provides MetaPost support for reading jhf vector font files, used
by (mostly? only?) the so-called Hershey Fonts of the late 1960s. The package
does not include the actual font files, which you can probably find in the
software repository of your operating system.

%package -n texlive-huffman
Summary:        Drawing binary Huffman trees with MetaPost and METAOBJ
Version:        svn67071
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-huffman
This MetaPost package allows to draw binary Huffman trees from two arrays : an
array of strings, and an array of weights (numeric). It is based on the METAOBJ
package which provides many tools for building trees in general.

%package -n texlive-latexmp
Summary:        Interface for LaTeX-based typesetting in MetaPost
Version:        svn55643
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-latexmp
The MetaPost package latexMP implements a user-friendly interface to access
LaTeX-based typesetting capabilities in MetaPost. The text to be typeset is
given as string. This allows even dynamic text elements, for example counters,
to be used in labels. Compared to other implementations it is much more
flexible, since it can be used as direct replacement for btex.etex, and much
faster, compared for example to the solution provided by tex.mp.

%package -n texlive-mcf2graph
Summary:        Draw chemical structure diagrams with MetaPost
Version:        svn76506
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mcf2graph
The Molecular Coding Format (MCF) is a linear notation for describing chemical
structure diagrams. This package converts MCF to graphic files using MetaPost.

%package -n texlive-metago
Summary:        MetaPost output of Go positions
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metago
The package allows you to draw Go game positions with MetaPost. Two methods of
usage are provided, either using the package programmatically, or using the
package via a script (which may produce several images).

%package -n texlive-metaobj
Summary:        MetaPost package providing high-level objects
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metaobj
METAOBJ is a large MetaPost package providing high-level objects. It implements
many of PSTricks' features for node connections, but also trees, matrices, and
many other things. It more or less contains boxes.mp and rboxes.mp. There is a
large (albeit not complete) documentation distributed with the package. It is
easily extensible with new objects.

%package -n texlive-metaplot
Summary:        Plot-manipulation macros for use in MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metaplot
MetaPlot is a set of MetaPost macros for manipulating pre-generated plots (and
similar objects), and formatting them for inclusion in a MetaPost figure. The
intent is that the plots can be generated by some outside program, in an
abstract manner that does not require making decisions about on-page sizing and
layout, and then they can be imported into MetaPlot and arranged using the full
capabilities of MetaPost. Metaplot also includes a very flexible set of macros
for generating plot axes, which may be useful in other contexts as well.
Presently, MetaPlot is in something of a pre-release beta state; it is quite
functional, but the syntax of the commands is still potentially in flux.

%package -n texlive-metapost-colorbrewer
Summary:        An implementation of the colorbrewer2.org colours for MetaPost
Version:        svn48753
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metapost-colorbrewer
This package provides two MetaPost include files that define all the
colorbrewer2.org colours: colorbrewer-cmyk.mp colorbrewer-rgb.mp The first
defines all the colours as CMYK, the second as RGB. Use whichever one you
prefer. For an example of what you can do, and a list of all the names, have a
look at colorbrewer-sampler.mp. You can also see the names on
http://colorbrewer2.org. The package also includes the Python script used to
generate the MP source from the colorbrewer project.

%package -n texlive-metauml
Summary:        MetaPost library for typesetting UML diagrams
Version:        svn49923
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-metauml
MetaUML is a MetaPost library for typesetting UML diagrams, which provides a
usable, human-friendly textual notation for UML, offering now support for
class, package, activity, state, and use case diagrams.

%package -n texlive-mfpic
Summary:        Draw Metafont/post pictures from (La)TeX commands
Version:        svn28444
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(mfpic.sty) = %{tl_version}
Provides:       tex(mfpic.tex) = %{tl_version}
Provides:       tex(mfpicdef.tex) = %{tl_version}

%description -n texlive-mfpic
Mfpic is a scheme for producing pictures from (La)TeX commands. Commands \mfpic
and \endmfpic (in LaTeX, the mfpic environment) enclose a group in which
drawing commands may be placed. The commands generate a Meta-language file,
which may be processed by MetaPost (or even Metafont). The resulting image file
will be read back in to the document to place the picture at the point where
the original (La)TeX commands appeared. Note that the ability to use MetaPost
here means that the package works equally well in LaTeX and pdfLaTeX.

%package -n texlive-mfpic4ode
Summary:        Macros to draw direction fields and solutions of ODEs
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mfpic4ode.sty) = %{tl_version}
Provides:       tex(mfpic4ode.tex) = %{tl_version}

%description -n texlive-mfpic4ode
The package is a small set of macros for drawing direction fields, phase
portraits and trajectories of differential equations and two dimensional
autonomous systems. The Euler, Runge-Kutta and 4th order Runge-Kutta algorithms
are available to solve the ODEs. The picture is translated into mfpic macros
and MetaPost is used to create the final drawing. The package is was designed
for use with LaTeX, but it can be used in plain TeX as well.

%package -n texlive-minim-hatching
Summary:        Create tiling patterns with the minim-mp MetaPost processor
Version:        svn70885
License:        EUPL-1.2
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-minim-hatching
This is a small proof-of-concept library of tiling patterns for use with the
minim-mp MetaPost processor.

%package -n texlive-mp-geom2d
Summary:        Flat geometry with MetaPost
Version:        svn77019
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mp-geom2d
This package was written with the aim of providing MetaPost macros for creating
a geometry figure that closely matches an imperative description: Let A be the
point with coordinates (2,3). Let B be the point with coordinates (4,5). Draw
the line (A, B). ...

%package -n texlive-mp-neuralnetwork
Summary:        Drawing artificial neural networks with MetaPost and METAOBJ
Version:        svn73627
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mp-neuralnetwork
This MetaPost package allows to draw artificial neural networks. It is based on
the METAOBJ package which provides many tools to draw and arrange nodes. This
package is in beta version -- do not hesitate to report bugs, as well as
requests for improvement.

%package -n texlive-mp3d
Summary:        3D animations
Version:        svn29349
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mp3d
Create animations of 3-dimensional objects (such as polyhedra) in MetaPost.

%package -n texlive-mparrows
Summary:        MetaPost module with different types of arrow heads
Version:        svn39729
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mparrows
A package to provide different types of arrow heads to be used with MetaPost
commands drawarrow and drawdblarrow commands.

%package -n texlive-mpattern
Summary:        Patterns in MetaPost
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpattern
A package for defining and using patterns in MetaPost, using the Pattern Color
Space available in PostScript Level 2.

%package -n texlive-mpchess
Summary:        Drawing chess boards and positions with MetaPost
Version:        svn73149
License:        LPPL-1.3c AND GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpchess
This package allows you to draw chess boards and positions. The appearance of
the drawings is modern and largely inspired by what is offered by the excellent
web site Lichess.org. Relying on MetaPost probably allows more graphic
flexibility than the excellent LaTeX packages. This package is in beta version,
do not hesitate to report bugs, as well as requests for improvement

%package -n texlive-mpcolornames
Summary:        Extend list of predefined colour names for MetaPost
Version:        svn23252
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpcolornames
The MetaPost format plain.mp provides only five built-in colour names
(variables), all of which are defined in the RGB model: red, green and blue for
the primary colours and black and white. The package makes more than 500 colour
names from different colour sets in different colour models available to
MetaPost. Colour sets include X11, SVG, DVIPS and xcolor specifications.

%package -n texlive-mpgraphics
Summary:        Process and display MetaPost figures inline
Version:        svn29776
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(iftex.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(mpgraphics.sty) = %{tl_version}

%description -n texlive-mpgraphics
The package allows LaTeX users to typeset MetaPost code inline and display
figures in their documents with only and only one run of LaTeX, pdfLaTeX or
XeLaTeX (no separate runs of mpost). Mpgraphics achieves this by using the
shell escape (\write 18) feature of current TeX distributions, so that the
whole process is automatic and the end user is saved the tiresome processing.

%package -n texlive-mpkiviat
Summary:        MetaPost package to draw Kiviat diagrams
Version:        svn75712
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mpkiviat
This MetaPost package allows to draw Kiviat diagrams (or radar chart, web
chart, spider chart, etc.).

%package -n texlive-mptrees
Summary:        Probability trees with MetaPost
Version:        svn70887
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-mptrees
This package provides MetaPost tools for drawing simple probability trees and
graphs (in discrete geometry).

%package -n texlive-piechartmp
Summary:        Draw pie-charts using MetaPost
Version:        svn19440
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-piechartmp
The piechartmp package is an easy way to draw pie-charts with MetaPost. The
package implements an interface that enables users with little MetaPost
experience to draw charts. A highlight of the package is the possibility of
suppressing some segments of the chart, thus creating the possibility of
several charts from the same data.

%package -n texlive-repere
Summary:        MetaPost macros for secondary school mathematics teachers
Version:        svn66998
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-repere
This package provides MetaPost macros for drawing secondary school mathematics
figures in a coordinate system: axis, grids points, vectors functions (curves,
tangents, integrals, sequences) statistic diagrams plane geometry (polygons,
circles) arrays and game boards

%package -n texlive-roex
Summary:        Metafont-PostScript conversions
Version:        svn45818
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-roex
A Metafont support package including: epstomf, a tiny AWK script for converting
EPS files into Metafont; mftoeps for generating (encapsulated) PostScript files
readable, e.g., by CorelDRAW, Adobe Illustrator and Fontographer; a collection
of routines (in folder progs) for converting Metafont-coded graphics into
encapsulated PostScript; and roex.mf, which provides Metafont macros for
removing overlaps and expanding strokes. In mftoeps, Metafont writes PostScript
code to a log-file, from which it may be extracted by either TeX or AWK.

%package -n texlive-roundrect
Summary:        MetaPost macros for highly configurable rounded rectangles (optionally with text)
Version:        svn39796
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-roundrect
The roundrect macros for MetaPost provide ways to produce rounded rectangles,
which may or may not contain a title bar or text (the title bar may itself
contain text). They are extremely configurable.

%package -n texlive-shapes
Summary:        Draw polygons, reentrant stars, and fractions in circles with MetaPost
Version:        svn42428
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-shapes
The shapes set of macros allows drawing regular polygons; their corresponding
reentrant stars in all their variations; and fractionally filled circles
(useful for visually demonstrating the nature of fractions) in MetaPost.

%package -n texlive-slideshow
Summary:        Generate slideshow with MetaPost
Version:        svn15878
License:        McPhee-slideshow
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-slideshow
The package provides a means of creating presentations in MetaPost, without
intervention from other utilities (except a distiller). Such an arrangement has
its advantages (though there are disadvantages too).

%package -n texlive-splines
Summary:        MetaPost macros for drawing cubic spline interpolants
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-splines
This is a small package of macros for creating cubic spline interpolants in
MetaPost or Metafont. Given a list of points the macros can produce a closed or
a relaxed spline joining them. Given a list of function values y_j at x_j, the
result would define the graph of a cubic spline interpolating function y=f(x),
which is either periodic or relaxed.

%package -n texlive-suanpan
Summary:        MetaPost macros for drawing Chinese and Japanese abaci
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-suanpan
These macros are described in Denis Roegel: MetaPost macros for drawing Chinese
and Japanese abaci, TUGboat (volume 30, number 1, 2009, pages 74-79)

%package -n texlive-textpath
Summary:        Setting text along a path with MetaPost
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(soul.sty)
Provides:       tex(textpathmp.sty) = %{tl_version}

%description -n texlive-textpath
This MetaPost package provides macros to typeset text along a free path with
the help of LaTeX, thereby preserving kerning and allowing for 8-bit input
(accented characters).

%package -n texlive-threeddice
Summary:        Create images of dice with one, two, or three faces showing, using MetaPost
Version:        svn20675
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-threeddice
The package provides MetaPost code to create all possible symmetrical views (up
to rotation) of a right-handed die. Configuration is possible by editing the
source code, following the guidance in the documentation.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-automata
%license lppl1.3c.txt
%{_texmf_main}/metapost/automata/
%doc %{_texmf_main}/doc/metapost/automata/

%files -n texlive-bbcard
%license pd.txt
%{_texmf_main}/metapost/bbcard/
%doc %{_texmf_main}/doc/metapost/bbcard/

%files -n texlive-blockdraw_mp
%license lppl1.3c.txt
%{_texmf_main}/metapost/blockdraw_mp/
%doc %{_texmf_main}/doc/metapost/blockdraw_mp/

%files -n texlive-bpolynomial
%license lppl1.3c.txt
%{_texmf_main}/metapost/bpolynomial/
%doc %{_texmf_main}/doc/metapost/bpolynomial/

%files -n texlive-cmarrows
%license lppl1.3c.txt
%{_texmf_main}/metapost/cmarrows/
%doc %{_texmf_main}/doc/metapost/cmarrows/

%files -n texlive-drv
%license lppl1.3c.txt
%{_texmf_main}/metapost/drv/
%doc %{_texmf_main}/doc/metapost/drv/

%files -n texlive-dviincl
%license pd.txt
%{_texmf_main}/metapost/dviincl/
%doc %{_texmf_main}/doc/metapost/dviincl/

%files -n texlive-emp
%license gpl2.txt
%{_texmf_main}/tex/latex/emp/
%doc %{_texmf_main}/doc/latex/emp/

%files -n texlive-epsincl
%license pd.txt
%{_texmf_main}/metapost/epsincl/
%doc %{_texmf_main}/doc/metapost/epsincl/

%files -n texlive-expressg
%license lppl1.3c.txt
%{_texmf_main}/metapost/expressg/
%doc %{_texmf_main}/doc/metapost/expressg/

%files -n texlive-exteps
%license gpl2.txt
%{_texmf_main}/metapost/exteps/
%doc %{_texmf_main}/doc/metapost/exteps/

%files -n texlive-featpost
%license gpl2.txt
%{_texmf_main}/metapost/featpost/
%doc %{_texmf_main}/doc/metapost/featpost/

%files -n texlive-feynmf
%license gpl2.txt
%{_texmf_main}/metafont/feynmf/
%{_texmf_main}/metapost/feynmf/
%{_texmf_main}/tex/latex/feynmf/
%doc %{_texmf_main}/doc/latex/feynmf/

%files -n texlive-feynmp-auto
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/feynmp-auto/
%doc %{_texmf_main}/doc/latex/feynmp-auto/

%files -n texlive-fiziko
%license gpl3.txt
%license cc-by-sa-4.txt
%{_texmf_main}/metapost/fiziko/
%doc %{_texmf_main}/doc/metapost/fiziko/

%files -n texlive-garrigues
%license lppl1.3c.txt
%{_texmf_main}/metapost/garrigues/
%doc %{_texmf_main}/doc/metapost/garrigues/

%files -n texlive-gmp
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/gmp/
%doc %{_texmf_main}/doc/latex/gmp/

%files -n texlive-hatching
%license pd.txt
%{_texmf_main}/metapost/hatching/
%doc %{_texmf_main}/doc/metapost/hatching/

%files -n texlive-hershey-mp
%license other-free.txt
%{_texmf_main}/metapost/hershey-mp/
%doc %{_texmf_main}/doc/metapost/hershey-mp/

%files -n texlive-huffman
%license lppl1.3c.txt
%{_texmf_main}/metapost/huffman/
%doc %{_texmf_main}/doc/metapost/huffman/

%files -n texlive-latexmp
%license pd.txt
%{_texmf_main}/metapost/latexmp/
%doc %{_texmf_main}/doc/metapost/latexmp/

%files -n texlive-mcf2graph
%license mit.txt
%{_texmf_main}/metapost/mcf2graph/
%doc %{_texmf_main}/doc/metapost/mcf2graph/

%files -n texlive-metago
%license lppl1.3c.txt
%{_texmf_main}/metapost/metago/
%doc %{_texmf_main}/doc/metapost/metago/

%files -n texlive-metaobj
%license lppl1.3c.txt
%{_texmf_main}/metapost/metaobj/
%doc %{_texmf_main}/doc/metapost/metaobj/

%files -n texlive-metaplot
%license lppl1.3c.txt
%{_texmf_main}/metapost/metaplot/
%doc %{_texmf_main}/doc/latex/metaplot/

%files -n texlive-metapost-colorbrewer
%license gpl3.txt
%{_texmf_main}/metapost/metapost-colorbrewer/
%doc %{_texmf_main}/doc/metapost/metapost-colorbrewer/

%files -n texlive-metauml
%license gpl2.txt
%{_texmf_main}/metapost/metauml/
%doc %{_texmf_main}/doc/metapost/metauml/

%files -n texlive-mfpic
%license lppl1.3c.txt
%{_texmf_main}/metafont/mfpic/
%{_texmf_main}/metapost/mfpic/
%{_texmf_main}/tex/generic/mfpic/
%doc %{_texmf_main}/doc/generic/mfpic/

%files -n texlive-mfpic4ode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mfpic4ode/
%doc %{_texmf_main}/doc/latex/mfpic4ode/

%files -n texlive-minim-hatching
%license other-free.txt
%{_texmf_main}/metapost/minim-hatching/
%doc %{_texmf_main}/doc/latex/minim-hatching/

%files -n texlive-mp-geom2d
%license lppl1.3c.txt
%{_texmf_main}/metapost/mp-geom2d/
%doc %{_texmf_main}/doc/metapost/mp-geom2d/

%files -n texlive-mp-neuralnetwork
%license lppl1.3c.txt
%{_texmf_main}/metapost/mp-neuralnetwork/
%doc %{_texmf_main}/doc/metapost/mp-neuralnetwork/

%files -n texlive-mp3d
%license lppl1.3c.txt
%{_texmf_main}/metapost/mp3d/
%doc %{_texmf_main}/doc/metapost/mp3d/

%files -n texlive-mparrows
%license pd.txt
%{_texmf_main}/metapost/mparrows/
%doc %{_texmf_main}/doc/metapost/mparrows/

%files -n texlive-mpattern
%license pd.txt
%{_texmf_main}/metapost/mpattern/
%doc %{_texmf_main}/doc/metapost/mpattern/

%files -n texlive-mpchess
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/fonts/truetype/public/mpchess/
%{_texmf_main}/metapost/mpchess/
%doc %{_texmf_main}/doc/metapost/mpchess/

%files -n texlive-mpcolornames
%license lppl1.3c.txt
%{_texmf_main}/metapost/mpcolornames/
%doc %{_texmf_main}/doc/metapost/mpcolornames/

%files -n texlive-mpgraphics
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/mpgraphics/
%doc %{_texmf_main}/doc/latex/mpgraphics/

%files -n texlive-mpkiviat
%license lppl1.3c.txt
%{_texmf_main}/metapost/mpkiviat/
%doc %{_texmf_main}/doc/metapost/mpkiviat/

%files -n texlive-mptrees
%license lppl1.3c.txt
%{_texmf_main}/metapost/mptrees/
%doc %{_texmf_main}/doc/metapost/mptrees/

%files -n texlive-piechartmp
%license lppl1.3c.txt
%{_texmf_main}/metapost/piechartmp/
%doc %{_texmf_main}/doc/metapost/piechartmp/

%files -n texlive-repere
%license lppl1.3c.txt
%{_texmf_main}/metapost/repere/
%doc %{_texmf_main}/doc/metapost/repere/

%files -n texlive-roex
%license pd.txt
%{_texmf_main}/metafont/roex/

%files -n texlive-roundrect
%license lppl1.3c.txt
%{_texmf_main}/metapost/roundrect/
%doc %{_texmf_main}/doc/metapost/roundrect/

%files -n texlive-shapes
%license lppl1.3c.txt
%{_texmf_main}/metapost/shapes/
%doc %{_texmf_main}/doc/metapost/shapes/

%files -n texlive-slideshow
%license other-free.txt
%{_texmf_main}/metapost/slideshow/
%doc %{_texmf_main}/doc/metapost/slideshow/

%files -n texlive-splines
%license lppl1.3c.txt
%{_texmf_main}/metapost/splines/
%doc %{_texmf_main}/doc/metapost/splines/

%files -n texlive-suanpan
%license lppl1.3c.txt
%{_texmf_main}/metapost/suanpan/
%doc %{_texmf_main}/doc/metapost/suanpan/

%files -n texlive-textpath
%license lppl1.3c.txt
%{_texmf_main}/metapost/textpath/
%{_texmf_main}/tex/latex/textpath/
%doc %{_texmf_main}/doc/metapost/textpath/

%files -n texlive-threeddice
%license lppl1.3c.txt
%{_texmf_main}/metapost/threeddice/
%doc %{_texmf_main}/doc/metapost/threeddice/

%changelog
* Sat Jan 31 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn73627-3
- fix licensing, descriptions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73627-2
- regen, no deps from docs

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73627-1
- Update to TeX Live 2025
