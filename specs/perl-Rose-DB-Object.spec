Name:		perl-Rose-DB-Object
Version:	0.822
Release:	%autorelease
Summary:	Extensible, high performance object-relational mapper (ORM)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Rose-DB-Object
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-Object-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Bit::Vector)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Clone)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Rose::DateTime::Util)
BuildRequires:	perl(Rose::DB)
BuildRequires:	perl(Rose::Object)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Time::Clock)
BuildRequires:	perl(warnings)

%global __requires_exclude ^perl\\(Rose::(DB|Object)::
%{?perl_default_filter}


%description
Rose::DB::Object is a base class for objects that encapsulate a single row
in a database table. Rose::DB::Object-derived objects are sometimes simply
called "Rose::DB::Object objects" in this documentation for the sake of
brevity, but be assured that derivation is the only reasonable way to use
this class.

%prep
%setup -q -n Rose-DB-Object-%{version}
find . -type f -executable -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
export AUTOMATED_TESTING=1
make test

%files
%doc Changes
%{perl_vendorlib}/Rose/DB/
%{_mandir}/man3/Rose::DB::Object*.3pm*

%changelog
%autochangelog
