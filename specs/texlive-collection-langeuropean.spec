%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langeuropean
Epoch:          12
Version:        svn73414
Release:        4%{?dist}
Summary:        Other European languages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langeuropean.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/armtex.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/armtex.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-albanian.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-albanian.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bosnian.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-bosnian.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-breton.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-breton.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-croatian.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-croatian.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-danish.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-danish.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-dutch.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-dutch.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-estonian.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-estonian.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-finnish.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-finnish.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-friulan.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-friulan.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hungarian.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hungarian.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-icelandic.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-icelandic.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-irish.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-irish.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-kurmanji.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-kurmanji.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latin.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latin.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latvian.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-latvian.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-lithuanian.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-lithuanian.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-macedonian.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-macedonian.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-norsk.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-norsk.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-occitan.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-occitan.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-piedmontese.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-piedmontese.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romanian.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romanian.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romansh.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-romansh.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-samin.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-samin.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-scottish.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-scottish.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovenian.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-slovenian.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-swedish.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-swedish.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-turkish.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-turkish.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-welsh.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-welsh.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/finbib.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gloss-occitan.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gloss-occitan.doc.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hrlatex.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hrlatex.doc.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huaz.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/huaz.doc.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hulipsum.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hulipsum.doc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-albanian.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-croatian.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-danish.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-dutch.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-estonian.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-finnish.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-friulan.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-hungarian.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-hungarian.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-icelandic.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-irish.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-kurmanji.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-latin.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-latvian.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-lithuanian.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-macedonian.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-norwegian.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-occitan.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-piedmontese.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-romanian.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-romansh.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-slovenian.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-swedish.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-turkish.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-uppersorbian.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-welsh.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kaytannollista-latexia.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kaytannollista-latexia.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lithuanian.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lithuanian.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-dutch.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-dutch.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-estonian.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-estonian.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-finnish.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-finnish.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovenian.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-slovenian.doc.tar.xz
Source107:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-turkish.tar.xz
Source108:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-turkish.doc.tar.xz
Source109:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nevelok.tar.xz
Source110:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nevelok.doc.tar.xz
Source111:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rojud.tar.xz
Source112:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rojud.doc.tar.xz
Source113:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swebib.tar.xz
Source114:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/swebib.doc.tar.xz
Source115:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turkmen.tar.xz
Source116:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/turkmen.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-armtex
Requires:       texlive-babel-albanian
Requires:       texlive-babel-bosnian
Requires:       texlive-babel-breton
Requires:       texlive-babel-croatian
Requires:       texlive-babel-danish
Requires:       texlive-babel-dutch
Requires:       texlive-babel-estonian
Requires:       texlive-babel-finnish
Requires:       texlive-babel-friulan
Requires:       texlive-babel-hungarian
Requires:       texlive-babel-icelandic
Requires:       texlive-babel-irish
Requires:       texlive-babel-kurmanji
Requires:       texlive-babel-latin
Requires:       texlive-babel-latvian
Requires:       texlive-babel-lithuanian
Requires:       texlive-babel-macedonian
Requires:       texlive-babel-norsk
Requires:       texlive-babel-occitan
Requires:       texlive-babel-piedmontese
Requires:       texlive-babel-romanian
Requires:       texlive-babel-romansh
Requires:       texlive-babel-samin
Requires:       texlive-babel-scottish
Requires:       texlive-babel-slovenian
Requires:       texlive-babel-swedish
Requires:       texlive-babel-turkish
Requires:       texlive-babel-welsh
Requires:       texlive-collection-basic
Requires:       texlive-finbib
Requires:       texlive-gloss-occitan
Requires:       texlive-hrlatex
Requires:       texlive-huaz
Requires:       texlive-hulipsum
Requires:       texlive-hyphen-albanian
Requires:       texlive-hyphen-croatian
Requires:       texlive-hyphen-danish
Requires:       texlive-hyphen-dutch
Requires:       texlive-hyphen-estonian
Requires:       texlive-hyphen-finnish
Requires:       texlive-hyphen-friulan
Requires:       texlive-hyphen-hungarian
Requires:       texlive-hyphen-icelandic
Requires:       texlive-hyphen-irish
Requires:       texlive-hyphen-kurmanji
Requires:       texlive-hyphen-latin
Requires:       texlive-hyphen-latvian
Requires:       texlive-hyphen-lithuanian
Requires:       texlive-hyphen-macedonian
Requires:       texlive-hyphen-norwegian
Requires:       texlive-hyphen-occitan
Requires:       texlive-hyphen-piedmontese
Requires:       texlive-hyphen-romanian
Requires:       texlive-hyphen-romansh
Requires:       texlive-hyphen-slovenian
Requires:       texlive-hyphen-swedish
Requires:       texlive-hyphen-turkish
Requires:       texlive-hyphen-uppersorbian
Requires:       texlive-hyphen-welsh
Requires:       texlive-kaytannollista-latexia
Requires:       texlive-lithuanian
Requires:       texlive-lshort-dutch
Requires:       texlive-lshort-estonian
Requires:       texlive-lshort-finnish
Requires:       texlive-lshort-slovenian
Requires:       texlive-lshort-turkish
Requires:       texlive-nevelok
Requires:       texlive-rojud
Requires:       texlive-swebib
Requires:       texlive-turkmen

%description
Support for a number of European languages; others (Greek, German, French, ...)
have their own collections, depending simply on the size of the support.


%package -n texlive-armtex
Summary:        A system for writing in Armenian with TeX and LaTeX
Version:        svn69418
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(arm.tex) = %{tl_version}
Provides:       tex(armkb-a8.tex) = %{tl_version}
Provides:       tex(armkb-u8.tex) = %{tl_version}
Provides:       tex(armscii8.def) = %{tl_version}
Provides:       tex(armtex.sty) = %{tl_version}
Provides:       tex(ot6enc.def) = %{tl_version}

