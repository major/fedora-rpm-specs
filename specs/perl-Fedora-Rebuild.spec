# This file is lincensed under the terms of GPLv2+.
Name:           perl-Fedora-Rebuild
Version:        0.12.1
Release:        35%{?dist}
Summary:        Rebuilds Fedora packages from scratch
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://ppisar.fedorapeople.org/Fedora-Rebuild/
Source0:        http://ppisar.fedorapeople.org/Fedora-Rebuild/Fedora-Rebuild-v%{version}.tar.gz
# Don't forget to reset a submitbuild state, in upstream after 0.12.1
Patch0:         Fedora-Rebuild-v0.12.1-Reset-submitbuild-state-by-F-R-Package-reset.patch
# Clean _topdir in shared mock enviroment before building a source package,
# in upstream after 0.12.1
Patch1:         Fedora-Rebuild-v0.12.1-Clean-_topdir-in-shared-mock-enviroment-before-build.patch
# Use createrepo_c instead of createrepo, in upstream after 0.12.1
Patch2:         Fedora-Rebuild-v0.12.1-Use-createrepo_c-instead-of-createrepo.patch
# Preserve file permissions when using a rebuildreset tool,
# in upstream after 0.12.1
Patch3:         Fedora-Rebuild-v0.12.1-rebuildreset-Preserve-file-permissions.patch
# Fix parsing repourls configuration option in a rebuildperl tool,
# in upstream after 0.12.1
Patch4:         Fedora-Rebuild-v0.12.1-rebuildperl-Fix-parsing-repourls-configuration-optio.patch
# Supress logging satisfied dependencies, in upstream after 0.12.1
Patch5:         Fedora-Rebuild-v0.12.1-Supress-logging-satisfied-dependencies.patch
# Do not clean mocks that failed to initialize, in upstream after 0.12.1
Patch6:         Fedora-Rebuild-v0.12.1-Do-not-clean-mocks-that-failed-to-initialize.patch
# Adapt to mock-1.4.1-1.fc25, in upstream after 0.12.1
Patch7:         Fedora-Rebuild-v0.12.1-Adapt-to-mock-1.4.1-1.fc25.patch
# Invoke pyrpkg build with --skip-nvr-check option,
# in upstream's nvrfromsrpm3 branch
Patch8:         Fedora-Rebuild-v0.12.1-Invoke-pyrpkg-build-with-skip-nvr-check-option.patch
# Switch to a selected git branch on the git reset,
# in upstream's nvrfromsrpm3 branch
Patch9:         Fedora-Rebuild-v0.12.1-Switch-to-selected-git-branch-on-git-reset.patch
# Report a package reset failure from a death thread,
# in upstream's nvrfromsrpm3 branch
Patch10:        Fedora-Rebuild-v0.12.1-rebuildreset-report-a-reset-failure-from-a-death-thr.patch
# 1/2 Adapt to changes in File-Path-Tiny-0.9, in upstream's nvrfromsrpm3 branch
Patch11:        Fedora-Rebuild-v0.12.1-Adapt-to-changes-in-File-Path-Tiny-0.9.patch
# 2/2 Adapt to changes in File-Path-Tiny-0.9, in upstream's nvrfromsrpm3 branch
Patch12:        Fedora-Rebuild-v0.12.1-Adapt-to-changes-in-File-Path-Tiny-0.9-in-Fedora-Reb.patch
# Adapt to changes in fedpkg-1.41, in upstreams's nvrfromsrpm3 branch
Patch13:        Fedora-Rebuild-v0.12.1-Use-release-instead-of-dist-at-pyrpkg-arguments.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::SyncExec)
BuildRequires:  perl(RPM2)
BuildRequires:  perl(RPM::VersionCompare)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ProgressBar)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
Requires:       createrepo_c
Requires:       fedpkg
Requires:       git-core
Requires:       koji
Requires:       mock
Requires:       rpmdevtools

%description
Main goal is to rebuild perl modules packages for Fedora. The rebuild is
driven from bottom to top, i.e. from perl interpreter to modules depending
on intermediate modules. This way, it's possible to upgrade perl
interpreter to incompatible version and to rebuild all modules against the
new interpreter.

%prep
%setup -q -n Fedora-Rebuild-v%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.12.1-34
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-27
- Perl 5.36 rebuild

* Wed Feb 23 2022 Petr Pisar <ppisar@redhat.com> - 0.12.1-26
- Adapt to changes in fedpkg-1.41

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-23
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-20
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-17
- Perl 5.30 rebuild

* Wed May 15 2019 Petr Pisar <ppisar@redhat.com> - 0.12.1-16
- Don't forget to reset a submitbuild state
- Clean _topdir in shared mock enviroment before building a source package
- Use createrepo_c instead of createrepo
- Preserve file permissions when using a rebuildreset tool
- Fix parsing repourls configuration option in a rebuildperl tool
- Supress logging satisfied dependencies
- Do not clean mocks that failed to initialize
- Adapt to mock-1.4.1-1.fc25
- Invoke pyrpkg build with --skip-nvr-check option
- Switch to a selected git branch on the git reset
- Report a package reset failure from a death thread
- Adapt to changes in File-Path-Tiny-0.9
- Require small git-core instead of big git package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-5
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.1-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Petr Pisar <ppisar@redhat.com> - 0.12.1-2
- Run-require createrepo

* Fri May 23 2014 Petr Pisar <ppisar@redhat.com> - 0.12.1-1
- 0.12.1 bump

* Tue May 13 2014 Petr Pisar <ppisar@redhat.com> - 0.12.0-1
- 0.12.0 bump

* Tue Jan 21 2014 Petr Pisar <ppisar@redhat.com> - 0.11.0-1
- 0.11.0 bump

* Thu Nov 07 2013 Petr Pisar <ppisar@redhat.com> - 0.10.0-1
- 0.10.0 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.9.1-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.9.1-2
- Perl 5.16 rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 0.9.1-1
- 0.9.1 bump

* Tue May 29 2012 Petr Pisar <ppisar@redhat.com> - 0.9.0-1
- 0.9.0 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 0.8.0-4
- Do not create back-up files when patching. They would be packaged.

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.8.0-3
- Use IO::Handle to build with perl5.14

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.8.0-2
- Perl mass rebuild

* Wed Jul 20 2011 Petr Pisar <ppisar@redhat.com> - 0.8.0-1
- 0.8.0 bump

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.7.0-2
- Perl mass rebuild

* Mon Jul 18 2011 Petr Pisar <ppisar@redhat.com> - 0.7.0-1
- 0.7.0 bump

* Fri Jul 15 2011 Petr Pisar <ppisar@redhat.com> - 0.5.1-1
- 0.5.1 version

* Fri Jul 15 2011 Petr Pisar <ppisar@redhat.com> - 0.5.0-1
- 0.5.0 bump

* Fri Jun 24 2011 Petr Pisar <ppisar@redhat.com> - 0.4.1-1
- 0.4.1 bump

* Wed Jun 22 2011 Petr Pisar <ppisar@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Fri Jun 17 2011 Petr Pisar <ppisar@redhat.com> - 0.2.1-1
- 0.2.1 bump

* Tue Jun 07 2011 Petr Pisar <ppisar@redhat.com> 0.0.1-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr code
