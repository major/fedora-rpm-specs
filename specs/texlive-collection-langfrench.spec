%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langfrench
Epoch:          12
Version:        svn72499
Release:        3%{?dist}
Summary:        French

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langfrench.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aeguill.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aeguill.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/annee-scolaire.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/annee-scolaire.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apprendre-a-programmer-en-tex.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apprendre-a-programmer-en-tex.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apprends-latex.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/apprends-latex.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-basque.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-basque.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-french.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/babel-french.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/basque-book.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/basque-book.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/basque-date.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/basque-date.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bib-fr.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bib-fr.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-french.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibleref-french.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/booktabs-fr.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/booktabs-fr.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cahierprof.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cahierprof.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/couleurs-fr.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/couleurs-fr.doc.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/droit-fr.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/droit-fr.doc.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/e-french.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/e-french.doc.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epslatex-fr.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epslatex-fr.doc.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expose-expl3-dunkerque-2019.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/expose-expl3-dunkerque-2019.doc.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/facture.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/facture.doc.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/faq-fr.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/faq-fr.doc.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/faq-fr-gutenberg.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/faq-fr-gutenberg.doc.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/formation-latex-ul.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/formation-latex-ul.doc.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frenchmath.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frenchmath.doc.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frletter.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frletter.doc.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frpseudocode.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/frpseudocode.doc.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-basque.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-french.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient-fr.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient-fr.doc.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impnattypo.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impnattypo.doc.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-french.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l2tabu-french.doc.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo-fr.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2e-help-texinfo-fr.doc.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letgut.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/letgut.doc.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-french.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-french.doc.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mafr.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mafr.doc.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matapli.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/matapli.doc.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/panneauxroute.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/panneauxroute.doc.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/profcollege.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/profcollege.doc.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proflabo.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proflabo.doc.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proflycee.tar.xz
Source75:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/proflycee.doc.tar.xz
Source76:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/profsio.tar.xz
Source77:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/profsio.doc.tar.xz
Source78:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabvar.tar.xz
Source79:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tabvar.doc.tar.xz
Source80:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tdsfrmath.tar.xz
Source81:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tdsfrmath.doc.tar.xz
Source82:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-fr.tar.xz
Source83:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-fr.doc.tar.xz
Source84:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-array-fr.tar.xz
Source85:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-array-fr.doc.tar.xz
Source86:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-dcolumn-fr.tar.xz
Source87:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-dcolumn-fr.doc.tar.xz
Source88:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-natbib-fr.tar.xz
Source89:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-natbib-fr.doc.tar.xz
Source90:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-tabbing-fr.tar.xz
Source91:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/translation-tabbing-fr.doc.tar.xz
Source92:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/variations.tar.xz
Source93:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/variations.doc.tar.xz
Source94:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualfaq-fr.tar.xz
Source95:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualfaq-fr.doc.tar.xz
Source96:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualtikz.tar.xz
Source97:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/visualtikz.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-aeguill
Requires:       texlive-annee-scolaire
Requires:       texlive-apprendre-a-programmer-en-tex
Requires:       texlive-apprends-latex
Requires:       texlive-babel-basque
Requires:       texlive-babel-french
Requires:       texlive-basque-book
Requires:       texlive-basque-date
Requires:       texlive-bib-fr
Requires:       texlive-bibleref-french
Requires:       texlive-booktabs-fr
Requires:       texlive-cahierprof
Requires:       texlive-collection-basic
Requires:       texlive-couleurs-fr
Requires:       texlive-droit-fr
Requires:       texlive-e-french
Requires:       texlive-epslatex-fr
Requires:       texlive-expose-expl3-dunkerque-2019
Requires:       texlive-facture
Requires:       texlive-faq-fr
Requires:       texlive-faq-fr-gutenberg
Requires:       texlive-formation-latex-ul
Requires:       texlive-frenchmath
Requires:       texlive-frletter
Requires:       texlive-frpseudocode
Requires:       texlive-hyphen-basque
Requires:       texlive-hyphen-french
Requires:       texlive-impatient-fr
Requires:       texlive-impnattypo
Requires:       texlive-l2tabu-french
Requires:       texlive-latex2e-help-texinfo-fr
Requires:       texlive-letgut
Requires:       texlive-lshort-french
Requires:       texlive-mafr
Requires:       texlive-matapli
Requires:       texlive-panneauxroute
Requires:       texlive-profcollege
Requires:       texlive-proflabo
Requires:       texlive-proflycee
Requires:       texlive-profsio
Requires:       texlive-tabvar
Requires:       texlive-tdsfrmath
Requires:       texlive-texlive-fr
Requires:       texlive-translation-array-fr
Requires:       texlive-translation-dcolumn-fr
Requires:       texlive-translation-natbib-fr
Requires:       texlive-translation-tabbing-fr
Requires:       texlive-variations
Requires:       texlive-visualfaq-fr
Requires:       texlive-visualtikz

%description
Support for French and Basque.


%package -n texlive-aeguill
Summary:        Add several kinds of guillemets to the ae fonts
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ae.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(latexsym.sty)
Provides:       tex(aeguill.sty) = %{tl_version}

%description -n texlive-aeguill
The package enables the user to add guillemets from several source (Polish cmr,
Cyrillic cmr, lasy and ec) to the ae fonts. This was useful when the ae fonts
were used to produce PDF files, since the additional guillemets exist in fonts
available in Adobe Type 1 format.

%package -n texlive-annee-scolaire
Summary:        Automatically typeset the academic year (French way)
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(annee-scolaire.sty) = %{tl_version}

%description -n texlive-annee-scolaire
This package provides a macro \anneescolaire to automatically write the
academic year in the French way, according to the date of compilation, two
other macros to obtain the first and the second calendar year of the academic
year, a macro to be redefined to change the presentation of the years.

%package -n texlive-apprendre-a-programmer-en-tex
Summary:        The book "Apprendre a programmer en TeX"
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-apprendre-a-programmer-en-tex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-apprendre-a-programmer-en-tex-doc <= 11:%{version}

%description -n texlive-apprendre-a-programmer-en-tex
This book explains the basic concepts required for programming in TeX and
explains the programming methods, providing many examples. The package makes
the compilable source code as well as the compiled pdf file accessible to
everyone. Ce livre expose les concepts de base requis pour programmer en TeX et
decrit les methodes de programmation en s'appuyant sur de nombreux exemples. Ce
package met a disposition de tous le code source compilable ainsi que le
fichier pdf du livre.

