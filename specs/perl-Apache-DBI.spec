Name:      perl-Apache-DBI
Version:   1.12
Release:   35%{?dist}
Summary:   Persistent database connections with Apache/mod_perl

License:   GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       https://metacpan.org/release/Apache-DBI
Source0:   https://cpan.metacpan.org/authors/id/P/PH/PHRED/Apache-DBI-%{version}.tar.gz

BuildArch: noarch
# build deps
BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# runtime deps
# perl(Apache) never used because we deliver mod_perl >= 2
# perl(Apache2::Access) not used at tests
# perl(Apache2::Const) not used at tests
# perl(Apache2::Log) not used at tests
# perl(Apache2::Module) not used at tests
# perl(Apache2::RequestRec) not used at tests
# perl(Apache2::RequestUtil) not used at tests
# perl(Apache2::ServerUtil) not used at tests
# perl(Apache::Constants) never used because we deliver mod_perl >= 2
BuildRequires: perl(Carp)
BuildRequires: perl(DBI) >= 1.00
# perl(Digest::MD5) >= 2.20 not used at tests
# perl(Digest::SHA1) >= 2.01 not used at tests
# perl(IPC::SysV) not used at tests
# perl(ModPerl::Util) not used at tests
BuildRequires: perl(constant)
# perl(mod_perl2) not used at tests
BuildRequires: perl(strict)
# perl(warnings) not used at tests
# test deps
BuildRequires: perl(DBD::mysql)
BuildRequires: perl(Test::More)
# Apache::DBI can be used as a compatibility layer in CGI scripts out of
# mod_perl environment. Then Apache2 modules are not loaded. Keep them
# optional.
# perl(Apache) is never used. We deliver mod_perl >= 2.
Recommends: perl(Apache2::Module)
Recommends: perl(Apache2::RequestUtil)
Recommends: perl(Apache2::ServerUtil)
Requires:   perl(DBI) >= 1.00
Recommends: perl(ModPerl::Util)
Recommends: perl(mod_perl2)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DBI|Digest::MD5|Digest::SHA1)\\)$

%description
This is version %{version} of Apache::DBI.

This module is supposed to be used with the Apache server together with
an embedded perl interpreter like mod_perl. It provises support for
persistent database connections via Perl's Database Independent Interface
(DBI):

  - connections can be established during server-startup 
  - configurable rollback to ensure data integrity 
  - configurable verification of the connections to avoid time-outs. 

Apache::DBI has been in widespread deployment on many platforms for
years.  Apache::DBI is one of the most widely used mod_perl related
modules.  It can be considered stable.


%package -n perl-Apache-AuthDBI
Summary:   Authentication and Authorization via Perl's DBI
# Split from perl-Apache-DBI in Fedora 40
Conflicts: perl-Apache-DBI < 1.12-31
Requires:   perl(Apache2::Access)
Requires:   perl(Apache2::Const)
Requires:   perl(Apache2::Log)
Requires:   perl(Apache2::RequestRec)
# Apache::AuthDBI requires mod_perl. We deliver mod_perl >= 2. Therefore hard
# require modules used with mod_perl >= 2 and do not requiree mod_perl 1
# modules.
Requires:   perl(Apache2::RequestUtil)
Requires:   perl(Apache2::ServerUtil)
Requires:   perl(DBI) >= 1.00
Requires:   perl(Digest::MD5) >= 2.20
Requires:   perl(Digest::SHA1) >= 2.01
Requires:   perl(IPC::SysV)
Requires:   perl(warnings)

%description -n perl-Apache-AuthDBI
This is version %{version} of Apache::AuthDBI.

This module is supposed to be used with the Apache server together with
an embedded perl interpreter like mod_perl. It provides support for basic
authentication and authorization via Perl's Database Independent Interface
(DBI):

  - optional shared cache for passwords to minimize database load
  - configurable cleanup-handler deletes outdated entries from the cache


%prep
%setup -q -n Apache-DBI-%{version}
perl -pi -MConfig -e 's|^#!/usr/local/bin/perl\b|$Config{startperl}|' eg/startup.pl
chmod 644 eg/startup.pl


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset MOD_PERL_API_VERSION
make test

%files
%doc Changes README TODO traces.txt eg/
%{_mandir}/man3/Apache::DBI.*
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/DBI.pm

%files -n perl-Apache-AuthDBI
%doc Changes README TODO traces.txt eg/
%{_mandir}/man3/Apache::AuthDBI.*
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/AuthDBI.pm

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Petr Pisar <ppisar@redhat.com> - 1.12-31
- Convert the license tag to an SPDX format
- Correct listing the dependencies
- Move Apache::AuthDBI to perl-Apache-AuthDBI RPM package

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
