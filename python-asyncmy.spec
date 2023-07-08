# Tests require interacting with a temporary MySQL database. We are able to do
# this, but leave a build conditional to fall back to a “smoke test” in case it
# breaks.
%bcond tests 1

Name:           python-asyncmy
Summary:        A fast asyncio MySQL/MariaDB driver
Version:        0.2.8
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/long2ice/asyncmy
# The GitHub source includes tests and examples; the PyPI source lacks them.
Source:         %{url}/archive/v%{version}/asyncmy-%{version}.tar.gz

# Doc/license files installed directly in site-packages
# https://github.com/long2ice/asyncmy/issues/33
Patch:          0001-Do-not-install-text-files-in-site-packages.patch

# Test failures and errors on 32-bit platforms
# https://github.com/long2ice/asyncmy/issues/34
# https://bugzilla.redhat.com/show_bug.cgi?id=2060899
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  mariadb-server

# pyproject.toml: [tool.poetry.dev-dependencies]
# aiomysql = "*" ← benchmarks only
# black = "*" ← linter/formatter
# cryptography = "*"
BuildRequires:  python3dist(cryptography)
# cython = "*" ← already in [build-system] requires
# flake8 = "*" ← linter
# isort = "*" ← linter/formatter
# mypy = "*" ← linter/typechecker
# mysqlclient = "*" ← benchmarks only
# pymysql = "0.8.1" ← benchmarks only
# pytest = "*"
BuildRequires:  python3dist(pytest)
# rich = "*" ← benchmarks only
# pyproject-flake8 = "*" ← linter/formatter
# pytest-asyncio = "*"
BuildRequires:  python3dist(pytest-asyncio)
# pytest-mock = "*"
BuildRequires:  python3dist(pytest-mock)
# pytest-xdist = "*"
BuildRequires:  python3dist(pytest-xdist)
# uvloop = { version = "*", markers = "…" } ← benchmarks only
%endif

%global common_description %{expand:
asyncmy is a fast asyncio MySQL/MariaDB driver, which reuses most of pymysql
and aiomysql but rewrites the core protocol with Cython to speed it up.}

%description %{common_description}


%package -n     python3-asyncmy
Summary:        %{summary}

%description -n python3-asyncmy %{common_description}


%prep
%autosetup -n asyncmy-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files asyncmy

# Do not distribute Cython-generated C source files; these are not useful
find '%{buildroot}%{python3_sitearch}/asyncmy' \
    -type f -name '*.c' -print -delete
sed -r -i '/\.c$/d' '%{pyproject_files}'


%check
%if %{with tests}
# Based on rubygem-mysql2 packaging:

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

sed -r -i "s/\b3306\b/${MYSQL_PORT}/" conftest.py
# Make sure we do not import the “un-built” package
rm -rf asyncmy

%pytest

%else
%pyproject_check_import
%endif


%files -n python3-asyncmy -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