%package -n texlive-apprends-latex
Summary:        Apprends LaTeX!
Version:        svn19306
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-apprends-latex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-apprends-latex-doc <= 11:%{version}

%description -n texlive-apprends-latex
Apprends LaTeX! ("Learn LaTeX", in English) is French documentation for LaTeX
beginners.

%package -n texlive-babel-basque
Summary:        Babel contributed support for Basque
Version:        svn30256
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(basque.ldf) = %{tl_version}

%description -n texlive-babel-basque
The package establishes Basque conventions in a document.

%package -n texlive-babel-french
Summary:        Babel contributed support for French
Version:        svn76067
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(acadian.ldf) = %{tl_version}
Provides:       tex(canadien.ldf) = %{tl_version}
Provides:       tex(francais.ldf) = %{tl_version}
Provides:       tex(french.ldf) = %{tl_version}
Provides:       tex(french3.ldf) = %{tl_version}
Provides:       tex(frenchb.ldf) = %{tl_version}

%description -n texlive-babel-french
The package, formerly known as frenchb, establishes French conventions in a
document (or a subset of the conventions, if French is not the main language of
the document).

%package -n texlive-basque-book
Summary:        Class for book-type documents written in Basque
Version:        svn32924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-basque-book
The class is derived from the LaTeX book class. The extensions solve
grammatical and numeration issues that occur when book-type documents are
written in Basque. The class is useful for writing books, PhD and Master
Theses, etc., in Basque.

%package -n texlive-basque-date
Summary:        Print the date in Basque
Version:        svn26477
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(basque-date.sty) = %{tl_version}

%description -n texlive-basque-date
The package provides two LaTeX commands to print the current date in Basque
according to the correct forms ruled by The Basque Language Academy
(Euskaltzaindia). The commands automatically solve the complex declination
issues of numbers in Basque.

%package -n texlive-bib-fr
Summary:        French translation of classical BibTeX styles
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-bib-fr
These files are French translations of the classical BibTeX style files. The
translations can easily be modified by simply redefining FUNCTIONs named fr.*,
at the beginning (lines 50-150) of each file.

%package -n texlive-bibleref-french
Summary:        French translations for bibleref
Version:        svn75246
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
Provides:       tex(bibleref-french.sty) = %{tl_version}

%description -n texlive-bibleref-french
The package provides translations and alternative typesetting conventions for
use of bibleref in French.

%package -n texlive-booktabs-fr
Summary:        French translation of booktabs documentation
Version:        svn21948
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-booktabs-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-booktabs-fr-doc <= 11:%{version}

%description -n texlive-booktabs-fr
The translation comes from a collection provided by Benjamin Bayart.

%package -n texlive-cahierprof
Summary:        Schedule and grade books for French teachers
Version:        svn76102
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(microtype.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xstring.sty)
Provides:       tex(cahierprof.sty) = %{tl_version}

%description -n texlive-cahierprof
This package provide tools to help teachers in France to produce weekly
schedules and grade books.

%package -n texlive-couleurs-fr
Summary:        French version of colour definitions from xcolor
Version:        svn76790
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xcolor.sty)
Provides:       tex(couleurs-fr.sty) = %{tl_version}

%description -n texlive-couleurs-fr
This package provides colours with French names, based on xcolor (svgnames,
dvipsnames) and xkcd.

%package -n texlive-droit-fr
Summary:        Document class and bibliographic style for French law
Version:        svn39802
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Provides:       tex(droit-fr.bbx) = %{tl_version}
Provides:       tex(droit-fr.cbx) = %{tl_version}

%description -n texlive-droit-fr
The bundle provides a toolkit intended for students writing a thesis in French
law. It features: a LaTeX document class; a bibliographic style for BibLaTeX
package; a practical example of french thesis document; and documentation. The
class assumes use of biber and BibLaTeX.

