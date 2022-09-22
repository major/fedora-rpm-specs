%global         srcname     azure-keyvault

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Microsoft Azure Key Vault Client Libraries for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
Patch0:         python-azure-keyvault-remove-nspkg.patch

Epoch:          1

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure Key Vault Client Libraries for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p0 -n %{srcname}-%{version}

# Remove the custom wheel builder.
rm -fv azure_bdist_wheel.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

# PEP 420 allows implicit namespace packaging without additional __init__.py
# files. Remove unneccessary __init__.py that conflicts with other packages.
rm -rf %{buildroot}%{python3_sitelib}/azure/{__init__.py,__pycache__}


%files -n python3-%{srcname}
%doc README.rst HISTORY.rst
%{python3_sitelib}/azure/keyvault
%{python3_sitelib}/azure_keyvault-%{version}.dist-info


%changelog
%autochangelog
