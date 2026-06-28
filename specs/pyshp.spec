Name:           pyshp
Version:        3.1.3
Release:        %autorelease
Summary:        Pure Python read/write support for ESRI Shapefile format

# The entire source is MIT, except that shapefiles/test/REL.zip is CC-BY-4.0;
# this does not affect the licenses of binary RPMs because this file is used
# only as test data.
License:        MIT
SourceLicense:  %{license} AND CC-BY-4.0
URL:            https://github.com/GeospatialPython/pyshp
Source:         %{url}/archive/%{version}/pyshp-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --assert-license shapefile
# We do not package the “stubs” extra because we do not need or wish to package
# python-pyshp-stubs.
BuildOption(generate_buildrequires): --dependency-groups test

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


%check -a
%pytest -m 'not network' --verbose
%{py3_test_envvars} %{python3} tests/run_doctests.py -m 'not network'


%files -n python3-pyshp -f %{pyproject_files}
%doc changelog.txt
%doc README.md


%changelog
%autochangelog
