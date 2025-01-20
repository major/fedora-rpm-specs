%bcond_with network_tests

Name:		perl-Test-Kwalitee-Extra
Version:	0.4.0
Release:	25%{?dist}
Summary:	Run Kwalitee tests including optional indicators
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Kwalitee-Extra
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Kwalitee-Extra-v%{version}.tar.gz
Patch0:		Test-Kwalitee-Extra-v0.4.0-CPAN128602.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(MetaCPAN::Client)
BuildRequires:	perl(Module::CoreList) > 2.31
BuildRequires:	perl(Module::CPANTS::Analyse) >= 0.87
BuildRequires:	perl(Module::CPANTS::Kwalitee::Prereq)
BuildRequires:	perl(Module::Extract::Namespaces)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::CPANTS::Kwalitee)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
# Author/Release Tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
# Dependencies
# (none)

%description
CPANTS checks Kwalitee indicators, which is not quality but
automatically-measurable indicators of how good your distribution is.
Module::CPANTS::Analyse calculates Kwalitee but it is not directly applicable
to your module test. CPAN has already had Test::Kwalitee for the test module of
Kwalitee. It is, however, impossible to calculate prereq_matches_use indicator,
because dependent module Module::CPANTS::Analyse itself cannot calculate
prereq_matches_use indicator. It is marked as needs_db, but only limited
information is needed to calculate the indicator. This module calculates
prereq_matches_use by querying needed information from MetaCPAN.

%prep
%setup -q -n Test-Kwalitee-Extra-v%{version}

# Work around issues with M:C:A 1.00 (CPAN RT#128602)
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%if !%{with network_tests}
mv t/{01-kwalitee,04-prereq_maches_use,05-build_prereq_matches_use,06-minperlver}.t ./
%endif

make test AUTHOR_TESTING=1 RELEASE_TESTING=1

%if !%{with network_tests}
mv ./{01-kwalitee,04-prereq_maches_use,05-build_prereq_matches_use,06-minperlver}.t t/
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Kwalitee::Extra.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-12
- Perl 5.32 rebuild

* Tue Mar 10 2020 Paul Howarth <paul@city-fan.org> - 0.4.0-11
- BR: perl(blib) for t/00-compile.t

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep  3 2019 Paul Howarth <paul@city-fan.org> - 0.4.0-9
- Work around issues with M:C:A 1.00 (CPAN RT#128602)
- Use author-independent source URL
- Modernize spec using %%{make_build} and %%{make_install}

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Paul Howarth <paul@city-fan.org> - 0.4.0-1
- Update to 0.4.0
  - Only search existing directories
  - Use MetaCPAN::Client rather than MetaCPAN::API::Tiny
- Simplify find command using -delete

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Paul Howarth <paul@city-fan.org> - 0.3.1-1
- Update to 0.3.1
  - Fix false alarm for warnings (GH#20, CPAN RT#104113)
  - Fix minor grammatical error in error message

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.0-3
- Perl 5.22 rebuild

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.0-2
- Perl 5.20 rebuild

* Tue Sep  9 2014 Paul Howarth <paul@city-fan.org> - 0.3.0-1
- Update to 0.3.0
  - Adopt to new stash layout of Module::CPANTS::Analyse since 0.93_01 (GH#19)
- Use %%license

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Paul Howarth <paul@city-fan.org> - 0.2.1-1
- Update to 0.2.1
  - Add explicit caution and workaround for network access in POD (GH #17)

* Tue Feb 25 2014 Paul Howarth <paul@city-fan.org> - 0.2.0-2
- Sanitize for Fedora submission

* Thu Feb  6 2014 Paul Howarth <paul@city-fan.org> - 0.2.0-1
- Initial RPM version
