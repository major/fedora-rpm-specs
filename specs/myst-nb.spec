# Building the documentation requires packages not available from Fedora:
# altair, coconut
%bcond doc 0

# Build from git HEAD until a version supporting Sphinx 9 is released
%global commit  d7012c43b1ec57c2be6eaca455540f1cfdac4735
%global shortcommit %{sub %{commit} 1 7}
%global gitdate 20260203
%global giturl  https://github.com/executablebooks/MyST-NB

Name:           myst-nb
Version:        1.3.0^%{gitdate}.%{shortcommit}
Release:        %autorelease
Summary:        Jupyter Notebook Sphinx reader

License:        BSD-3-Clause
URL:            https://myst-nb.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Preliminary support for Sphinx 9 and docutils 0.22, may still be buggy
Patch:          %{giturl}/pull/704.patch

BuildRequires:  help2man
%if %{with doc}
BuildRequires:  make
%endif

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x testing%{?with_doc:,rtd}
BuildOption(install): -L myst_nb

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
%autosetup -n MyST-NB-%{commit} -p1

# Do not run coverage tools in RPM builds
sed -i '/coverage/d;/pytest-cov/d' pyproject.toml

# Permit newer versions of matplotlib
sed -i 's/==/>=/' pyproject.toml

%build -a
%if %{with doc}
# Build the documentation
PYTHONPATH=$PWD make -C docs html
rm docs/_build/html/.buildinfo
%endif

%install -a
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

# TODO: Tests are disabled until a version supporting Sphinx 9 is released
#%%check
#%%pytest -v

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
