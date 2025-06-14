%bcond_with    tests

%global         srcname     azure-keyvault-securitydomain
%global         tarball     azure_keyvault_securitydomain

Name:           python-%{srcname}
Version:        1.0.0~b1
%global         pypi_version 1.0.0b1
Release:        %autorelease
Summary:        Azure Key Vault Security Domain client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball} %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure Key Vault Security Domain client library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{tarball}-%{pypi_version}


%generate_buildrequires
%pyproject_buildrequires -r


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
