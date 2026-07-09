Name:           python-azure-mgmt-domainregistration
Version:        1.0.0
Release:        %autorelease
Summary:        Microsoft Azure Domainregistration Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-domainregistration/
Source:         %{pypi_source azure_mgmt_domainregistration %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Domainregistration Management Client Library for Python.}

%description %{_description}


%package -n python3-azure-mgmt-domainregistration
Summary:        %{summary}

%description -n python3-azure-mgmt-domainregistration %{_description}


%prep
%autosetup -n azure_mgmt_domainregistration-%{version}


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


%files -n python3-azure-mgmt-domainregistration -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
