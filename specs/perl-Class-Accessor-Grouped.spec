# Use optional Class::XSAccessor
%bcond_without perl_Class_Accessor_Grouped_enables_Class_XSAccessor
# Run optional test
%bcond_without perl_Class_Accessor_Grouped_enables_optional_test
# Support arbitrary method names using Sub::Name
%bcond_without perl_Class_Accessor_Grouped_enables_Sub_Name

Name:           perl-Class-Accessor-Grouped
Version:        0.10014
Release:        22%{?dist}
Summary:        Build groups of accessors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor-Grouped
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-Accessor-Grouped-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::HasCompiler)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(mro)
BuildRequires:  perl(Scalar::Util)
# Optional run-time:
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
BuildRequires:  perl(Sub::Name) >= 0.05
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Class_XSAccessor}
BuildRequires:  perl(Class::XSAccessor) >= 1.19
%endif
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
BuildRequires:  perl(Devel::Hide)
%endif
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
%if %{with perl_Class_Accessor_Grouped_enables_optional_test}
# Optional tests:
# MRO::Compat not used on Perl >= 5.9.5
BuildRequires:  perl(Package::Stash)
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Class_XSAccessor}
Recommends:     perl(Class::XSAccessor) >= 1.19
%endif
Requires:       perl(mro)
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
Recommends:     perl(Sub::Name) >= 0.05
%endif

%{?perl_default_filter}

%description
This class lets you build groups of accessors that will call different
getters and setters.

%prep
%setup -q -n Class-Accessor-Grouped-%{version}
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.10014-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.10014-12
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Petr Pisar <ppisar@redhat.com> - 0.10014-10
- Modernize a spec file

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10014-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10014-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 0.10014-2
- Perl 5.28 rebuild

* Mon Jul 02 2018 Petr Pisar <ppisar@redhat.com> - 0.10014-1
- 0.10014 bump

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10012-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10012-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10012-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10012-8
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10012-7
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10012-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10012-2
- Perl 5.22 rebuild

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 0.10012-1
- 0.10012 bump
- Test suite enhancements and 5.10 compatibility fixes

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10010-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug  9 2013 Paul Howarth <paul@city-fan.org> - 0.10010-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 0.10009-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 0.10009-1
- update to latest upstream version
- drop obsoletes/provides for old -test sub-package

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.10006-4
- Perl 5.16 rebuild

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.10006-3
- drop tests subpackage; move tests to main package documentation

* Tue Jan 17 2012 Iain Arnell <iarnell@gmail.com> - 0.10006-2
- rebuilt again for F17 mass rebuild

* Fri Jan 13 2012 Iain Arnell <iarnell@gmail.com> 0.10006-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.10002-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 Iain Arnell <iarnell@gmail.com> 0.10002-1
- update to latest upstream version
- update R/BR perl(Sub::Name) >= 0.05
- update BR perl(Test::Exception) >= 0.31
- new BR perl(Devel::Hide)

* Wed Nov 03 2010 Iain Arnell <iarnell@gmail.com> 0.09008-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- new BR perl(Test::Exception)
- new BR perl(Class::XSAccessor)
- remove BR perl(Sub::Identify)
- new req perl(Class::XSAccessor)
- remove explicit req perl(Carp)
- remove explicit req perl(MRO::Compat)
- remove explicit req perl(Scalar::Util)

* Thu Sep 02 2010 Iain Arnell <iarnell@gmail.com> 0.09005-1
- update to latest upstream version

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09002-2
- Mass rebuild with perl-5.12.0

* Sun Feb 07 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.09002-1
- subpackage tests, drop t/ from doc
- update filtering (perl_default_filter)
- PERL_INSTALL_ROOT => DESTDIR in make install
- auto-update to 0.09002 (by cpan-spec-update 0.01)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09000-2
- rebuild against perl 5.10.1

* Tue Aug 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09000-1
- auto-update to 0.09000 (by cpan-spec-update 0.01)
- added a new br on perl(Carp) (version 0)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Scalar::Util) (version 0)
- added a new br on perl(Sub::Identify) (version 0)
- added a new br on perl(Sub::Name) (version 0.04)
- added a new br on CPAN (inc::Module::AutoInstall found)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(Class::Inspector) (version 0)
- added a new req on perl(MRO::Compat) (version 0)
- added a new req on perl(Scalar::Util) (version 0)
- added a new req on perl(Sub::Name) (version 0.04)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08003-1
- update to 0.08003

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 02 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08002-1
- update to 0.08002

* Wed May 21 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.08001-1
- update to 0.08001

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.07000-4
Rebuild for new perl

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.07000-3
- rebuild for new perl

* Sat Dec 08 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07000-2
- bump

* Tue Sep 18 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07000-1
- Specfile autogenerated by cpanspec 1.71.
