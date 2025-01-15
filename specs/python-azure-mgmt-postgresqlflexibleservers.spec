%global         srcname         azure-mgmt-postgresqlflexibleservers
%global         tarball_name    azure_mgmt_postgresqlflexibleservers

Name:           python-%{srcname}
Version:        1.1.0~b1
%global         pypi_version    1.1.0b1
Release:        %autorelease
Summary:        The Microsoft Azure Postgresqlflexibleservers Management Client Library
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
This is the Microsoft Azure Postgresqlflexibleservers Management Client Library.}


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{tarball_name}-%{pypi_version}


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
