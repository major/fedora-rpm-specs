%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langchinese
Epoch:          12
Version:        svn77432
Release:        4%{?dist}
Summary:        Chinese

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-langchinese.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic-ttf.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arphic-ttf.doc.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.doc.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-faq-zh-cn.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-faq-zh-cn.doc.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.doc.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cns.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cns.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex.doc.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex-faq.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctex-faq.doc.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exam-zh.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exam-zh.doc.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.doc.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fduthesis.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fduthesis.doc.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hanzibox.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hanzibox.doc.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-chinese.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient-cn.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/impatient-cn.doc.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/install-latex-guide-zh-cn.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/install-latex-guide-zh-cn.doc.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-notes-zh-cn.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-notes-zh-cn.doc.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-chinese.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lshort-chinese.doc.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex-cn.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex-cn.doc.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lxgw-fonts.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lxgw-fonts.doc.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanicolle.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/nanicolle.doc.tar.xz
Source41:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njurepo.tar.xz
Source42:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/njurepo.doc.tar.xz
Source43:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfornament-han.tar.xz
Source44:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pgfornament-han.doc.tar.xz
Source45:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qyxf-book.tar.xz
Source46:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/qyxf-book.doc.tar.xz
Source47:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sjtutex.tar.xz
Source48:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sjtutex.doc.tar.xz
Source49:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan-l3.tar.xz
Source50:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/suanpan-l3.doc.tar.xz
Source51:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-zh-cn.tar.xz
Source52:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-zh-cn.doc.tar.xz
Source53:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texproposal.tar.xz
Source54:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texproposal.doc.tar.xz
Source55:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.tar.xz
Source56:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.doc.tar.xz
Source57:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/upzhkinsoku.tar.xz
Source58:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/upzhkinsoku.doc.tar.xz
Source59:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpinyin.tar.xz
Source60:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpinyin.doc.tar.xz
Source61:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xtuthesis.tar.xz
Source62:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xtuthesis.doc.tar.xz
Source63:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlineskip.tar.xz
Source64:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlineskip.doc.tar.xz
Source65:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlipsum.tar.xz
Source66:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhlipsum.doc.tar.xz
Source67:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics.tar.xz
Source68:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics.doc.tar.xz
Source69:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics-uptex.tar.xz
Source70:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics-uptex.doc.tar.xz
Source71:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhnumber.tar.xz
Source72:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhnumber.doc.tar.xz
Source73:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhspacing.tar.xz
Source74:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhspacing.doc.tar.xz

# AppStream metadata for font components
Source75:        fandol.metainfo.xml

# Patches
Patch0:         texlive-xtuthesis-use-diagbox.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
Requires:       texlive-base
Requires:       texlive-arphic
Requires:       texlive-arphic-ttf
Requires:       texlive-asymptote-by-example-zh-cn
Requires:       texlive-asymptote-faq-zh-cn
Requires:       texlive-asymptote-manual-zh-cn
Requires:       texlive-cns
Requires:       texlive-collection-langcjk
Requires:       texlive-ctex
Requires:       texlive-ctex-faq
Requires:       texlive-exam-zh
Requires:       texlive-fandol
Requires:       texlive-fduthesis
Requires:       texlive-hanzibox
Requires:       texlive-hyphen-chinese
Requires:       texlive-impatient-cn
Requires:       texlive-install-latex-guide-zh-cn
Requires:       texlive-latex-notes-zh-cn
Requires:       texlive-lshort-chinese
Requires:       texlive-luatex-cn
Requires:       texlive-lxgw-fonts
Requires:       texlive-nanicolle
Requires:       texlive-njurepo
Requires:       texlive-pgfornament-han
Requires:       texlive-qyxf-book
Requires:       texlive-sjtutex
Requires:       texlive-suanpan-l3
Requires:       texlive-texlive-zh-cn
Requires:       texlive-texproposal
Requires:       texlive-tlmgr-intro-zh-cn
Requires:       texlive-upzhkinsoku
Requires:       texlive-xpinyin
Requires:       texlive-xtuthesis
Requires:       texlive-zhlineskip
Requires:       texlive-zhlipsum
Requires:       texlive-zhmetrics
Requires:       texlive-zhmetrics-uptex
Requires:       texlive-zhnumber
Requires:       texlive-zhspacing

%description
Support for Chinese; additional packages in collection-langcjk.


%package -n texlive-arphic
Summary:        Arphic (Chinese) font packages
Version:        svn15878
License:        Arphic-1999
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-arphic
These are font bundles for the Chinese Arphic fonts which work with the CJK
package. TrueType versions of these fonts for use with XeLaTeX and LuaLaTeX are
provided by the arphic-ttf package. Arphic is actually the name of the company
which created these fonts (and put them under a GPL-like licence).

