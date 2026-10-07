Name:           python-pytest-remaster
Version:        0.1.0
Release:        %autorelease
Summary:        Pytest plugin for golden master _characterisation_ testing

License:        MIT
URL:            https://github.com/Pierre-Sassoulas/pytest-remaster
Source:         %{pypi_source pytest_remaster}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pandas
BuildRequires:  python3-pytest-cov

%global _description %{expand:
Pytest plugin for golden master _characterisation_ testing
with automatic expected file regeneration.}

%description %_description

%package -n     python3-pytest-remaster
Summary:        %{summary}

%description -n python3-pytest-remaster %_description


%prep
%autosetup -p1 -n pytest_remaster-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pytest_remaster


%check
%pyproject_check_import
%pytest  --deselect=tests/demo_pylint/test_functional.py::test_pylint_functional_tests[3.11-simple_module.py] \
         --deselect=tests/demo_pylint/test_functional.py::test_pylint_functional_tests[3.12-simple_module.py] \
         --deselect=tests/demo_pylint/test_functional.py::test_pylint_functional_tests[3.13-simple_module.py] \
         --deselect=tests/demo_pylint/test_functional.py::test_pylint_functional_tests[3.14-simple_module.py]


%files -n python3-pytest-remaster -f %{pyproject_files}


%changelog
%autochangelog
