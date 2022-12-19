# When bootstrapping, break circular dependency on starlette in the tests.
%bcond_with bootstrap

# MySQL tests require interacting with a temporary MySQL database. We are able
# to do this, but leave a build conditional in case it breaks.
%bcond_without mysql_tests

# Post-release snapshot
#
# Includes upstream PR#513 “Fixes breaking changes in SQLAlchemy cursor”
%global commit 81cc6fdb1ce4e78875960a8a262a4b134745946e
%global snapdate 20221217

Name:           python-databases
Summary:        Async database support for Python
Version:        0.6.2%{?commit:^%{snapdate}git%(echo '%{commit}' | cut -b -7)}
Release:        %autorelease

%{?!commit:%global srcversion %{version}}
%{?commit:%global srcversion %{commit}}

License:        BSD-3-Clause
URL:            https://www.encode.io/databases/
%global forgeurl https://github.com/encode/databases
Source0:        %{forgeurl}/archive/%{srcversion}/databases-%{srcversion}.tar.gz

# This package contains no compiled code and should be inherently noarch, but
# the asyncmy dependency for the mysql_asyncmy/mysql+asyncmy extra is
# ExcludeArch on 32-bit platforms (RHBZ#2060899), which unfortunately means
# this package as a whole must be archful in order to drop that extra on the
# affected platforms. We can still make the binary RPMs noarch, except for the
# affected extra metapackage.
%global debug_package %{nil}
%if 0%{?__isa_bits} != 32
%global with_asyncmy 1
%endif

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

%if %{with mysql_tests}
BuildRequires:  mariadb-server
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
# MySQL backends so that we can add these drivers as Recommends. We can still
# handle the SQLite extras the easy way—but we don’t, because they would
# inherit the archfulness of the base package, and we want them to be noarch.
%package -n python3-databases+postgresql
Summary:        Metapackage for python3-databases: postgresql extras

BuildArch:      noarch

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(psycopg2)

%description -n python3-databases+postgresql
This is a metapackage bringing in postgresql extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+postgresql
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+asyncpg
Summary:        Metapackage for python3-databases: asyncpg extras

BuildArch:      noarch

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(psycopg2)

%description -n python3-databases+asyncpg
This is a metapackage bringing in asyncpg extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+asyncpg
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+aiopg
Summary:        Metapackage for python3-databases: aiopg extras

BuildArch:      noarch

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

BuildArch:      noarch

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(pymysql)

%description -n python3-databases+mysql
This is a metapackage bringing in mysql extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+mysql
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+aiomysql
Summary:        Metapackage for python3-databases: aiomysql extras

BuildArch:      noarch

Requires:       python3-databases = %{version}-%{release}
Recommends:     python3dist(pymysql)

