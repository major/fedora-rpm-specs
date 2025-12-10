Name:           pyshp
Version:        3.0.3
Release:        %autorelease
Summary:        Pure Python read/write support for ESRI Shapefile format

# SPDX
License:        MIT
# See Source10-Source25.
SourceLicense:  %{license} AND LicenseRef-Fedora-Public-Domain AND ODbl-1.0
URL:            https://github.com/GeospatialPython/pyshp
Source0:        %{url}/archive/%{version}/pyshp-%{version}.tar.gz

# Shapefiles for doctests. These are not packaged in the binary RPMs, so do not
# contribute to the License. They are LicenseRef-Fedora-Public-Domain
# (https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md; see
# also http://www.naturalearthdata.com/about/terms-of-use/). Upstream tests
# fetch these from the network.
%global ne_url https://github.com/nvkelso/natural-earth-vector
# Upstream uses “master”
%global ne_commit ca96624a56bd078437bca8184e78163e5039ad19
Source10:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.cpg
Source11:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.dbf
Source12:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.prj
Source13:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.shp
Source14:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.shx
Source20:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.cpg
Source21:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.dbf
Source22:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.prj
Source23:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.shp
Source24:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.shx
# This is an OpenStreetMap extract originally obtained from
# https://download.geofabrik.de/, so it is ODbl-1.0; see
# https://www.openstreetmap.org/copyright/.
%global data_url https://github.com/JamesParrott/PyShp_test_shapefile
# Upstream uses “main”
%global data_commit 2583dba70d0892fc787e1a837df07c3ea8e69950
Source25:       %{data_url}/raw/%{data_commit}/gis_osm_natural_a_free_1.zip

BuildSystem:            pyproject
BuildOption(install):   -l shapefile
# We do not package the “stubs” extra because we do not need or wish to package
# python-pyshp-stubs.
BuildOption(generate_buildrequires): -x test

BuildArch:      noarch

%global common_description %{expand:
The Python Shapefile Library (PyShp) provides read and write support for the
Esri Shapefile format. The Shapefile format is a popular Geographic Information
System vector data format created by Esri. For more information about this
format please read the well-written “ESRI Shapefile Technical Description –
July 1998” located at
http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf. The Esri document
describes the shp and shx file formats.  However a third file format called dbf
is also required. This format is documented on the web as the “XBase File
Format Description” and is a simple file-based database format created in the
1960’s. For more on this specification see:
http://www.clicketyclick.dk/databases/xbase/format/index.html

Both the Esri and XBase file-formats are very simple in design and memory
efficient which is part of the reason the shapefile format remains popular
despite the numerous ways to store and exchange GIS data available today.}

%description %{common_description}


%package -n python3-pyshp
Summary:        %{summary}

%py_provides python3-shapefile

%description -n python3-pyshp %{common_description}


%prep -a
mkdir -p _testdata
ln '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE20}' '%{SOURCE21}' '%{SOURCE22}' '%{SOURCE23}' '%{SOURCE24}' \
    '%{SOURCE25}' _testdata/


%check -a
# Serve the test data locally; see the “Network tests” section in README.md
pushd _testdata
%{python3} -m http.server 8000 &
SERVER_PID="$!"
trap "kill '${SERVER_PID}'" INT TERM EXIT
popd
export REPLACE_REMOTE_URLS_WITH_LOCALHOST='yes'

%pytest -v
# Doctests
%{py3_test_envvars} %{python3} test_shapefile.py


%files -n python3-pyshp -f %{pyproject_files}
%doc changelog.txt
%doc README.md


%changelog
%autochangelog
