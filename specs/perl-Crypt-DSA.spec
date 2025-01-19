Summary:	Perl module for DSA signatures and key generation
Name:		perl-Crypt-DSA
Version:	1.19
Release:	2%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Url:		https://metacpan.org/release/Crypt-DSA
Source0:	https://www.cpan.org/modules/by-module/Crypt/Crypt-DSA-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	openssl
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Convert::ASN1)
BuildRequires:	perl(Convert::PEM) >= 0.13
BuildRequires:	perl(Crypt::URandom)
BuildRequires:	perl(Data::Buffer) >= 0.01
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Which) >= 0.05
BuildRequires:	perl(integer)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Math::BigInt) >= 1.78
BuildRequires:	perl(Math::BigInt::GMP)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test::More) >= 0.42
# Optional Tests
BuildRequires:	perl(Crypt::DES_EDE3)
# Dependencies
# Crypt::DSA::Keychain calls openssl for DSA parameter generation
Requires:	openssl
# Convert::ASN1 used by Crypt::DSA::Signature
Requires:	perl(Convert::ASN1)
# Some operations are really slow without GMP (or Pari, but we test with GMP)
Requires:	perl(Math::BigInt::GMP)

%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. This package provides DSA signing, signature
verification, and key generation.

DSA (Digital Signature Algorithm) signatures are no longer considered to be
adequate for security. This module should only be used for verifying old
signatures and should not be used for new signatures. That being said, some
technologies still require DSA signatures even now. Consider using other
solutions or explicitly not using DSA signatures.

%prep
%setup -q -n Crypt-DSA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::DSA.3*
%{_mandir}/man3/Crypt::DSA::Key.3*
%{_mandir}/man3/Crypt::DSA::Key::PEM.3*
%{_mandir}/man3/Crypt::DSA::Key::SSH2.3*
%{_mandir}/man3/Crypt::DSA::KeyChain.3*
%{_mandir}/man3/Crypt::DSA::Signature.3*
%{_mandir}/man3/Crypt::DSA::Util.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Paul Howarth <paul@city-fan.org> - 1.19-1
- Update to 1.19
  - New maintainer
  - This release resolves CVE-2011-3599
  - Added a statement to recommend against using DSA
  - Fixed a few long standing bugs
  - The build process is moved to Dist::Zilla
- Switch source URL from cpan.metacpan.org to www.cpan.org

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Software Management Team <packaging-team-maint@redhat.com> - 1.17-41
- Eliminate use of obsolete %%patchN syntax (rhbz#2283636)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-35
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-32
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-29
- Perl 5.32 rebuild

* Tue Mar 10 2020 Paul Howarth <paul@city-fan.org> - 1.17-28
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Remove bundled modules and depend on them instead
  - Use %%{make_build} and %%{make_install}
  - Fix permissions verbosely
  - Use %%license

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-22
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-19
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-18
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-13
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Paul Howarth <paul@city-fan.org> - 1.17-10
- Remove the ability to fall back to the cryptographically-insecure Data::Random
  instead of using /dev/random (#743567, CPAN RT#71421, CVE-2011-3599)
- Don't need to remove empty directories from the buildroot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.17-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.17-5
- Perl 5.16 rebuild

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> 1.17-4
- Fedora 17 mass rebuild
- Use %%{_fixperms} macro rather than our own chmod incantation
- BR: perl(Carp)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> 1.17-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> 1.17-2
- Perl mass rebuild

* Fri Jun 17 2011 Paul Howarth <paul@city-fan.org> 1.17-1
- Update to 1.17
  - Upgrade to Module::Install 1.01
  - Added support for OpenSSL 1.0.0 dsaparam format change (CPAN RT#49668)
  - Requires perl 5.6 now (CPAN RT#58094)
  - Fixes for 64-bit support
- Drop upstreamed patches
- Release tests moved to xt/ directory upstream and now tested separately
- Nobody else likes macros for commands
- Drop backwards compatibility with ancient distributions

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> 1.16-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Jun  3 2010 Paul Howarth <paul@city-fan.org> 1.16-4
- META.yml should specify perl >= 5.006 due to use of 3-arg open (CPAN RT#58094)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> 1.16-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> 1.16-2
- Rebuild against perl 5.10.1

* Fri Sep 11 2009 Paul Howarth <paul@city-fan.org> 1.16-1
- Update to 1.16 (first production release)
- New upstream maintainer -> change source URL
- Change buildreq which to perl(File::Which)
- Add new buildreqs perl(Crypt::DES_EDE3), perl(File::Spec), perl(IPC::Open3)
- Buildreq perl(Math::BigInt) >= 1.78
- Enable AUTOMATED_TESTING
- New test requirements:
  - perl(Perl::MinimumVersion) >= 1.20
  - perl(Test::CPAN::Meta) >= 0.12
  - perl(Test::MinimumVersion) >= 0.008
  - perl(Test::Pod) >= 1.26
- ToDo no longer present upstream, but add LICENSE and README as %%doc
- Add runtime dependency on openssl (used for DSA parameter generation)
- Add patch for openssl dsaparam 1.0 compatibility (CPAN RT#49668)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov  3 2008 Paul Howarth <paul@city-fan.org> 0.14-7
- BuildRequire and Require a GMP support module, either Math::GMP or
  Math::BigInt::GMP depending on how recent Math::BigInt is
- BuildRequire openssl, which significantly speeds up the keygen test

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-6
- Rebuild for new perl

* Sat Aug 11 2007 Paul Howarth <paul@city-fan.org> 0.14-5
- Clarify license as GPL v1 or later, or Artistic (same as perl)
- Add buildreq perl(Test::More)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 0.14-4
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 0.14-3
- FE6 mass rebuild

* Mon May 29 2006 Paul Howarth <paul@city-fan.org> 0.14-2
- Add missing buildreq: which

* Tue May  9 2006 Paul Howarth <paul@city-fan.org> 0.14-1
- Update to 0.14

* Mon Nov 28 2005 Paul Howarth <paul@city-fan.org> 0.13-1
- Initial build
