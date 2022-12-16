# We need to break some cycles with optional dependencies for bootstrapping;
# given that a conditional is needed, we take the opportunity to omit as many
# optional dependencies as possible for bootstrapping.
%bcond_with bootstrap

# When not bootstrapping, run tests?
%bcond_without tests
%{?with_bootstrap:%undefine with_tests}
# When running tests, run ones that are marked as slow?
%bcond_without slow_tests
# When running tests, run ones that cannot be run in parallel?
%bcond_without single_tests

Name:           python-pandas
Version:        1.5.2
Release:        1%{?dist}
Summary:        Python library providing high-performance data analysis tools

# The entire source is BSD-3-Clause and covered by LICENSE, except:
#
# - pandas/util/version/__init__.py is (Apache-2.0 OR BSD-2-Clause): see
#   LICENSES/PACKAGING_LICENSE
# - pandas/_libs/src/headers/portable.h is (BSD-3-Clause AND MIT), because it
#   contains some trivial content under the overall BSD-3-Clause license but
#   also some macros from MUSL libc under the MIT license: see
#   LICENSES/MUSL_LICENSE
# - pandas/_libs/src/parser/tokenizer.c is (BSD-3-Clause AND Python-2.0.1): see
#   LICENSES/PSF_LICENSE
# - pandas/io/sas/sas7bdat.py is (BSD-3-Clause and MIT), because it is mostly
#   under the overall BSD-3-Clause license but is also based on
#   https://bitbucket.org/jaredhobbs/sas7bdat: see LICENSES/SAS7BDAT_LICENSE
# - pandas/core/accessor.py is (BSD-3-Clause AND Apache-2.0), because it is
#   partially under the overall BSD-3-Clause license but is also based on
#   xarray: see LICENSES/XARRAY_LICENSE
# - pandas/_libs/src/klib/khash.h is MIT: see LICENSES/KLIB_LICENSE
# - pandas/_libs/window/aggregations.pyx is (BSD-3-Clause AND BSD-2-Clause):
#   see “Bottleneck license” in LICENSES/OTHER
#
# In the python3-pandas+tests subpackage:
#
# - pandas/tests/io/data/spss/*.sav are MIT: see LICENSES/HAVEN_LICENSE and
#   LICENSES/HAVEN_MIT
# - pandas/tests/window/test_rolling.py is (BSD-3-Clause AND BSD-2-Clause)
#   since test_rolling_std_neg_sqrt is from Bottleneck: see “Bottleneck license”
#   in LICENSES/OTHER
#
# Additionally:
#
# - pandas/_libs/tslibs/parsing.pyx is BSD-3-Clause rather than
#   (BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0)), because it appears that at
#   least some trivial content in the code copied from dateutil in the
#   dateutil_parse() function (as of
#   https://github.com/dateutil/dateutil/pull/732) is by dateutil contributors
#   who have not agreed to re-license their previously submitted code: see
#   LICENSES/DATEUTIL_LICENSE.
# - LICENSES/OTHER suggests that some code may be derived from
#   google-api-python-client under Apache-2.0, but a search for attribution
#   comments did not turn up anything specific
# - pandas/_libs/tslibs/src/datetime/np_datetime.{h,c} are still BSD-3-Clause,
#   but see also LICENSES/NUMPY_LICENSE
# - pandas/io/clipboard/ is still BSD-3-Clause, but see also “Pyperclip v1.3
#   license” in LICENSES/OTHER
# - pandas/_testing/__init__.py is still BSD-3-Clause, but see also
#   LICENSES/SCIPY_LICENSE
# - pandas/_libs/src/ujson/lib/ is still BSD-3-Clause, but under
#   LICENSES/ULTRAJSON_LICENSE
#
# Additionally, the following are not packaged and so do not affect the overall
# License field:
#
# - scripts/no_bool_in_generic.py is MIT: see LICENSES/PYUPGRADE_LICENSE
License:        BSD-3-Clause AND (Apache-2.0 OR BSD-2-Clause) AND (BSD-3-Clause AND Apache-2.0) AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause AND Python-2.0.1) AND MIT AND (BSD-3-Clause AND BSD-2-Clause)
URL:            https://pandas.pydata.org/
# The GitHub archive contains tests; the PyPI sdist does not.
Source0:        https://github.com/pandas-dev/pandas/archive/v%{version}/pandas-%{version}.tar.gz

