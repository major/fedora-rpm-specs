%global srcname rasterio

Name:           python-%{srcname}
Version:        1.3.2
Release:        %autorelease
Summary:        Fast and direct raster I/O for use with Numpy and SciPy

License:        BSD
URL:            https://github.com/mapbox/rasterio
# PyPI tarball doesn't include test data.
Source0:        https://github.com/mapbox/rasterio/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0001:      0001-Loosen-up-build-requirements.patch

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

# Skip tests on s390x, GEOS is broken on that arch and results in test failures
%ifnarch s390x
# test_outer_boundless_pixel_fidelity is very flaky, so skip it.
# Skip debian tests since we are not on debian
%{pytest} -ra -m 'not network and not wheel' \
    -k 'not test_outer_boundless_pixel_fidelity and not debian'
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt CHANGES.txt CITATION.txt
%license LICENSE.txt
%{_bindir}/rio


%changelog
%autochangelog
