Name:           perl-Devel-Cover
Version:        1.44
Release:        3%{?dist}
Summary:        Code coverage metrics for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Cover
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Cover-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.38.0
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(B::Concise)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
# CPAN::Releases::Latest not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities) >= 3.69
# JSON or JSON::PP by Devel::Cover::DB::IO::JSON
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Moo)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Parallel::Iterator)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI::HTML) >= 1.07
BuildRequires:  perl(Sereal)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Template) >= 2.00
BuildRequires:  perl(Template::Provider)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Optional run-time:
# Browser::Open not used at tests
# (PPI && PPI::HTML 1.07) || Perl::Tidy 20060719
# Perl::Tidy 20060719 not used at tests
BuildRequires:  perl(Pod::Coverage) >= 0.06
BuildRequires:  perl(Pod::Coverage::CountParents)
# PPI::HTML 1.07 not used at tests 
BuildRequires:  perl(Test::Differences)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(DBM::Deep)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moose)
BuildRequires:  perl(overload)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(:VERSION) = %(eval "`perl -V:version`"; echo ${version:-0})
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
# CPAN::Releases::Latest not yet packaged
# JSON or JSON::PP by Devel::Cover::DB::IO::JSON
Requires:       perl(JSON)

%{?perl_default_filter}

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Cover::Dumper\\)
# Fiter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Template\\)$

%description
This module provides code coverage metrics for Perl. Code coverage metrics
describe how thoroughly tests exercise code. By using Devel::Cover you can
discover areas of code not exercised by your tests and determine which
tests to create to increase coverage. Code coverage can be considered as an
indirect measure of quality.

%prep
%setup -q -n Devel-Cover-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md docs/BUGS docs/TODO
%{_bindir}/cover
%{_bindir}/cpancover
%{_bindir}/gcov2perl
%{perl_vendorarch}/Devel/
%{perl_vendorarch}/auto/Devel/
%{_mandir}/man1/cover.1*
%{_mandir}/man1/cpancover.1*
%{_mandir}/man1/gcov2perl.1*
%{_mandir}/man3/Devel::Cover*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Paul Howarth <paul@city-fan.org> - 1.44-1
- 1.44 bump

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-2
- Perl 5.40 rebuild

* Sun Jun  9 2024 Paul Howarth <paul@city-fan.org> - 1.43-1
- 1.43 bump

* Fri May 17 2024 Paul Howarth <paul@city-fan.org> - 1.42-1
- 1.42 bump (rhbz#2280643)
- Use author-indepenent source URL
- Make %%files list more explicit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-5
- Rebuild for Perl 5.38.2

* Tue Nov 21 2023 Michal Josef Špaček <mspacek@redhat.com> - 1.40-4
- Add dependency to Perl version on which was build
  Resolves: RHBZ#2246773

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-2
- Perl 5.38 rebuild

* Fri May 26 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-1
- 1.40 bump
- Modernize spec
- Update license to SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-2
- Perl 5.32 rebuild

* Tue May 19 2020 Tom Callaway <spot@fedoraproject.org> - 1.36-1
- update to 1.36

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-5
- Add perl(blib) for tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-2
- Perl 5.30 rebuild

* Tue May 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-1
- 1.33 bump

* Thu Apr 25 2019 Tom Callaway <spot@fedoraproject.org> - 1.32-1
- update to 1.32

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-1
- 1.31 bump

* Tue Aug 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-1
- 1.30 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-1
- 1.29 bump

* Thu Oct 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-1
- 1.28 bump

* Tue Aug 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-1
- 1.26 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-2
- Perl 5.26 rebuild

* Tue May 16 2017 Tom Callaway <spot@fedoraproject.org> - 1.25-1
- update to 1.25

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-2
- Perl 5.24 rebuild

* Tue Apr 26 2016 Tom Callaway <spot@fedoraproject.org> - 1.23-1
- update to 1.23

* Mon Apr 11 2016 Tom Callaway <spot@fedoraproject.org> - 1.22-1
- update to 1.22

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-1
- 1.21 bump

* Wed Jul 22 2015 Petr Pisar <ppisar@redhat.com> - 1.20-2
- Specify all dependencies

* Mon Jul  6 2015 Tom Callaway <spot@fedoraproject.org> - 1.20-1
- update to 1.20

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-2
- Perl 5.22 rebuild

* Wed Apr  8 2015 Tom Callaway <spot@fedoraproject.org> - 1.18-1
- update to 1.18

* Mon Mar 30 2015 Tom Callaway <spot@fedoraproject.org> - 1.17-1
- update to 1.17

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-1
- 1.09 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.03-2
- Perl 5.18 rebuild

* Fri May 24 2013 Tom Callaway <spot@fedoraproject.org> - 1.03-1
- update to 1.03

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Marcela Mašláňová <mmaslano@redhat.com> 0.97-1
- Bump the release.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.89-4
- Perl 5.16 rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.89-3
- Do not require private Devel::Cover::Dumper module

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.89-2
- Perl 5.16 rebuild

* Thu Jun 21 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.89-1
- update to 0.89
* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.78-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.78-2
- Perl mass rebuild

* Thu May 19 2011 Iain Arnell <iarnell@gmail.com> 0.78-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.66-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.66-1
- Mass rebuild with perl-5.12.0 & update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.65-2
- Mass rebuild with perl-5.12.0

* Thu Jan 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.65-1
- update to 0.65

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.64-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.64-1
- update to 0.64

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-3
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.63-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-1
- 0.63

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.61-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Jan 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.61-1
- Update to 0.61.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.60-1
- Update to 0.60.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.59-1
- Update to 0.59.
- Dropped PPI::HTML from the requirements list (optional module).

* Wed Aug  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.58-1
- Update to 0.58.

* Fri Aug  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.57-1
- Update to 0.57.

* Thu Aug  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.56-1
- Update to 0.56.

* Fri May 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.55-2
- Removed dependencies pulled in by a documentation file (#191110).

* Thu May 04 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.55-1
- First build.
