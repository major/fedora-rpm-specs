# When bootstrapping, break circular dependency on starlette in the tests.
%bcond bootstrap 0

Name:           python-databases
Summary:        Async database support for Python
Version:        0.8.0
Release:        %autorelease

License:        BSD-3-Clause
URL:            https://www.encode.io/databases/
%global forgeurl https://github.com/encode/databases
Source:         %{forgeurl}/archive/%{version}/databases-%{version}.tar.gz

# Fix flaky tests with in-memory SQLite databases
# https://github.com/encode/databases/pull/569
#
# Fixes:
#
# New test test_should_remove_ref_on_disconnect in 0.8.0 fails on Fedora Linux
# https://github.com/encode/databases/issues/567
Patch:          %{forgeurl}/pull/569.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# Additional BR’s for testing, from requirements.txt only (therefore not
# generated):
# “Sync database drivers for standard tooling around
# setup/teardown/migrations.”
BuildRequires:  python3dist(psycopg2)
BuildRequires:  python3dist(pymysql)

# “Testing”
# We have excluded formatters, linters, and analysis tools: autoflake, black,
# codecov, isort, mypy, pytest-cov
BuildRequires:  python3dist(pytest)
%if %{without bootstrap}
BuildRequires:  python3dist(starlette)
# Used only as a soft dependency of starlette
BuildRequires:  python3dist(requests)
# Used only as a soft dependency of starlette.testclient
BuildRequires:  python3dist(httpx)
%endif

%global common_description %{expand:
Databases gives you simple asyncio support for a range of databases.

It allows you to make queries using the powerful SQLAlchemy Core expression
language, and provides support for PostgreSQL, MySQL, and SQLite.

Databases is suitable for integrating against any async Web framework, such as
Starlette, Sanic, Responder, Quart, aiohttp, Tornado, or FastAPI.

Documentation: https://www.encode.io/databases/

Community: https://discuss.encode.io/c/databases}

%description %{common_description}


# README.md:
#
#   Note that if you are using any synchronous SQLAlchemy functions such as
#   `engine.create_all()` or [alembic][alembic] migrations then you still have
#   to install a synchronous DB driver: [psycopg2][psycopg2] for PostgreSQL and
#   [pymysql][pymysql] for MySQL.
#
# Therefore we manually write out the extras metapackages for PostgreSQL and
# MySQL backends so that we can add these drivers as weak dependencies
# (Recommends). We can still handle the SQLite extras the easy way.
%package -n python3-databases+postgresql
Summary:        Metapackage for python3-databases: postgresql extras

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(psycopg2)

%description -n python3-databases+postgresql
This is a metapackage bringing in postgresql extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+postgresql
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+asyncpg
Summary:        Metapackage for python3-databases: asyncpg extras

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(psycopg2)

%description -n python3-databases+asyncpg
This is a metapackage bringing in asyncpg extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+asyncpg
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+aiopg
Summary:        Metapackage for python3-databases: aiopg extras

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(psycopg2)

# Provide upgrade/migration path for three releases:
%if 0%{?fedora} && 0%{?fedora} < 40
Provides:       python3-databases+postgresql_aiopg = %{version}-%{release}
Obsoletes:      python3-databases+postgresql_aiopg < 0.6.0-1
%endif

%description -n python3-databases+aiopg
This is a metapackage bringing in aiopg extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+aiopg
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+mysql
Summary:        Metapackage for python3-databases: mysql extras

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(pymysql)

%description -n python3-databases+mysql
This is a metapackage bringing in mysql extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+mysql
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+aiomysql
Summary:        Metapackage for python3-databases: aiomysql extras

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(pymysql)

%description -n python3-databases+aiomysql
This is a metapackage bringing in aiomysql extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+aiomysql
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+asyncmy
Summary:        Metapackage for python3-databases: asyncmy extras
Recommends:     python3dist(pymysql)

Requires: python3-databases = %{version}-%{release}

# Provide upgrade/migration path for three releases:
%if 0%{?fedora} && 0%{?fedora} < 40
Provides:       python3-databases+mysql_asyncmy = %{version}-%{release}
Obsoletes:      python3-databases+mysql_asyncmy < 0.6.0-1
%endif

%description -n python3-databases+asyncmy
This is a metapackage bringing in asyncmy extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+asyncmy
%ghost %{python3_sitelib}/*.dist-info


%pyproject_extras_subpkg -n python3-databases sqlite aiosqlite


%package -n     python3-databases
Summary:        %{summary}

Obsoletes:      python-databases-doc < 0.5.2-4

%description -n python3-databases %{common_description}


%prep
%autosetup -n databases-%{version} -p1


%generate_buildrequires
%{pyproject_buildrequires \
    -x postgresql \
    -x asyncpg \
    -x aiopg \
    -x mysql \
    -x aiomysql \
    -x asyncmy \
    -x sqlite \
    -x aiosqlite}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l databases


%check
%if %{with bootstrap}
rm tests/test_integration.py
%endif

# Since we won’t be able to test all of the backends, we start with an
# import-only “smoke test”
%pyproject_check_import

# E   ModuleNotFoundError: No module named 'tests'
touch tests/__init__.py

# We can only easily run the tests with SQLite; other databases require a
# properly configured server, which we cannot in general provide as an
# unprivileged user. However, see the MySQL support below.
#
# The following environment variable is a comma-separated list with (optional?)
# whitespace.
export TEST_DATABASE_URLS="sqlite:///testsuite, sqlite+aiosqlite:///testsuite"

%pytest --verbose


%files -n python3-databases -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
