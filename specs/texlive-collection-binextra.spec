%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-binextra
Epoch:          12
Version:        svn77772
Release:        7%{?dist}
Summary:        TeX auxiliary programs

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-binextra.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctan_chk.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctan_chk.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hook-pre-commit-pkg.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hook-pre-commit-pkg.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xdvipsk-support.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xdvipsk-support.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-a2ping
Requires:       texlive-adhocfilelist
Requires:       texlive-arara
Requires:       asymptote
Requires:       texlive-bibtex8
Requires:       texlive-bibtexu
Requires:       texlive-bundledoc
Requires:       texlive-checklistings
Requires:       texlive-chklref
Requires:       texlive-chktex
Requires:       texlive-clojure-pamphlet
Requires:       texlive-cluttex
Requires:       texlive-collection-basic
Requires:       texlive-ctan-o-mat
Requires:       texlive-ctan_chk
Requires:       texlive-ctanbib
Requires:       texlive-ctanify
Requires:       texlive-ctanupload
Requires:       texlive-ctie
Requires:       texlive-cweb
Requires:       texlive-de-macro
Requires:       texlive-detex
Requires:       texlive-digestif
Requires:       texlive-dtl
Requires:       texlive-dtxgen
Requires:       texlive-dvi2tty
Requires:       texlive-dviasm
Requires:       texlive-dvicopy
Requires:       texlive-dvidvi
Requires:       texlive-dviinfox
Requires:       texlive-dviljk
Requires:       texlive-dviout-util
Requires:       texlive-dvipng
Requires:       texlive-dvipos
Requires:       texlive-dvisvgm
Requires:       texlive-easydtx
Requires:       texlive-expltools
Requires:       texlive-findhyph
Requires:       texlive-fragmaster
Requires:       texlive-git-latexdiff
Requires:       texlive-gsftopk
Requires:       texlive-hook-pre-commit-pkg
Requires:       texlive-installfont
Requires:       texlive-ketcindy
Requires:       texlive-l3sys-query
Requires:       texlive-lacheck
Requires:       texlive-latex-git-log
Requires:       texlive-latex-papersize
Requires:       texlive-latex2man
Requires:       texlive-latex2nemeth
Requires:       texlive-latexdiff
Requires:       texlive-latexfileversion
Requires:       texlive-latexindent
Requires:       latexmk
Requires:       texlive-latexpand
Requires:       texlive-light-latex-make
Requires:       texlive-listings-ext
Requires:       texlive-ltxfileinfo
Requires:       texlive-ltximg
Requires:       texlive-make4ht
Requires:       texlive-match_parens
Requires:       texlive-mflua
Requires:       texlive-mkjobtexmf
Requires:       texlive-optexcount
Requires:       texlive-patgen
Requires:       texlive-pdfbook2
Requires:       texlive-pdfcrop
Requires:       texlive-pdfjam
Requires:       texlive-pdflatexpicscale
Requires:       texlive-pdftex-quiet
Requires:       texlive-pdftosrc
Requires:       texlive-pdfxup
Requires:       texlive-pfarrei
Requires:       texlive-pkfix
Requires:       texlive-pkfix-helper
Requires:       texlive-ppmcheckpdf
Requires:       texlive-purifyeps
Requires:       texlive-pythontex
Requires:       texlive-runtexfile
Requires:       texlive-runtexshebang
Requires:       texlive-seetexk
Requires:       texlive-show-pdf-tags
Requires:       texlive-spix
Requires:       texlive-sqltex
Requires:       texlive-srcredact
Requires:       texlive-sty2dtx
Requires:       texlive-synctex
Requires:       texlive-tex4ebook
Requires:       texlive-texaccents
Requires:       texlive-texblend
Requires:       texlive-texcount
Requires:       texlive-texdef
Requires:       texlive-texdiff
Requires:       texlive-texdirflatten
Requires:       texlive-texdoc
Requires:       texlive-texdoctk
Requires:       texlive-texfot
Requires:       texlive-texlive-scripts-extra
Requires:       texlive-texliveonfly
Requires:       texlive-texloganalyser
Requires:       texlive-texlogfilter
Requires:       texlive-texlogsieve
Requires:       texlive-texosquery
Requires:       texlive-texplate
Requires:       texlive-texware
Requires:       texlive-tie
Requires:       texlive-tpic2pdftex
Requires:       texlive-typeoutfileinfo
Requires:       texlive-upmendex
Requires:       texlive-web
Requires:       texlive-xdvipsk
Requires:       texlive-xdvipsk-support
Requires:       texlive-xindex
Requires:       texlive-xindy
Requires:       texlive-xpdfopen

