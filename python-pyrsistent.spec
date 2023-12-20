# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-pyrsistent
Summary:        Persistent/Functional/Immutable data structures
Version:        0.20.0
Release:        %autorelease

# The entire source is (SPDX) MIT, except pyrsistent/_toolz.py which is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/tobgu/pyrsistent/
Source:         %{url}/archive/v%{version}/pyrsistent-%{version}.tar.gz

# Replace _PyList_Extend with PyList_SetSlice
# https://github.com/tobgu/pyrsistent/pull/284
#
# Together with the 0.20.0 release, this fixes:
#
# python-pyrsistent fails to build with Python 3.13: implicit declaration of
# function ‘Py_TRASHCAN_SAFE_BEGIN’, ‘Py_TRASHCAN_SAFE_END’, ‘_PyList_Extend’
# https://bugzilla.redhat.com/show_bug.cgi?id=2246349
Patch:          %{url}/pull/284.patch

BuildRequires:  python3-devel
BuildRequires:  gcc

# For Sphinx documentation
%if %{with doc}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

# There is fancy machinery in setup.py to add pytest-runner to setup_requires
# in setup.py when it looks like tests are to be executed. Since we will not use
# “python3 setup.py test” to run tests, we can do without this dependency.

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


%if %{with doc}
%package        doc
Summary:        Documentation for pyrsistent
# The Sphinx documentation does contain content based on pyrsistent/_toolz.py,
# so the full License carries over from the base package.

BuildArch:      noarch

%description doc %{common_description}
%endif


%prep
%autosetup -n pyrsistent-%{version} -p1

# Remove all version pins for documentation dependencies. These tend to just be
# the latest versions at the time of release, and are generally not based on
# any particular analysis. In any case, we must attempt to use whatever is
# packaged.
sed -r 's/[>=]=.*//' docs/requirements.in | tee docs/requirements.in.unpinned

# Loosen exact-version pins in requirements.txt; we must tolerate newer
# versions and use what is packaged.
#
# We do not need:
#   - hypothesis, not included in RHEL
#   - memory-profiler or psutil, since we are not running the memorytest*
#     environment from tox.ini
#   - pip-tools, since it is for making pinned requirements files
#   - pyperform, since we are not running the benchmarks from
#     performance_suites/
#   - tox, since we are not using tox to run the tests
#   - twine, since it is for maintainer PyPI uploads

sed -r \
    -e 's/==/>=/' \
    -e '/\b(memory-profiler|pip-tools|psutil|pyperform|tox|twine)\b/d' \
%if %{defined rhel}
    -e '/\bhypothesis\b/d' \
%endif
    requirements.txt %{?with_doc:docs/requirements.in.unpinned} |
  tee requirements-filtered.txt


%generate_buildrequires
%pyproject_buildrequires requirements-filtered.txt


%build
%pyproject_wheel

# Default SPHINXOPTS are '-W -n', but -W turns warnings into errors and there
# are some warnings. We want to build the documentation as best we can anyway.
# Additionally, we parallelize sphinx-build.
%if %{with doc}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-n -j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l pyrsistent _pyrsistent_version pvectorc


%check
# See tox.ini:
%pytest %{?rhel:--ignore=tests/hypothesis_vector_test.py}
%pytest --doctest-modules pyrsistent


%files -n python3-pyrsistent -f %{pyproject_files}
%if %{without doc}
%doc CHANGES.txt README.rst
%endif


%if %{with doc}
%files doc
%license LICENSE.mit
%doc CHANGES.txt README.rst
%doc docs/build/latex/Pyrsistent.pdf
%endif


%changelog
%autochangelog
