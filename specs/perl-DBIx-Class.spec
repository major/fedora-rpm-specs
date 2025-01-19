Name:           perl-DBIx-Class
Summary:        Extensible and flexible object <-> relational mapper
Version:        0.082843
Release:        9%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-%{version}.tar.gz
URL:            https://metacpan.org/release/DBIx-Class
# Do not use /usr/bin/env in shell bangs, upstream does not agree
# (see Changes)
Patch0:         DBIx-Class-0.082840-Do-not-use-usr-bin-env-in-shell-bangs.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Class::C3::Componentised)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(constant)
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.2
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::Const::GetInfoReturn)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(DBIx::ContextualFetch)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.081
BuildRequires:  perl(Getopt::Long::Descriptive::Usage)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON::Any) >= 1.23
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Base36) >= 0.07
BuildRequires:  perl(Math::BigInt) >= 1.80
BuildRequires:  perl(Method::Generate::Accessor)
BuildRequires:  perl(Method::Generate::Constructor)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Object)
BuildRequires:  perl(Moose) >= 0.98
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types) >= 0.21
BuildRequires:  perl(MooseX::Types::JSON) >= 0.02
BuildRequires:  perl(MooseX::Types::LoadableClass) > 0.011
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class) >= 0.05
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(SQL::Abstract::Classic) >= 1.91
BuildRequires:  perl(SQL::Abstract::Tree)
BuildRequires:  perl(SQL::Abstract::Util)
BuildRequires:  perl(SQL::Translator::Diff)
BuildRequires:  perl(SQL::Translator::Schema::Constants)
BuildRequires:  perl(SQL::Translator::Utils)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Defer)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
# Tests only
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Class::DBI::Column)
BuildRequires:  perl(Class::DBI::Plugin::DeepAbstractSearch)
BuildRequires:  perl(Class::Unload)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::GUID)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::Pg)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
# Optional for TEST_VERBOSE: BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON)
#BuildRequires:  perl(JSON::DWIW)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(SQL::Abstract::Test)
BuildRequires:  perl(SQL::Translator) >= 0.11018
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::CSV) >= 1.16
BuildRequires:  perl(threads)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Piece::MySQL)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML)
Requires:       perl(B::Deparse)
Requires:       perl(Config::Any)
Requires:       perl(DateTime::Format::Strptime) >= 1.2
Requires:       perl(DBI::Const::GetInfoReturn)
Requires:       perl(DBI::Const::GetInfoType)
Requires:       perl(Digest::MD5)
Requires:       perl(File::Spec)
Requires:       perl(Getopt::Long::Descriptive) >= 0.081
Requires:       perl(JSON::Any) >= 1.23
Requires:       perl(Math::Base36) >= 0.07
Requires:       perl(Math::BigInt) >= 1.80
Requires:       perl(Module::Find)
Requires:       perl(Moose) >= 0.98
Requires:       perl(MooseX::Types) >= 0.21
Requires:       perl(MooseX::Types::JSON) >= 0.02
Requires:       perl(MooseX::Types::LoadableClass) > 0.011
Requires:       perl(MooseX::Types::Path::Class) >= 0.05
Requires:       perl(POSIX)
Requires:       perl(SQL::Translator::Diff)
Requires:       perl(Sub::Quote)
Requires:       perl(Text::Balanced)
# hidden from PAUSE
Provides:       perl(DBIx::Class::Admin::Descriptive) = %{version}
Provides:       perl(DBIx::Class::Admin::Types) = %{version}
Provides:       perl(DBIx::Class::Admin::Usage) = %{version}
Provides:       perl(DBIx::Class::Carp) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AbstractSearch) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AccessorMapping) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AttributeAPI) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AutoUpdate) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnCase) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnGroups) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnGroups::GrouperShim) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnsAsHash) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Constraints) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Constructor) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Copy) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::DestroyWarning) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::GetSet) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ImaDBI) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Iterator::ResultSet) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::LazyLoading) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::LiveObjectIndex) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::NoObjectIndex) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Pager) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ReadOnly) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Relationship) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Relationships) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Retrieve) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Stringify) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::TempColumns) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Triggers) = %{version}
Provides:       perl(DBIx::Class::ClassResolver::PassThrough) = %{version}
Provides:       perl(DBIx::Class::Componentised) = %{version}
Provides:       perl(DBIx::Class::_ENV_) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::DB2) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::MSSQL) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::MySQL) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::Oracle) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::Pg) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::SQLite) = %{version}
Provides:       perl(DBIx::Class::Relationship::Accessor) = %{version}
Provides:       perl(DBIx::Class::Relationship::BelongsTo) = %{version}
Provides:       perl(DBIx::Class::Relationship::CascadeActions) = %{version}
Provides:       perl(DBIx::Class::Relationship::HasMany) = %{version}
Provides:       perl(DBIx::Class::Relationship::HasOne) = %{version}
Provides:       perl(DBIx::Class::Relationship::Helpers) = %{version}
Provides:       perl(DBIx::Class::Relationship::ManyToMany) = %{version}
Provides:       perl(DBIx::Class::Relationship::ProxyMethods) = %{version}
Provides:       perl(DBIx::Class::ResultSetProxy) = %{version}
Provides:       perl(DBIx::Class::ResultSourceProxy) = %{version}
Provides:       perl(DBIx::Class::ResultSource::RowParser::Util) = %{version}
Provides:       perl(DBIx::Class::ResultSource::RowParser) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::MSSQL) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::MySQL) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::OracleJoins) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::Oracle) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::SQLite) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::ACCESS) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::MSSQL) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::MySQL) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::Oracle) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::SQLite) = %{version}
Provides:       perl(DBIx::Class::Storage::BlockRunner) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ADO::CursorUtils) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ADO::Microsoft_SQL_Server::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ADO::MS_Jet::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBIHacks) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Informix::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::InterBase::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::MSSQL::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ODBC::ACCESS::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Replicated::Types) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Sybase::ASE::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Sybase::Microsoft_SQL_Server::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::NESTED_ROLLBACK_EXCEPTION) = %{version}
Provides:       perl(DBIx::Class::_Util) = %{version}
Provides:       perl(DBIx::Class::_Util::ScopeGuard) = %{version}
Provides:       perl(DBIx::Class::VersionCompat) = %{version}
Provides:       perl(DBIx::Class::Version::TableCompat) = %{version}
Provides:       perl(DBIx::Class::Version::Table) = %{version}
Provides:       perl(DBIx::Class::Version) = %{version}
Provides:       perl(DBIx::ContextualFetch::st) = %{version}

