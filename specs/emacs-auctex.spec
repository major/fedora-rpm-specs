Summary:        Enhanced TeX modes for Emacs
Name:           emacs-auctex
Version:        14.1.2
Release:        %autorelease

# The project as a whole is GPL-3.0-or-later.  Exceptions:
# - doc/intro.texi is FSFAP
# - doc/auctex* and doc/preview* are GFDL-1.3-no-invariants-or-later
# - the generated PDF file contains fonts distributed under Knuth-CTAN
License:        GPL-3.0-or-later AND FSFAP AND GFDL-1.3-no-invariants-or-later AND Knuth-CTAN
URL:            https://www.gnu.org/software/auctex/
VCS:            git:https://git.savannah.gnu.org/cgit/auctex.git
Source:         https://github.com/emacsmirror/auctex/archive/auctex-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs-nw
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  tex(german.ldf)
BuildRequires:  tex(tex)
BuildRequires:  texinfo
BuildRequires:  texlive-latex
BuildRequires:  texlive-mylatex

Requires:       dvipng
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       ghostscript
Requires:       tex-preview = %{version}-%{release}
Requires:       texlive-dvips
Requires:       texlive-latex

Recommends:     texlive-mylatex

# This can be removed when F48 reaches EOL
Obsoletes:      %{name}-doc < 14.0.0
Provides:       %{name}-doc = %{version}-%{release}

%description
AUCTeX is an extensible package that supports writing and formatting TeX files
for most variants of Emacs.

AUCTeX supports many different TeX macro packages, including AMS-TeX, LaTeX,
Texinfo and basic support for ConTeXt.  Documentation can be found under
/usr/share/doc, e.g. the reference card (tex-ref.pdf) and the FAQ.  The AUCTeX
manual is available in Emacs info (C-h i d m AUCTeX RET).  On the AUCTeX home
page, we provide manuals in various formats.

AUCTeX includes preview-latex support which makes LaTeX a tightly integrated
component of your editing workflow by visualizing selected source chunks (such
as single formulas or graphics) directly as images in the source buffer.

This package is for GNU Emacs.

%package -n tex-preview
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
License:        GPL-3.0-or-later AND Knuth-CTAN
Summary:        Preview style files for LaTeX
Requires:       texlive-base
Requires:       texlive-kpathsea
# This is the latest build we accidentally provided from texlive
Obsoletes:      texlive-preview <= 12:svn78824-5
Provides:       texlive-preview = 12:svn78824-5

%description -n tex-preview
The preview package for LaTeX allows for the processing of selected parts of a
LaTeX input file.  This package extracts indicated pieces from a source file
(typically displayed equations, figures and graphics) and typesets with their
base point at the (1in,1in) magic location, shipping out the individual pieces
on separate pages without any page markup.  You can produce either DVI or PDF
files, and options exist that will set the page size separately for each page.
In that manner, further processing (as with Ghostscript or dvipng) will be
able to work in a single pass.

The main purpose of this package is the extraction of certain environments
(most notably displayed formulas) from LaTeX sources as graphics.  This works
with DVI files postprocessed by either Dvips and Ghostscript or dvipng, but it
also works when you are using PDFTeX for generating PDF files (usually also
postprocessed by Ghostscript).

The tex-preview package is generated from the AUCTeX package for Emacs.

%prep
%autosetup -n auctex-auctex-%{version}

%build
%make_build TEX=tex
%make_build preview.pdf TEX=tex

%install
# The makefile no longer has an install target, so install by hand
mkdir -p %{buildroot}%{_emacs_sitelispdir}/auctex
cp -a *.el *.elc images style %{buildroot}%{_emacs_sitelispdir}/auctex

# The tex-site file needs to be one directory higher
mv %{buildroot}%{_emacs_sitelispdir}/auctex/tex-site.el \
   %{buildroot}%{_emacs_sitelispdir}

# The startup files go in _emacs_sitestartdir
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}%{_emacs_sitelispdir}/auctex/auctex{,-autoloads}.el* \
   %{buildroot}%{_emacs_sitestartdir}

# Install the info files
mkdir -p %{buildroot}%{_infodir}
cp -p doc/{auctex,preview-latex}.info* %{buildroot}%{_infodir}

# Install the LaTeX files
mkdir -p %{buildroot}%{_texmf_main}/tex/latex/preview
cp -p latex/*.{cfg,def,sty} %{buildroot}%{_texmf_main}/tex/latex/preview
mkdir -p %{buildroot}%{_texmf_main}/doc/latex/preview
cp -p latex/{README,preview.pdf} %{buildroot}%{_texmf_main}/doc/latex/preview

%check
make -C tests

%files
%doc ChangeLog.1 NEWS.org
%doc %{_infodir}/*.info*
%license COPYING
%{_emacs_sitestartdir}/*
%{_emacs_sitelispdir}/auctex/
%{_emacs_sitelispdir}/tex-site.el

%files -n tex-preview
%license COPYING
%{_texmf_main}/tex/latex/preview/
%{_texmf_main}/doc/latex/preview/

%changelog
%autochangelog
