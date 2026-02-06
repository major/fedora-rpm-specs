%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langother
Epoch:          12
Version:        svn74620
Release:        3%{?dist}
Summary:        Other languages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langother.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/akshar.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/akshar.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsldoc-vn.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amsldoc-vn.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aramaic-serto.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aramaic-serto.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-azerbaijani.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-azerbaijani.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-esperanto.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-esperanto.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-georgian.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-georgian.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hebrew.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-hebrew.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-indonesian.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-indonesian.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-interlingua.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-interlingua.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-malay.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-malay.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-sorbian.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-sorbian.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-thai.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-thai.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-vietnamese.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-vietnamese.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangla.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangla.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangtex.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bangtex.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bengali.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bengali.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/burmese.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/burmese.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjhebrew.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjhebrew.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctib.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctib.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/culmus.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/culmus.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop-t1.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ethiop-t1.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fc.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonts-tlwg.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fonts-tlwg.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hebrew-fonts.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hebrew-fonts.doc.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hindawi-latex-template.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hindawi-latex-template.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-afrikaans.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-armenian.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-coptic.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-esperanto.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-ethiopic.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-georgian.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-hebrew.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-indic.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-indonesian.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-interlingua.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-sanskrit.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-sanskrit.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-thai.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-turkmen.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-vietnamese.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-mr.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-mr.doc.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexbangla.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexbangla.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latino-sine-flexione.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latino-sine-flexione.doc.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-thai.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-thai.doc.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-vietnamese.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-vietnamese.doc.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem-vn.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ntheorem-vn.doc.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-bn.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-bn.doc.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-id.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-id.doc.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-ur.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/quran-ur.doc.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit.doc.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit-t1.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sanskrit-t1.doc.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaienum.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaienum.doc.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaispec.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thaispec.doc.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuzuk.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tuzuk.doc.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-alphabets.tar.xz
Source98:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/unicode-alphabets.doc.tar.xz
Source99:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vntex.tar.xz
Source100:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vntex.doc.tar.xz
Source101:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri.tar.xz
Source102:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri.doc.tar.xz
Source103:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri-latex.tar.xz
Source104:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wnri-latex.doc.tar.xz
Source105:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-devanagari.tar.xz
Source106:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex-devanagari.doc.tar.xz
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-akshar
Requires:       texlive-amsldoc-vn
Requires:       texlive-aramaic-serto
Requires:       texlive-babel-azerbaijani
Requires:       texlive-babel-esperanto
Requires:       texlive-babel-georgian
Requires:       texlive-babel-hebrew
Requires:       texlive-babel-indonesian
Requires:       texlive-babel-interlingua
Requires:       texlive-babel-malay
Requires:       texlive-babel-sorbian
Requires:       texlive-babel-thai
Requires:       texlive-babel-vietnamese
Requires:       texlive-bangla
Requires:       texlive-bangtex
Requires:       texlive-bengali
Requires:       texlive-burmese
Requires:       texlive-cjhebrew
Requires:       texlive-collection-basic
Requires:       texlive-ctib
Requires:       texlive-culmus
Requires:       texlive-ebong
Requires:       texlive-ethiop
Requires:       texlive-ethiop-t1
Requires:       texlive-fc
Requires:       texlive-fonts-tlwg
Requires:       texlive-hebrew-fonts
Requires:       texlive-hindawi-latex-template
Requires:       texlive-hyphen-afrikaans
Requires:       texlive-hyphen-armenian
Requires:       texlive-hyphen-coptic
Requires:       texlive-hyphen-esperanto
Requires:       texlive-hyphen-ethiopic
Requires:       texlive-hyphen-georgian
Requires:       texlive-hyphen-hebrew
Requires:       texlive-hyphen-indic
Requires:       texlive-hyphen-indonesian
Requires:       texlive-hyphen-interlingua
Requires:       texlive-hyphen-sanskrit
Requires:       texlive-hyphen-thai
Requires:       texlive-hyphen-turkmen
Requires:       texlive-hyphen-vietnamese
Requires:       texlive-latex-mr
Requires:       texlive-latexbangla
Requires:       texlive-latino-sine-flexione
Requires:       texlive-lshort-thai
Requires:       texlive-lshort-vietnamese
Requires:       texlive-ntheorem-vn
Requires:       texlive-quran-bn
Requires:       texlive-quran-id
Requires:       texlive-quran-ur
Requires:       texlive-sanskrit
Requires:       texlive-sanskrit-t1
Requires:       texlive-thaienum
Requires:       texlive-thaispec
Requires:       texlive-tuzuk
Requires:       texlive-unicode-alphabets
Requires:       texlive-velthuis
Requires:       texlive-vntex
Requires:       texlive-wnri
Requires:       texlive-wnri-latex
Requires:       texlive-xetex-devanagari

%description
Support for languages not otherwise listed, including Indic, Thai, Vietnamese,
Hebrew, Indonesian, African languages, and plenty more. The split is made
simply on the basis of the size of the support, to keep both collection sizes
and the number of collections reasonable.


%package -n texlive-akshar
Summary:        Support for syllables in the Devanagari script
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Provides:       tex(akshar.sty) = %{tl_version}

%description -n texlive-akshar
This LaTeX3 package provides macros and interfaces to work with Devanagari
characters and syllables in a more correct way.

%package -n texlive-amsldoc-vn
Summary:        Vietnamese translation of AMSLaTeX documentation
Version:        svn21855
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsldoc-vn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsldoc-vn-doc <= 11:%{version}

%description -n texlive-amsldoc-vn
This is a Vietnamese translation of amsldoc, the users' guide to amsmath.

%package -n texlive-aramaic-serto
Summary:        Fonts and LaTeX for Syriac written in Serto
Version:        svn74548
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(assyr.sty) = %{tl_version}
Provides:       tex(serto.sty) = %{tl_version}
Provides:       tex(syriac.sty) = %{tl_version}

%description -n texlive-aramaic-serto
This package enables (La)TeX users to typeset words or phrases (e-TeX
extensions are needed) in Syriac (Aramaic) using the Serto-alphabet. The
package includes a preprocessor written in Python (>= 1.5.2) in order to deal
with right-to-left typesetting for those who do not want to use elatex and to
choose the correct letter depending on word context (initial/medial/final
form). Detailed documentation and examples are included.

