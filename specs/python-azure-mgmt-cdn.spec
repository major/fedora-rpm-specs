%global         srcname     azure-mgmt-cdn

Name:           python-%{srcname}
Version:        13.1.1
Release:        %autorelease
Summary:        Microsoft Azure CDN Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source:         %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure CDN Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
%pyproject_check_import


%install
%pyproject_install
%pyproject_save_files -l azure


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
