%global module_name pgactivity

Name:           pg_activity
Version:        3.6.1
Release:        %autorelease
Summary:        Command line tool for PostgreSQL server activity monitoring

License:        PostgreSQL
URL:            https://github.com/dalibo/pg_activity/
Source0:        https://github.com/dalibo/pg_activity/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for check
BuildRequires:  glibc-langpack-fr
BuildRequires:  glibc-langpack-zh
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-postgresql)
BuildRequires:  python3dist(psycopg)

Requires:       python3dist(psycopg)

%description
Top like application for PostgreSQL server activity monitoring

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

install -Dpm 0644 docs/man/pg_activity.1 %{buildroot}%{_mandir}/man1/pg_activity.1

%check
PY_IGNORE_IMPORTMISMATCH=1 %pytest

%files -n %{name} -f %{pyproject_files}
%license LICENSE.txt
%doc AUTHORS.md README.md
%{_bindir}/pg_activity
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
