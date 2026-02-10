%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-basic
Epoch:          12
Version:        svn72890
Release:        8%{?dist}
Summary:        Essential programs and files

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-basic.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsfonts.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsfonts.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cm.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colorprofiles.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/colorprofiles.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ec.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ec.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/enctex.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/enctex.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etex.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etex.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etex-pkg.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/etex-pkg.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-def.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/graphics-def.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyph-utf8.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyph-utf8.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-base.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphenex.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifplatform.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ifplatform.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iftex.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/iftex.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-lib.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/knuth-local.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-alt-getopt.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-alt-getopt.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflogo.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflogo.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modes.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/modes.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/plain.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-ini-files.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-ini-files.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-common.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-common.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-msg-translations.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-data.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-data.doc.tar.xz

# Patches
Patch0:         etex-addlanguage-fix-bz1215257.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-amsfonts
Requires:       texlive-bibtex
Requires:       texlive-cm
Requires:       texlive-colorprofiles
Requires:       texlive-dvipdfmx
Requires:       texlive-dvips
Requires:       texlive-ec
Requires:       texlive-enctex
Requires:       texlive-etex
Requires:       texlive-etex-pkg
Requires:       texlive-extractbb
Requires:       texlive-glyphlist
Requires:       texlive-graphics-def
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Requires:       texlive-hyphenex
Requires:       texlive-ifplatform
Requires:       texlive-iftex
Requires:       texlive-knuth-lib
Requires:       texlive-knuth-local
Requires:       texlive-kpathsea
Requires:       texlive-lua-alt-getopt
Requires:       texlive-luahbtex
Requires:       texlive-luatex
Requires:       texlive-makeindex
Requires:       texlive-metafont
Requires:       texlive-mflogo
Requires:       texlive-mfware
Requires:       texlive-modes
Requires:       texlive-pdftex
Requires:       texlive-plain
Requires:       texlive-tex
Requires:       texlive-tex-ini-files
Requires:       texlive-texlive-common
Requires:       texlive-texlive-en
Requires:       texlive-texlive-msg-translations
Requires:       texlive-texlive-scripts
Requires:       texlive-texlive.infra
Requires:       texlive-unicode-data
Requires:       texlive-xdvi
Provides:       tex(tex) = %{tl_version}
Provides:       tex = %{tl_version}

%description
These files are regarded as basic for any TeX system, covering plain TeX
macros, Computer Modern fonts, and configuration for common drivers; no LaTeX.


%package -n texlive-amsfonts
Summary:        TeX fonts from the American Mathematical Society
Version:        svn61937
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(amsfonts.sty) = %{tl_version}
Provides:       tex(amssym.def) = %{tl_version}
Provides:       tex(amssym.tex) = %{tl_version}
Provides:       tex(amssymb.sty) = %{tl_version}
Provides:       tex(cmmib57.sty) = %{tl_version}
Provides:       tex(cyracc.def) = %{tl_version}
Provides:       tex(eucal.sty) = %{tl_version}
Provides:       tex(eufrak.sty) = %{tl_version}
Provides:       tex(euscript.sty) = %{tl_version}

%description -n texlive-amsfonts
An extended set of fonts for use in mathematics, including: extra mathematical
symbols; blackboard bold letters (uppercase only); fraktur letters; subscript
sizes of bold math italic and bold Greek letters; subscript sizes of large
symbols such as sum and product; added sizes of the Computer Modern small caps
font; cyrillic fonts (from the University of Washington); Euler mathematical
fonts. All fonts are provided as Adobe Type 1 files, and all except the Euler
fonts are provided as Metafont source. The distribution also includes the
canonical Type 1 versions of the Computer Modern family of fonts. Basic LaTeX
support for the symbol fonts is provided by amsfonts.sty, with names of
individual symbols defined in amssymb.sty. The Euler fonts are supported by
separate packages; details can be found in the documentation.

%package -n texlive-cm
Summary:        Computer Modern fonts
Version:        svn57963
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cm
Knuth's final iteration of his re-interpretation of a c.19 Modern-style font
from Monotype. The family is comprehensive, offering both sans and roman
styles, and a monospaced font, together with mathematics fonts closely
integrated with the mathematical facilities of TeX itself. The base fonts are
distributed as Metafont source, but autotraced PostScript Type 1 versions are
available (one version in the AMS fonts distribution, and also the BaKoMa
distribution). The Computer Modern fonts have inspired many later families,
notably the European Computer Modern and the Latin Modern families.

