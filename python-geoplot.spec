%global srcname geoplot

%bcond_with network

Name:           python-%{srcname}
Version:        0.5.1
Release:        %autorelease
Summary:        High-level geospatial plotting for Python

License:        MIT
URL:            https://github.com/ResidentMario/geoplot
# PyPI tarball does not include tests.
Source0:        https://github.com/ResidentMario/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fedora specific
Patch:          0001-Remove-some-unavailable-test-dependencies.patch
# https://github.com/ResidentMario/geoplot/pull/286
Patch:          0002-Fix-tests-with-Matplotlib-3.7.patch
# Accommodate UserWarning not in geopandas 0.11
# https://github.com/ResidentMario/geoplot/pull/285
#   Fixes:
# Tests fail with geopandas 0.11
# https://github.com/ResidentMario/geoplot/issues/283
# https://bugzilla.redhat.com/show_bug.cgi?id=2148633
Patch:          https://github.com/ResidentMario/%{srcname}/pull/285.patch
# Fix issue with Pandas 2.
Patch:          https://github.com/ResidentMario/%{srcname}/pull/293.patch

BuildArch:      noarch
 
%global _description \
geoplot is a high-level Python geospatial plotting library. It's an extension \
to cartopy and matplotlib which makes mapping easy: like seaborn for \
geospatial.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
 
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -rx develop

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Skip tests that use the network.
MPLBACKEND=Agg \
%if %{with network}
    %{pytest} tests/*tests.py
%else
    %{pytest} tests/*tests.py -k 'not webmap'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
