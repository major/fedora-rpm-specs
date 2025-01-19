Name:		perl-Class-Autouse
Version:	2.01
Release:	41%{?dist}
Summary:	Run-time class loading on first method call
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-Autouse
Source0:	https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Class-Autouse-%{version}.tar.gz
# Update Makefile.PL to not use Module::Install::DSL CPAN RT#148302
Patch0:         Class-Autouse-2.01-Remove-using-of-MI-DSL.patch

# Upstream does its very best to prevent us from running them.
%bcond_with	xt_tests

BuildArch:	noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

BuildRequires:	perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl(File::Temp) >= 0.17
BuildRequires:	perl(List::Util) >= 1.18
BuildRequires:	perl(prefork)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(vars)

BuildRequires:  perl(inc::Module::Install)

# for xt tests
%if %{with xt_tests}
BuildRequires:	perl(Perl::MinimumVersion) >= 1.27
BuildRequires:	perl(Pod::Simple) >= 3.14
BuildRequires:	perl(Test::Pod) >= 1.44
BuildRequires:	perl(Test::MinimumVersion) >= 0.101080
BuildRequires:	perl(Test::CPAN::Meta) >= 0.17
%endif

%description
Class::Autouse allows you to specify a class the will only load when a
method of that class is called. For large classes that might not be used
during the running of a program, such as Date::Manip, this can save you
large amounts of memory, and decrease the script load time.

%prep
%setup -q -n Class-Autouse-%{version}
%patch -P0 -p1
rm -r inc/
sed -i -e '/^inc\//d' MANIFEST

%build
AUTOMATED_TESTING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test
%if %{with xt_tests}
# Manually invoke xt-tests
AUTOMATED_TESTING=1 PERL_DL_NONLAZY=1 %{__perl} "-MExtUtils::Command::MM" "-e" "test_harness(0, 'inc', 'blib/lib', 'blib/arch')" xt/*.t
%endif

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 14 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.01-36
- Remove inc/ from MANIFEST.

* Wed May 10 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-35
- Update Makefile.PL to not use Module::Install::DSL

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.01-33
- Modernize spec.
- Convert license to SPDX.
- Update sources to sha512.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-31
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-28
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-25
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-22
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-19
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-16
- Perl 5.26 rebuild

* Mon May 22 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.01-15
- Eliminate inc. perl(inc::Module::Install) (RHBZ#1452994).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.01-12
- Remove %%defattr.
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-10
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 2.01-6
- Perl 5.18 rebuild

* Sun Feb 17 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.01-5
- BR: perl(ExtUtils::MakeMaker) (Fix Fedora_19_Mass_Rebuild FTBFS).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 2.01-2
- Perl 5.16 rebuild

* Sun Feb 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.01-1
- Upstream update.
- Adjust BR:'s.
- Modernize spec.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.00-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.00-1
- Upstream update.
- Adjust BR:'s.
- Add %%bcond_with xt_tests.

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29-10
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jul 20 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.29-9
- Reenable pmv test.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.29-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.29-5
- Adjust minimum perl version in META.yml (Add Class-Autouse-1.29.diff).
- BR: perl(List::Util) >= 1.19.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.29-3
- rebuild for new perl

* Sun Nov 25 2007 Ralf Corsépius <rc040203@freenet.de> - 1.29-2
- Add BR: perl(Test-MinimumVersion).

* Tue Nov 20 2007 Ralf Corsépius <rc040203@freenet.de> - 1.29-1
- Upstream update.

* Wed Sep 05 2007 Ralf Corsépius <rc040203@freenet.de> - 1.28-1
- Upstream update.
- Update license.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.27-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.26-2
- Mass rebuild.

* Thu Apr 20 2006 Ralf Corsépius <rc040203@freenet.de> - 1.26-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.21-3
- Rebuild for perl-5.8.8.

* Wed Feb 01 2006 Ralf Corsepius <rc040203@freenet.de> - 1.21-2
- Revert to 1.21 (List::Util in Perl is too old).

* Sat Jan 14 2006 Ralf Corsepius <rc040203@freenet.de> - 1.24-1
- Upstream update.

* Wed Sep 28 2005 Ralf Corsepius <rc040203@freenet.de> - 1.21-1
- Upstream update.
- Fix bogus dep on perl(Carp).

* Thu Sep 15 2005 Ralf Corsepius <rc040203@freenet.de> - 1.20-2
- Spec cleanup.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 1.20-1
- Spec cleanup.
- FE submission.
