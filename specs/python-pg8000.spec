%global srcname pg8000

Name:           python-%{srcname}
Version:        1.31.5
Release:        %autorelease
Summary:        Pure Python PostgreSQL Driver

License:        BSD-3-Clause
URL:            https://codeberg.org/tlocke/pg8000
# Pypi source is used because with versioningit the usage of tarballs would
# be complicated: https://codeberg.org/tlocke/pg8000/issues/152
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pg8000 is a pure-Python PostgreSQL driver that complies with DB-API 2.0.
The driver communicates with the database using the PostgreSQL Backend and
Frontend Protocol.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pure Python3 PostgreSQL Driver
BuildRequires:  python%{python3_pkgversion}-devel

%{?fedora:Suggests:       python3-sqlalchemy}
%{?fedora:Suggests:       postgresql}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
pg8000 is a pure Python3 PostgreSQL driver that complies with DB-API 2.0.
The driver communicates with the database using the PostgreSQL Backend /
Frontend Protocol.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Test requires a running PostgreSQL instance
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
