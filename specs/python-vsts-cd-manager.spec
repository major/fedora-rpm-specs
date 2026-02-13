%global         srcname     vsts-cd-manager

Name:           python-%{srcname}
Version:        1.0.2
Release:        %autorelease
Summary:        Visual Studio Team Services Continuous Delivery Manager
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
Patch0:         %{name}-rm-python-mock-usage.diff

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package provides the class ContinuousDeliveryManager and supporting
classes. This CD manager class allows the caller to manage Azure Continuous
Delivery pipelines that are maintained within a VSTS account.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Fix wrong line endings in the README.rst.
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/aex_accounts
%{python3_sitelib}/continuous_delivery
%{python3_sitelib}/vsts_cd_manager
%{python3_sitelib}/vsts_info_provider
%{python3_sitelib}/vsts_cd_manager-%{version}.dist-info


%changelog
%autochangelog
