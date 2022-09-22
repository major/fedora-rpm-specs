%global pypi_name geopy

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        8%{?dist}
Summary:        Python client for several popular geocoding web services

License:        MIT
URL:            https://geopy.readthedocs.io
Source0:        https://github.com/geopy/geopy/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using third-
party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google
Geocoding API (V3), and many other geocoding services.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-GeographicLib
BuildRequires:  python3-pytz
BuildRequires:  python3-mock
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-async-generator
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using third-
party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google
Geocoding API (V3), and many other geocoding services.

%prep
%autosetup -n %{pypi_name}-%{version}

# Drop upper limit on geographiclib
# https://github.com/geopy/geopy/pull/520
sed -i 's/geographiclib<2,/geographiclib/' setup.py

%build
%py3_build

%install
%py3_install

%check
# Exclude tests which make API calls
%pytest -v test --ignore test/geocoders/

%files -n python3-%{pypi_name}
%doc AUTHORS CONTRIBUTING.md README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Mon Jul 25 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-8
- fix FTI

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21.0-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.0-1
- Update to latest upstream release 1.21.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.20.0-2
- Address issues (rhbz#1723052)

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.20.0-1
- Initial package for Fedora
