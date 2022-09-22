Name:    postgresqltuner
Version: 1.0.1
Release: %autorelease
Summary: Simple script to analyze PostgreSQL database configuration and tuning

License: GPLv3
URL:     https://github.com/jfcoz/postgresqltuner/
Source0: https://github.com/jfcoz/postgresqltuner/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch


Requires: perl(DBI)
Requires: perl(DBD::Pg)
Requires: perl(Getopt::Long)
Requires: perl(Term::ANSIColor)

BuildRequires: postgresql-test-rpm-macros
BuildRequires: perl(DBI)
BuildRequires: perl(DBD::Pg)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Term::ANSIColor)

%description
postgresqltuner is a simple script to analyze your PostgreSQL database. It is 
inspired by mysqltuner.pl

%prep
%autosetup

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a postgresqltuner.pl %{buildroot}%{_bindir}/postgresqltuner

%check
%postgresql_tests_run
%{buildroot}%{_bindir}/postgresqltuner --host=$PGHOST --port=$PGPORT --database=mockbuild --user=mockbuild --password=mockbuild

%files
%{_bindir}/postgresqltuner

%doc README.md README.fr.md
%license LICENSE.txt

%changelog
%autochangelog
