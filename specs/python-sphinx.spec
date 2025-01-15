# When bootstrapping sphinx in Fedora, we don't yet have sphinxcontrib-*
# Without the packages, we have warnings in docs, but it's not a hard dependency
# We don't want to support sphinxcontrib-* in RHEL, hence disabling the dependencies
%bcond sphinxcontrib %{undefined rhel}
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
%bcond latex_tests 1

Name:       python-sphinx
%global     general_version 8.1.3
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

%if %{with latex_tests}
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-collection-latex
BuildRequires: texlive-dvipng
BuildRequires: texlive-dvisvgm
BuildRequires: tex(amsmath.sty)
BuildRequires: tex(amsthm.sty)
BuildRequires: tex(anyfontsize.sty)
BuildRequires: tex(article.cls)
BuildRequires: tex(capt-of.sty)
BuildRequires: tex(cmap.sty)
BuildRequires: tex(color.sty)
BuildRequires: tex(ctablestack.sty)
BuildRequires: tex(fancyhdr.sty)
BuildRequires: tex(fancyvrb.sty)
BuildRequires: tex(fncychap.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(FreeSerif.otf)
BuildRequires: tex(geometry.sty)
BuildRequires: tex(hyperref.sty)
BuildRequires: tex(kvoptions.sty)
BuildRequires: tex(luatex85.sty)
BuildRequires: tex(needspace.sty)
BuildRequires: tex(parskip.sty)
BuildRequires: tex(polyglossia.sty)
BuildRequires: tex(tabulary.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(upquote.sty)
BuildRequires: tex(utf8x.def)
BuildRequires: tex(wrapfig.sty)
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


%package -n python%{python3_pkgversion}-sphinx-latex
Summary:       LaTeX builder dependencies for python%{python3_pkgversion}-sphinx

Requires:      python%{python3_pkgversion}-sphinx = %{epoch}:%{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      texlive-dvipng
Requires:      texlive-dvisvgm
Requires:      tex(amsmath.sty)
Requires:      tex(amsthm.sty)
Requires:      tex(anyfontsize.sty)
Requires:      tex(article.cls)
Requires:      tex(capt-of.sty)
Requires:      tex(cmap.sty)
Requires:      tex(color.sty)
Requires:      tex(ctablestack.sty)
Requires:      tex(fancyhdr.sty)
Requires:      tex(fancyvrb.sty)
Requires:      tex(fncychap.sty)
Requires:      tex(framed.sty)
Requires:      tex(FreeSerif.otf)
Requires:      tex(geometry.sty)
Requires:      tex(hyperref.sty)
Requires:      tex(kvoptions.sty)
Requires:      tex(luatex85.sty)
Requires:      tex(needspace.sty)
Requires:      tex(parskip.sty)
Requires:      tex(polyglossia.sty)
Requires:      tex(tabulary.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(upquote.sty)
Requires:      tex(utf8x.def)
Requires:      tex(wrapfig.sty)

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


%files -n python%{python3_pkgversion}-sphinx-latex
# empty, this is a metapackage


%files doc
%license LICENSE.rst
%doc html


%changelog
%autochangelog