%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Getopt::Long::Descriptive\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(JSON::Any\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types::JSON\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types::LoadableClass\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types::Path::Class\\)$


%description
This is an SQL to OO mapper with an object API inspired by Class::DBI
(and a compatibility layer as a springboard for porting) and a
result-set API that allows abstract encapsulation of database
operations. It aims to make representing queries in your code as perlish
as possible while still providing access to as many of the
capabilities of the database as possible, including retrieving related
records from multiple tables in a single query, JOIN, LEFT JOIN, COUNT,
DISTINCT, GROUP BY and HAVING support.

%prep
%setup -q -n DBIx-Class-%{version}
%patch -P0 -p1
chmod -c +x script/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# note this test suite is noisy!
export DBICTEST_THREAD_STRESS=1
export DBICTEST_FORK_STRESS=1
export DBICTEST_STORAGE_STRESS=1
export DATA_DUMPER_TEST=1
make test

%files
%license LICENSE
%doc AUTHORS Changes README examples/ t/
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man[13]/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.082843-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.082843-2
- Perl 5.36 rebuild

* Tue May 17 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.082843-1
- 0.082843 bump

* Wed Mar 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.082842-9
- Fix the test failure with SQLite 3.38.0 (bz#2069128)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.082842-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.082842-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.082842-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.082842-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.082842-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.082842-3
- Perl 5.32 rebuild

* Thu Jun 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.082842-2
- Remove dbic_pretty.t, it was removed from distribution

* Wed Jun 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.082842-1
- 0.082842 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.082841-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.082841-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.082841-8
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.082841-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.082841-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.082841-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.082841-4
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.082841-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.082841-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.082841-1
- 0.082841 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.082840-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.082840-8
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Petr Pisar <ppisar@redhat.com> - 0.082840-7
- Fix README encoding (CPAN RT#122028)
- Do not use /usr/bin/env in shell bangs
- Correct description wording

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.082840-6
- Perl 5.26 rebuild

* Fri May 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.082840-5
- Fix building on Perl without '.' in @INC

* Tue Feb 28 2017 Petr Pisar <ppisar@redhat.com> - 0.082840-4
- Disable a test incompatible with sqlite >= 3.14 (CPAN RT#119845)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.082840-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.082840-2
- Fix test failures of t/prefetch/grouped.t (BZ#1370461)

* Mon Jun 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.082840-1
- 0.082840 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.082821-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.082821-2
- Perl 5.24 rebuild

* Fri Feb 12 2016 Petr Šabata <contyk@redhat.com> - 0.082821-1
- 0.082821 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.082820-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Petr Pisar <ppisar@redhat.com> - 0.082820-3
- Restore compatability with SQLite-3.9.0 (bug #1272905)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.082820-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Petr Šabata <contyk@redhat.com> - 0.082820-1
- 0.082820 bump

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.082810-5
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.082810-4
- Perl 5.22 rebuild

* Thu May 28 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.082810-3
- Disable optional BR perl(Devel::FindRef)

* Mon Dec 08 2014 Petr Šabata <contyk@redhat.com> - 0.082810-2
- Explicitly provide modules I missed before, hopefully that's all this time

* Fri Dec 05 2014 Petr Šabata <contyk@redhat.com> - 0.082810-1
- 0.082810 bump
- Massive dependency lists rewrite
- Let's be consistent and provide all the hidden modules, not just some

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08250-8
- Perl 5.20 re-rebuild of bootstrapped packages

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08250-7
- Perl 5.20 rebuild

* Wed Jun 18 2014 Petr Pisar <ppisar@redhat.com> - 0.08250-6
- Fix ::Ordered in combination with delete_all (bug #1110272)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08250-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Petr Pisar <ppisar@redhat.com> - 0.08250-4
- Adapt to changes in SQL-Abstract-1.77 (bug #1099741)

* Wed Apr 09 2014 Petr Pisar <ppisar@redhat.com> - 0.08250-3
- Adapt to new sqlite-3.8.2 exception messages (bug #1085336)

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.08250-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Fri Aug  9 2013 Paul Howarth <paul@city-fan.org> - 0.08250-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.08206-1
- update to latest upstream version

* Sat Feb 02 2013 Iain Arnell <iarnell@gmail.com> 0.08205-3
- rebuild without bootstrap again

* Sat Feb 02 2013 Iain Arnell <iarnell@gmail.com> 0.08205-2
- explicitly provide DBIx::Class::Carp
- build with bootstrap enabled to fix broken dependencies

* Tue Jan 29 2013 Iain Arnell <iarnell@gmail.com> 0.08205-1
- update to latest upstream version

* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 0.08203-1
- update to latest upstream version

* Sun Aug 26 2012 Iain Arnell <iarnell@gmail.com> 0.08200-1
- update to latest upstream version

* Sat Aug 04 2012 Iain Arnell <iarnell@gmail.com> 0.08198-3
- rebuild without bootstrap again

* Sat Aug 04 2012 Iain Arnell <iarnell@gmail.com> 0.08198-2
- explicitly provide DBIx::Class::ResultSource::RowParser
- build with bootstrap enabled to fix broken dependencies

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.08198-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08196-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.08196-5
- Perl 5.16 re-rebuild of bootstrapped packages

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.08196-4
- Perl 5.16 rebuild

* Thu Apr 12 2012 Iain Arnell <iarnell@gmail.com> 0.08196-3
- BR DBIx::Class::Storage::Debug::PrettyPrint (rhbz#812143)

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.08196-2
- drop tests subpackage; move tests to main package documentation
- drop old-style filtering

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 0.08196-1
- update to latest upstream version

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.08195-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- minor filtering tweak

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.08127-5.1
- Fix the filters for perl(DBIx::Class::SQLMaker*)

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.08127-5
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.08127-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.08127-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08127-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Iain Arnell <iarnell@gmail.com> 0.08127-1
- update to latest upstream version
- additional filters from requires

* Sat Jan 08 2011 Iain Arnell <iarnell@gmail.com> 0.08126-1
- update to latest upstream version

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08123-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep 09 2010 Iain Arnell <iarnell@gmail.com> 0.08123-1.1
- don't buildrequire Test::Pod

* Thu Sep 02 2010 Iain Arnell <iarnell@gmail.com> 0.08123-1
- update to latest upstream version
- dbicadmin script needs to be executable for tests
- manually tweak real buildrequires

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08120-4
- Mass rebuild with perl-5.12.0

* Fri Mar 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08120-3
- quiet our repo/dep-checking scripts as we figure out how to handle no_index
  from a "requires" perspective

* Wed Mar 17 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08120-2
- update F::A::MT so bits marked as "no_index" are filtered both for provides
  _and_ requires
- update by Fedora::App::MaintainerTools 0.006
- additional deps script run; 27 deps found

* Sat Mar 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08120-1
- update by Fedora::App::MaintainerTools 0.004
- updating to latest GA CPAN version (0.08120)
- added a new br on perl(Context::Preserve) (version 0.01)
- added manual BR on perl(Test::Moose)
- added a new req on perl(Context::Preserve) (version 0.01)
- dropped old requires on perl(List::Util)
- dropped old requires on perl(Scalar::Util)
- dropped old requires on perl(Storable)
- additional deps script run; 27 deps found

* Fri Mar  5 2010 Stepan Kasal <skasal@redhat.com> 0.08119-3
- filter also requires for "hidden" package declarations

* Thu Mar 04 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08119-2
- add ok to BR (unlisted optional testing dep)

* Tue Feb 23 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08119-1
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- altered br on perl(Path::Class) (0.16 => 0.18)
- dropped old BR on perl(Class::C3)
- dropped old BR on perl(JSON::Any)
- altered req on perl(Path::Class) (0.16 => 0.18)
- dropped old requires on perl(DBD::SQLite)
- dropped old requires on perl(JSON::Any)
- additional deps script run; 26 deps found

* Sun Feb 07 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08117-1
- auto-update to 0.08117 (by cpan-spec-update 0.01)
- altered br on perl(Class::Accessor::Grouped) (0.09000 => 0.09002)
- altered br on perl(DBI) (1.605 => 1.609)
- altered br on perl(SQL::Abstract) (1.60 => 1.61)
- altered req on perl(Class::Accessor::Grouped) (0.09000 => 0.09002)
- altered req on perl(DBI) (1.605 => 1.609)
- altered req on perl(SQL::Abstract) (1.60 => 1.61)

* Sat Feb 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08115-1
- auto-update to 0.08115 (by cpan-spec-update 0.01)
- added a new br on perl(Data::Dumper::Concise) (version 1.000)
- altered br on perl(SQL::Abstract) (1.58 => 1.60)
- added a new req on perl(Data::Dumper::Concise) (version 1.000)
- altered req on perl(SQL::Abstract) (1.58 => 1.60)

* Tue Jan 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08112-2
- bump

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08112-1
- auto-update to 0.08112 (by cpan-spec-update 0.01)

* Fri Sep 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08111-1
- update filtering
- auto-update to 0.08111 (by cpan-spec-update 0.01)
- altered br on perl(Carp::Clan) (6 => 6.0)
- altered br on perl(Class::Accessor::Grouped) (0.08003 => 0.09000)
- altered br on perl(Data::Page) (2 => 2.00)
- altered br on perl(File::Temp) (0 => 0.22)
- altered br on perl(SQL::Abstract) (1.56 => 1.58)
- altered br on perl(Test::More) (0 => 0.92)
- altered br on perl(Test::Warn) (0.11 => 0.21)
- altered req on perl(Carp::Clan) (6 => 6.0)
- altered req on perl(Class::Accessor::Grouped) (0.08003 => 0.09000)
- altered req on perl(Data::Page) (2 => 2.00)
- altered req on perl(SQL::Abstract) (1.56 => 1.58)

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08109-1
- auto-update to 0.08109 (by cpan-spec-update 0.01)
- added a new br on perl(File::Temp) (version 0.22)
- altered br on perl(Test::More) (0.82 => 0.92)

* Fri Jul 31 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08108-1
- auto-update to 0.08108 (by cpan-spec-update 0.01)

* Thu Jul 30 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08107-3
- Add BR: perl(CPAN) to fix rebuild-breakdown.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08107-1
- auto-update to 0.08107 (by cpan-spec-update 0.01)
- altered br on perl(DBD::SQLite) (1.13 => 1.25)
- altered br on perl(SQL::Abstract) (1.55 => 1.56)
- added a new req on perl(Carp::Clan) (version 6)
- altered req on perl(Class::Accessor::Grouped) (0.05002 => 0.08003)
- altered req on perl(Class::C3::Componentised) (0 => 1.0005)
- added a new req on perl(Class::Inspector) (version 1.24)
- added a new req on perl(DBD::SQLite) (version 1.25)
- added a new req on perl(DBI) (version 1.605)
- added a new req on perl(Data::Page) (version 2)
- added a new req on perl(JSON::Any) (version 1.18)
- added a new req on perl(List::Util) (version 0)
- added a new req on perl(MRO::Compat) (version 0.09)
- added a new req on perl(Module::Find) (version 0.06)
- added a new req on perl(Path::Class) (version 0.16)
- altered req on perl(SQL::Abstract) (1.2 => 1.56)
- added a new req on perl(SQL::Abstract::Limit) (version 0.13)
- added a new req on perl(Scalar::Util) (version 0)
- added a new req on perl(Scope::Guard) (version 0.03)
- added a new req on perl(Storable) (version 0)
- added a new req on perl(Sub::Name) (version 0.04)
- ** manual updates follow
- force a provides on perl(DBIx::Class::Storage::DBI::Replicated::Types)
- rejigger filtering to a cleaner variant
- drop remaining patch artifacts

* Fri May 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08103-1
- auto-update to 0.08103 (by cpan-spec-update 0.01)
- altered br on perl(Class::Inspector) (0 => 1.24)
- altered br on perl(Carp::Clan) (0 => 6)
- altered br on perl(JSON::Any) (1.17 => 1.18)
- altered br on perl(Module::Find) (0 => 0.06)
- altered br on perl(DBI) (1.4 => 1.605)
- altered br on perl(SQL::Abstract) (1.51 => 1.55)
- added a new br on perl(Test::More) (version 0.82)
- altered br on perl(Path::Class) (0 => 0.16)

* Sun May 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08102-3
- we should also provide perl(DBIx::Class::CDBICompat::Relationship) (and do
  now so provide)

* Sun May 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08102-2
- additional BR's for optional tests

* Sun May 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08102-1
- drop verbose.patch: largely supersceded
- auto-update to 0.08102 (by cpan-spec-update 0.01)
- added a new br on perl(MRO::Compat) (version 0.09)
- added a new br on perl(Test::Warn) (version 0.11)
- altered br on perl(SQL::Abstract) (1.24 => 1.51)
- added a new br on perl(Sub::Name) (version 0.04)
- altered br on perl(Test::Builder) (0.32 => 0.33)
- altered br on perl(Class::C3::Componentised) (0 => 1.0005)
- altered br on perl(Class::Accessor::Grouped) (0.08002 => 0.08003)
- added a new br on perl(Path::Class) (version 0)

* Sun Mar 22 2009 Robert Scheck <robert@fedoraproject.org> 0.08012-3
- Added missing build requirement perl(Test::Deep) for make tests
- Re-diffed make tests patch for more verbosity when skipping tests

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08012-1
- update to 0.08012

* Thu Oct 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-9
- stop filtering perl(DBD::Multi)

* Sun Oct 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-8
- filter all prov/req from anything under _docdir
- note we still filter perl(DBD::Multi), at least until review bug bz#465690
  is completed...
- ...and perl(DBD::Pg) will always be filtered

* Wed Oct 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-7
- fix patch fuzz

* Mon Jun 02 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-6
- bump

* Wed Apr 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-5
- pod coverage testing NOT enabled; test currently "fails"
- make tests skip a little more verbosely...
- add a br of Class::Data::Inheritable for the CDBI-compat testing

* Tue Apr 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-4
- drop unneeded patch1
- set explicit provides version to 0 :)

* Wed Mar 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-3
- add perl(Test::Exception) as a br
- revert patches to skip on DBD::SQLite < 1.13

* Tue Mar 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-2
- BR JSON -> JSON::Any
- rework sqlite/tests patch to skip on DBD::SQLite < 1.15...  1.14 is in
  rawhide/f9, and frankly, doesn't quite pass muster *sigh*

* Sun Mar 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08010-1
- update to 0.08010

* Wed Jan 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08008-3
- add additional BR's for optional tests

* Fri Jan 11 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08008-2
- patch to work around certain tests as DBD::SQLite isn't going to 1.13
  anytime soon (see RH#245699)

* Tue Dec 04 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.08008-1
- update to 0.08008
- correct provides filtering...

* Tue Sep 18 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.08007-1
- Specfile autogenerated by cpanspec 1.71.
