# Mypy plugin is deprecated in 2.0. mypy is not in RHEL.
%bcond mypy %{undefined rhel}

# The asyncmy Python package isn’t available in x86 (32bit)
%ifnarch %ix86
%bcond asyncmy %{undefined rhel}
%else
%bcond asyncmy 0
%endif

# Tests crash when being run by pytest-xdist
%bcond xdist 0

%global srcname SQLAlchemy
%global canonicalname %{py_dist_name %{srcname}}

%if %{undefined rhel}
%global python_pkg_extras \
    asyncio \
    mssql_pymssql \
    mssql_pyodbc \
    mysql \
    mysql_connector \
    %{?with_mypy:mypy} \
    postgresql \
    postgresql_pg8000 \
    postgresql_asyncpg \
    pymysql \
    aiomysql \
    aioodbc \
    aiosqlite \
    %{?with_asyncmy:asyncmy}
%endif

Name:           python-%{canonicalname}
Version:        2.0.26
# cope with pre-release versions containing tildes
%global srcversion %{lua: srcversion, num = rpm.expand("%{version}"):gsub("~", ""); print(srcversion);}
Release:        %autorelease
Summary:        Modular and flexible ORM library for Python

License:        MIT
URL:            https://www.sqlalchemy.org/
Source0:        %{pypi_source %{srcname} %{srcversion}}

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  python3-devel >= 3.7
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
%autosetup -n %{srcname}-%{version} -p1

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
%if %{without mypy}
  -k 'not Mypy' \
%endif
%if %{with xdist}
--numprocesses=auto
%endif


%files doc -f doc-files.txt

%files -n python3-sqlalchemy -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
