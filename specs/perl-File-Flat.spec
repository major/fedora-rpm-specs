Name: 		perl-File-Flat
Version: 	1.07
Release: 	14%{?dist}
Summary: 	Implements a flat filesystem
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/File-Flat
Source0: 	https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Flat-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires: perl-generators
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Copy::Recursive) >= 0.35
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Remove) >= 0.38
BuildRequires: perl(File::Spec) >= 0.85
BuildRequires: perl(File::Temp) >= 0.17
BuildRequires: perl(IO::File)
BuildRequires: perl(prefork) >= 0.02
BuildRequires: perl(strict)
BuildRequires: perl(Test::ClassAPI) >= 1.02
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(vars)
BuildRequires: perl(warnings)


# For improved tests
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::MinimumVersion)
BuildRequires: perl(Test::CPAN::Meta)


%description
File::Flat implements a flat filesystem. A flat filesystem is a filesystem
in which directories do not exist. It provides an abstraction over any 
normal filesystem which makes it appear as if directories do not exist.

%prep
%setup -q -n File-Flat-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.07-8
- Modernize spec.
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.07-1
- Upstream update.

* Mon Aug 03 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.06-1
- Upstream update.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.05-1
- Upstream update.
- Rework deps.
- Reflect upstream URL having changed.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-29
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-26
- Perl 5.26 rebuild

* Tue May 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-25
- Next try.

* Tue May 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-24
- Eliminate inc. BR: perl(inc::Module::Install) (RHBZ#1454594).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-22
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ralf Corsépius <corsepiu@fedoraproject.de> - 1.04-20
- Remove %%defattr.
- Add %%license.
- Modernize spec.
- Don't remove 99_pmv.t.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-18
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.04-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.04-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.04-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.04-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 01 2008 Ralf Corsépius <rc040203@freenet.de> - 1.04-2
- BR: perl(Test::CPAN::Meta).

* Mon Apr 07 2008 Ralf Corsépius <rc040203@freenet.de> - 1.04-1
- Upstream update.
- Remove dep on perl(File::Slurp).

* Fri Mar 14 2008 Ralf Corsépius <rc040203@freenet.de> - 1.03-1
- Upstream update.
- BR: perl(Test::MinimumVersion).

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.00-3
- rebuild for new perl

* Sun Sep 02 2007 Ralf Corsépius <rc040203@freenet.de> - 1.00-2
- License update.

* Thu Jan 18 2007 Ralf Corsépius <rc040203@freenet.de> - 1.00-1
- Upstream update.
- BR: perl(File::Copy::Recursive).
- Drop BR: perl(File::NCopy).
- Activate AUTOMATED_TESTING (t/99_author.t).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.96-3
- Mass rebuild.

* Thu Jul 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0.96-2
- BR: perl(Test::Pod).

* Thu Jul 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0.96-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 0.95-3
- Rebuild for perl-5.8.8.

* Mon Sep 19 2005 Ralf Corsepius <rc040203@freenet.de> - 0.95-2
- Spec file cleanup.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 0.95-1
- Spec file cleanup.
- FE submission.

* Tue Jun 28 2005 Ralf Corsepius <ralf@links2linux.de> - 0.95-0.pm.1
- Initial packman version.