# Fix some little-endian assumptions in the tests
# https://github.com/pandas-dev/pandas/pull/49913
Patch:          https://github.com/pandas-dev/pandas/pull/49913.patch

%global _description %{expand:
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.}

%description %_description


%package -n python3-pandas
Summary:        %{summary}

# pandas/_libs/window/aggregations.pyx:
#
#   Moving maximum / minimum code taken from Bottleneck under the terms
#   of its Simplified BSD license
#   https://github.com/pydata/bottleneck
#
# These snippets are extracted from Bottleneck’s internals and cannot be
# replaced by calling the public Bottleneck API, so there is no reasonable path
# to unbundling.
Provides:       bundled(python3dist(bottleneck))

# pandas/_libs/tslibs/parsing.pyx:
#
# Contains a routine, dateutil_parse(), from an unspecified version of dateutil
#
# Cannot be unbundled because the function is forked and compiled as Cython
Provides:       bundled(python3dist(dateutil))

# pandas/_libs/src/klib/khash.h:
#
# From klib (https://github.com/attractivechaos/klib); it is not practical to
# package all of klib separately because it is designed as a copylib, and many
# of its components are not header-only.
Provides:       bundled(klib-khash) = 0.2.6

# pandas/_libs/src/headers/portable.h:
#
# Contains several preprocessor macros from an unspecified version of MUSL libc
#
# Cannot be unbundled because the macros are not directly exposed in the libc
Provides:       bundled(musl-libc)

# pandas/_libs/tslibs/src/datetime/np_datetime.{h,c}:
#
# Derived from Numpy 1.7
#
# Cannot be unbundled because the routines are forked.
Provides:       bundled(python3dist(numpy)) = 1.7

# pandas/util/version/__init__.py:
#
# Vendored from https://github.com/pypa/packaging/blob/main/packaging/_structures.py
# and https://github.com/pypa/packaging/blob/main/packaging/_structures.py
# changeset ae891fd74d6dd4c6063bb04f2faeadaac6fc6313
# 04/30/2021
#
# Cannot be (reasonably) unbundled because the vendored file is not part of
# packaging’s public API.
Provides:       bundled(python3dist(packaging)) = 20.10.dev0^20210430gitae891fd

# pandas/io/clipboard/:
#
# In https://github.com/pandas-dev/pandas/pull/28471, upstream considered and
# rejected the idea of de-vendoring pyperclip. Furthermore,
# https://github.com/pandas-dev/pandas/commits/main/pandas/io/clipboard and
# https://github.com/pandas-dev/pandas/commits/main/pandas/io/clipboard/__init__.py
# show that the vendored library has accrued Pandas-specific changes.
#
# Version number from:
# https://github.com/pandas-dev/pandas/pull/28471/commits/33cd2d72e0c007c460e59105efda9211441b2ce4
# “Updated internal pyperclip 1.5.27 -> 1.7.0”
Provides:       bundled(python3dist(pyperclip)) = 1.7.0

# pandas/_libs/src/parser/tokenizer.c:
#
# Combines some elements from Python's built-in csv module and Warren
# Weckesser's textreader project on GitHub.
#
# Elements from these are both forked and cannot be unbundled. The textreader
# project is a Python extension but is not on PyPI, and is not the same as
# python3dist(textreader).
Provides:       bundled(python3-libs)
Provides:       bundled(textreader)

# scripts/no_bool_in_generic.py:
#
# The function `visit` is adapted from a function by the same name in pyupgrade:
# https://github.com/asottile/pyupgrade/blob/5495a248f2165941c5d3b82ac3226ba7ad1fa59d/pyupgrade/_data.py#L70-L113
#
# Not packaged (pre-commit hook) therefore not bundled
# Provides:       bundled(python3dist(pyupgrade)) = 2.11.0^20210201git5495a24

