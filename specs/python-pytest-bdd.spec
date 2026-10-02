Name:           python-pytest-bdd
Version:        9.0.0
Release:        %autorelease
Summary:        BDD library for the pytest runner

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

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --tox
BuildOption(install): --assert-license pytest_bdd

BuildArch:      noarch

# Required for: tests/feature/test_report.py::test_complex_types
# Also in the “dev” dependency group.
BuildRequires:  %{py3_dist pytest-xdist} >= 3.3.1

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

%description -n python3-pytest-bdd %{common_description}


%install -a
install -D --mode 0644 --preserve-timestamps \
    --target-directory '%{buildroot}%{_mandir}/man1' \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


%check -a
%tox -- -- --numprocesses auto --verbose


%files -n python3-pytest-bdd -f %{pyproject_files}
%doc AUTHORS.rst
%doc CHANGES.rst
%doc README.rst
%{_bindir}/pytest-bdd
%{_mandir}/man1/pytest-bdd*.1*


%changelog
%autochangelog
