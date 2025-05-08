Name:           python-pytest-bdd
Version:        7.3.0
Release:        %autorelease
Summary:        BDD library for the py.test runner

# SPDX
License:        MIT
URL:            https://pytest-bdd.readthedocs.io/en/latest/
%global forgeurl https://github.com/pytest-dev/pytest-bdd
Source0:        %{forgeurl}/archive/%{version}/pytest-bdd-%{version}.tar.gz

# Downstream man page, written for Fedora in groff_man(7) format based on the
# command’s --help output.
Source10:       pytest-bdd.1
Source11:       pytest-bdd-generate.1
Source12:       pytest-bdd-migrate.1

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -t
BuildOption(install):   -L pytest_bdd

BuildArch:      noarch

# Required for: tests/feature/test_report.py::test_complex_types
# Also in pyproject.toml:[tool.poetry.group.dev.dependencies]
BuildRequires:  %{py3_dist pytest-xdist} >= 3.3.1

# Required for: tests/feature/test_tags.py (top-level pkg_resources import)
BuildRequires:  %{py3_dist setuptools}

%global common_description %{expand:
pytest-bdd implements a subset of the Gherkin language to enable automating
project requirements testing and to facilitate behavioral driven development.

Unlike many other BDD tools, it does not require a separate runner and benefits
from the power and flexibility of pytest. It enables unifying unit and
functional tests, reduces the burden of continuous integration server
configuration and allows the reuse of test setups.

Pytest fixtures written for unit tests can be reused for setup and actions
mentioned in feature steps with dependency injection. This allows a true BDD
just-enough specification of the requirements without maintaining any context
object containing the side effects of Gherkin imperative declarations.}

%description %{common_description}


%package -n     python3-pytest-bdd
Summary:        %{summary}

# Removed in F42; keep Obsoletes through F45.
Obsoletes:      python-pytest-bdd-doc < 7.3.0-3

%description -n python3-pytest-bdd %{common_description}


%install -a
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


%check -a
%tox -- -- -n auto -v


%files -n python3-pytest-bdd -f %{pyproject_files}
%license LICENSE.txt
%doc AUTHORS.rst
%doc CHANGES.rst
%doc README.rst
%{_bindir}/pytest-bdd
%{_mandir}/man1/pytest-bdd*.1*


%changelog
%autochangelog
