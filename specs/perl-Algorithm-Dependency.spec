Name: 		perl-Algorithm-Dependency
Version: 	1.112
Release: 	11%{?dist}
Summary: 	Algorithmic framework for implementing dependency trees
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Algorithm-Dependency
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Algorithm-Dependency-%{version}.tar.gz

BuildArch: noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)		>= 0.80
BuildRequires: perl(Test::ClassAPI)	>= 0.6
BuildRequires: perl(Test::More)		>= 0.47
BuildRequires: perl(Params::Util)	>= 0.31
BuildRequires: perl(List::Util)		>= 1.11

BuildRequires: perl(Test::Pod)		>= 1.00
BuildRequires: perl(Test::CPAN::Meta)	>= 0.12
BuildRequires: perl(Perl::MinimumVersion) >= 1.20
BuildRequires: perl(Test::MinimumVersion) >= 0.008

%description
Algorithm::Dependency is a framework for creating simple read-only
dependency hierarchies, where you have a set of items that rely on other
items in the set, and require actions on them as well.

%prep
%setup -q -n Algorithm-Dependency-%{version}

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
%{perl_vendorlib}/Algorithm
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.112-5
- Convert licence to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.112-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.112-1
- Update to 1.112.
- Modernize spec.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-9
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.111-1
- Update to 1.111.
- Reflect upstream URL having changed.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.110-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-28
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.110-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.110-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-25
- Perl 5.26 rebuild

* Thu May 18 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.110-24
- Eliminate inc. BR: perl(inc::Module::Install) (RHBZ#1452002).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.110-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-22
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.110-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.110-20
- Remove %%defattr.
- Add %%license.
- Use NO_PACKLIST.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-18
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.110-14
- Perl 5.18 rebuild

* Sun Feb 17 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.110-13
- Add BR: perl(ExtUtils::MakeMaker) (Fix Fedora_19_Mass_Rebuild FTBFS).
- Spec-file cleanup.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.110-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.110-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.110-6
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 25 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.110-5
- Reactivate pmv test.

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.110-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.110-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.110-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.108-1
- Upstream update.
- BR: perl(Test::CPAN::Meta).

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.106-2
- rebuild for new perl

* Mon Jan 21 2008 Ralf Corsépius <rc040203@freenet.de> - 1.106-1
- Upstream update.

* Sun Nov 25 2007 Ralf Corsépius <rc040203@freenet.de> - 1.104-2
- Add BR: perl(Test-MinimumVersion).

* Tue Nov 20 2007 Ralf Corsépius <rc040203@freenet.de> - 1.104-1
- Upstream update.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.103-2
- Update license tag.

* Sun Jul 29 2007 Ralf Corsépius <rc040203@freenet.de> - 1.103-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.102-2
- Mass rebuild.

* Mon Apr 24 2006 Ralf Corsépius <rc040203@freenet.de> - 1.102-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.101-2
- Rebuild for perl-5.8.8.

* Wed Oct 12 2005 Ralf Corsepius <rc040203@freenet.de> - 1.101-1
- Upstream update.

* Sat Sep 17 2005 Ralf Corsepius <rc040203@freenet.de> - 1.04-3
- Spec cleanup.

* Thu Sep 15 2005 Paul Howarth <paul@city-fan.org> - 1.04-2
- Fix Source0 URL
- Fix perl(Params::Util) BuildReq version
- Add BR: perl(Test::Pod) for improved test coverage

* Thu Sep 15 2005 Ralf Corsepius <rc040203@freenet.de> - 1.04-1
- Upstream update.
- Drop shipping README.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 1.03-1
- Spec file cleanup.
- FE submission.