%description -n texlive-armtex
ArmTeX is a system for typesetting Armenian text with Plain TeX or LaTeX(2e).
It may be used with input: from a standard Latin keyboard without any special
encoding and/or support for Armenian letters, from any keyboard which uses an
encoding that has Armenian letters in the second half (characters 128-255) of
the extended ASCII table (for example ArmSCII8 Armenian standard), from an
Armenian keyboard using UTF-8 encoding. Users should note that the manuals
still mostly describe the previous version of the package (ArmTeX 2.0).
However, a description of the new features of ArmTeX 3.0 is provided at the end
of the README file.

%package -n texlive-babel-albanian
Summary:        Support for Albanian within babel
Version:        svn57005
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(albanian.ldf) = %{tl_version}

%description -n texlive-babel-albanian
The package provides support for typesetting Albanian (as part of the babel
system).

%package -n texlive-babel-bosnian
Summary:        Babel contrib support for Bosnian
Version:        svn38174
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bosnian.ldf) = %{tl_version}

%description -n texlive-babel-bosnian
The package provides a language definition file that enables support of Bosnian
with babel.

%package -n texlive-babel-breton
Summary:        Babel contributed support for Breton
Version:        svn77470
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(breton.ldf) = %{tl_version}

%description -n texlive-babel-breton
Breton (being, principally, a spoken language) does not have typographic rules
of its own; this package provides an "appropriate" selection of French and
British typographic rules.

%package -n texlive-babel-croatian
Summary:        Babel contributed support for Croatian
Version:        svn35198
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(croatian.ldf) = %{tl_version}

%description -n texlive-babel-croatian
The package establishes Croatian conventions in a document (or a subset of the
conventions, if Croatian is not the main language of the document).

%package -n texlive-babel-danish
Summary:        Babel contributed support for Danish
Version:        svn57642
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(danish.ldf) = %{tl_version}

%description -n texlive-babel-danish
The package provides a language definition, file for use with babel, which
establishes Danish conventions in a document (or a subset of the conventions,
if Danish is not the main language of the document).

%package -n texlive-babel-dutch
Summary:        Babel contributed support for Dutch
Version:        svn60362
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(afrikaans.ldf) = %{tl_version}
Provides:       tex(dutch.ldf) = %{tl_version}

%description -n texlive-babel-dutch
The package provides a language definition, file for use with babel, which
establishes Dutch conventions in a document (or a subset of the conventions, if
Dutch is not the main language of the document).

%package -n texlive-babel-estonian
Summary:        Babel support for Estonian
Version:        svn38064
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(estonian.ldf) = %{tl_version}

%description -n texlive-babel-estonian
The package provides the language definition file for support of Estonian in
babel. Some shortcuts are defined, as well as translations to Estonian of
standard "LaTeX names".

%package -n texlive-babel-finnish
Summary:        Babel support for Finnish
Version:        svn57643
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(finnish.ldf) = %{tl_version}

%description -n texlive-babel-finnish
The package provides a language description file that enables support of
Finnish with babel.

%package -n texlive-babel-friulan
Summary:        Babel/Polyglossia support for Friulan(Furlan)
Version:        svn39861
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(friulan.ldf) = %{tl_version}

%description -n texlive-babel-friulan
The package provides a language description file that enables support of
Friulan either with babel or with polyglossia.

%package -n texlive-babel-hungarian
Summary:        Babel support for Hungarian
Version:        svn77586
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(magyar.ldf) = %{tl_version}

%description -n texlive-babel-hungarian
The package provides a language definition file that enables support of
Hungarian with babel.

%package -n texlive-babel-icelandic
Summary:        Babel support for Icelandic
Version:        svn51551
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(icelandic.ldf) = %{tl_version}

%description -n texlive-babel-icelandic
The package provides the language definition file for support of Icelandic in
babel. Some shortcuts are defined, as well as translations to Icelandic of
standard "LaTeX names".

%package -n texlive-babel-irish
Summary:        Babel support for Irish
Version:        svn30277
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(irish.ldf) = %{tl_version}

%description -n texlive-babel-irish
The package provides the language definition file for support of Irish Gaelic
in babel. The principal content is translations to Irish of standard "LaTeX
names". (No shortcuts are defined.)

%package -n texlive-babel-kurmanji
Summary:        Babel support for Kurmanji
Version:        svn30279
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(kurmanji.ldf) = %{tl_version}

%description -n texlive-babel-kurmanji
The package provides the language definition file for support of Kurmanji in
babel. Kurmanji belongs to the family of Kurdish languages. Some shortcuts are
defined, as well as translations to Kurmanji of standard "LaTeX names". Note
that the package is dealing with 'Northern' Kurdish, written using a
Latin-based alphabet. The arabxetex package offers support for Kurdish written
in Arabic script.

%package -n texlive-babel-latin
Summary:        Babel support for Latin
Version:        svn76176
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(classicallatin.ldf) = %{tl_version}
Provides:       tex(classiclatin.ldf) = %{tl_version}
Provides:       tex(ecclesiasticallatin.ldf) = %{tl_version}
Provides:       tex(ecclesiasticlatin.ldf) = %{tl_version}
Provides:       tex(latin.ldf) = %{tl_version}
Provides:       tex(medievallatin.ldf) = %{tl_version}

%description -n texlive-babel-latin
The babel-latin package provides the babel languages latin, classicallatin,
medievallatin, and ecclesiasticallatin. It also defines several useful
shorthands as well as some modifiers for typographical fine-tuning.

%package -n texlive-babel-latvian
Summary:        Babel support for Latvian
Version:        svn71108
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(latvian.ldf) = %{tl_version}

%description -n texlive-babel-latvian
The package provides the language definition file for support of Latvian in
babel.

%package -n texlive-babel-lithuanian
Summary:        Babel support for documents written in Lithuanian
Version:        svn66513
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lithuanian.ldf) = %{tl_version}

