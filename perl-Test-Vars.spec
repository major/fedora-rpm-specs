Name:		perl-Test-Vars
Version:	0.015
Release:	9%{?dist}
Summary:	Detects unused variables
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Vars
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Vars-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter >= 4:5.10.0
BuildRequires:	perl(Module::Build::Tiny) >= 0.035
BuildRequires:	sed
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(B)
BuildRequires:	perl(constant)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(IO::Pipe)
BuildRequires:	perl(List::Util) >= 1.33
BuildRequires:	perl(parent)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(warnings)
# ===================================================================
# Test suite requirements
# ===================================================================
BuildRequires:	perl(feature)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Tester)
# ===================================================================
# Optional test requirements
# ===================================================================
%if !0%{?rhel:1} && !0%{?perl_bootstrap:1}
BuildRequires:	perl(Moose::Role)
%endif
BuildRequires:	perl(Test::Output)
# ===================================================================
# Author/Release test requirements
# ===================================================================
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Synopsis)
# ===================================================================
# Runtime dependencies
# ===================================================================
# (none)

%description
Test::Vars finds unused variables in order to keep the source code tidy.

%prep
%setup -q -n Test-Vars-%{version}

# Placate rpmlint about script interpreters in examples
sed -i -e '1s|^#!perl|#!/usr/bin/perl|' example/*.t

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test
prove -Ilib $(echo $(find xt/ -name '*.t'))

%files
%license LICENSE
%doc Changes README.md example/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Vars.3*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-7
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-3
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-2
- Perl 5.34 rebuild

* Wed Apr 21 2021 Paul Howarth <paul@city-fan.org> - 0.015-1
- Update to 0.015
  - Support use of lexical subroutines (GH#41)
  - Account for subroutines stored directly in the stash in 5.27.6+ (GH#34)
- Use %%license unconditionally

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-16
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-15
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Paul Howarth <paul@city-fan.org> - 0.014-13
- Use author-independent source URL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-11
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-10
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-7
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-2
- Perl 5.26 rebuild

* Wed Apr 12 2017 Paul Howarth <paul@city-fan.org> - 0.014-1
- Update to 0.014
  - Fixed a bug where false positives were reported for some code constructs
    where a variable was used on the right side of an lvalue-expression
- Drop redundant Group: tag

* Fri Mar 17 2017 Paul Howarth <paul@city-fan.org> - 0.013-1
- Update to 0.013
  - Worked around a very weird bug with B's handling of multideref aux_list
    values on 5.22 and 5.24. This could cause a warning like "Use of
    uninitialized value $i in array element at lib/Test/Vars.pm line ..." when
    testing certain Perl constructs for unused vars; this appears to be fixed
    in blead's B

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - On Perl 5.22+, variables used in a substitution operator
    ($foo =~ s/foo/bar/) would be ignored (GH#28)

* Mon Oct 17 2016 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - Fixed tests to pass on Windows (GH#26 and GH#27)
- This release by DROLSKY → update source URL

* Fri Jul  1 2016 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Fix for pp_match in Perl 5.22+ (GH#23)
- This release by GFUJI → update source URL

* Sun May 22 2016 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - On recent Perls (5.22 and 5.24, maybe more) this module could detect an
    unused variable named "$"; this was a bogus false positive, as opposed to
    just a missing variable name in the output (GH#22)
  - Fixed tests to use File::Spec->catfile to generate paths so that tests pass
    on Windows (based on GH#20)
- Switch to Module::Build::Tiny flow
- BR: perl-generators

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - In some corner cases, Test::Vars would try to look inside the body of a
    stub sub ("sub foo;") and then blow up; this could be triggered by
    declaring a stub sub and then an attribute with a reader of the same name
    in a Moose::Role, for example

* Wed Aug 19 2015 Paul Howarth <paul@city-fan.org> - 0.007-1
- Update to 0.007
  - Fix tests with threaded Perl 5.22+

* Wed Aug 19 2015 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - This module now calls Test::Builder->diag and ->note _after_ calling ->ok;
    this is more in line with how most test modules work
  - Added a new exported sub, test_vars(), which does not output TAP; this is
    useful for integrating this module with things like Code::TidyAll
- This release by DROLSKY → update source URL
- Use %%license where possible

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.005-3
- Perl 5.18 rebuild

* Mon Jul 01 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-2
- Update dependencies

* Fri May 31 2013 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Use skip_all instead of planning 0 tests (#4)

* Sun May  5 2013 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - Re-package with Module::Build
  - Remove an unnecessary use of smart match operator
- Switch to Module::Build flow
- Classify buildreqs by usage
- Drop Test::Spelling requirement, no longer used

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-2
- Specify all dependencies.

* Wed Oct 10 2012 Paul Howarth <paul@city-fan.org> - 0.002-1
- Update to 0.002
  - Fix compatibility with Perl 5.16 (CPAN RT#72133)
- Drop upstreamed patch for 5.16 compatibility

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Paul Howarth <paul@city-fan.org> - 0.001-5
- Fix compatibility with Perl 5.16 (CPAN RT#72133)
- Don't need to remove empty directories from buildroot

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.001-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug  8 2011 Paul Howarth <paul@city-fan.org> - 0.001-2
- Sanitize for Fedora submission
- Clean up for modern rpm

* Mon Aug  8 2011 Paul Howarth <paul@city-fan.org> - 0.001-1
- Initial RPM version
