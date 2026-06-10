# Upstream has some basic scaffolding for running tests, but no tests are
# included yet in the 3.0.0 release. 😢
%bcond_with     tests

%global         srcname     azure-mgmt-subscription

Name:           python-%{srcname}
Version:        3.1.1
Release:        %autorelease
Summary:        Microsoft Azure Subscription Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

Epoch:          1

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-six

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

# Generated enum modules import six.with_metaclass, but six is not in the
# upstream dist metadata, so the dependency generators miss it (both the
# BuildRequires and this Requires must be added by hand). Needed at runtime
# whenever the module is imported.
Requires:       python3-six

%global _description %{expand:
Microsoft Azure Subscription Management Client Library for Python}

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
%doc CHANGELOG.md README.md


%changelog
%autochangelog
