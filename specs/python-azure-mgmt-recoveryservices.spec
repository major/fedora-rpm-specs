# Upstream has no tests.
%bcond_with    tests

%global         srcname     azure-mgmt-recoveryservices
%global         tarball_name     azure_mgmt_recoveryservices

Name:           python-%{srcname}
Version:        4.0.0
Release:        %autorelease
Summary:        Microsoft Azure Recovery Services Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source:         %{pypi_source %{tarball_name} %{version}}

BuildArch:      noarch

Epoch:          1


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
Microsoft Azure Recovery Services Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{tarball_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


# LICENSE missing. Made a PR to fix:
# https://github.com/Azure/azure-sdk-for-python/pull/20178
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
