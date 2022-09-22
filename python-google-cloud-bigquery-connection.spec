# F35: Do not update past 1.5.0. F35's protobuf is too old.

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-bigquery-connection
%global         forgeurl    https://github.com/googleapis/python-bigquery-connection
Version:        1.7.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python SDK for Google Cloud BigQuery Connection API

License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(grpcio-testing)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
Python SDK for Google Cloud BigQuery Connection API:
Manage BigQuery connections to external data sources.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%pyproject_check_import

%if %{with tests}
%pytest --disable-warnings tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.rst SECURITY.md
%{python3_sitelib}/google_cloud_bigquery_connection-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
