%global         srcname     azure-mgmt-consumption

Name:           python-%{srcname}
Version:        10.0.0
Release:        %autorelease
Summary:        Microsoft Azure Consumption Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source:         %{pypi_source azure-mgmt-consumption %{version} zip}

Epoch:          1

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure Consumption Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure-mgmt-consumption-%{version}


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
