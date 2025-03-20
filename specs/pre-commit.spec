%bcond check 1
# We can run these in a local mock build with --enable-network.
%bcond network_tests 0

Name:           pre-commit
Version:        4.2.0
Release:        %autorelease
Summary:        Framework for managing and maintaining multi-language pre-commit hooks

# SPDX
License:        MIT
URL:            https://pre-commit.com
%global forgeurl https://github.com/pre-commit/pre-commit
Source0:        %{forgeurl}/archive/v%{version}/pre-commit-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help:
Source100:       pre-commit.1
Source101:       pre-commit-autoupdate.1
Source102:       pre-commit-clean.1
Source103:       pre-commit-gc.1
Source104:       pre-commit-help.1
Source105:       pre-commit-init-templatedir.1
Source106:       pre-commit-install.1
Source107:       pre-commit-install-hooks.1
Source108:       pre-commit-migrate-config.1
Source109:       pre-commit-run.1
Source110:       pre-commit-sample-config.1
Source111:       pre-commit-try-repo.1
Source112:       pre-commit-uninstall.1
Source113:       pre-commit-validate-config.1
Source114:       pre-commit-validate-manifest.1

BuildArch:      noarch

# Much functionality relies on invoking git commands.
Requires:       git-core

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

install -t %{buildroot}%{_mandir}/man1 -p -m 0644 -D \
    %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
    %{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} \
    %{SOURCE110} %{SOURCE111} %{SOURCE112} %{SOURCE113} %{SOURCE114}


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
%{_mandir}/man1/pre-commit*.1*


%changelog
%autochangelog
