%global srcname geopandas

# There is a build dependency loop when built with tests.
# It involves libpysal, mapclassify, networkx.
# This bcond allows to bootstrap it.
%bcond bootstrap 0

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Geographic Pandas extensions

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
# PyPI source does not have test data.
Source:         https://github.com/%{srcname}/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
GeoPandas is a project to add support for geographic data to Pandas objects. \
\
The goal of GeoPandas is to make working with geospatial data in Python easier. \
It combines the capabilities of Pandas and Shapely, providing geospatial \
operations in Pandas and a high-level interface to multiple geometries to \
Shapely. GeoPandas enables you to easily do operations in Python that would \
otherwise require a spatial database such as PostGIS.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{without bootstrap}
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(fiona) >= 1.8.21
BuildRequires:  python3dist(geopy)
BuildRequires:  python3dist(mapclassify) >= 2.5
BuildRequires:  python3dist(matplotlib) >= 3.7
BuildRequires:  python3dist(psycopg) >= 3.1
BuildRequires:  python3dist(pyarrow) >= 8
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sqlalchemy) >= 2
BuildRequires:  python3dist(xyzservices)
# See:
# Depend on pandas[test] for testing
# https://github.com/geopandas/geopandas/pull/2438
BuildRequires:  python3dist(pandas[test])
%endif

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{without bootstrap}
%{pytest} -ra geopandas -m 'not web'
%else
%pyproject_check_import -e 'geopandas.*test*'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CHANGELOG.md

%changelog
%autochangelog