# pandas/io/sas/sas7bdat.py
#
# Based on code written by Jared Hobbs:
#   https://bitbucket.org/jaredhobbs/sas7bdat
#
# Cannot be unbundled because the code is modified, not directly copied
Provides:       bundled(python3dist(sas7bdat))

# pandas/_testing/__init__.py: in _create_missing_idx():
#
#   below is cribbed from scipy.sparse
#
# Cannot be unbundled because only a few lines are copied, not a standalone
# function that we can call
Provides:       bundled(python3dist(scipy))

# pandas/_libs/src/ujson/lib/:
#
# This is a stripped-down copy of UltraJSON. It would be an obvious target for
# unbundling, except:
#
# - Pandas uses the C library API, but UltraJSON upstream does not support
#   building and installing it separately from the Python package.
# - In https://github.com/pandas-dev/pandas/issues/24711 it is suggested that
#   Pandas might rely on features of the particular vendored version of
#   UltraJSON. It’s not immediately clear whether this is still true or not.
Provides:       bundled(python3dist(ujson))

# pandas/core/accessor.py
#
#   Ported with modifications from xarray
#   https://github.com/pydata/xarray/blob/master/xarray/core/extensions.py
#   1. We don't need to catch and re-raise AttributeErrors as RuntimeErrors
#   2. We use a UserWarning instead of a custom Warning
#
# Cannot be unbundled because the copied code is forked.
Provides:       bundled(python3dist(xarray))

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  python3-devel

# Since numpy is imported in setup.py, we need it to generate BR’s. This only
# becomes obvious during bootstrapping, in which the many optional dependencies
# that indirectly require numpy are removed.
BuildRequires:  python3dist(numpy)

%if %{without bootstrap}

# doc/source/getting_started/install.rst “Recommended dependencies”
# Since these provide large speedups, we make them hard dependencies except
# during bootstrapping.
BuildRequires:  python3dist(numexpr) >= 2.7.3
Requires:       python3dist(numexpr) >= 2.7.3
BuildRequires:  python3dist(bottleneck) >= 1.3.2
Requires:       python3dist(bottleneck) >= 1.3.2

# doc/source/getting_started/install.rst “Optional dependencies”
# We BR all weak dependencies to ensure they are installable.

# Timezones
BuildRequires:  tzdata >= 2022a
Recommends:     tzdata >= 2022a

# Visualization
BuildRequires:  python3dist(matplotlib) >= 3.3.2
Recommends:     python3dist(matplotlib) >= 3.3.2
BuildRequires:  python3dist(jinja2) >= 3
Recommends:     python3dist(jinja2) >= 3
BuildRequires:  python3dist(tabulate) >= 0.8.9
Recommends:     python3dist(tabulate) >= 0.8.9

# Computation
BuildRequires:  python3dist(scipy) >= 1.7.1
Recommends:     python3dist(scipy) >= 1.7.1
# python-numba is not currently packaged:
# BuildRequires:  python3dist(numba) >= 0.46
# Recommends:     python3dist(numba) >= 0.46
BuildRequires:  python3dist(xarray) >= 1.19
Recommends:     python3dist(xarray) >= 1.19

# Excel files
BuildRequires:  python3dist(xlrd) >= 2.0.1
Recommends:     python3dist(xlrd) >= 2.0.1
BuildRequires:  python3dist(xlwt) >= 1.3
Recommends:     python3dist(xlwt) >= 1.3
BuildRequires:  python3dist(xlsxwriter) >= 1.4.3
Recommends:     python3dist(xlsxwriter) >= 1.4.3
BuildRequires:  python3dist(openpyxl) >= 3.0.7
Recommends:     python3dist(openpyxl) >= 3.0.7
# python-pyxlsb is not currently packaged:
# BuildRequires:  python3dist(pyxlsb) >= 1.0.8
# Recommends:     python3dist(pyxlsb) >= 1.0.8
# Not in doc/source/getting_started/install.rst, but in environment.yml and in
# some doc-strings:
BuildRequires:  python3dist(odfpy) >= 1.4.1
Recommends:     python3dist(odfpy) >= 1.4.1

