Name:           perl-HTML-FormFu-Model-DBIC
Summary:        Integrate HTML::FormFu with DBIx::Class
Version:        2.03
Release:        23%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/HTML-FormFu-Model-DBIC-%{version}.tar.gz
URL:            https://metacpan.org/release/HTML-FormFu-Model-DBIC
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::FormFu::Constraint)
# HTML::FormFu::Model version from Makefile.PL's HTML::FormFu declaration
BuildRequires:  perl(HTML::FormFu::Model) >= 2.00
BuildRequires:  perl(HTML::FormFu::Util)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
# Tests:
BuildRequires:  perl(DateTime)
# DateTime::Format::SQLite needed by tests using SQLite via DBIx::Class
BuildRequires:  perl(DateTime::Format::SQLite)
# DBD::SQLite needed by connect('dbi:SQLite:…') in t/lib/DBICTestLib.pm
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class) >= 0.08108
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::FormFu) >= 2.00
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Test::More)

# DBIx::Class is used nowhere by the installed code, but let's assume this
# package is not compatible with former DBIx::Class versions
Requires:       perl(DBIx::Class) >= 0.08108
Requires:       perl(HTML::FormFu::Constraint)
# HTML::FormFu::Model version from Makefile.PL's HTML::FormFu declaration
Requires:       perl(HTML::FormFu::Model) >= 2.00


%{?perl_default_filter}
%{?perl_default_subpackage_tests}

# Remove under-specifed dependency
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTML::FormFu::Model\\)$

%description
Integrate your HTML::FormFu forms with a DBIx::Class model.


%prep
%setup -q -n HTML-FormFu-Model-DBIC-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.03-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-3
- Perl 5.28 rebuild

* Wed Apr 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.03-2
- Fix dependencies

* Wed Apr 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.03-1
- Update to 2.03

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.02-1
- Update to 2.02

* Sat Jun 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.01-1
- Update to 2.01

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 03 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.00-6
- Pass NO_PACKLIST to Makefile.PL
- Fix a typo

* Fri Oct 02 2015 Petr Pisar <ppisar@redhat.com> - 2.00-5
- Correct dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-3
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-2
- Perl 5.20 rebuild

* Sun Jun 08 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.00-1
- Update to 2.00

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 09 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.02-1
- Update to 1.02

* Sun Jan 12 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.01-1
- Update to 1.01

* Sun Jan 05 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00-1
- Update to 1.00

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09010-1
- Update to 0.09010

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Petr Pisar <ppisar@redhat.com> - 0.09002-2
- Perl 5.16 rebuild

* Thu Jan 12 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.09002-1
- Update to 0.09002
- Remove the defattr macro (no longer used)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.09000-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.09000-2
- Perl mass rebuild

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.09000-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08002-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 09 2010 Iain Arnell <iarnell@gmail.com> 0.08002-1
- update to latest upstream version
- fixes FTBFS RHBZ#660763
- clean up spec for modern rpmbuild

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06000-2
- Mass rebuild with perl-5.12.0

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.06000-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.06000)
- altered br on perl(DBIx::Class) (0.08106 => 0.08108)
- added a new br on perl(SQL::Translator) (version 0)
- altered req on perl(DBIx::Class) (0.08106 => 0.08108)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05002-2
- rebuild against perl 5.10.1

* Sat Aug 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.05002-1
- auto-update to 0.05002 (by cpan-spec-update 0.01)
- altered br on perl(DBIx::Class) (0.08002 => 0.08106)
- added a new br on perl(DateTime::Format::SQLite) (version 0)
- altered br on perl(HTML::FormFu) (0.03007 => 0.05000)
- added a new br on perl(List::MoreUtils) (version 0)
- added a new req on perl(DBD::SQLite) (version 0)
- altered req on perl(DBIx::Class) (0 => 0.08106)
- added a new req on perl(HTML::FormFu) (version 0.05000)
- added a new req on perl(List::MoreUtils) (version 0)
- added a new req on perl(Task::Weaken) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03007-1
- touch up for submission

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03007-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
