# This module usually ships with version numbers having two digits after the decimal point
%global cpan_version 1.995
%global rpm_version 1.99.5

Summary:	Test file attributes through Test::Builder
Name:		perl-Test-File
Version:	%{rpm_version}
Release:	2%{?dist}
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-File
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-File-%{cpan_version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(ExtUtils::Manifest) >= 1.21
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Test::Builder) >= 1.001006
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More) >= 1
BuildRequires:	perl(utf8)
BuildRequires:	perl(version) >= 0.86
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
# (none)

%description
This module provides a collection of test utilities for file attributes.

Some file attributes depend on the owner of the process testing the file
in the same way the file test operators do.

%prep
%setup -q -n Test-File-%{cpan_version}

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
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::File.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Apr 14 2025 Paul Howarth <paul@city-fan.org> - 1.99.5-1
- Update to 1.995
  - Require a newer version.pm for v5.10.1 tests

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan  3 2025 Paul Howarth <paul@city-fan.org> - 1.99.4-1
- Update to 1.994
  - Refresh distro and move to BRIANDFOY
- Package new file SECURITY.md

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug  8 2023 Paul Howarth <paul@city-fan.org> - 1.99.3-4
- Fix FTBFS in Rawhide due to %%rpmversion macro becoming an rpm built-in
  (rhbz#2229872)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Paul Howarth <paul@city-fan.org> - 1.99.3-1
- Update to 1.993
  - Try harder to check for symlinks on Windows by stealing some code from
    Win32:: (GH#36)
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.99.2-2
- Perl 5.36 rebuild

* Wed Feb 16 2022 Paul Howarth <paul@city-fan.org> - 1.99.2-1
- Update to 1.992
  - Fix race condition in tests for mtime (GH#29)

* Fri Jan 21 2022 Paul Howarth <paul@city-fan.org> - 1.99.1-1
- Update to 1.991
  - Enforce text files in some functions, as warned in GH#18
  - Change up some diag messages:
    - Lowercase first letter
    - Not ! at end
    - Use "file" instead of "filename"
    If you were matching on those, you may need to update your patterns

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.44.8-2
- Perl 5.34 rebuild

* Fri Mar  5 2021 Paul Howarth <paul@city-fan.org> - 1.44.8-1
- Update to 1.448
  - Try handling all-numeric user and group names (GH#26)

* Thu Feb 25 2021 Paul Howarth <paul@city-fan.org> - 1.44.7-1
- Update to 1.447
  - Trying harder to get the tests to pass on Cygwin

* Sun Feb 21 2021 Paul Howarth <paul@city-fan.org> - 1.44.6-1
- Update to 1.446
  - Better Cygwin detection

* Tue Feb 16 2021 Paul Howarth <paul@city-fan.org> - 1.44.5-1
- Update to 1.445
  - Get the tests to pass under Cygwin (GH#17)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Paul Howarth <paul@city-fan.org> - 1.44.4-1
- Update to 1.444
  - Change the file_writeable_ok tests to file_writable_ok, which is the
    correct spelling; the old names work but now warn to use the new name
  - Some updates to refresh the tests
  - Start mirroring Test2::Tools::File so we support the same names
  - Deprecated directories in tests appropriate for only plain files; it's a
    diag() message now but will be a test failure later
  - Merge some test additions from Desmond Daignault (GH#20)
  - Remove Travis, add GitHub actions
  - Add file_is_symlink_not_ok
- License changed to Artistic 2.0
- Use author-independent source URL
- Use %%{make_build} and %%{make_install}

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.44.3-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.44.3-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.44.3-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.44.3-2
- Perl 5.26 rebuild

* Mon Apr 17 2017 Paul Howarth <paul@city-fan.org> - 1.44.3-1
- Update to 1.443
  - Found another relative path require issue:
    http://blogs.perl.org/users/ryan_voots/2017/04/trials-and-troubles-with-changing-inc.html
  - This is another attempt at avoiding failures from the v5.26 removal of . from @INC
- Drop redundant Group: tag

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Paul Howarth <paul@city-fan.org> - 1.44.2-1
- Update to 1.442
  - Fix for missing . in @INC; this relates to CVE-2016-1238
    (https://github.com/briandfoy/test-file/issues/14)
- Split rpm and upstream versioning
- Use features from recent EUMM to simplify %%install section

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul  6 2015 Paul Howarth <paul@city-fan.org> - 1.44-1
- Update to 1.44
  - Fix problem with META* specifying requirements (CPAN RT#105210)
  - Don't install README.pod
  - check file_mode_has tests for Windows
  - Fix file_has_* tests to work on Windows (GH#13)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-2
- Perl 5.22 rebuild

* Wed Sep 24 2014 Paul Howarth <paul@city-fan.org> - 1.41-1
- Update to 1.41
  - Uncomment accidentally commented symlink_target_is_absolute_ok
  - Add mtime test functions (GH#8)
  - Allow tests to run in parallel (CPAN RT#89908, CPAN RT#91862)
  - Fix up tests for UTF-8 checks
- This release by BDFOY → update source URL
- Classify buildreqs by usage
- Use %%license

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  2 2014 Paul Howarth <paul@city-fan.org> - 1.36-1
- Update to 1.36
  - Fix bad line counts on latest dev version of Perl (CPAN RT#89849)

* Thu Oct 10 2013 Paul Howarth <paul@city-fan.org> - 1.35-1
- Update to 1.35
  - Don't distribute MYMETA.* (CPAN RT#89175)
  - Add dir_exists_ok and dir_contains_ok
  - Add file_contains_* functions
- Specify all dependencies

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.34-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Paul Howarth <paul@city-fan.org> - 1.34-1
- Update to 1.34
  - Added dir_exists_ok and dir_contains_ok
  - Added file_contains_like and file_contains_unlike
  - Fixed a few grammatical errors in POD
  - Added some SKIP blocks to avoid test failures when running as root
  - Fixed qr//mx patterns to work with older Perls (CPAN RT#74365)
  - Fixed incorrect spelling of "privileges" in SKIP blocks (CPAN RT#74483)
  - Skip testing of symlinks on Windows (CPAN RT#57682)
  - Fixed automatically generated test name for owner_isnt (CPAN RT#37676)
  - Fixed problem in MANIFEST file (CPAN RT#37676)
  - Fixed problem in links.t (CPAN RT#76853)
- This release by BAREFOOT -> update source URL
- BR: perl(base), perl(Exporter) and perl(File::Spec)
- Bump perl(Test::Manifest) version requirement to 1.21
- Bump perl(Test::More) version requirement to 0.88
- Drop perl(ExtUtils::MakeMaker) version requirement
- BR: at least version 1.00 of perl(Test::Pod)
- Drop buildreq perl(Test::Prereq) since t/prereq.t isn't in the test_manifest
- Package LICENSE file
- Expand %%summary and %%description
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands
- Make %%files list more explicit
- Use %%{_fixperms} macro rather than our own chmod incantation
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.29-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.29-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue Jun 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.29-1
- update to 1.29

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.25-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.25-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.25-1
- Upstream update.

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-3
- helps if you upload new source

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-1
- bump to 1.22
- fix license tag

* Sat Sep 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.16-1
- Update to 1.16.

* Fri May 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.15-1
- Update to 1.15.

* Wed May 03 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- First build.
