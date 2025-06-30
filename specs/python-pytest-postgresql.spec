%global pypi_name pytest-postgresql
%global name_with_underscore pytest_postgresql

Name:           python-%{pypi_name}
Version:        7.0.2
Release:        %autorelease
Summary:        A pytest plugin for PostgreSQL database integration

License:        LGPL-3.0-or-later
URL:            https://github.com/ClearcodeHQ/pytest-postgresql
Source0:        https://github.com/ClearcodeHQ/pytest-postgresql/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for check
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-de
BuildRequires:  libpq-devel
BuildRequires:  python3dist(psycopg)
BuildRequires:  postgresql-server

%description
This is a pytest plugin, that enables you to test your code that relies on a
running PostgreSQL Database. It allows you to specify fixtures for PostgreSQL
process and client.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This is a pytest plugin, that enables you to test your code that relies on a
running PostgreSQL Database. It allows you to specify fixtures for PostgreSQL
process and client.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name_with_underscore}

%check
# Since 5.0.0 there are issues during the check phase as pytest-postgresql is
# loaded twice and pytest errors as same params are loaded twice.
#
# To fix:
#   - remove unkown params from pyproject.toml
#   - remove test_postgres_options_plugin.py to avoid failing tests
#   - "-p no:postgresql" to avoid loading the plugin twice
sed -i '/^addopts/d' pyproject.toml
rm tests/test_postgres_options_plugin.py
%pytest -p no:postgresql --postgresql-exec="/usr/bin/pg_ctl" -k "not docker"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING COPYING.lesser
%doc AUTHORS.rst CHANGES.rst README.rst

%changelog
%autochangelog
