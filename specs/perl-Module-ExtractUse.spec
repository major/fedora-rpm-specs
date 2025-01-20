Name:           perl-Module-ExtractUse
Version:        0.345
Release:        7%{?dist}
Summary:        Find out which modules are used
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-ExtractUse
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-ExtractUse-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.37
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pod::Strip)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(UNIVERSAL::require)
# Dependencies

%description
Module::ExtractUse is basically a Parse::RecDescent grammar to parse Perl
code. It tries very hard to find all modules (whether pragmas, Core, or
from CPAN) used by the parsed code.

%prep
%setup -q -n Module-ExtractUse-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test
./Build test --test_files="xt/*.t"

%files
%license LICENSE
%doc Changes README example/
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/ExtractUse.pm
%dir %{perl_vendorlib}/Module/ExtractUse/
%{perl_vendorlib}/Module/ExtractUse/Grammar.pm
%{_mandir}/man3/Module::ExtractUse.3*
%{_mandir}/man3/Module::ExtractUse::Grammar.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.345-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.345-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.345-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.345-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.345-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.345-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Paul Howarth <paul@city-fan.org> - 0.345-1
- Update to 0.345 (rhbz#2161364)
  - Auto generate meta_yml_has_provides experimental Kwalitee
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.344-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.344-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.344-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep  6 2021 Paul Howarth <paul@city-fan.org> - 0.344-1
- Update to 0.344
  - Fixed some spelling errors in the Pod
- Use %%license unconditionally

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.343-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.343-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.343-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.343-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.343-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.343-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.343-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.343-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.343-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Paul Howarth <paul@city-fan.org> - 0.343-1
- Update to 0.343
  - Mention Perl::PrereqScanner modules family

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.342-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.342-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.342-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Paul Howarth <paul@city-fan.org> - 0.342-1
- Update to 0.342
  - Escape left (and right) braces to silence deprecation warnings
    (CPAN RT#124146)
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.341-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.341-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.341-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.341-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.341-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Paul Howarth <paul@city-fan.org> - 0.341-1
- Update to 0.341
  - load_first_existing_class() is now working
  - Class::Load::load_class(), try_load_class() and load_optional_class() are
    working
  - Detect uses of Module::Runtime
  - Include extractuse as provided by Jonathan Yu in example/
  - Linkify POD modules, mention Module::Extract::Use to resolve CPAN RT#45571
  - Fix 20_parse_self.t; version.pm is no longer used
- Classify buildreqs by usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 12 2014 Paul Howarth <paul@city-fan.org> - 0.33-1
- Update to 0.33
  - Added base() handling to no
  - Support 'no MODULE' etc. (CPAN RT#94305)
  - Typo fix
  - Ignore __DATA|END__ sections (CPAN RT#88969)
  - Ignore use/require method calls

* Wed Sep  4 2013 Paul Howarth <paul@city-fan.org> - 0.32-1
- Update to 0.32
  - Don't include cached results
  - Fix handling module beginning with v and pragma with version
  - Recognize "use parent"

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.31-2
- Perl 5.18 rebuild

* Fri May 31 2013 Paul Howarth <paul@city-fan.org> - 0.31-1
- Update to 0.31
  - Support use Foo::Bar (); etc. (CPAN RT#50723)
  - "use" after statement with trailing comment was ignored (CPAN RT#71761)
  - Fixed the Pod::Simple encoding issue
  - Fix incorrect regexp (ref gh-5)
  - Avoid regex features introduced only in later perl (close gh-5)
  - Use plan() instead of done_testing() (ref gh-5)
  - Add support for bareword leading hyphyen, in-place arrayref and hashref
  - Proper version number for older releases in Changes file

* Thu Apr 18 2013 Paul Howarth <paul@city-fan.org> - 0.30-1
- Update to 0.30
  - Add accessors and tests for _in_eval/_out_of_eval
  - Reworked 80_failing.t to TODO tests
  - Added more require-in-string corner test cases
  - Fix the case for eval["']expr["'] and add regression tests

* Mon Feb 25 2013 Paul Howarth <paul@city-fan.org> - 0.29-1
- Update to 0.29
  - Fixed regex to filter use/require (CPAN RT#83569)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Paul Howarth <paul@city-fan.org> - 0.28-1
- Update to 0.28
  - Whitespace in use base is valid

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.27-3
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.27-2
- Round Module::Build version to 2 digits

* Fri Mar 23 2012 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27
  - Removed Test::NoWarnings from a t/23_universal_require.t because it upsets
    the (manual) plan if the tests are skipped

* Thu Mar 22 2012 Paul Howarth <paul@city-fan.org> - 0.25-1
- Update to 0.25
  - Autogenerate the grammar during ./Build (CPAN RT#74879)
  - Added $VERSION to into Module::ExtractUse::Grammar (CPAN RT#75342)
  - Require at least version 1.967009 of Parse::RecDescent (CPAN RT#75130)
  - Fix typos (CPAN RT#75115)
  - Switched to Dist::Zilla
- Drop grammar recompilation, no longer needed
- BR: perl(Test::More)
- Bump perl(Module::Build) version requirement to 0.3601
- Bump perl(Parse::RecDescent) version requirement to 1.967009
- Drop perl(Pod::Strip) and perl(Test::Deep) version requirements
- Package manpage for Module::ExtractUse::Grammar

* Mon Mar 19 2012 Paul Howarth <paul@city-fan.org> - 0.24-3
- Recompile the grammar to work with the new Parse::RecDescent (CPAN RT#74879)

* Tue Mar  6 2012 Paul Howarth <paul@city-fan.org> - 0.24-2
- BR: perl(Carp) and perl(version)
- Don't use macros for commands
- Make %%files list more explicit
- Package example
- Drop %%defattr, redundant since rpm 4.4

* Mon Feb 13 2012 Daniel P. Berrange <berrange@redhat.com> - 0.24-1
- Update to 0.24, removing previous grammar hack (rhbz #789976)

* Sat Feb  4 2012 Daniel P. Berrange <berrange@redhat.com> - 0.23-11
- Regenerate grammar for new Parse::RecDescent (rhbz#786849)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.23-9
- Perl mass rebuild

* Thu Mar 17 2011 Paul Howarth <paul@city-fan.org> - 0.23-8
- Reinstate %%check

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-6
- Rebuild to fix problems with vendorarch/lib (#661697)

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-5
- Mass rebuild with perl-5.12.0 

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.23-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 Daniel P. Berrange <berrange@redhat.com> - 0.23-1
- Update to 0.23 release

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.22-2
- rebuild for new perl

* Fri Dec 21 2007 Daniel P. Berrange <berrange@redhat.com> 0.22-1.fc9
- Specfile autogenerated by cpanspec 1.73.
