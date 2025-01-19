%global cpan_version 0.9727

Name:           perl-Graph
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        5%{?dist}
Summary:        Perl module for dealing with graphs, the abstract data structures

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graph
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-%{cpan_version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(B::Deparse) >= 0.61
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Heap::Fibonacci) >= 0.80
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(overload)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Object) >= 1.40
BuildRequires:  perl(Storable) >= 2.05
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(Text::Abbrev)
# Optional tests
BuildRequires:  perl(Devel::Cycle)
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Heap::Fibonacci)
Requires:       perl(Safe)
Requires:       perl(Set::Object) >= 1.40

%description
This is Graph, a Perl module for dealing with graphs, the abstract
data structures. 
 
This is a full rewrite of the Graph module 0.2xx series as discussed
in the book "Mastering Algorithms with Perl", written by Jarkko
Hietaniemi (the undersigned), John Macdonald, and Jon Orwant,
and published by O'Reilly and Associates.  This rewrite is not
fully compatible with the 0.2xx series.

%prep
%setup -q -n Graph-%{cpan_version}

# avoid extra dependencies
chmod 644 util/cover.sh

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README RELEASE DESIGN Changes TODO util
%{perl_vendorlib}/Graph*
%{_mandir}/man3/Graph*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.27-1
- 0.9727 bump (rhbz#2217268)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 07 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.26-1
- 0.9726 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.25-2
- Perl 5.36 rebuild

* Thu May 05 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.25-1
- 0.9725 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.24-1
- 0.9724 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.16-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.16-1
- 0.9716 bump

* Tue Dec 08 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.12-1
- 0.9712 bump
- Modernize spec

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.04-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.04-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.04-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.04-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.04-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.97.04-1
- 0.9704 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.96-1
- 0.96 bump

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.91-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.91-10
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.91-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.91-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.91-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.91-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.91-1
- Update to upstream 0.91

* Wed Jun  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.84-3
- Remove old check construct that prevents build in F-10+ (#449571)

* Fri Feb 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.84-2
- rebuild for new perl

* Wed Sep 05 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.84-1
- Update to latest upstream.

* Thu Aug 23 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.83-3
- License tag to GPL+ or Artistic as per new guidelines.

* Sat Aug 18 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.83-2
- Add missing BR: perl(Test::More)

* Sat Aug 18 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.83-1
- Update to latest upstream

* Sat Mar 24 2007 Alex Lancaster <alexl@users.sourceforge.net> 0.81-1
- Update to 0.81

* Wed Apr 06 2005 Hunter Matthews <thm@duke.edu> 0.59-2
- Review suggestions from José Pedro Oliveira

* Fri Mar 18 2005 Hunter Matthews <thm@duke.edu> 0.59-1
- Initial Packageing.


