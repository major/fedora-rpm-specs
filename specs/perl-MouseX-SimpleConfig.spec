# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

# Similarly, for package note feature
%undefine _package_note_file

Name:		perl-MouseX-SimpleConfig
Summary:	A Mouse role for setting attributes from a simple configfile
Version:	0.11
Release:	37%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-SimpleConfig
Source0:	https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-SimpleConfig-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.31
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config::Any) >= 0.13
BuildRequires:	perl(English)
BuildRequires:	perl(Mouse) >= 0.35
BuildRequires:	perl(Mouse::Role)
BuildRequires:	perl(MouseX::ConfigFromFile) >= 0.02
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(lib)
BuildRequires:	perl(Path::Class::File)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(YAML::Syck)
# Author Tests (not used as code is not tidy enough)
#BuildRequires:	perl(Perl::Critic::Policy::Lax::RequireExplicitPackage::ExceptForPragmata)
#BuildRequires:	perl(Perl::Critic::Policy::Subroutines::ProhibitCallsToUndeclaredSubs)
#BuildRequires:	perl(Test::Perl::Critic)
# Release Tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::CheckChanges)
BuildRequires:	perl(Test::ConsistentVersion)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::DistManifest)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::HasVersion)
BuildRequires:	perl(Test::Kwalitee)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
# Note: Test::Vars not used since it is FTBFS with Perl 5.38
#BuildRequires:	perl(Test::Vars)
# Dependencies
# (none)

%description
This role loads simple configfiles to set object attributes. It is based on the
abstract role MouseX::ConfigFromFile, and uses Config::Any to load your
configfile. Config::Any will in turn support any of a variety of different
config formats, detected by the file extension. See Config::Any for more
details about supported formats.

Like all MouseX::ConfigFromFile-derived configfile loaders, this module is
automatically supported by the MouseX::Getopt role as well, which allows
specifying -configfile on the command line.

%prep
%setup -q -n MouseX-SimpleConfig-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::SimpleConfig.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Paul Howarth <paul@city-fan.org> - 0.11-35
- Drop BR: perl(Test::Vars), which is FTBFS with Perl 5.38

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-29
- Perl 5.36 rebuild

* Fri Mar 11 2022 Paul Howarth <paul@city-fan.org> - 0.11-28
- Work around FTBFS triggered by package note feature

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-25
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Paul Howarth <paul@city-fan.org> - 0.11-23
- Spec tidy-up
  - Use author-independent source URL
  - Specify all build dependencies
  - Use Test::Vars unconditionally
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Use %%license macro

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-21
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-7
- Perl 5.22 rebuild

* Tue Jun 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-6
- Disable using of Test::Vars with Perl 5.22

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Paul Howarth <paul@city-fan.org> - 0.11-3
- perl(Test::ConsistentVersion) now available in EPEL-7 too

* Fri Apr 25 2014 Paul Howarth <paul@city-fan.org> - 0.11-2
- Incorporate fixes from package review (#1088950)
  - Add perl(File::Find) and perl(Test::Script) test dependencies
  - Drop perl(Test::Pod::Content) as it should be pulled in via
    perl(Test::ConsistentVersion) (#1091285)
  - No need to clean buildroot in %%install

* Thu Apr 17 2014 Paul Howarth <paul@city-fan.org> - 0.11-1
- Initial RPM version
