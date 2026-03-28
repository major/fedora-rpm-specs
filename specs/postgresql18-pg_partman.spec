%{!?postgresql_default:%global postgresql_default 1}

%global pgversion 18
%global extension pg_partman

Name: postgresql%{pgversion}-%{extension}
Version: 5.4.3
Release: %autorelease

Summary: PostgresSQL Partition Manager
License: PostgreSQL

URL: https://github.com/pgpartman/%{extension}
Source0: https://github.com/pgpartman/%{extension}/archive/refs/tags/v%{version}.tar.gz

# drop i686 support (https://fedoraproject.org/wiki/Changes/Noi686Repositories)
ExcludeArch: %{ix86}
	
%if %?postgresql_default
%global pkgname %{extension}
%package -n %{pkgname}
Summary: PostgresSQL Partition Manager
%else
%global pkgname %name
%endif

# Patches the generic python shebangs to python3
# shebangs since the fedora packaging guidelines
# forbids generic python shebangs
Patch0: python_shebangs.patch

BuildRequires: postgresql%{pgversion}-server-devel gcc make

Requires: postgresql%{pgversion}-server
	
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
%{extension} is an extension to create and manage both time-based
and number-based table partition sets. As of version 5.0.1, only built-in,
declarative partitioning is supported and the older trigger-based methods
have been deprecated.

The declarative partitioning built into PostgreSQL provides the commands
to create a partitioned table and its children. pg_partman uses the built-in
declarative features that PostgreSQL provides and builds upon those with
additional features and enhancements to make managing partitions easier.
One key way that pg_partman extends partitioning in Postgres is by providing
a means to automate the child table maintenance over time
(Ex. adding new children, dropping old ones based on a retention policy).
pg_partman also has features to turn an existing table into a partitioned
table or vice versa.

A background worker (BGW) process is included to automatically run partition
maintenance without the need of an external scheduler (cron, etc)
in most cases.
	
%if %?postgresql_default
%description -n %{pkgname}
%{extension} is an extension to create and manage both time-based
and number-based table partition sets. As of version 5.0.1, only built-in,
declarative partitioning is supported and the older trigger-based methods
have been deprecated.

The declarative partitioning built into PostgreSQL provides the commands
to create a partitioned table and its children. pg_partman uses the built-in
declarative features that PostgreSQL provides and builds upon those with
additional features and enhancements to make managing partitions easier.
One key way that pg_partman extends partitioning in Postgres is by providing
a means to automate the child table maintenance over time
(Ex. adding new children, dropping old ones based on a retention policy).
pg_partman also has features to turn an existing table into a partitioned
table or vice versa.

A background worker (BGW) process is included to automatically run partition
maintenance without the need of an external scheduler (cron, etc)
in most cases.
%endif

%package -n %{pkgname}-doc
Summary: %{name} documentation
BuildArch: noarch
%if %?postgresql_default
Provides: %{name}-doc = %precise_version
Provides: postgresql-%{extension}-doc = %precise_version
%endif
Provides: %{extension}-doc-any
Conflicts: %{extension}-doc-any

Requires: %{pkgname} = %{version}-%{release}

%description -n %{pkgname}-doc
Documentation detailing the usage, migration and upgrading of the 
%{name} package

%prep
%setup -q -n %{extension}-%{version}
%patch -P0 -p1

%build
%make_build

%install
%make_install

# move the older sql patch files to a specific directory
# to avoid cluttering the extension dir of pgsql
mkdir -p %{buildroot}%{_datadir}/%{extension}
mv %{buildroot}%{_datadir}/pgsql/extension/%{extension}--*--*.sql %{buildroot}%{_datadir}/%{extension}

mkdir -p %{buildroot}%{_docdir}/postgresql/%{extension}
mv %{buildroot}%{_docdir}/pgsql/extension/* %{buildroot}%{_docdir}/postgresql/%{extension}

# The %%check section is not present since the extension
# would need to be installed in the default postgresql
# extension location and this is not feasible during the
# build without too much effort

%files -n %{pkgname}
%dir %{_datadir}/%{extension}/
%{_bindir}/check_unique_constraint.py
%{_bindir}/dump_partition.py
%{_bindir}/vacuum_maintenance.py
%{_libdir}/pgsql/%{extension}_bgw.so
%{_datadir}/pgsql/extension/%{extension}--%{version}.sql
%{_datadir}/pgsql/extension/%{extension}.control
%{_datadir}/%{extension}/%{extension}--*--*.sql
%license LICENSE.txt
%doc README.md 

%files -n %{pkgname}-doc
%doc CHANGELOG.md 
%dir %{_docdir}/postgresql/%{extension}/
%doc %{_docdir}/postgresql/%{extension}/fix_missing_procedures.md
%doc %{_docdir}/postgresql/%{extension}/migrate_to_declarative.md
%doc %{_docdir}/postgresql/%{extension}/migrate_to_partman.md
%doc %{_docdir}/postgresql/%{extension}/pg_partman.md
%doc %{_docdir}/postgresql/%{extension}/pg_partman_5.0.1_upgrade.md
%doc %{_docdir}/postgresql/%{extension}/pg_partman_howto.md

%changelog
%autochangelog
