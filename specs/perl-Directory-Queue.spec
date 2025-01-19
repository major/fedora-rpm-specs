%global cpan_name Directory-Queue

Name:           perl-%{cpan_name}
Version:        2.2
Release:        10%{?dist}
Summary:        Object oriented interface to a directory based queue
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LC/LCONS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(No::Worries::Die) >= 1.4
BuildRequires:  perl(No::Worries::Export)
BuildRequires:  perl(No::Worries::File)
BuildRequires:  perl(No::Worries::Stat)
BuildRequires:  perl(No::Worries::Warn)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(No::Worries::Dir)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(No::Worries::Die) >= 1.4

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(No::Worries::Die\\)$

%description
The goal of this module is to offer a simple queue system using the underlying
file system for storage, security and to prevent race conditions via atomic
operations. It focuses on simplicity, robustness and scalability.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{3pod,4podcov}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorlib}/Directory
%{perl_vendorlib}/Directory/Queue
%{perl_vendorlib}/Directory/Queue.pm
%{_mandir}/man3/Directory::Queue.*
%{_mandir}/man3/Directory::Queue::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 09 2024 Petr Pisar <ppisar@redhat.com> - 2.2-9
- Modernize a spec file
- Repackage tests to /usr/libexec/perl-Directory-Queue

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Lionel Cons <lionel.cons@cern.ch> - 2.2-1
- Updated to 2.2 (rhbz #2108568)

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Lionel Cons <lionel.cons@cern.ch> - 2.1-1
- Updated to 2.1 (rhbz #2013637)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-2
- Perl 5.28 rebuild

* Thu Apr 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-1
- 2.0 bump
- Specify all dependencies; Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Lionel Cons <lionel.cons@cern.ch> 1.9-2
- Spec file cleanup.

* Fri Nov 13 2015 Lionel Cons <lionel.cons@cern.ch> - 1.9-1
- Update to upstream version, rhbz #1281294.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-7
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 1.8-3
- Perl 5.18 rebuild

* Mon May 27 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.8-2
- rebuilt

* Wed May 22 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.8-1
- Update to 1.8 rhbz#965604.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.7-1
- Update to 1.7 rhbz#877951.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.6-2
- Perl 5.16 rebuild

* Sat Jun 9 2012 Steve Traylen <steve.traylen@cern.ch> - 1.6-1
- Update to 1.6 rhbz#828689

* Sat Jan 28 2012 Steve Traylen <steve.traylen@cern.ch> - 1.5-1
- Update to 1.5 rhbz#785073.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 8 2011 Steve Traylen <steve.traylen@cern.ch> - 1.4-1
- Update 1.4 rhbz#760472.

* Tue Aug 30 2011 Steve Traylen <steve.traylen@cern.ch> - 1.2-1
- Update 1.2 rhbz#73941.

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1-2
- Perl mass rebuild

* Mon May 2 2011 Steve Traylen <steve.traylen@cern.ch> 1.1-1
- New upstream 1.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Aug 31 2010 Steve Traylen <steve.traylen@cern.ch> 1.0-2
- perl(Time::HiRes) needed explicity on el4 and el6? 
  Just buildrequire it everywhere.

* Tue Aug 31 2010 Steve Traylen <steve.traylen@cern.ch> 1.0-1
- New upstream 1.0.

* Sun Jun 27 2010 Steve Traylen <steve.traylen@cern.ch> 0.5-3
- Rebuilt due to cvs mistake.

* Sun Jun 27 2010 Steve Traylen <steve.traylen@cern.ch> 0.5-2
- Explicit perl(Time::HiRes) br on EL4 added.

* Mon Jun 21 2010 Steve Traylen <steve.traylen@cern.ch> 0.5-1
- Specfile autogenerated by cpanspec 1.78.
- Add tests rpm generation  macro.
- Change PERL_INSTALL_DIR for DESTDIR.
- Add br perl(Test::Pod::Coverage) and perl(Test::Pod)
- Remove r of perl(Test::More)