# HTML
BuildRequires:  python3dist(beautifulsoup4) >= 4.9.3
Recommends:     python3dist(beautifulsoup4) >= 4.9.3
BuildRequires:  python3dist(html5lib) >= 1.1
Recommends:     python3dist(html5lib) >= 1.1
# lxml handled below:

# XML
BuildRequires:  python3dist(lxml) >= 4.6.3
Recommends:     python3dist(lxml) >= 4.6.3

# SQL databases
BuildRequires:  python3dist(sqlalchemy) >= 1.4.16
Recommends:     python3dist(sqlalchemy) >= 1.4.16
BuildRequires:  python3dist(psycopg2) >= 2.8.6
Recommends:     python3dist(psycopg2) >= 2.8.6
BuildRequires:  python3dist(pymysql) >= 1.0.2
Recommends:     python3dist(pymysql) >= 1.0.2

# Other data sources
BuildRequires:  python3dist(tables) >= 3.6.1
Recommends:     python3dist(tables) >= 3.6.1
# Dependencies on blosc and zlib are indirect, via PyTables, so we do not
# encode them here. Note also that the minimum blosc version in the
# documentation seems to be that of the blosc C library, not of the blosc PyPI
# package.
# python-fastparquet is not currently packaged:
# BuildRequires:  python3dist(fastparquet) >= 0.4
# Recommends:     python3dist(fastparquet) >= 0.4
# libarrow does not support 32-bit architectures:
%if 0%{?__isa_bits} != 32
BuildRequires:  python3dist(pyarrow) >= 1.0.1
Recommends:     python3dist(pyarrow) >= 1.0.1
%endif
# python-pyreadstat is not currently packaged:
# BuildRequires:  python3dist(pyreadstat) >= 1.1.2
# Recommends:     python3dist(pyreadstat) >= 1.1.2

# Access data in the cloud
BuildRequires:  python3dist(fsspec) >= 2021.7
Recommends:     python3dist(fsspec) >= 2021.7
# python-gcsfs is packaged, but is badly out of date in F37 and older:
# https://bugzilla.redhat.com/show_bug.cgi?id=2136233
# Since we will not package pandas 1.5.x for F36 and older, the conditional
# checks for F37 only.
%if !0%{?fc37}
BuildRequires:  python3dist(gcsfs) >= 2021.7
Recommends:     python3dist(gcsfs) >= 2021.7
%endif
# python-pandas-gbq is not currently packaged:
# BuildRequires:  python3dist(pandas-gbq) >= 0.15
# Recommends:     python3dist(pandas-gbq) >= 0.15
# python-s3fs is not currently packaged:
# BuildRequires:  python3dist(s3fs) >= 2021.8
# Recommends:     python3dist(s3fs) >= 2021.8

# Clipboard
BuildRequires:  python3dist(pyqt5)
Recommends:     python3dist(pyqt5)
BuildRequires:  python3dist(qtpy)
Recommends:     python3dist(qtpy)
BuildRequires:  xclip
Recommends:     xclip
BuildRequires:  xsel
Recommends:     xsel

# Compression
BuildRequires:  python3dist(brotli) >= 0.7
Recommends:     python3dist(brotli) >= 0.7
BuildRequires:  python3dist(python-snappy) >= 0.6
Recommends:     python3dist(python-snappy) >= 0.6
BuildRequires:  python3dist(zstandard) >= 0.15.2
Recommends:     python3dist(zstandard) >= 0.15.2

# This is just an “ecosystem” package in the upstream documentation, but there
# is an integration test for it. This package historically had a weak
# dependency on it, which we keep around until we package 1.4.0 to ensure
# backward compatibility.
BuildRequires:  python3dist(pandas-datareader)
Recommends:     python3dist(pandas-datareader)

%endif

%description -n python3-pandas %_description


%package -n python3-pandas+test
Summary:        Tests and test extras for Pandas

# See comment above base package License tag for licensing breakdown.
License:        BSD-3-Clause AND MIT

Requires:       python3-pandas%{?_isa} = %{version}-%{release}

%if %{without bootstrap}

# Additional BR’s and weak dependencies below are generally those that don’t
# provide enough added functionality to be weak dependencies of the library
# package, but for which there is some integration support and additional tests
# that can be enabled.

