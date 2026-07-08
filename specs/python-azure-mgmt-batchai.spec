%global         srcname     azure-mgmt-batchai

Name:           python-%{srcname}
Version:        7.0.0
Release:        %autorelease
Summary:        Microsoft Azure Batch AI Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source:         %{pypi_source azure_mgmt_batchai %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel
# Upstream depends on this, but fails to list it as such. It's also a very dead dependency.
BuildRequires:  python3dist(msrest)


%global _description %{expand:
Microsoft Azure Batch AI Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
# Upstream depends on this, but fails to list it as such. It's also a very dead dependency.
Requires:       python3dist(msrest)

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure_mgmt_batchai-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
