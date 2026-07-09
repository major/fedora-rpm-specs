# A "fake" bootstrap to not require python-pytest-regessions,
# as its long dependency chain allows to build it much later in new Python bootstrap
%bcond bootstrap 0
%global pypi_name myst-parser

Name:           python-%{pypi_name}
Version:        5.1.0
Release:        %autorelease
Summary:        A commonmark compliant parser, with bridges to docutils & sphinx

# SPDX
License:        MIT
URL:            https://github.com/executablebooks/MyST-Parser
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies- upstream uses tox with complicated matrix
# mixed with coverage, it's easier to set the ones we want here
BuildRequires:  python3-pytest
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-docutils
%if %{without bootstrap}
BuildRequires:  python3-pytest-regressions
%endif
BuildRequires:  python3-pytest-param-files
BuildRequires:  python3-sphinx-pytest
BuildRequires:  python3-linkify-it-py
BuildRequires:  python3-soupsieve


%global _description %{expand:
A fully-functional markdown flavor and parser for Sphinx.
MyST allows you to write Sphinx documentation entirely in markdown.
MyST markdown provides a markdown equivalent of the reStructuredText syntax,
meaning that you can do anything in MyST that you can do with reStructuredText.
It is an attempt to have the best of both worlds: the flexibility and
extensibility of Sphinx with the simplicity and readability of Markdown.
}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n MyST-Parser-%{version}

%pyproject_patch_dependency docutils:drop_upper

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files myst_parser

%check
# test_link_resolution: https://github.com/executablebooks/MyST-Parser/issues/1152
%pytest %{?with_bootstrap:--ignore tests/test_sphinx/test_sphinx_builds.py} -k 'not test_link_resolution%{?with_bootstrap: and not test_inv and not test_parse}'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/myst-anchors
%{_bindir}/myst-docutils-demo
%{_bindir}/myst-docutils-html
%{_bindir}/myst-docutils-html5
%{_bindir}/myst-docutils-latex
%{_bindir}/myst-docutils-xml
%{_bindir}/myst-docutils-pseudoxml
%{_bindir}/myst-inv

%changelog
%autochangelog
