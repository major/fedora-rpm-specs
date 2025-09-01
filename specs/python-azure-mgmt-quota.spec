%global         srcname azure-mgmt-quota
%global         upstream_version 2.0.0

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Microsoft Azure Quota Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_mgmt_quota %{upstream_version}}

BuildArch:      noarch

BuildRequires:  docker
BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Quota Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure_mgmt_quota-%{upstream_version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
