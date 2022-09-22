%global srcname geopandas

# There is a build dependency loop when built with tests.
# It involves libpysal, mapclassify, networkx.
# This bcons allows to bootstrap it.
%bcond_without tests

Name:           python-%{srcname}
Version:        0.11.1
Release:        %autorelease
Summary:        Geographic Pandas extensions

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/%{srcname}/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

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

%if %{with tests}
BuildRequires:  python3dist(numpy) >= 1.15
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(psycopg2)
BuildRequires:  python3dist(rtree) >= 0.8
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(matplotlib) >= 2.0.1
BuildRequires:  python3dist(mapclassify)
# See:
# Depend on pandas[test] for testing
# https://github.com/geopandas/geopandas/pull/2438
BuildRequires:  python3dist(pandas[test])
%endif

%description -n python3-%{srcname} %{_description}

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
%if %{with tests}
%{pytest} -ra geopandas -m 'not web'
%else
# naturalearth_creation assumes zipfile from naturalearthdata was downloaded to current directory
%pyproject_check_import -e 'geopandas.*test*' -e geopandas.datasets.naturalearth_creation
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CHANGELOG.md

%changelog
%autochangelog
