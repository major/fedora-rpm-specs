Name:           perl-HTTP-BrowserDetect
Summary:        Determine the Web browser, version, and platform from an HTTP user agent string
Version:        3.41
Release:        2%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-BrowserDetect
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-BrowserDetect-%{version}.tar.gz 
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP) >= 4.04
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Path::Tiny)
# XXX: BuildRequires:  perl(Test::Code::TidyAll) >= 0.24
# XXX: BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

This module is based upon the JavaScript browser detection code available
at http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

%prep
%setup -q -n HTTP-BrowserDetect-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

%check
%{make_build} test

%files
%license LICENSE
%doc Changes CONTRIBUTORS TODO
%{perl_vendorlib}/HTTP/
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 13 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 3.41-1
- Update to 3.41

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 22 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 3.40-1
- Update to 3.40

* Mon Sep 11 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 3.39-1
- Update to 3.39
- migrated to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 3.38-1
- Update to 3.38

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 18 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 3.37-1
- Update to 3.37

* Sun Sep 04 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 3.36-1
- Update to 3.36

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 24 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 3.35-1
- Update to 3.35

* Sun Aug 08 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 3.34-1
- Update to 3.34

* Sun Jul 25 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 3.33-1
- Update to 3.33

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.31-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.31-1
- Update to 3.31

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.30-1
- Update to 3.30

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.28-1
- Update to 3.28

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.27-2
- Perl 5.32 rebuild

* Sun Apr 19 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.27-1
- Update to 3.27

* Sun Mar 22 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.26-1
- Update to 3.26

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.25-1
- Update to 3.25

* Fri Nov 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.24-1
- Update to 3.24
- Replace calls to perl with /usr/bin/perl
- Replace calls to %%{__perl} with /usr/bin/perl
- Replace calls to "make install" with %%{make_install}
- Replace calls to make with %%{make_build}

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.23-2
- Perl 5.30 rebuild

* Sun Apr 07 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.23-1
- Update to 3.23

* Sun Mar 10 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.22-1
- Update to 3.22

* Sun Feb 10 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.21-1
- Update to 3.21

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 3.20-1
- Update to 3.20

* Sun Oct 14 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 3.19-1
- Update to 3.19

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.16-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 3.16-1
- Update to 3.16
- Switch to Makefile.PL as a build-system

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.14-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 29 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 3.14-1
- Update to 3.14

* Sat May 21 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 3.13-1
- Update to 3.13

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.12-2
- Perl 5.24 rebuild

* Fri May 06 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 3.12-1
- Update to 3.12

* Thu Mar 31 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 3.10-1
- Update to 3.10

* Tue Mar 01 2016 Petr Šabata <contyk@redhat.com> - 3.00-1
- 3.00 bump; tablets are no longer considered mobile devices

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Šabata <contyk@redhat.com> - 2.08-1
- 2.08 bump

* Thu Nov 19 2015 Petr Šabata <contyk@redhat.com> - 2.07-1
- 2.07 bump

* Thu Jul 30 2015 Petr Šabata <contyk@redhat.com> - 2.05-1
- 2.05 bump

* Thu Jun 25 2015 Petr Šabata <contyk@redhat.com> - 2.04-1
- 2.04 bump

* Sun Jun 21 2015 Petr Šabata <contyk@redhat.com> - 2.03-1
- 2.03 bump

* Thu Jun 18 2015 Petr Šabata <contyk@redhat.com> - 2.02-1
- 2.02 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-2
- Perl 5.22 rebuild

* Mon Apr 27 2015 Petr Šabata <contyk@redhat.com> - 2.01-1
- 2.01 bump

* Tue Mar 31 2015 Petr Šabata <contyk@redhat.com> - 2.00-1
- 2.00 bump
- This version removes the user_agent() function

* Fri Mar 20 2015 Petr Šabata <contyk@redhat.com> - 1.78-1
- 1.76 bump

* Wed Nov 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-1
- 1.75 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct  4 2013 Paul Howarth <paul@city-fan.org> - 1.61-1
- Update to 1.61 (see Changes for details)
- Specify all dependencies
- Package CONTRIBUTORS file
- Recode documentation as UTF-8
- Remove spurious exec permission from perl module file
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Drop redundant %%{?perl_default_filter}
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.21-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.21-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.21-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Steven Pritchard <steve@kspei.com> 1.21-1
- Update to 1.21.
- BR Module::Build and build with that.
- Add LICENSE and TODO to docs.
- Drop BR for Exporter, FindBin (both core modules), and YAML::Tiny, and
  add BR YAML.

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.10-3
- Rebuild to fix problems with vendorarch/lib (#661697)

* Wed May 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.10-2
- bump

* Wed May 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.10-1
- PERL_INSTALL_DIR => DESTDIR
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.10)
- added a new br on perl(Data::Dump) (version 0)
- added a new br on perl(Exporter) (version 0)
- added a new br on perl(FindBin) (version 0)
- added a new br on perl(Test::More) (version 0)
- added a new br on perl(YAML::Tiny) (version 0)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.99-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.99-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.99-2
- rebuild for new perl

* Fri May 18 2007 Steven Pritchard <steve@kspei.com> 0.99-1
- Update to 0.99.
- Update Source0 URL.
- Improve Summary and description.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.98-4
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Tue Sep 05 2006 Steven Pritchard <steve@kspei.com> 0.98-3
- Fix find option order.
- Use canonical Source0 URL.

* Fri Mar 10 2006 Steven Pritchard <steve@kspei.com> 0.98-2
- Improve Summary.

* Thu Aug 18 2005 Steven Pritchard <steve@kspei.com> 0.98-1
- Specfile autogenerated.
