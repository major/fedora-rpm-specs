%global srcname rasterio

Name:           python-%{srcname}
Version:        1.4.3
Release:        %autorelease
Summary:        Fast and direct raster I/O for use with Numpy and SciPy

License:        BSD-3-Clause
URL:            https://github.com/rasterio/rasterio
# PyPI tarball doesn't include test data.
Source0:        https://github.com/rasterio/rasterio/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fedora-specific.
Patch:          0001-Loosen-up-build-requirements.patch
# https://github.com/rasterio/rasterio/pull/3360
Patch:          0002-TST-Fix-test-fixture-for-test_reproject_error_propag.patch
# https://github.com/rasterio/rasterio/pull/3389
Patch:          0003-Set-INIT_DEST-to-0-instead-of-NO_DATA-if-it-s-unset.patch
# https://github.com/rasterio/rasterio/pull/3330
Patch:          0004-Change-nearest-neighbor-warp-expectations-at-GDAL-3..patch
# https://github.com/rasterio/rasterio/pull/3293
Patch:          0005-test_reproject_resampling-Add-another-value-for-mode.patch
# https://github.com/rasterio/rasterio/pull/3394
Patch:          0006-Update-warp-test-results-for-GDAL-3.11.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 3.5
BuildRequires:  gdal-devel >= 3.5

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

# Remove upper bound version restriction for Cython
sed -i -E 's/cython~=([0-9.]+)/cython>=\1/' pyproject.toml

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
