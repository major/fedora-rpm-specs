# Enable tests everywhere except EPEL 9, where python-pytest-aiohttp is not backported.
%if 0%{?el9} || 0%{?centos} >= 9
%bcond_with    tests
%else
%bcond_without tests
%endif

%global         srcname     azure-mgmt-datamigration

Name:           python-%{srcname}
Version:        10.0.0
Release:        %autorelease
Summary:        Microsoft Azure Data Migration Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-network)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Data Migration Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure



%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


# LICENSE file missing. PR made to fix:
# https://github.com/Azure/azure-sdk-for-python/pull/20164
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
