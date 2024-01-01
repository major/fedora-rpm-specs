# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond docs 1

Name:           python-wrapt
Version:        1.16.0
Release:        %autorelease
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD-2-Clause
URL:            https://github.com/GrahamDumpleton/wrapt
Source:         %{url}/archive/%{version}/wrapt-%{version}.tar.gz

BuildRequires:  gcc

BuildRequires:  python3-devel

# We bypass tox and instead BR and use pytest directly; this is simpler and
# avoids the need to patch out coverage analysis
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.}

%description %_description

%package -n python3-wrapt
Summary:        %{summary}

%description -n python3-wrapt %_description

%if %{with docs}
%package doc
Summary:        Documentation for the wrapt module

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# docs/requirements.txt
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%description doc
%{summary}.
%endif

%prep
%autosetup -n wrapt-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l wrapt

%check
%pytest -v

%if %{with docs}
%files doc
%license LICENSE
%doc docs/_build/latex/wrapt.pdf
%endif

%files -n python3-wrapt -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
