# Perform optional tests
%bcond_without perl_SQL_Shell_enables_optional_test

Name:       perl-SQL-Shell 
Version:    1.17
Release:    19%{?dist}
# lib/SQL/Shell.pm: GPLv2+
# bin/sqlsh:        GPLv2+
# README:           GPLv2+
# COPYING:          GPLv2 text (old FSF address, see CPAN RT#112335)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Summary:    Command interpreter for DBI shells 
Url:        https://metacpan.org/release/SQL-Shell
Source:     https://cpan.metacpan.org/authors/id/M/MG/MGUALDRON/SQL-Shell-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
%if %{with perl_SQL_Shell_enables_optional_test}
BuildRequires:  perl(CGI)
%endif
# Config not used at tests
BuildRequires:  perl(constant)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Path)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::File)
# IO::Scalar not used at tests
%if %{with perl_SQL_Shell_enables_optional_test}
BuildRequires:  perl(Locale::Recode)
%endif
# Log::Trace not used at tests
# Pod::Select not used at tests
# Pod::Usage not used at tests
BuildRequires:  perl(strict)
# Term::ReadKey not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(IO::CaptureOutput)
BuildRequires:  perl(Test::Assertions::TestScript)
BuildRequires:  perl(Test::More)
%if %{with perl_SQL_Shell_enables_optional_test}
# Optional tests:
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:   perl(CGI)
Requires:   perl(Locale::Recode)

%description
SQL::Shell is a command-interpreter API for building shells and batch
scripts. A command-line interface with readline support is included 
as part of the CPAN distribution. See SQL::Shell::Manual for a user
guide. SQL::Shell offers features similar to the mysql or sql*plus
client programs but is database independent.

This package provides the backend SQL::Shell libraries.  For the 
command-line interpreter (sqlsh), please also install the sqlsh package.

%package -n sqlsh
Summary:    Command interpreter for DBI shells
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   perl(IO::Scalar)
Requires:   perl(Pod::Select)
# Term::ReadLine::Gnu for GetHistory(), bug #707442
Requires:   perl(Term::ReadLine::Gnu)

%description -n sqlsh
sqlsh is a command-interpreter API for building shells and batch
scripts. sqlsh/SQL::Shell offers features similar to the mysql or 
sql*plus client programs but is database independent.

See the SQL::Shell::Manual manual page for a user guide.

%prep
%setup -q -n SQL-Shell-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset ORACLE_HOME PERL_READLINE_MODE
export UNIT_TEST_DSN='DBI:SQLite:dbname=test.db'
export UNIT_TEST_USER='anything'
export UNIT_TEST_PASS=''
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files -n sqlsh
%{_bindir}/sqlsh
%{_mandir}/man1/sqlsh.1.gz

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.17-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-2
- Perl 5.30 rebuild

* Mon May 27 2019 Petr Pisar <ppisar@redhat.com> - 1.17-1
- 1.17 bump

* Fri May 24 2019 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump (a license changed to GPLv2+)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-2
- Perl 5.24 rebuild

* Wed Feb 24 2016 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-18
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.14-14
- Perl 5.18 rebuild
- Perl 5.18 compatibility (CPAN RT#87245)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.14-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.14-9
- Perl mass rebuild

* Wed May 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.14-8
- add requires 707442
- clean specfile

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.14-6
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.14-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.14-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.14-2
- add defattr to sqlsh, as suggested in review

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.14-1
- submission
- define subpackage

* Wed Apr 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.14-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

