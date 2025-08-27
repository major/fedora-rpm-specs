%global srcname pep8-naming
%global srcname_ pep8_naming
%global _description %{expand:
Check the PEP-8 naming conventions.
This module provides a plugin for flake8, the Python code checker.
(It replaces the plugin flint-naming for the flint checker.)}


Name:           python-%{srcname}
Version:        0.15.1
Release:        %autorelease
Summary:        Check PEP-8 naming conventions, a plugin for flake8

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname_}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pep8ext_naming

%check
%{py3_test_envvars} %{python3} run_tests.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
