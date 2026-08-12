# DuckDB is not yet packaged
%bcond_with perl_DBIx_QuickDB_duckdb

Name:           perl-DBIx-QuickDB
Version:        0.000064
Release:        1%{?dist}
Summary:        Quickly start a database server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBIx-QuickDB
Source0:        https://www.cpan.org/authors/id/E/EX/EXODIST/DBIx-QuickDB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# DBIx::QuickDB::Driver::PostgreSQL defaults to en_US.UTF-8 locale
BuildRequires:  glibc-langpack-en
BuildRequires:  perl(Capture::Tiny) >= 0.20
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
# File::Copy::Recursive or coreutils or rsync; prefer coreutils
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Importer) >= 0.024
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Pluggable) >= 2.7
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::API) >= 1.302120
BuildRequires:  perl(Time::HiRes)
# Optional run-time:
# mysql-server conflicts with mariadb-server
BuildRequires:  mariadb-server-any
%if %{with perl_DBIx_QuickDB_duckdb}
BuildRequires:  perl(DBD::DuckDB) >= 0.16
%endif
# DBD::mysql is useless without mysql-server-any
BuildRequires:  perl(DBD::MariaDB)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  postgresql-server
BuildRequires:  sqlite
# Tests:
BuildRequires:  bash
BuildRequires:  perl(base)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::Tools::Basic)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Exports)
BuildRequires:  perl(Test2::Tools::Subtest)
BuildRequires:  perl(Test2::Util::Table)
BuildRequires:  perl(Test2::V0) >= 0.000097
BuildRequires:  perl(Test::More) >= 1.302120
# Optional tests:
BuildRequires:  perl(IO::Socket::UNIX)
# File::Copy::Recursive or coreutils or rsync; prefer coreutils
Requires:       coreutils
Requires:       perl(DBI)
Requires:       perl(Importer) >= 0.024
Requires:       perl(Module::Pluggable) >= 2.7
Requires:       perl(Test2::API) >= 1.302120

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Capture::Tiny|Importer|Module::Pluggable|Test2::API)\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(main::HBase|QDB::FakeDriver|QDB::Installs
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Fake::Export::Lib|QDB::DriverBody|QDB::FakeDriver|QDB::Installs|QDB::Installs::ResourceUnavailable|Test::Pool|XXX|YYY)\\)

%description
This library makes it easy to spin up a temporary database server for any
supported driver. PostgreSQL, MySQL and SQLite are the initially
supported drivers.

%if %{with perl_DBIx_QuickDB_duckdb}
%package Driver-DuckDB
Summary:        DuckDB driver for DBIx::QuickDB
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       /usr/bin/duckdb
Requires:       perl(Capture::Tiny) >= 0.20
Requires:       perl(DBD::MariaDB)
Requires:       perl(DBD::mysql)

%description Driver-DuckDB
This is DuckDB support for DBIx::QuickDB.
%endif

%package Driver-MySQL
Summary:        MySQL drivers for DBIx::QuickDB
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# Keep all the MySQL drivers in a single package as they require each other.
# mysql-server conflicts with mariadb-server
Requires:       (mariadb-server-any or mysql-server-any)
Requires:       perl(Capture::Tiny) >= 0.20
Requires:       perl(DBD::MariaDB)
Requires:       perl(DBD::mysql)

%description Driver-MySQL
This is MySQL support for DBIx::QuickDB.

%package Driver-PostgreSQL
Summary:        PostgreSQL driver for DBIx::QuickDB
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# DBIx::QuickDB::Driver::PostgreSQL defaults to en_US.UTF-8 locale
Requires:       glibc-langpack-en
Requires:       perl(DBD::Pg)
Requires:       postgresql-server

%description Driver-PostgreSQL
This is PostgreSQL support for DBIx::QuickDB.

%package Driver-SQLite
Summary:        SQLite driver for DBIx::QuickDB
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(DBD::SQLite)
Requires:       sqlite

