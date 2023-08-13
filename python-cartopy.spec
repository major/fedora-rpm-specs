%global srcname cartopy
%global Srcname Cartopy

# Some tests use the network.
%bcond_with network

Name:           python-%{srcname}
Version:        0.22.0
Release:        %autorelease
Summary:        Cartographic Python library with Matplotlib visualisations

License:        LGPL-3.0-only
URL:            https://scitools.org.uk/cartopy/docs/latest/
Source0:        %pypi_source %{Srcname}
# Set location of Fedora-provided pre-existing data.
Source1:        siteconfig.py

# Might not go upstream in current form.
Patch:          0001-Increase-tolerance-for-new-FreeType.patch

BuildRequires:  gcc-c++
BuildRequires:  proj-data-uk
BuildRequires:  python3-devel

%global _description %{expand:
Cartopy is a Python package designed to make drawing maps for data analysis
and visualisation easy. It features:
* object oriented projection definitions
* point, line, polygon and image transformations between projections
* integration to expose advanced mapping in Matplotlib with a simple and
  intuitive interface
* powerful vector data handling by integrating shapefile reading with Shapely
  capabilities
}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       python-%{srcname}-common = %{version}-%{release}
Recommends:     python3dist(cartopy[ows]) = %{version}-%{release}
Recommends:     python3dist(cartopy[plotting]) = %{version}-%{release}
%ifnarch %{ix86}
Recommends:     python3dist(cartopy[speedups]) = %{version}-%{release}
%endif

%description -n python3-%{srcname} %{_description}


%package -n     python-%{srcname}-common
Summary:        Data files for %{srcname}
BuildArch:      noarch

BuildRequires:  natural-earth-map-data-110m
BuildRequires:  natural-earth-map-data-50m

Recommends:     natural-earth-map-data-110m
Suggests:       natural-earth-map-data-50m
Suggests:       natural-earth-map-data-10m

%description -n python-%{srcname}-common
Data files for %{srcname}.


%ifnarch %{ix86}
%pyproject_extras_subpkg -n python3-cartopy ows plotting speedups
%else
%pyproject_extras_subpkg -n python3-cartopy ows plotting
%endif


%prep
%autosetup -n %{Srcname}-%{version} -p1
cp -a %SOURCE1 lib/cartopy/

sed -i -e 's/oldest-supported-numpy/numpy/g' pyproject.toml
sed -i -e 's/, "pytest-cov", "coveralls"//g' pyproject.toml

# Remove generated Cython sources
rm lib/cartopy/trace.cpp


%generate_buildrequires
%ifnarch %{ix86}
%pyproject_buildrequires -r -x ows,plotting,speedups,test
%else
%pyproject_buildrequires -r -x ows,plotting,test
%endif


%build
export FORCE_CYTHON=1 SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

mkdir -p %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/
for theme in physical cultural; do
    ln -s %{_datadir}/natural-earth-map-data/${theme} \
        %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/${theme}
done

mv %{buildroot}%{_bindir}/feature_download %{buildroot}%{_bindir}/cartopy_feature_download


%check
MPLBACKEND=Agg \
    %{pytest} -n auto --doctest-modules --mpl --mpl-generate-summary=html --pyargs cartopy \
%if %{with network}
    %{nil}
%else
    -m "not network"
%endif


%files -n python-%{srcname}-common
%doc README.md
%license COPYING COPYING.LESSER lib/cartopy/data/LICENSE
%{_datadir}/cartopy/

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/cartopy_feature_download


%changelog
%autochangelog