%package -n texlive-colorprofiles
Summary:        Collection of free ICC profiles
Version:        svn49086
License:        LPPL-1.3c AND MIT AND LicenseRef-Fedora-Public-Domain AND Zlib
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(colorprofiles.sty) = %{tl_version}
Provides:       tex(colorprofiles.tex) = %{tl_version}

%description -n texlive-colorprofiles
This package collects free ICC profiles that can be used by color profile aware
applications/tools like the pdfx package, as well as TeX and LaTeX packages to
access them.

%package -n texlive-ec
Summary:        Computer modern fonts in T1 and TS1 encodings
Version:        svn25033
License:        LicenseRef-ec
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ec
The EC fonts are European Computer Modern Fonts, supporting the complete LaTeX
T1 encoding defined at the 1990 TUG conference hold at Cork/Ireland. These
fonts are intended to be stable with no changes being made to the tfm files.
The set also contains a Text Companion Symbol font, called tc, featuring many
useful characters needed in text typesetting, for example oldstyle digits,
currency symbols (including the newly created Euro symbol), the permille sign,
copyright, trade mark and servicemark as well as a copyleft sign, and many
others. Recent releases of LaTeX2e support the EC fonts. The EC fonts supersede
the preliminary version released as the DC fonts. The fonts are available in
(traced) Adobe Type 1 format, as part of the cm-super bundle. The other
Computer Modern-style T1-encoded Type 1 set, Latin Modern, is not actually a
direct development of the EC set, and differs from the EC in a number of
particulars.

%package -n texlive-enctex
Summary:        A TeX extension that translates input on its way into TeX
Version:        svn34957
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(1250-csf.tex) = %{tl_version}
Provides:       tex(1250-il2.tex) = %{tl_version}
Provides:       tex(1250-latex.tex) = %{tl_version}
Provides:       tex(1250-t1.tex) = %{tl_version}
Provides:       tex(852-csf.tex) = %{tl_version}
Provides:       tex(852-il2.tex) = %{tl_version}
Provides:       tex(852-latex.tex) = %{tl_version}
Provides:       tex(852-t1.tex) = %{tl_version}
Provides:       tex(csfmacro.tex) = %{tl_version}
Provides:       tex(enc-u.tex) = %{tl_version}
Provides:       tex(encmacro.tex) = %{tl_version}
Provides:       tex(il2-1250.tex) = %{tl_version}
Provides:       tex(il2-852.tex) = %{tl_version}
Provides:       tex(il2-csf.tex) = %{tl_version}
Provides:       tex(il2-kam.tex) = %{tl_version}
Provides:       tex(il2-t1.tex) = %{tl_version}
Provides:       tex(kam-csf.tex) = %{tl_version}
Provides:       tex(kam-il2.tex) = %{tl_version}
Provides:       tex(kam-latex.tex) = %{tl_version}
Provides:       tex(kam-t1.tex) = %{tl_version}
Provides:       tex(mixcodes.tex) = %{tl_version}
Provides:       tex(noprefnt.tex) = %{tl_version}
Provides:       tex(plain-1250-cs.tex) = %{tl_version}
Provides:       tex(plain-852-cs.tex) = %{tl_version}
Provides:       tex(plain-il2-cs.tex) = %{tl_version}
Provides:       tex(plain-kam-cs.tex) = %{tl_version}
Provides:       tex(plain-utf8-cs.tex) = %{tl_version}
Provides:       tex(plain-utf8-ec.tex) = %{tl_version}
Provides:       tex(polyset.tex) = %{tl_version}
Provides:       tex(t1macro.tex) = %{tl_version}
Provides:       tex(utf8-csf.tex) = %{tl_version}
Provides:       tex(utf8-t1.tex) = %{tl_version}
Provides:       tex(utf8cseq.tex) = %{tl_version}
Provides:       tex(utf8lat1.tex) = %{tl_version}
Provides:       tex(utf8lata.tex) = %{tl_version}
Provides:       tex(utf8math.tex) = %{tl_version}
Provides:       tex(utf8off.tex) = %{tl_version}
Provides:       tex(utf8raw.tex) = %{tl_version}
Provides:       tex(utf8unkn.tex) = %{tl_version}
Provides:       tex(utf8warn.tex) = %{tl_version}