# Additional dependencies from environment.yml: “testing”
# Those not in the “test” extra are treated as weak dependencies for the tests.
BuildRequires:  python3dist(boto3)
Recommends:     python3dist(boto3)
BuildRequires:  python3dist(botocore) >= 1.11
Recommends:     python3dist(botocore) >= 1.11
# Already covered by “test” extra
# BuildRequires:  python3dist(hypothesis) >= 3.82
# Recommends:     python3dist(hypothesis) >= 3.82
# python-moto is not yet packaged
# BuildRequires:  python3dist(moto)
# Recommends:     python3dist(moto)
BuildRequires:  python3dist(flask)
Recommends:     python3dist(flask)
# Already covered by “test” extra
# BuildRequires:  python3dist(pytest) >= 5.0.1
# Requires:       python3dist(pytest) >= 5.0.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# BuildRequires:  python3dist(pytest-cov)
# Recommends:     python3dist(pytest-cov)
# Already covered by “test” extra
# BuildRequires:  python3dist(pytest-xdist) >= 1.21
# Requires:       python3dist(pytest-xdist) >= 1.21
BuildRequires:  python3dist(pytest-asyncio)
Recommends:     python3dist(pytest-asyncio)
# python-pytest-instafail is not yet packaged
# BuildRequires:  python3dist(pytest-instafail)
# Recommends:     python3dist(pytest-instafail)

# Additional dependencies from environment.yml:
# “Dask and its dependencies (that dont install with dask)”
# Asks for dask-core, but we just have dask
BuildRequires:  python3dist(dask)
Recommends:     python3dist(dask)
BuildRequires:  python3dist(toolz) >= 0.7.3
Recommends:     python3dist(toolz) >= 0.7.3
BuildRequires:  python3dist(partd) >= 0.3.10
Recommends:     python3dist(partd) >= 0.3.10
BuildRequires:  python3dist(cloudpickle) >= 0.2.1
Recommends:     python3dist(cloudpickle) >= 0.2.1

# Additional dependencies from environment.yml: “downstream tests”
BuildRequires:  python3dist(seaborn)
Recommends:     python3dist(seaborn)
BuildRequires:  python3dist(statsmodels)
Recommends:     python3dist(statsmodels)

# environment.yml: Needed for downstream xarray.CFTimeIndex test
BuildRequires:  python3dist(cftime)
Recommends:     python3dist(cftime)

# environment.yml: optional
BuildRequires:  python3dist(ipython) >= 7.11.1
Recommends:     python3dist(ipython) >= 7.11.1

# pandas/tests/io/data/spss/*.sav:
#
# From Haven
Provides:       bundled(R-haven)

# pandas/tests/window/test_rolling.py: test_rolling_std_neg_sqrt()
#
#   unit test from Bottleneck
#
# There is no reasonable path to unbundling a single unit test.
Provides:       bundled(python3dist(bottleneck))

%endif


%description -n python3-pandas+test
These are the tests for python3-pandas. This package:

• Provides the “pandas.tests” package
• Makes sure the “test” extra dependencies are installed
• Carries additonal weak dependencies for running the tests


%prep
%autosetup -n pandas-%{version} -p1

# Ensure Cython-generated sources are re-generated
rm -vf $(grep -rl '/\* Generated by Cython')

# We just want to build with the numpy in Fedora:
sed -r -i '/\boldest-supported-numpy\b/d' pyproject.toml
%if 0%{?fc37}
# We have Python 3.11, but we do not have the numpy version that Pandas upstrem
# wants for Python 3.11.
sed -r -i "s/(numpy>=)1\\.23\\.2(; python_version>='3\\.11')/\\11.22.0\\2/" \
    setup.cfg
%endif


%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pandas


%check
%if %{with tests}

# Clipboard tests don’t run without a graphical session, and it’s not worth
# using xvfb-run just for them.
m="${m-}${m+ and }not clipboard"
%if %{without single_tests}
m="${m-}${m+ and }not single"
%endif

# This test allocates a huge amount of memory (~12GB), which causes flaky OOM
# failures on some builders. It’s not worth it.
# https://github.com/pandas-dev/pandas/issues/45223#issuecomment-1250912663
k="${k-}${k+ and }not test_bytes_exceed_2gb"

