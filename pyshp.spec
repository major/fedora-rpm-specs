Name:           pyshp
Version:        2.3.1
Release:        %autorelease
Summary:        Pure Python read/write support for ESRI Shapefile format

# SPDX
License:        MIT
URL:            https://github.com/GeospatialPython/pyshp
Source0:        %{url}/archive/%{version}/pyshp-%{version}.tar.gz

# Shapefiles for doctests. These are not packaged in the binary RPMs, so do not
# contribute to the License. They are LicenseRef-Fedora-Public-Domain
# (https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md; see
# also http://www.naturalearthdata.com/about/terms-of-use/). Upstream tests
# fetch these from the network.
%global ne_url https://github.com/nvkelso/natural-earth-vector
# Upstream uses “master”
%global ne_commit e6fd44e64780e9724e2c663594dafcc4da5b1cc1
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
# Upstream also uses https://biogeo.ucdavis.edu/data/diva/rrd/NIC_rrd.zip, but
# the license is unclear, so we skip this one.

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix

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


%prep
%autosetup -p1

# Fix non-UTF-8 license file
iconv --from-code=Windows-1252 --to-code=UTF-8 --output=LICENSE.TXT.conv \
    LICENSE.TXT
touch -r LICENSE.TXT LICENSE.TXT.conv
mv LICENSE.TXT.conv LICENSE.TXT
# Fix line endings
dos2unix --keepdate LICENSE.TXT changelog.txt shapefile.py

# Allow newer versions of test dependencies
sed -r -i 's/==/>=/' requirements.test.txt

# Make a copy of README.md for which we do not need network access—either by
# using local copies of the resources that would be fetched, or by skipping
# tests where the resources are not appropriate for the source RPM (unclear
# licensing).
sed -r \
  -e 's@(Reader\("https?://biogeo.*)@\1  # doctest: +SKIP@' \
  -e 's@(Reader\(")(https?://github\.com/nvkelso/natural-earth-vector/[^"]*)/([^/"?]+)(\?[^/"]*)?@\1\3@' \
  'README.md' > 'README-no-network.md'
cp -p '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE20}' '%{SOURCE21}' '%{SOURCE22}' '%{SOURCE23}' '%{SOURCE24}' .


%generate_buildrequires
%pyproject_buildrequires requirements.test.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files shapefile


%check
# Although shapefile.py has an integrated runner for the doctests, we run them
# with pytest because we need to skip those that require network access.
%pytest --doctest-glob='README-no-network.md' -m '(not network)'


%files -n python3-pyshp -f %{pyproject_files}
# pyproject_files handles LICENSE.TXT; verify with “rpm -qL -p …”
%doc changelog.txt
%doc README.md


%changelog
%autochangelog
