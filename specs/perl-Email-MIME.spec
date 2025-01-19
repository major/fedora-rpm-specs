Name:           perl-Email-MIME
Version:        1.954
Release:        3%{?dist}
Summary:        Easy MIME message parsing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(Email::MessageID)
BuildRequires:  perl(Email::MIME::ContentType) >= 1.023
BuildRequires:  perl(Email::MIME::Encodings) >= 1.314
BuildRequires:  perl(Email::Simple) >= 2.102
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(Email::Simple::Header)
BuildRequires:  perl(Encode) >= 1.9801
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types) >= 1.13
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) > 0.99
# Release Tests
BuildRequires:  perl(Test::Pod) >= 1.41
# Dependencies
Requires:       perl(Email::Simple::Creator)
Requires:       perl(MIME::Types) >= 1.13

Obsoletes:      perl-Email-MIME-Creator < 1.457
Obsoletes:      perl-Email-MIME-Modifier < 1.445
Provides:       perl-Email-MIME-Creator = %{version}
Provides:       perl-Email-MIME-Modifier = %{version}

%description
This is an extension of the Email::Simple module, to handle MIME
encoded messages. It takes a message as a string, splits it up
into its constituent parts, and allows you access to various
parts of the message. Headers are decoded from MIME encoding.


%prep
%setup -q -n Email-MIME-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} -c %{buildroot}


%check
make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"


%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MIME.3*
%{_mandir}/man3/Email::MIME::Creator.3*
%{_mandir}/man3/Email::MIME::Encode.3*
%{_mandir}/man3/Email::MIME::Header.3*
%{_mandir}/man3/Email::MIME::Header::AddressList.3*
%{_mandir}/man3/Email::MIME::Modifier.3*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.954-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.954-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 16 2024 Paul Howarth <paul@city-fan.org> - 1.954-1
- Update to 1.954 (rhbz#2280644)
  - Fix for CVE-2024-4140: An excessive memory use issue (CWE-770) exists in
    Email-MIME before version 1.954, which can cause denial of service when
    parsing multipart MIME messages; the fix is the new $MAX_PARTS
    configuration, which limits how many parts we will consider parsing
    (the default $MAX_PARTS is 100)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.953-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.953-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.953-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.953-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 Paul Howarth <paul@city-fan.org> - 1.953-1
- Update to 1.953
  - As promised, this release no longer works on v5.8; in fact, due to some
    upstream libraries, it hasn't in some time
  - Documentation has been cleaned up to stop referencing long-dead other
    libraries or methods
  - Some small code changes to benefit from v5.10 and v5.12 improvements
- Use SPDX-format license tag
- Use %%{make_build} and %%{make_install}

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.952-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.952-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.952-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Paul Howarth <paul@city-fan.org> - 1.952-1
- Update to 1.952
  - When computing filename, start from raw Content-Disposition
  - Avoid a potentially very slow regex in parsing

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.949-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.949-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.949-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.949-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.949-2
- Perl 5.32 rebuild

* Sun May 24 2020 Paul Howarth <paul@city-fan.org> - 1.949-1
- Update to 1.949
  - Add $Email::MIME::MAX_DEPTH and refuse to parse deeper than that many
    parts; current default: 10
  - Fixes to handling of content-type parameters

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.946-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Paul Howarth <paul@city-fan.org> - 1.946-8
- Spec tidy-up
  - Use author-independent source URL
  - Specify all build dependencies
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.946-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.946-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.946-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.946-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.946-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.946-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.946-1
- update to 1.946

* Mon Jul 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.945-1
- update to 1.945

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.940-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.940-2
- Perl 5.26 rebuild

* Thu Feb  9 2017 Tom Callaway <spot@fedoraproject.org> - 1.940-1
- update to 1.940

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.937-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.937-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Tom Callaway <spot@fedoraproject.org> - 1.937-1
- update to 1.937

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 1.936-1
- update to 1.936

* Tue Aug  4 2015 Tom Callaway <spot@fedoraproject.org> - 1.934-1
- update to 1.934

* Mon Jul 27 2015 Tom Callaway <spot@fedoraproject.org> - 1.933-1
- update to 1.933

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.929-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.929-2
- Perl 5.22 rebuild

* Mon Mar 30 2015 Tom Callaway <spot@fedoraproject.org> - 1.929-1
- update to 1.929

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.926-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.926-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar  6 2014 Tom Callaway <spot@fedoraproject.org> - 1.926-1
- update to 1.926

* Sun Aug 11 2013 Paul Howarth <paul@city-fan.org> - 1.924-1
- Update to 1.924
  - Update use of Email::MIME::ContentType to match new, fixed hash keys:
    type/subtype

* Fri Aug  9 2013 Paul Howarth <paul@city-fan.org> - 1.923-1
- Update to 1.923
  - Repackage, remove PEP links, update bugtracker
  - Try to encode headers based on the header structure, if it has one, rather
    than treating the header as a big string in all cases
  - Do not call parts_set during walk_parts unless the parts have actually
    changed
  - When trying to decode a body, fall back to 7bit if the encoding is unknown;
    trying to create a new body in an unknown encoding is still forbidden
  - Avoid undefined warnings in debug_structure (CPAN RT#82388)
  - Better error message when the given body is a ref but not a scalar
    (CPAN RT#59205)
  - Do not consider the part-ending CRLF part of the body
- Update build-reqs as per upstream requirements
- Explicitly run the release tests
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Classify buildreqs by usage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.911-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.911-2
- Perl 5.18 rebuild

* Sat Feb 23 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.911-1
- Add BR: perl(ExtUtils::MakeMaker) (Fix FTBFS #914270).
- Upstream update.
- Modernize spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.906-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.906-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.906-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.906-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.906-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.906-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  3 2010 Paul Howarth <paul@city-fan.oth> - 1.906-2
- Obsolete perl-Email-MIME-Creator and perl-Email-MIME-Modifier, merged into
  Email::MIME at version 1.900

* Fri Dec  3 2010 Paul Howarth <paul@city-fan.oth> - 1.906-1
- Update to 1.906 (#659635)
- BR: perl(Email::Date::Format) and perl(Email::MessageID)
- BR: perl(Test::MinimumVersion) for additional test coverage
- Bump perl(Email::MIME::Encodings) version requirement to 1.313
- Bump perl(Email::Simple) version requirement to 2.004

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.863-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.863-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.863-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.863-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.863-1
- update to 1.863

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.861-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.861-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.861-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.861-1
- bump to 1.861

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.859-1
- Update to 1.859.

* Sat Feb 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.858-1
- Update to 1.858.

* Fri Dec  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.857-1
- Update to 1.857.

* Thu Oct 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.855-1
- Update to 1.855.

* Sun Oct 15 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.854-1
- Update to 1.854.

* Fri Oct 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.853-1
- Update to 1.853.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.852-1
- Update to 1.852.

* Mon Aug 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.851-1
- Update to 1.851.

* Fri Jul 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.85-1
- Update to 1.85.

* Thu Sep  8 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.82-2
- Requires Email::Simple (rpm "use base" shortcoming).

* Thu Sep 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.82-1
- First build.