%package -n texlive-e-french
Summary:        Comprehensive LaTeX support for French-language typesetting
Version:        svn52027
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(german.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(msg.sty)
Requires:       tex(ngerman.sty)
Provides:       tex(efrench.sty) = %{tl_version}
Provides:       tex(efrenchu.tex) = %{tl_version}
Provides:       tex(epreuve.sty) = %{tl_version}
Provides:       tex(fenglish.sty) = %{tl_version}
Provides:       tex(frabbrev-u8.tex) = %{tl_version}
Provides:       tex(frabbrev.tex) = %{tl_version}
Provides:       tex(french-msg.tex) = %{tl_version}
Provides:       tex(french.sty) = %{tl_version}
Provides:       tex(french_french-msg.tex) = %{tl_version}
Provides:       tex(frenchle.sty) = %{tl_version}
Provides:       tex(frenchpro.sty) = %{tl_version}
Provides:       tex(frhyphex.tex) = %{tl_version}
Provides:       tex(fxabbrev.tex) = %{tl_version}
Provides:       tex(german_french-msg.tex) = %{tl_version}
Provides:       tex(mlp-01.sty) = %{tl_version}
Provides:       tex(mlp-33.sty) = %{tl_version}
Provides:       tex(mlp-49.sty) = %{tl_version}
Provides:       tex(mlp-49n.sty) = %{tl_version}
Provides:       tex(mlp-opts.sty) = %{tl_version}
Provides:       tex(mlp.sty) = %{tl_version}
Provides:       tex(pmfrench.sty) = %{tl_version}

%description -n texlive-e-french
E-french is a distribution that keeps alive the work of Bernard Gaulle (now
deceased), under a free licence. It replaces the old "full" frenchpro (the
"professional" distribution) and the light-weight frenchle packages.

%package -n texlive-epslatex-fr
Summary:        French version of "graphics in LaTeX"
Version:        svn19440
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-epslatex-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-epslatex-fr-doc <= 11:%{version}

%description -n texlive-epslatex-fr
This is the French translation of epslatex, and describes how to use imported
graphics in LaTeX(2e) documents.

%package -n texlive-expose-expl3-dunkerque-2019
Summary:        Using expl3 to implement some numerical algorithms
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-expose-expl3-dunkerque-2019-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-expose-expl3-dunkerque-2019-doc <= 11:%{version}

%description -n texlive-expose-expl3-dunkerque-2019
An article, in French, based on a presentation made in Dunkerque for the "stage
LaTeX" on 12 June 2019. The articles gives three examples of code in expl3 with
(lots of) comments: Knuth's algorithm to create a list of primes, the sieve of
Eratosthenes, Kaprekar sequences. The package contains the code itself, the
documentation as a PDF file, and all the files needed to produce it.

%package -n texlive-facture
Summary:        Generate an invoice
Version:        svn67538
License:        CC-BY-SA-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-facture
Une classe simple permettant de produire une facture, avec ou sans TVA, avec
gestion d'une adresse differente pour la livraison et pour la facturation. A
simple class that allows production of an invoice, with or without VAT;
different addresses for delivery and for billing are permitted.

%package -n texlive-faq-fr
Summary:        French LaTeX FAQ (sources)
Version:        svn71182
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-faq-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-faq-fr-doc <= 11:%{version}

%description -n texlive-faq-fr
(English version below) Ce package contient les sources de la faq LaTeX
francophone, actuellement maintenue a jour sur un wiki ouvert a tous:
https://www.latex-fr.net/ Si vous souhaitez lire la FAQ, nous vous conseillons
de consulter URL ci-dessus. Vous pourrez egalement vous ouvrir un compte sur le
wiki pour participer au projet (en francais). Toutes les contributions sont les
bienvenues. Ce package est essentiellement mis a disposition sur le CTAN pour
encourager la reutilisation de ce contenu, et pour en conserver une copie
perenne. Le fichier "REUSE" contient les informations techniques pour la
reutilisation. English version: This package contains the source files of the
French-speaking FAQ, now hosted on an open wiki: https://www.latex-fr.net/ If
you just want to read the FAQ, please visit the URL above. You're also welcome
if you want to contribute to this resource (in French): just request an
account, it's open to everyone. This package is on CTAN mostly to encourage
reuse, and for archival purposes. Read the "REUSE" file to get technical data
about reusing the contents.

%package -n texlive-faq-fr-gutenberg
Summary:        Sources of the GUTenberg French LaTeX FAQ and PDF files
Version:        svn75712
License:        CC-BY-SA-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-faq-fr-gutenberg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-faq-fr-gutenberg-doc <= 11:%{version}

%description -n texlive-faq-fr-gutenberg
# French-speaking GUTenberg LaTeX FAQ -- Frequently Asked Questions (French
version below) This package contains the sources of the GUTenberg French LaTeX
FAQ (French (La)TeX users group), currently maintained as an Git repository
open to all: https://gitlab.gutenberg-asso.fr If you'd like to read the FAQ,
please visit the URL above. This package also contains two PDF versions of this
FAQ: faqlatexgutenberg.pdf with code verbatim in clear mode
faqlatexgutenberg-sombre.pdf with code verbatim in dark mode ## Participate You
can also open an account on the association's Gitlab forge:
https://gitlab.gutenberg-asso.fr and ask to join the repository
https://gitlab.gutenberg-asso.fr/gutenberg/faq-gut All contributions are
welcome: corrections of small errors, updating answers to questions, or adding
new questions! These files are made available on CTAN only to encourage reuse
of this content, and to preserve a permanent copy. ## Contact us For questions
and comments: faq@gutenberg-asso.fr ## Version 2024-10-07 # FAQ LaTeX
francophone GUTenberg -- Foire aux Questions Ce package contient les sources de
la FAQ LaTeX francophone GUTenberg (groupe des utilisateurs francophones de
(La)TeX), actuellement maintenue a jour sous forme d'un depot Git ouvert a
tous: https://gitlab.gutenberg-asso.fr Si vous souhaitez lire la FAQ, nous vous
conseillons de consulter l'URL ci-dessus. Ce package contient aussi deux
versions PDF de cette FAQ: faqlatexgutenberg.pdf avec verbatim des codes en
mode clair faqlatexgutenberg-sombre.pdf avec verbatim des codes en mode sombre
## Participer Vous pouvez egalement ouvrir un compte sur la forge Gitlab de
l'association GUTenberg: https://gitlab.gutenberg-asso.fr et demander a
rejoindre le depot: https://gitlab.gutenberg-asso.fr/gutenberg/faq-gut Toutes
les contributions sont les bienvenues: corrections des petites erreurs, mises a
jour des reponses aux questions, ou ajout de nouvelles questions ! Ces fichiers
ne sont mis a disposition sur le CTAN que pour encourager la reutilisation de
ce contenu, et pour en conserver une copie perenne. ## Nous contacter Pour
toutes questions et remarques: faq@gutenberg-asso.fr

%package -n texlive-formation-latex-ul
Summary:        Introductory LaTeX course in French
Version:        svn70507
License:        CC-BY-4.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-formation-latex-ul-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-formation-latex-ul-doc <= 11:%{version}

%description -n texlive-formation-latex-ul
This package contains the supporting documentation, slides, exercise files, and
templates for an introductory LaTeX course (in French) prepared for Universite
Laval, Quebec, Canada.

%package -n texlive-frenchmath
Summary:        Typesetting mathematics according to French rules
Version:        svn71205
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsopn.sty)
Requires:       tex(amstext.sty)
Requires:       tex(decimalcomma.sty)
Requires:       tex(dotlessj.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ibrackets.sty)
Requires:       tex(mathgreeks.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(xspace.sty)
Provides:       tex(frenchmath.sty) = %{tl_version}

%description -n texlive-frenchmath
The package provides: capital letters in roman (upright shape) in mathematical
mode according to French rule (can be optionally disabled), correct spacing in
math mode after commas, before a semicolon and around square brackets, some
useful macros and aliases for symbols used in France: \infeg, \supeg, \paral,
... several macros for writing french operator names like pgcd, ppcm, Card, rg,
Vect, ... optionally lowercase Greek letters in upright shape,

%package -n texlive-frletter
Summary:        Typeset letters in the French style
Version:        svn15878
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-frletter
A small class for typesetting letters in France. No assumption is made about
the language in use. The class represents a small modification of the beletter
class, which is itself a modification of the standard LaTeX letter class.

%package -n texlive-frpseudocode
Summary:        French translation for the algorithmicx package
Version:        svn56088
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(algpseudocode.sty)
Provides:       tex(frpseudocode.sty) = %{tl_version}

%description -n texlive-frpseudocode
This package is intended for use alongside Szasz Janos' algorithmicx package.
Its aim is to provide a French translation of terms and words used in
algorithms to make it integrate seamlessly in a French written document.

%package -n texlive-hyphen-basque
Summary:        Basque hyphenation patterns.
Version:        svn73410
License:        Unicode-DFS-2015
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-eu.ec.tex) = %{tl_version}
Provides:       tex(hyph-eu.tex) = %{tl_version}
Provides:       tex(loadhyph-eu.tex) = %{tl_version}

