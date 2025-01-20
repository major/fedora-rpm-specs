Name:           perl-Object-InsideOut
Version:        4.05
Release:        27%{?dist}
Summary:        Comprehensive inside-out object support module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-InsideOut
Source0:        https://cpan.metacpan.org/modules/by-module/Object/Object-InsideOut-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(attributes)
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper) >= 2.131
BuildRequires:  perl(Exception::Class) >= 1.32
BuildRequires:  perl(Scalar::Util) >= 1.23
# Optional run-time
%if %{undefined perl_bootstrap}
BuildRequires:  perl(Math::Random::MT::Auto) >= 6.18
%endif
BuildRequires:  perl(Want) >= 0.21
# Test only
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(threads)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads::shared)
# Optional tests
BuildRequires:  perl(Storable)
# Dependencies
Requires:       perl(Data::Dumper) >= 2.131
Requires:       perl(Scalar::Util) >= 1.23

# Remove underspecified dependencies
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Object::InsideOut\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Scalar::Util\\)

%if %{defined perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Math::Random::MT::Auto\\)
%endif

%description
This module provides comprehensive support for implementing classes using the
inside-out object model.

This module implements inside-out objects as anonymous scalar references that
are blessed into a class with the scalar containing the ID for the object
(usually a sequence number). Object data (i.e., fields) are stored within the
class's package in either arrays indexed by the object's ID, or hashes keyed
to the object's ID.

%prep
%setup -q -n Object-InsideOut-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc examples/ Changes README
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/Object/
%{_mandir}/man3/Bundle::Object::InsideOut.3*
%{_mandir}/man3/Object::InsideOut.3*
%{_mandir}/man3/Object::InsideOut::Metadata.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-25
- Perl 5.40 re-rebuild of bootstrapped packages

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-24
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-20
- Perl 5.38 re-rebuild of bootstrapped packages

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-19
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-16
- Perl 5.36 re-rebuild of bootstrapped packages

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-12
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Paul Howarth <paul@city-fan.org> - 4.05-1
- 4.05 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-7
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-2
- Perl 5.26 rebuild

* Wed Mar  1 2017 Paul Howarth <paul@city-fan.org> - 4.04-1
- 4.04 bump

* Mon Feb 27 2017 Paul Howarth <paul@city-fan.org> - 4.03-1
- 4.03 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Paul Howarth <paul@city-fan.org> - 4.02-8
- Bootstrapping done

* Mon Oct 31 2016 Paul Howarth <paul@city-fan.org> - 4.02-7
- Bootstrap build for Math::Random::MT::Auto on ppc64 and ppc64le

* Mon Sep 12 2016 Paul Howarth <paul@city-fan.org> - 4.02-6
- Bootstrapping done
- Simplify find command using -delete
- File permissions from tarball no longer need fixing
- Drop redundant %%{?perl_default_filter}

* Mon Sep 12 2016 Paul Howarth <paul@city-fan.org> - 4.02-5
- Bootstrap build for Math::Random::MT::Auto on aarch64

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Petr Pisar <ppisar@redhat.com> - 4.02-1
- 4.02 bump

* Wed Aug 26 2015 Petr Pisar <ppisar@redhat.com> - 3.99-1
- 3.99 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.98-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.98-8
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.98-7
- Perl 5.22 rebuild

* Thu Nov 27 2014 Paul Howarth <paul@city-fan.org> - 3.98-6
- Bootstrapping done

* Tue Nov 18 2014 Paul Howarth <paul@city-fan.org> - 3.98-5
- Bootstrap build for Math::Random::MT::Auto on arm

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.98-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.98-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 08 2013 Petr Pisar <ppisar@redhat.com> - 3.98-1
- 3.98 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.97-5
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.97-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 3.97-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Petr Pisar <ppisar@redhat.com> - 3.97-1
- 3.97 bump

* Tue Oct 02 2012 Petr Pisar <ppisar@redhat.com> - 3.96-1
- 3.96 bump

