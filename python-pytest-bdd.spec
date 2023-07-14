# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-pytest-bdd
Version:        6.1.1
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

# Remove old pytest logic
# Fixes FTBFS with setuptools >= 67.5.1
# Resolved upstream: https://github.com/pytest-dev/pytest-bdd/pull/580
Patch:          remove-old-pytest-logic.patch

# Fix python 3.12.0a3 syntax error
# https://github.com/pytest-dev/pytest-bdd/commit/628790921e05e614a7064aab29b8c60fc01c943b
Patch:          %{forgeurl}/commit/628790921e05e614a7064aab29b8c60fc01c943b.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Required for: tests/feature/test_report.py::test_complex_types
BuildRequires:  python3dist(pytest-xdist)

# Required for: tests/feature/test_tags.py (top-level pkg_resources import)
BuildRequires:  python3dist(setuptools)

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
%endif

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


%if %{with doc}
%package        doc
Summary:        Documentation for pytest-bdd

%description    doc %{common_description}
%endif


%prep
%autosetup -p1 -n pytest-bdd-%{version}

# Do not require package metadata from the installed wheel to build the
# documentation:
sed -r -i 's/metadata\.version\("pytest-bdd"\)/"%{version}"/' docs/conf.py
# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%if %{with doc}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files pytest_bdd
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


%check
# Work around unexpected PytestAssertRewriteWarning with pip 21.3
# https://github.com/pytest-dev/pytest-bdd/issues/453
mkdir -p _empty && cp -rp tests *.ini _empty && cd _empty

# Run tests in parallel (and verbosely)
export PYTEST_ADDOPTS='-n auto -v'

%tox


%files -n python3-pytest-bdd -f %{pyproject_files}
%license LICENSE.txt
%if %{without doc}
%doc AUTHORS.rst CHANGES.rst README.rst
%endif
%{_bindir}/pytest-bdd
%{_mandir}/man1/pytest-bdd*.1*


%if %{with doc}
%files doc
%license LICENSE.txt
%doc AUTHORS.rst CHANGES.rst README.rst
%doc docs/_build/latex/Pytest-BDD.pdf
%endif


%changelog
%autochangelog
