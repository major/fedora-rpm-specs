Name:           perl-Catalyst-Model-LDAP
Version:        0.21
Release:        16%{?dist}
Summary:        LDAP model class for Catalyst
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Catalyst-Model-LDAP
Source0:        https://cpan.metacpan.org/authors/id/G/GH/GHENRY/Catalyst-Model-LDAP-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst) >= 5.62
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Model)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Page)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Runtime) >= 0.015
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Net::LDAP) >= 0.65
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Control::ProxyAuth) >= 1.09
BuildRequires:  perl(Net::LDAP::Control::Sort)
BuildRequires:  perl(Net::LDAP::Control::VLV)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Search)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(warnings)

Requires:       perl(Catalyst) >= 5.62
Requires:       perl(Module::Runtime) >= 0.015
Requires:       perl(Net::LDAP) >= 0.65
Requires:       perl(Net::LDAP::Control::ProxyAuth) >= 1.09


%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Runtime\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Net::LDAP\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Net::LDAP::Control::ProxyAuth\\)\s*$

%description
This is the Net::LDAP model class for Catalyst. It is nothing more than a
simple wrapper for Net::LDAP.

%prep
%setup -q -n Catalyst-Model-LDAP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-15
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-12
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- 0.21 bump

* Wed Sep 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- 0.20 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-6
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-5
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 17 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-1
- 0.17 bump
- Modernize spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-20
- Perl 5.22 rebuild

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-19
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.16-17
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.16-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.16-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 07 2008 Caolán McNamara <caolanm@redhat.com> 0.16-4
- rebuild for dependancies

* Sat Apr 12 2008 Simon Wilkinson <simon@sxw.org.uk> 0.16-3
- Make test also check POD coverage
- Fix license to have correct value

* Thu Mar 27 2008 Simon Wilkinson <simon@sxw.org.uk> 0.16-2
- Add build dependencies on Test::Pod and Test::Pod::Coverage for tests

* Thu Mar 27 2008 Simon Wilkinson <simon@sxw.org.uk> 0.16-1
- Specfile autogenerated by cpanspec 1.73.
