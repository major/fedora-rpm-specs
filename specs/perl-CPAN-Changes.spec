# Extra tests require Test::Pod::Coverage::TrustMe, not yet available in Fedora
%bcond_with perl_CPAN_Changes_enables_extra_test

Name:		perl-CPAN-Changes
Summary:	Read and write Changes files
Version:	0.500005
Release:	2%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Changes
Source0:	https://cpan.metacpan.org/modules/by-module/CPAN/CPAN-Changes-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Moo) >= 1.006000
BuildRequires:	perl(Moo::Role)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Quote) >= 1.005000
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Types::Standard)
BuildRequires:	perl(version)
BuildRequires:	perl(warnings)
# Script Runtime
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
# Test Suite
BuildRequires:	perl(constant)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.96
# Optional Tests
BuildRequires:	perl(Test::Differences)
# Extra Tests
%if %{with perl_CPAN_Changes_enables_extra_test}
BuildRequires:	findutils
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage::TrustMe) => 0.002000
%endif
# Dependencies
# (none)

%description
It is standard practice to include a Changes file in your distribution. The
purpose of the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

%prep
%setup -q -n CPAN-Changes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_CPAN_Changes_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{_bindir}/tidy_changelog
%{perl_vendorlib}/CPAN/
%{perl_vendorlib}/Test/
%{_mandir}/man1/tidy_changelog.1*
%{_mandir}/man3/CPAN::Changes.3*
%{_mandir}/man3/CPAN::Changes::Entry.3*
%{_mandir}/man3/CPAN::Changes::Group.3*
%{_mandir}/man3/CPAN::Changes::Parser.3*
%{_mandir}/man3/CPAN::Changes::Release.3*
%{_mandir}/man3/CPAN::Changes::Spec.3*
%{_mandir}/man3/Test::CPAN::Changes.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.500005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Apr 18 2025 Paul Howarth <paul@city-fan.org> - 0.500005-1
- Update to 0.500005
  - Fix Test::CPAN::Changes on perl 5.10 without upgrading version.pm
- Use %%{make_build} and %%{make_install}

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.500004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.500004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May  3 2024 Paul Howarth <paul@city-fan.org> - 0.500004-1
- Update to 0.500004
  - Fix tests on Windows

* Fri Feb 23 2024 Paul Howarth <paul@city-fan.org> - 0.500003-1
- Update to 0.500003
  - Fix calling ->name on an unnamed group
  - Fix ->set_changes call on groups
- Disable extra tests for now

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.500002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.500002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Paul Howarth <paul@city-fan.org> - 0.500002-1
- Update to 0.500002
  - Full rewrite
    - The new version can parse nested entries to an arbitrary depth, rather
      than just groups
    - It can parse many more formats, and can format the outputs more flexibly;
      this means it can better handle the change logs that actually exist on
      CPAN
  - Parsed releases keep their original order
  - Pass given ChangeLog filename for --check
- Package LICENSE file

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-21
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-18
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-15
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 23 2019 Paul Howarth <paul@city-fan.org> - 0.400002-13
- Avoid optional test dependency perl(Moo) for EPEL builds
- Use author-independent source URL
- Simplify find command using -delete

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.400002-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.400002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Paul Howarth <paul@city-fan.org> - 0.400002-1
- Update to 0.400002
  - Revert whitespace changes that were inadvertantly included in previous
    release
  - Escape curly brackets in test to avoid warning in perl 5.22

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.400001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.400001-2
- Perl 5.22 rebuild

