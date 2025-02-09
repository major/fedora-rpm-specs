# Building the documentation requires packages not available from Fedora:
# altair, coconut, sphinx-book-theme
%bcond doc 0

%global giturl  https://github.com/executablebooks/MyST-NB

Name:           myst-nb
Version:        1.2.0
Release:        %autorelease
Summary:        Jupyter Notebook Sphinx reader

License:        BSD-3-Clause
BuildArch:      noarch
URL:            https://myst-nb.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  help2man
BuildRequires:  python3-devel

%if %{with doc}
BuildRequires:  make
%endif

%py_provides python3-%{name}
%py_provides python3-MyST-NB

%description
MyST is a rich and extensible flavor of Markdown meant for technical
documentation and publishing.  It is designed for simplicity, flexibility, and
extensibility.  This package contains a reference implementation of MyST
Markdown, as well as a collection of tools to support working with MyST in
Python and Sphinx.  It contains an extended CommonMark-compliant parser using
markdown-it-py, as well as a Sphinx extension that allows you to write MyST
Markdown in Sphinx.

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}

%description    doc
Documentation for %{name}.
%endif

%prep
%autosetup -n MyST-NB-%{version}

%generate_buildrequires
# Permit newer versions of matplotlib for testing only.  The newer version of
# matplotlib causes some changes in test output; pyproject.toml says:
#   Matplotlib outputs are sensitive to the matplotlib version
sed -i 's/==\([*.[:digit:]]*\)//' pyproject.toml
sed -e 's/9bc81205a14646a235d284d1b68223d17f30f7f1d3d8ed3e52cf47830b02e3bb/6b2036253586d5fc9698aafec0292cfad0dd12c9f8fefb3f6be255409b89ed39/g' \
    -e 's/a2e637020dfe58f670ba2c942d7a55e49ba48bed09312569ee15a84f5ac680cb/b99cf76118b984ae1e1a23821dd0793a98b20eb318387e0d64e45b6d7ce14a28/g' \
    -i tests/test_execute/test_complex_outputs_unrun_{auto,cache}.xml \
       tests/test_execute/test_custom_convert_{auto,cache}.xml \
       tests/test_execute/test_custom_convert_multiple_extensions_{auto,cache}.xml
%pyproject_buildrequires -x testing%{?with_doc:,rtd}

%build
%pyproject_wheel

%if %{with doc}
# Build the documentation
PYTHONPATH=$PWD make -C docs html
rm docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files -L myst_nb

export PYTHONPATH=%{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1
makeman() {
  help2man -N -n "$2" --version-string='%{version}' %{buildroot}%{_bindir}/$1 \
           -o %{buildroot}%{_mandir}/man1/$1.1
}
makeman mystnb-docutils-html 'Generate (X)HTML documents from MyST sources'
makeman mystnb-docutils-html5 'Generate HTML5 documents from MyST sources'
makeman mystnb-docutils-latex 'Generate LaTeX documents from MyST sources'
makeman mystnb-docutils-pseudoxml 'Generate pseudo-XML from MyST sources'
makeman mystnb-docutils-xml 'Generate docutils-native XML from MyST sources'
makeman mystnb-quickstart 'Create a basic MyST-NB project'
makeman mystnb-to-jupyter 'Convert a text-based notebook to a Jupyter notebook'

%check
%pytest -v

%files -n myst-nb -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/mystnb-docutils-html
%{_bindir}/mystnb-docutils-html5
%{_bindir}/mystnb-docutils-latex
%{_bindir}/mystnb-docutils-pseudoxml
%{_bindir}/mystnb-docutils-xml
%{_bindir}/mystnb-quickstart
%{_bindir}/mystnb-to-jupyter
%{_mandir}/man1/mystnb-docutils-html.1*
%{_mandir}/man1/mystnb-docutils-html5.1*
%{_mandir}/man1/mystnb-docutils-latex.1*
%{_mandir}/man1/mystnb-docutils-pseudoxml.1*
%{_mandir}/man1/mystnb-docutils-xml.1*
%{_mandir}/man1/mystnb-quickstart.1*
%{_mandir}/man1/mystnb-to-jupyter.1*

%if %{with doc}
%files doc
%doc doc/_build/html
%license LICENSE
%endif

%changelog
%autochangelog
