%global _with_bootstrap 1
# Loop between geopandas and pyogrio.
%bcond bootstrap 0

%global srcname pyogrio

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        Vectorized spatial vector file format I/O using GDAL/OGR

# Main license: MIT
# arrow_bridge.h: Apache-2.0
# For test data, see `pyogrio/tests/fixtures/README.md`: Public Domain and ODbl-1.0
# Note, public domain comes from a subset of `natural-earth-map-data`, so inherits its exception.
License:        MIT AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND ODbl-1.0
URL:            https://github.com/geopandas/pyogrio
Source:         %pypi_source %{srcname}
# Some Fedora-specific things
Patch:          0001-Drop-extra-dependencies.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  gdal-devel >= 2.4.0
# For testing only.
BuildRequires:  python3dist(pyarrow)

%global _description %{expand:
Pyogrio provides a GeoPandas-oriented API to OGR vector data sources, such as
ESRI Shapefile, GeoPackage, and GeoJSON. Vector data sources have geometries,
such as points, lines, or polygons, and associated records with potentially
many columns worth of data.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x dev,test%{!?with_bootstrap:,geopandas}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
mkdir empty
cd empty
%pytest --pyargs %{srcname} -m "not network" -ra

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
