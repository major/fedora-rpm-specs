%bcond tests 1
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

%global _description %{expand:
NiaClass is a framework for solving classification tasks using nature-inspired
algorithms. The framework is written fully in Python. Its goal is to find the
best possible set of classification rules for the input data using the NiaPy
framework, which is a popular Python collection of nature-inspired algorithms.
The NiaClass classifier support numerical and categorical features.}

Name:           python-niaclass
Version:        0.2.4
Release:        %autorelease
Summary:        Python framework for building classifiers using nature-inspired algorithms

# SPDX
License:        MIT
URL:            https://github.com/firefly-cpp/NiaClass
Source:         %{url}/archive/%{version}/NiaClass-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# See [tool.poetry.dev-dependencies] in pyproject.toml; it mixes documentation,
# testing, and other dev dependencies such as linters, formatters, and
# coverage-analysis tools, so we must track these dependencies manually.
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# The HTML theme is imported in conf.py even for LaTeX builds.
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description %_description

%package -n python3-niaclass
Summary:        %{summary}

%description -n python3-niaclass %_description

%package doc
Summary:        Documentation and examples for python-niaclass

%description doc
%{summary}.

%prep
%autosetup -n NiaClass-%{version}
# The SemVer pins on dependencies are far too strict to be practical. Convert
# them to lower bounds.
sed -r -i 's/( = ")\^/\1>=/' pyproject.toml
# Similarly, we cannot respect an upper bound on the Python interpreter
# version.
sed -r -i 's/^(python = "[^"]+),[[:blank:]]*<[^"]+"/\1"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files niaclass

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-niaclass -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%doc CITATION.cff

%files doc
%license LICENSE
%doc CITATION.cff

%doc examples/

%if %{with doc_pdf}
%doc docs/_build/latex/niaclass.pdf
%endif

%changelog
%autochangelog
