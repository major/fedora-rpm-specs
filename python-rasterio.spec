%global srcname rasterio

Name:           python-%{srcname}
Version:        1.3.6
Release:        %autorelease
Summary:        Fast and direct raster I/O for use with Numpy and SciPy

License:        BSD-3-Clause
URL:            https://github.com/rasterio/rasterio
# PyPI tarball doesn't include test data.
Source0:        https://github.com/rasterio/rasterio/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:          0001-Loosen-up-build-requirements.patch
# Backport test fix for GDAL 3.6.1
Patch:          https://github.com/rasterio/rasterio/pull/2680.patch
# Backport test fixes for GDL 3.7.0
Patch:          https://github.com/rasterio/rasterio/commit/9059c3ac005afadb3a08e744096a4bb3fcc87cba.patch
Patch:          https://github.com/rasterio/rasterio/commit/74c4a7c93ab3298a79b4d9aced8e6acab4507be5.patch
Patch:          https://github.com/rasterio/rasterio/commit/acef4a8f550ad5b3fca045734e0aa4307074d2d8.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 1.11
BuildRequires:  gdal-devel >= 1.11

%global _description \
Rasterio reads and writes geospatial raster data. Geographic information \
systems use GeoTIFF and other formats to organize and store gridded, or raster, \
datasets. Rasterio reads and writes these formats and provides a Python API \
based on ND arrays.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} ipython plot s3


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r -x ipython,plot,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
rm -r %{srcname}  # Don't try unbuilt copy.

# test_outer_boundless_pixel_fidelity is very flaky, so skip it.
# Skip debian tests since we are not on debian
%{pytest} -ra -m 'not network and not wheel' \
    -k 'not test_outer_boundless_pixel_fidelity and not debian'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt CHANGES.txt CITATION.txt
%license LICENSE.txt
%{_bindir}/rio

%changelog
%autochangelog
