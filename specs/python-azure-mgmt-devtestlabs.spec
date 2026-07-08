%global         srcname     azure-mgmt-devtestlabs

Name:           python-%{srcname}
Version:        9.0.1
Release:        %autorelease
Summary:        Microsoft Azure DevTestLabs Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_mgmt_devtestlabs %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure DevTestLabs Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure_mgmt_devtestlabs-%{version}


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