%package -n texlive-arphic-ttf
Summary:        TrueType version of Chinese Arphic fonts
Version:        svn42675
License:        Arphic-1999
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-arphic-ttf
This package provides TrueType versions of the Chinese Arphic fonts for use
with XeLaTeX and LuaLaTeX. Type1 versions of these fonts, for use with pdfLaTeX
and the cjk package, are provided by the arphic package. Arphic is actually the
name of the company which created these fonts.

%package -n texlive-asymptote-by-example-zh-cn
Summary:        Asymptote by example
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asymptote-by-example-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asymptote-by-example-zh-cn-doc <= 11:%{version}

%description -n texlive-asymptote-by-example-zh-cn
This is a tutorial written in Simplified Chinese.

%package -n texlive-asymptote-faq-zh-cn
Summary:        Asymptote FAQ (Chinese translation)
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asymptote-faq-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asymptote-faq-zh-cn-doc <= 11:%{version}

%description -n texlive-asymptote-faq-zh-cn
This is a Chinese translation of the Asymptote FAQ

%package -n texlive-asymptote-manual-zh-cn
Summary:        A Chinese translation of the asymptote manual
Version:        svn15878
License:        LGPL-2.1-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-asymptote-manual-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-asymptote-manual-zh-cn-doc <= 11:%{version}

%description -n texlive-asymptote-manual-zh-cn
This is an (incomplete, simplified) Chinese translation of the Asymptote
manual.

%package -n texlive-cns
Summary:        Chinese/Japanese/Korean bitmap fonts
Version:        svn45677
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-cns
Fonts to go with the cjk macro package for Chinese, Japanese and Korean with
LaTeX2e. The package aims to supersede HLaTeX fonts bundle.

%package -n texlive-ctex
Summary:        LaTeX classes and packages for Chinese typesetting
Version:        svn71527
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-adobemapping
Requires:       texlive-atbegshi
Requires:       texlive-beamer
Requires:       texlive-cjk
Requires:       texlive-cjkpunct
Requires:       texlive-ec
Requires:       texlive-epstopdf-pkg
Requires:       texlive-etoolbox
Requires:       texlive-everyhook
Requires:       texlive-fandol
Requires:       texlive-fontspec
Requires:       texlive-iftex
Requires:       texlive-infwarerr
Requires:       texlive-kvoptions
Requires:       texlive-kvsetkeys
Requires:       texlive-latex-bin
Requires:       texlive-ltxcmds
Requires:       texlive-luatexja
Requires:       texlive-mptopdf
Requires:       texlive-pdftexcmds
Requires:       texlive-platex-tools
Requires:       texlive-svn-prov
Requires:       texlive-tipa
Requires:       texlive-tools
Requires:       texlive-ttfutils
Requires:       texlive-ulem
Requires:       texlive-uplatex
Requires:       texlive-xcjk2uni
Requires:       texlive-xecjk
Requires:       texlive-xetex
Requires:       texlive-xkeyval
Requires:       texlive-xpinyin
Requires:       texlive-xunicode
Requires:       texlive-zhmetrics
Requires:       texlive-zhmetrics-uptex
Requires:       texlive-zhnumber
Provides:       tex(ctex-engine-aptex.def) = %{tl_version}
Provides:       tex(ctex-engine-luatex.def) = %{tl_version}
Provides:       tex(ctex-engine-pdftex.def) = %{tl_version}
Provides:       tex(ctex-engine-uptex.def) = %{tl_version}
Provides:       tex(ctex-engine-xetex.def) = %{tl_version}
Provides:       tex(ctex-fontset-adobe.def) = %{tl_version}
Provides:       tex(ctex-fontset-fandol.def) = %{tl_version}
Provides:       tex(ctex-fontset-founder.def) = %{tl_version}
Provides:       tex(ctex-fontset-mac.def) = %{tl_version}
Provides:       tex(ctex-fontset-macnew.def) = %{tl_version}
Provides:       tex(ctex-fontset-macold.def) = %{tl_version}
Provides:       tex(ctex-fontset-ubuntu.def) = %{tl_version}
Provides:       tex(ctex-fontset-windows.def) = %{tl_version}
Provides:       tex(ctex-heading-article.def) = %{tl_version}
Provides:       tex(ctex-heading-beamer.def) = %{tl_version}
Provides:       tex(ctex-heading-book.def) = %{tl_version}
Provides:       tex(ctex-heading-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-article.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-beamer.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-book.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-article.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-beamer.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-book.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain.def) = %{tl_version}
Provides:       tex(ctex-spa-macro.tex) = %{tl_version}
Provides:       tex(ctex-spa-make.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-adobe.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-fandol.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-founder.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-mac.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-ubuntu.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-windows.tex) = %{tl_version}
Provides:       tex(ctex.sty) = %{tl_version}
Provides:       tex(ctexcap.sty) = %{tl_version}
Provides:       tex(ctexheading.sty) = %{tl_version}
Provides:       tex(ctexhook.sty) = %{tl_version}
Provides:       tex(ctexpatch.sty) = %{tl_version}
Provides:       tex(ctexsize.sty) = %{tl_version}
Provides:       tex(ctexspa.def) = %{tl_version}
Provides:       tex(ctxdocstrip.tex) = %{tl_version}

