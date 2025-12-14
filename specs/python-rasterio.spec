%global srcname rasterio

Name:           python-%{srcname}
Version:        1.4.4
Release:        %autorelease
Summary:        Fast and direct raster I/O for use with Numpy and SciPy

License:        BSD-3-Clause
URL:            https://github.com/rasterio/rasterio
# PyPI tarball doesn't include test data.
Source0:        https://github.com/rasterio/rasterio/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fedora-specific.
Patch:          0001-Loosen-up-build-requirements.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 3.5
BuildRequires:  gdal-devel >= 3.5

# This is licensed as BSD-3-Clause, same as rasterio
Provides: bundled(python3dist(click-plugins)) = 2

%global _description %{expand:
Rasterio reads and writes geospatial raster data. Geographic information
systems use GeoTIFF and other formats to organize and store gridded, or raster,
datasets. Rasterio reads and writes these formats and provides a Python API
based on ND arrays.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} ipython plot s3


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x ipython,plot,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
rm -r %{srcname}  # Don't try unbuilt copy.

# test_outer_boundless_pixel_fidelity is very flaky, so skip it.
# Skip debian tests since we are not on debian
%{pytest} -ra -m 'not network and not wheel' \
    -k 'not test_outer_boundless_pixel_fidelity and not debian'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt CHANGES.txt CITATION.txt
%{_bindir}/rio

%changelog
%autochangelog
