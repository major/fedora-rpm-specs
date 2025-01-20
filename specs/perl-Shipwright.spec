Name:           perl-Shipwright
Version:        2.4.42
Release:        23%{?dist}
Summary:        Build and Manage Self-contained Software Bundle
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Shipwright
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SUNNAVY/Shipwright-%{version}.tar.gz
# Drop useless build-time feautures
Patch0:         Shipwright-2.4.41-Disable-author-test-and-network-installation-when-bu.patch
# Use real interpreter path instead of /usr/bin/env trampoline
Patch1:         Shipwright-2.4.41-Do-not-use-usr-bin-env.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install) >= 0.76
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::Share)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
# Algorithm::Dependency::Ordered not used at tests
# Algorithm::Dependency::Source::HoA not used at tests
BuildRequires:  perl(App::CLI)
# 0.47 is broken, fixed in 0.48
BuildConflicts: perl(App::CLI) = 0.47
BuildRequires:  perl(App::CLI::Command)
BuildRequires:  perl(App::CLI::Command::Help)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN) >= 1.9205
# CPAN::Config is optional
BuildRequires:  perl(CPAN::DistnameInfo)
# CPAN::MyConfig is optional
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
# File::Compare not used at tests
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Slurp)
# File::Spec not used at tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Log4perl)
# LWP::UserAgent not used at tests
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Info)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
# Tie::File not used at tests
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML::Tiny)
Requires:       perl(Algorithm::Dependency::Ordered)
Requires:       perl(Algorithm::Dependency::Source::HoA)
Requires:       perl(CPAN) >= 1.9205
Requires:       perl(File::Compare)
Requires:       perl(File::Path) >= 2.07
Requires:       perl(File::Temp) >= 0.18
Requires:       perl(LWP::UserAgent)
Requires:       perl(Test::More)
Requires:       perl(Tie::File)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Path|File::Temp)\\)$

%description
Shipwright is a tool to help you bundle your software with all its dependencies,
regardless of whether they are CPAN modules or non-Perl modules from elsewhere.
Shipwright makes the bundle work easy.

%prep
%setup -q -n Shipwright-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -rf ./inc
sed -i -e '/^inc\//d' MANIFEST
# Fix shellbangs unnoticed by build script
sed -i -e 's|#!perl|%(perl -MConfig -e 'print $Config{startperl}')|' \
    share/bin/* share/etc/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test %{?_smp_mflags}

%files
%doc AUTHORS Changes README TODO
%{_bindir}/shipwright*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.42-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.42-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.42-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.42-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.42-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.42-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 2.4.42-1
- 2.4.42 bump

* Tue Nov 07 2017 Petr Pisar <ppisar@redhat.com> - 2.4.41-8
- Adapt tests to App-CLI 0.47 (bug #1510360)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.41-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.41-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Petr Pisar <ppisar@redhat.com> - 2.4.41-1
- 2.4.41 bump

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.33-9
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.33-8
- Perl 5.20 rebuild

* Mon Sep 01 2014 Petr Pisar <ppisar@redhat.com> - 2.4.33-7
- Require Module::Build::Version (bug #1134862)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.33-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 2.4.33-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Robin Lee <cheeselee@fedoraproject.org> - 2.4.33-1
- Update to 2.4.33

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 2.4.31-2
- Perl 5.16 rebuild

* Sun Mar  4 2012 Robin Lee <cheeselee@fedoraproject.org> - 2.4.31-1
- Update to 2.4.31

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Robin Lee <cheeselee@fedoraproject.org> - 2.4.30-1
- Update to 2.4.30

* Wed Jul 27 2011 Robin Lee <cheeselee@fedoraproject.org> - 2.4.28-1
- Update to 2.4.28 (#712671)
- Use rpm 4.9 style filter

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.4.24-2
- Perl mass rebuild

* Wed Apr  6 2011 Robin Lee <cheeselee@fedoraproject.org> - 2.4.24-1
- Update to 2.4.24
- Initial import (#690359)

* Thu Mar 24 2011 Robin Lee <cheeselee@fedoraproject.org> - 2.4.23-1
- Initial packaging with help of cpanspec 1.78
