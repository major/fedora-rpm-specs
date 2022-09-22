# EPEL9 does not have python-aiohttp packaged yet.
%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif

%global         srcname     azure-mgmt-consumption

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Microsoft Azure Consumption Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
# This source comes from making a git archive of the main azure-sdk-for-python
# repository. To reproduce the source code, run the generate-source.sh script.
Source0:        %{srcname}-%{version}.tgz

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
Microsoft Azure Consumption Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p0 -n %{srcname}-%{version}

# Remove the custom wheel builder.
sed -i '/azure-namespace-package/d' setup.cfg
rm -fv azure_bdist_wheel.py


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
%pytest
%endif


%files -n python3-%{srcname}
%doc README.rst HISTORY.rst
%{python3_sitelib}/azure/mgmt/consumption
%{python3_sitelib}/azure_mgmt_consumption-%{version}.dist-info


%changelog
%autochangelog
