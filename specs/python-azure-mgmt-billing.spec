%global         srcname     azure-mgmt-billing

Name:           python-%{srcname}
Version:        6.0.0
Release:        %autorelease
Summary:        Microsoft Azure Billing Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch


BuildRequires:  python3-devel
# We're stuck on an old version of this package because azure-cli; it depends on six
# but doesn't include that detail in its metadata.
BuildRequires:  python3dist(six)


%global _description %{expand:
Microsoft Azure Billing AI Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
# We're stuck on an old version of this package because azure-cli; it depends on six
# but doesn't include that detail in its metadata.
BuildRequires:  python3dist(six)

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
