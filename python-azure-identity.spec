# Upstream's tests now require docker to be running.
%bcond_with     tests

%global         srcname     azure-identity

Name:           python-%{srcname}
Version:        1.15.0
Release:        %autorelease
Summary:        Microsoft Azure Identity Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

Epoch:          1

BuildArch:      noarch


BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Identity Library for Python}

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
# test_persistent_cache_linux fails with Python 3.12
# we skip it as it's likely problem between mocked objects
# reported upstream: https://github.com/Azure/azure-sdk-for-python/issues/30994
%pytest -k "not test_timeout and not test_persistent_cache_linux"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
