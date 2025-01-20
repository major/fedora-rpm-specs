Name:		perl-Test-Modern
Version:	0.013
Release:	30%{?dist}
Summary:	Precision testing for modern perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Modern
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Modern-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.000
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter::Tiny) >= 0.030
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::File) >= 1.08
BuildRequires:	perl(IO::Handle) >= 1.21
BuildRequires:	perl(Import::Into) >= 1.002000
BuildRequires:	perl(Module::Runtime) >= 0.012
BuildRequires:	perl(Moose::Util)
BuildRequires:	perl(Mouse::Util)
BuildRequires:	perl(Role::Tiny)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::API) >= 0.004
BuildRequires:	perl(Test::Deep) >= 0.111
BuildRequires:	perl(Test::Fatal) >= 0.007
BuildRequires:	perl(Test::LongString) >= 0.15
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Version)
BuildRequires:	perl(Test::Warnings) >= 0.009
BuildRequires:	perl(Try::Tiny) >= 0.15
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Data::Dumper)
# Optional Test Requirements
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Moose) >= 2.0600
BuildRequires:	perl(namespace::clean)
# Dependencies
Requires:	perl(B)
Requires:	perl(Moose::Util)
Requires:	perl(Mouse::Util)
Requires:	perl(Role::Tiny)
Requires:	perl(Scalar::Util)
Requires:	perl(Test::LongString) >= 0.15
Requires:	perl(Test::Pod)
Requires:	perl(Test::Pod::Coverage)
Requires:	perl(Test::Version)

%description
Test::Modern provides the best features of Test::More, Test::Fatal,
Test::Warnings, Test::API, Test::LongString, and Test::Deep, as well as ideas
from Test::Requires, Test::DescribeMe, Test::Moose, and Test::CleanNamespaces.

Test::Modern also automatically imposes strict and warnings on your script,
and loads IO::File (much of the same stuff Modern::Perl does).

%prep
%setup -q -n Test-Modern-%{version}

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
%license COPYRIGHT LICENSE
%doc Changes CONTRIBUTING CREDITS README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Modern.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-23
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-20
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov  5 2019 Paul Howarth <paul@city-fan.org> - 0.013-15
- Spec tidy-up
  - Use author-independent source URL
  - Specify all build dependencies
  - Simplify find command using -delete
  - Fix permissions verbosely

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-2
- Perl 5.22 rebuild

* Thu Oct  9 2014 Paul Howarth <paul@city-fan.org> - 0.013-1
- Update to 0.013
  - Add 'test recommends' dependencies on a few modules

* Tue Sep 30 2014 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - does_ok no longer calls the internal Test::Builder '_try' method

* Thu Sep 18 2014 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - version_all_same now copes better with undef versions
- Use %%license

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.20 rebuild

* Fri Jul 18 2014 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Fix the behaviour of the BAIL_OUT called within object_ok
  - Add is_fastest, inspired by Test::Benchmark

* Mon Jul  7 2014 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - Added: Implement an `-internet` feature allowing test scripts to declare
    they need access to the Internet; this honours the NO_NETWORK_TESTS
    environment variable
  - Precautionary bypassing of prototype for internal calls to
    `Test::More::subtest`
  - Updated: Improved `namespaces_clean` implementation along the same lines
    as recent changes to Test::CleanNamespaces

* Thu Jun 19 2014 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Package with a newer Dist::Inkt to provide a better Makefile.PL (copes
    better with missing CPAN::Meta::Requirements)
- CONTRIBUTING file is now licensed CC-BY-SA or GPL+ or Artistic so we can
  make the whole package GPL+ or Artistic now

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Paul Howarth <paul@city-fan.org> - 0.007-1
- Update to 0.007
  - Fix for warnings being generated deep in the bowels of File::Spec
    (CPAN RT#94383)

* Fri Apr  4 2014 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - EXPERIMENTALLY provide Test::Lib-like behavior, and a related -lib export
    tag
  - Support an environment variable PERL_TEST_MODERN_ALLOW_WARNINGS to allow
    end-users to skip running end warnings tests
  - Added shouldnt_warn function
- Add upstream workaround for warnings generated in File::Spec

* Wed Mar 26 2014 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Support Perl 5.6.1+

* Tue Mar 25 2014 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - EXPERIMENTALLY provide Test::Pod functions
  - EXPERIMENTALLY provide Test::Pod::Coverage functions
  - EXPERIMENTALLY provide Test::Version functions
  - Improve the implementation of -without, including better compatibility with
    pre-5.12 versions of Perl

* Tue Mar 25 2014 Paul Howarth <paul@city-fan.org> - 0.003-1
- Update to 0.003
  - Provide a Test::Without::Module-like feature (-without)
  - Load IO::File and IO::Handle like Modern::Perl does

* Thu Mar 20 2014 Paul Howarth <paul@city-fan.org> - 0.002-3
- Incorporate feedback from package review (#1078950)
  - BR: perl for build process
  - BR: perl(base) for test suite
  - BR:/R: perl(Moose::Util), perl(Mouse::Util) and perl(Role::Tiny) for
    runtime
  - CONTRIBUTING file is CC-BY-SA
    (https://github.com/tobyink/p5-test-modern/issues/1)

* Thu Mar 20 2014 Paul Howarth <paul@city-fan.org> - 0.002-2
- Sanitize for Fedora submission

* Fri Mar 14 2014 Paul Howarth <paul@city-fan.org> - 0.002-1
- Initial RPM version
