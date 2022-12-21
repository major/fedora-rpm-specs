%global srcname pep8-naming
%global srcname_ pep8ext_naming
%global _description \
Check the PEP-8 naming conventions. \
This module provides a plugin for flake8, the Python code checker. \
(It replaces the plugin flint-naming for the flint checker.)


Name:           python-%{srcname}
Version:        0.13.2
Release:        %autorelease
Summary:        Check PEP-8 naming conventions, a plugin for flake8

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} run_tests.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
