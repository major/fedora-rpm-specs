# EPEL9 does not have python-aiohttp packaged yet.
%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif

%global         srcname     azure-loganalytics

Name:           python-%{srcname}
Version:        0.1.0
Release:        %autorelease
Summary:        Microsoft Azure Log Analytics Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
# This source comes from making a git archive of the main azure-sdk-for-python
# repository. To reproduce the source code, run the generate-source.sh script.
Source0:        %{srcname}-%{version}.tgz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(msrestazure)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Log Analytics Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove the customized wheel builder included by Microsoft that adds
# azure-nspkg to the requirements.
sed -i '/azure-namespace-package/d' setup.cfg
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

%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/azure/loganalytics
%{python3_sitelib}/azure_loganalytics-%{version}.dist-info


%changelog
%autochangelog