%package -n texlive-babel-azerbaijani
Summary:        Support for Azerbaijani within babel
Version:        svn44197
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(azerbaijani.ldf) = %{tl_version}

%description -n texlive-babel-azerbaijani
This is the babel style for Azerbaijani. This language poses special challenges
because no "traditional" font encoding contains the full character set, and
therefore a mixture must be used (e.g., T2A and T1). This package is compatible
with Unicode engines (LuaTeX, XeTeX), which are very likely the most convenient
way to write Azerbaijani documents.

%package -n texlive-babel-esperanto
Summary:        Babel support for Esperanto
Version:        svn75781
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(esperanto.ldf) = %{tl_version}

%description -n texlive-babel-esperanto
The package provides the language definition file for support of Esperanto in
babel. Some shortcuts are defined, as well as translations to Esperanto of
standard "LaTeX names".

%package -n texlive-babel-georgian
Summary:        Babel support for Georgian
Version:        svn45864
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(georgian.ldf) = %{tl_version}
Provides:       tex(georgian.sty) = %{tl_version}
Provides:       tex(georgiancaps.tex) = %{tl_version}

%description -n texlive-babel-georgian
The package provides support for use of Babel in documents written in Georgian.
The package is adapted for use both under 'traditional' TeX engines, and under
XeTeX and LuaTeX.

%package -n texlive-babel-hebrew
Summary:        Babel support for Hebrew
Version:        svn68016
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(inputenc.sty)
Provides:       tex(hebcal.sty) = %{tl_version}
Provides:       tex(hebrew.ldf) = %{tl_version}
Provides:       tex(hebrew_newcode.sty) = %{tl_version}
Provides:       tex(hebrew_oldcode.sty) = %{tl_version}
Provides:       tex(hebrew_p.sty) = %{tl_version}
Provides:       tex(rlbabel.def) = %{tl_version}

%description -n texlive-babel-hebrew
The package provides the language definition file for support of Hebrew in
babel. Macros to control the use of text direction control of TeX--XeT and
e-TeX are provided (and may be used elsewhere). Some shortcuts are defined, as
well as translations to Hebrew of standard "LaTeX names".

%package -n texlive-babel-indonesian
Summary:        Support for Indonesian within babel
Version:        svn75372
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bahasa.ldf) = %{tl_version}
Provides:       tex(bahasai.ldf) = %{tl_version}
Provides:       tex(indon.ldf) = %{tl_version}
Provides:       tex(indonesian.ldf) = %{tl_version}

%description -n texlive-babel-indonesian
This is the babel style for Indonesian.

%package -n texlive-babel-interlingua
Summary:        Babel support for Interlingua
Version:        svn30276
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(interlingua.ldf) = %{tl_version}

%description -n texlive-babel-interlingua
The package provides the language definition file for support of Interlingua in
babel. Translations to Interlingua of standard "LaTeX names" (no shortcuts are
provided). Interlingua itself is an auxiliary language, built from the common
vocabulary of Spanish/Portuguese, English, Italian and French, with some
normalisation of spelling.

%package -n texlive-babel-malay
Summary:        Support for Malay within babel
Version:        svn43234
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bahasam.ldf) = %{tl_version}
Provides:       tex(malay.ldf) = %{tl_version}
Provides:       tex(melayu.ldf) = %{tl_version}
Provides:       tex(meyalu.ldf) = %{tl_version}

%description -n texlive-babel-malay
This is the babel style for Malay.

%package -n texlive-babel-sorbian
Summary:        Babel support for Upper and Lower Sorbian
Version:        svn60975
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lsorbian.ldf) = %{tl_version}
Provides:       tex(usorbian.ldf) = %{tl_version}

%description -n texlive-babel-sorbian
The package provides language definitions file for support of both Upper and
Lower Sorbian, in babel. Some shortcuts are defined, as well as translations to
the relevant language of standard "LaTeX names".

%package -n texlive-babel-thai
Summary:        Support for Thai within babel
Version:        svn30564
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(lthenc.def) = %{tl_version}
Provides:       tex(thai.ldf) = %{tl_version}
Provides:       tex(tis620.def) = %{tl_version}

%description -n texlive-babel-thai
The package provides support for typesetting Thai text. within the babel
system.

%package -n texlive-babel-vietnamese
Summary:        Babel support for typesetting Vietnamese
Version:        svn39246
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(vietnamese.ldf) = %{tl_version}

%description -n texlive-babel-vietnamese
The package provides the language definition file for support of Vietnamese in
babel.

%package -n texlive-bangla
Summary:        A comprehensive Bangla LaTeX package
Version:        svn76924
License:        LPPL-1.3c AND OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-charissil
Requires:       texlive-doulossil
Requires:       tex(CharisSIL.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(polyglossia.sty)
Provides:       tex(bangla.sty) = %{tl_version}
Provides:       tex(banglamap.tex) = %{tl_version}

%description -n texlive-bangla
This package provides all the necessary LaTeX frontends for the Bangla language
and comes with some fonts of its own.

%package -n texlive-bangtex
Summary:        Writing Bangla and Assamese with LaTeX
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bangfont.tex) = %{tl_version}

%description -n texlive-bangtex
The bundle provides class files for writing Bangla and Assamese with LaTeX, and
Metafont sources for fonts.

%package -n texlive-bengali
Summary:        Support for the Bengali language
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(beng.sty) = %{tl_version}

%description -n texlive-bengali
The package is based on Velthuis' transliteration scheme, with extensions to
deal with the Bengali letters that are not in Devanagari. The package also
supports Assamese.

%package -n texlive-burmese
Summary:        Basic Support for Writing Burmese
Version:        svn25185
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(relsize.sty)
Provides:       tex(birm.sty) = %{tl_version}

%description -n texlive-burmese
This package provides basic support for writing Burmese. The package provides a
preprocessor (written in Perl), an Adobe Type 1 font, and LaTeX macros.

%package -n texlive-cjhebrew
Summary:        Typeset Hebrew with LaTeX
Version:        svn43444
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(luabidi.sty)
Provides:       tex(cjhebrew.sty) = %{tl_version}

