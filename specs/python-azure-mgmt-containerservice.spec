# Upstream has marked all of their tests as skipped.
%bcond_with     tests

Name:           python-azure-mgmt-containerservice
Version:        40.1.0
Release:        %autorelease
Summary:        Microsoft Azure Container Service Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-containerservice/
Source:         %{pypi_source azure_mgmt_containerservice %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-mgmt-storage)
BuildRequires:  python3dist(azure-mgmt-network)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif


%global _description %{expand:
Microsoft Azure Container Service Management Client Library for Python}

%description %{_description}


%package -n python3-azure-mgmt-containerservice
Summary:        %{summary}
%description -n python3-azure-mgmt-containerservice %{_description}


%prep
%autosetup -n azure_mgmt_containerservice-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


%check
%pyproject_check_import

%if %{with tests}
%pytest --disable-warnings
%endif


%files -n python3-azure-mgmt-containerservice -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
