%bcond_without doc
# tests are known to be broken: https://github.com/lnoor/sphinx-jsonschema
%bcond_with tests

Name:           python-sphinx-jsonschema
Version:        1.19.1
Release:        %autorelease
Summary:        Sphinx extension to display JSON Schema

License:        GPL-3.0-only
URL:            https://github.com/lnoor/sphinx-jsonschema
# PyPI source does not contain tests... and license text
# Source:         %%{pypi_source sphinx-jsonschema}
Source:         %{url}/archive/v.%{version}/sphinx-jsonschema-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with doc}
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif


%global _description %{expand:
This package contains sphinx-jsonschema, an extension to Sphinx to allow authors
to display a JSON Schema in their documentation.}

%description %_description

%package -n     python3-sphinx-jsonschema
Summary:        %{summary}

%description -n python3-sphinx-jsonschema %_description


%if %{with doc}
%package        doc
Summary:        Documentation for sphinx-jsonschema

%description    doc
This package contains the documentation for sphinx-jsonschema.
%endif


%prep
%autosetup -p1 -n sphinx-jsonschema-v.%{version}


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH=$PWD make -C docs html
%endif


%install
%pyproject_install
%pyproject_save_files sphinx-jsonschema


%check
%pyproject_check_import sphinx-jsonschema
%if %{with tests}
%tox
%endif


%files -n python3-sphinx-jsonschema -f %{pyproject_files}
%doc README.rst

%if %{with doc}
%files doc
%license LICENSE
%doc docs/_build/html/*
%endif


%changelog
%autochangelog