%description -n texlive-cjhebrew
The cjhebrew package provides Adobe Type 1 fonts for Hebrew, and LaTeX macros
to support their use. Hebrew text can be vocalised, and a few accents are also
available. The package makes it easy to include Hebrew text in other-language
documents. The package makes use of the e-TeX extensions to TeX, so should be
run using an "e-LaTeX".

%package -n texlive-ctib
Summary:        Tibetan for TeX and LaTeX2e
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(ctib.sty) = %{tl_version}
Provides:       tex(ctib.tex) = %{tl_version}
Provides:       tex(lctenc.def) = %{tl_version}

%description -n texlive-ctib
A package using a modified version of Sirlin's Tibetan font. An advantage of
this Tibetan implementation is that all consonant clusters are formed by TeX
and Metafont. No external preprocessor is needed.

%package -n texlive-culmus
Summary:        Hebrew fonts from the Culmus project
Version:        svn76924
License:        LPPL-1.3c AND GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(culmus.sty) = %{tl_version}

%description -n texlive-culmus
Hebrew fonts from the Culmus Project. Both Type1 and Open/TrueType versions of
the fonts are provided, as well as font definition files. It is recommended to
use these fonts with the NHE8 font encoding, from the hebrew-fonts package.

%package -n texlive-ethiop
Summary:        LaTeX macros and fonts for typesetting Amharic
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(etharab.sty) = %{tl_version}
Provides:       tex(ethiop.ldf) = %{tl_version}
Provides:       tex(ethiop.sty) = %{tl_version}

%description -n texlive-ethiop
Ethiopian language support for the babel package, including a collection of
fonts and TeX macros for typesetting the characters of the languages of
Ethiopia, with Metafont fonts based on EthTeX's. The macros use the Babel
framework.

%package -n texlive-ethiop-t1
Summary:        Type 1 versions of Amharic fonts
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-ethiop-t1
These fonts are drop-in Adobe type 1 replacements for the fonts of the ethiop
package.

%package -n texlive-fc
Summary:        Fonts for African languages
Version:        svn32796
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontenc.sty)
Requires:       tex(newlfont.sty)
Provides:       tex(fclfont.sty) = %{tl_version}
Provides:       tex(fcuse.sty) = %{tl_version}
Provides:       tex(t4enc.def) = %{tl_version}
Provides:       tex(t4phonet.sty) = %{tl_version}

%description -n texlive-fc
The fonts are provided as Metafont source, in the familiar arrangement of lots
of (autogenerated) preamble files and a modest set of glyph specifications. (A
similar arrangement appears in the ec and lh font bundles.)

%package -n texlive-fonts-tlwg
Summary:        Thai fonts for LaTeX from TLWG
Version:        svn60817
License:        GPL-2.0-or-later AND LPPL-1.3c AND Bitstream-Vera
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(fonts-tlwg.sty) = %{tl_version}

%description -n texlive-fonts-tlwg
A collection of free Thai fonts, supplied as FontForge sources, and with LaTeX
.fd files.

%package -n texlive-hebrew-fonts
Summary:        Input encodings, font encodings and font definition files for Hebrew
Version:        svn68038
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(8859-8.def) = %{tl_version}
Provides:       tex(cp1255.def) = %{tl_version}
Provides:       tex(cp862.def) = %{tl_version}
Provides:       tex(he8enc.def) = %{tl_version}
Provides:       tex(hebfont.sty) = %{tl_version}
Provides:       tex(lheenc.def) = %{tl_version}
Provides:       tex(nhe8enc.def) = %{tl_version}
Provides:       tex(si960.def) = %{tl_version}

%description -n texlive-hebrew-fonts
A collection of input encodings, font encodings and font definition files for
the Hebrew language.

%package -n texlive-hindawi-latex-template
Summary:        A LaTeX template for authors of the Hindawi journals
Version:        svn57757
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hindawi-latex-template-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hindawi-latex-template-doc <= 11:%{version}

%description -n texlive-hindawi-latex-template
This package contains a LaTeX template for authors of the Hindawi journals.
Authors can use this template for formatting their research articles for
submissions. The package has been created and is maintained by the Typeset
team.

%package -n texlive-hyphen-afrikaans
Summary:        Afrikaans hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-af.ec.tex) = %{tl_version}
Provides:       tex(hyph-af.tex) = %{tl_version}
Provides:       tex(hyph-quote-af.tex) = %{tl_version}
Provides:       tex(loadhyph-af.tex) = %{tl_version}

%description -n texlive-hyphen-afrikaans
Hyphenation patterns for Afrikaans in T1/EC and UTF-8 encodings. OpenOffice
includes older patterns created by a different author, but the patterns
packaged with TeX are considered superior in quality.

%package -n texlive-hyphen-armenian
Summary:        Armenian hyphenation patterns.
Version:        svn73410
License:        LGPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-hy.tex) = %{tl_version}
Provides:       tex(loadhyph-hy.tex) = %{tl_version}

%description -n texlive-hyphen-armenian
Hyphenation patterns for Armenian for Unicode engines. Auto-generated from a
script included in hyph-utf8.

%package -n texlive-hyphen-coptic
Summary:        Coptic hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(copthyph.tex) = %{tl_version}
Provides:       tex(hyph-cop.tex) = %{tl_version}
Provides:       tex(loadhyph-cop.tex) = %{tl_version}

%description -n texlive-hyphen-coptic
Hyphenation patterns for Coptic in UTF-8 encoding as well as in ASCII-based
encoding for 8-bit engines. The latter can only be used with special Coptic
fonts (like CBcoptic). The patterns are considered experimental.

%package -n texlive-hyphen-esperanto
Summary:        Esperanto hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-eo.il3.tex) = %{tl_version}
Provides:       tex(hyph-eo.tex) = %{tl_version}
Provides:       tex(loadhyph-eo.tex) = %{tl_version}

%description -n texlive-hyphen-esperanto
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8 encodings. Note that
TeX distributions don't ship any suitable fonts in Latin 3 encoding, so unless
you create your own font support or want to use MlTeX, using native Unicode
engines is highly recommended.

%package -n texlive-hyphen-ethiopic
Summary:        Hyphenation patterns for Ethiopic scripts.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-mul-ethi.tex) = %{tl_version}
Provides:       tex(loadhyph-mul-ethi.tex) = %{tl_version}