# This test (only) expects the current working directory to be the
# site-packages directory containing the built pandas. This is not how we run
# the tests, because we don’t want to clutter the buildroot with
# testing-related hidden files and directories. We could run tests from
# %%pyproject_build_lib if this were a problem for a lot of tests, but it’s
# easier just to skip it.
k="${k-}${k+ and }not test_html_template_extends_options"

%ifarch ppc64le s390x
# TODO: Why does this fail? The differences are large!
k="${k-}${k+ and }not test_rolling_var_numerical_issues"
%endif

%ifarch %{ix86}
# These failures are i686-specific; most are likely 32-bit issues. It’s not
# really worth trying to fix them.

# This “high-memory” test is just not appropriate for 32-bit platforms:
# E       OverflowError: join() result is too long for a Python string
k="${k-}${k+ and }not test_bytes_exceed_2gb[c_high]"

# E           assert 243.164 == 243.16400000000002
# Fails for both [c_high] and [c_low].
k="${k-}${k+ and }not test_float_precision_options"

# E   AssertionError: DataFrame.iloc[:, 2] (column name="C") are different
# E
# E   DataFrame.iloc[:, 2] (column name="C") values are different (11.66363 %)
# E   [index]: [0, 1, …
# Fails for [left], [right], [outer], and [inner]
k="${k-}${k+ and }not (TestMerge and test_int64_overflow_how_merge)"

# E           AssertionError: Attributes of DataFrame.iloc[:, 1] (column name="b") are different
# E
# E           Attribute "dtype" are different
# E           [left]:  int32
# E           [right]: int64
k="${k-}${k+ and }not test_frame_setitem_dask_array_into_new_col"

# E       IndexError: index 0 is out of bounds for axis 0 with size 0
k="${k-}${k+ and }not (TestPivotTable and test_pivot_number_of_levels_larger_than_int32)"
k="${k-}${k+ and }not (TestStackUnstackMultiLevel and test_unstack_number_of_levels_larger_than_int32)"

# E       OverflowError: timestamp out of range for platform time_t
# These fail only for the [tzlocal()] case, but it’s not clear how to validly
# name those in a pytest keyword expression due to the parentheses in tzlocal()
k="${k-}${k+ and }not (TestTimestampProperties and test_is_leap_year)"
k="${k-}${k+ and }not (TestBusinessDay and test_apply_out_of_range)"
k="${k-}${k+ and }not (TestBusinessHour and test_apply_out_of_range)"
k="${k-}${k+ and }not (TestCustomBusinessDay and test_apply_out_of_range)"
k="${k-}${k+ and }not (TestCustomBusinessHour and test_apply_out_of_range)"
k="${k-}${k+ and }not (TestWeek and test_apply_out_of_range)"

# E       AssertionError: Index are different
# E
# E       Index length are different
k="${k-}${k+ and }not (TestDateRanges and test_date_range_int64_overflow_stride_endpoint_different_signs)"
%endif

%ifarch s390x
# Note that pandas does not test big-endian support but will happily accept
# patches to improve it:
# https://github.com/pandas-dev/pandas/issues/4737#issuecomment-1090931741

# TODO: Why does this fail?
#
# >                   os.fsync(self._handle.fileno())
# E                   OverflowError: Python int too large to convert to C int
k="${k-}${k+ and }not test_flush"

# These are a cluster of similar pyarrow/parquet tests with apparent endianness
# issues. It is not immediately obvious where the bug is—in the library or in
# the tests?
k="${k-}${k+ and }not (TestBasic and test_write_index[pyarrow])"
k="${k-}${k+ and }not (TestBasic and test_multiindex_with_columns)"
k="${k-}${k+ and }not (TestBasic and test_write_column_multiindex_string)"
k="${k-}${k+ and }not (TestBasic and test_write_column_index_string)"
k="${k-}${k+ and }not (TestBasic and test_use_nullable_dtypes[pyarrow])"
k="${k-}${k+ and }not (TestParquetPyArrow and test_basic)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_to_bytes_without_path_or_buf_provided)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_categorical)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_additional_extension_arrays)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_pyarrow_backed_string_array[python])"
k="${k-}${k+ and }not (TestParquetPyArrow and test_pyarrow_backed_string_array[pyarrow])"
k="${k-}${k+ and }not (TestParquetPyArrow and test_additional_extension_types)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_timezone_aware_index[timezone_aware_date_list0])"
k="${k-}${k+ and }not test_to_read_gcs[parquet]"

