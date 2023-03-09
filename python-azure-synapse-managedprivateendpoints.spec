# No tests from upstream yet.
%bcond_with     tests

%global         srcname     azure-synapse-managedprivateendpoints

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        Microsoft Azure Synapse Managed Private Endpoints Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
# NOTE(mhayden): Still trying to get upstream to accept multiple PRs to add
# licenses to all PyPi packages, but they're moving slowly.
Source1:        https://github.com/Azure/azure-sdk-for-python/raw/%{srcname}_%{version}/LICENSE.txt

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
Microsoft Azure Synapse Managed Private Endpoints Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
cp %SOURCE1 .


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


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.txt


%changelog
%autochangelog
