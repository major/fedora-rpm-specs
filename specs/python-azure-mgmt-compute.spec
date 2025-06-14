# NOTE(mhayden): Tests require docker + network access. Disabled for now.
%bcond_with     tests

%global         srcname     azure-mgmt-compute
%global         tarball_name     azure_mgmt_compute

Name:           python-%{srcname}
Version:        34.1.0
Release:        %autorelease
Summary:        Microsoft Azure Compute Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-authorization)
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
Microsoft Azure Compute Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{tarball_name}-%{version}


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
%pytest --disable-warnings
%endif


# LICENSE file is missing. PR made to fix:
# https://github.com/Azure/azure-sdk-for-python/pull/20160
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
