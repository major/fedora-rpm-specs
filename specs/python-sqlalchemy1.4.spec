# Tests crash when being run by pytest-xdist
%bcond_with xdist

%global srcname SQLAlchemy
%global canonicalname %{py_dist_name %{srcname}}

%global python_pkg_extras \
    asyncio \
    mssql_pymssql \
    mssql_pyodbc \
    mysql \
    postgresql \
    postgresql_pg8000 \
    postgresql_asyncpg \
    pymysql \
    aiomysql \
    aiosqlite

Name:           python-sqlalchemy1.4
Version:        1.4.54
# cope with pre-release versions containing tildes
%global srcversion %{lua: srcversion, num = rpm.expand("%{version}"):gsub("~", ""); print(srcversion);}
Release:        %autorelease
Summary:        Modular and flexible ORM library for Python

License:        MIT
URL:            https://www.sqlalchemy.org/
Source0:        %{pypi_source %{canonicalname} %{srcversion}}

# Fix tests on Python 3.14
# https://github.com/sqlalchemy/sqlalchemy/pull/12666
Patch:          0001-Remove-test-warning-in-python-3.13.patch
Patch:          0001-use-asyncio.Runner-for-tests.patch
Patch:          0002-Python-3.14-Skip-broken-test.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  python3-devel >= 3.6
# The dependencies needed for testing don’t get auto-generated.
BuildRequires:  python3dist(pytest)
%if %{with xdist}
BuildRequires:  python3dist(pytest-xdist)
%endif

%description
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

This package contains version 1.4 of SQLAlchemy for software which is not
compatible with SQLAlchemy version 2.

%package -n python3-sqlalchemy1.4
Summary:        %{summary}
Conflicts:      python3-sqlalchemy >= 2
Provides:       python3-sqlalchemy = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-sqlalchemy1.4
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

This package contains version 1.4 of SQLAlchemy for software which is not
compatible with SQLAlchemy version 2.

# Subpackages to ensure dependencies enabling extra functionality
%pyproject_extras_subpkg -n python3-sqlalchemy1.4 %python_pkg_extras

%package doc
Summary:        Documentation for SQLAlchemy 1.4
BuildArch:      noarch

%description doc
Documentation for SQLAlchemy 1.4.


%generate_buildrequires
%pyproject_buildrequires


%prep
%autosetup -n %{canonicalname}-%{srcversion} -p1

%build
export REQUIRE_SQLALCHEMY_CEXT=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{canonicalname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}

install -d %{buildroot}%{_pkgdocdir}
cp -a doc examples %{buildroot}%{_pkgdocdir}/
# remove unnecessary scripts for building documentation
rm -rf %{buildroot}%{_pkgdocdir}/doc/build
find %{buildroot}%{_pkgdocdir} | while read long; do
    short="${long#%{buildroot}}"
    if [ -d "$long" ]; then
        echo "%%doc %%dir $short"
    else
        if [ "$short" != "${short/copyright/}" ]; then
            echo "%%license $short"
        else
            echo "%%doc $short"
        fi
    fi
done > doc-files.txt


%check
# Skip memory profiling, which takes a long time, does not run by default in
# the upstream tox config, and makes little sense to run downstream.
k="${k-}${k+ and }not aaa_profiling"

%pytest test -k "${k-}" \
%if %{with xdist}
--numprocesses=auto
%endif


%files doc -f doc-files.txt

%files -n python3-sqlalchemy1.4 -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
