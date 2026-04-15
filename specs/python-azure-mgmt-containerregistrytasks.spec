Name:           python-azure-mgmt-containerregistrytasks
Version:        1.0.0~b1
%global         pypi_version 1.0.0b1
Release:        %autorelease
Summary:        The Azure Containerregistrytasks Management Client Library
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-containerregistrytasks/
Source:         %{pypi_source azure_mgmt_containerregistrytasks %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This is the Microsoft Azure Containerregistrytasks Management Client Library.
This package has been tested with Python 3.9+. For a more complete view of
Azure libraries, see the azure sdk python release.}

%description %{_description}


%package -n python3-azure-mgmt-containerregistrytasks
Summary:        %{summary}

%description -n python3-azure-mgmt-containerregistrytasks %{_description}


%prep
%autosetup -n azure_mgmt_containerregistrytasks-%{pypi_version}


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


%files -n python3-azure-mgmt-containerregistrytasks -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
