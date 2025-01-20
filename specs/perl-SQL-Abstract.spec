Name:           perl-SQL-Abstract
Version:        2.000001
Release:        17%{?dist}
Summary:        Generate SQL from Perl data structures
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Abstract
Source0:        https://cpan.metacpan.org/modules/by-module/SQL/SQL-Abstract-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper::Concise)
%if !%{defined perl_bootstrap}
# DBIx::Class::Storage::Statistic used only with optional tests
BuildRequires:  perl(DBIx::Class::Storage::Statistics)
%endif
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo) >= 2.000001
BuildRequires:  perl(mro)
# MRO::Compat 0.12 not needed since perl 5.9
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote) >= 2.000001
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep) >= 0.101
BuildRequires:  perl(Text::Balanced) >= 2.00
# Optional run-time:
# Term::ANSIColor not usefull for tests
# Tests:
BuildRequires:  perl(overload)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::Warn)
%if !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(DBIx::Class) >= 0.08124
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Hash::Merge) >= 0.12
Requires:       perl(Moo) >= 2.000001
Requires:       perl(mro)
# MRO::Compat 0.12 not needed since perl 5.9
Requires:       perl(Sub::Quote) >= 2.000001
Requires:       perl(Test::Deep) >= 0.101
Requires:       perl(Text::Balanced) >= 2.00

%{?perl_default_filter}
# Remove under-speciefed dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exporter|Test::Deep)\\)$
%global __requires_exclude %__requires_exclude|^perl\\((Moo|Sub::Quote)\\)$

%description
%{summary}.

%package -n perl-DBIx-Class-Storage-Debug-PrettyPrint
Summary:        Pretty Printing DebugObj
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
# Optional run-time:
# Term::ANSIColor

%description -n perl-DBIx-Class-Storage-Debug-PrettyPrint
%{summary}.

%package -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
Summary:	A test of future possibilities
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl

%description -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
%{summary}.

%prep
%setup -q -n SQL-Abstract-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
# %%{_bindir}/format-sql
%{perl_vendorlib}/SQL/
%{_mandir}/man3/DBIx::Class::SQLMaker::Role::SQLA2Passthrough.3pm*
%{_mandir}/man3/SQL::Abstract.3pm*
%{_mandir}/man3/SQL::Abstract::Plugin::BangOverrides.3pm*
%{_mandir}/man3/SQL::Abstract::Plugin::ExtraClauses.3pm*
%{_mandir}/man3/SQL::Abstract::Reference.3pm*
%{_mandir}/man3/SQL::Abstract::Role::Plugin.3pm*
%{_mandir}/man3/SQL::Abstract::Test.3pm*
%{_mandir}/man3/SQL::Abstract::Tree.3pm*

%files -n perl-DBIx-Class-Storage-Debug-PrettyPrint
%license LICENSE
%{perl_vendorlib}/DBIx/Class/Storage/
%{_mandir}/man3/DBIx::Class::Storage::Debug::PrettyPrint.3pm*

%files -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
%license LICENSE
%{perl_vendorlib}/DBIx/Class/SQLMaker/
%{_mandir}/man3/DBIx::Class::SQLMaker::Role::SQLA2Passthrough.3pm*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.000001-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Yaroslav Fedevych <yaroslav@fedevych.name> - 2.000001-14
- Changed source URL to an author-agnostic one

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.000001-8
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.000001-7
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.000001-4
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.000001-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tom Callaway <spot@fedoraproject.org> - 2.000001-1
- update to 2.000001

* Fri Jan 22 2021 Tom Callaway <spot@fedoraproject.org> - 2.000000-1
- update to 2.000000. I think their zero key is stuck.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.87-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.87-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.87-2
- Perl 5.32 rebuild

* Tue Jun 16 2020 Tom Callaway <spot@fedoraproject.org> - 1.87-1
- update to 1.87

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-5
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Tom Callaway <spot@fedoraproject.org> - 1.86-1
- update to 1.86

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.85-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.85-2
- Perl 5.28 rebuild

* Tue Feb 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.85-1
- 1.85 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-2
- Perl 5.26 rebuild

* Tue Apr 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-1
- 1.84 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-9
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-5
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-4
- Perl 5.22 rebuild

* Thu Feb 05 2015 Petr Pisar <ppisar@redhat.com> - 1.81-3
- Skip DBIx::Class tests on boostrap

* Wed Dec 03 2014 Petr Pisar <ppisar@redhat.com> - 1.81-2
- Specify all dependencies (bug #1168882)

* Mon Nov 24 2014 Tom Callaway <spot@fedoraproject.org> - 1.81-1
- update to 1.81

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.77-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  9 2014 Paul Howarth <paul@city-fan.org> - 1.77-1
- Update to latest upstream version
- This release by RIBASUSHI -> update source URL
- BR: perl(Data::Dumper) and perl(Test::Deep) ≥ 0.101
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 1.73-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 1.73-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.72-6
- Perl 5.16 rebuild

* Sun Apr  8 2012 Paul Howarth <paul@city-fan.org> - 1.72-5
- Split DBIx::Class::Storage::Debug::PrettyPrint off into its own sub-package
  to avoid a dependency cycle, since perl-SQL-Abstract and perl-DBIx-Class
  would otherwise require each other and make perl-DBIx-Class unbootable

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.72-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 Iain Arnell <iarnell@gmail.com> 1.72-1
- update to latest upstream version
- update BR perl(Test::Deep) >= 0.106
- update BR perl(Test::More) >= 0.92
- new R/BR perl(Class::Accessor::Grouped) >= 0.10002
- new R/BR perl(Getopt::Long::Descriptive) >= 0.086
- new R/BR perl(Hash::Merge) >= 0.12
- add format-sql script and PrettyPrint.pm to files

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.67-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jul 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.67-1
- update to 1.67

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.61-2
- Mass rebuild with perl-5.12.0

* Mon Feb 22 2010 Chris Weyl <cweyl@alumni.drew.edu> - 1.61-1
- update to 1.61 (for latest DBIx::Class)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.60-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.60-1
- auto-update to 1.60 (by cpan-spec-update 0.01)

* Fri Sep 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.58-1
- add default filtering (pro forma)
- auto-update to 1.58 (by cpan-spec-update 0.01)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.56-1
- auto-update to 1.56 (by cpan-spec-update 0.01)

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.55-1
- added SQLATEST_TESTER=1 to force tests
- auto-update to 1.55 (by cpan-spec-update 0.01)
- added a new br on perl(ExtUtils::MakeMaker) (version 6.42)
- added a new br on perl(Clone) (version 0.31)
- added a new br on perl(Scalar::Util) (version 0)
- added a new br on perl(List::Util) (version 0)
- added a new br on perl(Test::Builder) (version 0)

* Mon Mar 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.50-2
- add missing BR: perl(Test::Exception)

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.50-1
- update to 1.50

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.24-1
- update to 1.24 (for DBIx::Class 0.8012)

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-4
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-3
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-2
- license tag fix

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-1
- bump to 1.22

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.21-2
- fc6 bump

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.21-1
- bump to 1.21

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.20-1
- bump to 1.20

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.19-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.19-1
- Initial package for Fedora Extras
