%bcond check 1
# We can run these in a local mock build with --enable-network.
%bcond network_tests 0

Name:           pre-commit
Version:        4.1.0
Release:        %autorelease
Summary:        Framework for managing and maintaining multi-language pre-commit hooks

# SPDX
License:        MIT
URL:            https://pre-commit.com
%global forgeurl https://github.com/pre-commit/pre-commit
Source:         %{forgeurl}/archive/v%{version}/pre-commit-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

%if %{with check}
# Manually added to speed up the %%check section
BuildRequires:  python3dist(pytest-xdist)
%endif

%description
A framework for managing and maintaining multi-language pre-commit hooks.


%prep
%autosetup -p1 -S git
# Do not generate BR’s for coverage, linters, etc.:
sed -r '/^(covdefaults|coverage)\b/d' requirements-dev.txt |
  tee requirements-dev-filtered.txt


%generate_buildrequires
%pyproject_buildrequires -r %{?with_check:requirements-dev-filtered.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pre_commit


%check
# Any Python files inside pre_commit.resources are templates and are not
# intended to be imported.
%pyproject_check_import -e 'pre_commit.resources.*'

%if %{with check}
# For general discusson on test failures building distribution packages, see:
# https://github.com/pre-commit/pre-commit/issues/1183,
# https://github.com/pre-commit/pre-commit/issues/1202

# Does not work under (i.e., respect) an “external” PYTHONPATH
k="${k-}${k+ and }not test_installed_from_venv"

%if %{without network_tests}
k="${k-}${k+ and }not test_additional_dependencies_roll_forward"
k="${k-}${k+ and }not test_repository_state_compatibility[v1]"
k="${k-}${k+ and }not test_repository_state_compatibility[v2]"
k="${k-}${k+ and }not test_reinstall"
k="${k-}${k+ and }not test_control_c_control_c_on_install"
k="${k-}${k+ and }not test_invalidated_virtualenv"
k="${k-}${k+ and }not test_really_long_file_paths"
k="${k-}${k+ and }not test_local_python_repo"
%endif

# These are the tests that run by default via tox; see tox.ini. See also
# .github/workflows/main.yml.
%pytest --ignore=tests/languages -k "${k-}" -v
%endif


%files -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/pre-commit


%changelog
%autochangelog