%description -n texlive-hyphen-basque
Hyphenation patterns for Basque in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-french
Summary:        French hyphenation patterns.
Version:        svn73410
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-fr.ec.tex) = %{tl_version}
Provides:       tex(hyph-fr.tex) = %{tl_version}
Provides:       tex(hyph-quote-fr.tex) = %{tl_version}
Provides:       tex(loadhyph-fr.tex) = %{tl_version}

%description -n texlive-hyphen-french
Hyphenation patterns for French in T1/EC and UTF-8 encodings.

%package -n texlive-impatient-fr
Summary:        Free edition of the book "TeX for the Impatient"
Version:        svn54080
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-impatient-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-impatient-fr-doc <= 11:%{version}

%description -n texlive-impatient-fr
"TeX for the Impatient" is a book (of around 350 pages) on TeX, Plain TeX and
Eplain. The book is also available in French and Chinese translations.

%package -n texlive-impnattypo
Summary:        Support typography of l'Imprimerie Nationale Francaise
Version:        svn50227
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifluatex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(impnattypo.sty) = %{tl_version}

%description -n texlive-impnattypo
The package provides useful macros implementing recommendations by the French
Imprimerie Nationale.

%package -n texlive-l2tabu-french
Summary:        French translation of l2tabu
Version:        svn31315
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-l2tabu-french-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-l2tabu-french-doc <= 11:%{version}

%description -n texlive-l2tabu-french
French translation of l2tabu.

%package -n texlive-latex2e-help-texinfo-fr
Summary:        A French translation of "latex2e-help-texinfo"
Version:        svn64228
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex2e-help-texinfo-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex2e-help-texinfo-fr-doc <= 11:%{version}

%description -n texlive-latex2e-help-texinfo-fr
This package provides a complete French translation of latex2e-help-texinfo.

%package -n texlive-letgut
Summary:        Class for the newsletter "La Lettre GUTenberg" of the French TeX User Group GUTenberg
Version:        svn76652
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(accsupp.sty)
Requires:       tex(numeric.cbx)
Requires:       tex(xcolor.sty)
Provides:       tex(informations-gut.tex) = %{tl_version}
Provides:       tex(letgut-acronyms.tex) = %{tl_version}
Provides:       tex(letgut-banner.sty) = %{tl_version}
Provides:       tex(letgut-lstlang.sty) = %{tl_version}
Provides:       tex(letgut.cbx) = %{tl_version}

%description -n texlive-letgut
The French TeX User Group GUTenberg has been publishing "The GUTenberg Letter",
its irregular newsletter, since February 1993. For this purpose, a dedicated,
in-house (La)TeX class was gradually created but, depending on new needs and on
the people who were publishing the Newsletter, its development was somewhat
erratic; in particular, it would not have been possible to publish its code as
it was. In addition, its documentation was non-existent. The Board of Directors
of the association, elected in November 2020, wished to provide a better
structured, more perennial and documented class, able to be published on the
CTAN. This is now done with the present 'letgut' class. # French L'association
GUTenberg publie "La Lettre GUTenberg", son bulletin irregulomestriel, depuis
fevrier 1993. Pour ce faire, une classe (La)TeX dediee, maison, a peu a peu vu
le jour mais, au gre des nouveaux besoins et des personnes qui ont assure la
publication de la Lettre, son developpement a ete quelque peu erratique ; il
n'aurait notamment pas ete possible de publier son code en l'etat. En outre, sa
documentation etait inexistante. Le Conseil d'Administration de l'association,
elu en novembre 2020, a souhaite fournir une classe mieux structuree, davantage
perenne et documentee, a meme d'etre publiee sur le CTAN. C'est desormais chose
faite avec la presente classe letgut.

%package -n texlive-lshort-french
Summary:        Short introduction to LaTeX, French translation
Version:        svn23332
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-french-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-french-doc <= 11:%{version}

%description -n texlive-lshort-french
French version of A Short Introduction to LaTeX2e.