%description -n texlive-babel-lithuanian
Babel support material for documents written in Lithuanian moved from the
lithuanian package into a new package babel-lithuanian to match babel support
for other languages.

%package -n texlive-babel-macedonian
Summary:        Babel module to support Macedonian Cyrillic
Version:        svn39587
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(macedonian.ldf) = %{tl_version}

%description -n texlive-babel-macedonian
The package provides support for Macedonian documents written in Cyrillic, in
babel.

%package -n texlive-babel-norsk
Summary:        Babel support for Norwegian
Version:        svn70691
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(norsk.ldf) = %{tl_version}
Provides:       tex(norwegian.ldf) = %{tl_version}
Provides:       tex(nynorsk.ldf) = %{tl_version}

%description -n texlive-babel-norsk
The package provides the language definition file for support of Norwegian in
babel. Some shortcuts are defined, as well as translations to Norsk of standard
"LaTeX names".

%package -n texlive-babel-occitan
Summary:        Babel support for Occitan
Version:        svn39608
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(occitan.ldf) = %{tl_version}

%description -n texlive-babel-occitan
Occitan language description file with usage instructions.

%package -n texlive-babel-piedmontese
Summary:        Babel support for Piedmontese
Version:        svn30282
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(piedmontese.ldf) = %{tl_version}

%description -n texlive-babel-piedmontese
The package provides the language definition file for support of Piedmontese in
babel. Some shortcuts are defined, as well as translations to Piedmontese of
standard "LaTeX names".

%package -n texlive-babel-romanian
Summary:        Babel support for Romanian
Version:        svn58776
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(romanian.ldf) = %{tl_version}

%description -n texlive-babel-romanian
The package provides the language definition file for support of Romanian in
babel. Translations to Romanian of standard "LaTeX names" are provided.

%package -n texlive-babel-romansh
Summary:        Babel/Polyglossia support for the Romansh language
Version:        svn30286
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(romansh.ldf) = %{tl_version}

%description -n texlive-babel-romansh
The package provides a language description file that enables support of
Romansh either with babel or with polyglossia.

%package -n texlive-babel-samin
Summary:        Babel support for Samin
Version:        svn69604
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(northernsami.ldf) = %{tl_version}
Provides:       tex(samin.ldf) = %{tl_version}

%description -n texlive-babel-samin
The package provides the language definition file for support of North Sami in
babel. (Several Sami dialects/languages are spoken in Finland, Norway, Sweden
and on the Kola Peninsula of Russia). Not all use the same alphabet, and no
attempt is made to support any other than North Sami here. Some shortcuts are
defined, as well as translations to Norsk of standard "LaTeX names".

%package -n texlive-babel-scottish
Summary:        Babel support for Scottish Gaelic
Version:        svn69610
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(scottish.ldf) = %{tl_version}
Provides:       tex(scottishgaelic.ldf) = %{tl_version}

%description -n texlive-babel-scottish
The package provides the language definition file for support of Gaidhlig
(Scottish Gaelic) in babel. Some shortcuts are defined, as well as translations
of standard "LaTeX names".

%package -n texlive-babel-slovenian
Summary:        Babel support for typesetting Slovenian
Version:        svn75181
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(slovene.ldf) = %{tl_version}
Provides:       tex(slovenian.ldf) = %{tl_version}

%description -n texlive-babel-slovenian
The package provides the language definition file for support of Slovenian in
babel. Several shortcuts are defined, as well as translations to Slovenian of
standard "LaTeX names".

%package -n texlive-babel-swedish
Summary:        Babel support for typesetting Swedish
Version:        svn57647
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(swedish.ldf) = %{tl_version}

%description -n texlive-babel-swedish
The package provides the language definition file for Swedish.

%package -n texlive-babel-turkish
Summary:        Babel support for Turkish documents
Version:        svn51560
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(turkish.ldf) = %{tl_version}

%description -n texlive-babel-turkish
The package provides support, within babel, of the Turkish language.

%package -n texlive-babel-welsh
Summary:        Babel support for Welsh
Version:        svn73855
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(welsh.ldf) = %{tl_version}

%description -n texlive-babel-welsh
The package provides the language definition file for Welsh. (Mostly
Welsh-language versions of the standard names in a LaTeX file.)

%package -n texlive-finbib
Summary:        A Finnish version of plain.bst
Version:        svn76790
License:        LicenseRef-Bibtex
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-finbib
A Finnish version of plain.bst

%package -n texlive-gloss-occitan
Summary:        Polyglossia support for Occitan
Version:        svn52593
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-gloss-occitan-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-gloss-occitan-doc <= 11:%{version}

%description -n texlive-gloss-occitan
Occitan language description file for polyglossia

%package -n texlive-hrlatex
Summary:        LaTeX support for Croatian documents
Version:        svn18020
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amsopn.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(cancel.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(multicol.sty)
Requires:       tex(optional.sty)
Requires:       tex(paralist.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(fsbmath.sty) = %{tl_version}
Provides:       tex(hrlatex.sty) = %{tl_version}

%description -n texlive-hrlatex
This package simplifies creation of new documents for the (average) Croatian
user. As an example, a class file hrdipl.cls (designed for the graduation
thesis at the University of Zagreb) and sample thesis documents are included.

%package -n texlive-huaz
Summary:        Automatic Hungarian definite articles and suffixes
Version:        svn77576
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Requires:       tex(refcount.sty)
Requires:       tex(xstring.sty)
Provides:       tex(huaz.sty) = %{tl_version}

%description -n texlive-huaz
In Hungarian there are two definite articles, "a" and "az", which are
determined by the pronunciation of the subsequent word. The definite article is
"az", if the first phoneme of the pronounced word is a vowel, otherwise it is
"a". The huaz package helps the user to insert automatically the correct
definite article for cross-references and other commands containing text.
Another service offered by the package is the automatic suffixing of numbers
and cross-references, also based on their pronunciation.

%package -n texlive-hulipsum
Summary:        Hungarian dummy text (Lorum ipse)
Version:        svn77317
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hulipsum.sty) = %{tl_version}

%description -n texlive-hulipsum
Lorem ipsum is an improper Latin filler dummy text, cf. the lipsum package. It
is commonly used for demonstrating the textual elements of a document template.
Lorum ipse is a Hungarian variation of Lorem ipsum. (Lorum is a Hungarian card
game, and ipse is a Hungarian slang word meaning bloke.) With this package you
can typeset 150 paragraphs of Lorum ipse. All paragraphs are taken with
permission from http://www.lorumipse.hu. Thanks to Lorum Ipse Lab (Viktor Nagy
and David Takacs) for their work.

