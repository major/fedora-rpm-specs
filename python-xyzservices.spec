%global srcname xyzservices

Name:           python-%{srcname}
Version:        2022.9.0
Release:        %autorelease
Summary:        Source of XYZ tiles providers

License:        BSD
URL:            https://github.com/geopandas/xyzservices
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
xyzservices is a lightweight library providing a repository of available XYZ
services offering raster basemap tiles. The repository is provided via Python
API and as a compressed JSON file. XYZ tiles can be used as background for your
maps to provide necessary spatial context.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3dist(mercantile)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)

%description -n python3-%{srcname}
xyzservices is a lightweight library providing a repository of available XYZ
services offering raster basemap tiles. The repository is provided via Python
API and as a compressed JSON file. XYZ tiles can be used as background for your
maps to provide necessary spatial context.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -o 'markers=request'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_datadir}/%{srcname}/

%changelog
%autochangelog
