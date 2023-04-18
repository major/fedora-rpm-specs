%global srcname dask

# Requires distributed, which is a loop.
# Also, some tests require packages that require dask itself.
# Force bootstrap for package review.
%bcond_without bootstrap

# We have an arched package to detect arch-dependent issues in dependencies,
# but all of the installable RPMs are noarch and there is no compiled code.
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        2023.4.0
%global tag     2023.4.0
Release:        %autorelease
Summary:        Parallel PyData with Task Scheduling

License:        BSD-3-Clause
URL:            https://github.com/dask/dask
Source0:        %{pypi_source %{srcname}}
# https://github.com/dask/dask/issues/6725
Patch:          0001-Skip-test_encoding_gh601-on-big-endian-machines.patch

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
# Fastavro does not support 32 bit architectures and is ExcludeArch:
# https://bugzilla.redhat.com/show_bug.cgi?id=1943932
%ifnarch %{arm32} %{ix86}
BuildRequires:  python3dist(fastavro)
%endif
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(psutil)
# libarrow does not support 32 bit architectures and is ExcludeArch.
# Tests don't pass on s390x either.
%ifnarch %{arm} %{ix86} s390x
BuildRequires:  python3dist(pyarrow)
%endif
BuildRequires:  python3dist(requests)
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


%pyproject_extras_subpkg -n python3-%{srcname} array bag dataframe delayed
%if %{without bootstrap}
%pyproject_extras_subpkg distributed
%endif


%if %{without bootstrap}
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
# we don't use pre-commit when running tests
sed -i '/"pre-commit"/d' setup.py


%generate_buildrequires
%pyproject_buildrequires -r -x test,array,bag,dataframe,delayed
%if %{without bootstrap}
%pyproject_buildrequires -x distributed
%endif


%build
%pyproject_wheel

%if %{without bootstrap}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files %{srcname}


%check
%ifarch arm
# Is there a way to do this in one line?
%global have_arm 1
%endif

%if 0%{?__isa_bits} == 32
# read_sql_query with meta converts dtypes from 32 to 64.
# https://github.com/dask/dask/issues/8620

# >           tm.assert_frame_equal(
#                 a, b, check_names=check_names, check_dtype=check_dtype, **kwargs
# E               AssertionError: Attributes of DataFrame.iloc[:, 1] (column name="age") are different
# E
# E               Attribute "dtype" are different
# E               [left]:  int32
# E               [right]: int64
# dask/dataframe/utils.py:555: AssertionError
k="${k-}${k+ and }not test_query_with_meta"
%endif

%ifarch ppc64le
# TODO: Should this be reported upstream? Is it a dask issue, or a numpy one?
# Possibly related to
# https://fedoraproject.org/wiki/Changes/PPC64LE_Float128_Transition?

# >           assert allclose(a, b, equal_nan=equal_nan, **kwargs), msg
# E           AssertionError: found values in 'a' and 'b' which differ by more than the allowed amount
# E           assert False
# E            +  where False = allclose(array([0.12586355-0.09957204j, 0.20256483+0.04098342j,\n       0.05781123-0.03588671j, 0.01135963-0.03334219j,\n       0.03747771+0.07495994j, 0.2106574 -0.0363521j ,\n       0.16352091+0.03782915j, 0.1381678 -0.06815128j,\n       0.03781295-0.04011523j, 0.01493269+0.07780643j]), array([0.12559072-0.07164038j, 0.20256483+0.05438578j,\n       0.05781123-0.03588671j, 0.01135963-0.03334219j,\n       0.03747771+0.07495994j, 0.2106574 -0.0363521j ,\n       0.16352091+0.03782915j, 0.1381678 -0.06815128j,\n       0.03781295-0.04011523j, 0.01493269+0.07780643j]), equal_nan=True, **{})
# dask/array/utils.py:361: AssertionError
k="${k-}${k+ and }not test_lstsq[100-10-10-True]"
# >           assert allclose(a, b, equal_nan=equal_nan, **kwargs), msg
# E           AssertionError: found values in 'a' and 'b' which differ by more than the allowed amount
# E           assert False
# E            +  where False = allclose(array([ 0.20168675+0.08857556j,  0.144233  -0.19173091j,\n       -0.03367557-0.08053959j,  0.04108325-0.24648308j,\n       -0.01844576+0.00841932j,  0.29652375+0.05682199j,\n        0.05551828+0.20156798j, -0.08409592+0.02354949j,\n        0.09848743-0.00748637j,  0.22889193-0.07372773j]), array([ 0.20067551+0.2642591j ,  0.144233  -0.18573336j,\n       -0.03367557-0.08053959j,  0.04108325-0.24648308j,\n       -0.01844576+0.00841932j,  0.29652375+0.05682199j,\n        0.05551828+0.20156798j, -0.08409592+0.02354949j,\n        0.09848743-0.00748637j,  0.22889193-0.07372773j]), equal_nan=True, **{})
# dask/array/utils.py:361: AssertionError
k="${k-}${k+ and }not test_lstsq[20-10-5-True]"

# test_vdot fails with NumPy 1.19.0
# https://github.com/dask/dask/issues/6406
#
# vdot returns incorrect results on ppc64le
# https://github.com/numpy/numpy/issues/17087

# >           assert allclose(a, b, equal_nan=equal_nan, **kwargs), msg
# E           AssertionError: found values in 'a' and 'b' which differ by more than the allowed amount
# E           assert False
# E            +  where False = allclose((0.38772781971416226-0.6851997484294434j), (0.38772781971416226-0.306563166009585j), equal_nan=True, **{})
# dask/array/utils.py:361: AssertionError
k="${k-}${k+ and }not test_vdot[shape0-chunks0]"
# >           assert allclose(a, b, equal_nan=equal_nan, **kwargs), msg
# E           AssertionError: found values in 'a' and 'b' which differ by more than the allowed amount
# E           assert False
# E            +  where False = allclose((0.38772781971416226-0.6851997484294434j), (0.38772781971416226-0.306563166009585j), equal_nan=True, **{})
# dask/array/utils.py:361: AssertionError
k="${k-}${k+ and }not test_vdot[shape1-chunks1]"
%endif

# This test compares against files in .github/. It does not work on the PyPI
# sdist, and is only relevant to upstream CI anyway.
#
# test_development_guidelines_matches_ci fails from sdist
# https://github.com/dask/dask/issues/8499
k="${k-}${k+ and }not test_development_guidelines_matches_ci"

pytest_args=(
  -m 'not network'

  -n %[0%{?have_arm}?"2":"auto"]

%ifarch %{ix86}
  # Ignore 32-bit warning
  -W 'ignore:invalid value encountered in cast:RuntimeWarning'
%endif

  -k "${k-}"

  --pyargs dask
)

cd docs
%{pytest} "${pytest_args[@]}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt dask/array/NUMPY_LICENSE.txt
%{_bindir}/dask

%if %{without bootstrap}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt dask/array/NUMPY_LICENSE.txt
%endif


%changelog
%autochangelog
