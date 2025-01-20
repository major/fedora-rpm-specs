Name:       perl-MooseX-App-Cmd
Version:    0.34
Release:    13%{?dist}
# see lib/MooseX/App/Cmd.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Mashes up MooseX::Getopt and App::Cmd
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-App-Cmd-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-App-Cmd
BuildArch:  noarch

BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Module::Build::Tiny)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

# Run-time:
BuildRequires: perl(Any::Moose)
BuildRequires: perl(App::Cmd) >= 0.321
BuildRequires: perl(App::Cmd::Command)
BuildRequires: perl(English)
BuildRequires: perl(File::Basename)
BuildRequires: perl(Getopt::Long::Descriptive) >= 0.091
# any_moose('::Object')
BuildRequires: perl(Moose::Object)
BuildRequires: perl(MooseX::NonMoose)
# any_moose('X::Getopt')
BuildRequires: perl(MooseX::Getopt) >= 0.18
BuildRequires: perl(namespace::clean)

# Tests:
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(CPAN::Meta) >= 2.120900
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(lib)
BuildRequires: perl(Moose) >= 0.86
BuildRequires: perl(MooseX::ConfigFromFile)
BuildRequires: perl(Pod::Coverage::TrustPod)
BuildRequires: perl(Test::EOL)
BuildRequires: perl(Test::Kwalitee) >= 1.21
BuildRequires: perl(Test::CPAN::Changes)
BuildRequires: perl(Test::CPAN::Meta)
BuildRequires: perl(Test::More) >= 0.94
BuildRequires: perl(Test::NoTabs)
BuildRequires: perl(Test::Pod) >= 1.41
BuildRequires: perl(Test::Pod::Coverage) >=  1.08
BuildRequires: perl(YAML)

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Output)

# we don't pick up Moose keywords automagically yet
Requires:   perl(App::Cmd) >= 0.321
Requires:   perl(App::Cmd::Command)
Requires:   perl(Getopt::Long::Descriptive) >= 0.091
# any_moose('::Object')
Requires:   perl(Moose::Object)
# any_moose('X::Getopt')
Requires:   perl(MooseX::Getopt) >= 0.18

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Getopt::Long::Descriptive\\)$


%description
This package marries App::Cmd with MooseX::Getopt.

Use it like the App::Cmd man-page advises (especially see the
App::Cmd::Tutorial man-page), swapping App::Cmd::Command for
MooseX::App::Cmd::Command.

Then you can write your commands as Moose classes, with the
MooseX::Getopt defining the options for you instead of 'opt_spec'
returning a Getopt::Long::Descriptive spec.


%prep
%setup -q -n MooseX-App-Cmd-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%doc Changes README
%license LICENCE
%{perl_vendorlib}/MooseX
%{_mandir}/man3/MooseX::*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.34-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.34 rebuild

* Sun Mar 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.34-1
- Update to 0.34
- Replace calls to %%{__perl} with /usr/bin/perl

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.32-1
- Update to 0.32
- Switch to the Module::Build::Tiny way of doing things

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-2
- Perl 5.22 rebuild

* Mon May 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.31-1
- Update to 0.31

* Wed Feb 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.30-1
- Update to 0.30
- Drop MouseX::App::Cmd (which now has its own distribution)
- Drop upstreamed patch
- Use the %%license tag

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Pisar <ppisar@redhat.com> - 0.27-2
- Adapt to Params-Validate-1.09 (bug #1099738)

* Thu Apr 17 2014 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump (bug #1088741)

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.09-7
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 26 2012 Iain Arnell <iarnell@gmail.com> 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.09-3
- Perl 5.16 rebuild

* Fri May 18 2012 Iain Arnell <iarnell@gmail.com> 0.09-2
- add LICENSE, README and TODO to files

* Fri May 18 2012 Iain Arnell <iarnell@gmail.com> 0.09-1
- update to latest upstream version

* Sat Mar 03 2012 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- BR perl(Test::Output) for improved test coverage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.06-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-4
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-2
- rebuild against perl 5.10.1

* Sat Sep 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- switch filtering systems
- auto-update to 0.06 (by cpan-spec-update 0.01)
- altered br on perl(App::Cmd) (0 => 0.3)
- altered req on perl(App::Cmd) (0 => 0.3)
- added a new req on perl(Test::use::ok) (version 0)

* Wed Aug 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- auto-update to 0.05 (by cpan-spec-update 0.01)
- altered br on perl(Moose) (0 => 0.86)
- altered br on perl(MooseX::Getopt) (0.09 => 0.18)
- added a new req on perl(Getopt::Long::Descriptive) (version 0)
- added a new req on perl(Moose) (version 0.86)
- altered req on perl(MooseX::Getopt) (0.09 => 0.18)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-2
- I swear I fixed those "manpage" references...

* Wed Nov 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- update for submission

* Mon Oct 27 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)
