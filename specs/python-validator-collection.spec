Name:           python-validator-collection
Version:        1.5.0
Release:        %autorelease
Summary:        Collection of 60+ Python functions for validating data

License:        MIT
URL:            https://github.com/insightindustry/validator-collection
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v.%{version}/validator-collection-v.%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
The Validator Collection is a Python library that provides more than 60
functions that can be used to validate the type and contents of an input
value.}

%description %_description

%package -n     python3-validator-collection
Summary:        %{summary}

%description -n python3-validator-collection %_description

%prep
%autosetup -p1 -n validator-collection-v.%{version}

# Drop unnecessary linter dependency
sed -i '/codecov/d' requirements.txt setup.py tox.ini

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l validator_collection

%check
# Disable tests that attempt to access host paths that do not exist in mock
%pytest -v \
  --deselect='tests/test_checkers.py::test_is_readable[/var/data/xx1.txt-True-False]' \
  --deselect='tests/test_validators.py::test_readable[/var/data/xx1.txt-True-False]' \
  --deselect='tests/test_validators.py::test_writeable[/var/data/xx1.txt-True-False]' \
  --deselect='tests/test_validators.py::test_executable[/var/data/xx1.txt-True-False]' \
  %{nil}

%files -n python3-validator-collection -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
