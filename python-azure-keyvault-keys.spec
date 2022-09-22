# Enable tests everywhere except EPEL 9, where more backports are needed.
%if 0%{?el9} || 0%{?centos} >= 9
%bcond_with    tests
%else
%bcond_without tests
%endif

%global         srcname     azure-keyvault-keys

Name:           python-%{srcname}
Version:        4.5.1
Release:        %autorelease
Summary:        Microsoft Azure Key Vault Keys Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-core)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(dateutils)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
Microsoft Azure Key Vault Keys Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%if %{with tests}
%check
%pyproject_check_import

# NOTE(mhayden): Skip some tests that require network connectivity to Azure's
# APIs. The challenge_auth/parse_id tests require parameterized, which depends on the
# orhpaned nose2.
%pytest --disable-warnings \
    --ignore-glob=tests/test_*crypto*.py \
    --ignore-glob=tests/test_key*.py \
    --ignore-glob=tests/test_samples_keys*.py \
    --ignore-glob=tests/test_challenge_auth*.py \
    --ignore-glob=tests/test_parse_id.py \
    -k "not test_parse_key_id_with_version"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
