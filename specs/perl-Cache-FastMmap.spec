Name:           perl-Cache-FastMmap
Version:        1.59
Release:        3%{?dist}
Summary:        Uses an mmap'ed file to act as a shared memory interprocess cache
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/Cache::FastMmap
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBM/Cache-FastMmap-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Optional run-time
BuildRequires:  perl(Compress::Zlib)
# Tests
BuildRequires:  perl(Data::Dumper)
# ExtUtils::testlib not used
# lib not used
# POSIX not used
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
# Optional tests
# Do not BR GTop to disable test t/6.t because it fails randomly against
# Perl 5.24 on x86_64 arch (CPAN RT#39342)
# BuildRequires:  perl(GTop)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Sereal)

%description
In multi-process environments (eg mod_perl, forking daemons, etc),
it's common to want to cache information, but have that cache shared
between processes. Many solutions already exist, and may suit your
situation better.

%prep
%setup -q -n Cache-FastMmap-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Cache*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-2
- Perl 5.42 rebuild

* Tue Jun 10 2025 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-1
- 1.59 bump (rhbz#2364034)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.57-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.57-11
- Perl 5.40 rebuild

* Thu Feb 22 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.57-10
- Modernize spec.
- Add BR: perl(JSON), perl(Sereal).

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.57-6
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.57-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 08 2021 Jan Pazdziora <jpazdziora@redhat.com> - 1.57-1
- 2009211 - Rebase to upstream version 1.57.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Jan Pazdziora <jpazdziora@redhat.com> - 1.56-1
- 1906256 - Rebase to upstream version 1.56.

* Sat Nov 14 2020 Jan Pazdziora <jpazdziora@redhat.com> - 1.51-1
- 1896657 - Rebase to upstream version 1.51.

* Mon Nov 09 2020 Jan Pazdziora <jpazdziora@redhat.com> - 1.50-1
- 1895331 - Rebase to upstream version 1.50.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-2
- Perl 5.32 rebuild

* Mon Mar 30 2020 Jan Pazdziora <jpazdziora@redhat.com> - 1.49-1
- 1816436 - Rebase to upstream version 1.49.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-2
- Perl 5.30 rebuild

* Thu Apr 11 2019 Jan Pazdziora <jpazdziora@redhat.com> - 1.48-1
- 1698704 - Rebase to upstream version 1.48.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.47-2
- Perl 5.28 rebuild

* Mon Apr 09 2018 Jan Pazdziora <jpazdziora@redhat.com> - 1.47-1
- 1564476 - Rebase to upstream version 1.47.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Jan Pazdziora <jpazdziora@redhat.com> - 1.46-1
- 1471090 - Rebase to upstream version 1.46.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-2
- Perl 5.26 rebuild

* Wed Mar 22 2017 Jan Pazdziora <jpazdziora@redhat.com> - 1.45-1
- 1432914 - Rebase to upstream version 1.45.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Jan Pazdziora <jpazdziora@redhat.com> - 1.44-1
- 1341869 - Rebase to upstream version 1.44.

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-4
- Do not build-require perl(GTop)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-10
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.40-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.40-2
- Perl 5.16 rebuild
- Specify all dependencies

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 1.40-1
- update to latest upstream version

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 1.39-1
- update to latest upstream
- clean up spec for modern rpmbuild
- re-enable leak test t/6.t

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.36-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 02 2010 Iain Arnell <iarnell@gmail.com> 1.36-1
- update to latest upstream
- re-enable leak test

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.35-2
- Mass rebuild with perl-5.12.0

* Sat Feb 20 2010 Iain Arnell <iarnell@gmail.com> 1.35-1
- update to latest upstream version

* Fri Feb 12 2010 Iain Arnell <iarnell@gmail.com> 1.34-5
- use perl_default_filter

* Tue Dec 08 2009 Iain Arnell <iarnell@gmail.com> 1.34-4
- drop failing leak test (rt #39342)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.34-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Iain Arnell <iarnell@gmail.com> 1.34-1
- update to latest upstream version

* Thu May 14 2009 Iain Arnell <iarnell@gmail.com> 1.30-1
- update to latest upstream version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 15 2008 Iain Arnell <iarnell@gmail.com> 1.28-2
- BR perl(GTop) and perl(Compress::Zlib) to enable optional tests

* Sun Sep 14 2008 Iain Arnell <iarnell@gmail.com> 1.28-1
- Specfile autogenerated by cpanspec 1.77.
