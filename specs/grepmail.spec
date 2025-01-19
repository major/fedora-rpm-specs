Summary:	Search mailboxes for a particular email
Name:		grepmail
Version:	5.3111
Release:	22%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/grepmail
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/grepmail-%{version}.tar.gz
Patch0:		grepmail-5.3111-Test-Compile.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode) >= 2.11
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Fcntl) >= 1.03
BuildRequires:	perl(File::HomeDir::Unix)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(PerlIO::encoding)
BuildRequires:	perl(PerlIO::utf8_strict)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Getopt::Std)
BuildRequires:	perl(Mail::Mbox::MessageParser) >= 1.4001
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(Time::Local) >= 1.23
# Test Suite
BuildRequires:	perl(ExtUtils::Command)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More) >= 0.62
BuildRequires:	perl(UNIVERSAL::require)
# Optional Tests
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Dependencies
Requires:	perl(Date::Manip)
Requires:	perl(Date::Parse)
Requires:	perl(Digest::MD5)
Requires:	perl(File::Find)
Requires:	perl(Mail::Mbox::MessageParser) >= 1.4001
Requires:	perl(Time::Local)

%description
Grepmail searches a normal or compressed mailbox for a given regular
expression, and returns those emails that match it. Piped input is allowed,
and date and size restrictions are supported, as are searches using logical
operators.

%prep
%setup -q -n %{name}-%{version}

# Workaround for Test::Compile ≥ 2.0.0
%patch -P 0 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
export TZ=GMT0
make test

%files
%license LICENSE
%doc CHANGES README TODO
%{_bindir}/grepmail
%{_mandir}/man1/grepmail.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Paul Howarth <paul@city-fan.org> - 5.3111-17
- Avoid use of deprecated patch syntax
- Use %%license unconditionally

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.3111-14
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.3111-11
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.3111-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Paul Howarth <paul@city-fan.org> - 5.3111-5
- Workaround for FTBFS with Test::Compile ≥ 2.0.0

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.3111-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Paul Howarth <paul@city-fan.org> - 5.3111-1
- Update to 5.3111
  - Fix test case for binary data
  - Updating META.yml
  - Fix Makefile.PL warning
  - Fix deleting of inc during release process
  - Better fix for AutomatedTester warning

* Mon Jul  9 2018 Paul Howarth <paul@city-fan.org> - 5.3109-1
- Update to 5.3109
  - Switch from File::Slurp to File::Slurper

* Sun Jul  8 2018 Paul Howarth <paul@city-fan.org> - 5.3108-1
- Update to 5.3108
  - Check in standard tests, including one that skips the compile check on
    Windows
  - Attempt to be more compatible with CPAN testing, which apparently doesn't
    support symlinks
  - Disable "check redirect to input file" feature on Windows, where apparently
    it doesn't work

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 5.3105-2
- Perl 5.28 rebuild

* Tue Jul  3 2018 Paul Howarth <paul@city-fan.org> - 5.3105-1
- Update to 5.3105
  - Add standard tests
  - Search headers of attachments, such as filename
  - Detect when someone accidentally makes STDOUT or STDERR also an input file
  - Fix compatibility issue with newer versions of perl, which remove "." from
    @INC
- Simplify find command using -delete
- Drop buildroot cleaning in %%install section
- Drop legacy Group: tag

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.3104-11
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3104-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3104-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.3104-8
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.3104-7
- Fix building on Perl without '.' in @INC

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.3104-5
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.3104-2
- Perl 5.22 rebuild

* Sun May  3 2015 Paul Howarth <paul@city-fan.org> - 5.3104-1
- Update to 5.3104
  - Clarify licensing terms
  - Don't install private Module::Install extension (CPAN RT#103482)
  - Move verbose testing to a private module, and implement it in a way that
    doesn't require editing the Makefile after it is generated
  - Require File::Slurp instead of including it, to avoid potential problems
    like this:
    http://www.cpantesters.org/cpan/report/86a0145a-e52b-11e4-a1d1-8536eb4f9f07
  - Miscellaneous fixes for Windows compatibility, including weaking the
    invalid mailbox test so that it only looks for output from grepmail, and
    not any "broken pipe" message from the OS

* Mon Apr 13 2015 Paul Howarth <paul@city-fan.org> - 5.3102-1
- Update to 5.3102
  - Force the user to upgrade their Time::Local, to work around bugs in the
    stock version that came with old OSes like RHEL 5
    http://www.cpantesters.org/cpan/report/61043eda-dd0e-11e4-abc4-b553e14af301
  - Enable verbose testing for CPAN-testers
  - Consolidate issue tracking at rt.cpan.org
  - Use proper temp dir instead of t/temp