%description Driver-SQLite
This is SQLite support for DBIx::QuickDB.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Capture::Tiny) >= 0.20
Requires:       perl(File::Copy::Recursive)
Requires:       perl(IO::Socket::UNIX)
Requires:       perl(Test2::API) >= 1.302120
# Optional run-time:
Requires:       %{name}-Driver-MySQL = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Driver-PostgreSQL = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Driver-SQLite = %{?epoch:%{epoch}:}%{version}-%{release}
# Pin to this implementation to have reproducible tests
Requires:       mariadb-server

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n DBIx-QuickDB-%{version}
%if !%{with perl_DBIx_QuickDB_duckdb}
for F in lib/DBIx/QuickDB/Driver/DuckDB.pm \
        t/Drivers/DuckDB.t t/Pool/duckdb.t t/QuickDB/DuckDB.t t/schema/duckdb.sql; do
    rm -- "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in $(find t -type f -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset DB_VERBOSE QDB_DIAG_FIXTURE_MODE QDB_INSTALL_EXTERNAL_TRACE QDB_INSTALL_JOBS \
    QDB_MARIADB_IGNORE_BROKEN HOME QDB_MARIADB_DBD QDB_MARIADB_SSL_FIPS \
    QDB_START_TIMEOUT QDB_STOP_GRACE QDB_TMPDIR
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DB_VERBOSE QDB_DIAG_FIXTURE_MODE QDB_INSTALL_EXTERNAL_TRACE QDB_INSTALL_JOBS \
    QDB_MARIADB_IGNORE_BROKEN HOME QDB_MARIADB_DBD QDB_MARIADB_SSL_FIPS \
    QDB_START_TIMEOUT QDB_STOP_GRACE QDB_TMPDIR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README.md is reduntant
%doc Changes README RUN_COMMAND_STDERR_LEAK.md
%dir %{perl_vendorlib}/DBIx
%dir %{perl_vendorlib}/DBIx/QuickDB
%{perl_vendorlib}/DBIx/QuickDB.pm
%dir %{perl_vendorlib}/DBIx/QuickDB/Driver
%{perl_vendorlib}/DBIx/QuickDB/Driver.pm
%{perl_vendorlib}/DBIx/QuickDB/Pool.pm
%{perl_vendorlib}/DBIx/QuickDB/Util
%{perl_vendorlib}/DBIx/QuickDB/Util.pm
%{perl_vendorlib}/DBIx/QuickDB/Watcher.pm
%dir %{perl_vendorlib}/Test2
%dir %{perl_vendorlib}/Test2/Tools
%{perl_vendorlib}/Test2/Tools/QuickDB.pm
%{_mandir}/man3/DBIx::QuickDB.*
%{_mandir}/man3/DBIx::QuickDB::Driver.*
%{_mandir}/man3/DBIx::QuickDB::Pool.*
%{_mandir}/man3/DBIx::QuickDB::Util::*
%{_mandir}/man3/DBIx::QuickDB::Watcher.*
%{_mandir}/man3/Test2::Tools::QuickDB.*

%if %{with perl_DBIx_QuickDB_duckdb}
%files Driver-DuckDB
%{perl_vendorlib}/DBIx/QuickDB/Driver/DuckDB.pm
%{_mandir}/man3/DBIx::QuickDB::Driver::DuckDB.*
%endif

%files Driver-MySQL
%{perl_vendorlib}/DBIx/QuickDB/Driver/MariaDB.pm
%{perl_vendorlib}/DBIx/QuickDB/Driver/MySQL.pm
%{perl_vendorlib}/DBIx/QuickDB/Driver/MySQLCom.pm
%{perl_vendorlib}/DBIx/QuickDB/Driver/Percona.pm
%{_mandir}/man3/DBIx::QuickDB::Driver::MariaDB.*
%{_mandir}/man3/DBIx::QuickDB::Driver::MySQL.*
%{_mandir}/man3/DBIx::QuickDB::Driver::MySQLCom.*
%{_mandir}/man3/DBIx::QuickDB::Driver::Percona.*

%files Driver-PostgreSQL
%{perl_vendorlib}/DBIx/QuickDB/Driver/PostgreSQL.pm
%{_mandir}/man3/DBIx::QuickDB::Driver::PostgreSQL.*

%files Driver-SQLite
%{perl_vendorlib}/DBIx/QuickDB/Driver/SQLite.pm
%{_mandir}/man3/DBIx::QuickDB::Driver::SQLite.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Aug 10 2026 Petr Pisar <ppisar@redhat.com> - 0.000064-1
- 0.000064 bump

* Fri Aug 07 2026 Petr Pisar <ppisar@redhat.com> - 0.000062-1
- 0.000062 bump

* Tue Aug 04 2026 Petr Pisar <ppisar@redhat.com> - 0.000061-2
- Increase timeout for TMT tests

* Tue Aug 04 2026 Petr Pisar <ppisar@redhat.com> - 0.000061-1
- 0.000061 bump

* Wed Apr 08 2026 Petr Pisar <ppisar@redhat.com> - 0.000054-1
- First packaged version