%description -n texlive-hyphen-ethiopic
Hyphenation patterns for languages written using the Ethiopic script for
Unicode engines. They are not supposed to be linguistically relevant in all
cases and should, for proper typography, be replaced by files tailored to
individual languages.

%package -n texlive-hyphen-georgian
Summary:        Georgian hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ka.t8m.tex) = %{tl_version}
Provides:       tex(hyph-ka.tex) = %{tl_version}
Provides:       tex(loadhyph-ka.tex) = %{tl_version}

%description -n texlive-hyphen-georgian
Hyphenation patterns for Georgian in T8M, T8K and UTF-8 encodings.

%package -n texlive-hyphen-hebrew
Summary:        Hebrew hyphenation patterns.
Version:        svn74032
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-he.tex) = %{tl_version}

%description -n texlive-hyphen-hebrew
Prevents hyphenation in Arabic.

%package -n texlive-hyphen-indic
Summary:        Indic hyphenation patterns.
Version:        svn73410
License:        MIT OR LGPL-3.0-or-later OR GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-as.tex) = %{tl_version}
Provides:       tex(hyph-bn.tex) = %{tl_version}
Provides:       tex(hyph-gu.tex) = %{tl_version}
Provides:       tex(hyph-hi.tex) = %{tl_version}
Provides:       tex(hyph-kn.tex) = %{tl_version}
Provides:       tex(hyph-ml.tex) = %{tl_version}
Provides:       tex(hyph-mr.tex) = %{tl_version}
Provides:       tex(hyph-or.tex) = %{tl_version}
Provides:       tex(hyph-pa.tex) = %{tl_version}
Provides:       tex(hyph-pi.tex) = %{tl_version}
Provides:       tex(hyph-ta.tex) = %{tl_version}
Provides:       tex(hyph-te.tex) = %{tl_version}
Provides:       tex(loadhyph-as.tex) = %{tl_version}
Provides:       tex(loadhyph-bn.tex) = %{tl_version}
Provides:       tex(loadhyph-gu.tex) = %{tl_version}
Provides:       tex(loadhyph-hi.tex) = %{tl_version}
Provides:       tex(loadhyph-kn.tex) = %{tl_version}
Provides:       tex(loadhyph-ml.tex) = %{tl_version}
Provides:       tex(loadhyph-mr.tex) = %{tl_version}
Provides:       tex(loadhyph-or.tex) = %{tl_version}
Provides:       tex(loadhyph-pa.tex) = %{tl_version}
Provides:       tex(loadhyph-pi.tex) = %{tl_version}
Provides:       tex(loadhyph-ta.tex) = %{tl_version}
Provides:       tex(loadhyph-te.tex) = %{tl_version}

%description -n texlive-hyphen-indic
Hyphenation patterns for Assamese, Bengali, Gujarati, Hindi, Kannada,
Malayalam, Marathi, Oriya, Panjabi, Tamil and Telugu for Unicode engines.

%package -n texlive-hyphen-indonesian
Summary:        Indonesian hyphenation patterns.
Version:        svn73410
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-id.tex) = %{tl_version}
Provides:       tex(loadhyph-id.tex) = %{tl_version}

%description -n texlive-hyphen-indonesian
Hyphenation patterns for Indonesian (Bahasa Indonesia) in ASCII encoding. They
are probably also usable for Malay (Bahasa Melayu).

%package -n texlive-hyphen-interlingua
Summary:        Interlingua hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-ia.tex) = %{tl_version}
Provides:       tex(loadhyph-ia.tex) = %{tl_version}

%description -n texlive-hyphen-interlingua
Hyphenation patterns for Interlingua in ASCII encoding.

%package -n texlive-hyphen-sanskrit
Summary:        Sanskrit hyphenation patterns.
Version:        svn73410
License:        LicenseRef-Fedora-UltraPermissive
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-sa.tex) = %{tl_version}
Provides:       tex(loadhyph-sa.tex) = %{tl_version}

%description -n texlive-hyphen-sanskrit
Hyphenation patterns for Sanskrit and Prakrit in transliteration, and in
Devanagari, Bengali, Kannada, Malayalam and Telugu scripts for Unicode engines.

%package -n texlive-hyphen-thai
Summary:        Thai hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-th.lth.tex) = %{tl_version}
Provides:       tex(hyph-th.tex) = %{tl_version}
Provides:       tex(loadhyph-th.tex) = %{tl_version}

%description -n texlive-hyphen-thai
Hyphenation patterns for Thai in LTH and UTF-8 encodings.

%package -n texlive-hyphen-turkmen
Summary:        Turkmen hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-tk.ec.tex) = %{tl_version}
Provides:       tex(hyph-tk.tex) = %{tl_version}
Provides:       tex(loadhyph-tk.tex) = %{tl_version}

%description -n texlive-hyphen-turkmen
Hyphenation patterns for Turkmen in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-vietnamese
Summary:        Vietnamese hyphenation patterns.
Version:        svn74032
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-vi.tex) = %{tl_version}

%description -n texlive-hyphen-vietnamese
Prevents hyphenation in Vietnamese.

%package -n texlive-latex-mr
Summary:        A practical guide to LaTeX and Polyglossia for Marathi and other Indian languages
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-mr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-mr-doc <= 11:%{version}

%description -n texlive-latex-mr
The package provides a short guide to LaTeX and specifically to the polyglossia
package. This document aims to introduce LaTeX and polyglossia for Indian
languages. Though the document often discusses the language Marathi, the
discussion applies to other India languages also, with some minute changes
which are described in Section 1.2. We assume that the user of this document
knows basic (La)TeX or has, at least, tried her hand on it. This document is
not very suitable for first time users.

