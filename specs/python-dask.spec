%global srcname dask

# Requires distributed, which is a loop.
# Also, some tests require packages that require dask itself.
# Force bootstrap for package review.
%bcond bootstrap 0
# We don't have all dependencies available yet.
%bcond docs 0

# We have an arched package to detect arch-dependent issues in dependencies,
# but all of the installable RPMs are noarch and there is no compiled code.
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        2025.4.1
%global tag     %{version}
Release:        %autorelease
Summary:        Parallel PyData with Task Scheduling

License:        BSD-3-Clause
URL:            https://github.com/dask/dask
Source0:        %{pypi_source %{srcname}}
# Fedora-specific patches.
Patch:          0001-Remove-extra-test-dependencies.patch
# https://github.com/dask/dask/pull/11892
Patch:          0002-XFAIL-test-if-NotImplementedError-is-raised.patch
# https://github.com/dask/dask/issues/12043
Patch:          0003-TST-Fall-back-to-cloudpickle-in-more-cases.patch
# https://github.com/dask/dask/pull/12047
Patch:          0004-TST-Fix-test_enforce_columns-on-Python-3.14.patch
# Allow an xfail to pass; may be due to the warning filter later.
Patch:          0005-Mark-test_combine_first_all_nans-as-a-non-strict-xfa.patch
# Fix compatibility with latest Pandas.
Patch:          https://github.com/dask/dask/commit/7751beb21807fa7f206079b8f69bf887ec16a199.patch

# Stop building on i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Dask is a flexible parallel computing library for analytics.


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(graphviz)
BuildRequires:  python3dist(ipython)
%if %{without bootstrap}
BuildRequires:  python3dist(scikit-image)
BuildRequires:  python3dist(xarray)
%endif
# Optional test requirements.
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(bottleneck)
BuildRequires:  python3dist(crick)
BuildRequires:  python3dist(fastavro)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(python-snappy)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(tables)
BuildRequires:  python3dist(zarr)

Recommends:     python3-%{srcname}+array = %{version}-%{release}
Recommends:     python3-%{srcname}+bag = %{version}-%{release}
Recommends:     python3-%{srcname}+dataframe = %{version}-%{release}
Recommends:     python3-%{srcname}+delayed = %{version}-%{release}
%if %{without bootstrap}
Recommends:     python3-%{srcname}+distributed = %{version}-%{release}
%endif
# No recent enough Bokeh is packaged
Obsoletes:      python3-%{srcname}+diagnostics < 2022.5.0-1
# dask-expr is part of dask since version 2025.1.0
Obsoletes:      python3-dask-expr < 2025.1.0
Obsoletes:      python3-dask-expr+analyze < 2025.1.0

# There is nothing that can be unbundled; there are some some snippets forked
# or copied from unspecified versions of numpy, under a BSD-3-Clause license
# similar to that of dask itself.
#
# - dask/array/numpy_compat.py:
#     _Recurser, moveaxis, rollaxis, sliding_window_view
# - dask/array/backends.py:
#     _tensordot
# - dask/array/core.py:
#     block
# - dask/array/einsumfuncs.py:
#     parse_einsum_input
# - dask/array/routines.py:
#     cov, _average
Provides:       bundled(numpy)

%description -n python3-%{srcname}
Dask is a flexible parallel computing library for analytics.


%pyproject_extras_subpkg -n python3-%{srcname} -a array bag dataframe delayed
%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-%{srcname} -a distributed
%endif


%if %{with docs}
%package -n python-%{srcname}-doc
Summary:        dask documentation

BuildArch:      noarch

BuildRequires:  python3dist(dask_sphinx_theme) >= 1.3.5
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx) >= 4

%description -n python-%{srcname}-doc
Documentation for dask.
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -x test,array,bag,dataframe,delayed
%if %{without bootstrap}
%pyproject_buildrequires -x distributed
%endif


%build
%pyproject_wheel

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l %{srcname}


%check
# This test compares against files in .github/. It does not work on the PyPI
# sdist, and is only relevant to upstream CI anyway.
#
# test_development_guidelines_matches_ci fails from sdist
# https://github.com/dask/dask/issues/8499
k="${k-}${k+ and }not test_development_guidelines_matches_ci"

# Fails with Python 3.14: https://github.com/dask/dask/issues/12042
%if 0%{?fedora} >= 43
k="${k-}${k+ and }not test_multiple_repartition_partition_size"
%endif

# Previously excluded for dask-expr. Those tests use parquet files,
# which involves pyarrow.
%ifarch s390x
k="${k-}${k+ and }not test_combine_similar_no_projection_on_one_branch"
k="${k-}${k+ and }not test_parquet_all_na_column"
%endif

pytest_args=(
  -m 'not network'

  -n "auto"

  -k "${k-}"

# Ignore warnings about Pandas deprecations, which should be fixed in the next release.
  -W 'ignore::FutureWarning'

# arrow tests all fail on s390x, it's not at all BE-safe
# https://github.com/dask/dask/issues/11186
%ifarch s390x
  --ignore %{srcname}/dataframe/io/tests/test_parquet.py
%endif

  # Upstream uses 'thread' for Windows, but that kills the whole session, and
  # we'd like to see exactly which tests fail.
  --timeout_method=signal

  --import-mode=importlib
)

%{pytest} "${pytest_args[@]}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license dask/array/NUMPY_LICENSE.txt
%{_bindir}/dask

%if %{with docs}
%files -n python-%{srcname}-doc
%doc html
%license dask/array/NUMPY_LICENSE.txt
%endif


%changelog
%autochangelog
