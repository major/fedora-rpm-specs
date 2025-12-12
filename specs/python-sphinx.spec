# When bootstrapping sphinx in Fedora, we don't yet have sphinxcontrib-*
# Without the packages, we have warnings in docs, but it's not a hard dependency
# We don't want to support sphinxcontrib-* in RHEL, hence disabling the dependencies
%bcond sphinxcontrib %{undefined rhel}
# RHEL does not include python3-snowballstemmer (SRPM: snowball)
%bcond snowballstemmer %{undefined rhel}
# Also, we don't have all the tests requirements
%bcond tests 1

# Unset -s on python shebang to allow RPM-installed sphinx to be used
# with user-installed modules (#1903763)
%undefine _py3_shebang_s

# No internet in Koji
%bcond internet 0

# Build without BuildRequires ImageMagick, to skip imgconverter tests
%bcond imagemagick_tests %{undefined rhel}

# During texlive updates, sometimes the latex environment is unstable
# NOTE: LaTeX tests are never run when building for ELN.
%bcond latex_tests 1

Name:       python-sphinx
%global     general_version 8.2.3
#global     prerel ...
%global     upstream_version %{general_version}%{?prerel}
Version:    %{general_version}%{?prerel:~%{prerel}}
Release:    %autorelease
Epoch:      1
Summary:    Python documentation generator

# Unless otherwise noted, the license for code is BSD-2-Clause
# sphinx/themes/haiku/static/haiku.css_t has bits licensed with MIT
License:    BSD-2-Clause AND MIT

URL:        https://www.sphinx-doc.org/
Source:     %{pypi_source sphinx %{upstream_version}}

# Allow extra themes to exist. We pull in python3-sphinx-theme-alabaster
# which causes that test to fail.
Patch:      sphinx-test_theming.patch

# Make the first party extensions optional
# This removes the runtime dependencies on:
#  - sphinxcontrib.applehelp
#  - sphinxcontrib.devhelp
#  - sphinxcontrib.jsmath
#  - sphinxcontrib.htmlhelp
#  - sphinxcontrib.serializinghtml
#  - sphinxcontrib.qthelp
# The majority of Fedora RPM packages does not need any of those.
# By removing the dependencies, we minimize the stuff that's pulled into
# the buildroots of 700+ of packages.
#
# This is a downstream-only change - rejected upstream.
# https://github.com/sphinx-doc/sphinx/pull/11747
Patch:      Make-the-first-party-extensions-optional.patch

# Compatibility with Python 3.14
Patch:      https://github.com/sphinx-doc/sphinx/commit/8962398b761c3d85a.patch
Patch:      https://github.com/sphinx-doc/sphinx/commit/e01e42f5fc738815b.patch
Patch:      https://github.com/sphinx-doc/sphinx/pull/13527.patch
# Compatibility with docutils 0.22+
Patch:      https://github.com/sphinx-doc/sphinx/pull/13610.patch
Patch:      https://github.com/sphinx-doc/sphinx/pull/13883.patch

BuildArch:     noarch

BuildRequires: make
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: pyproject-rpm-macros

%if %{with sphinxcontrib}
# applehelp and jsmath have been orphaned, we cannot use the [docs] extra directly
BuildRequires: python%{python3_pkgversion}-sphinxcontrib-devhelp
BuildRequires: python%{python3_pkgversion}-sphinxcontrib-htmlhelp
BuildRequires: python%{python3_pkgversion}-sphinxcontrib-serializinghtml
BuildRequires: python%{python3_pkgversion}-sphinxcontrib-qthelp
BuildRequires: python%{python3_pkgversion}-sphinxcontrib-websupport
%endif

%if %{with tests}
# tests import _testcapi
BuildRequires: python%{python3_pkgversion}-test

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: graphviz
BuildRequires: texinfo

%if %{with imagemagick_tests}
BuildRequires: ImageMagick
%endif

