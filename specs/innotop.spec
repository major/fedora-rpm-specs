Name:           innotop
Version:        1.16.0
Release:        %autorelease
Summary:        A MySQL and InnoDB monitor program
BuildArch:      noarch
License:        GPL-2.0-only or Artistic-1.0-Perl
URL:            https://github.com/innotop/innotop
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?el5}
%endif

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
# Term::ANSIColor not used at tests
BuildRequires:  perl(Term::ReadKey)
# Term::ReadLine not used at tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)

Requires:       perl(DBD::mysql)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::ReadLine)

%description
innotop connects to a MySQL database server and retrieves information from it,
then displays it in a manner similar to the UNIX top program.  innotop uses
the data from SHOW VARIABLES, SHOW GLOBAL STATUS, SHOW FULL PROCESSLIST, and
SHOW ENGINE INNODB STATUS, among other things.

%prep
%autosetup

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%license COPYING
%doc README.md
%{_bindir}/innotop
%{_mandir}/man1/innotop.1*

%changelog
%autochangelog
