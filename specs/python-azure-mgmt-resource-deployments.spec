Name:           python-azure-mgmt-resource-deployments
Version:        1.0.0~b1
%global         pypi_version %(echo '%{version}' | tr -d '~')
Release:        %autorelease
Summary:        Microsoft Azure Resource Deployments Management Client Library
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-resource-deployments/
Source0:        %{pypi_source azure_mgmt_resource_deployments %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Resource Deployments Management Client Library}

%description %{_description}


%package -n python3-azure-mgmt-resource-deployments
Summary:        %{summary}

%description -n python3-azure-mgmt-resource-deployments %{_description}


%prep
%autosetup -n azure_mgmt_resource_deployments-%{pypi_version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


# Like other Azure SDK packages, the tests expect Azure to be available
%check
%pyproject_check_import


%files -n python3-azure-mgmt-resource-deployments -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
