Summary:	A fast and simple mbox folder reader
Name:		perl-Mail-Mbox-MessageParser
Version:	1.5111
Release:	21%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/Mail-Mbox-MessageParser
Source0:	https://cpan.metacpan.org/modules/by-module/Mail/Mail-Mbox-MessageParser-%{version}.tar.gz
Source1:	perl-module-version-filter
Patch0:		Mail-Mbox-MessageParser-1.5111-Test-Compile.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	grep, gzip, bzip2, lzip >= 1.3, xz, /usr/bin/diff
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode) >= 2.11
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(PerlIO::encoding)
BuildRequires:	perl(PerlIO::utf8_strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FileHandle::Unget)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Path) >= 2.08
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(UNIVERSAL::require)
# Optional Tests
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Dependencies
Requires:	grep, gzip, bzip2, lzip >= 1.3, xz, /usr/bin/diff
Requires:	perl(Storable)

%description
Mail::Mbox::MessageParser is a feature-poor but very fast mbox parser. It uses
the best of three strategies for parsing a mailbox: either using cached folder
information, GNU grep, or highly optimized Perl.

%prep
%setup -q -n Mail-Mbox-MessageParser-%{version}

# Workaround for Test::Compile ≥ 2.0.0
%patch -P 0 -p0

# Auto provides aren't clever enough for what Mail::Mbox::MessageParser does
%if 0%{?__perllib_provides:1}
%global provfilt /bin/sh -c "%{__perllib_provides} | perl -n -s %{SOURCE1} -lib=%{_builddir}/%{buildsubdir}/lib"
%global __perllib_provides %{provfilt}
%else
%global provfilt /bin/sh -c "%{__perl_provides} | perl -n -s %{SOURCE1} -lib=%{_builddir}/%{buildsubdir}/lib"
%global __perl_provides %{provfilt}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor \
	BZIP=/usr/bin/bzip2 \
	BZIP2=/usr/bin/bzip2 \
	CAT=/bin/cat \
	DIFF=/usr/bin/diff \
	GREP=/bin/grep \
	GZIP=/bin/gzip \
	LZIP=/usr/bin/lzip \
	XZ=/usr/bin/xz

make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc anonymize_mailbox CHANGES README TODO
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::Mbox::MessageParser.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Cache.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Config.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Grep.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::MetaInfo.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Perl.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.5111-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.5111-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.5111-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Paul Howarth <paul@city-fan.org> - 1.5111-5
- Workaround for FTBFS with Test::Compile ≥ 2.0.0

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.5111-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Paul Howarth <paul@city-fan.org> - 1.5111-1
- Update to 1.5111
  - Ensure that temp file is created in temp dir
  - Fix Makefile.PL warning
  - Fix deleting of inc during release process
  - Better fix for AutomatedTester warning

* Mon Jul  9 2018 Paul Howarth <paul@city-fan.org> - 1.5110-1
- Update to 1.5110
  - Check in standard tests, including one that skips the compile check on
    Windows
  - Switch from File::Slurp to File::Slurper
  - Updating META.yml

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 1.5106-2
- Perl 5.28 rebuild

