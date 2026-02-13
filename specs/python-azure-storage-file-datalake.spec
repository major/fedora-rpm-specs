Name:           python-azure-storage-file-datalake
Version:        12.23.0
Release:        %autorelease
Summary:        Azure DataLake service client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-storage-file-datalake/
Source:         %{pypi_source azure_storage_file_datalake %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure DataLake service client library for Python.}

%description %{_description}


%package -n python3-azure-storage-file-datalake
Summary:        %{summary}

%description -n python3-azure-storage-file-datalake %{_description}


%prep
%autosetup -n azure_storage_file_datalake-%{version}


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


%files -n python3-azure-storage-file-datalake -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
