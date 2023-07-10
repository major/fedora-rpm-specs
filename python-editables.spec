# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
# Not all doc requirements are available in RHEL
%bcond doc %{undefined rhel}

Name:           python-editables
Version:        0.4
Release:        %autorelease
Summary:        Editable installations

# SPDX
License:        MIT
URL:            https://github.com/pfmoore/editables
# PyPI source distributions lack tests; use the GitHub archive
Source:         %{url}/archive/%{version}/editables-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Most of the dependencies, and all of the pytest options, in tox.ini are for
# coverage analysis and for installation with pip/virtualenv. Rather than
# working around all of these, it is simpler not to use tox for dependency
# generation or testing.
BuildRequires:  python3dist(pytest)

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex(pict2e.sty)
%endif

%global common_description %{expand:
A Python library for creating “editable wheels”

This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in “editable mode”. In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.}

%description %{common_description}


%package -n python3-editables
Summary:        %{summary}

%description -n python3-editables %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation for python-editables

%description    doc %{common_description}
%endif


%prep
%autosetup -n editables-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_doc:docs/requirements.txt}


%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files editables


%check
%pytest


%files -n python3-editables -f %{pyproject_files}
%license LICENSE.txt
%if %{without doc}
%doc CHANGELOG.md
%doc README.md
%endif


%if %{with doc}
%files doc
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%doc docs/build/latex/editables.pdf
%endif


%changelog
%autochangelog