%description
Myriad additional TeX-related support programs. Includes programs and macros
for DVI file manipulation, literate programming, patgen, and plenty more.


%package -n texlive-ctan_chk
Summary:        CTAN guidelines verifier and corrector for uploading projects
Version:        svn36304
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ctan_chk-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ctan_chk-doc <= 11:%{version}

%description -n texlive-ctan_chk
Basic gawk program that uses CTAN's published guidelines for authors to help
eliminate sloppiness in uploaded files/projects. It is completely open for
users to program additional guidelines as well as CTAN's future adjustments.

%package -n texlive-hook-pre-commit-pkg
Summary:        Pre-commit git hook for LaTeX package developers
Version:        svn76790
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hook-pre-commit-pkg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hook-pre-commit-pkg-doc <= 11:%{version}

%description -n texlive-hook-pre-commit-pkg
This package provides a pre-commit git hook to check basic LaTeX syntax for the
use of package developers. It is installed by copying it into the .git/.hooks
file. It then checks the following file types: .sty, .dtx, .bbx, .cbx, and
.lbx. List of performed checks: Each line must be terminated by a %, without a
space before it. Empty lines are allowed, but not lines with nothing but spaces
in them. \begin{macro} and \end{macro} must be paired. \begin{macrocode} and
\end{macrocode} must be paired. \begin{macro} must have a second argument. One
space must be printed between % and \begin{macro} or \end{macro}. % must be the
first character in the line. Four spaces must be printed between % and
\begin{macrocode} or \end{macrocode}. \cs argument must not start with a
backslash.

%package -n texlive-xdvipsk-support
Summary:        LuaLaTeX packages for the xdvipsk binary (dvips extension)
Version:        svn77772
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-xdvipsk
Requires:       tex(luatexbase.sty)
Provides:       tex(xdvipsk-support.sty) = %{tl_version}
Provides:       tex(xdvipsk.def) = %{tl_version}
Provides:       tex(xdvipskmaps.sty) = %{tl_version}

%description -n texlive-xdvipsk-support
This LaTeX package bundle offers support for xdvipsk, an extension of the dvips
binary. xdvipsk supports BMP, PCX, TIFF, JPEG, and PNG formats and performs
scaling, rotating, trim, and viewport operations like EPS images. The
xdvispk.def driver for the graphics package offers a LaTeX interface. However,
it lacks clipping, trimming, and viewport operations. The LuaLaTeX package
xdvipskmaps provides OpenType font support for xdvipsk. It generates map files
containing information about OpenType fonts used in DVI files.


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-ctan_chk
%license gpl3.txt
%doc %{_texmf_main}/doc/support/ctan_chk/

%files -n texlive-hook-pre-commit-pkg
%license gpl3.txt
%doc %{_texmf_main}/doc/support/hook-pre-commit-pkg/

%files -n texlive-xdvipsk-support
%license lppl1.3c.txt
%{_texmf_main}/tex/lualatex/xdvipsk-support/
%doc %{_texmf_main}/doc/lualatex/xdvipsk-support/

%changelog
* Sat Mar 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77772-7
- Update collection from svn75830 to svn77772
- Add xdvipsk-support

* Sat Mar 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75830-6
- move runtexfile and show-pdf-tags to texlive-base

* Sun Feb  8 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75830-5
- update show-pdf-tags

* Thu Jan 15 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75830-4
- fix runtexfile summary length to be under 80 chars

* Mon Jan 12 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn75830-3
- fix descriptions, fix licensing
- update components to latest revisions

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75830-2
- regenerated, no longer generates deps from docs

* Thu Sep 18 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn75830-1
- Update to TeX Live 2025
