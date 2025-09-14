# Tests are not included in the PyPi source, but this PR should include them:
# https://github.com/Azure/azure-sdk-for-python/pull/21543
%bcond_with     tests

%global         srcname     azure-common

Name:           python-%{srcname}
Version:        1.1.28
Release:        %autorelease
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

# https://github.com/Azure/azure-sdk-for-python/issues/41648
Patch:          0001-Make-msrestazure-and-msrest-optional-dependencies.patch

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
Microsoft Azure Client Library for Python (Common)}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p4 -n %{srcname}-%{version}


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
%doc CHANGELOG.md README.md


%changelog
%autochangelog
