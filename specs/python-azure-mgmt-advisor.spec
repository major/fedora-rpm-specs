%global         srcname     azure-mgmt-advisor

Name:           python-%{srcname}
Version:        9.0.1
Release:        %autorelease
Summary:        Microsoft Azure Advisor Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_mgmt_advisor %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Advisor Client Library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n azure_mgmt_advisor-%{version}


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