%package -n texlive-mafr
Summary:        Mathematics in accord with French usage
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(babel.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(mafr.sty) = %{tl_version}

%description -n texlive-mafr
The package provides settings and macros for typesetting mathematics with LaTeX
in compliance with French usage. It comes with two document classes, 'fiche'
and 'cours', useful to create short high school documents such as tests or
lessons. The documentation is in French.

%package -n texlive-matapli
Summary:        Class for the french journal "MATAPLI"
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-matapli
This is a class for the french journal "MATAPLI" of the Societe de
Mathematiques Appliquees et Industrielles (SMAI).

%package -n texlive-panneauxroute
Summary:        Commands to display French road signs (vector graphics)
Version:        svn73069
License:        LPPL-1.3c AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(PanneauxRoute.sty) = %{tl_version}

%description -n texlive-panneauxroute
The package provides commands to insert French road signs as vector graphics:
\AffPanneau[graphicx options]{code} \prcode[graphicx options]

%package -n texlive-profcollege
Summary:        A LaTeX package for French maths teachers in college
Version:        svn77090
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(cancel.sty)
Requires:       tex(datatool.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(gmp.sty)
Requires:       tex(hhline.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(longtable.sty)
Requires:       tex(luacas.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(modulus.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multido.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(pifont.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(stringstrings.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xlop.sty)
Requires:       tex(xstring.sty)
Provides:       tex(PfCAireSimple.tex) = %{tl_version}
Provides:       tex(PfCAllumettes.tex) = %{tl_version}
Provides:       tex(PfCArbreCalcul.tex) = %{tl_version}
Provides:       tex(PfCArbreChiffre.tex) = %{tl_version}
Provides:       tex(PfCAssemblagesSolides.tex) = %{tl_version}
Provides:       tex(PfCAutomatismes.tex) = %{tl_version}
Provides:       tex(PfCAutonomie.tex) = %{tl_version}
Provides:       tex(PfCBalance.tex) = %{tl_version}
Provides:       tex(PfCBandeNumerique.tex) = %{tl_version}
Provides:       tex(PfCBarreNiveaux.tex) = %{tl_version}
Provides:       tex(PfCBarresCalculs.tex) = %{tl_version}
Provides:       tex(PfCBillard.tex) = %{tl_version}
Provides:       tex(PfCBoiteADix.tex) = %{tl_version}
Provides:       tex(PfCBonSortie.tex) = %{tl_version}
Provides:       tex(PfCBonbon.tex) = %{tl_version}
Provides:       tex(PfCCAN.tex) = %{tl_version}
Provides:       tex(PfCCalculatrice.tex) = %{tl_version}
Provides:       tex(PfCCalculsCroises.tex) = %{tl_version}
Provides:       tex(PfCCalculsDetailles.tex) = %{tl_version}
Provides:       tex(PfCCalculsFractions.tex) = %{tl_version}
Provides:       tex(PfCCalisson.tex) = %{tl_version}
Provides:       tex(PfCCartesJeux.tex) = %{tl_version}
Provides:       tex(PfCCartesMentales.tex) = %{tl_version}
Provides:       tex(PfCCartographie.tex) = %{tl_version}
Provides:       tex(PfCCheque.tex) = %{tl_version}
Provides:       tex(PfCCible.tex) = %{tl_version}
Provides:       tex(PfCCibleQOp.tex) = %{tl_version}
Provides:       tex(PfCColorilude.tex) = %{tl_version}
Provides:       tex(PfCCompteBon.tex) = %{tl_version}
Provides:       tex(PfCConversion.tex) = %{tl_version}
Provides:       tex(PfCCritere.tex) = %{tl_version}
Provides:       tex(PfCCryptarithme.tex) = %{tl_version}
Provides:       tex(PfCDeAJouer.tex) = %{tl_version}
Provides:       tex(PfCDecDeci.tex) = %{tl_version}
Provides:       tex(PfCDecompFrac.tex) = %{tl_version}
Provides:       tex(PfCDecompFracDeci.tex) = %{tl_version}
Provides:       tex(PfCDecomposerNombrePremier.tex) = %{tl_version}
Provides:       tex(PfCDefiCalc.tex) = %{tl_version}
Provides:       tex(PfCDefiTables.tex) = %{tl_version}
Provides:       tex(PfCDessinAlgo.tex) = %{tl_version}
Provides:       tex(PfCDessinGradue.tex) = %{tl_version}
Provides:       tex(PfCDessinerRatio.tex) = %{tl_version}
Provides:       tex(PfCDiagrammeRadar.tex) = %{tl_version}
Provides:       tex(PfCDistributivite.tex) = %{tl_version}
Provides:       tex(PfCDobble.tex) = %{tl_version}
Provides:       tex(PfCDomino.tex) = %{tl_version}
Provides:       tex(PfCDontCountDots.tex) = %{tl_version}
Provides:       tex(PfCEcrireunQCM.tex) = %{tl_version}
Provides:       tex(PfCEcritureLettres.tex) = %{tl_version}
Provides:       tex(PfCEcritureUnites.tex) = %{tl_version}
Provides:       tex(PfCEngrenagesBase.tex) = %{tl_version}
Provides:       tex(PfCEnigmeAire.tex) = %{tl_version}
Provides:       tex(PfCEnquete.tex) = %{tl_version}
Provides:       tex(PfCEquationBalance.tex) = %{tl_version}
Provides:       tex(PfCEquationComposition2.tex) = %{tl_version}
Provides:       tex(PfCEquationLaurent1.tex) = %{tl_version}
Provides:       tex(PfCEquationModeleBarre.tex) = %{tl_version}
Provides:       tex(PfCEquationPose1.tex) = %{tl_version}
Provides:       tex(PfCEquationSoustraction2.tex) = %{tl_version}
Provides:       tex(PfCEquationSymbole1.tex) = %{tl_version}
Provides:       tex(PfCEquationTerme1.tex) = %{tl_version}
Provides:       tex(PfCEratosthene.tex) = %{tl_version}
Provides:       tex(PfCFactorisation.tex) = %{tl_version}
Provides:       tex(PfCFicheMemo.tex) = %{tl_version}
Provides:       tex(PfCFonctionAffine.tex) = %{tl_version}
Provides:       tex(PfCFractionAireCarre.tex) = %{tl_version}
Provides:       tex(PfCFractionNombre.tex) = %{tl_version}
Provides:       tex(PfCFrise.tex) = %{tl_version}
Provides:       tex(PfCFubuki.tex) = %{tl_version}
Provides:       tex(PfCFutoshiki.tex) = %{tl_version}
Provides:       tex(PfCGaram.tex) = %{tl_version}
Provides:       tex(PfCGeometrie.tex) = %{tl_version}
Provides:       tex(PfCGrades.tex) = %{tl_version}
Provides:       tex(PfCGrimuku.tex) = %{tl_version}
Provides:       tex(PfCHiddenMessage.tex) = %{tl_version}
Provides:       tex(PfCHorloge.tex) = %{tl_version}
Provides:       tex(PfCInfixRPN.sty) = %{tl_version}
Provides:       tex(PfCIteration.tex) = %{tl_version}
Provides:       tex(PfCJeton.tex) = %{tl_version}
Provides:       tex(PfCJeuRangement.tex) = %{tl_version}
Provides:       tex(PfCKakurasu.tex) = %{tl_version}
Provides:       tex(PfCKakuro.tex) = %{tl_version}
Provides:       tex(PfCKenKen.tex) = %{tl_version}
Provides:       tex(PfCLabyrintheJeu.tex) = %{tl_version}
Provides:       tex(PfCLabyrintheNombre.tex) = %{tl_version}
Provides:       tex(PfCLego.tex) = %{tl_version}
Provides:       tex(PfCLignesBrisees.tex) = %{tl_version}
Provides:       tex(PfCMentalo.tex) = %{tl_version}
Provides:       tex(PfCMidpoint.tex) = %{tl_version}
Provides:       tex(PfCModeleBarre.tex) = %{tl_version}
Provides:       tex(PfCMonnaieEuro.tex) = %{tl_version}
Provides:       tex(PfCMosaique.tex) = %{tl_version}
Provides:       tex(PfCMotsCodes.tex) = %{tl_version}
Provides:       tex(PfCMotsCroises.tex) = %{tl_version}
Provides:       tex(PfCMotsEmpiles.tex) = %{tl_version}
Provides:       tex(PfCMulArt.tex) = %{tl_version}
Provides:       tex(PfCMulEthiopie.tex) = %{tl_version}
Provides:       tex(PfCMulJal.tex) = %{tl_version}
Provides:       tex(PfCMulJap.tex) = %{tl_version}
Provides:       tex(PfCMulPiecesPuzzle.tex) = %{tl_version}
Provides:       tex(PfCNombreAstral.tex) = %{tl_version}
Provides:       tex(PfCNonogramme.tex) = %{tl_version}
Provides:       tex(PfCNotionFonction.tex) = %{tl_version}
Provides:       tex(PfCNumberHive.tex) = %{tl_version}
Provides:       tex(PfCNumerationsAnciennes.tex) = %{tl_version}
Provides:       tex(PfCOpCroisees.tex) = %{tl_version}
Provides:       tex(PfCOperationsTrou.tex) = %{tl_version}
Provides:       tex(PfCPanneauxRoutiers.tex) = %{tl_version}
Provides:       tex(PfCPapiers.tex) = %{tl_version}
Provides:       tex(PfCPatronPaves.tex) = %{tl_version}
Provides:       tex(PfCPattern.tex) = %{tl_version}
Provides:       tex(PfCPatternJeton.tex) = %{tl_version}
Provides:       tex(PfCPavage.tex) = %{tl_version}
Provides:       tex(PfCPavageAvecMotifImage.tex) = %{tl_version}
Provides:       tex(PfCPixelArt.tex) = %{tl_version}
Provides:       tex(PfCPointsBlancs.tex) = %{tl_version}
Provides:       tex(PfCPourcentage.tex) = %{tl_version}
Provides:       tex(PfCProbaFrequence.tex) = %{tl_version}
Provides:       tex(PfCProbabilites.tex) = %{tl_version}
Provides:       tex(PfCProgrammeCalcul.tex) = %{tl_version}
Provides:       tex(PfCPropor.tex) = %{tl_version}
Provides:       tex(PfCProprietesDroites.tex) = %{tl_version}
Provides:       tex(PfCPuissanceQuatre.tex) = %{tl_version}
Provides:       tex(PfCPuzzleSommePyramide.tex) = %{tl_version}
Provides:       tex(PfCPyraVoca.tex) = %{tl_version}
Provides:       tex(PfCPyramideCalculs.tex) = %{tl_version}
Provides:       tex(PfCPythagore.tex) = %{tl_version}
Provides:       tex(PfCQuestionsFlash.tex) = %{tl_version}
Provides:       tex(PfCQuestionsRelier.tex) = %{tl_version}
Provides:       tex(PfCQuiSuisJe.tex) = %{tl_version}
Provides:       tex(PfCRLE.tex) = %{tl_version}
Provides:       tex(PfCRangementNombres.tex) = %{tl_version}
Provides:       tex(PfCRapido.tex) = %{tl_version}
Provides:       tex(PfCRappelsFormules.tex) = %{tl_version}
Provides:       tex(PfCRecyclage.tex) = %{tl_version}
Provides:       tex(PfCReperage.tex) = %{tl_version}
Provides:       tex(PfCRepresentationGraphique.tex) = %{tl_version}
Provides:       tex(PfCRepresenterEntier.tex) = %{tl_version}
Provides:       tex(PfCRepresenterFraction.tex) = %{tl_version}
Provides:       tex(PfCRepresenterTableur.tex) = %{tl_version}
Provides:       tex(PfCReseauxSociaux.tex) = %{tl_version}
Provides:       tex(PfCResoudreEquation.tex) = %{tl_version}
Provides:       tex(PfCRondeInfernale.tex) = %{tl_version}
Provides:       tex(PfCRose.tex) = %{tl_version}
Provides:       tex(PfCRullo.tex) = %{tl_version}
Provides:       tex(PfCScrabble.tex) = %{tl_version}
Provides:       tex(PfCScratch.tex) = %{tl_version}
Provides:       tex(PfCSerpent.tex) = %{tl_version}
Provides:       tex(PfCShikaku.tex) = %{tl_version}
Provides:       tex(PfCSimplifierFraction.tex) = %{tl_version}
Provides:       tex(PfCSolides.tex) = %{tl_version}
Provides:       tex(PfCSommeAngles.tex) = %{tl_version}
Provides:       tex(PfCSquaro.tex) = %{tl_version}
Provides:       tex(PfCStatistiques.tex) = %{tl_version}
Provides:       tex(PfCSystemeImage.tex) = %{tl_version}
Provides:       tex(PfCTableauDoubleEntree.tex) = %{tl_version}
Provides:       tex(PfCTableauxUnites.tex) = %{tl_version}
Provides:       tex(PfCTablesOperations.tex) = %{tl_version}
Provides:       tex(PfCTectonic.tex) = %{tl_version}
Provides:       tex(PfCThales.tex) = %{tl_version}
Provides:       tex(PfCTicketCaisse.tex) = %{tl_version}
Provides:       tex(PfCTortueBase.tex) = %{tl_version}
Provides:       tex(PfCTrigonometrie.tex) = %{tl_version}
Provides:       tex(PfCTrio.tex) = %{tl_version}
Provides:       tex(PfCTriominos.tex) = %{tl_version}
Provides:       tex(PfCUrneProba.tex) = %{tl_version}
Provides:       tex(PfCVisualisationMulDeci.tex) = %{tl_version}
Provides:       tex(PfCVueCubes.tex) = %{tl_version}
Provides:       tex(PfCYohaku.tex) = %{tl_version}
Provides:       tex(ProfCollege.sty) = %{tl_version}

%description -n texlive-profcollege
This package provides some commands to help French mathematics teachers for
11-16 years olds, for example: \Tableau[Metre] to write the tabular km|hm|...
with some facilities, \Pythagore{ABC}{5}{7} to write the entire calculation of
AC with the Pythagorean theorem, \Trigo[Cosinus]{ABC}{3}{}{60} to write the
entire calculation of AC with cosine, ... and some others.

%package -n texlive-proflabo
Summary:        Draw laboratory equipment
Version:        svn63147
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(pgf.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tikz.sty)
Provides:       tex(ProfLabo.sty) = %{tl_version}

%description -n texlive-proflabo
This package was developed to help French chemistry teachers to create drawings
(using TikZ) for laboratory stuff.

%package -n texlive-proflycee
Summary:        A LaTeX package for French maths teachers in high school
Version:        svn77424
License:        LPPL-1.3c AND CC0-1.0 AND MIT AND CC-BY-SA-3.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amssymb.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(nicefrac.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(pythontex.sty)
Requires:       tex(randomlist.sty)
Requires:       tex(settobox.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-tab.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ProfLycee-Light.sty) = %{tl_version}
Provides:       tex(ProfLycee-Macros.sty) = %{tl_version}
Provides:       tex(ProfLycee-Pictosbac.sty) = %{tl_version}
Provides:       tex(ProfLycee.sty) = %{tl_version}
Provides:       tex(proflycee-tools-aleatoire.tex) = %{tl_version}
Provides:       tex(proflycee-tools-analyse.tex) = %{tl_version}
Provides:       tex(proflycee-tools-arithm.tex) = %{tl_version}
Provides:       tex(proflycee-tools-cliparts.tex) = %{tl_version}
Provides:       tex(proflycee-tools-competences.tex) = %{tl_version}
Provides:       tex(proflycee-tools-complexes.tex) = %{tl_version}
Provides:       tex(proflycee-tools-ecritures.tex) = %{tl_version}
Provides:       tex(proflycee-tools-espace.tex) = %{tl_version}
Provides:       tex(proflycee-tools-exams.tex) = %{tl_version}
Provides:       tex(proflycee-tools-geom.tex) = %{tl_version}
Provides:       tex(proflycee-tools-graphiques.tex) = %{tl_version}
Provides:       tex(proflycee-tools-listings.tex) = %{tl_version}
Provides:       tex(proflycee-tools-minted.tex) = %{tl_version}
Provides:       tex(proflycee-tools-piton.tex) = %{tl_version}
Provides:       tex(proflycee-tools-probas.tex) = %{tl_version}
Provides:       tex(proflycee-tools-pythontex.tex) = %{tl_version}
Provides:       tex(proflycee-tools-recreat.tex) = %{tl_version}
Provides:       tex(proflycee-tools-stats.tex) = %{tl_version}
Provides:       tex(proflycee-tools-suites.tex) = %{tl_version}
Provides:       tex(proflycee-tools-trigo.tex) = %{tl_version}

%description -n texlive-proflycee
This package provides some commands to help French mathematics teachers for
15-18 years olds, for example: solve equations to approximation ; calculate an
approximate value of an integral ; present Python code or pseudocode, a Python
execution console ; simplify calculations in fractional form, simplify roots ;
display and use a trigonometric circle ; display a small diagram for the sign
of an affine function or a trinomial ; ...

%package -n texlive-profsio
Summary:        Commands (with TikZ) to work with French "BTS SIO" maths themes
Version:        svn76398
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(luacode.sty)
Requires:       tex(lualinalg.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(systeme.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xintbinhex.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Provides:       tex(ProfSio.sty) = %{tl_version}

%description -n texlive-profsio
This package provides some commands (in French) to work with: tables of
Karnaugh ; MPM graphs ; simple graphs.

%package -n texlive-tabvar
Summary:        Typesetting tables showing variations of functions
Version:        svn63921
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(varwidth.sty)
Provides:       tex(tabvar.sty) = %{tl_version}

%description -n texlive-tabvar
This LaTeX package is meant to ease the typesetting of tables showing
variations of functions as they are used in France.

%package -n texlive-tdsfrmath
Summary:        Macros for French teachers of mathematics
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
Provides:       tex(tdsfrmath.sty) = %{tl_version}

%description -n texlive-tdsfrmath
A collection of macros for French maths teachers in colleges and lycees (and
perhaps elsewhere). It is hoped that the package will facilitate the everyday
use of LaTeX by mathematics teachers.

%package -n texlive-texlive-fr
Summary:        TeX Live manual (French)
Version:        svn74301
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-fr-doc <= 11:%{version}

%description -n texlive-texlive-fr
TeX Live manual (French)

%package -n texlive-translation-array-fr
Summary:        French translation of the documentation of array
Version:        svn24344
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-array-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-array-fr-doc <= 11:%{version}

%description -n texlive-translation-array-fr
A French translation of the documentation of array.

%package -n texlive-translation-dcolumn-fr
Summary:        French translation of the documentation of dcolumn
Version:        svn24345
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-dcolumn-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-dcolumn-fr-doc <= 11:%{version}

%description -n texlive-translation-dcolumn-fr
A French translation of the documentation of dcolumn.

%package -n texlive-translation-natbib-fr
Summary:        French translation of the documentation of natbib
Version:        svn25105
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-natbib-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-natbib-fr-doc <= 11:%{version}

%description -n texlive-translation-natbib-fr
A French translation of the documentation of natbib.

%package -n texlive-translation-tabbing-fr
Summary:        French translation of the documentation of Tabbing
Version:        svn24228
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-translation-tabbing-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-translation-tabbing-fr-doc <= 11:%{version}

%description -n texlive-translation-tabbing-fr
A translation to French (by the author) of the documentation of the Tabbing
package.

%package -n texlive-variations
Summary:        Typeset tables of variations of functions
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(variations.sty) = %{tl_version}
Provides:       tex(variations.tex) = %{tl_version}

%description -n texlive-variations
The package provides macros for typesetting tables showing variations of
functions according to French usage. These macros may be used by both LaTeX and
plain TeX users.

%package -n texlive-visualfaq-fr
Summary:        FAQ LaTeX visuelle francophone
Version:        svn71053
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-visualfaq-fr-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-visualfaq-fr-doc <= 11:%{version}

%description -n texlive-visualfaq-fr
(French version below.) The Visual LaTeX FAQ is an innovative new search
interface on LaTeX Frequently Asked Questions. This version is a French
translation, offering links to the French-speaking LaTeX FAQ. Vous avez du mal
a trouver la reponse a une question sur LaTeX ou meme a trouver les mots pour
exprimer votre question? La FAQ LaTeX visuelle est une interface de recherche
innovante qui presente plus d'une centaine d'exemples de mises en forme de
documents frequemment demandees. Il suffit de cliquer sur l'hyperlien qui
correspond a ce que vous souhaitez faire - ou ne pas faire - et la FAQ LaTeX
visuelle enverra votre navigateur web a la page correspondante de la FAQ LaTeX
francophone.

%package -n texlive-visualtikz
Summary:        Visual help for TikZ based on images with minimum text
Version:        svn54080
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-visualtikz-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-visualtikz-doc <= 11:%{version}

%description -n texlive-visualtikz
Visual help for TikZ based on images with minimum text: an image per command or
parameter. The document is in French, but will be translated into English
later.

%post -n texlive-hyphen-basque
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/basque.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "basque loadhyph-eu.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{basque}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{basque}{loadhyph-eu.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-basque
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/basque.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{basque}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%post -n texlive-hyphen-french
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/french.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "french loadhyph-fr.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=patois.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=patois" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/=francais.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "=francais" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{french}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{french}{loadhyph-fr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{patois}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{patois}{loadhyph-fr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
sed --follow-symlinks -i '/\\addlanguage{francais}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{francais}{loadhyph-fr.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-french
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/french.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=patois.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/=francais.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{french}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{patois}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{francais}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-aeguill
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/aeguill/
%doc %{_texmf_main}/doc/latex/aeguill/

%files -n texlive-annee-scolaire
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/annee-scolaire/
%doc %{_texmf_main}/doc/latex/annee-scolaire/

%files -n texlive-apprendre-a-programmer-en-tex
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/plain/apprendre-a-programmer-en-tex/

%files -n texlive-apprends-latex
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/apprends-latex/

%files -n texlive-babel-basque
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-basque/
%doc %{_texmf_main}/doc/generic/babel-basque/

%files -n texlive-babel-french
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-french/
%doc %{_texmf_main}/doc/generic/babel-french/

%files -n texlive-basque-book
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/basque-book/
%doc %{_texmf_main}/doc/latex/basque-book/

%files -n texlive-basque-date
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/basque-date/
%doc %{_texmf_main}/doc/latex/basque-date/

%files -n texlive-bib-fr
%license lppl1.3c.txt
%{_texmf_main}/bibtex/bst/bib-fr/
%doc %{_texmf_main}/doc/bibtex/bib-fr/

%files -n texlive-bibleref-french
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/bibleref-french/
%doc %{_texmf_main}/doc/latex/bibleref-french/

%files -n texlive-booktabs-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/booktabs-fr/

%files -n texlive-cahierprof
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cahierprof/
%doc %{_texmf_main}/doc/latex/cahierprof/

%files -n texlive-couleurs-fr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/couleurs-fr/
%doc %{_texmf_main}/doc/latex/couleurs-fr/

%files -n texlive-droit-fr
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/droit-fr/
%doc %{_texmf_main}/doc/latex/droit-fr/

%files -n texlive-e-french
%license lppl1.3c.txt
%{_texmf_main}/makeindex/e-french/
%{_texmf_main}/tex/generic/e-french/
%doc %{_texmf_main}/doc/generic/e-french/

%files -n texlive-epslatex-fr
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/epslatex-fr/

%files -n texlive-expose-expl3-dunkerque-2019
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/expose-expl3-dunkerque-2019/

%files -n texlive-facture
%{_texmf_main}/tex/xelatex/facture/
%doc %{_texmf_main}/doc/xelatex/facture/

%files -n texlive-faq-fr
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/faq-fr/

%files -n texlive-faq-fr-gutenberg
%license cc-by-sa-4.txt
%doc %{_texmf_main}/doc/latex/faq-fr-gutenberg/

%files -n texlive-formation-latex-ul
%license cc-by-4.txt
%doc %{_texmf_main}/doc/latex/formation-latex-ul/

%files -n texlive-frenchmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/frenchmath/
%doc %{_texmf_main}/doc/latex/frenchmath/

%files -n texlive-frletter
%license pd.txt
%{_texmf_main}/tex/latex/frletter/
%doc %{_texmf_main}/doc/latex/frletter/

%files -n texlive-frpseudocode
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/frpseudocode/
%doc %{_texmf_main}/doc/latex/frpseudocode/

%files -n texlive-hyphen-basque
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-hyphen-french
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-impatient-fr
%license fdl.txt
%doc %{_texmf_main}/doc/plain/impatient-fr/

%files -n texlive-impnattypo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/impnattypo/
%doc %{_texmf_main}/doc/latex/impnattypo/

%files -n texlive-l2tabu-french
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/l2tabu-french/

%files -n texlive-latex2e-help-texinfo-fr
%license pd.txt
%doc %{_texmf_main}/doc/info/
%doc %{_texmf_main}/doc/latex/latex2e-help-texinfo-fr/

%files -n texlive-letgut
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/letgut/
%doc %{_texmf_main}/doc/lualatex/letgut/

%files -n texlive-lshort-french
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-french/

%files -n texlive-mafr
%license gpl2.txt
%{_texmf_main}/tex/latex/mafr/
%doc %{_texmf_main}/doc/latex/mafr/

%files -n texlive-matapli
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/matapli/
%doc %{_texmf_main}/doc/latex/matapli/

%files -n texlive-panneauxroute
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/panneauxroute/
%doc %{_texmf_main}/doc/latex/panneauxroute/

%files -n texlive-profcollege
%license lppl1.3c.txt
%{_texmf_main}/metapost/profcollege/
%{_texmf_main}/tex/latex/profcollege/
%doc %{_texmf_main}/doc/latex/profcollege/

%files -n texlive-proflabo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/proflabo/
%doc %{_texmf_main}/doc/latex/proflabo/

%files -n texlive-proflycee
%license lppl1.3c.txt
%{_texmf_main}/metapost/proflycee/
%{_texmf_main}/tex/latex/proflycee/
%doc %{_texmf_main}/doc/latex/proflycee/

%files -n texlive-profsio
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/profsio/
%doc %{_texmf_main}/doc/latex/profsio/

%files -n texlive-tabvar
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/tabvar/
%{_texmf_main}/fonts/map/dvips/tabvar/
%{_texmf_main}/fonts/tfm/public/tabvar/
%{_texmf_main}/fonts/type1/public/tabvar/
%{_texmf_main}/metapost/tabvar/
%{_texmf_main}/tex/latex/tabvar/
%doc %{_texmf_main}/doc/latex/tabvar/

%files -n texlive-tdsfrmath
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/tdsfrmath/
%doc %{_texmf_main}/doc/latex/tdsfrmath/

%files -n texlive-texlive-fr
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-fr/

%files -n texlive-translation-array-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-array-fr/

%files -n texlive-translation-dcolumn-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-dcolumn-fr/

%files -n texlive-translation-natbib-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-natbib-fr/

%files -n texlive-translation-tabbing-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/translation-tabbing-fr/

%files -n texlive-variations
%license gpl2.txt
%{_texmf_main}/tex/generic/variations/
%doc %{_texmf_main}/doc/generic/variations/

%files -n texlive-visualfaq-fr
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/visualfaq-fr/

%files -n texlive-visualtikz
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/visualtikz/

%changelog
* Sat Jan 24 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn72499-3
- fix descriptions, licensing

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72499-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72499-1
- Update to TeX Live 2025
