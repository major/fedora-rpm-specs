Name:      perl-Apache-DBI
Version:   1.12
Release:   28%{?dist}
Summary:   Persistent database connections with Apache/mod_perl

License:   GPL+ or Artistic
URL:       https://metacpan.org/release/Apache-DBI
Source0:   https://cpan.metacpan.org/authors/id/P/PH/PHRED/Apache-DBI-%{version}.tar.gz

BuildArch: noarch
# build deps
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(DBD::mysql)
# runtime deps
BuildRequires: perl(Apache)
BuildRequires: perl(Apache2::Access)
BuildRequires: perl(Apache2::Const)
BuildRequires: perl(Apache2::Log)
BuildRequires: perl(Apache2::Module)
BuildRequires: perl(Apache2::RequestRec)
BuildRequires: perl(Apache2::RequestUtil)
BuildRequires: perl(Apache2::ServerUtil)
BuildRequires: perl(Apache::Constants)
BuildRequires: perl(Carp)
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(IPC::SysV)
BuildRequires: perl(ModPerl::Util)
BuildRequires: perl(constant)
BuildRequires: perl(mod_perl2)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# test deps
BuildRequires: perl(DBD::mysql)
BuildRequires: perl(Test::More)


%{?perl_default_filter}


%description
This is version %{version} of Apache::AuthDBI and Apache::DBI.

These modules are supposed to be used with the Apache server together with 
an embedded perl interpreter like mod_perl. They provide support for basic 
authentication and authorization as well as support for persistent database 
connections via Perl's Database Independent Interface (DBI). 

o DBI.pm provides persistent database connections: 
  - connections can be established during server-startup 
  - configurable rollback to ensure data integrity 
  - configurable verification of the connections to avoid time-outs. 

o AuthDBI.pm provides authentication and authorization: 
  - optional shared cache for passwords to minimize database load 
  - configurable cleanup-handler deletes outdated entries from the cache 

Apache::DBI has been in widespread deployment on many platforms for
years.  Apache::DBI is one of the most widely used mod_perl related
modules.  It can be considered stable.

%prep
%setup -q -n Apache-DBI-%{version}
%{__perl} -pi -e 's|/usr/local/bin/perl|%{__perl}|' eg/startup.pl
chmod 644 eg/startup.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO traces.txt eg/
%{_mandir}/man3/Apache*
%{perl_vendorlib}/Apache

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-27
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-24
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-21
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.12-16
- Overhaul of the spec file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-14
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-6
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.12-2
- Perl 5.18 rebuild

* Sat Jun 15 2013 Remi Collet <Fedora@famillecollet.com> 1.12-1
- update to 1.12

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.11-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 15 2011 Remi Collet <Fedora@famillecollet.com> 1.11-1
- update to 1.11 (bugfix)

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.10-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Remi Collet <Fedora@famillecollet.com> 1.10-1
- update to 1.10 (bugfix)

* Tue Nov 23 2010 Remi Collet <Fedora@famillecollet.com> 1.09-1
- update to 1.09 (bugfix)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-2
- Mass rebuild with perl-5.12.0

* Tue Feb 09 2010 Remi Collet <Fedora@famillecollet.com> 1.08-1
- update to 1.08 (bugfix)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.07-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 17 2008 Remi Collet <Fedora@famillecollet.com> 1.07-1
- update to 1.07

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-2.2
Rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.06-1.2
- add BR: perl(Test::More)

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.06-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sun Mar 25 2007 Remi Collet <Fedora@famillecollet.com> 1.06-1
- update to 1.06

* Sat Nov 25 2006 Remi Collet <Fedora@famillecollet.com> 1.05-2
- change from review (-perldoc +traces +eg)

* Sat Nov 25 2006 Remi Collet <Fedora@famillecollet.com> 1.05-1
- initial spec
