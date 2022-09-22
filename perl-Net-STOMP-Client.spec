%global cpan_name Net-STOMP-Client

Name:           perl-%{cpan_name}
Version:        2.5
Release:        4%{?dist}
Summary:        STOMP object oriented client module
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LC/LCONS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Messaging::Message)
BuildRequires:  perl(No::Worries) >= 1.2
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides an object oriented client interface to interact with
servers supporting STOMP (Streaming Text Orientated Messaging Protocol). It
supports the major features of messaging brokers: SSL, asynchronous I/O,
receipts and transactions.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
rm -fr $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Lionel Cons <lionel.cons@cern.ch> - 2.5-1
- Updated to 2.5 (rhbz #2013643)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.3-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.3-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.3-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Lionel Cons <lionel.cons@cern.ch> 2.3-1
- New upstream 2.3, rhbz#1418132.

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Lionel Cons <lionel.cons@cern.ch> 2.2-6
- Spec file cleanup.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Massimo Paladin <massimo.paladin@gmail.com> - 2.2-1
- New upstream 2.2, rhbz#1035761.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Pisar <ppisar@redhat.com> - 2.1-2
- Perl 5.18 rebuild

* Thu Jun 13 2013 Massimo Paladin <massimo.paladin@gmail.com> - 2.1-1
- New upstream 2.1, rhbz#973910.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Massimo Paladin <massimo.paladin@gmail.com> - 2.0-1
- New upstream 2.0, rhbz#893464.

* Mon Aug 6 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.8-1
- New upstream 1.8, rhbz#867297.

* Mon Aug 6 2012 Steve Traylen <steve.traylen@cern.ch> - 1.7-1
- New upstream 1.7, rhbz#837746.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.5-2
- Perl 5.16 rebuild

* Fri Apr 20 2012 Steve Traylen <steve.traylen@cern.ch> - 1.5-1
- New upstream 1.5, rhbz#811862

* Wed Feb 1 2012 Steve Traylen <steve.traylen@cern.ch> - 1.4-1
- New upstream 1.4, rhbz#785732
- Add BR Messaging::Message, Test::Pod and Test::Pod::Coverage to
  execute new tests.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Steve Traylen <steve.traylen@cern.ch> - 1.2-1
- New upstream 1.2

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.0-2
- Perl mass rebuild

* Tue May 10 2011 Steve Traylen <steve.traylen@cern.ch> - 1.0-1
- New upstream 1.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Steve Traylen <steve.traylen@cern.ch> - 0.9.5-2
- Add BR perl(Time::HiRes) on EPEL6.

* Mon Jan 10 2011 Steve Traylen <steve.traylen@cern.ch> - 0.9.5-1
- New upstream 0.9.5

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.9.2-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 0.9.2-2
- rebuild

* Tue Jun 08 2010 Steve Traylen <steve.traylen@cern.ch> - 0.9.2-1
- New upstream 0.9.2.

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.9-2
- Mass rebuild with perl-5.12.0

* Mon Mar 29 2010 Steve Traylen <steve.traylen@cern.ch> - 0.9-1
- New upstream 0.9
* Tue Mar 09 2010 Steve Traylen <steve.traylen@cern.ch> - 0.8-2
- Bump for first EPEL/F release

* Tue Mar 02 2010 Steve Traylen <steve.traylen@cern.ch> 0.8-1
- Specfile autogenerated by cpanspec 1.78.
