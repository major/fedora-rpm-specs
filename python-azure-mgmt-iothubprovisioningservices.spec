# Upstream has skipped all tests.
%bcond_with     tests

%global         srcname     azure-mgmt-iothubprovisioningservices

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Microsoft Azure IoTHub Provisioning Services Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch


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
Microsoft Azure IoTHub Provisioning Services Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove the customized wheel builder included by Microsoft that adds
# azure-mgmt-nspkg to the requirements.
sed -i '/azure-namespace-package/d' setup.cfg
sed -i '/azure_bdist_wheel.py/d' MANIFEST.in
rm -f azure_bdist_wheel.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# PEP 420 allows implicit namespace packaging without additional __init__.py
# files. Remove unneccessary __init__.py that conflicts with other packages.
rm -rf %{buildroot}%{python3_sitelib}/azure/{__init__.py,__pycache__}
rm -rf %{buildroot}%{python3_sitelib}/azure/mgmt/{__init__.py,__pycache__}

%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
%pytest --disable-warnings
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
