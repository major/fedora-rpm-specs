%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langcjk
Epoch:          12
Version:        svn65824
Release:        4%{?dist}
Summary:        Chinese/Japanese/Korean (base)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langcjk.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adobemapping.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/c90.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/c90.doc.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk.doc.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjkpunct.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjkpunct.doc.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dnp.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/evangelion-jfm.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/evangelion-jfm.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixjfm.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fixjfm.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/garuda-c90.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/norasi-c90.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxtatescale.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pxtatescale.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcjk2uni.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xcjk2uni.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecjk.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xecjk.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zitie.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zitie.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zxjafont.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zxjafont.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-adobemapping
Requires:       texlive-c90
Requires:       texlive-cjk
Requires:       texlive-cjk-gs-integrate
Requires:       texlive-cjkpunct
Requires:       texlive-cjkutils
Requires:       texlive-collection-basic
Requires:       texlive-dnp
Requires:       texlive-evangelion-jfm
Requires:       texlive-fixjfm
Requires:       texlive-garuda-c90
Requires:       texlive-jfmutil
Requires:       texlive-norasi-c90
Requires:       texlive-pxtatescale
Requires:       texlive-xcjk2uni
Requires:       texlive-xecjk
Requires:       texlive-zitie
Requires:       texlive-zxjafont

%description
Packages supporting a combination of Chinese, Japanese, Korean, including
macros, fonts, documentation. Also Thai in the c90 encoding, since there is
some overlap in those fonts; standard Thai support is in collection-langother.
Additional packages for CJK are in their individual language collections.


%package -n texlive-adobemapping
Summary:        Adobe cmap and pdfmapping files
Version:        svn66552
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-adobemapping
The package comprises the collection of CMap and PDF mapping files made
available for distribution by Adobe.

%package -n texlive-c90
Summary:        C90 font encoding for Thai
Version:        svn60830
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-c90
part of the CJK package, ctan.org/pkg/cjk

%package -n texlive-cjk
Summary:        CJK language support
Version:        svn60865
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-arphic
Requires:       texlive-cns
Requires:       texlive-garuda-c90
Requires:       texlive-norasi-c90
Requires:       texlive-uhc
Requires:       texlive-wadalab
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(ulem.sty)
Provides:       tex(CJK.sty) = %{tl_version}
Provides:       tex(CJKfntef.sty) = %{tl_version}
Provides:       tex(CJKnumb.sty) = %{tl_version}
Provides:       tex(CJKspace.sty) = %{tl_version}
Provides:       tex(CJKulem.sty) = %{tl_version}
Provides:       tex(CJKutf8.sty) = %{tl_version}
Provides:       tex(CJKvert.sty) = %{tl_version}
Provides:       tex(MULEenc.sty) = %{tl_version}
Provides:       tex(c90enc.def) = %{tl_version}
Provides:       tex(pinyin.ldf) = %{tl_version}
Provides:       tex(pinyin.sty) = %{tl_version}
Provides:       tex(pshan.sty) = %{tl_version}
Provides:       tex(ruby.sty) = %{tl_version}
Provides:       tex(thaicjk.ldf) = %{tl_version}

%description -n texlive-cjk
CJK is a macro package for LaTeX, providing simultaneous support for various
Asian scripts in many encodings (including Unicode): Chinese (both traditional
and simplified), Japanese, Korean and Thai. A special add-on feature is an
interface to the Emacs editor (cjk-enc.el) which gives simultaneous,
easy-to-use support to a bunch of other scripts in addition to the above --
Cyrillic, Greek, Latin-based scripts, Russian and Vietnamese are supported.

%package -n texlive-cjkpunct
Summary:        Adjust locations and kerning of CJK punctuation marks
Version:        svn41119
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(CJKpunct.sty) = %{tl_version}

%description -n texlive-cjkpunct
The package serves as a companion package for CJK.

%package -n texlive-dnp
Summary:        Subfont numbers for DNP font encoding
Version:        svn54074
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dnp
part of the CJK package, ctan.org/pkg/cjk

%package -n texlive-evangelion-jfm
Summary:        A Japanese font metric supporting many advanced features
Version:        svn69751
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-evangelion-jfm
This package provides a Japanese Font Metric supporting vertical and horizontal
typesetting, 'linegap punctuations', 'extended fonts', and more interesting and
helpful features using traditional ('tc') and simplified ('sc') Chinese or
Japanese fonts under LuaTeX-ja. It also makes full use of the 'priority'
feature, meeting the standards, and allows easy customisation.

%package -n texlive-fixjfm
Summary:        Fix JFM (for *pTeX)
Version:        svn77677
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fixjfm.sty) = %{tl_version}

%description -n texlive-fixjfm
This package fixes several bugs in the JFM format. Both LaTeX and plain TeX are
supported.

%package -n texlive-garuda-c90
Summary:        TeX support (from CJK) for the garuda font
Version:        svn60832
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fonts-tlwg

%description -n texlive-garuda-c90
TeX support (from CJK) for the garuda font

%package -n texlive-norasi-c90
Summary:        TeX support (from CJK) for the norasi font
Version:        svn60831
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fonts-tlwg

%description -n texlive-norasi-c90
TeX support (from CJK) for the norasi font

