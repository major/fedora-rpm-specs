%global srcname mapclassify

Name:           python-%{srcname}
Version:        2.4.3
Release:        %autorelease
Summary:        Classification Schemes for Choropleth Maps

License:        BSD
URL:            https://github.com/pysal/mapclassify
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy) >= 1.3
BuildRequires:  python3dist(pandas) >= 1
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy) >= 1
BuildRequires:  python3dist(setuptools)

# Tests
BuildRequires:  python3dist(geopandas)
BuildRequires:  python3dist(libpysal)
BuildRequires:  python3dist(rtree)
BuildRequires:  python3dist(pytest)

# Docs
#BuildRequires:  python3dist(numpydoc)
#BuildRequires:  python3dist(sphinx) >= 1.4.3
#BuildRequires:  python3dist(sphinx-bootstrap-theme)
#BuildRequires:  python3dist(sphinx-gallery)
#BuildRequires:  python3dist(sphinxcontrib-bibtex)

%description
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

%install
%py3_install

%check
# This test is flaky due to networkx:
# https://github.com/pysal/mapclassify/pull/77
%{pytest} -k 'not test_smallest_last'

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
