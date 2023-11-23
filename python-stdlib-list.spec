# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:       python-stdlib-list
Version:    0.10.0
Release:    %autorelease
Summary:    A list of Python Standard Libraries

# SPDX
License:    MIT
URL:        https://github.com/pypi/stdlib-list
# pypi is missing docs, so use the github tarball instead
Source:     %{url}/archive/v%{version}/stdlib-list-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
# We BR this manually since the other dependencies in the “test” extra are for
# coverage analysis and are unwanted
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
BuildRequires:  %{py3_dist pytest}

%global desc %{expand:
This package includes lists of all of the standard libraries for Python.}

%description %{desc}

%package -n python3-stdlib-list
Summary:    %{summary}

%description -n python3-stdlib-list %{desc}

%package doc
Summary:   Documentation for python-stdlib-list

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc
%{summary}.

%prep
%autosetup -n stdlib-list-%{version}
# We don’t need the HTML theme to build PDF documentation:
sed -r -i 's/, "furo"//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:-x doc}

%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files stdlib_list

%check
%pytest

%files -n python3-stdlib-list -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/PythonStandardLibraryList.pdf
%endif

%changelog
%autochangelog
