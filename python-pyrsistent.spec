# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-pyrsistent
Summary:        Persistent/Functional/Immutable data structures
Version:        0.18.1
Release:        %autorelease

# The entire source is MIT, except pyrsistent/_toolz.py which is BSD.
License:        MIT and BSD
URL:            https://github.com/tobgu/pyrsistent/
Source0:        %{url}/archive/v%{version}/pyrsistent-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc

# For Sphinx documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

# ============================================================================
# From setup_requires in setup.py, when tests are to be executed:
BuildRequires:  python3dist(pytest-runner)

# Note that pyrsistent/_toolz.py contains a bit of code ported from toolz, but
# not enough to constitute a bundled dependency.

%global common_description %{expand:
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

All methods on a data structure that would normally mutate it instead
return a new copy of the structure containing the requested updates. The
original structure is left untouched.}

%description %{common_description}


%package -n     python3-pyrsistent
Summary:        %{summary}

%description -n python3-pyrsistent %{common_description}


%package        doc
Summary:        Documentation for pyrsistent

BuildArch:      noarch

%description doc %{common_description}


%prep
%autosetup -n pyrsistent-%{version} -p1

# Loosen exact-version pins in requirements.txt; we must tolerate newer
# versions and use what is packaged.
#
# We do not need:
#   - memory-profiler or psutil, since we are not running the memorytest*
#     environment from tox.ini
#   - pyperform, since we are not running the benchmarks from
#     performance_suites/
#   - tox, since we are not using tox to run the tests
#   - twine, since it is for maintainer PyPI uploads
sed -r \
    -e 's/==/>=/' \
    -e '/\b(memory-profiler|psutil|pyperform|tox|twine)\b/d' \
    requirements.txt | tee requirements-filtered.txt


%generate_buildrequires
%pyproject_buildrequires -r requirements-filtered.txt


%build
%pyproject_wheel

# Default SPHINXOPTS are '-W -n', but -W turns warnings into errors and there
# are some warnings. We want to build the documentation as best we can anyway.
# Additionally, we parallelize sphinx-build.
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='-n %{?_smp_mflags}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files pyrsistent _pyrsistent_version pvectorc


%check
# # See tox.ini:
%pytest
%pytest --doctest-modules pyrsistent


%files -n python3-pyrsistent -f %{pyproject_files}


%files doc
%license LICENSE.mit
%doc CHANGES.txt
%doc README.rst
%if %{with doc_pdf}
%doc docs/build/latex/Pyrsistent.pdf
%endif


%changelog
%autochangelog
