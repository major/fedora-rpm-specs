Name:           perl-pmtools
Version:        2.2.0
Release:        23%{?dist}
Summary:        A suite of small programs to help manage Perl modules

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/pmtools
Source:         https://cpan.metacpan.org/authors/id/M/ML/MLFISHER/pmtools-%{version}.tar.gz
# Adapt to Perl 5.26.0 POD changes, bug #1465062, CPAN RT#122210
Patch0:         pmtools-2.0.0-t_pfcat_5.26.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant) >= 1.01
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
BuildRequires:  perl(perlfaq)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This is pmtools -- a suite of small programs to help manage modules.
The names are totally preliminary, and in fact, so is the code.  We follow
the "keep it small" notion of many tiny tools each doing one thing well,
eschewing giant megatools with millions of options.

Tom Christiansen


%prep
%setup -q -n pmtools-%{version}
%patch -P 0 -p1
find . -type f -perm 755 | xargs perl -pi -MConfig -e 's{^#!/usr/bin/env perl}{$Config{startperl}}'
chmod -c a-x Changes TODO lib/Devel/Loaded.pm


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{make_build}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# Default perl's pager less fails with /dev/null on stdin (bug #2208970)
export PAGER=/usr/bin/cat
make test


%files
%license LICENSE
%doc Changes README TODO
%{_bindir}/basepods
%{_bindir}/faqpods
%{_bindir}/modpods
%{_bindir}/pfcat
%{_bindir}/plxload
%{_bindir}/pm*
%{_bindir}/podgrep
%{_bindir}/podpath
%{_bindir}/pods
%{_bindir}/podtoc
%{_bindir}/sitepods
%{_bindir}/stdpods
%{perl_vendorlib}/Devel/
%{perl_vendorlib}/pmtools.pm
%{_mandir}/man1/basepods.1*
%{_mandir}/man1/faqpods.1*
%{_mandir}/man1/modpods.1*
%{_mandir}/man1/pfcat.1*
%{_mandir}/man1/plxload.1*
%{_mandir}/man1/pm*.1*
%{_mandir}/man1/podgrep.1*
%{_mandir}/man1/podpath.1*
%{_mandir}/man1/pods.1*
%{_mandir}/man1/podtoc.1*
%{_mandir}/man1/sitepods.1*
%{_mandir}/man1/stdpods.1*
%{_mandir}/man3/Devel::Loaded.3*
%{_mandir}/man3/pmtools.3*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 31 2023 Petr Pisar <ppisar@redhat.com> - 2.2.0-18
- Convert a license tag to an SPDX syntax
- Adapt tests to changes in less-633 (bug #2208970)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-9
- Perl 5.32 rebuild

* Tue Mar 10 2020 Petr Pisar <ppisar@redhat.com> - 2.2.0-8
- Build-require perl-doc for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-2
- Perl 5.28 rebuild

* Thu Apr 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-1
- 2.2.0 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Petr Pisar <ppisar@redhat.com> - 2.0.0-9
- Adapt to Perl 5.26.0 POD changes (bug #1465062)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.0-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Petr Šabata <contyk@redhat.com> - 2.0.0-5
- Fix the build by patching faqpods to work with perlfaq in vendorlib
  This is needed following the perl-perlfaq subpackaging from perl in F24
- Correct the build time dependency list, too

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.0-3
- Perl 5.22 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb  8 2014 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.0-1
- Update to 2.0.0.

* Wed Dec 11 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.54-2
- The test suite also needs the less command in the build root (F20+).

* Wed Dec 11 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.54-1
- Update to 1.54.
- New build requirement: perl(Test::More).

* Tue Dec 10 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-1
- Update to 1.30.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.10-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.10-10
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.10-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.10-6
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.10-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.10-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.10-1
- update to 1.10
- license change to GPL+ or Artistic

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-2.1
- add BR: perl(ExtUtils::MakeMaker)

* Thu Mar 30 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-2
- New doc files: Changes and TODO.

* Wed Mar 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- Update to 1.01.
- URL updated: pmtools is now available in CPAN.
- Dropped patches pmtools-1.00-{different-tarball.patch,pmall.patch}:
  they were accepted upstream.

* Thu Mar  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-4
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-3
- Dist tag.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.00-2
- rebuilt

* Sun Feb 06 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-1
- Valid source file link found.
- Package renamed to 'perl-pmtools' in order to avoid name clash with
  the ACPI debugging tools (pmtools).

* Tue Dec 28 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.00-0.fdr.1
- The patch adds a missing target in Makefile.PL (pmeth) and renames the
  script 'pman' into 'pmman' in order to avoid a filename clash with
  the pinfo package.

* Sat Feb 28 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.00-0.fdr.0
- Initial build for fedora.us
