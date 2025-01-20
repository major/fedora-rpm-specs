Name:           perl-ORLite
Summary:        Extremely light weight SQLite-specific ORM
Version:        2.00
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/ORLite-%{version}.tar.gz
# Normalize shebangs, not suitable for the upstream
Patch0:         ORLite-1.99-Normalize-shebangs.patch
URL:            https://metacpan.org/release/ORLite
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite) >= 1.27
BuildRequires:  perl(DBI) >= 1.607
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Params::Util) >= 1.00
# Optional run-time, test it while building
BuildRequires:  perl(Class::XSAccessor) >= 1.05
BuildRequires:  perl(Class::XSAccessor::Array) >= 1.05
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional tests
# CPAN::Meta and CPAN::Meta::Prereqs are not helpful
Requires:       perl(File::Remove)
Requires:       perl(File::Temp)

%{?perl_default_filter}
# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(LocalTest\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((LocalTest|MyDB::TableOne)\\)

%description
SQLite is a light weight single file SQL database that provides
an excellent platform for embedded storage of structured data.
However, while it is superficially similar to a regular server-side
SQL database, SQLite has some significant attributes that make using
it like a traditional database difficult. For example, SQLite is
extremely fast to connect to compared to server databases 
(1000 connections per second is not unknown) and is particularly bad
at concurrency, as it can only lock transactions at a database-wide level.
This role as a super-fast internal data store can clash with the roles and
designs of traditional object-relational modules like Class::DBI or 
DBIx::Class. What this situation would seem to need is an object-relation
system that is designed specifically for SQLite and is aligned with its
idiosyncrasies. ORLite is an object-relation system specifically
for SQLite that follows many of the same principles as the ::Tiny
series of modules and has a design that aligns directly to the capabilities
of SQLite.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Class::XSAccessor) >= 1.05
Requires:       perl(Class::XSAccessor::Array) >= 1.05

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n ORLite-%{version}
# Correct permissions
chmod a+x t/*.t t/08_prune.pl
# Correct end of lines
perl -i -pe 's/\r\n$/\n/' t/08_prune.pl

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
#!/bin/bash
set -e
# Many tests write into CWD, or just open an existing database read-write.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset AUTHOR_TESTING
prove
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
# Not parallel safe
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/ORLite.pm
%{_mandir}/man3/ORLite.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 21 2023 Petr Pisar <ppisar@redhat.com> - 2.00-1
- 2.00 bump

* Mon Aug 14 2023 Petr Pisar <ppisar@redhat.com> - 1.99-1
- 1.99 bump
- Package the tests

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 05 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-32
- Update Makefile.PL to not use Module::Install::DSL

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-29
- Perl 5.36 rebuild

* Thu Mar 24 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-28
- Update tests to work for SQLite 3.38 and later (bug #2066641)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-25
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-16
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-13
- Perl 5.26 rebuild

* Wed Feb 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-12
- Update tests to work for SQLite 3.15 and later (bug #1413027)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.98-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 05 2012 Petr Šabata <contyk@redhat.com> - 1.98-1
- 1.98 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.97-2
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Šabata <contyk@redhat.com> - 1.97-1
- 1.97 bump
- Drop command macros

* Mon Feb 27 2012 Petr Pisar <ppisar@redhat.com> - 1.96-1
- 1.96 bump

* Thu Feb 23 2012 Petr Pisar <ppisar@redhat.com> - 1.91-1
- 1.91 bump

* Wed Feb 22 2012 Petr Pisar <ppisar@redhat.com> - 1.90-1
- 1.90 bump

* Tue Feb 21 2012 Petr Pisar <ppisar@redhat.com> - 1.54-1
- 1.54 bump
- Do not package tests

* Thu Feb 02 2012 Petr Šabata <contyk@redhat.com> - 1.52-1
- 1.52 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Petr Pisar <ppisar@redhat.com> - 1.51-1
- 1.51 bump

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.50-2
- Perl mass rebuild

* Wed Jun 08 2011 Petr Sabata <contyk@redhat.com> - 1.50-1
- 1.50 bump

* Wed Jun 01 2011 Petr Sabata <contyk@redhat.com> - 1.49-1
- 1.49 bump
- BuildRoot and defattr cleanup
- BR vars

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> - 1.48-2
- Test with Class::XSAccessor

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> - 1.48-1
- 1.48 bump

* Mon Dec 13 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.47-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.47)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(File::Basename) (version 0)
- added a new br on perl(File::Path) (version 2.08)
- added a new br on perl(File::Spec) (version 0.80)
- added a new br on perl(File::Temp) (version 0.20)
- dropped old BR on perl(Class::XSAccessor::Array)
- added a new req on perl(DBD::SQLite) (version 1.27)
- added a new req on perl(DBI) (version 1.607)
- added a new req on perl(File::Basename) (version 0)
- added a new req on perl(File::Path) (version 2.08)
- added a new req on perl(File::Remove) (version 1.40)
- added a new req on perl(File::Spec) (version 0.80)
- added a new req on perl(File::Temp) (version 0.20)
- added a new req on perl(Params::Util) (version 0.33)

* Thu Dec  2 2010 Petr Sabata <psabata@redhat.com> - 1.46-1
- 1.46 version bump

* Mon Sep 20 2010 Petr Pisar <ppisar@redhat.com> - 1.45-2
- perl(Class::XSAccessor::Array) needed

* Thu Sep 16 2010 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump
- Correct description spelling

* Fri Aug  6 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.44-1
- update

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.42-2
- Mass rebuild with perl-5.12.0

* Wed Mar 31 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.42-1
- update

* Mon Feb  8 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.40-1
- update to 1.40

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.22-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun  3 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.22-1
- update to 0.22

* Thu Feb 12 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.20-1
- update to 0.20

* Mon Jan 12 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.17-1
- update to 1.17

* Wed Oct 29 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.15-1
- update to 0.15

* Fri Aug 29 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.13-2
- fix requires
- update to 0.13

* Fri Aug 29 2008 Marcela Mašláňová 0.11-2
- update to 0.11

* Fri Aug 29 2008 Marcela Mašláňová 0.10-1
- Specfile autogenerated by cpanspec 1.77.
