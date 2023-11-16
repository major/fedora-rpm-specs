# Upstream's tests require docker now. 😢
%bcond_with    tests

%global         srcname     azure-keyvault-keys

Name:           python-%{srcname}
Version:        4.9.0~b3
%global         pypi_version 4.9.0b3
Release:        %autorelease
Summary:        Microsoft Azure Key Vault Keys Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-core)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(dateutils)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
Microsoft Azure Key Vault Keys Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{pypi_version}


%generate_buildrequires
%pyproject_buildrequires -r


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


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