%if %{undefined rhel} && %{with latex_tests}
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-collection-latex
BuildRequires: texlive-gnu-freefont
BuildRequires: latexmk
BuildRequires: texlive-dvipng
BuildRequires: texlive-dvisvgm
BuildRequires: tex(article.cls)
BuildRequires: tex(utf8x.def)
# Other dependencies.
BuildRequires: tex(alltt.sty)
BuildRequires: tex(amsfonts.sty)
BuildRequires: tex(amsmath.sty)
BuildRequires: tex(amssymb.sty)
BuildRequires: tex(amstext.sty)
BuildRequires: tex(amsthm.sty)
BuildRequires: tex(anyfontsize.sty)
BuildRequires: tex(atbegshi.sty)
BuildRequires: tex(babel.sty)
BuildRequires: tex(bm.sty)
BuildRequires: tex(booktabs.sty)
BuildRequires: tex(capt-of.sty)
BuildRequires: tex(cmap.sty)
BuildRequires: tex(colortbl.sty)
BuildRequires: tex(ellipse.sty)
BuildRequires: tex(etoolbox.sty)
BuildRequires: tex(fancyhdr.sty)
BuildRequires: tex(fancyvrb.sty)
BuildRequires: tex(float.sty)
BuildRequires: tex(fncychap.sty)
BuildRequires: tex(fontawesome.sty)
BuildRequires: tex(fontawesome5.sty)
BuildRequires: tex(fontenc.sty)
BuildRequires: tex(fontspec.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(geometry.sty)
BuildRequires: tex(graphicx.sty)
BuildRequires: tex(hypcap.sty)
BuildRequires: tex(hyperref.sty)
BuildRequires: tex(inputenc.sty)
BuildRequires: tex(kvoptions.sty)
BuildRequires: tex(longtable.sty)
BuildRequires: tex(ltxcmds.sty)
BuildRequires: tex(luatex85.sty)
BuildRequires: tex(makeidx.sty)
BuildRequires: tex(multicol.sty)
BuildRequires: tex(needspace.sty)
BuildRequires: tex(parskip.sty)
BuildRequires: tex(pict2e.sty)
BuildRequires: tex(polyglossia.sty)
BuildRequires: tex(remreset.sty)
BuildRequires: tex(substitutefont.sty)
BuildRequires: tex(tabulary.sty)
BuildRequires: tex(textalpha.sty)
BuildRequires: tex(textcomp.sty)
BuildRequires: tex(tgheros.sty)
BuildRequires: tex(tgtermes.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(upquote.sty)
BuildRequires: tex(varwidth.sty)
BuildRequires: tex(wrapfig.sty)
BuildRequires: tex(xcolor.sty)
%endif
%endif


%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.


%package -n python%{python3_pkgversion}-sphinx
Summary:       Python documentation generator

Recommends:    graphviz
Recommends:    ImageMagick
Recommends:    make

# Upstream Requires those, but we have a patch to remove the dependency.
# We keep them Recommended to preserve the default user experience.
%if %{with sphinxcontrib}
# applehelp and jsmath have been orphaned
Recommends:    python%{python3_pkgversion}-sphinxcontrib-devhelp
Recommends:    python%{python3_pkgversion}-sphinxcontrib-htmlhelp
Recommends:    python%{python3_pkgversion}-sphinxcontrib-serializinghtml
Recommends:    python%{python3_pkgversion}-sphinxcontrib-qthelp
%endif

%description -n python%{python3_pkgversion}-sphinx
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.


%if %{undefined rhel}
%package -n python%{python3_pkgversion}-sphinx-latex
Summary:       LaTeX builder dependencies for python%{python3_pkgversion}-sphinx

Requires:      python%{python3_pkgversion}-sphinx = %{epoch}:%{version}-%{release}
# Required dependencies as stated in the documentation [1]:
#
#   - texlive-collection-latexrecommended
#   - texlive-collection-fontsrecommended
#   - texlive-collection-fontsextra
#   - texlive-collection-latexextra
#   - texlive-tex-gyre
#   - latexmk
#
# [1] https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder
#
# These packages install 2500+ other packages requiring ~3 GiB of space.
# Therefore, a more precise list of dependencies.

Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      texlive-gnu-freefont
Requires:      latexmk

# Required by sphinx.ext.imgmath – Render math as images
Requires:      texlive-dvipng
Requires:      texlive-dvisvgm
#Requires:     tex(preview.sty)    Pulls in texlive-collection-latexrecommended

Requires:      tex(article.cls)
Requires:      tex(utf8x.def)

# Other dependencies.
# -- After searching for \RequirePackage{..} and \usepackage{..}.
Requires:      tex(alltt.sty)
Requires:      tex(amsfonts.sty)
Requires:      tex(amsmath.sty)
Requires:      tex(amssymb.sty)
Requires:      tex(amstext.sty)
Requires:      tex(amsthm.sty)
Requires:      tex(anyfontsize.sty)
Requires:      tex(atbegshi.sty)
Requires:      tex(babel.sty)
Requires:      tex(bm.sty)
Requires:      tex(booktabs.sty)
Requires:      tex(capt-of.sty)
Requires:      tex(cmap.sty)
Requires:      tex(colortbl.sty)
Requires:      tex(ellipse.sty)
Requires:      tex(etoolbox.sty)
Requires:      tex(fancyhdr.sty)
Requires:      tex(fancyvrb.sty)
Requires:      tex(float.sty)
Requires:      tex(fncychap.sty)
Requires:      tex(fontawesome.sty)
Requires:      tex(fontawesome5.sty)
Requires:      tex(fontenc.sty)
Requires:      tex(fontspec.sty)
Requires:      tex(framed.sty)
Requires:      tex(geometry.sty)
Requires:      tex(graphicx.sty)
Requires:      tex(hypcap.sty)
Requires:      tex(hyperref.sty)
Requires:      tex(inputenc.sty)
Requires:      tex(kvoptions.sty)
Requires:      tex(longtable.sty)
Requires:      tex(ltxcmds.sty)
Requires:      tex(luatex85.sty)
Requires:      tex(makeidx.sty)
Requires:      tex(multicol.sty)
Requires:      tex(needspace.sty)
Requires:      tex(parskip.sty)
Requires:      tex(pict2e.sty)
Requires:      tex(polyglossia.sty)
Requires:      tex(remreset.sty)
Requires:      tex(substitutefont.sty)
Requires:      tex(tabulary.sty)
Requires:      tex(textalpha.sty)
Requires:      tex(textcomp.sty)
Requires:      tex(tgheros.sty)
Requires:      tex(tgtermes.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(upquote.sty)
Requires:      tex(varwidth.sty)
Requires:      tex(wrapfig.sty)
Requires:      tex(xcolor.sty)
#Requires:     tex(xeCJK.sty)      Pulls in pLaTeX and upLaTeX

# No files in this package, automatic provides don't work:
%py_provides   python%{python3_pkgversion}-sphinx-latex

%description  -n python%{python3_pkgversion}-sphinx-latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.
%endif


%package doc
Summary:       Documentation for %{name}
License:       BSD-2-Clause
Recommends:    python%{python3_pkgversion}-sphinx = %{epoch}:%{version}-%{release}

%description doc
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains documentation in the HTML format.


%prep
%autosetup -n sphinx-%{upstream_version} -p1

# Drop test-dependency on pytest-xdist
# This allows for parallel testing, but has a lot of dependencies.
# We want to avoid the dependency in RHEL, where it is not available.
%if 0%{?rhel}
sed -i -e '/pytest-xdist/d' pyproject.toml
%endif

# Support for docutils 0.22+
sed -i -e 's/docutils>=0.20,<0.22/docutils>=0.20,<0.23/' pyproject.toml

# Drop test-dependency on defusedxml,
# use xml from the standard library instead.
# defusedxml is safer but this is only used in tests.
# Upstream uses defusedxml to be "safer for future contributors when they
# create/open branches and pull requests" -- that does not concern us.
# https://github.com/sphinx-doc/sphinx/pull/12168#discussion_r1535383868
# We want to avoid the dependency in RHEL, but no harm in doing so unconditionally.
sed -i '/"defusedxml/d' pyproject.toml
sed -i 's/from defusedxml./from xml.etree./' sphinx/testing/util.py tests/test_theming/test_theming.py

%if %{without snowballstemmer}
# Drop dependency on snowballstemmer for RHEL, implement dummy method instead
sed -i -e '/snowballstemmer/d' pyproject.toml
sed -i -e 's/^import \(snowballstemmer\)/from . import dummystemmer as \1/' sphinx/search/*.py
cat > sphinx/search/dummystemmer.py <<_EOF
class stemmer:
    def __init__(self, *args, **kwargs): pass
    def stemWord(self, word): return word
_EOF
%endif

%if %{without imagemagick_tests}
rm tests/test_extensions/test_ext_imgconverter.py
%endif


%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}


%build
%pyproject_wheel

export PYTHONPATH=$PWD
pushd doc
export SPHINXBUILD="%{python3} ../sphinx/cmd/build.py"
make html SPHINXBUILD="$SPHINXBUILD"
make man SPHINXBUILD="$SPHINXBUILD"
rm -rf _build/html/.buildinfo
# Those files are copied to _build/html/_images and loaded to the
# html pages from there - we can safely remove the duplicated and unused files
rm -rf _build/html/_static/themes _build/html/_static/tutorial
rm -f _build/html/_static/more.png _build/html/_static/translation.svg
mv _build/html ..
popd


%install
%pyproject_install

# For backwards compatibility. Remove with care, if at all
for i in sphinx-{apidoc,autogen,build,quickstart}; do
    ln -s %{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python3_version}
    ln -s %{_bindir}/$i %{buildroot}%{_bindir}/$i-3
done

# Clean up non-python files
rm -f %{buildroot}%{python3_sitelib}/sphinx/locale/.DS_Store
rm -rf %{buildroot}%{python3_sitelib}/sphinx/locale/.tx

pushd doc
# Deliver man pages
install -d %{buildroot}%{_mandir}/man1
for f in _build/man/sphinx-*.1;
do
    cp -p $f %{buildroot}%{_mandir}/man1/$(basename $f)
done
popd

# Move language files to /usr/share;
# patch to support this incorporated in 0.6.6
pushd %{buildroot}%{python3_sitelib}

for lang in `find sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/sphinx/locale/$lang
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.js \
     %{buildroot}%{_datadir}/sphinx/locale/$lang/
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.mo \
    %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
  rm -rf sphinx/locale/$lang
done
popd

# Create the sphinxcontrib directory, so we can own it
# See https://bugzilla.redhat.com/show_bug.cgi?id=1669790 for rationale
mkdir %{buildroot}%{python3_sitelib}/sphinxcontrib

%find_lang sphinx

# Language files; Since these are javascript, it's not immediately obvious to
# find_lang that they need to be marked with a language.
(cd %{buildroot} && find . -name 'sphinx.js') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:' \
  >> sphinx.lang


%if %{with tests}
%check
# Currently, all linkcheck tests and test_latex_images need internet
# test_build_latex_doc needs internet to download pictures,
# but fails also with it enabled, we decided to skip it entirely
# test_autodoc_type_aliases fails with Python 3.12.4, 3.13.0b3
# skip temporarily until resolved:
# https://github.com/sphinx-doc/sphinx/issues/12430
k="not test_autodoc_type_aliases"
%if %{without internet}
k="${k} and not linkcheck and not test_latex_images and not test_build_latex_doc"
%endif

%if %{without snowballstemmer}
# Without snowballstemmer, some tests have to be skipped as well,
# as the results with dummystemmer do not exactly match the testcases
k="${k} and not test_meta_keys_are_handled_for_language_en and not test_stemmer"
k="${k} and not test_term_in_heading_and_section and not test_IndexBuilder"
k="${k} and not test_check_js_search_indexes"
%endif

%pytest -k "${k}"
%endif

%files -n python%{python3_pkgversion}-sphinx -f sphinx.lang
%license LICENSE.rst
%doc README.rst
%{_bindir}/sphinx-*
%{python3_sitelib}/sphinx/
%dir %{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinx-%{upstream_version}.dist-info/
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*
%{_mandir}/man1/sphinx-*

%if %{undefined rhel}
%files -n python%{python3_pkgversion}-sphinx-latex
# empty, this is a metapackage
%endif

%files doc
%license LICENSE.rst
%doc html


%changelog
%autochangelog