%package -n texlive-hyphen-albanian
Summary:        Albanian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-quote-sq.tex) = %{tl_version}
Provides:       tex(hyph-sq.ec.tex) = %{tl_version}
Provides:       tex(hyph-sq.tex) = %{tl_version}
Provides:       tex(loadhyph-sq.tex) = %{tl_version}

%description -n texlive-hyphen-albanian
Hyphenation patterns for Albanian in UTF-8 and T1 encoding.

%package -n texlive-hyphen-croatian
Summary:        Croatian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hr.ec.tex) = %{tl_version}
Provides:       tex(hyph-hr.tex) = %{tl_version}
Provides:       tex(loadhyph-hr.tex) = %{tl_version}

%description -n texlive-hyphen-croatian
Hyphenation patterns for Croatian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-danish
Summary:        Danish hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-da.ec.tex) = %{tl_version}
Provides:       tex(hyph-da.tex) = %{tl_version}
Provides:       tex(loadhyph-da.tex) = %{tl_version}

%description -n texlive-hyphen-danish
Hyphenation patterns for Danish in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-dutch
Summary:        Dutch hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-nl.ec.tex) = %{tl_version}
Provides:       tex(hyph-nl.tex) = %{tl_version}
Provides:       tex(loadhyph-nl.tex) = %{tl_version}

%description -n texlive-hyphen-dutch
Hyphenation patterns for Dutch in T1/EC and UTF-8 encodings. These patterns
don't handle cases like 'menuutje' > 'menu-tje', and don't hyphenate words that
have different hyphenations according to their meaning.

%package -n texlive-hyphen-estonian
Summary:        Estonian hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-et.ec.tex) = %{tl_version}
Provides:       tex(hyph-et.tex) = %{tl_version}
Provides:       tex(loadhyph-et.tex) = %{tl_version}

%description -n texlive-hyphen-estonian
Hyphenation patterns for Estonian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-finnish
Summary:        Finnish hyphenation patterns.
Version:        svn73410
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fi-x-school.ec.tex) = %{tl_version}
Provides:       tex(hyph-fi-x-school.tex) = %{tl_version}
Provides:       tex(hyph-fi.ec.tex) = %{tl_version}
Provides:       tex(hyph-fi.tex) = %{tl_version}
Provides:       tex(loadhyph-fi-x-school.tex) = %{tl_version}
Provides:       tex(loadhyph-fi.tex) = %{tl_version}

%description -n texlive-hyphen-finnish
Hyphenation patterns for Finnish in T1 and UTF-8 encodings. The older set,
labelled just 'fi', tries to implement etymological rules, while the newer ones
(fi-x-school) implements the simpler rules taught at Finnish school.

%package -n texlive-hyphen-friulan
Summary:        Friulan hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fur.ec.tex) = %{tl_version}
Provides:       tex(hyph-fur.tex) = %{tl_version}
Provides:       tex(hyph-quote-fur.tex) = %{tl_version}
Provides:       tex(loadhyph-fur.tex) = %{tl_version}

%description -n texlive-hyphen-friulan
Hyphenation patterns for Friulan in ASCII encoding. They are supposed to comply
with the common spelling of the Friulan (Furlan) language as fixed by the
Regional Law N.15/96 dated November 6, 1996 and its following amendments.

%package -n texlive-hyphen-hungarian
Summary:        Hungarian hyphenation patterns.
Version:        svn73410
License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hu.ec.tex) = %{tl_version}
Provides:       tex(hyph-hu.tex) = %{tl_version}
Provides:       tex(loadhyph-hu.tex) = %{tl_version}

%description -n texlive-hyphen-hungarian
Hyphenation patterns for Hungarian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-icelandic
Summary:        Icelandic hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-is.ec.tex) = %{tl_version}
Provides:       tex(hyph-is.tex) = %{tl_version}
Provides:       tex(loadhyph-is.tex) = %{tl_version}

%description -n texlive-hyphen-icelandic
Hyphenation patterns for Icelandic in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-irish
Summary:        Irish hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-or-later OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ga.ec.tex) = %{tl_version}
Provides:       tex(hyph-ga.tex) = %{tl_version}
Provides:       tex(loadhyph-ga.tex) = %{tl_version}

%description -n texlive-hyphen-irish
Hyphenation patterns for Irish (Gaeilge) in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-kurmanji
Summary:        Kurmanji hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-kmr.ec.tex) = %{tl_version}
Provides:       tex(hyph-kmr.tex) = %{tl_version}
Provides:       tex(loadhyph-kmr.tex) = %{tl_version}

