%global srcname xarray

# A bootstrap build disables tests needing dask,
# allowing to break a dependency loop between xarray and dask.
# Note that dask has a similar approach, thus we have 2 ways of breaking the loop,
# so we can attempt both, whichever is more convenient.
%bcond bootstrap 0
%bcond dask %{without bootstrap}

Name:           python-%{srcname}
Version:        2026.2.0
Release:        %autorelease
Summary:        N-D labeled arrays and datasets in Python

License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source:         %pypi_source %{srcname}
# Fedora specific.
Patch:          0001-Drop-pydap-from-dependencies.patch
# Fix failures with latest dependencies.
Patch:          https://github.com/pydata/xarray/pull/11204.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bottleneck)
BuildRequires:  python3dist(pint) >= 0.22
BuildRequires:  python3dist(pytest) >= 2.7.1
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(rasterio) >= 1.3
BuildRequires:  python3dist(seaborn) >= 0.13
%if %{with dask}
BuildRequires:  python3dist(dask[array]) >= 2023.11
BuildRequires:  python3dist(dask[dataframe]) >= 2023.11
%endif

%global _description %{expand: \
Xarray (formerly xray) is an open source project and Python package that
makes working with labelled multi-dimensional arrays simple, efficient,
and fun!

Xarray introduces labels in the form of dimensions, coordinates and
attributes on top of raw NumPy-like arrays, which allows for a more
intuitive, more concise, and less error-prone developer experience. The
package includes a large and growing library of domain-agnostic functions
for advanced analytics and visualization with these data structures.

Xarray was inspired by and borrows heavily from pandas, the popular data
analysis package focused on labelled tabular data. It is particularly
tailored to working with netCDF files, which were the source of xarray’s
data model, and integrates tightly with dask for parallel computing.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} io

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x io

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
rm -rf xarray

echo >> pytest.ini  # Ignore any command-line arguments from upstream.

# this test somehow crashes python interpreter entirely, was xfail upstream till recently
k="${k-}${k+ and }not test_save_mfdataset_compute_false_roundtrip"

%if %{without dask}
k="${k-}${k+ and }not test_source_encoding_always_present_with_fsspec"
k="${k-}${k+ and }not test_h5netcdf_storage_options"
# The following test does not need dask, but fails without it,
# see https://github.com/pydata/xarray/pull/11384
k="${k-}${k+ and }not (TestDataset and test_repr)"
%endif

%{pytest} -ra -n auto -m "not network" ${k:+-k "${k}"} --pyargs xarray --timeout 300 --full-trace

%files -n python3-%{srcname} -f %{pyproject_files}
%license licenses/*
%doc README.md

%changelog
%autochangelog