%description -n texlive-ctex
ctex is a collection of macro packages and document classes for LaTeX Chinese
typesetting.

%package -n texlive-ctex-faq
Summary:        LaTeX FAQ by the Chinese TeX Society (ctex.org)
Version:        svn15878
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ctex-faq-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ctex-faq-doc <= 11:%{version}

%description -n texlive-ctex-faq
Most questions were collected on the bbs.ctex.org forum, and were answered in
detail by the author.

%package -n texlive-exam-zh
Summary:        LaTeX template for Chinese exams
Version:        svn76834
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(exam-zh-chinese-english.sty) = %{tl_version}
Provides:       tex(exam-zh-choices.sty) = %{tl_version}
Provides:       tex(exam-zh-font.sty) = %{tl_version}
Provides:       tex(exam-zh-math.sty) = %{tl_version}
Provides:       tex(exam-zh-question.sty) = %{tl_version}
Provides:       tex(exam-zh-symbols.sty) = %{tl_version}
Provides:       tex(exam-zh-textfigure.sty) = %{tl_version}

%description -n texlive-exam-zh
Although there are already several excellent exam packages or classes like exam
and bhcexam, these do not fit the Chinese style very well, or they cannot be
customized easily for Chinese exams of all types, like exams in primary school,
junior high school, senior high school and even college. This is the main
reason why this package was created. This package provides a class exam-zh.cls
and several module packages like exam-zh-question.sty and exam-zh-choices.sty,
where these module packages can be used individually. Using exam-zh you can
separate the format and the content very well; use the choices environment to
typeset choice items easily and automatically; design the seal line easily; and
more (see manual).

%package -n texlive-fandol
Summary:        Four basic fonts for Chinese typesetting
Version:        svn37889
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-fandol
Fandol fonts designed for Chinese typesetting. The current version contains
four styles: Song, Hei, Kai, Fang. All fonts are in OpenType format.

%package -n texlive-fduthesis
Summary:        LaTeX thesis template for Fudan University
Version:        svn67231
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fdulogo.sty) = %{tl_version}
Provides:       tex(fduthesis.def) = %{tl_version}

%description -n texlive-fduthesis
This package is a LaTeX thesis template package for Fudan University. It can
make it easy to write theses both in Chinese and English.

%package -n texlive-hanzibox
Summary:        Boxed Chinese characters with Pinyin above and translation below
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(hanzibox.sty) = %{tl_version}

%description -n texlive-hanzibox
This is a LaTeX package written to simplify the input of Chinese with Hanyu
Pinyin and translation. Hanyu Pinyin is placed above Chinese with the xpinyin
package, and the translation is placed below. The package can be used as a
utility for learning to write and pronounce Chinese characters, for Chinese
character learning plans, presentations, exercise booklets and other
documentation work.

%package -n texlive-hyphen-chinese
Summary:        Chinese pinyin hyphenation patterns.
Version:        svn74115
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-zh-latn-pinyin.ec.tex) = %{tl_version}
Provides:       tex(hyph-zh-latn-pinyin.tex) = %{tl_version}
Provides:       tex(loadhyph-zh-latn-pinyin.tex) = %{tl_version}

%description -n texlive-hyphen-chinese
Hyphenation patterns for unaccented transliterated Mandarin Chinese (pinyin) in
T1/EC and UTF-8 encodings. The latter can hyphenate pinyin with or without tone
markers; the former only without.

%package -n texlive-impatient-cn
Summary:        Free edition of the book "TeX for the Impatient"
Version:        svn54080
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-impatient-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-impatient-cn-doc <= 11:%{version}

%description -n texlive-impatient-cn
"TeX for the Impatient" is a book (of around 350 pages) on TeX, Plain TeX and
Eplain. The book is also available in French and Chinese translations.

%package -n texlive-install-latex-guide-zh-cn
Summary:        A short introduction to LaTeX installation written in Chinese
Version:        svn77231
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-install-latex-guide-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-install-latex-guide-zh-cn-doc <= 11:%{version}

%description -n texlive-install-latex-guide-zh-cn
This package will introduce the operations related to installing TeX Live
(introducing MacTeX in macOS), upgrading packages, and compiling simple
documents on Windows 11, Ubuntu 24.04, and macOS systems, and mainly
introducing command line operations.

%package -n texlive-latex-notes-zh-cn
Summary:        Chinese Introduction to TeX and LaTeX
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex-notes-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex-notes-zh-cn-doc <= 11:%{version}

%description -n texlive-latex-notes-zh-cn
The document is an introduction to TeX/LaTeX, in Chinese. It covers basic text
typesetting, mathematics, graphics, tables, Chinese language & fonts, and some
miscellaneous features (hyperlinks, long documents, bibliographies, indexes and
page layout).

%package -n texlive-lshort-chinese
Summary:        Introduction to LaTeX, in Chinese
Version:        svn73160
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-chinese-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-chinese-doc <= 11:%{version}

