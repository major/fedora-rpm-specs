Name:           perl-File-ChangeNotify
Summary:        Watch for changes to files, cross-platform style
Version:        0.31
Release:        19%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-ChangeNotify-%{version}.tar.gz 
URL:            https://metacpan.org/release/File-ChangeNotify
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
# XXX: BuildRequires:  perl(IO::KQueue)
BuildRequires:  perl(Linux::Inotify2) >= 1.2
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test2::V0)
# Optional tests only
BuildRequires:  perl(Test::Without::Module)

%description
Watch for changes to files, easily, cleanly, and across different platforms.

%prep
%setup -q -n File-ChangeNotify-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%exclude %{perl_vendorlib}/File/ChangeNotify/Watcher/KQueue.pm
%{perl_vendorlib}/*
%exclude %{_mandir}/man3/File::ChangeNotify::Watcher::KQueue.3pm*
%{_mandir}/man3/*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-1
- 0.31 bump

* Wed Oct 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-1
- 0.29 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-2
- Perl 5.28 rebuild

* Mon Feb 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-1
- 0.28 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.26 rebuild

* Tue Mar 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-1
- 0.27 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- 0.26 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Petr Šabata <contyk@redhat.com> - 0.24-6
- Package cleanup
- Don't ship the KQueue watcher

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb  1 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.24-1
- Update to 0.24
- Drop tests subpackage

* Fri Aug  9 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.23-1
- Update to 0.23

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.22-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.22-3
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.22-2
- Round Module::Build version to 2 digits

* Sun May 27 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.22-1
- Update to 0.22

* Mon Mar 12 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.21-1
- Update to 0.21

* Fri Jan 13 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.20-1
- Update to 0.20
- Changed to Build.PL style
- BR: add perl(Test::Exception), perl(Linux::Inotify2)

* Fri Jul 22 2011 Iain Arnell <iarnell@gmail.com> 0.16-6
- update filtering for rpm 4.9

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.16-5
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.16-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Aug 26 2010 Iain Arnell <iarnell@gmail.com> 0.16-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.16)
- new license Artistic 2.0
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.31)
- altered br on perl(Module::Build) (0 => 0.3601)
- altered br on perl(Test::More) (0 => 0.88)
- added a new br on perl(namespace::autoclean) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)
- BR perl(Test::Exception), perl(Test::Without::Module) to enable tests

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-1
- update

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.12-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.12-3
- Mass rebuild with perl-5.12.0

* Mon Mar 15 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.12-2
- update by Fedora::App::MaintainerTools 0.006

* Sat Mar 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.12-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.12)
- added a new br on perl(Module::Build)
- dropped old BR on perl(Module::Build::Compat)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.07-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- auto-update to 0.07 (by cpan-spec-update 0.01)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(Class::MOP) (version 0)
- added a new req on perl(File::Find) (version 0)
- added a new req on perl(File::Spec) (version 0)
- added a new req on perl(Module::Pluggable::Object) (version 0)
- added a new req on perl(Moose) (version 0)
- added a new req on perl(MooseX::Params::Validate) (version 0.08)
- added a new req on perl(MooseX::SemiAffordanceAccessor) (version 0)
- added a new req on perl(Time::HiRes) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- submission

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
