%{!?postgresql_default:%global postgresql_default 0}

%global pgversion       16
%global extension       pg_cron

Name:           postgresql%{pgversion}-%{extension}
Version:        1.6.7
Release:        %autorelease
Summary:        A simple cron-based job scheduler for PostgreSQL

License:        PostgreSQL
URL:            https://github.com/citusdata/%{extension}
Source0:        https://github.com/citusdata/%{extension}/archive/refs/tags/v%{version}.tar.gz

# drop i686 support (https://fedoraproject.org/wiki/Changes/Noi686Repositories)
ExcludeArch:    %{ix86}

%if %?postgresql_default
%global pkgname %{extension}
%package -n %{pkgname}
Summary:        A simple cron-based job scheduler for PostgreSQL
%else
%global pkgname %name
%endif

BuildRequires:  make gcc redhat-rpm-config
BuildRequires:  postgresql%{pgversion}-server-devel
Requires:       postgresql%{pgversion}-server

%global precise_version %{?epoch:%epoch:}%version-%release
%if %?postgresql_default
Provides: %name = %precise_version
Provides: postgresql-%{extension} = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{pkgname} = %precise_version
Provides: %{extension}-any
Conflicts: %{extension}-any

%description
pg_cron is a simple cron-based job scheduler for PostgreSQL (10 or higher)
that runs inside the database as an extension.
The extension creates a background worker that tracks jobs in the `cron.job`
table. Based on your configurations, to execute a job, the extension
establishes a Postgres connection or spawns a database worker.

%if %?postgresql_default
%description -n %{pkgname}
pg_cron is a simple cron-based job scheduler for PostgreSQL (10 or higher)
that runs inside the database as an extension.
The extension creates a background worker that tracks jobs in the `cron.job`
table. Based on your configurations, to execute a job, the extension
establishes a Postgres connection or spawns a database worker.
%endif

%prep
%autosetup -n %extension-%version


%build
%make_build


%install
%make_install

# Running tests is impossible without compiling own postgres
# (hard-coded location for extensions). Omitting check phase
# Integration tests are in gating.


%files -n %{pkgname}
%{_libdir}/pgsql/%{extension}.so
%{_datadir}/pgsql/extension/%{extension}.control
%{_datadir}/pgsql/extension/%{extension}--1*.sql
%license LICENSE
%doc CHANGELOG.md README.md 


%changelog
%autochangelog
