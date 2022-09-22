# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-pytest-bdd
Version:        5.0.0
Release:        %autorelease
Summary:        BDD library for the py.test runner

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

# Documentation
%if %{with doc_pdf}
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


%package        doc
Summary:        Documentation for pytest-bdd

%description    doc %{common_description}


%prep
%autosetup -n pytest-bdd-%{version}

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files pytest_bdd
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'


%check
# Work around unexpected PytestAssertRewriteWarning with pip 21.3
# https://github.com/pytest-dev/pytest-bdd/issues/453
mkdir -p _empty && cp -rp tests *.ini _empty && cd _empty

%pytest -n %{?_smp_build_ncpus}


%files -n python3-pytest-bdd -f %{pyproject_files}
%{_bindir}/pytest-bdd
%{_mandir}/man1/pytest-bdd.1*


%files doc
%license LICENSE.txt
%doc AUTHORS.rst
%doc CHANGES.rst
%doc README.rst
%if %{with doc_pdf}
%doc docs/_build/latex/Pytest-BDD.pdf
%endif


%changelog
%autochangelog
