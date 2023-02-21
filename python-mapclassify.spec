%global srcname mapclassify

Name:           python-%{srcname}
Version:        2.5.0
Release:        %autorelease
Summary:        Classification Schemes for Choropleth Maps

License:        BSD-3-Clause
URL:            https://github.com/pysal/mapclassify
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel

# Tests
BuildRequires:  python3dist(rtree)

%description
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# This test is flaky due to networkx:
# https://github.com/pysal/mapclassify/pull/77
%{pytest} -k 'not test_smallest_last'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
