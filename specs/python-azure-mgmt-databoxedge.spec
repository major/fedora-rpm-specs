%global         srcname     azure-mgmt-databoxedge

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Microsoft Azure Databoxedge Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel
# The module depends on this but doesn't declare that
BuildRequires:  python3dist(six)

%global _description %{expand:
Microsoft Azure Databoxedge Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
# The module depends on this but doesn't declare that
Requires:       python3dist(six)

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


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
%doc README.md CHANGELOG.md


%changelog
%autochangelog
