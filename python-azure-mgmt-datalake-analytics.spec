# Upstream has no tests yet.
%bcond_with     tests

%global         srcname     azure-mgmt-datalake-analytics

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease
Summary:        Microsoft Azure Data Lake Analytics Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

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
Microsoft Azure Data Lake Analytics Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove the customized wheel builder included by Microsoft that adds
# azure-mgmt-nspkg to the requirements.
sed -i '/^azure-namespace-package/d' setup.cfg
rm -f azure_bdist_wheel.py

# Fix line endings.
sed -i 's/\r$//' README.rst


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
rm -rf %{buildroot}%{python3_sitelib}/azure/mgmt/datalake/{__init__.py,__pycache__}

%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname}
%doc README.rst HISTORY.rst
%{python3_sitelib}/azure/mgmt/datalake/analytics
%{python3_sitelib}/azure_mgmt_datalake_analytics-%{version}.dist-info


%changelog
%autochangelog
