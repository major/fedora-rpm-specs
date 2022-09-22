# Tests are skipped for now since all of them require running a docker daemon
# with network access.
%bcond_with     tests

%global         srcname     azure-mgmt-batch

Name:           python-%{srcname}
Version:        16.2.0
Release:        %autorelease
Summary:        Microsoft Azure Batch Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
# This source comes from making a git archive of the main azure-sdk-for-python
# repository. To reproduce the source code, run the generate-source.sh script.
Source0:        %{srcname}-%{version}.tgz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-network)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Batch Management Client Library for Python}

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
%doc README.md CHANGELOG.md


%changelog
%autochangelog