%description -n texlive-enctex
EncTeX is (another) TeX extension, written at the change-file level. It
provides means of translating input on the way into TeX. It allows, for
example, translation of multibyte sequences, such as utf-8 encoding.

%package -n texlive-etex
Summary:        An extended version of TeX, from the NTS project
Version:        svn73850
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-etex
An extended version of TeX (capable of running as if it were unmodified TeX).
E-TeX has been specified by the LaTeX team as the base engine for LaTeX2e.
Thus, LaTeX programmers may assume e-TeX functionality, along with additional
extensions. The pdftex engine and others directly incorporate the e-TeX
extensions. The etex program in most distributions is an incarnation of pdftex
running in DVI mode. The development source for e-TeX is the TeX Live source
repository, although further extensions have taken place in the pdftex and
other engine sources, keeping e-TeX stable.

%package -n texlive-etex-pkg
Summary:        E-TeX support package
Version:        svn41784
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(etex.sty) = %{tl_version}

%description -n texlive-etex-pkg
The package provides support for LaTeX documents to use many of the extensions
offered by e-TeX; in particular, it modifies LaTeX's register allocation macros
to make use of the extended register range. The etextools package provides
macros that make more sophisticated use of e-TeX's facilities.

%package -n texlive-graphics-def
Summary:        Colour and graphics option files
Version:        svn76719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dvipdfmx.def) = %{tl_version}
Provides:       tex(dvips.def) = %{tl_version}
Provides:       tex(dvisvgm.def) = %{tl_version}
Provides:       tex(luatex.def) = %{tl_version}
Provides:       tex(pdftex.def) = %{tl_version}
Provides:       tex(xetex.def) = %{tl_version}

%description -n texlive-graphics-def
This bundle is a combined distribution consisting of dvips.def, pdftex.def,
luatex.def, xetex.def, dvipdfmx.def, and dvisvgm.def driver option files for
the LaTeX graphics and color packages. It is hoped that by combining their
source repositories at https://github.com/latex3/graphics-def it will be easier
to coordinate updates.

%package -n texlive-hyph-utf8
Summary:        Hyphenation patterns expressed in UTF-8
Version:        svn74823
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(conv-utf8-ec.tex) = %{tl_version}
Provides:       tex(conv-utf8-il2.tex) = %{tl_version}
Provides:       tex(conv-utf8-il3.tex) = %{tl_version}
Provides:       tex(conv-utf8-l7x.tex) = %{tl_version}
Provides:       tex(conv-utf8-lmc.tex) = %{tl_version}
Provides:       tex(conv-utf8-lth.tex) = %{tl_version}
Provides:       tex(conv-utf8-qx.tex) = %{tl_version}
Provides:       tex(conv-utf8-t2a.tex) = %{tl_version}
Provides:       tex(conv-utf8-t8m.tex) = %{tl_version}

%description -n texlive-hyph-utf8
Modern native UTF-8 engines such as XeTeX and LuaTeX need hyphenation patterns
in UTF-8 format, whereas older systems require hyphenation patterns in the
8-bit encoding of the font in use (such encodings are codified in the LaTeX
scheme with names like OT1, T2A, TS1, OML, LY1, etc). The present package
offers a collection of conversions of existing patterns to UTF-8 format,
together with converters for use with 8-bit fonts in older systems. Since
hyphenation patterns for Knuthian-style TeX systems are only read at iniTeX
time, it is hoped that the UTF-8 patterns, with their converters, will
completely supplant the older patterns.

%package -n texlive-hyphen-base
Summary:        Core hyphenation support files
Version:        svn74125
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(dumyhyph.tex) = %{tl_version}
Provides:       tex(hyphen.tex) = %{tl_version}
Provides:       tex(hypht1.tex) = %{tl_version}
Provides:       tex(language.def) = %{tl_version}
Provides:       tex(language.us.def) = %{tl_version}
Provides:       tex(zerohyph.tex) = %{tl_version}

%description -n texlive-hyphen-base
Includes Knuth's original hyphen.tex, zerohyph.tex to disable hyphenation,
language.us which starts the autogenerated files language.dat and language.def
(and default versions of those), etc.

%package -n texlive-hyphenex
Summary:        US English hyphenation exceptions file
Version:        svn57387
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ushyphex.tex) = %{tl_version}