%package -n texlive-pxtatescale
Summary:        Patch to graphics driver for scaling in vertical direction of pTeX
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pxtatescale.sty) = %{tl_version}

%description -n texlive-pxtatescale
Patch for graphics driver 'dvipdfmx' to support correct scaling in vertical
direction of Japanese pTeX/upTeX.

%package -n texlive-xcjk2uni
Summary:        Convert CJK characters to Unicode, in pdfTeX
Version:        svn54958
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xCJK2uni-UBg5plus.def) = %{tl_version}
Provides:       tex(xCJK2uni-UBig5.def) = %{tl_version}
Provides:       tex(xCJK2uni-UGB.def) = %{tl_version}
Provides:       tex(xCJK2uni-UGBK.def) = %{tl_version}
Provides:       tex(xCJK2uni-UJIS.def) = %{tl_version}
Provides:       tex(xCJK2uni-UKS.def) = %{tl_version}
Provides:       tex(xCJK2uni.sty) = %{tl_version}

%description -n texlive-xcjk2uni
The package provides commands to convert CJK characters to Unicode in non-UTF-8
encoding; it provides hooks to support hyperref in producing correct bookmarks.
The bundle also provides /ToUnicode mapping file(s) for a CJK subfont; these
can be used with the cmap package, allowing searches of, and cut-and-paste
operations on a PDF file generated by pdfTeX.

%package -n texlive-xecjk
Summary:        Support for CJK documents in XeLaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-ctex
Provides:       tex(xeCJK-listings.sty) = %{tl_version}
Provides:       tex(xeCJK.sty) = %{tl_version}
Provides:       tex(xeCJKfntef.sty) = %{tl_version}
Provides:       tex(xunicode-addon.sty) = %{tl_version}
Provides:       tex(xunicode-extra.def) = %{tl_version}

%description -n texlive-xecjk
A LaTeX package for typesetting CJK documents in the way users have become used
to, in the CJK package. The package requires a current version of xtemplate
(and hence of the current LaTeX3 development environment).

%package -n texlive-zitie
Summary:        Create CJK character calligraphy practicing sheets
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(zitie.luatex.def) = %{tl_version}
Provides:       tex(zitie.sty) = %{tl_version}
Provides:       tex(zitie.xetex.def) = %{tl_version}

%description -n texlive-zitie
This is a LaTeX package for creating CJK character calligraphy practicing
sheets (copybooks). Currently, only XeTeX is supported.

%package -n texlive-zxjafont
Summary:        Set up Japanese font families for XeLaTeX
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(keyval.sty)
Provides:       tex(zxjafont.sty) = %{tl_version}

%description -n texlive-zxjafont
Set up Japanese font families for XeLaTeX


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

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-adobemapping
%license bsd.txt
%{_texmf_main}/fonts/cmap/adobemapping/

%files -n texlive-c90
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/c90/
%doc %{_texmf_main}/doc/fonts/enc/

%files -n texlive-cjk
%license gpl2.txt
%{_texmf_main}/tex/latex/cjk/
%doc %{_texmf_main}/doc/latex/cjk/

%files -n texlive-cjkpunct
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cjkpunct/
%doc %{_texmf_main}/doc/latex/cjkpunct/

%files -n texlive-dnp
%license gpl2.txt
%{_texmf_main}/fonts/sfd/dnp/

%files -n texlive-evangelion-jfm
%license mit.txt
%{_texmf_main}/tex/luatex/evangelion-jfm/
%doc %{_texmf_main}/doc/luatex/evangelion-jfm/

%files -n texlive-fixjfm
%license knuth.txt
%{_texmf_main}/tex/generic/fixjfm/
%doc %{_texmf_main}/doc/generic/fixjfm/

%files -n texlive-garuda-c90
%license lppl1.3c.txt
%{_texmf_main}/dvips/garuda-c90/
%{_texmf_main}/fonts/map/dvips/garuda-c90/
%{_texmf_main}/fonts/tfm/public/garuda-c90/

%files -n texlive-norasi-c90
%license lppl1.3c.txt
%{_texmf_main}/dvips/norasi-c90/
%{_texmf_main}/fonts/map/dvips/norasi-c90/
%{_texmf_main}/fonts/tfm/public/norasi-c90/

%files -n texlive-pxtatescale
%license mit.txt
%{_texmf_main}/tex/latex/pxtatescale/
%doc %{_texmf_main}/doc/latex/pxtatescale/

%files -n texlive-xcjk2uni
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xcjk2uni/
%doc %{_texmf_main}/doc/latex/xcjk2uni/

%files -n texlive-xecjk
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xelatex/xecjk/
%doc %{_texmf_main}/doc/xelatex/xecjk/

%files -n texlive-zitie
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/zitie/
%doc %{_texmf_main}/doc/xelatex/zitie/

%files -n texlive-zxjafont
%license mit.txt
%{_texmf_main}/tex/latex/zxjafont/
%doc %{_texmf_main}/doc/latex/zxjafont/

%changelog
* Wed Feb 11 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn65824-4
- Update fixjfm pxtatescale xecjk zitie zxjafont

* Wed Jan 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn65824-3
- Update components
- fix descriptions
- fix Knuth license tag

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn65824-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn65824-1
- Update to TeX Live 2025
