Name:           perl-Net-Appliance-Session
Version:        4.300005
Release:        19%{?dist}
Summary:        Run command-line sessions to network appliances
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Appliance-Session
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Net-Appliance-Session-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Load)
# Cwd not used at tests
# Data::Dumper not used at tests
# Getopt::Long not used at tests
# IO::Handle not used at tests
# IO::Prompt::Tiny not used at tests
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::CLI::Interact) >= 2.300003
BuildRequires:  perl(Sub::Quote)
# Term::ANSIColor not used at tests
# Term::ReadPassword not used at tests
# Text::Glob not used at tests
# Text::ParseWords not used at tests
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Class::Load)
Requires:       perl(Net::CLI::Interact) >= 2.300003

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::CLI::Interact\\)$

%description
Use this module to establish an interactive command-line session with a
network appliance. There is special support for moving into "privileged"
mode and "configure" mode, along with the ability to send commands to the
connected device and retrieve returned output.

%prep
%setup -q -n Net-Appliance-Session-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples
%{perl_vendorlib}/*
%{_bindir}/nas
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 4.300005-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.300005-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.300005-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.300005-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.300005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.300005-2
- Perl 5.30 rebuild

* Mon May 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.300005-1
- 4.300005 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.300001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.300001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.300001-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.300001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.300001-1
- 4.300001 bump

* Thu Oct 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.300000-1
- 4.300000 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.200003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.200003-2
- Perl 5.26 rebuild

* Thu Apr 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.200003-1
- 4.200003 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.200002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.200002-1
- 4.200002 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.200000-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.200000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Petr Pisar <ppisar@redhat.com> - 4.200000-1
- 4.200000 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.131260-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.131260-5
- Perl 5.22 rebuild

* Tue Feb 10 2015 Petr Pisar <ppisar@redhat.com> - 4.131260-4
- Specify all dependencies

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.131260-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.131260-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Simone Caronni <negativo17@gmail.com> - 4.131260-1
- Update to 4.131260.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.122100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 03 2012 "Simone Caronni <negativo17@gmail.com>" 3.122100-2
- Specfile regenerated by cpanspec 1.78.
- Added perl module compat.
- Removed duplicate Requires.

* Thu Aug 30 2012 Simone Caronni <negativo17@gmail.com> - 3.122100-1
- First build.