* Mon Jul  2 2018 Paul Howarth <paul@city-fan.org> - 1.5106-1
- Update to 1.5106
  - Add standard tests
  - Detect mailboxes that contain a mix of newline types; complain about it,
    but also allow the force option to continue processing
  - Avoid OO interface to File::Temp, which in some versions and on some
    operating systems, deletes the file when it is closed (CPAN RT#103835)
  - Fix compatibility issue with newer versions of perl, which remove "." from
    @INC (CPAN RT#121466)
- Simplify find command using -delete

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.5105-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5105-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5105-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.5105-9
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.5105-8
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5105-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.5105-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5105-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Paul Howarth <paul@city-fan.org> - 1.5105-4
- Prefer %%global over %%define
- Drop EL-5 build support as File::Path version is too old there

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.5105-2
- Perl 5.22 rebuild

* Sun May  3 2015 Paul Howarth <paul@city-fan.org> - 1.5105-1
- Update to 1.5105
  - Prevent CPAN from indexing private-lib

* Mon Apr 20 2015 Paul Howarth <paul@city-fan.org> - 1.5104-1
- Update to 1.5104
  - Add File::Path dependency for testing (CPAN RT#103482)
  - Don't install private Module::Install extension (CPAN RT#103482)
  - Clarify licensing terms
  - Move verbose testing to a private module, and implement it in a way that
    doesn't require editing the Makefile after it is generated
  - Require File::Slurp instead of including it, to avoid potential problems
    like this:
    http://www.cpantesters.org/cpan/report/86a0145a-e52b-11e4-a1d1-8536eb4f9f07
  - Improve the ability of the test suite to be run in parallel
  - Fix Windows test incompatibilities, such as:
    http://www.cpantesters.org/cpan/report/12187014-af8d-1014-92d8-fdf72a825c07
    http://www.cpantesters.org/cpan/report/12187014-af8d-1014-92d8-fdf72a825c07

* Mon Apr 13 2015 Paul Howarth <paul@city-fan.org> - 1.5102-1
- Update to 1.5102
  - Add a version check for lzip, to make sure the .lz file can be decompressed
    properly during testing
  - Fix warning about deleting nonexistent test cache
  - Enhance "make test TEST_VERBOSE=1" to dump debug information
  - Work around a POD-stripping bug that would cause module load to fail on
    some platforms (CPAN RT#103025)
  - Fix xz and lzip test skip for when tools are not installed
  - Enable verbose testing for CPAN-testers
  - Use proper temp dir instead of t/temp
  - Consolidate issue tracking at rt.cpan.org
- License changed to GPLv2
- Remove file installed by accident (CPAN RT#103482)

* Mon Mar 23 2015 Paul Howarth <paul@city-fan.org> - 1.5100-1
- Update to 1.5100
  - Moved code to github
  - Added xz support (CPAN RT#68286)
  - Added lzip support (http://sourceforge.net/p/grepmail/patches/8/)
  - Added POD test
  - Fixed hang in pure Perl implementation for a malformed mbox file scenario
  - Fixed $OLDSTDERR used only once warning (CPAN RT#58053)
  - Fixed enabling of warnings (CPAN RT#79898)
  - Fixed a division by zero error for malformed mbox files that start with a
    newline (CPAN RT#69469)
  - Fix bug in M::M::Perl documentation
  - Add more cache file validation
- Classify buildreqs by usage
- Add patch to fix build error (CPAN RT#103025)
- Use %%license where possible
- Drop %%defattr, redundant since rpm 4.4

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5002-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5002-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.5002-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5002-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5002-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.5002-11
- Perl 5.16 rebuild

* Sat Jan  7 2012 Paul Howarth <paul@city-fan.org> - 1.5002-10
- Fedora 17 Mass Rebuild

* Tue Jun 28 2011 Paul Howarth <paul@city-fan.org> - 1.5002-9
- Fix provides filter to work with rpm 4.9 onwards
- Nobody else likes macros for commands

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.5002-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.5002-6
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue Jun  1 2010 Paul Howarth <paul@city-fan.org> 1.5002-5
- Fix used-only-once warning that breaks grepmail with perl 5.12.0

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.5002-4
- Mass rebuild with perl-5.12.0

* Fri Feb 19 2010 Paul Howarth <paul@city-fan.org> 1.5002-3
- Fix versioned provides for perl modules
- Use %%{_fixperms} macro instead of our own %%{__chmod} incantation

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 1.5002-2
- Rebuild against perl 5.10.1

* Wed Sep  2 2009 Paul Howarth <paul@city-fan.org> 1.5002-1 
- Update to 1.5002 
  - perl 5.10 patch upstreamed 
  - disable the grep interface, known to be buggy 
  - fix infinite loop in emails of less than 200 characters (CPAN RT#33493) 
  - update Makefile.PL for versions of Module::Install > 0.88 
  - instead of returning an error for an empty mailbox, a valid mailbox is 
    returned that immediately fails the end_of_mailbox check (CPAN RT#43665) 
  - fix missing "m" modifier issue exposed by Perl 5.10 (CPAN RT#33004) 
  - added some debugging information for the "cache data not validated" error 
  - fix an off-by-one error that could cause warnings about undefined values 
- BuildRequire perl(Test::More) and perl(Text::Diff) 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Paul Howarth <paul@city-fan.org> 1.5000-6
- Project upstream has moved from Sourceforge to Google Code but Google Code
  site is content-free so use standard CPAN URLs instead

* Sat Feb  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5000-5
- Fix for perl 5.10 (Andreas König)

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5000-4
- Rebuild for new perl

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 1.5000-3
- Clarify license as GPL (unspecified version)

* Thu Mar  8 2007 Paul Howarth <paul@city-fan.org> 1.5000-2
- Buildrequire perl(ExtUtils::MakeMaker)

* Tue Feb 27 2007 Paul Howarth <paul@city-fan.org> 1.5000-1
- Update to 1.5000
- Fix argument order for find with -depth
- Permission fixes no longer needed in %%prep
- Buildreq various utils for running test suite

* Fri Aug 25 2006 Paul Howarth <paul@city-fan.org> 1.4005-1
- Update to 1.4005

* Wed Jul 12 2006 Paul Howarth <paul@city-fan.org> 1.4004-1
- Update to 1.4004

* Mon May 22 2006 Paul Howarth <paul@city-fan.org> 1.4003-1
- Update to 1.4003

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> 1.4002-2
- Rebuild

* Fri Feb 10 2006 Paul Howarth <paul@city-fan.org> 1.4002-1
- Update to 1.4002
- Don't use macros in build-time command paths, hardcode them instead
- Add dependency on /usr/bin/diff
- Tzip support removed upstream

* Wed Oct 12 2005 Paul Howarth <paul@city-fan.org> 1.4001-1
- Fedora Extras submission
