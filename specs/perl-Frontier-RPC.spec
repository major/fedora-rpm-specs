Summary:        A Perl interface for making and serving XML-RPC calls
Name:           perl-Frontier-RPC
Version:        0.07b4p1
Release:        52%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Frontier-RPC
Source0:        https://cpan.metacpan.org/authors/id/R/RT/RTFIREFLY/Frontier-RPC-%{version}.tar.gz
Patch0:         perl-frontier-raw-call.patch
Patch1:         perl-frontier-raw-serve.patch
Patch2:         perl-frontier-undef-scalar.patch
Patch3:         security-xml-external-entity.patch
Patch4:         apache2.patch
# Respect proxy setting for HTTPS, bug #832390, CPAN RT#117812
Patch5:         Frontier-RPC-0.07b4p1-Respect-proxy-setting-for-HTTPS.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# Apache2::Const not used at tests
# Apache2::ServerUtil not used at tests
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::Parser)
Requires:       perl-Frontier-RPC-doc = %{?epoch:%{epoch}:}%{version}-%{release}

%package Client
Summary:        Frontier-RPC-Client Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl-Frontier-RPC-doc = %{?epoch:%{epoch}:}%{version}-%{release}

# To solve conflicts between those two packages
%package doc
Summary:        Frontier-RPC-Client Perl module documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote
Procedure Calls using Extensible Markup Language).  Frontier::RPC
includes both a client module for making requests to a server and
several server modules for implementing servers using CGI, Apache,
and standalone with HTTP::Daemon.

%description Client
Frontier::RPC::Client implements UserLand Software's XML RPC (Remote
Procedure Calls using Extensible Markup Language).  Frontier::RPC::Client
includes just client module for making requests to a server.

%description doc
Documentation and examples to Frontier::RPC and Frontier::RPC::Client.

%prep
%autosetup -p1 -n Frontier-RPC-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorlib}/Apache*
%{perl_vendorlib}/Frontier*

%files Client
%{perl_vendorlib}/Frontier/Client.pm
%{perl_vendorlib}/Frontier/RPC2.pm

%files doc
%doc ChangeLog Changes COPYING README examples/
%{_mandir}/man3/Apache*
%{_mandir}/man3/Frontier*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-48
- Modernize specfile

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-44
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-41
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-38
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-35
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-32
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-29
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Petr Pisar <ppisar@redhat.com> - 0.07b4p1-27
- Respect proxy setting for HTTPS (bug #832390)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-26
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07b4p1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-23
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07b4p1-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 Petr Pisar <ppisar@redhat.com> - 0.07b4p1-20
- Rebase patches to suppress creating *.orig files
- Modernize the spec file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.07b4p1-18
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.07b4p1-15
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.07b4p1-13
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07b4p1-11
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May  3 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.07b4p1-10
- create doc sub-package to solve conflicts

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07b4p1-9
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.07b4p1-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07b4p1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.07b4p1-5
- fix license tag

* Wed Jul 30 2008 Miroslav Suchý <msuchy@redhat.com> 0.07b4p1-4
- applied security patches.
- created light package with only Client part.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.07b4-4
Rebuild for new perl

* Fri Oct 26 2007 Robin Norwood <rnorwood@redhat.com> - 0.07b4-3
- Various fixes from package review:
- Remove BR: perl
- Use dist tag in release
- Resolves: bz#226258

* Wed Aug 29 2007 Robin Norwood <rnorwood@redhat.com> - 0.07b4-2
- Update license tag
- add some files to %%doc section
- Update BuildRequires

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 0.07b4-1
- Upgrade to upstream version 0.07b4

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 0.06-39.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sat Apr 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.06-39
- Source URL: using the Comprehensive Perl Arcana Society Tapestry address
  (Frontier::RPC version 0.06 no longer available in CPAN mirrors).
- spec cleanup (#156480)

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 0.06-38
- rebuild

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Fri Apr  5 2002 Chip Turner <cturner@redhat.com>
- add patch from RHN to allow raw non-conformat calls.
- doesn't affect main code path, but adds functionality
- similar to python xmlrpc module

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 30 2001 Chip Turner <cturner@redhat.com>
- Spec file was autogenerated.

