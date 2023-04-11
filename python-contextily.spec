%global srcname contextily

# Some tests require the network.
%bcond_with network

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Context geo-tiles in Python

License:        BSD-3-Clause
URL:            https://github.com/geopandas/contextily
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

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
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with network}
%{pytest}
%else
%{pytest} -m 'not network'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
