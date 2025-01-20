# Perform optional tests
%bcond_without perl_MooseX_Types_DateTime_enables_optional_test

Name:       perl-MooseX-Types-DateTime
Version:    0.13
Release:    30%{?dist}
# see, e.g., lib/MooseX/Types/DateTime.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl

Summary:    DateTime related constraints and coercions for Moose
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-DateTime-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-Types-DateTime
BuildArch:  noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(:VERSION) >= 5.8.3
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time:
BuildRequires: perl(DateTime) >= 0.43
BuildRequires: perl(DateTime::Duration) >= 0.43
BuildRequires: perl(DateTime::Locale) >= 0.40
BuildRequires: perl(DateTime::TimeZone) >= 0.95
BuildRequires: perl(if)
BuildRequires: perl(Moose) >= 0.41
BuildRequires: perl(MooseX::Types) >= 0.30
BuildRequires: perl(MooseX::Types::Moose) >= 0.30
BuildRequires: perl(namespace::clean) >= 0.19
BuildRequires: perl(namespace::autoclean)
# Tests:
BuildRequires: perl(File::Spec)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(ok)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More) >= 0.88
# Test::Warnings not used
%if %{with perl_MooseX_Types_DateTime_enables_optional_test}
# Optional tests:
BuildRequires: perl(Locale::Maketext)
%endif
# Clamp version to decimal 2 digits
Requires:   perl(DateTime) >= 0.43
Requires:   perl(DateTime::Duration) >= 0.43
Requires:   perl(DateTime::Locale) >= 0.40
Requires:   perl(namespace::autoclean)

%{?perl_default_filter}

# Remove over-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime[:)].*\\.[0-9]{3,}$

%description
This module packages several type constraints (Moose::Util::TypeConstraints)
and coercions designed to work with the DateTime suite of objects.


%prep
%setup -q -n MooseX-Types-DateTime-%{version}

perl -MConfig -i -pe 's{^#!.*perl}{$Config{startperl}}' t/*.t
find . -type f -exec chmod -c -x {} +

%build
PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL \
    INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
make test

%files
%doc Changes t/
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13-29
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-16
- Perl 5.32 re-rebuild updated packages

* Thu Jun 25 2020 Petr Pisar <ppisar@redhat.com> - 0.13-15
- Specify all dependencies
- Patch shebangs properly
- Build using ExtUtils::MakeMaker

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.13-1
- Update to 0.13

* Fri Oct 02 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-1
- Update to 0.12

* Sat Aug 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.11-1
- Update to 0.11
- Move to the Module::Build::Tiny workflow
- Remove tests subpackage
- Use %%license macro

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-2
- Perl 5.22 rebuild

* Sat Nov 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.10-1
- Update to 0.10
- Tighten file listing

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.08-2
- Perl 5.18 rebuild

* Sun Feb 03 2013 Iain Arnell <iarnell@gmail.com> 0.08-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.07-4
- Perl 5.16 rebuild

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.07-3
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Petr Pisar <ppisar@redhat.com> - 0.07-2
- Adjust Perl versions to RPM versions

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream version
- remove unnecessary explicit requires

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.05-8
- Perl mass rebuild

* Sun Jun 26 2011 Iain Arnell <iarnell@gmail.com> 0.05-7
- remove unnecessary explicit requires
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-5
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-4
- Mass rebuild with perl-5.12.0

* Sat Feb 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.05-3
- PERL_INSTALL_ROOT => DESTDIR
- add perl_default_filter, _default_subpackage_tests
- drop version req on DateTime (buildfailures with latest perl-DateTime)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.05-2
- rebuild against perl 5.10.1

* Sat Sep 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- auto-update to 0.05 (by cpan-spec-update 0.01)
- altered br on perl(MooseX::Types) (0.04 => 0.19)
- altered req on perl(MooseX::Types) (0.04 => 0.19)
- added a new req on perl(Test::Exception) (version 0.27)
- added a new req on perl(Test::use::ok) (version 0.02)

* Mon Aug 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- auto-update to 0.04 (by cpan-spec-update 0.01)
- altered br on perl(DateTime::Locale) (0 => 0.4001)
- altered br on perl(DateTime::TimeZone) (0.7701 => 0.95)
- added a new req on perl(DateTime) (version 0.4302)
- added a new req on perl(DateTime::Format::DateParse) (version 0.04)
- added a new req on perl(DateTime::Format::Flexible) (version 0.05)
- added a new req on perl(DateTime::Format::Natural) (version 0.71)
- added a new req on perl(DateTime::Locale) (version 0.4001)
- added a new req on perl(DateTime::TimeZone) (version 0.95)
- added a new req on perl(DateTimeX::Easy) (version 0.082)
- added a new req on perl(Moose) (version 0.41)
- added a new req on perl(MooseX::Types) (version 0.04)
- added a new req on perl(Time::Duration::Parse) (version 0.06)
- added a new req on perl(namespace::clean) (version 0.08)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03-3
- add DateTime::Format::DateManip as a br

* Sat Dec 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.03-2
- touchup for submission

* Sat Oct 11 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.03-1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.1)