%description -n texlive-hyphen-kurmanji
Hyphenation patterns for Kurmanji (Northern Kurdish) as spoken in Turkey and by
the Kurdish diaspora in Europe, in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-latin
Summary:        Latin hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-la-x-classic.ec.tex) = %{tl_version}
Provides:       tex(hyph-la-x-classic.tex) = %{tl_version}
Provides:       tex(hyph-la-x-liturgic.ec.tex) = %{tl_version}
Provides:       tex(hyph-la-x-liturgic.tex) = %{tl_version}
Provides:       tex(hyph-la.ec.tex) = %{tl_version}
Provides:       tex(hyph-la.tex) = %{tl_version}
Provides:       tex(loadhyph-la-x-classic.tex) = %{tl_version}
Provides:       tex(loadhyph-la-x-liturgic.tex) = %{tl_version}
Provides:       tex(loadhyph-la.tex) = %{tl_version}

%description -n texlive-hyphen-latin
Hyphenation patterns for Latin in T1/EC and UTF-8 encodings, mainly in modern
spelling (u when u is needed and v when v is needed), medieval spelling with
the ligatures \ae and \oe and the (uncial) lowercase 'v' written as a 'u' is
also supported. Apparently there is no conflict between the patterns of modern
Latin and those of medieval Latin. Hyphenation patterns for the Classical Latin
in T1/EC and UTF-8 encodings. Classical Latin hyphenation patterns are
different from those of 'plain' Latin, the latter being more adapted to modern
Latin. Hyphenation patterns for the Liturgical Latin in T1/EC and UTF-8
encodings.

%package -n texlive-hyphen-latvian
Summary:        Latvian hyphenation patterns.
Version:        svn73410
License:        LGPL-2.1-only OR GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-lv.l7x.tex) = %{tl_version}
Provides:       tex(hyph-lv.tex) = %{tl_version}
Provides:       tex(loadhyph-lv.tex) = %{tl_version}

%description -n texlive-hyphen-latvian
Hyphenation patterns for Latvian in L7X and UTF-8 encodings.

%package -n texlive-hyphen-lithuanian
Summary:        Lithuanian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-lt.l7x.tex) = %{tl_version}
Provides:       tex(hyph-lt.tex) = %{tl_version}
Provides:       tex(loadhyph-lt.tex) = %{tl_version}

%description -n texlive-hyphen-lithuanian
Hyphenation patterns for Lithuanian in L7X and UTF-8 encodings. \lefthyphenmin
and \righthyphenmin have to be at least 2.

%package -n texlive-hyphen-macedonian
Summary:        Macedonian hyphenation patterns.
Version:        svn73410
License:        GPL-1.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-mk.macedonian.tex) = %{tl_version}
Provides:       tex(hyph-mk.tex) = %{tl_version}
Provides:       tex(loadhyph-mk.tex) = %{tl_version}

%description -n texlive-hyphen-macedonian
Hyphenation patterns for Macedonian

%package -n texlive-hyphen-norwegian
Summary:        Norwegian Bokmal and Nynorsk hyphenation patterns.
Version:        svn73410
License:        FSFAP
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-nb.ec.tex) = %{tl_version}
Provides:       tex(hyph-nb.tex) = %{tl_version}
Provides:       tex(hyph-nn.ec.tex) = %{tl_version}
Provides:       tex(hyph-nn.tex) = %{tl_version}
Provides:       tex(hyph-no.tex) = %{tl_version}
Provides:       tex(loadhyph-nb.tex) = %{tl_version}
Provides:       tex(loadhyph-nn.tex) = %{tl_version}

%description -n texlive-hyphen-norwegian
Hyphenation patterns for Norwegian Bokmal and Nynorsk in T1/EC and UTF-8
encodings.

%package -n texlive-hyphen-occitan
Summary:        Occitan hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-oc.ec.tex) = %{tl_version}
Provides:       tex(hyph-oc.tex) = %{tl_version}
Provides:       tex(hyph-quote-oc.tex) = %{tl_version}
Provides:       tex(loadhyph-oc.tex) = %{tl_version}

%description -n texlive-hyphen-occitan
Hyphenation patterns for Occitan in T1/EC and UTF-8 encodings. They are
supposed to be valid for all the Occitan variants spoken and written in the
wide area called 'Occitanie' by the French. It ranges from the Val d'Aran
within Catalunya, to the South Western Italian Alps encompassing the southern
half of the French pentagon.

%package -n texlive-hyphen-piedmontese
Summary:        Piedmontese hyphenation patterns.
Version:        svn73410
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-pms.tex) = %{tl_version}
Provides:       tex(hyph-quote-pms.tex) = %{tl_version}
Provides:       tex(loadhyph-pms.tex) = %{tl_version}

%description -n texlive-hyphen-piedmontese
Hyphenation patterns for Piedmontese in ASCII encoding. Compliant with
'Gramatica dla lengua piemonteisa' by Camillo Brero.

%package -n texlive-hyphen-romanian
Summary:        Romanian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ro.ec.tex) = %{tl_version}
Provides:       tex(hyph-ro.tex) = %{tl_version}
Provides:       tex(loadhyph-ro.tex) = %{tl_version}

%description -n texlive-hyphen-romanian
Hyphenation patterns for Romanian in T1/EC and UTF-8 encodings. The UTF-8
patterns use U+0219 for the character 's with comma accent' and U+021B for 't
with comma accent', but we may consider using U+015F and U+0163 as well in the
future. Generated by PatGen2-output hyphen-level 9.

%package -n texlive-hyphen-romansh
Summary:        Romansh hyphenation patterns.
Version:        svn74115
License:        MIT OR LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-rm.ec.tex) = %{tl_version}
Provides:       tex(hyph-rm.tex) = %{tl_version}
Provides:       tex(loadhyph-rm.tex) = %{tl_version}

%description -n texlive-hyphen-romansh
Hyphenation patterns for Romansh. All Romansh idioms and Rumantsch Grischun
taken into account, developed in collaboration with Fundaziun Medias
Rumantschas (Romansh news agency) and Lia Rumantscha (Romansh umbrella
organisation).

%package -n texlive-hyphen-slovenian
Summary:        Slovenian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sl.ec.tex) = %{tl_version}
Provides:       tex(hyph-sl.tex) = %{tl_version}
Provides:       tex(loadhyph-sl.tex) = %{tl_version}