%description -n python3-databases+aiomysql
This is a metapackage bringing in aiomysql extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+aiomysql
%ghost %{python3_sitelib}/*.dist-info


%if 0%{?with_asyncmy}
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
%endif


%package -n python3-databases+sqlite
Summary:        Metapackage for python3-databases: sqlite extras

BuildArch:      noarch

Requires:       python3-databases = %{version}-%{release}

%description -n python3-databases+sqlite
This is a metapackage bringing in sqlite extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+sqlite
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-databases+aiosqlite
Summary:        Metapackage for python3-databases: aiosqlite extras

BuildArch:      noarch

Requires:       python3-databases = %{version}-%{release}

%description -n python3-databases+aiosqlite
This is a metapackage bringing in aiosqlite extras requires for
python3-databases. It makes sure the dependencies are installed.

%files -n python3-databases+aiosqlite
%ghost %{python3_sitelib}/*.dist-info


%package -n     python3-databases
Summary:        %{summary}

BuildArch:      noarch

Obsoletes:      python-databases-doc < 0.5.2-4

%description -n python3-databases %{common_description}


%prep
%autosetup -n databases-%{srcversion} -p1

# The patch for sqlalchemy >=1.4.42 is not backwards-compatible.
sed -r -i 's/(sqlalchemy>=1\.4),/\1\.42,/' setup.py

%if !0%{?with_asyncmy}
sed -r -i \
    -e 's/^([[:blank:]]*)(.*import AsyncMyBackend.*)$/# \1\2\n\1pass/' \
    -e 's/^def test_asyncmy_.*$/@pytest.mark.skip("asyncmy does not support 32-bit")\n&/' \
    tests/test_connection_options.py
%endif


%generate_buildrequires
%{pyproject_buildrequires \
    -x postgresql \
    -x asyncpg \
    -x aiopg \
    -x mysql \
    -x aiomysql \
    %{?with_asyncmy:-x asyncmy} \
    -x sqlite \
    -x aiosqlite}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files databases


%check
%if %{with bootstrap}
rm tests/test_integration.py
%endif

# Since we won’t be able to test all of the backends, we start with an
# import-only “smoke test”
%{pyproject_check_import %{?!with_asyncmy:-e 'databases.backends.asyncmy'}}

# E   ModuleNotFoundError: No module named 'tests'
touch tests/__init__.py

# We can only easily run the tests with SQLite; other databases require a
# properly configured server, which we cannot in general provide as an
# unprivileged user. However, see the MySQL support below.
#
# The following environment variable is a comma-separated list with (optional?)
# whitespace.
export TEST_DATABASE_URLS="sqlite:///testsuite, sqlite+aiosqlite:///testsuite"

%if %{with mysql_tests}
# Based on rubygem-mysql2 packaging; see also python-asyncmy

# Use a randomized port in case the standard mysqld port 3306 is occupied, and
# to account for multiple simultaneous builds on the same host.
# https://src.fedoraproject.org/rpms/rubygem-pg/pull-request/3
MYSQL_PORT="$((13306 + ${RANDOM} % 1000))"
MYSQL_USER="$(whoami)"
MYSQL_DATA_DIR="${PWD}/data"
MYSQL_SOCKET="${PWD}/mysql.sock"
MYSQL_LOG="${PWD}/mysql.log"
MYSQL_PID_FILE="${PWD}/mysql.pid"

mkdir "${MYSQL_DATA_DIR}"
mysql_install_db --datadir="${MYSQL_DATA_DIR}" --log-error="${MYSQL_LOG}"

%{_libexecdir}/mysqld --port="${MYSQL_PORT}" --skip-ssl \
    --datadir="${MYSQL_DATA_DIR}" --log-error="${MYSQL_LOG}" \
    --socket="${MYSQL_SOCKET}" --pid-file="${MYSQL_PID_FILE}" & :

echo "Waiting for server… ${i}" 1>&2
TIMEOUT=30
while ! grep -q 'ready for connections.' "${MYSQL_LOG}"
do
  sleep 1
  TIMEOUT=$((TIMEOUT - 1))
  if [[ "${TIMEOUT}" = '0' ]]
  then
    echo 'Timed out' 1>&2
    exit 1
  fi
done

echo 'Ready' 1>&2
trap "kill $(cat "${MYSQL_PID_FILE}")" INT TERM EXIT

# See https://github.com/brianmario/mysql2/blob/master/.travis_setup.sh
mysql -u "${MYSQL_USER}" -S "${MYSQL_SOCKET}" -P "${MYSQL_PORT}" \
  -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';"
mysql -u 'root' --password='123456' \
  --protocol='TCP' -h 'localhost' -P "${MYSQL_PORT}" \
  -e 'CREATE DATABASE testsuite;'

for url in \
    "mysql://root:123456@localhost:${MYSQL_PORT}/testsuite" \
%if %{with asyncmy}
    "mysql+asyncmy://root:123456@localhost:${MYSQL_PORT}/testsuite" \
%endif
    "mysql+aiomysql://root:123456@localhost:${MYSQL_PORT}/testsuite"
do
  export TEST_DATABASE_URLS="${TEST_DATABASE_URLS}, ${url}"
done
%endif

%pytest --verbose


%files -n python3-databases -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
