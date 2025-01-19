Name:           perl-Catalyst-Devel
Summary:        Catalyst Development Tools
Version:        1.42
Release:        14%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Devel-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Devel
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 5.90001
BuildRequires:  perl(Catalyst::Action::RenderView) >= 0.10
BuildRequires:  perl(Catalyst::Plugin::ConfigLoader) >= 0.30
BuildRequires:  perl(Catalyst::Plugin::Static::Simple) >= 0.28
BuildRequires:  perl(Config::General) >= 2.42
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(File::ChangeNotify) >= 0.07
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(Module::Install) >= 1.02
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Path::Class) >= 0.09
BuildRequires:  perl(Starman)
BuildRequires:  perl(Template) >= 2.14
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Fatal)

BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(IPC::Run3)

Requires:       perl(Catalyst) >= 5.90001
Requires:       perl(Catalyst::Action::RenderView) >= 0.10
Requires:       perl(Catalyst::Plugin::ConfigLoader) >= 0.30
Requires:       perl(Catalyst::Plugin::Static::Simple) >= 0.28
Requires:       perl(Config::General) >= 2.42
Requires:       perl(File::ChangeNotify) >= 0.07
Requires:       perl(Module::Install) >= 1.02
Requires:       perl(MooseX::Daemonize)
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)
Requires:       perl(Path::Class) >= 0.09
Requires:       perl(Starman)
Requires:       perl(Template) >= 2.14
Requires:       perl-Catalyst-Runtime-scripts

%{?perl_default_filter}

%description
The Catalyst::Devel package includes a variety of modules useful for the
development of Catalyst applications, but not required to run them. This is
intended to make it easier to deploy Catalyst apps. The runtime parts of
Catalyst are now known as Catalyst::Runtime.

%prep
%setup -q -n Catalyst-Devel-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test


%files
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man[13]/*
# we don't need this, and it's causing dep problems.
%exclude %{perl_vendorlib}/Catalyst/Restarter/Win32.pm

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.42-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-6
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.42-1
- Update to 1.42

* Sun Aug 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.41-1
- Update to 1.41
- Use /usr/bin/perl instead of %%{__perl}

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-2
- Perl 5.32 rebuild

* Sun Mar 01 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.40-1
- Update to 1.40
- Use /usr/bin/perl instead of %%{__perl}
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Pass NO_PACKLIST and NO_PERLLOCAL to Makefile.PL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-2
- Perl 5.22 rebuild

* Sat Nov 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.39-1
- Update to 1.39

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 1.37-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 1.37-2
- Perl 5.16 rebuild

* Sat May 19 2012 Iain Arnell <iarnell@gmail.com> 1.37-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 1.36-2
- drop old tests subpackage; move tests to main package documentation

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 1.36-1
- update to latest upstream version
- clean up spec for moderm rpmbuild

* Mon Aug 29 2011 Iain Arnell <iarnell@gmail.com> 1.34-1
- update to latest upstream version

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.31-4
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.31-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Iain Arnell <iarnell@gmail.com> 1.31-1
- update to latest upstream version
- update R/BR perl(Catalyst::Plugin::ConfigLoader) >= 0.30
- remove unnecessary explicit requires

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.28-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Aug 31 2010 Iain Arnell <iarnell@gmail.com> 1.28-1
- update to latest upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-2
- Mass rebuild with perl-5.12.0

* Sat Mar 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.27-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (1.27)
- altered br on perl(Catalyst) (5.8000 => 5.80015)
- altered br on perl(Catalyst::Action::RenderView) (0.04 => 0.10)
- altered br on perl(Catalyst::Plugin::ConfigLoader) (0 => 0.23)
- altered br on perl(Catalyst::Plugin::Static::Simple) (0.16 => 0.28)
- added a new br on perl(File::ShareDir) (version 0)
- added a new br on perl(Moose) (version 0)
- added a new br on perl(MooseX::Emulate::Class::Accessor::Fast) (version 0)
- altered br on perl(Test::More) (0 => 0.94)
- added a new br on perl(namespace::autoclean) (version 0)
- added a new br on perl(namespace::clean) (version 0)
- dropped old BR on perl(Class::Accessor::Fast)
- dropped old BR on perl(parent)
- added manual BR on perl(Test::More) (or override to 0.92)
- altered req on perl(Catalyst) (5.8000 => 5.80015)
- altered req on perl(Catalyst::Action::RenderView) (0.04 => 0.10)
- altered req on perl(Catalyst::Plugin::ConfigLoader) (0 => 0.23)
- altered req on perl(Catalyst::Plugin::Static::Simple) (0.16 => 0.28)
- added a new req on perl(File::ShareDir) (version 0)
- added a new req on perl(Moose) (version 0)
- added a new req on perl(MooseX::Emulate::Class::Accessor::Fast) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)
- added a new req on perl(namespace::clean) (version 0)
- dropped old requires on perl(Class::Accessor::Fast)
- dropped old requires on perl(YAML)
- dropped old requires on perl(parent)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.20-2
- rebuild against perl 5.10.1

* Tue Aug 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.20-1
- auto-update to 1.20 (by cpan-spec-update 0.01)
- altered br on perl(File::ChangeNotify) (0.03 => 0.07)
- altered req on perl(File::ChangeNotify) (0.03 => 0.07)

* Mon Jul 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.19-1
- auto-update to 1.19 (by cpan-spec-update 0.01)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.18-3
- exclude Catalyst::Restarter::Win32 (dep issues and unneeded on this
  platform)

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.18-2
- br CPAN until bundled M::I is updated

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.18-1
- auto-update to 1.18 (by cpan-spec-update 0.01)
- altered br on perl(Module::Install) (0.64 => 0.91)
- altered req on perl(Catalyst) (5.7000 => 5.8000)
- added a new req on perl(Config::General) (version 2.42)
- added a new req on perl(File::ChangeNotify) (version 0.03)
- added a new req on perl(File::Copy::Recursive) (version 0)
- altered req on perl(Module::Install) (0.64 => 0.91)
- added a new req on perl(Template) (version 2.14)

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.17-1
- auto-update to 1.17 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Catalyst) (5.7000 => 5.8000)
- altered br on perl(Config::General) (0 => 2.42)
- added a new br on perl(File::ChangeNotify) (version 0.03)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.10-1
- update to 1.10

* Wed Sep 10 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-2
- add perl(parent) as a requires (BZ#461581)

* Thu Jul 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-1
- update to 1.08

* Thu Jul 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.07-2
- drop requires on Catalyst::Manual that should have been dropped in 1.06-1

* Sun Jun 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.07-1
- update to 1.07
- require perl-Catalyst-Runtime-scripts; catalyst.pl lives in there now.

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.06-1
- update to 1.06 (runtime to 5.7014)
- drop br on Catalyst::Manual; add br on parent

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-2
- rebuild for new perl

* Sat Mar 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.03-1
- update to 1.03 (runtime to 5.7012)

* Fri Aug 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.02-3
- bump

* Tue Jul 24 2007 Chris Weyl <cweyl@alumni.drew.edu>
- add t/ to doc

* Fri Apr 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.02-1
- Specfile autogenerated by cpanspec 1.71.
