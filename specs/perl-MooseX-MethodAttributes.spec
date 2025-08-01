Name:           perl-MooseX-MethodAttributes
Summary:        Introspect your method code attributes
Version:        0.32
Release:        15%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-MethodAttributes-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-MethodAttributes
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose) >= 0.98
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean) >= 0.10
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)

%{?perl_default_filter}

%description
This module allows code attributes of methods to be introspected using
Moose meta method objects.


%prep
%setup -q -n MooseX-MethodAttributes-%{version}

# silence rpmlint warning
sed -i '1s,#!.*perl,#!/usr/bin/perl,' t/*.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README t/
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.32-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.32-1
- Update to 0.32
- Replace %%{__perl} with /usr/bin/perl
- Pass NO_PERLLOCAL to Makefile.PL
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.31-1
- Update to 0.31
- Switch build workflow again

* Thu Aug 20 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.30-1
- Update to 0.30
- Move to the Module::Build::Tiny workflow

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-2
- Perl 5.22 rebuild

* Tue Nov 11 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.29-1
- Update to 0.29

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.28-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.28-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.27-2
- Perl 5.16 rebuild
- Specify all dependencies

* Mon Feb 20 2012 Iain Arnell <iarnell@gmail.com> 0.27-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.26-3
- drop tests subpackage; move tests to main package documentation

* Tue Jan 17 2012 Iain Arnell <iarnell@gmail.com> - 0.26-2
- rebuilt again for F17 mass rebuild

* Sat Jan 14 2012 Iain Arnell <iarnell@gmail.com> 0.26-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.25-2
- Perl mass rebuild

* Sat Jul 02 2011 Iain Arnell <iarnell@gmail.com> 0.25-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- remove explicit requires

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.24-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Aug 28 2010 Iain Arnell <iarnell@gmail.com> 0.24-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.24)
- altered br on perl(ExtUtils::MakeMaker) (6.11 => 6.31)
- altered br on perl(Moose) (0.97 => 0.98)
- added a new br on perl(MooseX::Types::Moose) (version 0.21)
- dropped old BR on perl(MooseX::Types)
- altered req on perl(Moose) (0.97 => 0.98)
- added a new req on perl(MooseX::Types::Moose) (version 0.21)
- dropped old requires on perl(MooseX::Types)
- dropped old requires on perl(namespace::autoclean)

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.20-2
- Mass rebuild with perl-5.12.0

* Mon Mar 08 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- update by Fedora::App::MaintainerTools 0.004
- updating to latest GA CPAN version (0.20)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.11)
- altered br on perl(Moose) (0.90 => 0.97)
- dropped old BR on perl(MRO::Compat)
- altered req on perl(Moose) (0.90 => 0.97)
- dropped old requires on perl(MRO::Compat)

* Fri Feb 05 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- add perl_default_filter
- PERL_INSTALL_ROOT => DESTDIR in install
- auto-update to 0.19 (by cpan-spec-update 0.01)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.18-2
- rebuild against perl 5.10.1

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.18-1
- auto-update to 0.18 (by cpan-spec-update 0.01)
- altered br on perl(Moose) (0.79 => 0.90)
- altered br on perl(MooseX::Types) (0.06 => 0.20)
- altered br on perl(Test::More) (0 => 0.88)
- added a new br on perl(namespace::autoclean) (version 0)
- altered br on perl(namespace::clean) (0 => 0.10)
- altered req on perl(Moose) (0.79 => 0.90)
- altered req on perl(MooseX::Types) (0.06 => 0.20)
- added a new req on perl(namespace::autoclean) (version 0)
- altered req on perl(namespace::clean) (0 => 0.10)

* Sat Sep 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.16-1
- auto-update to 0.16 (by cpan-spec-update 0.01)

* Wed Aug 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- auto-update to 0.15 (by cpan-spec-update 0.01)
- added a new br on perl(MRO::Compat) (version 0)
- added a new req on perl(MRO::Compat) (version 0)
- added a new req on perl(Moose) (version 0.79)
- added a new req on perl(MooseX::Types) (version 0.06)
- added a new req on perl(namespace::clean) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.14-1
- auto-update to 0.14 (by cpan-spec-update 0.01)

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.13-1
- auto-update to 0.13 (by cpan-spec-update 0.01)

* Wed May 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.12-1
- add br on Test::Exception (missing as a test/br:
  https://rt.cpan.org/Ticket/Display.html?id=46396)
- auto-update to 0.12 (by cpan-spec-update 0.01)

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- auto-update to 0.11 (by cpan-spec-update 0.01)
- altered br on perl(Moose) (0.70 => 0.79)

* Mon Apr 20 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-2
- must remember to check summary! *sigh*

* Mon Apr 20 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- submission

* Mon Apr 20 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
