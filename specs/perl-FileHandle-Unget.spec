Summary:	A FileHandle that supports ungetting of multiple bytes
Name:		perl-FileHandle-Unget
Version:	0.1634
Release:	21%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/FileHandle-Unget
Source0:	https://cpan.metacpan.org/modules/by-module/FileHandle/FileHandle-Unget-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(bytes)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(Scalar::Util) >= 1.14
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Slurper)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
# Optional Tests
BuildRequires:	perl(Devel::Leak)
BuildRequires:	perl(Test::Pod)
# Dependencies
Provides:	perl(FileHandle::Unget) = %{version}

%description
FileHandle::Unget is a drop-in replacement for FileHandle that allows more
than one byte to be placed back on the input. It supports an ungetc(ORD), which
can be called more than once in a row, and an ungets(SCALAR), which places a
string of bytes back on the input.

%prep
%setup -q -n FileHandle-Unget-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc CHANGES README TODO
%{perl_vendorlib}/FileHandle/
%{_mandir}/man3/FileHandle::Unget.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Paul Howarth <paul@city-fan.org> - 0.1634-16
- Use SPDX-format license tag
- Drop support for building with rpm < 4.9
- Use %%license unconditionally

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.1634-13
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.1634-10
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1634-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.1634-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1634-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Paul Howarth <paul@city-fan.org> - 0.1634-1
- Update to 0.1634
  - Fix Makefile.PL warning
  - Fix deleting of inc during release process
  - Better fix for AutomatedTester warning

* Mon Jul  9 2018 Paul Howarth <paul@city-fan.org> - 0.1633-1
- Update to 0.1633
  - Check in standard tests, including one that skips the compile check on
    Windows
  - Add missing URI::Escape dependency
  - Switch from File::Slurp to File::Slurper

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 0.1629-2
- Perl 5.28 rebuild

* Tue Jul  3 2018 Paul Howarth <paul@city-fan.org> - 0.1629-1
- Update to 0.1629
  - Add standard tests
  - Fix compatibility issue with newer versions of perl, which remove "." from
    @INC (CPAN RT#121434)
- Simplify find command using -delete
- Drop buildroot cleaning in %%install section
- Drop legacy Group: tag

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.1628-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1628-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1628-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.1628-10
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.1628-9
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1628-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 0.1628-7
- Adjust RPM version detection to SRPM build root without perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.1628-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1628-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Paul Howarth <paul@city-fan.org> - 0.1628-4
- Prefer %%global over %%define

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1628-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.1628-2
- Perl 5.22 rebuild

* Sun May  3 2015 Paul Howarth <paul@city-fan.org> - 0.1628-1
- Update to 0.1628
  - Prevent CPAN from indexing private-lib

* Mon Apr 20 2015 Paul Howarth <paul@city-fan.org> - 0.1627-1
- Update to 0.1627
  - Clarify licensing terms
  - Move verbose testing to a private module, and implement it in a way that
    doesn't require editing the Makefile after it is generated
  - Require File::Slurp instead of including it, to avoid potential problems
    like this:
    http://www.cpantesters.org/cpan/report/86a0145a-e52b-11e4-a1d1-8536eb4f9f07
  - Fix tests so that they don't prematurely delete the temp file, e.g.:
    http://www.cpantesters.org/cpan/report/3adcb600-6bf9-1014-8336-f8616735162a
  - Fix tests on Windows:
    http://www.cpantesters.org/cpan/report/482c4765-af8d-1014-8ca5-91062b825c07

* Mon Apr 13 2015 Paul Howarth <paul@city-fan.org> - 0.1626-1
- Update to 0.1626
  - Enable verbose testing for CPAN-testers
  - Consolidate issue tracking at rt.cpan.org
  - Use File::Temp for temporary files in the test suite
- License changed to GPLv2

* Sun Apr  5 2015 Paul Howarth <paul@city-fan.org> - 0.1625-1
- Update to 0.1625
  - Modify the memory leak test to check for ≤ 0 bytes; I'm not sure how this
    scenario happens, but test failures like this indicate that it can:
    http://www.cpantesters.org/cpan/report/bdd0e36c-d0dd-11e4-954f-5702e0bfc7aa
  - Attempt to fix loss of lines when $/ is undef
    http://www.cpantesters.org/cpan/report/60452d60-d3cc-11e4-b60b-c2157e3e1735

* Mon Mar 23 2015 Paul Howarth <paul@city-fan.org> - 0.1624-1
- Update to 0.1624
  - Moved code to github
  - Added POD test
  - Improve testability of binmode_bug.t, stdin_tell_bug.t
  - Implement a potential fix for test failures where FileHandle::getline()
    seems to be reading a single line even though $/ is undef
  - Use "local $/" instead of reassigning global $/
  - Improve documentation for input_record_separator()
- Classify buildreqs by usage
- Use %%license where possible

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.1623-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1623-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1623-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.1623-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1623-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1623-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Paul Howarth <paul@city-fan.org> 0.1623-11
- BR: perl(Data::Dumper) for test suite
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> 0.1623-10
- Perl 5.16 rebuild

* Sat Jan  7 2012 Paul Howarth <paul@city-fan.org> 0.1623-9
- Rebuilt for Fedora 17 Mass Rebuild

* Thu Jul 28 2011 Paul Howarth <paul@city-fan.org> 0.1623-8
- Tweak provides filter for rpm 4.9 compatibility
- Nobody else likes macros for commands
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.1623-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1623-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.1623-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.1623-4
- Mass rebuild with perl-5.12.0

* Fri Feb 19 2010 Paul Howarth <paul@city-fan.org> 0.1623-3
- Fix versioned provide for perl(FileHandle::Unget)
- Add buildreq perl(Devel::Leak) for additional test coverage
- Use %%{_fixperms} macro instead of our own %%{__chmod} incantation

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 0.1623-2
- Rebuild against perl 5.10.1

* Tue Sep  1 2009 Paul Howarth <paul@city-fan.org> 0.1623-1
- Update to 0.1623
  - fix uninitialized value warning and incorrect behaviour (CPAN RT#48528)
  - remove reference to obsolete ExtUtils::MakeMaker::bytes (CPAN RT#48984)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1622-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1622-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Paul Howarth <paul@city-fan.org> 0.1622-1
- Update to 0.1622
- BuildRequire perl(Test::More)
- Unget.pm permissions no longer need fixing

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1621-6
- rebuild for new perl

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 0.1621-5
- Clarify license as GPL (unspecified version)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 0.1621-4
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 0.1621-3
- FE6 mass rebuild

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> 0.1621-2
- Don't use macros in command paths, hardcode them instead

* Wed Oct 12 2005 Paul Howarth <paul@city-fan.org> 0.1621-1
- Fedora Extras submission
