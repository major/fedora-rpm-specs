# Mypy plugin is deprecated in 2.0. mypy is not in RHEL.
# Some mypy plugin tests fail with mypy 1.14.1:
# https://github.com/sqlalchemy/sqlalchemy/issues/12287
%bcond mypy 0

# The asyncmy Python package isn’t available in x86 (32bit)
%ifnarch %ix86
%bcond asyncmy %{undefined rhel}
%else
%bcond asyncmy 0
%endif

# Whether to run tests in parallel
%bcond xdist %{undefined rhel}

# Whether certain type hinting tests should be skipped, to work around changes in typing_extensions.
# Remove after things have settled, see here for details:
# https://bugzilla.redhat.com/show_bug.cgi?id=2350336
%bcond typing_tests_quirk 1

%global srcname SQLAlchemy
%global canonicalname %{py_dist_name %{srcname}}

%if %{undefined rhel}
# postgresql_pg8000, postgresql_asyncpg extras removed to unblock the Python 3.14 rebuild
# TODO add them back once ready
%if v"0%{?python3_version}" >= v"3.14"
%bcond py314quirk 1
%else
%bcond py314quirk 0
%endif

%global python_pkg_extras \
    asyncio \
    mssql_pymssql \
    mssql_pyodbc \
    mysql \
    mysql_connector \
    %{?with_mypy:mypy} \
    postgresql \
    %{!?with_py314quirk:postgresql_pg8000} \
    %{!?with_py314quirk:postgresql_asyncpg} \
    pymysql \
    aiomysql \
    aioodbc \
    aiosqlite \
    %{?with_asyncmy:asyncmy}
%endif

Name:           python-%{canonicalname}
Version:        2.0.39
# cope with pre-release versions containing tildes
%global srcversion %{lua: srcversion, num = rpm.expand("%{version}"):gsub("~", ""); print(srcversion);}
Release:        %autorelease
Summary:        Modular and flexible ORM library for Python

License:        MIT
URL:            https://www.sqlalchemy.org/
Source0:        %{pypi_source %{canonicalname} %{srcversion}}

# Fix test suite on Python 3.14
# https://bugzilla.redhat.com/show_bug.cgi?id=2350336
# https://gerrit.sqlalchemy.org/c/sqlalchemy/sqlalchemy/+/5739
Patch0:         https://gerrit.sqlalchemy.org/changes/sqlalchemy%2Fsqlalchemy~5739/revisions/12/patch?zip#/eb84fed.diff.zip

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  patch
BuildRequires:  python3-devel >= 3.7
# The dependencies needed for testing don’t get auto-generated.
BuildRequires:  python3dist(pytest)
%if %{with xdist}
BuildRequires:  python3dist(pytest-xdist)
%endif
BuildRequires:  unzip

%description
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

%package -n python3-sqlalchemy
Summary:        %{summary}
%if %{without asyncmy}
Obsoletes:      python3-sqlalchemy+asyncmy < %{version}-%{release}
%endif

%description -n python3-sqlalchemy
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually

as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

%if %{undefined rhel}
# Subpackages to ensure dependencies enabling extra functionality
%pyproject_extras_subpkg -n python3-sqlalchemy %python_pkg_extras
%endif

%package doc
Summary:        Documentation for SQLAlchemy
BuildArch:      noarch

%description doc
Documentation for SQLAlchemy.


%generate_buildrequires
%pyproject_buildrequires %{!?rhel:-x %{gsub %{quote:%python_pkg_extras} %%s+ ,}}


%prep
%autosetup -N -n %{canonicalname}-%{version}
# For some reason, setup.cfg in git and the tarball differ in whitespace, so
# ignore it when applying the patch.
unzip -p %{PATCH0} | patch --ignore-whitespace -p1 -b -z .py314

%build
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
%pytest test \
  -k '. \
%if %{without mypy}
  and not Mypy \
%endif
%if %{with typing_tests_quirk}
  and not test_unions_are_the_same \
%endif
  ' \
%if %{with xdist}
  --numprocesses=auto
%endif


%files doc -f doc-files.txt

%files -n python3-sqlalchemy -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
