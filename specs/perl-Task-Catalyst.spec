Name:       perl-Task-Catalyst 
Version:    4.02
Release:    38%{?dist}
# lib/Task/Catalyst.pm -> GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-1.0-or-later OR Artistic-1.0-Perl

Summary:    All you need to start with Catalyst 
Source0:    https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Task-Catalyst-%{version}.tar.gz
URL:        https://metacpan.org/release/Task-Catalyst
BuildArch:  noarch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) => 6.42
# tests for Task::Catalyst itself
BuildRequires: perl(Test::More)
# tests for release-testing
BuildRequires: perl(Pod::Coverage::TrustPod)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

# This macro allows us to easily define identical Requires and BR
%global req_both() %{expand:\
Requires: %*\
BuildRequires: %*\
} 

# Core Modules
%req_both perl(Catalyst) >= 5.80000
%req_both perl(Catalyst::Devel) >= 1.26
%req_both perl(Catalyst::Manual) >= 5.8000
# Recommended Models
%req_both perl(Catalyst::Model::Adaptor)
%req_both perl(Catalyst::Model::DBIC::Schema)
# Recommended Views
%req_both perl(Catalyst::View::TT)
%req_both perl(Catalyst::View::Email)
# Recommended Components
%req_both perl(Catalyst::Controller::ActionRole)
%req_both perl(CatalystX::Component::Traits)
%req_both perl(CatalystX::SimpleLogin)
%req_both perl(Catalyst::Action::REST)
%req_both perl(Catalyst::Component::InstancePerContext)
# Session Support
%req_both perl(Catalyst::Plugin::Session)
%req_both perl(Catalyst::Plugin::Session::State::Cookie)
%req_both perl(Catalyst::Plugin::Session::Store::File)
%req_both perl(Catalyst::Plugin::Session::Store::DBIC)
# Authentication and Authorization
%req_both perl(Catalyst::Plugin::Authentication)
%req_both perl(Catalyst::Authentication::Store::DBIx::Class)
%req_both perl(Catalyst::Authentication::Credential::HTTP)
%req_both perl(Catalyst::ActionRole::ACL)
# Recommended Plugins
%req_both perl(Catalyst::Plugin::Static::Simple)
%req_both perl(Catalyst::Plugin::Unicode::Encoding)
%req_both perl(Catalyst::Plugin::I18N)
%req_both perl(Catalyst::Plugin::ConfigLoader)
# Testing, Debugging and Profiling
%req_both perl(Test::WWW::Mechanize::Catalyst)
%req_both perl(Catalyst::Plugin::StackTrace)
%req_both perl(CatalystX::REPL)
%req_both perl(CatalystX::LeakChecker)
%req_both perl(CatalystX::Profile)
# Deployment
%req_both perl(FCGI)
%req_both perl(FCGI::ProcManager)
%req_both perl(Starman)
%req_both perl(local::lib)

# Make sure we pull it in, regardless of where it is
Requires:   %{_bindir}/catalyst.pl

%description
This package ensures everything you need to write serious Catalyst
applications is installed.  Install this if you're interested in 
developing Catalyst apps. 

%prep
%setup -q -n Task-Catalyst-%{version}

%build
PERL_AUTOINSTALL='--skipdeps' %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 TEST_POD=1 make test

%files
%doc Changes README 
%{perl_vendorlib}/Task*
%{_mandir}/man3/Task*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr  9 2024 Jerry James <loganjerry@gmail.com> - 4.02-36
- Stop building for 32-bit x86
- SPDX migration

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-30
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-27
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-24
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-21
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.02-19
- Use %%{_bindir} instead of /usr/bin
- Fix Url and Source directives
- Use $RPM_BUILD_ROOT instead of %%{buildroot}

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-17
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-14
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-12
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 4.02-10
- Clean up spec file
- Tighten file listing

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Petr Pisar <ppisar@redhat.com> - 4.02-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 4.02-1
- update to latest upstream version
- update dependencies accordingly
- clean up spec for modern rpmbuild

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 3.0000-9
- drop Log4perl requirements. Catalyst::Log::Log4perl has been 
  deprecated, and Task-Catalyst upstream no longer includes Log4perl
  support.

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 3.0000-8
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 3.0000-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.0000-5
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.0000-4
- Mass rebuild with perl-5.12.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 3.0000-2
- make sure we get catalyst.pl installed, too

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 3.0000-1
- implement the req_both macro and pull in the deps we require from
  Makefile.PL

* Thu Feb 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 3.0000-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

