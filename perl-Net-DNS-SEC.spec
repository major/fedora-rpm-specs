Name:           perl-Net-DNS-SEC
Version:        1.20
Release:        5%{?dist}
Summary:        DNSSEC modules for Perl
License:        MIT
URL:            https://metacpan.org/release/Net-DNS-SEC
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-SEC-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel => 1.1
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec) >= 0.86
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64) >= 2.11
BuildRequires:  perl(Net::DNS) >= 1.08
BuildRequires:  perl(Net::DNS::ZoneFile)
# Tests only
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
Requires:       perl(File::Spec) >= 0.86
Requires:       perl(Net::DNS) >= 1.08

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Spec|Net::DNS)\\)

%description
Net::DNS::SEC is installed as an extension to an existing Net::DNS
installation providing packages to support DNSSEC as specified in
RFC4033, RFC4034, RFC4035 and related documents.

It also provides support for SIG0 which is useful for dynamic updates.

Implements cryptographic signature generation and verification functions
using RSA, DSA, ECDSA, and Edwards curve algorithms.

%prep
%setup -q -n Net-DNS-SEC-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README demo
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Wes Hardaker <wjhnns174@hardakers.net> - 1.19-1
- version bump

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.18-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Wes Hardaker <wjhnns174@hardakers.net> - 1.18-1
- version bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Wes Hardaker <wjhnns174@hardakers.net> - 1.17-1
- version bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-6
- Perl 5.32 rebuild

* Fri May 01 2020 Petr Pisar <ppisar@redhat.com> - 1.12-5
- Correct list of the dependencies (bug #1765957)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-2
- Perl 5.30 rebuild

* Fri Apr 12 2019 Wes Hardaker <wjhns174@hardakers.net> - 1.12-1
- Update to 1.12
- Fixed README per patch suggestion in #1699090

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-1
- 1.11 bump

* Fri Aug 31 2018 Paul Wouters <pwouters@redhat.com> - 1.10-1
- Update to 1.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-2
- Perl 5.28 rebuild

* Thu Jun 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-1
- 1.09 bump

* Wed May 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-1
- 1.08 bump

* Tue Mar 20 2018 Wes Hardaker <wjhns174@hardakers.net> - 1.05-1
- 1.05 bump

* Fri Feb 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump

* Wed Feb 14 2018 Paul Wouters <pwouters@redhat.com> - 1.03_08-1
- Updated to 1.04 - rewrite to use custom code to support openssl-1.1
- Package changed from noarch to arch

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.26 rebuild

* Tue Mar 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 01 2016 Paul Wouters <pwouters@redhat.com> - 1.02-4
- Require perl(Net::DNS) >= 1.01 as some code moved from here to there

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-1
- 1.02 bump

* Fri Aug 07 2015 Petr Šabata <contyk@redhat.com> - 1.01-4
- Re-enable the test suite and drop the now unneeded dependency filters

* Fri Aug 07 2015 Petr Šabata <contyk@redhat.com> - 1.01-3
- D'oh, drop the explicit runtime dependencies as well

* Fri Aug 07 2015 Petr Šabata <contyk@redhat.com> - 1.01-2
- Also temporarily filter out the new, autogenerated Net::DNS runtime dependency

* Fri Aug 07 2015 Petr Šabata <contyk@redhat.com> - 1.01-1
- Updating to 1.01, needed for new Net::DNS (#1240457)
- Correcting the license tag which was wrong since the very beginning
- Modernizing the spec file somewhat
- Fixing the dep list
- Temporarily disabling the test suite until Net::DNS-1.01+ is built

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.22 rebuild

* Mon Apr 20 2015 Wes Hardaker <wjhns174@hardakers.net> - 0.22-2
- remove GOST files before packaging due to R.H. GOST policy

* Mon Apr 20 2015 Wes Hardaker <wjhns174@hardakers.net> - 0.22-1
- updated to 0.22

* Fri Oct 31 2014 Paul Wouters <pwouters@redhat.com> - 0.21-1
- Updated to 0.21, restores canonicalization of a RRSIG’s Signer Name

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-2
- Perl 5.20 rebuild

* Sat Aug 16 2014 Paul Wouters <pwouters@redhat.com> - 0.20-1
- Updated to 0.20, fixes "-" (zero) salt fields in NSEC3 representation
- Remove inappropriate deprecation warning in DNSKEY.pm (0.19 upstream)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Paul Wouters <pwouters@redhat.com> - 0.18-1
- Updated to 0.18 - Recode RR implementations, null salt NSEC3PARAM fix

* Fri Nov 29 2013 Paul Wouters <pwouters@redhat.com> - 0.17-1
- Updated to 0.17
- Cleanup some old rhel5 style macros

* Thu Aug 08 2013 Paul Wouters <pwouters@redhat.com> - 0.16-15
- Rebuild for newer perl dependancies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.16-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.16-10
- Perl 5.16 rebuild

* Mon Mar 19 2012 Wes Hardaker <wjhns174@hardakers.net> - 0.16-9
- Added a patch to fix the NSEC shouldn't be downcased issue

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.16-7
- Perl mass rebuild

* Thu Jun 23 2011 Wes Hardaker <wjhns174@hardakers.net> - 0.16-6
- added support for the v1.3 private key format

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep 23 2010 Wes Hardaker <wjhns174@hardakers.net> - 0.16-3
- rebuild after prereq now properly in the system

* Tue Aug 24 2010 Wes Hardaker <wjhns174@hardakers.net> - 0.16-2
- added MIME::Base32 as a build req

* Tue Aug 24 2010 Wes Hardaker <wjhns174@hardakers.net> - 0.16-1
- Update to upstream 0.16

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.14-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-3
Rebuild for new perl

* Wed Jul 11 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.14-2
- BuildRequire Digest::SHA
- include the demo scripts in the documentation

* Wed Apr 18 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.14-1
- Initial version
