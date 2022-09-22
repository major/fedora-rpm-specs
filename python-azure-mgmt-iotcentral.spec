# Upstream has not included tests yet, but there is a scaffolding for adding
# them in the future.
%bcond_with     tests

%global         srcname     azure-mgmt-iotcentral

Name:           python-%{srcname}
Version:        10.0.0~b1
%global         pypi_version    10.0.0b1
Release:        %autorelease
Summary:        Microsoft Azure IoTCentral Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{pypi_version} zip}

BuildArch:      noarch

Epoch:          2

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
Microsoft Azure IoTCentral Management Client Library for Python}

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


# LICENSE missing. Made PR to fix.
# https://github.com/Azure/azure-sdk-for-python/pull/20167
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
