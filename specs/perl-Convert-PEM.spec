Name:           perl-Convert-PEM
Version:        0.13
Release:        2%{?dist}
Summary:        Read/write encrypted ASN.1 PEM files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-PEM
Source0:        https://www.cpan.org/modules/by-module/Convert/Convert-PEM-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(Convert::ASN1) >= 0.34
BuildRequires:  perl(Crypt::DES_EDE3)
BuildRequires:  perl(Crypt::PRNG)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Optional tests
# Not available in Fedora: perl(Crypt::Camellia), perl(Crypt::Rijndael_PP), perl(Crypt::SEED)
BuildRequires:  openssl
BuildRequires:  perl(Crypt::IDEA)
BuildRequires:  perl(Crypt::OpenSSL::AES)
BuildRequires:  perl(Crypt::Rijndael)
# Dependencies
Requires:       perl(Convert::ASN1) >= 0.34
Requires:       perl(Crypt::DES_EDE3)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Convert::ASN1\\)$

%description
This is Convert::PEM, a module implementing read/write access
to ASN.1-encoded PEM files (with optional encryption).

%prep
%setup -q -n Convert-PEM-%{version}

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
%{perl_vendorlib}/Convert/
%{_mandir}/man3/Convert::PEM.3*
%{_mandir}/man3/Convert::PEM::CBC.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec  3 2024 Paul Howarth <paul@city-fan.org> - 0.13-1
- Update to 0.13 (rhbz#2330122)
  - Fix recent issues in Crypt::DSA (CPAN RT#156495)
  - Handle undefined values and redefined iv (GH#2)
- Switch source URL from cpan.metacpan.org to www.cpan.org

* Tue Oct 22 2024 Paul Howarth <paul@city-fan.org> - 0.12-1
- Update to 0.12 (rhbz#2320853)
  - Add extra cipher support (GH#1)
  - Add DES support
  - Add AES 128/192/256 support
  - Add IDEA support
  - Add SEED Support
  - Add Camellia 128/192/256 support
  - Add tests and test files for additional ciphers and alternate cipher
    modules (if available)
  - Add supporting function(s)/method(s) for additional ciphers
  - Add tests to verify OpenSSL can read files encrypted by Convert::PEM (if
    available)
  - Change key bytes_to_key in Convert::PEM::CBC to match openssl algorithm
  - Make some modifications to accommodate SEED and IDEA (really old) cipher
    modules
  - Make ASN optional
  - Add DER support and documentation
  - Add other access methods to documentation
  - Additional encode/decode testing with DER

* Wed Oct 16 2024 Paul Howarth <paul@city-fan.org> - 0.09-1
- Update to 0.09 (rhbz#2319049)
  - Fix flaky encode test (CPAN RT#27574)
  - Convert build to Dist::Zilla
- Package LICENSE file

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Software Management Team <packaging-team-maint@redhat.com> - 0.08-46
- Eliminate use of obsolete %%patchN syntax (rhbz#2283636)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-40
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-37
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-34
- Perl 5.32 rebuild

* Tue Mar 10 2020 Paul Howarth <paul@city-fan.org> - 0.08-33
- Drop bundled modules and depend on them instead

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Paul Howarth <paul@city-fan.org> - 0.08-31
- Spec tidy-up
  - Use author-independent source URL
  - Use %%{make_build} and %%{make_install}
  - Fix permissions verbosely
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-29
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-26
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-23
- Perl 5.26 rebuild

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-22
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Petr Šabata <contyk@redhat.com> - 0.08-18
- Rewrite the dep list and fix the FTBFS (#1243849)
- Modernize the spec somewhat

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-16
- Perl 5.22 rebuild

* Fri Sep 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-15
- Perl 5.20 rebuild

* Fri Sep 05 2014 Petr Pisar <ppisar@redhat.com> - 0.08-14
- Disable tests relying on probabilistic output (bug #1136745)

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.08-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.08-7
- Perl 5.16 rebuild

* Tue Jan 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08-6
- Add BR: perl(Digest::MD5) (Fix mass rebuild FTBFS).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Steven Pritchard <steve@kspei.com> 0.08-1
- Update to 0.08.
- BR Test::Exception and Test::More.
- Drop extraneous docs.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-10
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.07-9
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.07-6
- rebuild for new perl

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.07-5
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 0.07-4
- Canonicalize Source0 URL.
- Fix find option order.

* Thu Feb 02 2006 Steven Pritchard <steve@kspei.com> 0.07-3
- Better Summary.

* Sat Sep 17 2005 Steven Pritchard <steve@kspei.com> 0.07-2
- Remove explicit core module dependencies.
- Include license files.

* Thu Aug 25 2005 Steven Pritchard <steve@kspei.com> 0.07-1
- Specfile autogenerated.
