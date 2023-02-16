# NOTE(mhayden): Temporarily disabling tests due to import errors.
%bcond_with     tests

# opentelemetry-instrumentation is not yet packaged.
%bcond_with     opentelemetry-instrumentation
# db-dtypes is not yet packaged
%bcond_with     db-dtypes

%global         srcname     google-cloud-bigquery
%global         forgeurl    https://github.com/googleapis/python-bigquery
Version:        3.4.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google BigQuery

License:        ASL 2.0
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

# Remove the upper bound on the version of packaging
sed -r -i "s/(packaging\\b.*)(, [[:blank:]]*<[^'\"]*)/\1/" setup.py

# Remove the upper bound on the version of pyarrow.
sed -r -i "s/(pyarrow\\b.*)(, [[:blank:]]*<[^'\"]*)/\1/" setup.py

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'

# Remove Python version limitation.
sed -i '/python_requires/d' setup.py


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
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest tests/unit \
    -k "not test_to_query_parameters_w_list \
        and not test_consume_unexpected_eol"
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_bigquery-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
