%global srcname azure-storage-blob

Name:           python-%{srcname}
Version:        12.26.0
Release:        %autorelease
Summary:        Azure Storage Blobs client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source:         %{pypi_source azure_storage_blob}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure Storage Blobs client library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%pyproject_extras_subpkg -n python3-%{srcname} aio


%prep
%autosetup -n azure_storage_blob-%{version}


%generate_buildrequires
%pyproject_buildrequires -x aio


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


%check
%pyproject_check_import

# pytest unittest are not run as the test depends on the vcrpy that is pinned https://github.com/Azure/azure-sdk-for-python/tree/main/tools/vcrpy
# Furthermore the pypi_source file are missing some test files used to run the test e.g recording rules


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