# Similarly, there are a cluster of similar stata test failures for which the
# root cause is not immediately obvious.
k="${k-}${k+ and }not (TestStata and test_writer_117)"
k="${k-}${k+ and }not (TestStata and test_convert_strl_name_swap)"
k="${k-}${k+ and }not (TestStata and test_strl_latin1)"
# Fails for [118], [119], and [None]
k="${k-}${k+ and }not (TestStata and test_utf8_writer)"
%endif

%if 0%{?fedora} > 37
# The text of an error message has changed in libarrow/pyarrow 10, which is
# harmless but breaks one test. Disable it until a patch is available upstream.
#   CI: pyarrow 10 broke our ci
#   https://github.com/pandas-dev/pandas/issues/50058
k="${k-}${k+ and }not test_arrow_array"
%endif

%if 0%{?fc37}
# TODO: Why do these fail on F37 but not on F38?

# E       AssertionError: Did not use numexpr as expected.
# E       assert []
k="${k-}${k+ and }not (TestExpressions and test_run_binary)"
%endif

# Ensure pytest doesn’t find the “un-built” library. We can get away with this
# approach because the tests are also in the installed library. We can’t simply
# “cd” to the buildroot’s python3_sitearch because testing leaves files in the
# current working directory.
mkdir -p _empty
cd _empty

# See: test_fast.sh
# Workaround for pytest-xdist flaky collection order
# https://github.com/pytest-dev/pytest/issues/920
# https://github.com/pytest-dev/pytest/issues/1075
export PYTHONHASHSEED="$(
  %{python3} -c 'import random; print(random.randint(1, 4294967295))'
)"

# Previously, we ran tests in parallel. Upstream seems to support this;
# however, in practice, there were still some flaky test failures that seem to
# be fixed by eschewing parallelism.
#
# If we start running tests in parallel again in the future, note that on
# 32-bit platforms (%%if 0%%{?__isa_bits} == 32) it may be necessary to limit
# the number of concurrent tests to e.g. 8 in order to prevent memory
# exhaustion.
%constrain_build -c 1

%pytest -v '%{buildroot}%{python3_sitearch}/pandas' \
    %{?!with_slow_tests:--skip-slow} \
    --skip-network \
    --skip-db \
    -m "${m-}" \
    -k "${k-}" \
    -n %{_smp_build_ncpus} \
    -r sxX

%else
# Some imports require optional dependencies, and must be excluded during
# bootstrapping.
%{pyproject_check_import \
  %{?with_bootstrap:-e 'pandas.io.formats.style'} \
  %{?with_bootstrap:-e 'pandas.io.formats.style_render'} \
  -e 'pandas.conftest' \
  -e 'pandas.tests.*'}
%endif


%files -n python3-pandas -f %{pyproject_files}
# While pyproject_files automatically handles the LICENSE file in the Python
# package’s dist-info directory, we also want to package the entire LICENSES/
# directory to include third-party license text.  We include a second copy of
# the LICENSE file since it would be surprising to see a license directory for
# the package without the overall license file in it.
%license LICENSE LICENSES/
%doc README.md
%doc RELEASE.md
%exclude %{python3_sitearch}/pandas/tests


