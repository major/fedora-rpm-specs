Name:		perl-MouseX-Getopt
Summary:	Mouse role for processing command line options
Version:	0.38
Release:	28%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-Getopt
Source0:	https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Getopt-%{version}.tar.gz
Patch0:		MouseX-Getopt-0.38-GLD-0.113.patch
Patch1:		MouseX-Getopt-0.38-GLD-0.116.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build::Tiny) >= 0.035
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Getopt::Long) >= 2.37
BuildRequires:	perl(Getopt::Long::Descriptive) >= 0.081
BuildRequires:	perl(Mouse) >= 0.64
BuildRequires:	perl(Mouse::Meta::Attribute)
BuildRequires:	perl(Mouse::Role)
BuildRequires:	perl(Mouse::Util::TypeConstraints)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Mouse::Meta::Class)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception) >= 0.21
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Mouse)
BuildRequires:	perl(Test::Warn) >= 0.21
BuildRequires:	perl(Test2::V0)
# Optional Tests (have circular dependencies)
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(MouseX::ConfigFromFile)
BuildRequires:	perl(MouseX::SimpleConfig) >= 0.07
%endif
# Dependencies
Requires:	perl(Mouse) >= 0.64
Requires:	perl(Mouse::Meta::Attribute)

# Filter under-specified dependency
%global __requires_exclude ^perl\\(Mouse\\)$

%description
This is a Mouse role that provides an alternate constructor for creating
objects using parameters passed in from the command line.

%prep
%setup -q -n MouseX-Getopt-%{version}

# Fix compatibility with GLD 0.107 .. 0.113
# https://github.com/gfx/mousex-getopt/pull/15
%patch -P 0

# Fix compatibility with GLD 0.116
# https://github.com/gfx/mousex-getopt/pull/16
%patch -P 1 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
# Note: malformed LICENSE file in 0.35 .. 0.38 not shipped
# https://github.com/gfx/mousex-getopt/issues/2
%doc Changes README.md
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::Getopt.3*
%{_mandir}/man3/MouseX::Getopt::Basic.3*
%{_mandir}/man3/MouseX::Getopt::Dashes.3*
%{_mandir}/man3/MouseX::Getopt::GLD.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute::NoGetopt.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute::Trait.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute::Trait::NoGetopt.3*
%{_mandir}/man3/MouseX::Getopt::OptionTypeMap.3*
%{_mandir}/man3/MouseX::Getopt::Strict.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Paul Howarth <paul@city-fan.org> - 0.38-27
- Fix compatibility with GLD 0.116

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Paul Howarth <paul@city-fan.org> - 0.38-23
- Fix compatibility with GLD 0.113

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May  3 2023 Paul Howarth <paul@city-fan.org> - 0.38-21
- Spec tidy-up
  - Use SPDX-format license tag
  - Avoid use of deprecated patch syntax
  - Fix permissions of installed files

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-18
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-17
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-14
- Perl 5.34 re-rebuild of bootstrapped packages

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-13
- Perl 5.34 rebuild

* Mon Mar 15 2021 Paul Howarth <paul@city-fan.org> - 0.38-12
- Fix compatibility with GLD 0.107

* Sat Mar 13 2021 Paul Howarth <paul@city-fan.org> - 0.38-11
- Fix compatibility with GLD 0.106

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Paul Howarth <paul@city-fan.org> - 0.38-1
- Update to 0.38
  - Cope with GLD output changes in version 0.103 (GH#13)

* Tue Aug 21 2018 Paul Howarth <paul@city-fan.org> - 0.37-10
- Fix compatibility with GLD 0.103 (GH#12, GH#13)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-8
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Paul Howarth <paul@city-fan.org> - 0.37-1
- Update to 0.37
  - Cope with GLD output changes in version 0.100 (GH#10)
- Switch to Module::Build::Tiny flow

* Tue Jul 12 2016 Paul Howarth <paul@city-fan.org> - 0.36-8
- Fix FTBFS with Geopt::Long::Descriptive 0.100

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-2
- Perl 5.22 rebuild

* Thu Apr  2 2015 Paul Howarth <paul@city-fan.org> - 0.36-1
- Update to 0.36
  - Fix tests that follow GLD changes
    (https://github.com/gfx/mousex-getopt/pull/6)
- This release by GFUJI → update source URL and directory case

* Thu Feb  5 2015 Paul Howarth <paul@city-fan.org> - 0.35-7
- Fix FTBFS with Geopt::Long::Descriptive ≥ 0.99 (#1189458)
  https://github.com/gfx/mousex-getopt/issues/5
  https://github.com/gfx/mousex-getopt/pull/6

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-6
- Perl 5.20 re-rebuild of bootstrapped packages

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Paul Howarth <paul@city-fan.org> - 0.35-3
- Add buildreqs for optional tests now they're available

* Thu Apr 17 2014 Paul Howarth <paul@city-fan.org> - 0.35-2
- Incorporate feedback from package review (#1088856)
  - Don't ship bogus LICENSE file
    (https://github.com/gfx/mousex-getopt/issues/2)
  - Make upstream URL refer to current release
  - Upstream wants Module::Build ≥ 0.38
  - BR:/R: perl(Mouse::Meta::Attribute)
  - BR: perl(Scalar::Util) for test suite
  - R: perl(Mouse) ≥ 0.64

* Thu Apr 17 2014 Paul Howarth <paul@city-fan.org> - 0.35-1
- Update to 0.35
  - GLD 0.097 no longer defaults to no_ignore_case (CPAN RT#93593)
- This release by TOKUHIROM → update source URL and directory case
- Switch to Module::Build flow
- Release tests no longer included

* Thu Apr 17 2014 Paul Howarth <paul@city-fan.org> - 0.34-1
- Initial RPM version
