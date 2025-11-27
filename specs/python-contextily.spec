%global srcname contextily

# Some tests require the network.
%bcond network 0

Name:           python-%{srcname}
Version:        1.7.0
Release:        %autorelease
Summary:        Context geo-tiles in Python

License:        BSD-3-Clause
URL:            https://github.com/geopandas/contextily
Source:         %pypi_source %{srcname}
# https://github.com/geopandas/contextily/pull/273
Patch:          0001-Mark-another-test-as-using-the-network.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
contextily is a small Python 3 package to retrieve and write to disk tile maps
from the internet into geospatial raster files. Bounding boxes can be passed in
both WGS84 (EPSG:4326) and Spheric Mercator (EPSG:3857).

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
contextily is a small Python 3 package to retrieve and write to disk tile maps
from the internet into geospatial raster files. Bounding boxes can be passed in
both WGS84 (EPSG:4326) and Spheric Mercator (EPSG:3857).

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{pytest} %{!?with_network:-m 'not network'}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
