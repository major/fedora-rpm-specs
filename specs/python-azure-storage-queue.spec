Name:           python-azure-storage-queue
Version:        12.15.0
Release:        %autorelease
Summary:        Azure Storage Queues client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-storage-queue/
Source:         %{pypi_source azure_storage_queue %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure Queue storage is a service for storing large numbers of messages that can
be accessed from anywhere in the world via authenticated calls using HTTP or
HTTPS. A single queue message can be up to 64 KiB in size, and a queue can
contain millions of messages, up to the total capacity limit of a storage
account.}

%description %{_description}


%package -n python3-azure-storage-queue
Summary:        %{summary}

%description -n python3-azure-storage-queue %{_description}


%prep
%autosetup -n azure_storage_queue-%{version}


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


%files -n python3-azure-storage-queue -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
