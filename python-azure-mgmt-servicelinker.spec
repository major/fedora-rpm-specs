# This SDK component has no tests upstream yet. 😭
%bcond_with     tests

%global         srcname     azure-mgmt-servicelinker

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Microsoft Azure Servicelinker Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

# NOTE(mhayden): Set an epoch number because I used 1.0.0b1 as a version as a mistake
# and 1.0.0~b2 sorts poorly with it. 🤦🏻‍♂️
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
%endif

%global _description %{expand:
Microsoft Azure Servicelinker Management Client Library for Python}

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


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
