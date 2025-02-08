Name:           perl-TAP-Formatter-JUnit
Version:        0.17
Release:        1%{?dist}
Summary:        Harness output delegate for JUnit output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TAP-Formatter-JUnit
Source0:        https://cpan.metacpan.org/modules/by-module/TAP/TAP-Formatter-JUnit-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(TAP::Formatter::Console)
BuildRequires:  perl(TAP::Formatter::Console::Session)
BuildRequires:  perl(XML::Generator)
# Script Runtime
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(TAP::Parser::Aggregator)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(TAP::Harness) >= 3.12
BuildRequires:  perl(Test::DiagINC)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::XML)
BuildRequires:  perl(version)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Runtime
Requires:       perl(TAP::Formatter::Console)
Requires:       perl(TAP::Formatter::Console::Session)

%description
This module provides JUnit output formatting for TAP::Harness (a replacement
for Test::Harness.

%prep
%setup -q -n TAP-Formatter-JUnit-%{version}

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
%doc Changes README
%{_bindir}/tap2junit
%{perl_vendorlib}/TAP/
%{_mandir}/man1/tap2junit.1*
%{_mandir}/man3/TAP::Formatter::JUnit.3*
%{_mandir}/man3/TAP::Formatter::JUnit::Result.3*
%{_mandir}/man3/TAP::Formatter::JUnit::Session.3*

%changelog
* Thu Feb  6 2025 Paul Howarth <paul@city-fan.org> - 0.17-1
- Update to 0.17 (rhbz#2344113)
  - Bump minimum required Perl to 5.010; XML::Generator v1.11 now requires that
    as a minimum acceptable Perl
  - Skip BAIL_OUT test when using Test::Harness 3.45_01-3.48, as those versions
    contained a bug that resulted in outputting a double summary (GH#15)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May  2 2023 Paul Howarth <paul@city-fan.org> - 0.16-3
- Fix permissions verbosely
- Make %%files list more explicit

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.36 rebuild

* Mon May 09 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-1
- 0.15 bump

* Thu May 05 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-1
- 0.14 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-1
- 0.13 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-2
- Perl 5.22 rebuild

* Wed Oct  8 2014 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11
  - Use "IPC::Run" instead of "IPC::Open2" in tests, to fix problems with tests
    freezing on Windows

* Wed Oct  1 2014 Paul Howarth <paul@city-fan.org> - 0.10-1
- Update to 0.10
  - Switch from "Test::Differences" to "Test::XML", to eliminate failures due
    to differences in ordering of XML attributes (CPAN RT#81552)
  - Use "File::Spec->null()" to get proper path to NULL (CPAN RT#81200,
    CPAN RT#82227)
  - Moved POD tests to "xt/" directory
  - Move timing sensitive tests to "xt/" directory (CPAN RT#69777)
- Classify buildreqs by usage

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Paul Howarth <paul@city-fan.org> - 0.09-7
- Address test failures due to hash order randomization (CPAN RT#81552)
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.09-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Perl 5.16 rebuild

* Fri Jan 27 2012 Daniel P. Berrange <berrange@redhat.com> - 0.09-1
- Update to 0.09 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Daniel P. Berrange <berrange@redhat.com> - 0.08-2
- Updated with suggestions from review (rhbz #752838)

* Mon Nov 07 2011 Daniel P. Berrange <berrange@redhat.com> - 0.08-1
- Specfile autogenerated by cpanspec 1.78.
