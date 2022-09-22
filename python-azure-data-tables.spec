# Disable tests everywhere since the latest version requires docker
# for testing.
%bcond_with     tests

%global         srcname     azure-data-tables

Name:           python-%{srcname}
Version:        12.4.0
Release:        %autorelease
Summary:        Microsoft Azure Azure Data Tables Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
# NOTE(mhayden): Upstream does not include some of the testing VCR cassettes in their
# code released to PyPi because it makes their archive really large. Because of this,
# about half of the tests fail. 😭
# This source comes from making a git archive of the main azure-sdk-for-python
# repository. To reproduce the source code, run these commands:
#
#   git clone https://github.com/azure/azure-sdk-for-python
#   cd azure-sdk-for-python
#   export VERSION=12.4.0
#   git archive --format tar.gz --prefix=azure-data-tables-${VERSION}/ azure-data-tables_${VERSION}:sdk/tables/azure-data-tables \
#     > azure-data-tables-$VERSION.tgz
#
Source0:        azure-data-tables-12.4.0.tgz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-azure-sdk-tools
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-cosmosdb)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Azure Data Tables Client Library for Python}

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
# NOTE(mhayden): The tests which require network access carry the "live_test_only"
# marker and we skip those here. It's only about 5-10% of the total tests.
%pytest -m "not live_test_only" --disable-warnings
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md samples/


%changelog
%autochangelog
