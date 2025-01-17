# Building the documentation requires the furo Sphinx theme.  But building furo
# requires sphinx_theme_builder, which requires this package.  Avoid a
# dependency loop with this conditional.
%bcond doc 0

Name:           python-pyproject-metadata
Version:        0.8.0
Release:        %autorelease
Summary:        PEP 621 metadata parsing

License:        MIT
URL:            https://github.com/FFY00/python-pyproject-metadata
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/pyproject-metadata-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}

%global _desc %{expand:
Dataclass for PEP 621 metadata with support for core metadata generation.

This project does not implement the parsing of pyproject.toml containing
PEP 621 metadata.  Instead, given a Python data structure representing
PEP 621 metadata (already parsed), it will validate this input and
generate a PEP 643-compliant metadata file (e.g. PKG-INFO).}

%description %_desc

%package     -n python3-pyproject-metadata
Summary:        PEP 621 metadata parsing

# This can be removed when F40 reaches EOL
Obsoletes:      python3-pep621 < 0.5
Provides:       python3-pep621 = %{version}-%{release}

%description -n python3-pyproject-metadata %_desc

%if %{with doc}
%package        doc
Summary:        Documentation for python3-pyproject-metadata

# This can be removed when F40 reaches EOL
Obsoletes:      python3-pep621-doc < 0.5
Provides:       python3-pep621-doc = %{version}-%{release}

%description    doc
Documentation for python3-pyproject-metadata.
%endif

%prep
%autosetup -n pyproject-metadata-%{version}
# No need to BuildRequire pytest-cov to run pytest
sed -i /pytest-cov/d pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test%{?with_doc:,docs}

%build
%pyproject_wheel
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html

%if %{with doc}
# Build the documentation
PYTHONPATH=$PWD/build/lib
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
%endif

%install
%pyproject_install
%pyproject_save_files -L pyproject_metadata

%check
%pytest -v

%files -n python3-pyproject-metadata -f %{pyproject_files}
%doc CHANGELOG.html README.md
%license LICENSE

%if %{with doc}
%files doc
%doc html
%endif

%changelog
%autochangelog
