# When bootstrapping a new architecture, there is no gap-pkg-io package yet,
# since it requires this package to build.  This package can be built without
# gap-pkg-io, but needs it for completeness.  Use the following procedure:
# 1. Do a bootstrap build of this package
# 2. Build gap-pkg-autodoc in bootstrap mode
# 3. Build gap-pkg-io
# 4. Do a normal build of this packages, which builds the documentation
# 5. Build gap-pkg-autodoc in non-bootstrap mode
%bcond bootstrap 0

# The tests require gap-pkg-browse, which is not available in the bootstrap
# process until well after we build the non-bootstrap GAPDoc.  Use this to
# enable the tests later.
%bcond test 0

Name:           GAPDoc
Version:        1.6.7
Release:        %autorelease
Summary:        GAP documentation tool

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/
VCS:            git:https://github.com/frankluebeck/GAPDoc.git
Source:         %{url}/%{name}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  ghostscript
BuildRequires:  libxml2
BuildRequires:  tex(amssym.tex)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(english.ldf)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(grfext.sty)
BuildRequires:  tex(pslatex.sty)
BuildRequires:  tex(psnfss.map)
BuildRequires:  tex(tex)
BuildRequires:  tex-cm-super
BuildRequires:  tex-ec
BuildRequires:  tex-helvetic
BuildRequires:  tex-latex-bin
BuildRequires:  tex-rsfs
BuildRequires:  tex-symbol
BuildRequires:  tex-times

Requires:       gap-core
# For xmllint
Requires:       libxml2

%if %{without bootstrap}
BuildRequires:  gap-pkg-io-doc
Requires:       gap-pkg-io
%endif

%if %{with test}
BuildRequires:  gap-pkg-browse
%endif

Provides:       gap-pkg-gapdoc = %{version}-%{release}

%description
This package describes a document format for writing GAP documentation.

The idea is to define a sufficiently abstract markup language for GAP
documentation which can be (relatively easily) converted into different
output formats.  We used XML to define such a language.

This package provides:
- Utilities to use the documentation which is written in GAPDoc format
  with the GAP help system.  If you don't want to write your own
  (package) documentation you can skip to the last point of this list.
- The description of a markup language for GAP documentation (which is
  defined using the XML standard).
- Three example documents using this language: The GAPDoc documentation
  itself, a short example which demonstrates all constructs defined in
  the GAPDoc language, and a very short example explained in the
  introduction of the main documentation.
- A mechanism for distributing documentation among several files,
  including source code files.
- GAP programs (written by the first named author) which produce from
  documentation written in the GAPDoc language several document formats:
  * text format with color markup for onscreen browsing.
  * LaTeX format and from this PDF- (and DVI)-versions with hyperlinks.
  * HTML (XHTML 1.0 strict) format for reading with a Web-browser (and
    many hooks for CSS layout).
- Utility GAP programs which are used for the above but can be of
  independent interest as well:
  * Unicode strings with translations to and from other encodings
  * further utilities for manipulating strings
  * tools for dealing with BibTeX data
  * another data format BibXMLext for bibliographical data including
    tools to manipulate/translate them
  * a tool ComposedDocument for composing documents which are
    distributed in many files

%package latex
Summary:        All LaTeX dependencies for GAPDoc
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       ghostscript
Requires:       tex(amssym.tex)
Requires:       tex(color.sty)
Requires:       tex(english.ldf)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(geometry.sty)
Requires:       tex(grfext.sty)
Requires:       tex(pslatex.sty)
Requires:       tex(psnfss.map)
Requires:       tex(tex)
Requires:       tex-cm-super
Requires:       tex-ec
Requires:       tex-helvetic
Requires:       tex-latex-bin
Requires:       tex-rsfs
Requires:       tex-symbol
Requires:       tex-times

# Needed to fetch BibTeX entries from MathSciNet
Suggests:       gap-pkg-io

%description latex
This package contains all of the LaTeX dependencies for GAPDoc.  GAP
proper requires that the GAP portions of GAPDoc be installed; it
refuses to start otherwise.  However, if GAPDoc is not actively used,
then dragging in all of the LaTeX dependencies is wasteful.  Install
this package to pull in all of the necessary LaTeX dependencies for
building GAP package documentation.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        GAPDoc documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%if %{without bootstrap}
Requires:       gap-pkg-io-doc
%endif

%description doc
This package contains documentation for GAPDoc.

%prep
%autosetup

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir ../pkg
ln -s ../GAPDoc-%{version} ../pkg
gap -l "$PWD/..;" --bare -c 'LoadPackage("GAPDoc");' makedocrel.g
rm -fr ../../doc ../pkg

# Remove build paths
sed -i "s|$PWD/..|%{gap_libdir}|g" doc/*.html example/*.html

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/GAPDoc/{3k+1,doc,example}
cp -a *.{dtd,g} lib styles tst version %{buildroot}%{gap_libdir}/pkg/GAPDoc
%gap_copy_docs -n GAPDoc
%gap_copy_docs -n GAPDoc -d 3k+1
%gap_copy_docs -n GAPDoc -d example
# Link, rather than copy, the style files
for fil in %{gapdoc_files}; do
  for dir in 3k+1 doc example; do
    path=%{buildroot}%{gap_libdir}/pkg/GAPDoc/$dir/$fil
    rm -f $path
    ln -s ../styles/$fil $path
  done
done

%if %{with test}
%check
mkdir ../pkg
ln -s ../%{name}-%{version} ../pkg
gap -l "$PWD/..;" << EOF
LoadPackage( "Browse" );
GAP_EXIT_CODE( Test( "tst/test.tst" ) );
EOF
rm -fr ../pkg
%endif

%files
%doc CHANGES README.md
%license GPL
%dir %{gap_libdir}/pkg/%{name}/
%{gap_libdir}/pkg/%{name}/*.dtd
%{gap_libdir}/pkg/%{name}/*.g
%{gap_libdir}/pkg/%{name}/lib/
%{gap_libdir}/pkg/%{name}/styles/
%{gap_libdir}/pkg/%{name}/tst/
%{gap_libdir}/pkg/%{name}/version

%files latex
# This is a metapackage to pull in dependencies only

%files doc
%docdir %{gap_libdir}/pkg/%{name}/3k+1/
%docdir %{gap_libdir}/pkg/%{name}/doc/
%docdir %{gap_libdir}/pkg/%{name}/example/
%{gap_libdir}/pkg/%{name}/3k+1/
%{gap_libdir}/pkg/%{name}/doc/
%{gap_libdir}/pkg/%{name}/example/

%changelog
%autochangelog
