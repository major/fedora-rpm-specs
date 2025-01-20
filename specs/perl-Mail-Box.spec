Name:           perl-Mail-Box
Version:        3.010
Release:        6%{?dist}
Summary:        Manage a mailbox, a folder with messages
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::FcntlLock)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Remove) >= 0.20
BuildRequires:  perl(File::Spec) >= 0.7
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(filetest)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mail::Box::Parser::Perl)
# Versions prior to 3.008 result in a failed test (prerequisite)
BuildRequires:  perl(Mail::Message) >= 3.013
BuildRequires:  perl(Mail::Message::Body)
BuildRequires:  perl(Mail::Message::Body::File)
BuildRequires:  perl(Mail::Message::Body::Lines)
BuildRequires:  perl(Mail::Message::Body::Multipart)
BuildRequires:  perl(Mail::Message::Body::String)
BuildRequires:  perl(Mail::Message::Construct)
BuildRequires:  perl(Mail::Message::Head)
BuildRequires:  perl(Mail::Reporter)
BuildRequires:  perl(Mail::Transport) >= 3.0
BuildRequires:  perl(Object::Realize::Later) >= 0.19
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(User::Identity::Collection)
BuildRequires:  perl(User::Identity::Item)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildArch:      noarch

%description
The Mail::Box folder is a modern mail-folder manager -- at least at
the moment of this writing ;)  It is written to replace Mail::Folder,
although its interface is different.

%prep
%setup -q -n Mail-Box-%{version}

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::SpamAssassin[:\\)]

%build
yes y |%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
# Nuke Zero length files
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Overview.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Cookbook.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Index.pod

%check
make test

%files
%doc README.md README.todo ChangeLog examples/
%{perl_vendorlib}/Mail/
%{_mandir}/man3/*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 3.010-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.010-1
- 3.010 bump (rhbz#2224548)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.009-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.009-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Tom Callaway <spot@fedoraproject.org> - 3.009-1
- update to 3.009

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.008-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Tom Callaway <spot@fedoraproject.org> - 3.008-1
- update to 3.008

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-2
- Perl 5.30 rebuild

* Fri May 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-1
- 3.007 bump

* Sat Mar 02 2019 Sérgio Basto <sergio@serjux.com> - 3.006-2
- Add prerequisite Mail::Message 3.008

* Thu Feb 28 2019 Tom Callaway <spot@fedoraproject.org> - 3.006-1
- update to 3.006

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-2
- Perl 5.28 rebuild

* Mon Mar  5 2018 Tom Callaway <spot@fedoraproject.org> - 3.005-1
- update to 3.005

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Tom Callaway <spot@fedoraproject.org> - 3.004-1
- update to 3.004

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-1
- 3.003 bump

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-2
- Perl 5.26 rebuild

* Thu Jun  1 2017 Tom Callaway <spot@fedoraproject.org> - 3.002-1
- update to 3.002

* Tue Feb 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.120-4
- Update content of subpackages due to CPAN module

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 2.120-3
- subpackage out things

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Tom Callaway <spot@fedoraproject.org> - 2.120-1
- update to 2.120

* Wed Sep 21 2016 Tom Callaway <spot@fedoraproject.org> - 2.119-1
- update to 2.119

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.118-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.118-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.118-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.118-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.118-2
- Perl 5.22 rebuild

* Fri Mar 27 2015 Tom Callaway <spot@fedoraproject.org> - 2.118-1
- update to 2.118

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.107-8
- Perl 5.20 re-rebuild of bootstrapped packages

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.107-7
- Perl 5.20 rebuild

* Wed Jul 23 2014 Petr Pisar <ppisar@redhat.com> - 2.107-6
- Rewrite dependency filters to RPM-4.9 syntax in order not to require
  spamassassis (bug #647783)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.107-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.107-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 2.107-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb  1 2013 Tom Callaway <spot@fedoraproject.org> - 2.107-1
- update to 2.107

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.102-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 2.102-2
- Perl 5.16 rebuild

* Thu Apr 12 2012 Tom Callaway <spot@fedoraproject.org> - 2.102-1
- update to 2.102
- conditionalize perl(Email::Abstract) BuildRequires so that it is only used 
  if we're bootstrapping perl, works around a circular dependency (bz810724)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.097-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.097-2
- Perl mass rebuild

* Wed Mar  2 2011 Tom Callaway <spot@fedoraproject.org> - 2.097-1
- update to 2.097
- remove Mail::SpamAssassin from BuildRequires
- filter Mail::SpamAssassin out of Requires

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.095-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.095-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jul 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.095-1
- update to 2.095

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.091-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.091-2
- rebuild against perl 5.10.1

* Wed Sep  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.091-1
- update to 2.091

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.087-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.087-1
- update to 2.087

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.084-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.084-1
- update to 2.084

* Thu Jun  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.082-1
- update to 2.082

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.073-5
- Rebuild second pass, tests enabled

* Sun Mar  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.073-4
- Rebuild, first pass, disable tests, BR on Email::Abstract

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.073-3
- Rebuild for perl 5.10 (again)

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.073-2
- rebuild for new perl

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.073-1.1
- first rebuild pass, break look with Email::Abstract

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.073-1
- 2.073
- license fix

* Wed Apr  4 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.070-2
- add examples/ to %%doc

* Mon Apr  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.070-1
- Initial package for Fedora
