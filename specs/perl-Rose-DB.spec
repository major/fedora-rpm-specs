Name:		perl-Rose-DB
Version:	0.788
Release:	%autorelease
Summary:	DBI wrapper and abstraction layer
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Rose-DB
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(Bit::Vector::Overload) >= 6.4
BuildRequires:	perl(Carp)
BuildRequires:	perl(Clone::PP)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(DateTime::Duration)
BuildRequires:	perl(DateTime::Format::MySQL)
BuildRequires:	perl(DateTime::Format::Oracle)
BuildRequires:	perl(DateTime::Format::Pg) >= 0.11
BuildRequires:	perl(DateTime::Infinite)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBD::MariaDB)
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(DBD::Pg)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Rose::DateTime::Util) >= 0.532
BuildRequires:	perl(Rose::Object) >= 0.854
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(SQL::ReservedWords)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Clock)
BuildRequires:	perl(Test::Pod) >= 1.0
BuildRequires:	perl(warnings)
BuildRequires:	perl(YAML)


%description
Rose::DB is a wrapper and abstraction layer for DBI-related functionality.
A Rose::DB object "has a" DBI object; it is not a subclass of DBI.

%prep
%setup -q -n Rose-DB-%{version}

%build
find . -type f -executable -exec chmod -x {} +

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} %{buildroot}/*

%check
export AUTOMATED_TESTING=1
make test

%files
%doc Changes
%{perl_vendorlib}/Rose/
%{_mandir}/man3/Rose::DB*.3pm*

%changelog
%autochangelog
