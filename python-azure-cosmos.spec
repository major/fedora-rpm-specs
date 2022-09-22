# All tests in 3.2.0 require networking, but this is corrected in future
# versions. However, the cosmos requirement from azure-cli is stuck at 3.2.0.
%bcond_with     tests

%global         srcname     azure-cosmos

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        Microsoft Azure Cosmos Client Library for Python
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
Microsoft Azure Cosmos Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Fix wrong-file-end-of-line-encoding.
sed -i 's/\r$//' README.md


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
%doc README.md samples
%license LICENSE.txt


%changelog
%autochangelog
