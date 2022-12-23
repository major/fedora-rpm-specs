Name:           python-pytest-bdd5
Version:        5.0.0
Release:        %autorelease
Summary:        BDD library for the py.test runner (version 5 compat package)

# SPDX
License:        MIT
URL:            https://pytest-bdd.readthedocs.io/en/latest/
%global forgeurl https://github.com/pytest-dev/pytest-bdd
Source0:        %{forgeurl}/archive/%{version}/pytest-bdd-%{version}.tar.gz

# Downstream man page, written for Fedora in groff_man(7) format based on the
# command’s --help output.
Source1:        pytest-bdd.1

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Required for: tests/feature/test_report.py::test_complex_types
BuildRequires:  python3dist(pytest-xdist)

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
object containing the side effects of Gherkin imperative declarations.

This compatibility package provides major version 5 of pytest-bdd. It is not
parallel-installable with the main package.}

%description %{common_description}


%package -n     python3-pytest-bdd5
Summary:        %{summary}

# Renaming the Python package from pytest_bdd to pytest_bdd5 requires too many
# invasive and nontrivial changes to be practical. Instead we resort to an
# explicit Conflict with the main package. See:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
#
# Note that because this is a testing package, it is used in Fedora only as a
# BuildRequires, which reduces the impact of the conflict.
Conflicts:      python3-pytest-bdd

%description -n python3-pytest-bdd5 %{common_description}


%prep
%autosetup -n pytest-bdd-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_bdd
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'


%check
# Work around unexpected PytestAssertRewriteWarning with pip 21.3
# https://github.com/pytest-dev/pytest-bdd/issues/453
mkdir -p _empty && cp -rp tests *.ini _empty && cd _empty

%pytest -n auto -v


%files -n python3-pytest-bdd5 -f %{pyproject_files}
%doc AUTHORS.rst
%doc CHANGES.rst
%doc README.rst
%{_bindir}/pytest-bdd
%{_mandir}/man1/pytest-bdd.1*


%changelog
%autochangelog
