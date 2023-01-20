%global srcname xarray
%global data_commit 86974d54ce83a130303fe8caa629e60deb3cb6e5

%bcond_with docs

Name:           python-%{srcname}
Version:        2023.1.0
Release:        %autorelease
Summary:        N-D labeled arrays and datasets in Python

License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source0:        %pypi_source %{srcname}
# Data for examples only.
Source1:        https://github.com/pydata/xarray-data/archive/%{data_commit}/xarray-data-%{data_commit}.tar.gz
Source2:        https://github.com/rasterio/rasterio/raw/1.2.10/tests/data/RGB.byte.tif
# All Fedora specific.
Patch0001:      0001-DOC-Don-t-download-RGB.byte.tif-during-build.patch
Patch0002:      0002-DOC-Skip-examples-using-unpackaged-dependencies.patch
Patch0003:      0003-DOC-Don-t-print-out-conda-pip-environment.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bottleneck)
BuildRequires:  python3dist(cftime) >= 1.2
BuildRequires:  python3dist(dask[array]) >= 2.30
BuildRequires:  python3dist(dask[dataframe]) >= 2.30
BuildRequires:  python3dist(netcdf4) >= 1.5
BuildRequires:  python3dist(pint) >= 0.16
BuildRequires:  python3dist(pytest) >= 2.7.1
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(rasterio) >= 1.1
BuildRequires:  python3dist(seaborn) >= 0.11
BuildRequires:  python3dist(zarr) >= 2.5

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


%if %{with docs}
%package -n python-%{srcname}-doc
Summary:        xarray documentation

BuildRequires:  python3dist(cartopy)
BuildRequires:  natural-earth-map-data-110m
BuildRequires:  natural-earth-map-data-10m
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(matplotlib) >= 3.3
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python-%{srcname}-doc
Documentation for xarray
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1

%if %{with docs}
# Provide example datasets for building docs.
tar xf %SOURCE1 --transform='s~^\(%{srcname}-data-%{data_commit}/\)~\1.xarray_tutorial_data/~'
cp -p %SOURCE2 ./doc/gallery/
%endif


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%if %{with docs}
# generate html docs
pushd doc
PYTHONPATH=${PWD}/.. HOME=${PWD}/../%{srcname}-data-%{data_commit} make html
# remove the sphinx-build leftovers
rm -rf _build/html/.{doctrees,buildinfo}
popd
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
rm -rf xarray

pytest_args=(
  -n auto
  -m "not network"
  # https://bugzilla.redhat.com/show_bug.cgi?id=2113663
  -k 'not test_open_nczarr'
)

%{pytest} -ra "${pytest_args[@]}" --pyargs xarray


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE licenses/DASK_LICENSE licenses/NUMPY_LICENSE licenses/PANDAS_LICENSE licenses/PYTHON_LICENSE licenses/SEABORN_LICENSE
%doc README.md

%if %{with docs}
%files -n python-%{srcname}-doc
%doc doc/_build/html
%license LICENSE licenses/DASK_LICENSE licenses/NUMPY_LICENSE licenses/PANDAS_LICENSE licenses/PYTHON_LICENSE licenses/SEABORN_LICENSE
%endif


%changelog
%autochangelog