- License changed to GPLv2

* Sun Apr  5 2015 Paul Howarth <paul@city-fan.org> - 5.3101-1
- Update to 5.3101
  - Add explicit include for Module::AutoInstall
    (https://code.google.com/p/grepmail/issues/detail?id=1)
  - Improve the recursive.t test
    (https://code.google.com/p/grepmail/issues/detail?id=2)
  - Add explicit "provides" to META.yml

* Wed Mar 25 2015 Paul Howarth <paul@city-fan.org> - 5.3100-1
- Update to 5.3100
  - Move code to github
  - Fixed a bug where complex -E search patterns containing '\/' would fail to
    match emails properly (http://bugs.debian.org/432083)
  - Add POD test
  - Update tests to use Config{perlpath} for better compatibility with
    automated testing
  - Prevent MakeMaker from recursing into any "old" directory
  - Fix t/invalid_date.t to work even when Date::Manip is not installed
  - Fix t/nonexistent_mailbox.t - broken STDIN does not cause $SIG{PIPE}
  - Added lzip support (http://sourceforge.net/p/grepmail/patches/8/)
  - Added xz support
  - Fix incompatibility with newer versions of Date::Manip (CPAN RT#54621)
- Classify buildreqs by usage
- Drop %%defattr, redundant since rpm 4.4
- Use %%license where possible
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't need to run test suite with LANG=C
- Don't need to remove empty directories from the buildroot

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.3034-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3034-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3034-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 5.3034-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3034-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3034-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 5.3034-9
- Perl 5.16 rebuild

* Sat Jan  7 2012 Paul Howarth <paul@city-fan.org> 5.3034-8
- Fedora 17 Mass Rebuild

* Sat Oct  8 2011 Paul Howarth <paul@city-fan.org> 5.3034-7
- BR/R: perl(Digest::MD5) for improved memory usage
- BR: perl(Carp)
- Nobody else likes macros for commands

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> 5.3034-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 5.3034-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> 5.3034-4
- Mass rebuild with perl-5.12.0

* Mon Feb 15 2010 Paul Howarth <paul@city-fan.org> 5.3034-3
- Fix incompatibilities with Date::Manip 6.x (#564839, CPAN RT#54621)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> 5.3034-2
- Rebuild against perl 5.10.1

* Wed Sep  2 2009 Paul Howarth <paul@city-fan.org> 5.3034-1
- Update to 5.3034
  - fix man page year typo (Debian bug #428973)
  - updated to the latest version of Module::Install
  - added TODO to the distribution
  - fix a bug where grepmail could abort with -L
  - fix a bug in the -R test that could cause a false test failure
  - fix uninitialized variable warnings for emails missing certain headers
- URLs moved back to search.cpan.org
- Buildreq perl(Test::More)
- Buildreq perl(Module::AutoInstall), should have been bundled
- Revert change to t/recursive.t from 5.3033 that causes test failure
- Patch t/nonexistent_mailbox.t to support changed behaviour of
  Mail::Mbox::MessageParser >= 1.5002

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 5.3033-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 5.3033-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.3033-4
- Rebuild for new perl

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 5.3033-3
- Buildrequire perl(ExtUtils::MakeMaker) instead of perl-devel

* Thu Mar  8 2007 Paul Howarth <paul@city-fan.org> 5.3033-2
- Buildrequire perl-devel for Fedora 7 onwards

* Fri Mar  2 2007 Paul Howarth <paul@city-fan.org> 5.3033-1
- Update to 5.3033
- CPAN RT#24341 fixed upstream, remove patch
- Permissions fixes in %%prep no longer needed
- Changed download host from dl.sf.net to downloads.sf.net

* Tue Feb 27 2007 Paul Howarth <paul@city-fan.org> 5.3032-5
- Add patch to fix CPAN RT#24341 (test suite failures with recent
  Mail::Mbox::MessageParser)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 5.3032-4
- FE6 rebuild

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> 5.3032-3
- Don't use macros in command paths, hardcode them instead

* Wed Oct 12 2005 Paul Howarth <paul@city-fan.org> 5.3032-2
- Remove spec file comments about package naming (#170506)

* Wed Oct 12 2005 Paul Howarth <paul@city-fan.org> 5.3032-1
- Fedora Extras submission
