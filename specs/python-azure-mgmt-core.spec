%global         srcname     azure-mgmt-core
%global         tarball_name     azure_mgmt_core

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        Azure Management Core Library
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel


%global _description %{expand:
Azure Management Core Library}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{tarball_name}-%{version}


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
%doc README.md


%changelog
%autochangelog
