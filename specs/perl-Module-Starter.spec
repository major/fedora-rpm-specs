Name:           perl-Module-Starter
Epoch:          1
Version:        1.77
Release:        14%{?dist}
Summary:        A simple starter kit for any module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Starter
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Module-Starter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Pod::Usage) >= 1.21
# Software::LicenseUtils version from Software::License in META
BuildRequires:  perl(Software::LicenseUtils) >= 0.103005
# Tests:
# base not used
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
# File::Temp not used
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(version) >= 0.77
Requires:  perl(ExtUtils::Manifest)
# Software::LicenseUtils version from Software::License in META
Requires:  perl(Software::LicenseUtils) >= 0.103005

%{?perl_default_filter}
# Filter in-lined Perl code from lib/Module/Starter/Simple.pm
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((ExtUtils::MakeMaker|inc::Module::Install|Module::Build|Test::More)\\)

%description
This is a CPAN module/utility to assist in the creation of new modules in a
sensible and sane fashion.  Unless you're interested in extending the
functionality of this module, you should examine the documentation for
'module-starter', for information on how to use this tool.

It is noted that there are a number of extensions to this tool, including
plugins to create modules using templates as recommended by Damian Conway's
"Perl Best Practices" (O'Reilly, 2005).  (See also the package
perl-Module-Starter-PBP for the aforementioned templates.)


%prep
%setup -q -n Module-Starter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset DONT_DEL_TEST_DIST MODULE_STARTER_DIR RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man[13]/*.[13]*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.77-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.77-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.77-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Petr Pisar <ppisar@redhat.com> - 1:1.77-1
- 1.77 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.76-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.76-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.76-2
- Perl 5.30 rebuild

* Tue Mar 12 2019 Petr Pisar <ppisar@redhat.com> - 1:1.76-1
- 1.76 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.75-2
- Perl 5.28 rebuild

* Fri Jun 15 2018 Petr Pisar <ppisar@redhat.com> - 1:1.75-1
- 1.75 bump

* Wed Jun 13 2018 Petr Pisar <ppisar@redhat.com> - 1:1.74-1
- 1.74 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Petr Pisar <ppisar@redhat.com> - 1:1.73-1
- 1.73 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.72-2
- Perl 5.26 rebuild

* Thu Apr 06 2017 Petr Pisar <ppisar@redhat.com> - 1:1.72-1
- 1.72 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.71-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.71-2
- Perl 5.22 rebuild

* Mon Feb 02 2015 Petr Pisar <ppisar@redhat.com> - 1:1.71-1
- 1.71 bump

* Wed Oct 15 2014 Petr Pisar <ppisar@redhat.com> - 1:1.62-5
- Revert the previous license identifiers patches which broke
  Software::License
- Produce valid Software::License identifiers (bug #1152319)

* Tue Oct 14 2014 Petr Pisar <ppisar@redhat.com> - 1:1.62-4
- Produce valid license identifiers (bug #1152319)
- Document the default license is artistic2

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.62-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 10 2013 Petr Pisar <ppisar@redhat.com> - 1:1.62-1
- 1.62 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1:1.60-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Petr Pisar <ppisar@redhat.com> - 1:1.60-2
- Drop build-time dependencies for unused author tests

* Fri Oct 26 2012 Petr Pisar <ppisar@redhat.com> - 1:1.60-1
- 1.60 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1:1.58-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 1:1.58-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- remove explicit requires
- update filtering macros

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.54-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.54-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> 1:1.54-1
- update
- rebuild with perl-5.12

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1:1.52-1
- auto-update to 1.52 (by cpan-spec-update 0.01)
- added a new br on perl(ExtUtils::Command) (version 0)
- added a new br on perl(ExtUtils::MakeMaker) (version 0)
- added a new br on perl(File::Spec) (version 0)
- added a new br on perl(Getopt::Long) (version 0)
- added a new br on perl(Pod::Usage) (version 0)
- added a new br on perl(Test::More) (version 0)
- added a new req on perl(ExtUtils::Command) (version 0)
- added a new req on perl(File::Spec) (version 0)
- added a new req on perl(Getopt::Long) (version 0)
- added a new req on perl(Pod::Usage) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.50-2
- correct source

* Wed Nov 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.50-1
- update to 1.50

* Sat Jul 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.470-1
- update to 1.470

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.42-5
- rebuild for new perl

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.42-4
- bump for mass rebuild

* Mon Aug 07 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.42-3
- bump for build & release

* Sun Aug 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.42-2
- add additional br's for test suite:
  perl(Test::Pod::Coverage), perl(Test::Pod)

* Sat Aug 05 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.42-1
- Initial spec file for F-E
