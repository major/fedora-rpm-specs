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

BuildSystem:            pyproject
BuildOption(install):   -l pyrsistent _pyrsistent_version pvectorc
BuildOption(generate_buildrequires): requirements-filtered.txt

BuildRequires:  gcc

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

# Removed for Fedora 43; we can drop the Obsoletes after Fedora 46
Obsoletes:      python-pyrsistent-doc < 0.20.0-11

%description -n python3-pyrsistent %{common_description}


%prep -a
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
    requirements.txt | tee requirements-filtered.txt


%check -a
# See tox.ini:
%pytest %{?rhel:--ignore=tests/hypothesis_vector_test.py}
%pytest --doctest-modules pyrsistent


%files -n python3-pyrsistent -f %{pyproject_files}
%doc CHANGES.txt
%doc README.rst


%changelog
%autochangelog
