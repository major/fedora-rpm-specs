Name: 		perl-Test-Inline
Version: 	2.214
Release: 	14%{?dist}
Summary: 	Test::Inline Perl module
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Test-Inline
Source0: 	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Inline-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires:	%{__perl}
BuildRequires:	%{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

BuildRequires:	perl(Algorithm::Dependency) >= 1.02
BuildRequires:	perl(Class::Autouse) >= 1.29
BuildRequires:	perl(Config::Tiny) >= 2.00
BuildRequires:	perl(File::chmod) >= 0.31
BuildRequires:	perl(File::Find::Rule) >= 0.26
BuildRequires:	perl(File::Flat) >= 1.00
BuildRequires:	perl(File::Remove) >= 0.37
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long) >= 2.34
BuildRequires:	perl(List::Util) >= 1.19
BuildRequires:	perl(Params::Util) >= 0.21
BuildRequires:	perl(Test::ClassAPI) >= 1.02
BuildRequires:	perl(Test::More) >= 0.42
BuildRequires:	perl(Test::Script)

# For improved tests
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  perl(Perl::MinimumVersion) >= 1.20

# Required by t/00-report-prereqs.t
BuildRequires:	perl(Encode) >= 3.08
BuildRequires:	perl(File::Temp) >= 0.2311
BuildRequires:	perl(JSON::PP) >= 4.06
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(YAML)
BuildRequires:	perl(autodie)


# RPM misses these deps
Requires:	perl(File::Flat)
Requires:	perl(File::Find::Rule)

# Filter duplicate unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$

%description
Test::Inline allows you to inline your tests next to the code being tested.

%prep
%setup -q -n Test-Inline-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes
%license LICENSE
%{_bindir}/*
%{perl_vendorlib}/Test
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.214-8
- Modernize spec.
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.214-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.214-3
- Perl 5.34 rebuild

* Tue Apr 27 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.214-2
- Fix Source0-URL.

* Tue Apr 27 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.214-1
- Upstream update.
- Rework BRs.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-19
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-16
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-13
- Perl 5.26 rebuild

* Tue May 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.213-12
- Eliminate inc. BR: perl(inc::Module::Install) (RHBZ#1454702).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.213-8
- Remove %%defattr.
- Modernize spec.
- Add %%license.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.213-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-6
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.213-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.213-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 2.213-2
- Perl 5.18 rebuild

* Wed Apr 17 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.213-1
- Upstream update.

* Mon Feb 18 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.212-8
- Fix changelog day of weeks (Fix Fedora_19_Mass_Rebuild FTBFS).
- BR: perl(ExtUtils::MakeMaker) (Fix Fedora_19_Mass_Rebuild FTBFS).
- Modernize spec-file.
- Filter duplicate unversioned R:'s.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.212-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.212-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 2.212-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.212-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.212-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.212-1
- Upstream update.

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.211-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.211-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.211-1
- Upstream update.

* Wed Jun 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.210-1
- Upstream update.

* Fri Feb 27 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.208-5
- Adjust minimum perl version in META.yml (Add Test-Inline-2.208.diff).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.208-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 02 2008 Ralf Corsépius <rc040203@freenet.de> - 2.208-3
- BR: perl(List::Utils) >= 1.19

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.208-2
- rebuild for new perl

* Wed Jan 02 2008 Ralf Corsépius <rc040203@freenet.de> - 2.208-1
- Upstream update.
- Update build deps.
- Re-enable AUTOMATED_TESTING.

* Wed Sep 19 2007 Ralf Corsépius <rc040203@freenet.de> - 2.207-1
- Upstream update.
- Disable AUTOMATED_TESTING.

* Tue Aug 07 2007 Ralf Corsépius <rc040203@freenet.de> - 2.205-1
- Upstream update.

* Tue Jul 10 2007 Ralf Corsépius <rc040203@freenet.de> - 2.202-1
- Upstream update.

* Thu Jan 18 2007 Ralf Corsépius <rc040203@freenet.de> - 2.201-2
- BR: perl(File::Remove).

* Thu Jan 18 2007 Ralf Corsépius <rc040203@freenet.de> - 2.201-1
- Upstream update.
- Don't chmod -x Changes (Fixed upstream).
- BR: perl(File::Flat) >= 1.00.
- Inline perl-Test-Inline-filter-requires.sh.

* Wed Oct 04 2006 Ralf Corsépius <rc040203@freenet.de> - 2.105-2
- Activate AUTOMATED_TESTING (t/99_author.t).

* Wed Oct 04 2006 Ralf Corsépius <rc040203@freenet.de> - 2.105-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.103-4
- Mass rebuild.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 2.103-3
- Rebuild for perl-5.8.8.

* Fri Oct  7 2005 Paul Howarth <paul@city-fan.org> - 2.103-2
- Minor spec file cleanup
- Add BR: perl(Test::Pod) for extra test coverage

* Thu Sep 29 2005 Ralf Corsepius <ralf@links2linux.de> - 2.103-1
- Upstream update.
- Update BR's.

* Fri Sep 23 2005 Ralf Corsepius <ralf@links2linux.de> - 2.102-1
- Upstream update.

* Wed Sep 14 2005 Ralf Corsepius <ralf@links2linux.de> - 2.101-1
- Upstream update.

* Tue Sep 13 2005 Ralf Corsepius <ralf@links2linux.de> - 2.100-1
- Add filter-requires to filter bogus perl(script).

* Mon Aug 22 2005 Ralf Corsepius <ralf@links2linux.de> - 2.100-0
- Update to 2.100.