%description -n texlive-lshort-chinese
A Chinese edition of the not so short introduction to LaTeX2e, with additional
information of typesetting Chinese language.

%package -n texlive-luatex-cn
Summary:        A LuaTeX based package to handle Chinese text typesetting
Version:        svn77432
License:        Apache-2.0
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(enumitem.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Provides:       tex(luatex-cn-banxin.sty) = %{tl_version}
Provides:       tex(luatex-cn-font-autodetect.sty) = %{tl_version}
Provides:       tex(luatex-cn-splitpage.sty) = %{tl_version}
Provides:       tex(luatex-cn-vertical.sty) = %{tl_version}
Provides:       tex(luatex-cn.sty) = %{tl_version}

%description -n texlive-luatex-cn
A LuaTeX package for Chinese character typesetting, covering
horizontal/vertical, traditional/modern layout. Currently focus on Ancient Book
replication. Implemented core logic of vertical typesetting, decorative
elements of traditional Chinese books, and interlinear notes.

%package -n texlive-lxgw-fonts
Summary:        A CJK font family with a comprehensive character set
Version:        svn77400
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(ctex-fontset-lxgw.def) = %{tl_version}
Provides:       tex(ctex-makespa-lxgw.tex) = %{tl_version}
Provides:       tex(ctex-zhmap-lxgw.tex) = %{tl_version}

%description -n texlive-lxgw-fonts
The LXGW Font Family provides an open-source CJK font family with a
comprehensive character set for Chinese (Simplified/Traditional), Cantonese,
and Japanese. A 'fontset' configuration of this font family for the 'ctex-kit'
is also provided in this package.

%package -n texlive-nanicolle
Summary:        Typesetting herbarium specimen labels
Version:        svn56224
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-nanicolle
This package provides a LaTeX class nanicolle.cls for typesetting collection
labels and identification labels in Chinese style or in western style for plant
herbarium specimens. So far, documents using this class can only be compiled
with XeLaTeX. Note: The name of the package is a compound of the Japanese
"nani" (meaning "what") and a truncated form of the English "collect", thus
expressing the ideas of identification/classification (taxonomy) and
collection.

%package -n texlive-njurepo
Summary:        Reports for Nanjing University
Version:        svn50492
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-njurepo
This LaTeX document class provides a thesis template for Nanjing University in
order to make it easy to write experiment reports and homework for the
bachelor's curriculum. NJUrepo stands for Nanjing University versatile Report.

%package -n texlive-pgfornament-han
Summary:        Pgfornament library for Chinese traditional motifs and patterns
Version:        svn72640
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(needspace.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(relsize.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Provides:       tex(beamerthemeHeavenlyClouds.sty) = %{tl_version}
Provides:       tex(beamerthemeTianQing.sty) = %{tl_version}
Provides:       tex(beamerthemeXiaoshan.sty) = %{tl_version}
Provides:       tex(cncolours.sty) = %{tl_version}
Provides:       tex(pgflibraryhan.code.tex) = %{tl_version}
Provides:       tex(pgfornament-han.sty) = %{tl_version}

%description -n texlive-pgfornament-han
This package provides a pgfornament library for Chinese traditional motifs and
patterns. The command \pgfornamenthan takes the same options as \pgfornament
from the pgfornament package, but renders Chinese traditional motifs instead.
The list of supported motifs, as well as some examples, can be found in the
accompanying documentation. This bundle also provides three beamer themes
incorporating these motifs; sample .tex files for creating beamer presentations
and posters are included. Yi pgfornament Hong Bao De Ji Zhi ,Shi Xian Hui Zhi
Yi Feng Tu Wen . \pgfornamenthan He \pgfornament De Can Shu Shi Yi Yang De ;
Bian Yi De Chu Lai De Dang Ran Shi Yi Feng Wen Yang Liao . Hong Bao Shou Ce Li
You Wan Zheng De Wen Yang Lie Biao Yi Ji Shi Yong Fan Li . Wo Men Ye Ji Yu Zhe
Xie Wen Yang ,Kai Fa Liao San Kuan beamerZhu Ti , Bing Fu Shang Zhi Zuo
beamerHuan Deng Pian He Hai Bao De Shi Fan .texWen Dang .

%package -n texlive-qyxf-book
Summary:        Book Template for Qian Yuan Xue Fu
Version:        svn75712
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-qyxf-book
qyxf-book is a LaTeX document class (template) developed by Qian Yuan Xue Fu
(QYXF), a student club of Xi'an Jiaotong University (XJTU). Up to now, this
template has been applied to academic counselling material ("course helpers")
written by members of QYXF, including Solutions to University Physics Notes on
Computing Methods Features of the template: Minimalistic document style, as
preferred for "course helpers". Several color schemes are offered, and it is
easy to customize your own scheme. Simple interfaces for users to customize the
style of preface, main part and so on. Currently the template is only designed
for Chinese typesetting.

%package -n texlive-sjtutex
Summary:        LaTeX classes for Shanghai Jiao Tong University
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(sjtu-cjk-font-adobe.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-fandol.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-founder.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-hanyi.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-mac.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-ubuntu.def) = %{tl_version}
Provides:       tex(sjtu-cjk-font-windows.def) = %{tl_version}
Provides:       tex(sjtu-lang-de.def) = %{tl_version}
Provides:       tex(sjtu-lang-en.def) = %{tl_version}
Provides:       tex(sjtu-lang-ja.def) = %{tl_version}
Provides:       tex(sjtu-lang-zh.def) = %{tl_version}
Provides:       tex(sjtu-math-font-cambria.def) = %{tl_version}
Provides:       tex(sjtu-math-font-libertinus.def) = %{tl_version}
Provides:       tex(sjtu-math-font-lm.def) = %{tl_version}
Provides:       tex(sjtu-math-font-newcm.def) = %{tl_version}
Provides:       tex(sjtu-math-font-newpx.def) = %{tl_version}
Provides:       tex(sjtu-math-font-newtx.def) = %{tl_version}
Provides:       tex(sjtu-math-font-stixtwo.def) = %{tl_version}
Provides:       tex(sjtu-math-font-times.def) = %{tl_version}
Provides:       tex(sjtu-math-font-xits.def) = %{tl_version}
Provides:       tex(sjtu-scheme-de.def) = %{tl_version}
Provides:       tex(sjtu-scheme-en.def) = %{tl_version}
Provides:       tex(sjtu-scheme-ja.def) = %{tl_version}
Provides:       tex(sjtu-scheme-zh.def) = %{tl_version}
Provides:       tex(sjtu-text-font-cambria.def) = %{tl_version}
Provides:       tex(sjtu-text-font-libertinus.def) = %{tl_version}
Provides:       tex(sjtu-text-font-lm.def) = %{tl_version}
Provides:       tex(sjtu-text-font-newcm.def) = %{tl_version}
Provides:       tex(sjtu-text-font-newpx.def) = %{tl_version}
Provides:       tex(sjtu-text-font-newtx.def) = %{tl_version}
Provides:       tex(sjtu-text-font-stixtwo.def) = %{tl_version}
Provides:       tex(sjtu-text-font-times.def) = %{tl_version}
Provides:       tex(sjtu-text-font-xits.def) = %{tl_version}
Provides:       tex(sjtu-thesis-de.def) = %{tl_version}
Provides:       tex(sjtu-thesis-en.def) = %{tl_version}
Provides:       tex(sjtu-thesis-ja.def) = %{tl_version}
Provides:       tex(sjtu-thesis-zh.def) = %{tl_version}

%description -n texlive-sjtutex
SJTUTeX aims to establish a simple and easy-to-use collection of document
classes for Shanghai Jiao Tong University, including the thesis document class
sjtuthesis, as well as the regular document classes sjtuarticle and sjtureport.

%package -n texlive-suanpan-l3
Summary:        Traditional Chinese 7-bids suanpan (abacus) package based on l3draw
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(suanpan-l3.sty) = %{tl_version}

%description -n texlive-suanpan-l3
This traditional Chinese 7-bids abacus drawing package utilizes l3draw and is
developed with expl3. It can effectively manage both upper and lower bids,
while also considering bottom bid, top bid, and hanging bid. The package offers
a unique environment for drawing abacuses, denoted as suanpan. Within this
environment, 7 specialized macros are available for the creation of abacuses.
The \rod macro is used to lay out a single rod, while the \rod* macro draws a
counting point on this rod's beam. The \rods macro is capable of laying out a
set of rods. The \bid macro colors the specified bid. The \bids macro colors
all inner bids that are near the beam, while the \bids* macro colors all outer
bids that are far from the beam. Lastly, the \lrframe macro is used to lay out
the left and right frames of an abacus. At the same time, the package offers
customization options for abacus, including line width, draw color, fill color,
bid space, rod space, etc. These can be configured through package options,
suanpan environment options, or the \suanpanset macro.

%package -n texlive-texlive-zh-cn
Summary:        TeX Live manual (Chinese)
Version:        svn74098
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-zh-cn-doc <= 11:%{version}

%description -n texlive-texlive-zh-cn
TeX Live manual (Chinese)

%package -n texlive-texproposal
Summary:        A proposal prototype for LaTeX promotion in Chinese universities
Version:        svn43151
License:        CC-BY-4.0 AND MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texproposal-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texproposal-doc <= 11:%{version}

%description -n texlive-texproposal
This package contains the original source code and necessary attachment of the
document "Proposal for Offering TeX Courses and Relevant Resources in Chongqing
University". This proposal could be helpful if one is considering to suggest
his/her university or company to use TeX (or LaTeX, or XeLaTeX) as a
typesetting system, especially for Chinese universities and companies. The
present proposal mainly explains the importance and necessity of introducing
TeX, a typesetting system often used in academic writing, to students and
teachers. This proposal starts from a brief introduction of TeX, then steps
further into its fascinating application to academic writing and dissertation
formatting. Finally, a set of possible implementation strategies with regard to
the proper introduction of TeX and relevant resources to our university, is
proposed.

%package -n texlive-tlmgr-intro-zh-cn
Summary:        A short tutorial on using tlmgr in Chinese
Version:        svn59100
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tlmgr-intro-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tlmgr-intro-zh-cn-doc <= 11:%{version}

%description -n texlive-tlmgr-intro-zh-cn
This is a Chinese translation of the tlmgr documentation. It introduces some of
the common usage of the TeX Live Manager. The original can be found in the
tlmgrbasics package.

%package -n texlive-upzhkinsoku
Summary:        Supplementary Chinese kinsoku for Unicode *pTeX
Version:        svn47354
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(upzhkinsoku.sty) = %{tl_version}

%description -n texlive-upzhkinsoku
This package provides supplementary Chinese kinsoku (line breaking rules etc.)
settings for Unicode (e-)upTeX (when using Unicode as its internal encoding),
and ApTeX. Both LaTeX and plain TeX are supported.

%package -n texlive-xpinyin
Summary:        Automatically add pinyin to Chinese characters
Version:        svn76924
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xpinyin-database.def) = %{tl_version}
Provides:       tex(xpinyin.sty) = %{tl_version}

%description -n texlive-xpinyin
The package is written to simplify the input of Hanyu Pinyin. Macros are
provided that automatically add pinyin to Chinese characters.

%package -n texlive-xtuthesis
Summary:        XTU thesis template
Version:        svn47049
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amscd.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(caption.sty)
Requires:       tex(cite.sty)
Requires:       tex(color.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(diagbox.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(xtuformat.sty) = %{tl_version}

%description -n texlive-xtuthesis
The package provides a thesis template for the Xiangtan University.

%package -n texlive-zhlineskip
Summary:        Line spacing for CJK documents
Version:        svn51142
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xintexpr.sty)
Provides:       tex(zhlineskip.sty) = %{tl_version}

%description -n texlive-zhlineskip
This package supports typesetting CJK documents. It allows users to specify the
two ratios between the leading and the font size of the body text and the
footnote text. For CJK typesetting, these ratios usually range from 1.5 to
1.67. This package is also capable of restoring the math leading to that of the
Latin text (usually 1.2 times the font size). Finally, it is possible to
achieve the Microsoft Word multiple line spacing style using zhlineskip.

%package -n texlive-zhlipsum
Summary:        Chinese dummy text
Version:        svn54994
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zhlipsum-big5.def) = %{tl_version}
Provides:       tex(zhlipsum-gbk.def) = %{tl_version}
Provides:       tex(zhlipsum-utf8.def) = %{tl_version}
Provides:       tex(zhlipsum.sty) = %{tl_version}

%description -n texlive-zhlipsum
This package provides an interface to dummy text in Chinese language, which
will be useful for testing Chinese documents. UTF-8, GBK and Big5 encodings are
supported.

%package -n texlive-zhmetrics
Summary:        TFM subfont files for using Chinese fonts in 8-bit TeX
Version:        svn22207
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zhwinfonts.tex) = %{tl_version}

%description -n texlive-zhmetrics
These are metrics to use existing Chinese TrueType fonts in workflows that use
LaTeX & dvipdfmx, or pdfLaTeX. The fonts themselves are not included in the
package. Six font families are supported: kai, song, lishu, fangsong, youyuan
and hei. Two encodings (GBK and UTF-8) are supported.

%package -n texlive-zhmetrics-uptex
Summary:        Chinese font metrics for upTeX
Version:        svn40728
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-zhmetrics-uptex
The package contains some Chinese font metrics (JFM, VF, etc) for upTeX engine,
together with a simple DVIPDFMx font mapping of Fandol fonts for DVIPDFMx.

%package -n texlive-zhnumber
Summary:        Typeset Chinese representations of numbers
Version:        svn66115
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(zhnumber.sty) = %{tl_version}

%description -n texlive-zhnumber
The package provides commands to typeset Chinese representations of numbers.
The main difference between this package and CJKnumb is that the commands
provided are expandable in the 'proper' way.

%package -n texlive-zhspacing
Summary:        Spacing for mixed CJK-English documents in XeTeX
Version:        svn41145
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(fontspec.sty)
Requires:       tex(ulem.sty)
Provides:       tex(t-zhspacing.tex) = %{tl_version}
Provides:       tex(zhfont.sty) = %{tl_version}
Provides:       tex(zhmath.sty) = %{tl_version}
Provides:       tex(zhsmyclass.sty) = %{tl_version}
Provides:       tex(zhspacing.sty) = %{tl_version}
Provides:       tex(zhsusefulmacros.sty) = %{tl_version}
Provides:       tex(zhulem.sty) = %{tl_version}

%description -n texlive-zhspacing
The package manages spacing in a CJK document; between consecutive Chinese
letters, spaces are ignored, but a consistent space is inserted between Chinese
text and English (or mathematics). The package may be used by any document
format under XeTeX.

%post -n texlive-hyphen-chinese
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/pinyin.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "pinyin loadhyph-zh-latn-pinyin.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{pinyin}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-chinese
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/pinyin.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{pinyin}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%prep
# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

mkdir -p %{buildroot}%{_datadir}/fonts
mkdir -p %{buildroot}%{_datadir}/appdata

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

# Install AppStream metadata for font components
cp %{SOURCE75} %{buildroot}%{_datadir}/appdata/

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Create symlinks for OpenType fonts
ln -sf %{_texmf_main}/fonts/opentype/public/fandol %{buildroot}%{_datadir}/fonts/fandol

# Apply xtuthesis patch
pushd %{buildroot}%{_texmf_main}
patch -p0 < %{_sourcedir}/texlive-xtuthesis-use-diagbox.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Validate AppData files
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.metainfo.xml

# Main collection metapackage (empty)
%files

%files -n texlive-arphic
%license other-free.txt
%{_texmf_main}/dvips/arphic/
%{_texmf_main}/fonts/afm/arphic/bkaiu/
%{_texmf_main}/fonts/afm/arphic/bsmiu/
%{_texmf_main}/fonts/afm/arphic/gbsnu/
%{_texmf_main}/fonts/afm/arphic/gkaiu/
%{_texmf_main}/fonts/map/dvips/arphic/
%{_texmf_main}/fonts/tfm/arphic/bkaimp/
%{_texmf_main}/fonts/tfm/arphic/bkaiu/
%{_texmf_main}/fonts/tfm/arphic/bsmilp/
%{_texmf_main}/fonts/tfm/arphic/bsmiu/
%{_texmf_main}/fonts/tfm/arphic/gbsnlp/
%{_texmf_main}/fonts/tfm/arphic/gbsnu/
%{_texmf_main}/fonts/tfm/arphic/gkaimp/
%{_texmf_main}/fonts/tfm/arphic/gkaiu/
%{_texmf_main}/fonts/type1/arphic/bkaiu/
%{_texmf_main}/fonts/type1/arphic/bsmiu/
%{_texmf_main}/fonts/type1/arphic/gbsnu/
%{_texmf_main}/fonts/type1/arphic/gkaiu/
%{_texmf_main}/fonts/vf/arphic/bkaimp/
%{_texmf_main}/fonts/vf/arphic/bsmilp/
%{_texmf_main}/fonts/vf/arphic/gbsnlp/
%{_texmf_main}/fonts/vf/arphic/gkaimp/
%doc %{_texmf_main}/doc/fonts/arphic/

%files -n texlive-arphic-ttf
%license other-free.txt
%{_texmf_main}/fonts/truetype/public/arphic-ttf/
%doc %{_texmf_main}/doc/fonts/arphic-ttf/

%files -n texlive-asymptote-by-example-zh-cn
%license gpl2.txt
%doc %{_texmf_main}/doc/support/asymptote-by-example-zh-cn/

%files -n texlive-asymptote-faq-zh-cn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/support/asymptote-faq-zh-cn/

%files -n texlive-asymptote-manual-zh-cn
%license lgpl2.1.txt
%doc %{_texmf_main}/doc/support/asymptote-manual-zh-cn/

%files -n texlive-cns
%license pd.txt
%{_texmf_main}/fonts/misc/cns/
%{_texmf_main}/fonts/tfm/cns/c0so12/
%{_texmf_main}/fonts/tfm/cns/c1so12/
%{_texmf_main}/fonts/tfm/cns/c2so12/
%{_texmf_main}/fonts/tfm/cns/c3so12/
%{_texmf_main}/fonts/tfm/cns/c4so12/
%{_texmf_main}/fonts/tfm/cns/c5so12/
%{_texmf_main}/fonts/tfm/cns/c6so12/
%{_texmf_main}/fonts/tfm/cns/c7so12/
%doc %{_texmf_main}/doc/fonts/cns/

%files -n texlive-ctex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/ctex/
%{_texmf_main}/tex/latex/ctex/
%{_texmf_main}/tex/luatex/ctex/
%doc %{_texmf_main}/doc/latex/ctex/

%files -n texlive-ctex-faq
%license fdl.txt
%doc %{_texmf_main}/doc/latex/ctex-faq/

%files -n texlive-exam-zh
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/exam-zh/
%doc %{_texmf_main}/doc/xelatex/exam-zh/

%files -n texlive-fandol
%license gpl2.txt
%{_texmf_main}/fonts/opentype/public/fandol/
%doc %{_texmf_main}/doc/fonts/fandol/
%{_datadir}/fonts/fandol
%{_datadir}/appdata/fandol.metainfo.xml

%files -n texlive-fduthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fduthesis/
%doc %{_texmf_main}/doc/latex/fduthesis/

%files -n texlive-hanzibox
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/hanzibox/
%doc %{_texmf_main}/doc/xelatex/hanzibox/

%files -n texlive-hyphen-chinese
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-impatient-cn
%license fdl.txt
%doc %{_texmf_main}/doc/plain/impatient-cn/

%files -n texlive-install-latex-guide-zh-cn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/install-latex-guide-zh-cn/

%files -n texlive-latex-notes-zh-cn
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/generic/latex-notes-zh-cn/

%files -n texlive-lshort-chinese
%license fdl.txt
%doc %{_texmf_main}/doc/latex/lshort-chinese/

%files -n texlive-luatex-cn
%license apache2.txt
%{_texmf_main}/tex/lualatex/luatex-cn/
%doc %{_texmf_main}/doc/latex/luatex-cn/

%files -n texlive-lxgw-fonts
%license ofl.txt
%{_texmf_main}/fonts/truetype/public/lxgw-fonts/
%{_texmf_main}/tex/latex/lxgw-fonts/
%doc %{_texmf_main}/doc/fonts/lxgw-fonts/

%files -n texlive-nanicolle
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/nanicolle/
%doc %{_texmf_main}/doc/xelatex/nanicolle/

%files -n texlive-njurepo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/njurepo/
%doc %{_texmf_main}/doc/latex/njurepo/

%files -n texlive-pgfornament-han
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/pgfornament-han/
%doc %{_texmf_main}/doc/latex/pgfornament-han/

%files -n texlive-qyxf-book
%license mit.txt
%{_texmf_main}/tex/latex/qyxf-book/
%doc %{_texmf_main}/doc/latex/qyxf-book/

%files -n texlive-sjtutex
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/sjtutex/
%doc %{_texmf_main}/doc/latex/sjtutex/

%files -n texlive-suanpan-l3
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/suanpan-l3/
%doc %{_texmf_main}/doc/latex/suanpan-l3/

%files -n texlive-texlive-zh-cn
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-zh-cn/

%files -n texlive-texproposal
%license cc-by-4.txt
%license mit.txt
%doc %{_texmf_main}/doc/latex/texproposal/

%files -n texlive-tlmgr-intro-zh-cn
%license gpl3.txt
%doc %{_texmf_main}/doc/support/tlmgr-intro-zh-cn/

%files -n texlive-upzhkinsoku
%license knuth.txt
%{_texmf_main}/tex/generic/upzhkinsoku/
%doc %{_texmf_main}/doc/generic/upzhkinsoku/

%files -n texlive-xpinyin
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xpinyin/
%doc %{_texmf_main}/doc/latex/xpinyin/

%files -n texlive-xtuthesis
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xtuthesis/
%doc %{_texmf_main}/doc/latex/xtuthesis/

%files -n texlive-zhlineskip
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zhlineskip/
%doc %{_texmf_main}/doc/latex/zhlineskip/

%files -n texlive-zhlipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zhlipsum/
%doc %{_texmf_main}/doc/latex/zhlipsum/

%files -n texlive-zhmetrics
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/zhmetrics/cyberb/
%{_texmf_main}/fonts/tfm/zhmetrics/gbk/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkfs/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkhei/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkkai/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkli/
%{_texmf_main}/fonts/tfm/zhmetrics/gbksong/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkyou/
%{_texmf_main}/fonts/tfm/zhmetrics/unifs/
%{_texmf_main}/fonts/tfm/zhmetrics/unihei/
%{_texmf_main}/fonts/tfm/zhmetrics/unikai/
%{_texmf_main}/fonts/tfm/zhmetrics/unili/
%{_texmf_main}/fonts/tfm/zhmetrics/unisong/
%{_texmf_main}/fonts/tfm/zhmetrics/uniyou/
%{_texmf_main}/tex/generic/zhmetrics/
%{_texmf_main}/tex/latex/zhmetrics/
%doc %{_texmf_main}/doc/fonts/zhmetrics/

%files -n texlive-zhmetrics-uptex
%license lppl1.3c.txt
%{_texmf_main}/fonts/tfm/public/zhmetrics-uptex/
%{_texmf_main}/fonts/vf/public/zhmetrics-uptex/
%doc %{_texmf_main}/doc/fonts/zhmetrics-uptex/

%files -n texlive-zhnumber
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/zhnumber/
%doc %{_texmf_main}/doc/latex/zhnumber/

%files -n texlive-zhspacing
%license lppl1.3c.txt
%{_texmf_main}/tex/context/third/
%{_texmf_main}/tex/generic/zhspacing/
%{_texmf_main}/tex/xelatex/zhspacing/
%doc %{_texmf_main}/doc/generic/zhspacing/

%changelog
* Sun Feb 08 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn77432-4
- Update to svn77432, fix licensing files

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 12:svn76973-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jan 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76973-2
- fix Knuth licensing
- validate appdata files

* Wed Jan 14 2026 Tom Callaway <spot@fedoraproject.org> - 12:svn76973-1
- Update to svn76973
- fix descriptions, update components, new component

* Wed Oct 08 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72136-2
- regen, no deps from docs

* Wed Sep 17 2025 Tom Callaway <spot@fedoraproject.org> - 12:svn72136-1
- Update to TeX Live 2025
