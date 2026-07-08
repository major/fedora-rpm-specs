
%global         srcname     azure-mgmt-loganalytics

Name:           python-%{srcname}
Version:        13.1.1
Release:        %autorelease
Summary:        Microsoft Azure Log Analytics Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_mgmt_loganalytics %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure Log Analytics Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n azure_mgmt_loganalytics-%{version}


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
