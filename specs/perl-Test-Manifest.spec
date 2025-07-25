Summary:        Test case module for Perl
Name:           perl-Test-Manifest
Version:        2.026
Release:        2%{?dist}
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Manifest
Source0:        https://www.cpan.org/modules/by-module/Test/Test-Manifest-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(version) >= 0.86
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
Requires:       perl(File::Spec)
Requires:       perl(Test::Harness)

%description
MakeMaker assumes that you want to run all of the .t files in the t/ directory
in ASCII-betical order during make test unless you say otherwise. This leads to
some interesting naming schemes for test files to get them in the desired
order.

You can specify any order or any files that you like, though, with the test
directive to WriteMakefile.

Test::Manifest looks in the t/test_manifest file to find out which tests you
want to run and the order in which you want to run them. It constructs the
right value for MakeMaker to do the right thing.

%prep
%setup -q -n Test-Manifest-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Manifest.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Apr 14 2025 Paul Howarth <paul@city-fan.org> - 2.026-1
- Update to 2.026
  - Require a newer version.pm for v5.10.1 tests

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan  5 2025 Paul Howarth <paul@city-fan.org> - 2.025-1
- Update to 2.025
  - Refresh distro and move to BRIANDFOY
- Package new file SECURITY.md

* Wed Dec  4 2024 Paul Howarth <paul@city-fan.org> - 2.024-5
- Switch source URL from cpan.metacpan.org to www.cpan.org
- Use %%{make_build} and %%{make_install}

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.024-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  9 2024 Paul Howarth <paul@city-fan.org> - 2.024-1
- Update to 2.024
  - Refresh distro

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.023-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan  9 2022 Paul Howarth <paul@city-fan.org> - 2.023-1
- Update to 2.023
  - Fix a link in the README.pod

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.022-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Paul Howarth <paul@city-fan.org> - 2.022-1
- Update to 2.022
  - Freshen distro, remove Travis CI, add GitHub Actions
  - Fix parallel testing (CPAN RT#92604, GH#4)
- Use %%license unconditionally

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.021-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.021-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.021-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.021-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.021-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.021-2
- Perl 5.28 rebuild

* Tue May  8 2018 Paul Howarth <paul@city-fan.org> - 2.021-1
- Update to 2.021
  - Clarify that it's the Artistic License 2.0
- License changed to Artistic 2.0
- Drop legacy BuildRoot: and Group: tags
- Drop explicit %%clean section
- Drop buildroot cleaning in %%install section
- Simplify find command using -delete
- Classify build requirements by usage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-2
- Perl 5.22 rebuild

* Tue Sep  9 2014 Paul Howarth <paul@city-fan.org> - 2.02-1
- Update to 2.02
  - Fix a spelling mistake (CPAN RT#98288)
- Drop manpage patch, no longer needed
- Use %%license where possible

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.23-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Paul Howarth <paul@city-fan.org> - 1.23-1
- Update to 0.23
  - Fix bug for missing file (should warn and skip, not pass to run_t_files)
  - File path and unlink fixes for VMS (CPAN RT#32061)
- Add patch to reinstate manpage, dropped upstream
- BR:/R: perl(File::Spec) and perl(Test::Harness)
- BR: perl(base), perl(Carp), perl(Exporter) and perl(File::Spec::Functions)
- Don't use macros for commands
- Reformat %%description
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use %%{_fixperms} macro rather than our own chmod incantation
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Package LICENSE and README files

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.22-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.22-10
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-8
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.22-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-1
- 1.22
- license fix

* Fri Feb 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.17-1
- Update to 1.17.

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-5
- Rebuild for FC6.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-4
- Rebuild for FC5 (perl 5.8.8).

* Thu May 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-3
- Add dist tag.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.14-2
- rebuilt

* Tue Mar 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Wed Mar 23 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.13-1
- Update to 1.13.

* Sat Oct 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.11-1
- Update to 1.11.

* Sun Jun 13 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.93-0.fdr.2
- Bring up to date with current fedora.us perl spec template.
- Require perl >= 2:5.8.0 for vendor install dir support
  (also resolves the ExtUtils::MakeMaker version problem).

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.93-0.fdr.1
- Update to 0.93.
- Reduce directory ownership bloat.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.92-0.fdr.1
- First build.
