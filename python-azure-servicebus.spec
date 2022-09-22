# EPEL9 does not have python-aiohttp packaged yet.
%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif

%global         srcname     azure-servicebus

Name:           python-%{srcname}
Version:        7.6.1
Release:        %autorelease
Summary:        Microsoft Azure Service Bus Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch


BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-mgmt-servicebus)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Service Bus Client Library for Python}

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
# Many tests try to connect to various Azure APIs during the test and that won't work
# during the package build. These exclusions remove those tests while keeping as many of
# the non-network tests as possible.
%pytest -m "not (live_test_only or liveTest)" \
    --ignore=tests/async_tests --ignore=tests/mgmt_tests
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md migration_guide.md README.md samples


%changelog
%autochangelog
