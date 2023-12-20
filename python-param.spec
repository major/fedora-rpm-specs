Name:           python-param
Version:        2.0.1
Release:        %autorelease
Summary:        Make your Python code clearer and more reliable by declaring Parameters

License:        BSD-3-Clause
# The GitHub tarball contains documentation, examples, and tests; the PyPI
# tarball does not. See:
# https://github.com/holoviz/param/issues/219
# https://github.com/holoviz/param/issues/103
URL:            https://github.com/holoviz/param
Source:         %{url}/archive/v%{version}/param-%{version}.tar.gz

# Downstream-only: don’t fail tests on warnings
#
# This makes sense for upstream development and CI, but is too strict and
# brittle for distribution packaging.
Patch:          0001-Downstream-only-don-t-fail-tests-on-warnings.patch

# The binary package is noarch, and there is no compiled code, but we allow the
# base package to be arched due to a history of platform-dependent test
# failures.
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# Additional test dependencies from the tests-full extra. We can’t use it
# directly because it includes tests-examples dependencies, and python-nbval
# and python-panel are not packaged.
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jsonschema}
# Upgrade gmpy support to gmpy2
# https://github.com/holoviz/param/issues/661
# BuildRequires:  %%{py3_dist gmpy}
BuildRequires:  %{py3_dist cloudpickle}
BuildRequires:  %{py3_dist nest_asyncio}

%global common_description %{expand:
Param is a library providing Parameters: Python attributes extended to have
features such as type and range checking, dynamically generated values,
documentation strings, default values, etc., each of which is inherited from
parent classes if not specified in a subclass.

Documentation and examples may be found at https://param.holoviz.org.}

%description %{common_description}


%package -n python3-param
Summary:        %{summary}

BuildArch:      noarch

%py_provides python3-numbergen

# The file param/version.py is derived from a forked copy of
# https://github.com/pyviz-dev/autover. See the comments at the top of the file
# for details. Note that we cannot unbundle this library because it is in the
# public API, so the fork matters.
Provides:       bundled(python3dist(autover)) = 0.2.5

%description -n python3-param %{common_description}


# We don’t generate any “extras” metapackages:
#   - “examples” doesn’t make sense because the examples aren’t installed
#   - “doc” is only for building documentation
#   - “tests*” and “lint” are only for testing and linting, respectively
#   - “all” is for development: it contains the unwanted doc/lint/test deps.


%prep
%autosetup -n param-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)("coverage)/\1# \2/' pyproject.toml


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x tests,tests-deser


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l param numbergen


%check
# Based on testing in a virtualenv, all of the following go away when pandas is
# upgraded past 2.0.
#
# E           ImportError: Can't determine version for tables
k="${k-}${k+ and }not (TestFileDeserialization and test_data_frame_hdf5)"
# E       Failed: DID NOT RAISE <class 'Exception'>
k="${k-}${k+ and }not test_parameterized_warns_explicit_no_ref"

%ifarch s390x
# Probably either a pandas bug or a pyarrow one. TODO: does this go away when
# pandas >= 2.0?
k="${k-}${k+ and }not (TestFileDeserialization and test_data_frame_parquet)"
%endif

%pytest -k "${k-}" -v


%files -n python3-param -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
