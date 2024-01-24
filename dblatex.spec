Name:       dblatex
Version:    0.3.12
Release:    %autorelease
Summary:    DocBook to LaTeX/ConTeXt Publishing
BuildArch:  noarch
# Most of package is GPLv2+, except:
# xsl/ directory is DMIT
# lib/dbtexmf/core/sgmlent.txt is Public Domain
# latex/misc/enumitem.sty, multirow2.sry and ragged2e.sty are LPPL
# latex/misc/lastpage.sty is GPLv2 (no +)
# latex/misc/passivetex is MIT (not included in binary RPM so not listed)
License:    GPL-2.0-or-later AND GPL-2.0-only AND LPPL-1.3a AND LicenseRef-DMIT AND LicenseRef-Fedora-Public-Domain
URL:        http://dblatex.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}3-%{version}.tar.bz2
# Source1 is from http://docbook.sourceforge.net/release/xsl/current/COPYING
Source1:    COPYING-docbook-xsl
Patch0:     dblatex-0.3.11-disable-debian.patch
Patch1:     dblatex-0.3.11-which-shutil.patch
Patch2:     dblatex-0.3.11-replace-inkscape-by-rsvg.patch
# Patch3 sent upstream: https://sourceforge.net/p/dblatex/patches/12/
Patch3:     dblatex-0.3.12-replace-imp-by-importlib.patch
# Patch4 sent upstream: https://sourceforge.net/p/dblatex/patches/13/
Patch4:     dblatex-0.3.12-adjust-submodule-imports.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libxslt
BuildRequires:  texlive-base
BuildRequires:  texlive-collection-latex
BuildRequires:  texlive-collection-xetex
BuildRequires:  texlive-xmltex-bin
BuildRequires:  texlive-anysize
BuildRequires:  texlive-appendix
BuildRequires:  texlive-changebar
BuildRequires:  texlive-fancybox
BuildRequires:  texlive-jknapltx
BuildRequires:  texlive-multirow
BuildRequires:  texlive-overpic
BuildRequires:  texlive-passivetex
BuildRequires:  texlive-pdfpages
BuildRequires:  texlive-subfigure
BuildRequires:  texlive-stmaryrd
BuildRequires:  texlive-wasysym
Requires:       texlive-base
Requires:       texlive-collection-latex
Requires:       texlive-collection-xetex
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-xmltex texlive-xmltex-bin
Requires:       texlive-anysize
Requires:       texlive-appendix
Requires:       texlive-bibtopic
Requires:       texlive-changebar
Requires:       texlive-ec
Requires:       texlive-fancybox
Requires:       texlive-jknapltx
Requires:       texlive-multirow
Requires:       texlive-overpic
Requires:       texlive-passivetex
Requires:       texlive-pdfpages
Requires:       texlive-subfigure
Requires:       texlive-stmaryrd
Requires:       texlive-wasysym
Requires:       texlive-xmltex-bin
Requires:       libxslt docbook-dtds
Recommends:     ImageMagick
Recommends:     texlive-epstopdf-bin
Recommends:     transfig
Recommends:     librsvg2-tools

%description
dblatex is a program that transforms your SGML/XMLDocBook
documents to DVI, PostScript or PDF by translating them
into pure LaTeX as a first process.  MathML 2.0 markups
are supported, too. It started as a clone of DB2LaTeX.

Authors:
--------
   Benoît Guillon <marsgui at users dot sourceforge dot net>
   Andreas Hoenen <andreas dot hoenen at arcor dot de>


%prep
%autosetup -n %{name}3-%{version} -p 1

rm -rf lib/contrib
%py3_shebang_fix .

%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --root $RPM_BUILD_ROOT
%py3_shebang_fix $RPM_BUILD_ROOT%{_bindir}/dblatex

# these are already in tetex-latex:
for file in bibtopic.sty enumitem.sty ragged2e.sty passivetex/ xelatex/; do
  rm -rf $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/misc/$file
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex
for file in ` find $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/ -name '*.sty' ` ; do
  mv $file $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/`basename $file`;
done

## also move .xetex files
for file in ` find $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/ -name '*.xetex' ` ; do
  mv $file $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/`basename $file`;
done

rmdir $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/{misc,contrib/example,style}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dblatex
# shipped in %%docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/

sed -e 's/\r//' xsl/mathml2/README > README-xsltml
touch -r xsl/mathml2/README README-xsltml
cp -p %{SOURCE1} COPYING-docbook-xsl


%files
%{_mandir}/man1/dblatex.1*
%doc COPYRIGHT docs/manual.pdf COPYING-docbook-xsl README-xsltml
%{python3_sitelib}/dbtexmf/
%{python3_sitelib}/dblatex-*.egg-info
%{_bindir}/dblatex
%{_datadir}/dblatex/
%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/
%dir %{_sysconfdir}/dblatex

%post -p /usr/bin/texhash

%postun -p /usr/bin/texhash

%changelog
%autochangelog
