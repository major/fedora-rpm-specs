# No tests included yet.
%bcond_with     tests

%global         srcname     azure-mgmt-msi

Name:           python-%{srcname}
Version:        7.0.0
Release:        %autorelease
Summary:        Microsoft Azure MSI Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure MSI Management Client Library for Python}

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

%if %{with tests}
%pytest
%endif


%install
%pyproject_install
%pyproject_save_files azure


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md


%changelog
%autochangelog
