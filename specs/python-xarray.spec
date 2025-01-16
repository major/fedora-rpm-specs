%global srcname xarray

Name:           python-%{srcname}
Version:        2025.1.1
Release:        %autorelease
Summary:        N-D labeled arrays and datasets in Python

License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source:         %pypi_source %{srcname}

# Fix test_dask_da_groupby_quantile.
Patch:          https://github.com/pydata/xarray/pull/9945.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bottleneck)
BuildRequires:  python3dist(dask[array]) >= 2023.9
BuildRequires:  python3dist(dask[dataframe]) >= 2023.9
BuildRequires:  python3dist(pint) >= 0.16
BuildRequires:  python3dist(pytest) >= 2.7.1
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(rasterio) >= 1.1
BuildRequires:  python3dist(seaborn) >= 0.11

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

pytest_args=(
  -n auto
  -m "not network"
  # this test somehow crashes python interpreter entirely, was xfail upstream till recently
  -k 'not test_save_mfdataset_compute_false_roundtrip'
)

%{pytest} -ra "${pytest_args[@]}" --pyargs xarray

%files -n python3-%{srcname} -f %{pyproject_files}
%license licenses/*
%doc README.md

%changelog
%autochangelog