%files -n python3-pandas+test
%{python3_sitearch}/pandas/tests
%ghost %{python3_sitearch}/*.dist-info


%changelog
* Sun Dec 04 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.5.2-1
- Update to 1.5.2
- Re-enable python-gcsfs BR/weak-dep. on F38 and later
- Work around a harmless test failure with libarrow/pyarrow 10
- Allow a slightly older numpy version for F37
- Skip a test that sometimes hangs on aarch64 and ppc64le
- Additional test skips for F37
- Drop some test skips that are no longer needed
- Fix several flaky test failures by no longer running tests in parallel

* Wed Nov 23 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.5.1-2
- Update license breakdown and convert to SPDX
- Fully update optional dependencies and their versions
- Do not BR/Recommend pyarrow on 32-bit arches, where it is unavailable
- Drop accommodations for 32-bit ARM and Fedoras older than 36
- Update test skips for i686

* Mon Nov 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.5.1-1
- Update to 1.5.1 rhbz#2014890

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Python Maint <python-maint@redhat.com> - 1.3.5-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.5-2
- Bootstrap for Python 3.11

* Sat Apr 02 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.5-1
- Update to 1.3.5
- Drop compatibility with old RHEL releases that will not get this version anyway
- Update weak dependencies from documentation
- Also package README.md
- Do not install C sources
- Carefully handle virtual Provides and licenses for bundled/copied code
- Use pyproject-rpm-macros
- Run the tests (requires switching to GitHub source)
- Minimize optional dependencies when bootstrapping

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.3.3-2
- New release of pandas 1.3.3
- Add missing sources

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.3.0-1
- New release of pandas 1.3.0

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 1.2.4-2
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.4-1
- New release of pandas 1.2.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Orion Poplawski <orion@nwra.com> - 1.2.1-1
- Update to 1.2.1

* Wed Jan 13 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.0-1
- New release of pandas 1.2.0

* Fri Nov 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.4-1
- New release of pandas 1.1.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.5-1
- Update to latest version

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Orion Poplawski <orion@nwra.com> - 1.0.1-1
- Update to 1.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.25.3-1
- New release of pandas 0.25.3 (python 3.8 support included)

* Fri Sep 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.1-2
- Backport patch for Python 3.8 compatibility

* Sat Aug 24 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.25.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.1-3
- Fix doc build with numpydoc 0.9

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.1-2
- Subpackage python2-pandas has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Mar 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.1-1
- Update to 0.24.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.4-1
- New release of pandas 0.23.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.0-1
- New release of pandas 0.23.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.22.0-1
- New release of pandas 0.22.0

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 0.20.3-2
- Update conditionals

* Sun Sep 10 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.20.3-1
- New upstream version (0.20.3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.20.1-1
- New upstream version (0.20.1)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.2-1
- New upstream version (0.19.2)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.1-1
- New upstream version (0.19.1)

* Wed Oct 19 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.0-1
- New upstream version (0.19.0)
- Brings pandas-datareader using recommends

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18.1-3
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.1-1
- New upstream version (0.18.1)
- Update pypi url

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18.0-3
- Fix broken deps

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18.0-2
- Fix python_provide macros usage (FTBFS for some packages)

* Wed Mar 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.0-1
- New upstream version (0.18.0)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.1-1
- New upstream version (0.17.1)
- Add new dependecy as weak dep (fixes bz #1288919)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Orion Poplawski <orion@cora.nwra.com> - 0.17.0-2
- Use common build directory, new python macros
- Filter provides
- Fix provides

* Mon Oct 12 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.0-1
- New release of pandas 0.17.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.2-1
- New release of pandas 0.16.2

* Mon May 18 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.1-1
- New release of pandas 0.16.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 24 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.0-1
- New release of pandas 0.16.0
- Use license macro
- Don't use py3dir (new python guidelines)

* Tue Jan 20 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-3
- Pandas actually supports dateutil 2

* Mon Jan 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-2
- Update dependency on dateutil to dateutil15 (bz #1183368)

* Wed Dec 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-1
- New release of pandas 0.15.2

* Thu Nov 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.1-1
- New release of pandas 0.15.1

* Mon Oct 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-1
- New release of pandas 0.15.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-1
- New release of pandas 0.14.1

* Mon Jun 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.0-1
- New release of pandas 0.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.12.0-4
- Enable python3 build
- Set CFLAGS before build

* Fri Dec 13 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-3
- Fixed dependency name

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 0.12.0-2
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Fri Sep 20 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-1
- New release of pandas 0.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.9-1
- New release of pandas

* Fri Aug 03 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-2
- Fixes from review request

* Tue Jul 10 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-1
- Initial release in Fedora

