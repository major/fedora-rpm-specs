# Enable tests everywhere except EPEL 9, where python-httpretty is not backported.
%if 0%{?el9} || 0%{?centos} >= 9
%bcond_with    tests
%else
# change back to bcond_without when the azure-sdk-tools/azure-devtools mess gets sorted out.
# It seems azure-devtools now lives inside azure-sdk-tools, as a separate package, and renamed.
%bcond_with     tests
%endif

%global         srcname     azure-appconfiguration

Name:           python-%{srcname}
Version:        1.7.2
Release:        %autorelease
Summary:        Microsoft App Configuration Data Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_appconfiguration %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Microsoft App Configuration Data Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure_appconfiguration-%{version}


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
# All of the configuration client tests require network access.
%pytest --ignore-glob=tests/test_azure_configuration_client*.py
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
