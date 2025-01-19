Name:           perl-Catalyst-Model-DBIC-Schema
Summary:        DBIx::Class::Schema Model Class
Version:        0.66
Release:        6%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBJK/Catalyst-Model-DBIC-Schema-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Model-DBIC-Schema
BuildArch:      noarch

Provides:       perl(Catalyst::Model::DBIC::Schema::Types) = %{version}

BuildRequires: make
BuildRequires:  /usr/bin/catalyst.pl
BuildRequires:  perl-generators
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Catalyst::Component::InstancePerContext)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80005
BuildRequires:  perl(Catalyst::Devel) >= 1.0
BuildRequires:  perl(CatalystX::Component::Traits) >= 0.14
BuildRequires:  perl(CPAN)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class) >= 0.08114
BuildRequires:  perl(DBIx::Class::Cursor::Cached)
BuildRequires:  perl(DBIx::Class::Schema::Loader) >= 0.04005
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose) >= 1.12
BuildRequires:  perl(MooseX::MarkAsMethods) >= 0.13
BuildRequires:  perl(MooseX::NonMoose) >= 0.16
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::LoadableClass)
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)

Requires:       perl(Catalyst::Runtime) >= 5.80005
Requires:       perl(CatalystX::Component::Traits) >= 0.14
Requires:       perl(DBIx::Class) >= 0.08114
Requires:       perl(DBIx::Class::Cursor::Cached)
Requires:       perl(DBIx::Class::Schema::Loader) >= 0.04005
Requires:       perl(Hash::Merge)
Requires:       perl(Moose) >= 1.12
Requires:       perl(MooseX::NonMoose) >= 0.16

%{?perl_default_filter}

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models. See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information on
generating these Models via Helper scripts.

%prep
%setup -q -n Catalyst-Model-DBIC-Schema-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 C_M_DBIC_SCHEMA_TESTAPP=1 make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.66-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 31 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.66-1
- Update to 0.66

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-23
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-20
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.65-12
- Clean up spec file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-2
- Perl 5.22 rebuild

* Sat Nov 22 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.65-1
- Update to 0.65
- Drop upstreamed patch

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Petr Pisar <ppisar@redhat.com> - 0.61-2
- Restore compatibility with Data-Dumper-2.151 (bug #1085905)

* Sat Aug 10 2013 Paul Howarth <paul@city-fan.org> - 0.61-1
- Update to 0.61
  - Fix test failure caused by hash randomization in perl 5.17 (RT#82917)
- This release by ILMARI -> update source URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.60-2
- Perl 5.16 rebuild

* Sun Jun 17 2012 Iain Arnell <iarnell@gmail.com> 0.60-1
- update to latest upstream version
- BR inc::Module::Install instead of EU::MM

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.59-2
- drop tests subpackage; move tests to main package documentation

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 0.59-1
- update to latest upstream version

* Thu Jul 21 2011 Iain Arnell <iarnell@gmail.com> 0.50-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.40-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.40-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.40-3
- Mass rebuild with perl-5.12.0

* Mon Mar 22 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.40-2
- manually provide Catalyst::Model::DBIC::Schema::Types... le sigh

* Fri Mar 12 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.40-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.40)
- added a new br on perl(Carp::Clan) (version 0)
- altered br on perl(Catalyst::Runtime) (5.70 => 5.80005)
- added a new br on perl(CatalystX::Component::Traits) (version 0.14)
- altered br on perl(DBIx::Class) (0.07006 => 0.08114)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(List::MoreUtils) (version 0)
- added a new br on perl(Moose) (version 0.90)
- added a new br on perl(MooseX::Types) (version 0)
- added a new br on perl(Test::Exception) (version 0)
- added a new br on perl(Test::More) (version 0.94)
- added a new br on perl(Tie::IxHash) (version 0)
- added a new br on perl(namespace::autoclean) (version 0)
- dropped old BR on perl(Class::Accessor::Fast)
- dropped old BR on perl(Class::C3)
- dropped old BR on perl(Class::C3::XS)
- dropped old BR on perl(Class::Data::Accessor)
- dropped old BR on perl(MRO::Compat)
- dropped old BR on perl(Test::Pod::Coverage)
- dropped old BR on perl(UNIVERSAL::require)
- added manual BR on perl(Hash::Merge)
- added a new br on CPAN (inc::Module::AutoInstall found)
- added a new req on perl(Carp::Clan) (version 0)
- altered req on perl(Catalyst::Runtime) (5.70 => 5.80005)
- added a new req on perl(CatalystX::Component::Traits) (version 0.14)
- added a new req on perl(DBIx::Class) (version 0.08114)
- added a new req on perl(List::MoreUtils) (version 0)
- added a new req on perl(Moose) (version 0.90)
- added a new req on perl(MooseX::Types) (version 0)
- added a new req on perl(Tie::IxHash) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)
- dropped old requires on perl(Class::Accessor::Fast)
- dropped old requires on perl(Class::Data::Accessor)
- added manual requires on perl(Hash::Merge)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.23-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.23-1
- update to 0.23

* Sat Apr 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.23-1
- update to 0.23

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.21-2
- bump

* Tue Sep 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- update to 0.21

* Tue Jul 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.20-2
- add DBIx::Class::Schema::Loader as a BR and R

* Sun Mar 30 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- Specfile autogenerated by cpanspec 1.74.