%description -n texlive-hyphen-slovenian
Hyphenation patterns for Slovenian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-swedish
Summary:        Swedish hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sv.ec.tex) = %{tl_version}
Provides:       tex(hyph-sv.tex) = %{tl_version}
Provides:       tex(loadhyph-sv.tex) = %{tl_version}

%description -n texlive-hyphen-swedish
Hyphenation patterns for Swedish in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-turkish
Summary:        Turkish hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-tr.ec.tex) = %{tl_version}
Provides:       tex(hyph-tr.tex) = %{tl_version}
Provides:       tex(loadhyph-tr.tex) = %{tl_version}

%description -n texlive-hyphen-turkish
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings. Auto-generated
from a script included in the distribution. The patterns for Turkish were first
produced for the Ottoman Texts Project in 1987 and were suitable for both
Modern Turkish and Ottoman Turkish in Latin script, however the required
character set didn't fit into EC encoding, so support for Ottoman Turkish had
to be dropped to keep compatibility with 8-bit engines.

%package -n texlive-hyphen-uppersorbian
Summary:        Upper Sorbian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hsb.ec.tex) = %{tl_version}
Provides:       tex(hyph-hsb.tex) = %{tl_version}
Provides:       tex(loadhyph-hsb.tex) = %{tl_version}

%description -n texlive-hyphen-uppersorbian
Hyphenation patterns for Upper Sorbian in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-welsh
Summary:        Welsh hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-cy.ec.tex) = %{tl_version}
Provides:       tex(hyph-cy.tex) = %{tl_version}
Provides:       tex(loadhyph-cy.tex) = %{tl_version}

%description -n texlive-hyphen-welsh
Hyphenation patterns for Welsh in T1/EC and UTF-8 encodings.

%package -n texlive-kaytannollista-latexia
Summary:        Practical manual for LaTeX (Finnish)
Version:        svn77555
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-kaytannollista-latexia-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-kaytannollista-latexia-doc <= 11:%{version}

%description -n texlive-kaytannollista-latexia
"Kaytannollista Latexia" is a practical manual for LaTeX written in the Finnish
language. The manual covers most of the topics that a typical document author
needs. So it can be a useful guide for beginners as well as a reference manual
for advanced users.

%package -n texlive-lithuanian
Summary:        Lithuanian language support
Version:        svn66461
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(cp775.def) = %{tl_version}
Provides:       tex(l7xenc.def) = %{tl_version}
Provides:       tex(l7xenc.sty) = %{tl_version}
Provides:       tex(latin7.def) = %{tl_version}

%description -n texlive-lithuanian
This language support package provides: extra 8-bit encoding L7x used by
fontenc: l7xenc.def, l7xenc.dfu, l7xenc.sty Lithuanian TeX support for URW
family Type1 fonts: map, fd, tfm with L7x encoding extra code page definitions
used by inputenc: cp775.def, latin7.def

%package -n texlive-lshort-dutch
Summary:        Introduction to LaTeX in Dutch
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-dutch-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-dutch-doc <= 11:%{version}

%description -n texlive-lshort-dutch
This is the Dutch (Nederlands) translation of the Short Introduction to
LaTeX2e.

%package -n texlive-lshort-estonian
Summary:        Estonian introduction to LaTeX
Version:        svn39323
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-estonian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-estonian-doc <= 11:%{version}

%description -n texlive-lshort-estonian
This is the Estonian translation of Short Introduction to LaTeX2e.

%package -n texlive-lshort-finnish
Summary:        Finnish introduction to LaTeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-finnish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-finnish-doc <= 11:%{version}

%description -n texlive-lshort-finnish
This is the Finnish translation of Short Introduction to LaTeX2e, with added
coverage of Finnish typesetting rules.

%package -n texlive-lshort-slovenian
Summary:        Slovenian translation of lshort
Version:        svn77050
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-slovenian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-slovenian-doc <= 11:%{version}

%description -n texlive-lshort-slovenian
A Slovenian translation of the Not So Short Introduction to LaTeX2e.

%package -n texlive-lshort-turkish
Summary:        Turkish introduction to LaTeX
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-turkish-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-turkish-doc <= 11:%{version}

%description -n texlive-lshort-turkish
A Turkish translation of Oetiker's (not so) short introduction.

%package -n texlive-nevelok
Summary:        LaTeX package for automatic definite articles for Hungarian
Version:        svn39029
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(nevelok.sty) = %{tl_version}

%description -n texlive-nevelok
LaTeX package for automatic definite articles for Hungarian

%package -n texlive-rojud
Summary:        A font with the images of the counties of Romania
Version:        svn56895
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(iftex.sty)
Provides:       tex(rojud.sty) = %{tl_version}

%description -n texlive-rojud
This package provides a Type 1 font with images of the 42 counties of Romania,
constructed using a general method which is described in detail in the
documentation. The package name is an abbreviation of "judetele Romaniei" (=
counties of Romania).

%package -n texlive-swebib
Summary:        Swedish bibliography styles
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-swebib
The bundle contains Swedish versions of the standard bibliography styles, and
of the style plainnat. The styles should be functionally equivalent to the
corresponding original styles, apart from the Swedish translations. The styles
do not implement Swedish collation.

%package -n texlive-turkmen
Summary:        Babel support for Turkmen
Version:        svn17748
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(turkmen.ldf) = %{tl_version}

%description -n texlive-turkmen
The package provides support for Turkmen in babel, but integration with babel
is not available.