%package -n texlive-latexbangla
Summary:        Enhanced LaTeX integration for Bangla
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(ucharclasses.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(latexbangla.sty) = %{tl_version}

%description -n texlive-latexbangla
This package simplifies the process of writing Bangla in LaTeX and addresses
most of the associated typesetting issues. Notable features: Automated
transition from Bangla to English and vice versa. Patch for the unproportionate
whitespace issue in popular Bangla fonts. Full support for all the common
commands and environments. Bangla numbering for page, section, chapter,
footnotes etc. (extending polyglossia's support). New theorem, problems,
example, solution and other environments, all of which are in Bangla.

%package -n texlive-latino-sine-flexione
Summary:        LaTeX support for documents written in Peano's Interlingua
Version:        svn69568
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(datetime.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(latino-sine-flexione.sty) = %{tl_version}

%description -n texlive-latino-sine-flexione
Latino sine Flexione (or Interlingua) is a language constructed by Giuseppe
Peano at the beginning of the last century. This simplified Latin is designed
to be an instrument for international cooperation, especially in the academic
sphere. (Note that this "Interlingua" is different from the "Interlingua" that
was created a few decades after Peano's work and which is supported by
babel-interlingua!) This package provides the necessary translations to use the
language within a LaTeX document. It also imports fontenc in order to be able
to use ligatures and quotation marks. Finally, it offers a text in Interlingua
that can be used as a dummy text: Fundamento de intelligentia. This article by
H. Bijlsma was first published in Schola et Vita Anno I (1926).

%package -n texlive-lshort-thai
Summary:        Introduction to LaTeX in Thai
Version:        svn55643
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-thai-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-thai-doc <= 11:%{version}

%description -n texlive-lshort-thai
This is the Thai translation of the Short Introduction to LaTeX2e.

%package -n texlive-lshort-vietnamese
Summary:        Vietnamese version of the LaTeX introduction
Version:        svn55643
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-vietnamese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-vietnamese-doc <= 11:%{version}

%description -n texlive-lshort-vietnamese
Vietnamese version of A Short Introduction to LaTeX2e.

%package -n texlive-ntheorem-vn
Summary:        Vietnamese translation of documentation of ntheorem
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ntheorem-vn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ntheorem-vn-doc <= 11:%{version}

%description -n texlive-ntheorem-vn
This is a translation of the documentation provided with ntheorem.

%package -n texlive-quran-bn
Summary:        Bengali translations to the quran package
Version:        svn74830
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-bn.sty) = %{tl_version}
Provides:       tex(qurantext-bni.translation.def) = %{tl_version}
Provides:       tex(qurantext-bnii.translation.def) = %{tl_version}

%description -n texlive-quran-bn
The package is prepared for typesetting some Bengali translations of the Holy
Quran. It adds two Bengali translations to the quran package.

%package -n texlive-quran-id
Summary:        Indonesian translation extension to the quran package
Version:        svn74874
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-id.sty) = %{tl_version}
Provides:       tex(qurantext-idi.translation.def) = %{tl_version}
Provides:       tex(qurantext-idii.translation.def) = %{tl_version}

%description -n texlive-quran-id
The package is prepared for typesetting some Indonesian translations of the
Holy Quran. It adds two Indonesian translations to the quran package.

%package -n texlive-quran-ur
Summary:        Urdu translations to the quran package
Version:        svn74829
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(biditools.sty)
Requires:       tex(quran.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(quran-ur.sty) = %{tl_version}
Provides:       tex(qurantext-uri.translation.def) = %{tl_version}
Provides:       tex(qurantext-urii.translation.def) = %{tl_version}
Provides:       tex(qurantext-uriii.translation.def) = %{tl_version}
Provides:       tex(qurantext-uriv.translation.def) = %{tl_version}
Provides:       tex(qurantext-urv.translation.def) = %{tl_version}
Provides:       tex(qurantext-urvi.translation.def) = %{tl_version}
Provides:       tex(qurantext-urvii.translation.def) = %{tl_version}
Provides:       tex(qurantext-urviii.translation.def) = %{tl_version}

%description -n texlive-quran-ur
The package is prepared for typesetting some Urdu translations of the Holy
Quran. It adds eight Urdu translations to the quran package.

%package -n texlive-sanskrit
Summary:        Sanskrit support
Version:        svn76869
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(relsize.sty)
Provides:       tex(skt.sty) = %{tl_version}

%description -n texlive-sanskrit
A font and pre-processor suitable for the production of documents written in
Sanskrit. Type 1 versions of the fonts are available.

%package -n texlive-sanskrit-t1
Summary:        Type 1 version of 'skt' fonts for Sanskrit
Version:        svn55475
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-sanskrit-t1
The sanskrit-t1 font package provides Type 1 version of Charles Wikner's skt
font series for the Sanskrit language.

%package -n texlive-thaienum
Summary:        Thai labels in enumerate environments
Version:        svn44140
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Provides:       tex(thaienum.sty) = %{tl_version}

%description -n texlive-thaienum
This LaTeX package provides a command to use Thai numerals or characters as
labels in enumerate environments. Once the package is loaded with
\usepackage{thaienum} you can use labels such as \thainum* or \thaimultialph*
in conjunction with the package enumitem. Concrete examples are given in the
documentation.

%package -n texlive-thaispec
Summary:        Thai Language Typesetting in XeLaTeX
Version:        svn58019
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathspec.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(setspace.sty)
Requires:       tex(ucharclasses.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
Provides:       tex(thaispec.sty) = %{tl_version}

%description -n texlive-thaispec
This package allows you to input Thai characters directly to LaTeX documents
and choose any (system wide) Thai fonts for typesetting in XeLaTeX. It also
tries to appropriately justify paragraphs with no more external tools. Required
packages are fontspec, ucharclasses, polyglossia, setspace, kvoptions, xstring,
and xpatch.

%package -n texlive-tuzuk
Summary:        Turkish bylaws and regulations document class
Version:        svn74620
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-tuzuk
The tuzuk class provides a standardized format for writing bylaws and
regulations in Turkish-governmental style. It includes features for creating
numbered articles, subsections, and signature areas commonly found in legal
documents. Features: Easy creation of numbered articles with the \madde
command, Section titles with \bolumadi, Automatic lettered lists with the fikra
environment, Built-in signature area formatting with \imzalar, Full Turkish
language support. Built originally for creating the regulation for Ozgur
Yazilim Dernegi (The Free Software Association in Turkey), https://oyd.org.tr/.
Explanation of the package name: "tuzuk" in Turkish means "regulations", as a
document. For example, GDPR, which stands for "General Data Protection
Regulation", translates as "Genel Veri Koruma Tuzugu". In Turkish law, the
non-profit associations have a "tuzuk" as their constitution-like governing
document.

%package -n texlive-unicode-alphabets
Summary:        Macros for using characters from Unicode's Private Use Area
Version:        svn66225
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(csvsimple.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(xparse.sty)
Provides:       tex(unicode-alphabets.sty) = %{tl_version}

%description -n texlive-unicode-alphabets
While Unicode supports the vast majority of use cases, there are certain
specialized niches which require characters and glyphs not (yet) represented in
the standard. Thus the Private Use Area (PUA) at code points E000-F8FF, which
enables third parties to define arbitrary character sets. This package allows
configuring a number of macros for using various PUA character sets in LaTeX
(AGL, CYFI, MUFI, SIL, TITUS, UCSUR, UNZ), to enable transcription and display
of medieval and other documents.

%package -n texlive-vntex
Summary:        Support for Vietnamese
Version:        svn62837
License:        GPL-1.0-or-later AND LGPL-2.1-or-later AND LPPL-1.3c AND LicenseRef-Utopia
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(cmap.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(ucs.sty)
Provides:       tex(dblaccnt.sty) = %{tl_version}
Provides:       tex(dblaccnt.tex) = %{tl_version}
Provides:       tex(mcviscii.def) = %{tl_version}
Provides:       tex(pd1supp.def) = %{tl_version}
Provides:       tex(swpvntex.sty) = %{tl_version}
Provides:       tex(t5code.tex) = %{tl_version}
Provides:       tex(t5enc.def) = %{tl_version}
Provides:       tex(tcvn.def) = %{tl_version}
Provides:       tex(varioref-vi.sty) = %{tl_version}
Provides:       tex(vietnam.sty) = %{tl_version}
Provides:       tex(viscii.def) = %{tl_version}
Provides:       tex(vncaps.tex) = %{tl_version}
Provides:       tex(vntex.sty) = %{tl_version}
Provides:       tex(vntexinfo.tex) = %{tl_version}
Provides:       tex(vps.def) = %{tl_version}

%description -n texlive-vntex
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX macros for
typesetting documents in Vietnamese. Users of the fonts (in both Metafont and
Adobe Type 1 format) of this bundle may alternatively use the lm fonts bundle,
for which map files are available to provide a Vietnamese version.

%package -n texlive-wnri
Summary:        Ridgeway's fonts
Version:        svn22459
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-wnri
Fonts (as Metafont source) for Old English, Indic languages in Roman
transliteration and Puget Salish (Lushootseed) and other Native American
languages.

%package -n texlive-wnri-latex
Summary:        LaTeX support for wnri fonts
Version:        svn22338
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(wnri.def) = %{tl_version}
Provides:       tex(wnri.sty) = %{tl_version}

%description -n texlive-wnri-latex
LaTeX support for the wnri fonts.

%package -n texlive-xetex-devanagari
Summary:        XeTeX input map for Unicode Devanagari
Version:        svn34296
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-xetex-devanagari
The package provides a map for use with Jonathan Kew's TECkit, to translate
Devanagari (encoded according to the Harvard/Kyoto convention) to Unicode
(range 0900-097F).

%post -n texlive-hyphen-afrikaans
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/afrikaans.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "afrikaans loadhyph-af.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{afrikaans}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{afrikaans}{loadhyph-af.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-afrikaans
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/afrikaans.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{afrikaans}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-armenian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/armenian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "armenian loadhyph-hy.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{armenian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{armenian}{loadhyph-hy.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-armenian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/armenian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{armenian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-coptic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/coptic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "coptic loadhyph-cop.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{coptic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{coptic}{loadhyph-cop.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-coptic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/coptic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{coptic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-esperanto
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/esperanto.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "esperanto loadhyph-eo.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{esperanto}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{esperanto}{loadhyph-eo.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-esperanto
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/esperanto.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{esperanto}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-ethiopic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/ethiopic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "ethiopic loadhyph-mul-ethi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=amharic.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=amharic" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=geez.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=geez" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{ethiopic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{amharic}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{geez}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ethiopic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/ethiopic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=amharic.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=geez.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{ethiopic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{amharic}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{geez}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-georgian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/georgian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "georgian loadhyph-ka.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{georgian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{georgian}{loadhyph-ka.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-georgian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/georgian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{georgian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-hebrew
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/hebrew.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "hebrew hyph-he.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{hebrew}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{hebrew}{hyph-he.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-hebrew
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/hebrew.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{hebrew}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-indic
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/assamese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "assamese loadhyph-as.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{assamese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/bengali.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "bengali loadhyph-bn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{bengali}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/gujarati.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "gujarati loadhyph-gu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{gujarati}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/hindi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "hindi loadhyph-hi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{hindi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/kannada.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "kannada loadhyph-kn.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{kannada}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/malayalam.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "malayalam loadhyph-ml.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{malayalam}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/marathi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "marathi loadhyph-mr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{marathi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/oriya.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "oriya loadhyph-or.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{oriya}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/pali.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "pali loadhyph-pi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{pali}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{pali}{loadhyph-pi.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/panjabi.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "panjabi loadhyph-pa.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{panjabi}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/tamil.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "tamil loadhyph-ta.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{tamil}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/telugu.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "telugu loadhyph-te.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{telugu}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-indic
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/assamese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{assamese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/bengali.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{bengali}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/gujarati.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{gujarati}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/hindi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{hindi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/kannada.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{kannada}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/malayalam.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{malayalam}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/marathi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{marathi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/oriya.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{oriya}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/pali.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{pali}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/panjabi.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{panjabi}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/tamil.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{tamil}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/telugu.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{telugu}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-indonesian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/indonesian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "indonesian loadhyph-id.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{indonesian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{indonesian}{loadhyph-id.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-indonesian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/indonesian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{indonesian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-interlingua
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/interlingua.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "interlingua loadhyph-ia.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{interlingua}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{interlingua}{loadhyph-ia.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-interlingua
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/interlingua.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{interlingua}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-sanskrit
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/sanskrit.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "sanskrit loadhyph-sa.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{sanskrit}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{sanskrit}{loadhyph-sa.tex}{}{1}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-sanskrit
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/sanskrit.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{sanskrit}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-thai
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/thai.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "thai loadhyph-th.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{thai}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{thai}{loadhyph-th.tex}{}{2}{3}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-thai
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/thai.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{thai}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-turkmen
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/turkmen.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "turkmen loadhyph-tk.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{turkmen}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{turkmen}{loadhyph-tk.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-turkmen
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/turkmen.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{turkmen}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-vietnamese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/vietnamese.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "vietnamese hyph-vi.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{vietnamese}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{vietnamese}{hyph-vi.tex}{}{0}{0}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-vietnamese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/vietnamese.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{vietnamese}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-akshar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/akshar/
%doc %{_texmf_main}/doc/latex/akshar/

%files -n texlive-amsldoc-vn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsldoc-vn/

%files -n texlive-aramaic-serto
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/aramaic-serto/
%{_texmf_main}/fonts/map/dvips/aramaic-serto/
%{_texmf_main}/fonts/source/public/aramaic-serto/
%{_texmf_main}/fonts/tfm/public/aramaic-serto/
%{_texmf_main}/fonts/type1/public/aramaic-serto/
%{_texmf_main}/tex/latex/aramaic-serto/
%doc %{_texmf_main}/doc/latex/aramaic-serto/

%files -n texlive-babel-azerbaijani
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-azerbaijani/
%doc %{_texmf_main}/doc/generic/babel-azerbaijani/

%files -n texlive-babel-esperanto
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-esperanto/
%doc %{_texmf_main}/doc/generic/babel-esperanto/

%files -n texlive-babel-georgian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-georgian/
%doc %{_texmf_main}/doc/generic/babel-georgian/

%files -n texlive-babel-hebrew
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-hebrew/
%doc %{_texmf_main}/doc/generic/babel-hebrew/

%files -n texlive-babel-indonesian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-indonesian/
%doc %{_texmf_main}/doc/generic/babel-indonesian/

%files -n texlive-babel-interlingua
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-interlingua/
%doc %{_texmf_main}/doc/generic/babel-interlingua/

%files -n texlive-babel-malay
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-malay/
%doc %{_texmf_main}/doc/generic/babel-malay/

%files -n texlive-babel-sorbian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-sorbian/
%doc %{_texmf_main}/doc/generic/babel-sorbian/

%files -n texlive-babel-thai
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-thai/
%doc %{_texmf_main}/doc/generic/babel-thai/

%files -n texlive-babel-vietnamese
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-vietnamese/
%doc %{_texmf_main}/doc/generic/babel-vietnamese/

%files -n texlive-bangla
%license lppl1.3c.txt
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/bangla/
%{_texmf_main}/tex/latex/bangla/
%doc %{_texmf_main}/doc/latex/bangla/

%files -n texlive-bangtex
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/bangtex/
%{_texmf_main}/fonts/tfm/public/bangtex/
%{_texmf_main}/tex/latex/bangtex/
%doc %{_texmf_main}/doc/latex/bangtex/

%files -n texlive-bengali
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/bengali/
%{_texmf_main}/fonts/tfm/public/bengali/
%{_texmf_main}/tex/latex/bengali/
%doc %{_texmf_main}/doc/fonts/bengali/

%files -n texlive-burmese
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/burmese/
%{_texmf_main}/fonts/tfm/public/burmese/
%{_texmf_main}/fonts/type1/public/burmese/
%{_texmf_main}/tex/latex/burmese/
%doc %{_texmf_main}/doc/fonts/burmese/

%files -n texlive-cjhebrew
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/cjhebrew/
%{_texmf_main}/fonts/enc/dvips/cjhebrew/
%{_texmf_main}/fonts/map/dvips/cjhebrew/
%{_texmf_main}/fonts/tfm/public/cjhebrew/
%{_texmf_main}/fonts/type1/public/cjhebrew/
%{_texmf_main}/fonts/vf/public/cjhebrew/
%{_texmf_main}/tex/latex/cjhebrew/
%doc %{_texmf_main}/doc/latex/cjhebrew/

%files -n texlive-ctib
%license gpl2.txt
%{_texmf_main}/fonts/source/public/ctib/
%{_texmf_main}/fonts/tfm/public/ctib/
%{_texmf_main}/tex/latex/ctib/
%doc %{_texmf_main}/doc/latex/ctib/

%files -n texlive-culmus
%license lppl1.3c.txt
%license gpl2.txt
%{_texmf_main}/fonts/afm/public/culmus/
%{_texmf_main}/fonts/enc/dvips/culmus/
%{_texmf_main}/fonts/map/dvips/culmus/
%{_texmf_main}/fonts/opentype/public/culmus/
%{_texmf_main}/fonts/tfm/public/culmus/
%{_texmf_main}/fonts/truetype/public/culmus/
%{_texmf_main}/fonts/type1/public/culmus/
%{_texmf_main}/fonts/type3/culmus/
%{_texmf_main}/fonts/vf/public/culmus/
%{_texmf_main}/tex/latex/culmus/
%doc %{_texmf_main}/doc/fonts/culmus/

%files -n texlive-ethiop
%license gpl2.txt
%{_texmf_main}/fonts/ofm/public/ethiop/
%{_texmf_main}/fonts/ovf/public/ethiop/
%{_texmf_main}/fonts/ovp/public/ethiop/
%{_texmf_main}/fonts/source/public/ethiop/
%{_texmf_main}/fonts/tfm/public/ethiop/
%{_texmf_main}/omega/ocp/ethiop/
%{_texmf_main}/omega/otp/ethiop/
%{_texmf_main}/tex/latex/ethiop/
%doc %{_texmf_main}/doc/latex/ethiop/

%files -n texlive-ethiop-t1
%license gpl2.txt
%{_texmf_main}/fonts/map/dvips/ethiop-t1/
%{_texmf_main}/fonts/type1/public/ethiop-t1/
%doc %{_texmf_main}/doc/latex/ethiop-t1/

%files -n texlive-fc
%license gpl2.txt
%{_texmf_main}/fonts/source/jknappen/fc/
%{_texmf_main}/fonts/tfm/jknappen/fc/
%{_texmf_main}/tex/latex/fc/
%doc %{_texmf_main}/doc/fonts/fc/

%files -n texlive-fonts-tlwg
%license gpl2.txt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/fonts-tlwg/
%{_texmf_main}/fonts/enc/dvips/fonts-tlwg/
%{_texmf_main}/fonts/map/dvips/fonts-tlwg/
%{_texmf_main}/fonts/opentype/public/fonts-tlwg/
%{_texmf_main}/fonts/tfm/public/fonts-tlwg/
%{_texmf_main}/fonts/type1/public/fonts-tlwg/
%{_texmf_main}/fonts/vf/public/fonts-tlwg/
%{_texmf_main}/tex/latex/fonts-tlwg/
%doc %{_texmf_main}/doc/fonts/fonts-tlwg/

%files -n texlive-hebrew-fonts
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/hebrew-fonts/
%doc %{_texmf_main}/doc/latex/hebrew-fonts/

%files -n texlive-hindawi-latex-template
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/hindawi-latex-template/

%files -n texlive-hyphen-afrikaans
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-armenian
%license lgpl.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-coptic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-esperanto
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-ethiopic
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-georgian
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-hebrew
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-indic
%license mit.txt
%license lgpl.txt
%license gpl3.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-indonesian
%license gpl2.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-interlingua
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-sanskrit
%{_texmf_main}/tex/generic/hyph-utf8/
%doc %{_texmf_main}/doc/generic/hyph-utf8/

%files -n texlive-hyphen-thai
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-turkmen
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-vietnamese
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-latex-mr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/latex-mr/

%files -n texlive-latexbangla
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/latexbangla/
%doc %{_texmf_main}/doc/latex/latexbangla/

%files -n texlive-latino-sine-flexione
%license pd.txt
%{_texmf_main}/tex/latex/latino-sine-flexione/
%doc %{_texmf_main}/doc/latex/latino-sine-flexione/

%files -n texlive-lshort-thai
%license pd.txt
%doc %{_texmf_main}/doc/latex/lshort-thai/

%files -n texlive-lshort-vietnamese
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/lshort-vietnamese/

%files -n texlive-ntheorem-vn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/ntheorem-vn/

%files -n texlive-quran-bn
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quran-bn/
%doc %{_texmf_main}/doc/latex/quran-bn/

%files -n texlive-quran-id
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/quran-id/
%doc %{_texmf_main}/doc/xelatex/quran-id/

%files -n texlive-quran-ur
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/quran-ur/
%doc %{_texmf_main}/doc/latex/quran-ur/

%files -n texlive-sanskrit
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/sanskrit/
%{_texmf_main}/fonts/tfm/public/sanskrit/
%{_texmf_main}/tex/latex/sanskrit/
%doc %{_texmf_main}/doc/latex/sanskrit/

%files -n texlive-sanskrit-t1
%license lppl1.3c.txt
%{_texmf_main}/fonts/map/dvips/sanskrit-t1/
%{_texmf_main}/fonts/type1/public/sanskrit-t1/
%doc %{_texmf_main}/doc/fonts/sanskrit-t1/

%files -n texlive-thaienum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thaienum/
%doc %{_texmf_main}/doc/latex/thaienum/

%files -n texlive-thaispec
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/thaispec/
%doc %{_texmf_main}/doc/latex/thaispec/

%files -n texlive-tuzuk
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tuzuk/
%doc %{_texmf_main}/doc/latex/tuzuk/

%files -n texlive-unicode-alphabets
%license cc-by-sa-4.txt
%{_texmf_main}/tex/latex/unicode-alphabets/
%doc %{_texmf_main}/doc/latex/unicode-alphabets/

%files -n texlive-vntex
%license gpl.txt
%license lgpl2.1.txt
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/vntex/chartervn/
%{_texmf_main}/fonts/afm/vntex/grotesqvn/
%{_texmf_main}/fonts/afm/vntex/urwvn/
%{_texmf_main}/fonts/afm/vntex/vntopia/
%{_texmf_main}/fonts/enc/dvips/vntex/
%{_texmf_main}/fonts/enc/pdftex/vntex/
%{_texmf_main}/fonts/map/dvips/vntex/
%{_texmf_main}/fonts/source/vntex/vnr/
%{_texmf_main}/fonts/tfm/vntex/arevvn/
%{_texmf_main}/fonts/tfm/vntex/chartervn/
%{_texmf_main}/fonts/tfm/vntex/cmbrightvn/
%{_texmf_main}/fonts/tfm/vntex/concretevn/
%{_texmf_main}/fonts/tfm/vntex/grotesqvn/
%{_texmf_main}/fonts/tfm/vntex/txttvn/
%{_texmf_main}/fonts/tfm/vntex/urwvn/
%{_texmf_main}/fonts/tfm/vntex/vnr/
%{_texmf_main}/fonts/tfm/vntex/vntopia/
%{_texmf_main}/fonts/type1/vntex/arevvn/
%{_texmf_main}/fonts/type1/vntex/chartervn/
%{_texmf_main}/fonts/type1/vntex/cmbrightvn/
%{_texmf_main}/fonts/type1/vntex/concretevn/
%{_texmf_main}/fonts/type1/vntex/grotesqvn/
%{_texmf_main}/fonts/type1/vntex/txttvn/
%{_texmf_main}/fonts/type1/vntex/urwvn/
%{_texmf_main}/fonts/type1/vntex/vnr/
%{_texmf_main}/fonts/type1/vntex/vntopia/
%{_texmf_main}/fonts/vf/vntex/chartervn/
%{_texmf_main}/fonts/vf/vntex/urwvn/
%{_texmf_main}/fonts/vf/vntex/vntopia/
%{_texmf_main}/tex/latex/vntex/
%{_texmf_main}/tex/plain/vntex/
%doc %{_texmf_main}/doc/generic/vntex/

%files -n texlive-wnri
%license gpl2.txt
%{_texmf_main}/fonts/source/public/wnri/
%{_texmf_main}/fonts/tfm/public/wnri/
%doc %{_texmf_main}/doc/fonts/wnri/

%files -n texlive-wnri-latex
%license gpl2.txt
%{_texmf_main}/tex/latex/wnri-latex/
%doc %{_texmf_main}/doc/latex/wnri-latex/

%files -n texlive-xetex-devanagari
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%doc %{_texmf_main}/doc/xetex/xetex-devanagari/

%changelog
* Thu Jan 29 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn74620-3
- fix licensing, descriptions, update components

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74620-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn74620-1
- Update to TeX Live 2025
