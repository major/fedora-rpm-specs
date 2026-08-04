%global srcname cartopy

# Some tests use the network.
%bcond_with network

Name:           python-%{srcname}
Version:        0.25.0
Release:        %autorelease
Summary:        Cartographic Python library with Matplotlib visualisations

License:        BSD-3-Clause
URL:            https://scitools.org.uk/cartopy/docs/latest/
Source0:        %pypi_source %{srcname}
# Set location of Fedora-provided pre-existing data.
Source1:        siteconfig.py

# Fedora specific.
Patch:          0001-Reduce-numpy-build-dependency.patch
# Might not go upstream in current form.
Patch:          0002-Increase-tolerance-for-new-FreeType.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  natural-earth-map-data-110m
BuildRequires:  natural-earth-map-data-50m
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
Recommends:     python3dist(cartopy[speedups]) = %{version}-%{release}

%description -n python3-%{srcname} %{_description}


%package -n     python-%{srcname}-common
Summary:        Data files for %{srcname}
BuildArch:      noarch

Recommends:     natural-earth-map-data-110m
Suggests:       natural-earth-map-data-50m
Suggests:       natural-earth-map-data-10m

%description -n python-%{srcname}-common
Data files for %{srcname}.


%pyproject_extras_subpkg -n python3-cartopy ows plotting speedups


%prep
%autosetup -n %{srcname}-%{version} -p1
cp -a %{SOURCE1} lib/cartopy/

sed -i -e 's/, "pytest-cov", "coveralls"//g' pyproject.toml
# workaround for broken pytest-mpl
sed -i -e 's/, "pytest-mpl>=0.11"//g' pyproject.toml
sed -i -e '/addopts = "--mpl"/d' pyproject.toml

# Remove generated Cython sources
rm lib/cartopy/trace.cpp


%generate_buildrequires
%pyproject_buildrequires -r -x ows,plotting,speedups,test


%build
export FORCE_CYTHON=1 SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install

# Remove C++ and Cython source files installed into site-packages
find %{buildroot}%{python3_sitearch}/cartopy/ -name "*.cpp" -delete
find %{buildroot}%{python3_sitearch}/cartopy/ -name "*.pyx" -delete

# Fix shebang in non-executable script
sed -i -e '/^#!/d' %{buildroot}%{python3_sitearch}/cartopy/feature/download/__main__.py

%pyproject_save_files -l %{srcname}

# Remove deleted C++ and Cython source files from pyproject_files list
sed -i '/trace\.cpp/d' %{pyproject_files}
sed -i '/trace\.pyx/d' %{pyproject_files}

mkdir -p %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/
for theme in physical cultural; do
    ln -s %{_datadir}/natural-earth-map-data/${theme} \
        %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/${theme}
done


%check
MPLBACKEND=Agg \
    %{pytest} -n auto -p no:pytest_mpl --doctest-modules --pyargs cartopy \
    -k "not (test_robinson or test_oblique_mercator or test_geostationary or test_transverse_mercator or test_lambert_conformal or test_LatitudeFormatter_mercator or test_extents or test_get_extent or test_pcolormesh_datalim or test_invalid_xy_domain_corner or test_invalid_y_domain or test_plot_after_contour_doesnt_shrink or test_cursor_values or test_gridliner_labels_zoom or test_tiny_point_between_boundary_points or test_infinite_loop_bounds or test_with_transform)" \
%if %{with network}
    -m "not mpl_image_compare"
%else
    -m "not network and not mpl_image_compare"
%endif


%files -n python-%{srcname}-common
%doc README.md
%{_datadir}/cartopy/

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/cartopy_feature_download


%changelog
%autochangelog