%post -n texlive-hyphen-albanian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/albanian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "albanian loadhyph-sq.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{albanian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{albanian}{loadhyph-sq.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-albanian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/albanian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{albanian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-croatian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/croatian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "croatian loadhyph-hr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{croatian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{croatian}{loadhyph-hr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-croatian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/croatian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{croatian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-danish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/danish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "danish loadhyph-da.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{danish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{danish}{loadhyph-da.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-danish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/danish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{danish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-dutch
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/dutch.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "dutch loadhyph-nl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{dutch}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{dutch}{loadhyph-nl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-dutch
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/dutch.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{dutch}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-estonian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/estonian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "estonian loadhyph-et.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{estonian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{estonian}{loadhyph-et.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-estonian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/estonian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{estonian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-finnish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/finnish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "finnish loadhyph-fi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{finnish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{finnish}{loadhyph-fi.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/schoolfinnish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "schoolfinnish loadhyph-fi-x-school.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{schoolfinnish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{schoolfinnish}{loadhyph-fi-x-school.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-finnish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/finnish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{finnish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/schoolfinnish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{schoolfinnish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-friulan
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/friulan.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "friulan loadhyph-fur.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{friulan}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{friulan}{loadhyph-fur.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-friulan
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/friulan.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{friulan}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-hungarian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/hungarian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "hungarian loadhyph-hu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{hungarian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{hungarian}{loadhyph-hu.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-hungarian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/hungarian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{hungarian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-icelandic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/icelandic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "icelandic loadhyph-is.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{icelandic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{icelandic}{loadhyph-is.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-icelandic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/icelandic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{icelandic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-irish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/irish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "irish loadhyph-ga.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{irish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{irish}{loadhyph-ga.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-irish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/irish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{irish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-kurmanji
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/kurmanji.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "kurmanji loadhyph-kmr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{kurmanji}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{kurmanji}{loadhyph-kmr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-kurmanji
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/kurmanji.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{kurmanji}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-latin
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/classiclatin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "classiclatin loadhyph-la-x-classic.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{classiclatin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{classiclatin}{loadhyph-la-x-classic.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/latin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "latin loadhyph-la.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{latin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{latin}{loadhyph-la.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/liturgicallatin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "liturgicallatin loadhyph-la-x-liturgic.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{liturgicallatin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{liturgicallatin}{loadhyph-la-x-liturgic.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-latin
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/classiclatin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{classiclatin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/latin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{latin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/liturgicallatin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{liturgicallatin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-latvian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/latvian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "latvian loadhyph-lv.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{latvian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{latvian}{loadhyph-lv.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-latvian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/latvian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{latvian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-lithuanian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/lithuanian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "lithuanian loadhyph-lt.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{lithuanian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{lithuanian}{loadhyph-lt.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-lithuanian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/lithuanian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{lithuanian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-macedonian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/macedonian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "macedonian loadhyph-mk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{macedonian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{macedonian}{loadhyph-mk.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-macedonian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/macedonian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{macedonian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-norwegian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/bokmal.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "bokmal loadhyph-nb.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=norwegian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=norwegian" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=norsk.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=norsk" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{bokmal}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{bokmal}{loadhyph-nb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{norwegian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{norwegian}{loadhyph-nb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{norsk}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{norsk}{loadhyph-nb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/nynorsk.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "nynorsk loadhyph-nn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{nynorsk}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{nynorsk}{loadhyph-nn.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-norwegian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/bokmal.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=norwegian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=norsk.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{bokmal}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{norwegian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{norsk}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/nynorsk.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{nynorsk}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-occitan
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/occitan.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "occitan loadhyph-oc.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{occitan}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{occitan}{loadhyph-oc.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-occitan
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/occitan.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{occitan}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-piedmontese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/piedmontese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "piedmontese loadhyph-pms.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{piedmontese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{piedmontese}{loadhyph-pms.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-piedmontese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/piedmontese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{piedmontese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-romanian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/romanian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "romanian loadhyph-ro.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{romanian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{romanian}{loadhyph-ro.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-romanian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/romanian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{romanian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-romansh
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/romansh.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "romansh loadhyph-rm.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{romansh}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{romansh}{loadhyph-rm.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-romansh
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/romansh.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{romansh}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-slovenian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/slovenian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "slovenian loadhyph-sl.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=slovene.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=slovene" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{slovenian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{slovenian}{loadhyph-sl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{slovene}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{slovene}{loadhyph-sl.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-slovenian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/slovenian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=slovene.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{slovenian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{slovene}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-swedish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/swedish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "swedish loadhyph-sv.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{swedish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{swedish}{loadhyph-sv.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-swedish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/swedish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{swedish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-turkish
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/turkish.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "turkish loadhyph-tr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{turkish}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-turkish
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/turkish.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{turkish}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-uppersorbian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/uppersorbian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "uppersorbian loadhyph-hsb.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{uppersorbian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{uppersorbian}{loadhyph-hsb.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-uppersorbian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/uppersorbian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{uppersorbian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-welsh
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/welsh.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "welsh loadhyph-cy.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{welsh}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{welsh}{loadhyph-cy.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-welsh
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/welsh.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{welsh}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-armtex
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/armenian/
%{_texmf_main}/fonts/map/dvips/armenian/
%{_texmf_main}/fonts/source/public/armenian/
%{_texmf_main}/fonts/tfm/public/armenian/
%{_texmf_main}/fonts/type1/public/armenian/
%{_texmf_main}/tex/latex/armenian/
%{_texmf_main}/tex/plain/armenian/
%doc %{_texmf_main}/doc/generic/armenian/

%files -n texlive-babel-albanian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-albanian/
%doc %{_texmf_main}/doc/generic/babel-albanian/

%files -n texlive-babel-bosnian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-bosnian/
%doc %{_texmf_main}/doc/generic/babel-bosnian/

%files -n texlive-babel-breton
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-breton/
%doc %{_texmf_main}/doc/generic/babel-breton/

%files -n texlive-babel-croatian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-croatian/
%doc %{_texmf_main}/doc/generic/babel-croatian/

%files -n texlive-babel-danish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-danish/
%doc %{_texmf_main}/doc/generic/babel-danish/

%files -n texlive-babel-dutch
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-dutch/
%doc %{_texmf_main}/doc/generic/babel-dutch/

%files -n texlive-babel-estonian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-estonian/
%doc %{_texmf_main}/doc/generic/babel-estonian/

%files -n texlive-babel-finnish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-finnish/
%doc %{_texmf_main}/doc/generic/babel-finnish/

%files -n texlive-babel-friulan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-friulan/
%doc %{_texmf_main}/doc/generic/babel-friulan/

%files -n texlive-babel-hungarian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-hungarian/
%doc %{_texmf_main}/doc/generic/babel-hungarian/

%files -n texlive-babel-icelandic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-icelandic/
%doc %{_texmf_main}/doc/generic/babel-icelandic/

%files -n texlive-babel-irish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-irish/
%doc %{_texmf_main}/doc/generic/babel-irish/

%files -n texlive-babel-kurmanji
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-kurmanji/
%doc %{_texmf_main}/doc/generic/babel-kurmanji/

%files -n texlive-babel-latin
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-latin/
%doc %{_texmf_main}/doc/generic/babel-latin/

%files -n texlive-babel-latvian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-latvian/
%doc %{_texmf_main}/doc/generic/babel-latvian/

%files -n texlive-babel-lithuanian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-lithuanian/
%doc %{_texmf_main}/doc/generic/babel-lithuanian/

%files -n texlive-babel-macedonian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-macedonian/
%doc %{_texmf_main}/doc/generic/babel-macedonian/

%files -n texlive-babel-norsk
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-norsk/
%doc %{_texmf_main}/doc/generic/babel-norsk/

%files -n texlive-babel-occitan
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-occitan/
%doc %{_texmf_main}/doc/generic/babel-occitan/

%files -n texlive-babel-piedmontese
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-piedmontese/
%doc %{_texmf_main}/doc/generic/babel-piedmontese/

%files -n texlive-babel-romanian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-romanian/
%doc %{_texmf_main}/doc/generic/babel-romanian/

%files -n texlive-babel-romansh
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-romansh/
%doc %{_texmf_main}/doc/generic/babel-romansh/

%files -n texlive-babel-samin
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-samin/
%doc %{_texmf_main}/doc/generic/babel-samin/

%files -n texlive-babel-scottish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-scottish/
%doc %{_texmf_main}/doc/generic/babel-scottish/

%files -n texlive-babel-slovenian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-slovenian/
%doc %{_texmf_main}/doc/generic/babel-slovenian/

%files -n texlive-babel-swedish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-swedish/
%doc %{_texmf_main}/doc/generic/babel-swedish/

%files -n texlive-babel-turkish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-turkish/
%doc %{_texmf_main}/doc/generic/babel-turkish/

%files -n texlive-babel-welsh
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-welsh/
%doc %{_texmf_main}/doc/generic/babel-welsh/

%files -n texlive-finbib
%license other-free.txt
%{_texmf_main}/bibtex/bst/finbib/

%files -n texlive-gloss-occitan
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/gloss-occitan/

%files -n texlive-hrlatex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hrlatex/
%doc %{_texmf_main}/doc/latex/hrlatex/

%files -n texlive-huaz
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/huaz/
%doc %{_texmf_main}/doc/latex/huaz/

%files -n texlive-hulipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hulipsum/
%doc %{_texmf_main}/doc/latex/hulipsum/

%files -n texlive-hyphen-albanian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-croatian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-danish
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-dutch
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-estonian
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-finnish
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-friulan
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-hungarian
%license other-free.txt
%license gpl2.txt
%license lgpl2.1.txt
%{_texmf_main}/tex/generic/hyph-utf8/
%doc %{_texmf_main}/doc/generic/huhyphen/
%doc %{_texmf_main}/doc/generic/hyph-utf8/

%files -n texlive-hyphen-icelandic
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-irish
%license gpl2.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-kurmanji
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-latin
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-latvian
%license lgpl2.1.txt
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-lithuanian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-macedonian
%license gpl.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-norwegian
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-occitan
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-piedmontese
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-romanian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-romansh
%license mit.txt
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-slovenian
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-swedish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-turkish
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-uppersorbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-welsh
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-kaytannollista-latexia
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/kaytannollista-latexia/

%files -n texlive-lithuanian
%license lppl1.3c.txt
%{_texmf_main}/fonts/enc/dvips/lithuanian/
%{_texmf_main}/fonts/map/dvips/lithuanian/
%{_texmf_main}/fonts/tfm/public/lithuanian/
%{_texmf_main}/tex/latex/lithuanian/
%doc %{_texmf_main}/doc/latex/lithuanian/

%files -n texlive-lshort-dutch
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-dutch/

%files -n texlive-lshort-estonian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-estonian/

%files -n texlive-lshort-finnish
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-finnish/

%files -n texlive-lshort-slovenian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-slovenian/

%files -n texlive-lshort-turkish
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-turkish/

%files -n texlive-nevelok
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/nevelok/
%doc %{_texmf_main}/doc/latex/nevelok/

%files -n texlive-rojud
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/rojud/
%{_texmf_main}/fonts/tfm/public/rojud/
%{_texmf_main}/fonts/type1/public/rojud/
%{_texmf_main}/tex/latex/rojud/
%doc %{_texmf_main}/doc/fonts/rojud/

%files -n texlive-swebib
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/swebib/
%doc %{_texmf_main}/doc/latex/swebib/

%files -n texlive-turkmen
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/turkmen/
%doc %{_texmf_main}/doc/latex/turkmen/

%changelog
* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn73414-4
- Update babel-breton babel-hungarian huaz kaytannollista-latexia
- fix licensing files

* Sat Jan 24 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn73414-3
- fix descriptions, licensing, update to latest versions for components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73414-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn73414-1
- Update to TeX Live 2025
