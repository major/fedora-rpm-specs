%global pypi_name geoip2
%global srcname GeoIP2-python
%global desc This package provides an API for the GeoIP2 web services.
%global test_data MaxMind-DB
%global test_data_rls 1271107ccad72c320bc7dc8aefd767cba550101a

Name:           python-%{pypi_name}
Version:        5.0.1
Release:        %autorelease
Summary:        MaxMind GeoIP2 API

License:        Apache-2.0
URL:            https://www.maxmind.com/
Source0:        https://github.com/maxmind/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/maxmind/%{test_data}/archive/%{test_data_rls}/%{test_data}-%{test_data_rls}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{_bindir}/sphinx-build

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides the documentation for %{pypi_name}.

%prep
%autosetup -n %{srcname}-%{version} -a 1
rmdir tests/data
mv -f %{test_data}-%{test_data_rls} tests/data

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
sphinx-build -b html docs html
rm -rf html/.{buildinfo,doctrees}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# tests/webservice_test.py requires mocket not available in Fedora
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest tests/database_test.py tests/models_test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%files doc
%doc html/
%license LICENSE

%changelog
%autochangelog
