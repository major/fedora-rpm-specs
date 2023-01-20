# When bootstrapping a new architecture, there is no gap-pkg-io package yet,
# since it requires this package to build.  This package can be built without
# gap-pkg-io, but needs it for completeness.  Use the following procedure:
# 1. Do a bootstrap build of this package
# 2. Build gap-pkg-autodoc in bootstrap mode
# 3. Build gap-pkg-io
# 4. Do a normal build of this packages, which builds the documentation
# 5. Build gap-pkg-autodoc in non-bootstrap mode
%bcond_with bootstrap

# The tests require gap-pkg-browse, which is not available in the bootstrap
# process until well after we build the non-bootstrap GAPDoc.  Use this to
# enable the tests later.
%bcond_with test

Name:           GAPDoc
Version:        1.6.6
Release:        5%{?dist}
Summary:        GAP documentation tool

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/
Source0:        %{url}/%{name}-%{version}.tar.bz2

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
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir ../pkg
ln -s ../GAPDoc-%{version} ../pkg
%if %{with bootstrap}
gap -l "$PWD/..;" --bare makedocrel.g
%else
gap -l "$PWD/..;" --bare -c 'LoadPackage("GAPDoc");' makedocrel.g
%endif
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
export LC_ALL=C.UTF-8
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
%{gap_libdir}/pkg/%{name}/
%exclude %{gap_libdir}/pkg/%{name}/3k+1/
%exclude %{gap_libdir}/pkg/%{name}/doc/
%exclude %{gap_libdir}/pkg/%{name}/example/

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
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.6.6-4
- Update for split GAP directories
- Add dependency on grfext.sty for TeXLive 2022 compatibility

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.6.6-3
- Use upstream's method of bootstrapping
- Clarify license of the doc subpackage

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 1.6.6-3
- Update for gap 4.12.0
- Add conditionally-enabled %%check script

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.6.6-2
- Convert License tag to SPDX
- Drop license tags for no longer bundled mathml files

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.6.6-1
- Version 1.6.6
- Add dependency on libxml2 for xmllint

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan  7 2022 Jerry James <loganjerry@gmail.com> - 1.6.5-1
- Version 1.6.5
- gap-pkg-io is now needed for non-bootstrap builds

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Jerry James <loganjerry@gmail.com> - 1.6.4-4
- Version 1.6.4

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- New upstream version

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.6.2-3
- Rebuild for GAP 4.10.0
- Change BRs and Rs due to recent TeXLive packaging changes
- Create -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 1.6.2-1
- New upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 1.6.1-4
- Require tex(pdftex.map) also so PostScript fonts can be generated

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 1.6.1-3
- Require metafont as well to generate fonts as needed

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 1.6.1-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-11
- Adjust dependencies for the latest texlive

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-10
- Rebuild for gap 4.8.3
- Split out LaTeX dependencies into a -latex subpackage

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.5.1-8
- Minimize LaTeX dependencies
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Jerry James <loganjerry@gmail.com> - 1.5.1-6
- Fix scriptlets so they don't complain when uninstalling
- Use license macro

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Jerry James <loganjerry@gmail.com> - 1.5.1-2
- Rebuild to fix _gap_dir expansion issue

* Thu Sep 13 2012 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version

* Mon Aug 20 2012 Jerry James <loganjerry@gmail.com> - 1.3-2
- Fix line endings in some mathml files

* Tue Jan 31 2012 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
