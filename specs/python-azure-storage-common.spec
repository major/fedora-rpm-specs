# No tests from upstream yet.
%bcond_with     tests

%global         srcname     azure-storage-common

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Microsoft Azure Storage Common Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

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
Microsoft Azure Storage Common Client Library for Python}

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
%doc README.rst
%license LICENSE.txt


%changelog
%autochangelog
