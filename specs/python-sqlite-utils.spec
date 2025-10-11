Summary:        Python CLI utility and library for manipulating SQLite databases
Name:           python-sqlite-utils
Version:        3.38
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://pypi.python.org/project/sqlite-utils/
Source:         %{pypi_source sqlite_utils}
Patch:          python-sqlite-utils-3.38-click.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
%global _description \
Python CLI utility and library for manipulating SQLite databases. \
Some features: \
\
- Pipe JSON (or CSV or TSV) directly into a new SQLite database file, \
  automatically creating a table with the appropriate schema \
\
- Run in-memory SQL queries, including joins, directly against data in \
  CSV, TSV or JSON files and view the results \
\
- Configure SQLite full-text search against your database tables and run \
  search queries against them, ordered by relevance \
\
- Run transformations against your tables to make schema changes that \
  SQLite ALTER TABLE does not directly support, such as changing the type of a column \
\
- Extract columns into separate tables to better normalize your existing data \
\
- Install plugins to add custom SQL functions and additional features

%description %{_description}

%package     -n python3-sqlite-utils
Summary:        %{summary}
%description -n python3-sqlite-utils %{_description}

%prep
%autosetup -p1 -n sqlite_utils-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sqlite_utils

%check
%pytest

%files -n python3-sqlite-utils -f %{pyproject_files}
%doc README.md
%{_bindir}/sqlite-utils

%changelog
%autochangelog
