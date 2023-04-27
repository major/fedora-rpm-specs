# No tests provided. 😢
%bcond_with    tests

%global         srcname     azure-mgmt-rdbms

Name:           python-%{srcname}
Version:        10.2.0~b7
%global         pypi_version    10.2.0b7
Release:        %autorelease
Summary:        Microsoft Azure RDBMS Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{pypi_version} zip}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

BuildRequires:  python3dist(msrest)

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
Microsoft Azure RDBMS Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{pypi_version}


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


# LICENSE missing. Made PR to fix:
# https://github.com/Azure/azure-sdk-for-python/pull/20176
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