%description -n texlive-hyphenex
Exceptions for American English hyphenation patterns are occasionally published
in the TeX User Group journal TUGboat. This bundle provides alternative Perl
and Bourne shell scripts to convert the source of such an article into an
exceptions file, together with a recent copy of the article and
machine-readable files.

%package -n texlive-ifplatform
Summary:        Conditionals to test which platform is being used
Version:        svn45533
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(catchfile.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(shellesc.sty)
Provides:       tex(ifplatform.sty) = %{tl_version}

%description -n texlive-ifplatform
This package uses the (La)TeX extension -shell-escape to establish whether the
document is being processed on a Windows or on a Unix-like system (Mac OS X,
Linux, etc.), or on Cygwin (Unix environment over a windows system). Booleans
provided are: \ifwindows, \iflinux, \ifmacosx and \ifcygwin. The package also
preserves the output of uname on a Unix-like system, which may be used to
distinguish between various classes of Unix systems.

%package -n texlive-iftex
Summary:        Am I running under pdfTeX, XeTeX or LuaTeX?
Version:        svn73115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ifetex.sty) = %{tl_version}
Provides:       tex(ifluatex.sty) = %{tl_version}
Provides:       tex(ifpdf.sty) = %{tl_version}
Provides:       tex(iftex.sty) = %{tl_version}
Provides:       tex(ifvtex.sty) = %{tl_version}
Provides:       tex(ifxetex.sty) = %{tl_version}

%description -n texlive-iftex
The package, which works both for Plain TeX and for LaTeX, defines the
\ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for testing which engine is
being used for typesetting. The package also provides the \RequirePDFTeX,
\RequireXeTeX, and \RequireLuaTeX commands which throw an error if pdfTeX,
XeTeX or LuaTeX (respectively) is not the engine in use.

%package -n texlive-knuth-lib
Summary:        Core TeX and Metafont sources from Knuth
Version:        svn57963
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(manmac.tex) = %{tl_version}
Provides:       tex(mftmac.tex) = %{tl_version}
Provides:       tex(null.tex) = %{tl_version}
Provides:       tex(story.tex) = %{tl_version}
Provides:       tex(testfont.tex) = %{tl_version}
Provides:       tex(webmac.tex) = %{tl_version}

%description -n texlive-knuth-lib
A collection of core TeX and Metafont macro files from DEK, apart from the
plain format and base. Includes the MF logo font(s), webmac.tex, etc.

%package -n texlive-knuth-local
Summary:        Knuth's local information
Version:        svn57963
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xepsf.tex) = %{tl_version}

%description -n texlive-knuth-local
A collection of experimental programs and developments based on, or
complementary to, the matter in his distribution directories.

%package -n texlive-lua-alt-getopt
Summary:        Process application arguments the same way as getopt_long
Version:        svn56414
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-lua-alt-getopt
lua_altgetopt is a MIT-licensed module for Lua, for processing application
arguments in the same way as BSD/GNU getopt_long(3) functions do. This module
is made available for lua script writers to have consistent command line
parsing routines.

%package -n texlive-mflogo
Summary:        LaTeX support for Metafont logo fonts
Version:        svn42428
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mflogo.sty) = %{tl_version}

%description -n texlive-mflogo
LaTeX package and font definition file to access the Knuthian mflogo fonts
described in 'The Metafontbook' and to typeset Metafont logos in LaTeX
documents.

%package -n texlive-modes
Summary:        A collection of Metafont mode_def's
Version:        svn77365
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-modes
The modes file collects all known Metafont modes for printing or display
devices, of whatever printing technology. Special provision is made for
write-white printers, and a 'landscape' mode is available, for making suitable
fonts for printers with pixels whose aspect is non-square. The file also
provides definitions that make \specials identifying the mode in Metafont's GF
output, and put coding information and other Xerox-world information in the TFM
file.

%package -n texlive-plain
Summary:        The Plain TeX format
Version:        svn75712
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fontchart.tex) = %{tl_version}
Provides:       tex(gkpmac.tex) = %{tl_version}
Provides:       tex(letterformat.tex) = %{tl_version}
Provides:       tex(list-latin.tex) = %{tl_version}
Provides:       tex(list.tex) = %{tl_version}
Provides:       tex(llist-latin.tex) = %{tl_version}
Provides:       tex(llist.tex) = %{tl_version}
Provides:       tex(mptmac.tex) = %{tl_version}
Provides:       tex(pdftexmagfix.tex) = %{tl_version}
Provides:       tex(picmac.tex) = %{tl_version}
Provides:       tex(plain.tex) = %{tl_version}
Provides:       tex(wlist.tex) = %{tl_version}

