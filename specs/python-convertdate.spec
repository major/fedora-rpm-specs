%global pypi_name convertdate

Name:           python-%{pypi_name}
Version:        2.4.1
Release:        %autorelease
Summary:        Python module to convert date formats and calculating holidays

License:        MIT
URL:            https://github.com/fitnr/convertdate
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO,
Julian, Mayan and Persian.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{pypi_name}
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO,
Julian, Mayan and Persian.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v tests -k "not testPersian"

%files -n python3-%{pypi_name}
%doc HISTORY.rst README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-*.dist-info
%{python3_sitelib}/%{pypi_name}/

%changelog
%autochangelog
