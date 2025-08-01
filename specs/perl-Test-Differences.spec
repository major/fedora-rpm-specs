# TODO: BR: optional test dependency Unknown::Values if it becomes available

Name:           perl-Test-Differences
%global cpan_version 0.72
Version:        %(LANG=C printf "%.4f" %{cpan_version})
Release:        2%{?dist}
Summary:        Test strings and data structures and show differences if not OK
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Differences
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Differences-%{cpan_version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper) >= 2.126
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Diff) >= 1.43
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Capture::Tiny) >= 0.24
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Explicit Dependencies
Requires:       perl(B::Deparse)
Requires:       perl(Text::Diff) >= 1.43

%description
When the code you're testing returns multiple lines, records or data
structures and they're just plain wrong, an equivalent to the Unix
diff utility may be just what's needed.

%prep
%setup -q -n Test-Differences-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Differences.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul  7 2025 Paul Howarth <paul@city-fan.org> - 0.7200-1
- Update to 0.72
  - Changes to tests only, so tests pass when you have a new perl that supports
    bools, but an old Data::Dumper that doesn't
- Use %%{make_build} and %%{make_install}

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 20 2024 Michal Josef Špaček <mspacek@redhat.com> - 0.7100-5
- Fix version handling for build with different locales set
  `printf "%.4f" 0.71` has different results e.g. for cs_CZ.UTF-8 vs C

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 13 2023 Paul Howarth <paul@city-fan.org> - 0.7100-1
- Update to 0.71
  - Document and test different behavior regarding Booleans in perl 5.38.0
    compared to earlier versions (GH#21)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul  8 2023 Paul Howarth <paul@city-fan.org> - 0.7000-1
- Update to 0.70
  - Stop pointless use of taint-mode in tests, so tests pass when perl is
    built without taint support

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6900-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6900-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.6900-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan  8 2022 Paul Howarth <paul@city-fan.org> - 0.6900-1
- Update to 0.69
  - Special-case Unknown::Values objects in comparisons, as it's better to spit
    out a diagnostic failure than to just die
  - Correct misleading Unicode doco

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6800-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.6800-2
- Perl 5.34 rebuild

* Wed May 19 2021 Paul Howarth <paul@city-fan.org> - 0.6800-1
- Update to 0.68
  - Revert undocumented change that was causing unreasonably verbose output
    (GH#5)
  - Improve documentation about text vs. data mode and eq_or_diff_{text,data}
    (GH#8)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6700-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6700-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6700-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6700-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6700-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.6700-2
- Perl 5.30 rebuild

* Thu Mar  7 2019 Paul Howarth <paul@city-fan.org> - 0.6700-1
- Update to 0.67
  - Correctly compare subroutine references

* Thu Feb 28 2019 Paul Howarth <paul@city-fan.org> - 0.6600-1
- Update to 0.66
  - Fix tests on Windows

* Wed Feb 20 2019 Paul Howarth <paul@city-fan.org> - 0.6500-1
- Update to 0.65
  - Canonical repo is now
    https://github.com/DrHyde/perl-modules-Test-Differences
  - Fix discrepancies in copyright notices
  - Make the tests more consistent
  - Add unicode tests
  - Fix whitespace issue in tests when using recent Test::More in verbose mode
  - Get rid of Build.PL, just use Makefile.PL
- Drop redundant buildroot cleaning in %%install section
- Simplify find command using -delete

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6400-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6400-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.6400-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6400-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6400-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6400-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6400-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 0.6400-4
- Adjust package version computation to SRPM build root witout perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.6400-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Paul Howarth <paul@city-fan.org> - 0.6400-1
- Update to 0.64
  - Bump dependency version for Text::Diff to avoid a buggy release
  - Make tests pass with relocatable perl (CPAN RT#103133)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6300-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.6300-2
- Perl 5.22 rebuild

* Fri Nov 21 2014 Paul Howarth <paul@city-fan.org> - 0.6300-1
- Update to 0.63
  - Make '' and undef not equal
  - Made Data::Dumper minimum version 2.126 to resolve CPAN RT#60798
  - Allow an option to override Sortkeys in C<eq_or_diff>
  - Unnumbered tests; there's no point to them
  - Document the Text::Diff unicode fix
  - Add ability to customize 'Got' and 'Expected' column headers
  - Minor doco-fixes
  - Remove use of flatten, always use Data::Dumper for saner, more readable
    output (CPAN RT#95446)
- This release by DCANTRELL → update source URL
- Drop %%defattr, redundant since rpm 4.4
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't need to remove empty directories from the buildroot

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.5000-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.5000-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.5000-7
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5000-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.5000-3
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Jul 08 2010 Iain Arnell <iarnell@gmail.com> 0.500-2
- explicitly require perl(Text::Diff)

* Tue Jun 29 2010 Paul Howarth <paul@city-fan.org> - 0.5000-1
- Update to 0.500
  - Add support for all diff styles supplied by Text::Diff (CPAN RT#23579)
  - Add Build.PL
  - Convert to universally use Test::More instead of Test
  - Convert to modern Perl distribution.
  - Applied doc suggestion from CPAN RT#24297
  - Fix the { a => 1 } versus { a => '1' } bug (CPAN RT#3029)
- Upstream dropped eg/ docs
- Bump perl(Text::Diff) requirement to 0.35
- BR: perl(Test::Pod) and perl(Test::Pod::Coverage) for extra test cover

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4801-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.4801-4
- rebuild against perl 5.10.1

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4801-3
- fix source url

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4801-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4801-1
- update to 0.4801

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-4
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-2.2
- add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sun May 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.47-2
- Bumping release (repodata checksum inconsistency for previous release).

* Mon May 01 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.47-1
- First build.
