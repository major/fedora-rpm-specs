%global srcname cartopy
%global Srcname Cartopy

# Some tests use the network.
%bcond_with network

Name:           python-%{srcname}
Version:        0.21.0
Release:        %autorelease
Summary:        Cartographic Python library with Matplotlib visualisations

License:        LGPLv3
URL:            http://scitools.org.uk/cartopy/docs/latest/
Source0:        %pypi_source %{Srcname}
# Set location of Fedora-provided pre-existing data.
Source1:        siteconfig.py

# Might not go upstream in current form.
Patch0001:      0001-Increase-tolerance-for-new-FreeType.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2088864
Patch0002:      0002-Use-pkg-config-to-find-GEOS-instead-of-geos-config.patch
Patch0003:      0003-Remove-extraneous-insertion-of-default-compiler-path.patch
# We don't need to worry about the bugs with setuptools-scm < 7.
Patch0004:      0004-Allow-older-setuptools-scm.patch

BuildRequires:  gcc-c++
BuildRequires:  geos-devel >= 3.7.2
BuildRequires:  proj-data-uk
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest-xdist)

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
Recommends:     python3dist(pykdtree) >= 1.2.2

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


%pyproject_extras_subpkg -n python3-cartopy ows plotting


%prep
%autosetup -n %{Srcname}-%{version} -p1
cp -a %SOURCE1 lib/cartopy/

sed -i -e 's/oldest-supported-numpy/numpy/g' pyproject.toml

# Remove generated Cython sources
rm lib/cartopy/trace.cpp


%generate_buildrequires
%pyproject_buildrequires -r -x ows,plotting,tests


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


%check
MPLBACKEND=Agg \
    %{pytest} -n auto --doctest-modules --mpl --pyargs cartopy \
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
%{_bindir}/cartopy_feature_download.py


%changelog
%autochangelog
