# No tests are included with this version of azure-datalake-store.
%bcond_with     tests

%global         srcname     azure-datalake-store

Name:           python-%{srcname}
Version:        0.0.49
Release:        %autorelease
Summary:        Azure Data Lake Store Filesystem Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

Epoch:          1

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Azure Data Lake Store Filesystem Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Fix incorrect line endings in the README.
sed -i 's/\r$//' README.rst


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure

# Remove the samples since many of them are empty or have wrong line endings.
rm -rf %{buildroot}%{python3_sitelib}/samples


%check
%pyproject_check_import -e 'samples*'

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.rst


%changelog
%autochangelog
