# Tests crash when being run by pytest-xdist
%bcond_with xdist

%global srcname SQLAlchemy

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

Name:           python-sqlalchemy
Version:        1.4.51
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
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-greenlet >= 1.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%if %{with xdist}
BuildRequires:  python3-pytest-xdist
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

%description -n python3-sqlalchemy
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

# Subpackages to ensure dependencies enabling extra functionality
%{?python_extras_subpkg:%python_extras_subpkg -n python3-sqlalchemy -i %{python3_sitearch}/*.egg-info %python_pkg_extras}

%package doc
Summary:        Documentation for SQLAlchemy
BuildArch:      noarch

%description doc
Documentation for SQLAlchemy.


%prep
%autosetup -n %{srcname}-%{srcversion} -p1

%build
%py3_build

%install
%py3_install

install -d %{buildroot}%{_pkgdocdir}
cp -a doc %{buildroot}%{_pkgdocdir}/
# remove unnecessary scripts for building documentation
rm -rf %{buildroot}%{_pkgdocdir}/doc/build
find %{buildroot}%{_pkgdocdir}/doc | while read long; do
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
%if %{with xdist}
--numprocesses=auto
%endif


%files doc -f doc-files.txt
%doc examples

%files -n python3-sqlalchemy
%license LICENSE
%doc README.rst
%{python3_sitearch}/SQLAlchemy-*.egg-info/
%{python3_sitearch}/sqlalchemy/

%changelog
%autochangelog
