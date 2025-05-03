# No tests from upstream yet.
%bcond_with     tests

%global         srcname     azure-multiapi-storage

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Microsoft Azure Storage Client Library for Python with multi API version support
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

# Needed for import checks.
BuildRequires:  python3dist(aiohttp)

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(azure-storage-blob)
BuildRequires:  python3dist(azure-storage-common)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Storage Client Library for Python with multi API version
support}

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
%pyproject_check_import -e azure.multiapi.storagev2.filedatalake* -e azure.multiapi.storagev2.queue*

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