%description -n texlive-plain
Contains files used to build the Plain TeX format, as described in the TeXbook,
together with various supporting files (some also discussed in the book).

%package -n texlive-tex-ini-files
Summary:        Model TeX format creation files
Version:        svn73863
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(luatexconfig.tex) = %{tl_version}
Provides:       tex(luatexiniconfig.tex) = %{tl_version}
Provides:       tex(pdftexconfig.tex) = %{tl_version}

%description -n texlive-tex-ini-files
This bundle provides a collection of model .ini files for creating TeX formats.
These files are commonly used to introduce distribution-dependent variations in
formats. They are also used to allow existing format source files to be used
with newer engines, for example to adapt the plain e-TeX source file to work
with XeTeX and LuaTeX.

%package -n texlive-texlive-common
Summary:        TeX Live documentation (common elements)
Version:        svn75685
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-common-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-common-doc <= 11:%{version}

%description -n texlive-texlive-common
TeX Live documentation (common elements)

%package -n texlive-texlive-msg-translations
Summary:        Translations of the TeX Live installer and TeX Live Manager
Version:        svn77513
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-texlive-msg-translations
This package contains the translated messages of the TeX Live installer and TeX
Live Manager. For information on creating or updating translations, see
https://tug.org/texlive/doc.html#install-tl-xlate.

%package -n texlive-unicode-data
Summary:        Unicode data and loaders for TeX
Version:        svn76413
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(load-unicode-data.tex) = %{tl_version}
Provides:       tex(load-unicode-math-classes.tex) = %{tl_version}
Provides:       tex(load-unicode-xetex-classes.tex) = %{tl_version}

%description -n texlive-unicode-data
This bundle provides generic access to Unicode Consortium data for TeX use. It
contains a set of text files provided by the Unicode Consortium which are
currently all from Unicode 8.0.0, with the exception of MathClass.txt which is
not currently part of the Unicode Character Database. Accompanying these source
data are generic TeX loader files allowing this data to be used as part of TeX
runs, in particular in building format files. Currently there are two loader
files: one for general character set up and one for initialising XeTeX
character classes as has been carried out to date by unicode-letters.tex. The
source data are distributed in accordance with the license stipulated by the
Unicode Consortium. The bundle as a whole is co-ordinated by the LaTeX3 Project
as a general resource for TeX users.


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

# disable all hyphenations (except us english)
# The prebuilt language.dat and language.def files enable all possible language hyphenations
# but we probably do not have them installed and we don't want to
cp -f %{buildroot}%{_texmf_main}/tex/generic/config/language.us %{buildroot}%{_texmf_main}/tex/generic/config/language.dat
cp -f %{buildroot}%{_texmf_main}/tex/generic/config/language.us.def %{buildroot}%{_texmf_main}/tex/generic/config/language.def

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Clean out enctex INSTALL files (useless)
rm -rf %{buildroot}%{_texmf_main}/doc/generic/enctex/INSTALL*

# Apply etex patch
pushd %{buildroot}%{_texmf_main}/tex/plain/etex/
patch -p0 < %{_sourcedir}/etex-addlanguage-fix-bz1215257.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-amsfonts
%license ofl.txt
%{_texmf_main}/fonts/afm/public/amsfonts/
%{_texmf_main}/fonts/map/dvips/amsfonts/
%{_texmf_main}/fonts/source/public/amsfonts/
%{_texmf_main}/fonts/tfm/public/amsfonts/
%{_texmf_main}/fonts/type1/public/amsfonts/
%{_texmf_main}/tex/latex/amsfonts/
%{_texmf_main}/tex/plain/amsfonts/
%doc %{_texmf_main}/doc/fonts/amsfonts/

%files -n texlive-cm
%license knuth.txt
%{_texmf_main}/fonts/map/dvips/cm/
%{_texmf_main}/fonts/pk/ljfour/public/
%{_texmf_main}/fonts/source/public/cm/
%{_texmf_main}/fonts/tfm/public/cm/
%doc %{_texmf_main}/doc/fonts/cm/

%files -n texlive-colorprofiles
%license lppl1.3c.txt
%license mit.txt
%license pd.txt
%license other-free.txt
%{_texmf_main}/tex/generic/colorprofiles/
%doc %{_texmf_main}/doc/generic/colorprofiles/

