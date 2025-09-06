%global  forgeurl https://github.com/pyinfra-dev/pyinfra
%global  pypi_name pyinfra
Name:           python-%{pypi_name}
Version:        3.4.1
%global  tag    v%{version}
Release:        %autorelease

Summary:        Provision, manage and deploy infrastructure

License:        MIT
URL:            https://pyinfra.com
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
%forgemeta

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies include extra formatting and coverage tests
# that are not needed in Fedora CI
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  python3-pytest-testinfra

%global _description %{expand:
pyinfra turns Python code into shell commands and runs them on your
servers. Execute ad-hoc commands and write declarative operations.
Target SSH servers, local machine and Docker containers.}

%description %_description

%package -n     python3-pyinfra
Summary:        %{summary}

%description -n python3-pyinfra %_description


%prep
%forgesetup
# Remove unneeded dependency
sed -i '/configparser/d' setup.py
# Remove unused scripts, package documentation
# as text files
rm docs/*.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Remove test files
rm -r %{buildroot}%{python3_sitelib}/tests
%pyproject_save_files -l pyinfra


%check
%pyproject_check_import
# Do not run test that depend on network access
k="${k-}${k+ and }not (test_put_file_sudo)"
# Temporarily deselect tests that need click 8.2+
deselect="${deselect-} --deselect=tests/test_cli/test_cli.py::TestFactCli::test_get_fact"
deselect="${deselect-} --deselect=tests/test_cli/test_cli.py::TestFactCli::test_get_fact_with_kwargs"
deselect="${deselect-} --deselect=tests/test_cli/test_cli_inventory.py::TestCliInventory::test_host_groups_may_only_contain_strings_or_tuples"
deselect="${deselect-} --deselect=tests/test_cli/test_cli_inventory.py::TestCliInventory::test_ignores_variables_with_leading_underscore"
deselect="${deselect-} --deselect=tests/test_cli/test_cli_inventory.py::TestCliInventory::test_only_supports_list_and_tuples"
%pytest -k "${k-}" ${deselect-}


%files -n python3-pyinfra -f %{pyproject_files}
%{_bindir}/pyinfra
%{python3_sitelib}/pyinfra_cli/
%license LICENSE.md
%doc README.md
%doc CHANGELOG.md
%doc docs

%changelog
%autochangelog
