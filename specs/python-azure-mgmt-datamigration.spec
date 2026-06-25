
%global         srcname     azure-mgmt-datamigration

Name:           python-%{srcname}
Version:        10.1.0
Release:        %autorelease
Summary:        Microsoft Azure Data Migration Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_mgmt_datamigration %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure Data Migration Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure_mgmt_datamigration-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure



%check
%pyproject_check_import


# LICENSE file missing. PR made to fix:
# https://github.com/Azure/azure-sdk-for-python/pull/20164
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