%files -n texlive-ec
%license other-free.txt
%{_texmf_main}/fonts/source/jknappen/ec/
%{_texmf_main}/fonts/tfm/jknappen/ec/
%doc %{_texmf_main}/doc/fonts/ec/

%files -n texlive-enctex
%license gpl2.txt
%{_texmf_main}/tex/generic/enctex/
%doc %{_texmf_main}/doc/generic/enctex/

%files -n texlive-etex
%license knuth.txt
%{_texmf_main}/fonts/source/public/etex/
%{_texmf_main}/fonts/tfm/public/etex/
%{_texmf_main}/tex/plain/etex/
%doc %{_texmf_main}/doc/etex/base/
%doc %{_texmf_main}/doc/man/man1/

%files -n texlive-etex-pkg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/etex-pkg/
%doc %{_texmf_main}/doc/latex/etex-pkg/

%files -n texlive-graphics-def
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/graphics-def/
%doc %{_texmf_main}/doc/latex/graphics-def/

%files -n texlive-hyph-utf8
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%{_texmf_main}/tex/luatex/hyph-utf8/
%doc %{_texmf_main}/doc/generic/hyph-utf8/
%doc %{_texmf_main}/doc/luatex/hyph-utf8/

%files -n texlive-hyphen-base
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/config/
%{_texmf_main}/tex/generic/hyphen/

%files -n texlive-hyphenex
%license pd.txt
%{_texmf_main}/tex/generic/hyphenex/

%files -n texlive-ifplatform
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ifplatform/
%doc %{_texmf_main}/doc/latex/ifplatform/

%files -n texlive-iftex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/iftex/
%doc %{_texmf_main}/doc/generic/iftex/

%files -n texlive-knuth-lib
%license knuth.txt
%{_texmf_main}/fonts/source/public/knuth-lib/
%{_texmf_main}/fonts/tfm/public/knuth-lib/
%{_texmf_main}/tex/generic/knuth-lib/
%{_texmf_main}/tex/plain/knuth-lib/

%files -n texlive-knuth-local
%license pd.txt
%{_texmf_main}/fonts/source/public/knuth-local/
%{_texmf_main}/fonts/tfm/public/knuth-local/
%{_texmf_main}/mft/knuth-local/
%{_texmf_main}/tex/plain/knuth-local/

%files -n texlive-lua-alt-getopt
%license mit.txt
%{_texmf_main}/scripts/lua-alt-getopt/
%doc %{_texmf_main}/doc/support/lua-alt-getopt/

%files -n texlive-mflogo
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/mflogo/
%{_texmf_main}/fonts/tfm/public/mflogo/
%{_texmf_main}/tex/latex/mflogo/
%doc %{_texmf_main}/doc/latex/mflogo/

%files -n texlive-modes
%license pd.txt
%{_texmf_main}/fonts/source/public/modes/
%doc %{_texmf_main}/doc/fonts/modes/

%files -n texlive-plain
%license knuth.txt
%{_texmf_main}/makeindex/plain/
%{_texmf_main}/tex/plain/base/
%{_texmf_main}/tex/plain/config/

%files -n texlive-tex-ini-files
%license pd.txt
%{_texmf_main}/tex/generic/tex-ini-files/
%{_texmf_main}/tex/latex/tex-ini-files/
%doc %{_texmf_main}/doc/generic/tex-ini-files/

%files -n texlive-texlive-common
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/texlive/

%files -n texlive-texlive-msg-translations
%license lppl1.3c.txt
%{_texmf_main}/tlpkg/translations/

%files -n texlive-unicode-data
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/unicode-data/
%doc %{_texmf_main}/doc/generic/unicode-data/

%changelog
* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-8
- Update modes, texlive-msg-translations

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn72890-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jan 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-6
- Fix knuth & public domain license labels to be correct
- Fix capitalization on summaries that needed it
- Flush out unnecessary INSTALL file in enctex

* Fri Jan  9 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-5
- fix description for collection
- update graphics-def (svn76719)

* Wed Oct  8 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-4
- update graphics-def, unicode-data, regenerate with dependency generation turned off for docs

* Mon Sep 22 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-3
- add "legacy" provides for tex(tex) and tex for other Fedora deps

* Mon Sep 22 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-2
- override language.dat/def with files that just have usenglish

* Tue Sep 16 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72890-1
- Update to TeX Live 2025
