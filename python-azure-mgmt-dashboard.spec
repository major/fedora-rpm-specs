# No tests provided by upstream.
%bcond_with     tests

%global         srcname     azure-mgmt-dashboard

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Microsoft Azure Dashboard Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
The Microsoft Azure Dashboard Management Client Library provides
a Python client for managing Azure DevOps dashboards.}

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


%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
%autochangelog