* Tue May 26 2015 Paul Howarth <paul@city-fan.org> - 0.400001-1
- Update to 0.400001
  - Accept either UTF-8 or ISO-8859-1 files and decode them
  - Only treat bracketed text if it is on its own line with no other brackets
  - Bump version.pm prereq to make sure it works properly
  - Let long tokens (like URLs) overflow rather than splitting them into
    multiple lines
  - Don't wrap on non-breaking spaces
  - Clean up packaging
  - Return undef for dates or notes that don't exist
  - Quote meta chars to fix a problem that clobbered dates with timezones due
    to the '+' char (GH #20)
- This release by HAARG → update source URL
- Classify buildreqs by usage

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.20 rebuild

* Mon Jul 28 2014 Paul Howarth <paul@city-fan.org> - 0.30-1
- Update to 0.30:
  - Fix for subclassing CPAN::Changes::Group (GH #23)

* Thu Jul 24 2014 Paul Howarth <paul@city-fan.org> - 0.29-1
- Update to 0.29:
  - Groups are now objects (CPAN::Changes::Group); backwards compatibility
    from hashes should be preserved (GH #22)

* Thu Jun 12 2014 Paul Howarth <paul@city-fan.org> - 0.28-1
- Update to 0.28:
  - Add "SEE ALSO" links to similar modules (CPAN RT#94636)
  - Use perl 5.8-compatible regex

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27:
  - Bump spec version to 0.04
  - Allow non-"word" characters between a Version and a Date

* Fri Nov 22 2013 Paul Howarth <paul@city-fan.org> - 0.26-1
- Update to 0.26:
  - Fix reference issues when adding a release (CPAN RT#90605)

* Wed Oct  9 2013 Paul Howarth <paul@city-fan.org> - 0.25-1
- Update to 0.25:
  - Fix Dist::Zilla date parsing: now puts timezone data in note section
    (Github #17)
  - Move Text::Wrap usage to proper module
  - Typo fix

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 0.23-1
- Update to 0.23:
  - Bump spec version to 0.03
  - Be more strict about what we consider to be a Dist::Zilla-style date
    to avoid false positive matches
  - Update W3CDTF parsing to make the "T" marker optional (CPAN RT#87499)
  - Fix extra whitespace for empty values after version (CPAN RT#87524)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Paul Howarth <paul@city-fan.org> - 0.22-1
- Update to 0.22:
  - Sync module versions (CPAN RT#87455)

* Tue Jul 30 2013 Paul Howarth <paul@city-fan.org> - 0.21-1
- Update to 0.21:
  Spec Changes:
  - Bump version to 0.02
  - Added "unknown/dev" release date options (CPAN RT#67705)
  - Added optional release note (CPAN RT#69321)
  - Added another preamble example
  - Added a note about line length
  Code Changes:
  - Require Test::More 0.96 (CPAN RT#84994)
  - Added --check and --help flags to tidy_changelog script
  - Properly parse multi-line preamble
  - Test::CPAN::Changes now warns about parsed dates not in spec-compliant form
  - Handle unknown/dev release dates and release note from new spec
- BR: perl(Pod::Usage)

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.20-2
- Perl 5.18 rebuild

* Thu May  2 2013 Paul Howarth <paul@city-fan.org> - 0.20-1
- Update to 0.20:
  - 'delete_empty_groups' shouldn't erronously delete default group
  - Add tidy_changelog utility script
  - Minor pod fix
- Bump Test::More version requirement to 0.96 (CPAN RT#84994)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-4
- Update dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.19-2
- Perl 5.16 rebuild

* Tue May  1 2012 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19:
  - Test::CPAN::Changes now accepts version entries ending in '-TRIAL'
    (CPAN RT#76882)
  - releases() in CPAN::Changes also accepts entries ending in '-TRIAL'
- Don't need to remove empty directories from buildroot
- Drop %%defattr, redundant since rpm 4.4

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 0.18-2
- Fedora 17 mass rebuild

* Tue Oct 18 2011 Paul Howarth <paul@city-fan.org> - 0.18-1
- Update to 0.18:
  - Expand changes_file_ok() to accept arguments so that a specific version may
    be checked
  - Add $VERSION to Test::CPAN::Changes so it plays nice with the toolchain
    e.g. Module::Install::AuthorRequires

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.17-2
- Perl mass rebuild

* Thu Apr 21 2011 Paul Howarth <paul@city-fan.org> - 0.17-1
- Update to 0.17:
  - Eliminate extra whitespace when release data is not defined (CPAN RT#67441)
  - Require version.pm 0.79, which introduced the $LAX regexp (CPAN RT#67613)
  - Add the option to sort groups

* Wed Apr 20 2011 Paul Howarth <paul@city-fan.org> - 0.16-1
- Initial RPM version
