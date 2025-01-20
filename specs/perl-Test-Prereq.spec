Name:           perl-Test-Prereq
Version:        2.005
Release:        2%{?dist}
Summary:        Check if Makefile.PL has the right pre-requisites
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Prereq
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Prereq-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 4:5.22.0
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Extract::Use)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 1.00
# Optional Tests
BuildRequires:  perl(Test::Manifest) >= 1.21
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
# (none)

%description
The prereq_ok() function examines the modules it finds in blib/lib/,
blib/script, and the test files it finds in t/ (and test.pl). It figures out
which modules they use and compares that list of modules to those in the
PREREQ_PM section of Makefile.PL.

If you use Module::Build, see Test::Prereq::Build instead.

%prep
%setup -q -n Test-Prereq-%{version}

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
%{_mandir}/man3/Test::Prereq.3*
%{_mandir}/man3/Test::Prereq::Build.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan  3 2025 Paul Howarth <paul@city-fan.org> - 2.005-1
- Update to 2.005 (rhbz#2335386)
  - Refresh distro
  - Move to BRIANDFOY user
  - Add SECURITY.md policy

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Paul Howarth <paul@city-fan.org> - 2.003-1
- Update to 2.003
  - Uniq the list of modules this extracts; Module::Extract::Use 1.045 changed
    slightly to return a bit more than it used to do

* Sat Oct 12 2019 Paul Howarth <paul@city-fan.org> - 2.002-11
- Spec tidy-up
  - Use author-independent source URL
  - Use %%{make_build} and %%{make_install}

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.002-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.002-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.002-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Paul Howarth <paul@city-fan.org> - 2.002-1
- Update to 2.002
  - No more filtering out core modules (some things are ejected from core!)
  - Switched from Module::Info to Module::Extract::Use
  - Switched from old Test::Builder to Test::Builder::Module
  - Fix postderef (GH#14)
  - Support test_requires in Module::Build (GH#15)
- License changed to Artistic 2.0

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.039-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.039-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Petr Šabata <contyk@redhat.com> - 1.039-1
- 1.039 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.038-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Petr Šabata <contyk@redhat.com> - 1.038-3
- Avoid FTBFS with perl5.22

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.038-2
- Perl 5.22 rebuild

* Thu Nov 06 2014 Petr Šabata <contyk@redhat.com> - 1.038-1
- 1.038 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.037-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.037-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.037-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.037-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.037-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.037-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.037-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.037-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.037-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.037-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.037-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.037-4
- Mass rebuild with perl-5.12.0

* Wed Apr 21 2010 Petr Pisar <ppisar@redhat.com> - 1.037-3
- Disable t/get_from_prereqs.t test because it requires interactive
  configuration <https://rt.cpan.org/Public/Bug/Display.html?id=56785> and
  network access (#539015)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.037-2
- rebuild against perl 5.10.1

* Fri Oct 30 2009 Stepan Kasal <skasal@redhat.com> - 1.037-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.036-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Steven Pritchard <steve@kspei.com> 1.036-1
- Update to 1.036.
- Add some dependencies when building with --with-check.

* Wed Dec 10 2008 Steven Pritchard <steve@kspei.com> 1.034-1
- Update to 1.034.

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.033-2
- rebuild for new perl

* Fri Mar 23 2007 Steven Pritchard <steve@kspei.com> 1.033-1
- Update to 1.033.

* Wed Jan 17 2007 Steven Pritchard <steve@kspei.com> 1.032-1
- Update to 1.032.
- Use fixperms macro instead of our own chmod incantation.
- Add LICENSE to docs.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.031-2
- Fix find option order.

* Wed May 24 2006 Steven Pritchard <steve@kspei.com> 1.031-1
- Update to 1.031.

* Fri Mar 24 2006 Steven Pritchard <steve@kspei.com> 1.030-1
- Specfile autogenerated by cpanspec 1.64.
- Fix License.
- Drop explicit Requires.
- Disable tests by default (uses network).
