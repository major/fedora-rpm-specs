Name:           perl-App-Cmd
Summary:        Write command line apps with less suffering
Version:        0.336
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/App-Cmd-%{version}.tar.gz 
URL:            https://metacpan.org/release/App-Cmd
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter >= 5.20.0
BuildRequires:  perl-generators
BuildRequires:  perl(parent)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(IO::TieCombine) >= 1
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Sub::Exporter) >= 0.975
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(experimental)

Requires:       perl(Getopt::Long::Descriptive) >= 0.084
Requires:       perl(IO::TieCombine) >= 1
Requires:       perl(Sub::Exporter) >= 0.975

%{?perl_default_filter}

%description
App::Cmd is intended to make it easy to write complex command-line
applications without having to think about most of the annoying things
usually involved.

For information on how to start using App::Cmd, see App::Cmd::Tutorial.

%prep
%setup -q -n App-Cmd-%{version}

/usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t t/*.pl

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/App*
%{_mandir}/man3/App*.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.336-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.336-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.336-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.336-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 27 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.336-1
- Update to 0.336
- migrated to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.335-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.335-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.335-1
- Update to 0.335

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.334-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.334-4
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.334-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.334-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.334-1
- Update to 0.334

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.333-2
- Perl 5.34 rebuild

* Sun Mar 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.333-1
- Update to 0.333

* Sun Mar 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.332-1
- Update to 0.332
- Replace calls to %%{__perl} with /usr/bin/perl
- Pass NO_PERLLOCAL to Makefile.PL
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.331-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.331-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.331-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.331-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.331-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.331-2
- Remove tests from documentation, per user request (#1385280)

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.331-1
- Update to 0.331

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.330-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.330-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.330-1
- Update to 0.330

* Fri Oct 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.329-1
- Update to 0.329

* Sun Sep 06 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.328-1
- Update to 0.328

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.327-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.327-2
- Perl 5.22 rebuild

* Sun Mar 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.327-1
- Update to 0.327

* Thu Dec 04 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.326-1
- Update to 0.326
- Drop LICENSE from the documentation

* Fri Oct 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.324-1
- Update to 0.324
- Tighten files declaration
- Use the %%license tag

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.323-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.323-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 15 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.323-1
- Update to 0.323

* Sun Nov 03 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.322-1
- Update to 0.322

* Sun Oct 27 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.321-1
- Update to 0.321

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.320-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 0.320-2
- Perl 5.18 rebuild

* Sat Feb 02 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.320-1
- Update to 0.320

* Sun Jan 27 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.319-1
- Update to 0.319
- Remove the obsoletes/provides macro for the tests subpackage
- Remove the group macro
- Add Test::Pod to the BuildRequires

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.318-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.318-2
- Perl 5.16 rebuild

* Sat May 05 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.318-1
- Update to 0.318

* Mon Mar 26 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.317-1
- Update to 0.317

* Sun Feb 12 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.316-1
- Update to 0.316

* Sat Feb 11 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.315-1
- Update to 0.315

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.314-2
- drop tests-subpackage; move tests to main package documentation

* Thu Jan 12 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.314-1
- Update to 0.314

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.312-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.311-2
- Perl mass rebuild

* Fri Mar 18 2011 Iain Arnell <iarnell@gmail.com> 0.311-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.309-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Iain Arnell <iarnell@gmail.com> 0.309-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.309)
- added a new br on perl(Carp) (version 0)
- added a new br on perl(Data::Dumper) (version 0)
- added a new br on perl(Data::OptList) (version 0)
- altered br on perl(ExtUtils::MakeMaker) (6.42 => 6.31)
- added a new br on perl(File::Basename) (version 0)
- added a new br on perl(Sub::Exporter::Util) (version 0)
- added a new br on perl(Test::Fatal) (version 0)
- altered br on perl(Test::More) (0 => 0.96)
- added a new br on perl(Text::Abbrev) (version 0)
- added a new br on perl(constant) (version 0)
- clean up spec for modern rpmbuild

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.307-3
- Mass rebuild with perl-5.12.0

* Fri Apr 23 2010 Iain Arnell <iarnell@gmail.com> 0.307-2
- requires perl(IO::TieCombine)

* Thu Apr 08 2010 Iain Arnell <iarnell@gmail.com> 0.307-1
- update to latest upstream
- R/BR perl(String::RewritePrefix)
- Bump R/BR perl(Getopt::Long::Descriptive) >= 0.084

* Mon Mar 01 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.304-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- altered br on perl(Getopt::Long::Descriptive) (0.075 => 0.081)
- altered req on perl(Getopt::Long::Descriptive) (0.075 => 0.081)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.301-2
- rebuild against perl 5.10.1

* Sat Sep 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.301-1
- auto-update to 0.301 (by cpan-spec-update 0.01)

* Sat Aug 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.207-1
- switch filtering to perl_default_filter
- auto-update to 0.207 (by cpan-spec-update 0.01)

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.206-1
- auto-update to 0.206 (by cpan-spec-update 0.01)
- altered br on perl(Getopt::Long::Descriptive) (0.06 => 0.075)
- altered req on perl(Getopt::Long::Descriptive) (0.06 => 0.075)

* Sat Aug 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.204-1
- auto-update to 0.204 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new req on perl(Getopt::Long::Descriptive) (version 0.06)
- added a new req on perl(Module::Pluggable::Object) (version 0)
- added a new req on perl(Sub::Exporter) (version 0.975)
- added a new req on perl(Sub::Install) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.203-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.203-1
- update to 0.203

* Mon Nov 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.202-3
- br Test::More; drink more coffee

* Mon Nov 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.202-2
- bump

* Tue Nov 04 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.202-1
- update for submission

* Mon Oct 27 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.202-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)
