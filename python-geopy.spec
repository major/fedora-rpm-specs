Name:           python-geopy
Version:        2.4.1
Release:        %autorelease
Summary:        Geocoding library for Python

# SPDX
License:        MIT
URL:            https://geopy.readthedocs.io
%global forgeurl https://github.com/geopy/geopy
Source:         %{forgeurl}/archive/%{version}/geopy-%{version}.tar.gz

# Downstream-only: drop coverage from test extra
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-drop-coverage-from-test-extra.patch

# Downstream-only: allow newer Sphinx for testing
# (We have no choice; we must use what we have!)
#
# Applies on top of the coverage patch.
Patch:          0002-Downstream-only-allow-newer-Sphinx-for-testing.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
geopy is a Python client for several popular geocoding web services.

geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using third-party
geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google
Geocoding API (V3), and many other geocoding services.}

%description %{common_description}

%package -n python3-geopy
Summary:        %{summary}

%description -n python3-geopy %{common_description}

%pyproject_extras_subpkg -n python3-geopy aiohttp,requests,timezone

%prep
%autosetup -n geopy-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x dev-test,aiohttp,requests,timezone

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l geopy

%check
# Exclude tests which make API calls (require network access)
k="${k-}${k+ and }not test_geocoder_constructor_uses_https_proxy"
k="${k-}${k+ and }not test_geocoder_https_proxy_auth_is_respected"
k="${k-}${k+ and }not test_ssl_context_with_proxy_is_respected"
k="${k-}${k+ and }not test_ssl_context_without_proxy_is_respected"
%pytest -v test --ignore test/geocoders/ -k "${k-}"

%files -n python3-geopy -f %{pyproject_files}
%doc CONTRIBUTING.md README.rst

%changelog
%autochangelog