* Wed Jul 25 2012 Jitka Plesnikova <jplesnik@redhat.com> - 3.95-1
- 3.95 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 3.94-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 3.94-2
- Perl 5.16 rebuild

* Fri May 11 2012 Petr Pisar <ppisar@redhat.com> - 3.94-1
- 3.94 bump

* Tue Apr 10 2012 Petr Pisar <ppisar@redhat.com> - 3.93-1
- 3.93 bump

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 3.92-1
- 3.92 bump

* Thu Feb 23 2012 Petr Pisar <ppisar@redhat.com> - 3.91-1
- 3.91 bump

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 3.89-1
- 3.89 bump

* Fri Jan 27 2012 Petr Pisar <ppisar@redhat.com> - 3.88-2
- Finish bootstrapping Math::Random::MT::Auto

* Fri Jan 27 2012 Petr Pisar <ppisar@redhat.com> - 3.88-1
- 3.88 bump
- Do not package tests
- Bootstrap new Math::Random::MT::Auto version

* Thu Jan 19 2012 Petr Pisar <ppisar@redhat.com> - 3.87-1
- 3.87 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Iain Arnell <iarnell@gmail.com> 3.84-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 3.81-3
- Perl mass rebuild

* Tue Jul 19 2011 Iain Arnell <iarnell@gmail.com> 3.81-2
- fix provides filter
- on filter requires when bootstrapping
- remove unnecessary explicit requires

* Sat Jul 02 2011 Iain Arnell <iarnell@gmail.com> 3.81-1
- minimize the impact of perl_bootstrap on testing; it's only
  perl-Math-Random-MT-Auto which causes circular deps and is
  automatically skipped in tests if not available

* Sat Jul 02 2011 Iain Arnell <iarnell@gmail.com> 3.81-1
- update to latest upstream version

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.79-2
- use perl_bootstrap macro

* Fri Feb 25 2011 Iain Arnell <iarnell@gmail.com> 3.79-1
- update to latest upstream version

* Sat Feb 19 2011 Iain Arnell <iarnell@gmail.com> 3.56-8
- only filter unversioned perl(Object::InsideOut) from provides

* Thu Feb 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.56-7
- add into filter requires on Object::InsideOut

* Tue Feb 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.56-6
- clean spec, add correct filters

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.56-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.56-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.56-2
- rebuild against perl 5.10.1

* Tue Aug 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 3.56-1
- auto-update to 3.56 (by cpan-spec-update 0.01)
- altered br on perl(Scalar::Util) (1.19 => 1.21)
- added a new req on perl(B) (version 0)
- added a new req on perl(Config) (version 0)
- added a new req on perl(Data::Dumper) (version 0)
- added a new req on perl(Exception::Class) (version 1.29)
- added a new req on perl(Scalar::Util) (version 1.21)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 3.55-1
- auto-update to 3.55 (by cpan-spec-update 0.01)
- added a new br on perl(ExtUtils::MakeMaker) (version 0)
- added a new br on perl(Data::Dumper) (version 0)
- added a new br on perl(Scalar::Util) (version 1.19)
- added a new br on perl(Config) (version 0)
- added a new br on perl(Test::More) (version 0.5)
- altered br on perl(Exception::Class) (1.22 => 1.29)
- added a new br on perl(B) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 3.51-1
- update to 3.51
- replace filter-provides.sh style filtering with inline

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.38-1
- 3.38

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.06-2
- rebuild for new perl

* Tue Oct 10 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.06-1
- update to 2.06
- add additional BRs: perl(Test::Pod[::Coverage])

* Mon Sep 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.02-1
- update to 2.02

* Tue Sep 05 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.52-1
- update to 1.52

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.51-1
- update to 1.51, which now has a BR of perl(Want)
- rebuild per mass rebuild

* Fri Aug 11 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.49-1
- update to 1.49

* Sat Aug 05 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.48-1
- update to 1.48
- drop some unneeded bits from the spec

* Wed Jul  5 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.45-1
- bump release for build

* Mon Jul  3 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.45-0.1
- corrected url's.

* Sat Jul 01 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.45-0
- Initial spec file for F-E
