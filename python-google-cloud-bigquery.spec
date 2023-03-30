%bcond_without  tests

# opentelemetry-instrumentation is not yet packaged.
%bcond_with     opentelemetry-instrumentation
# db-dtypes is not yet packaged
%bcond_with     db-dtypes

%global         srcname     google-cloud-bigquery
%global         forgeurl    https://github.com/googleapis/python-bigquery
Version:        3.9.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google BigQuery

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(google-cloud-testutils)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
Python Client for Google BigQuery}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

# Extra packages
%pyproject_extras_subpkg -n python3-%{srcname} bqstorage
%if %{with db-dtypes}
%pyproject_extras_subpkg -n python3-%{srcname} pandas
%endif

%if %{with opentelemetry-instrumentation}
%pyproject_extras_subpkg -n python3-%{srcname} opentelemetry
%endif

%pyproject_extras_subpkg -n python3-%{srcname} geopandas
%pyproject_extras_subpkg -n python3-%{srcname} ipython
%pyproject_extras_subpkg -n python3-%{srcname} tqdm


%prep
%forgeautosetup

# Allow a slightly older protobuf.
sed -i 's/"protobuf.*",/"protobuf>=3.19.4",/' setup.py

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'

# Allow a slightly older version of grpcio.
sed -i 's/1.49.1/1.48.3/g' setup.py

# Remove Python version limitation.
sed -i '/python_requires/d' setup.py

# Remove upper bound on Shapely.
sed -i 's/Shapely>=1.8.4, <2.0dev/Shapely>=1.8.4/' setup.py


%generate_buildrequires
%pyproject_buildrequires -x bqstorage,%{?with_db-dtypes:pandas,geopandas,}%{?with_opentelemetry-instrumentation:opentelemetry,}ipython,tqdm


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_bigquery-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
