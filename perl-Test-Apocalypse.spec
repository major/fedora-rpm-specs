Name:           perl-Test-Apocalypse
Version:        1.006
Release:        26%{?dist}
Summary:        Apocalypse's favorite tests bundled into a simple interface
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Apocalypse
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Test-Apocalypse-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Capture::Tiny) >= 0.10
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.113640
# Data::Dumper not used at tests
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find::Rule) >= 0.32
BuildRequires:  perl(File::Slurp) >= 9999.13
BuildRequires:  perl(File::Spec) >= 3.31
BuildRequires:  perl(File::Which) >= 1.09
BuildRequires:  perl(JSON::Any) >= 1.25
BuildRequires:  perl(Module::CPANTS::Analyse) >= 0.95
BuildRequires:  perl(Module::Pluggable) >= 3.9
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::Critic::Deprecated) >= 1.108
BuildRequires:  perl(Perl::Critic::Itch) >= 0.07
BuildRequires:  perl(Perl::Critic::Utils::Constants)
BuildRequires:  perl(Perl::Metrics::Simple) >= 0.13
BuildRequires:  perl(Perl::PrereqScanner) >= 1.000
BuildRequires:  perl(Pod::Coverage::TrustPod) >= 0.092830
BuildRequires:  perl(Task::Perl::Critic) >= 1.007
BuildRequires:  perl(Test::AutoLoader) >= 0.03
BuildRequires:  perl(Test::Compile) >= 0.11
BuildRequires:  perl(Test::ConsistentVersion) >= 0.2.2
BuildRequires:  perl(Test::CPAN::Changes) >= 0.30
BuildRequires:  perl(Test::CPAN::Meta) >= 0.18
BuildRequires:  perl(Test::CPAN::Meta::JSON) >= 0.10
BuildRequires:  perl(Test::CPAN::Meta::YAML) >= 0.17
BuildRequires:  perl(Test::Deep) >= 0.108
BuildRequires:  perl(Test::Dir) >= 1.006
BuildRequires:  perl(Test::DistManifest) >= 1.005
BuildRequires:  perl(Test::EOL) >= 0.3
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::File) >= 1.29
BuildRequires:  perl(Test::Fixme) >= 0.04
BuildRequires:  perl(Test::HasVersion) >= 0.012
BuildRequires:  perl(Test::MinimumVersion) >= 0.101080
BuildRequires:  perl(Test::Mojibake) >= 0.3
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoBreakpoints) >= 0.13
BuildRequires:  perl(Test::NoPlan) >= 0.0.6
BuildRequires:  perl(Test::Perl::Critic) >= 1.02
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Pod::LinkCheck) >= 0.004
BuildRequires:  perl(Test::Pod::No404s) >= 0.01
BuildRequires:  perl(Test::Pod::Spelling::CommonMistakes) >= 1.000
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Script) >= 1.07
BuildRequires:  perl(Test::Signature) >= 1.10
BuildRequires:  perl(Test::Spelling) >= 0.11
BuildRequires:  perl(Test::Strict) >= 0.14
BuildRequires:  perl(Test::Synopsis) >= 0.06
BuildRequires:  perl(Test::Vars) >= 0.001
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(YAML) >= 0.70
BuildRequires:  perl(YAML::Any) >= 0.72
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Data::Dumper)
Requires:       perl(Perl::Critic::Utils::Constants)
Requires:       perl(Test::FailWarnings)
Requires:       perl(Test::Portability::Files)

# Remove under-specified dependenices
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
This module greatly simplifies common author tests for modules heading towards
CPAN. I was sick of copy/pasting the tons of t/foo.t scripts + managing them
in every distribution. I thought it would be nice to bundle all of it into one
module and toss it on CPAN :) That way, every time I update this module all of
my distributions would be magically updated!

%prep
%setup -q -n Test-Apocalypse-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CommitLog examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-24
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-21
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-18
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-17
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-14
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Petr Pisar <ppisar@redhat.com> - 1.006-4
- Add plugins requiring fixed Test::Vars (bug #1231903)

* Fri Jul 10 2015 Petr Pisar <ppisar@redhat.com> - 1.006-3
- Remove plugins requiring broken Test::Vars (bug #1231903)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Petr Pisar <ppisar@redhat.com> - 1.006-1
- 1.006 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.002-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 1.002-2
- Perl 5.16 rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 1.002-1
- 1.002 bump

* Fri Mar 25 2011 Petr Pisar <ppisar@redhat.com> - 1.001-1
- 1.001 bump
- Build-require Test::NoWarnings

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
