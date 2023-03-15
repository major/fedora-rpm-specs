Name:           python-pyproject-api
Version:        1.5.1
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

%generate_buildrequires
%pyproject_buildrequires -w -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyproject_api

%check
# We don't want to depend on Python 2
%pytest -k "not test_can_build_on_python_2"

%files -n python3-pyproject-api -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
