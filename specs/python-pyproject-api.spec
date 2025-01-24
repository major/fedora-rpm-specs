Name:           python-pyproject-api
Version:        1.9.0
Release:        %autorelease
Summary:        API to interact with the python pyproject.toml based projects

License:        MIT
URL:            https://pyproject-api.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/p/pyproject-api/pyproject_api-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
API to interact with the python pyproject.toml based projects.}

%description %_description

%package -n     python3-pyproject-api
Summary:        %{summary}

%description -n python3-pyproject-api %_description

%prep
%autosetup -n pyproject_api-%{version}
# Remove unneeded testing deps
sed -i "/covdefaults/d;/pytest-cov/d" pyproject.toml
sed -i 's/"setuptools>=.*"/"setuptools"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyproject_api

%check
# Skip test_setuptools_prepare_metadata_for_build_wheel
# see https://github.com/tox-dev/pyproject-api/issues/153
%pytest -k "not test_setuptools_prepare_metadata_for_build_wheel"

%files -n python3-pyproject-api -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
