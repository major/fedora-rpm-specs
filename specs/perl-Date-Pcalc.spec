Name: 		perl-Date-Pcalc
Version:	6.1
Release:	46%{?dist}
Summary:	Gregorian calendar date calculations
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Date-Pcalc
Source0: 	https://cpan.metacpan.org/authors/id/S/ST/STBEY/Date-Pcalc-%{version}.tar.gz
# Perl 5.16 compatibility, CPAN RT #76442
Patch0:		Date-Pcalc-6.1-boolean.patch
# Related: rt#101232
Patch1:         Date-Pcalc-6.1-century.patch
# Fixed error "Unescaped left brace in regex is deprecated"
Patch2:         Date-Pcalc-6.1-Fix-unescaped-left-brace-in-regex.patch
# bool, true and false are keywords in modern C
Patch3:         0001-Fix-bool-detection.patch

BuildRequires:  %{_bindir}/iconv
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Bit::Vector) >= 7.1
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp::Clan) >= 5.3
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(vars)
# Tests only
# nothing
Requires:       perl(bytes)
Requires:       perl(Bit::Vector) >= 7.1
Requires:       perl(Carp::Clan) >= 5.3

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Bit::Vector\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp::Clan\\)$

%description
This package consists of a Perl module for all kinds of date calculations based
on the Gregorian calendar (the one used in all western countries today), 
thereby complying with all relevant norms and standards: ISO/R 2015-1971, 
DIN 1355 and, to some extent, ISO 8601 (where applicable).

%prep
%setup -q -n Date-Pcalc-%{version}
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 </dev/null
make %{?_smp_mflags}

%install
%{_bindir}/iconv --from-code=ISO-8859-1 --to-code=UTF-8 blib/man3/Date::Pcalc.3pm -o blib/man3/Date::Pcalc.3pm-utf8
mv blib/man3/Date::Pcalc.3pm-utf8 blib/man3/Date::Pcalc.3pm 
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

# Interactive build, prompts if binary of PP version should be built
# Defaults to binary if gcc is found (default Fedora buildroot contains gcc)
# There's No option available to specify explicitly
%files
%license GNU_GPL.txt Artistic.txt
%doc CHANGES.txt README.txt EXAMPLES.txt CREDITS.txt
%{perl_vendorarch}/auto/Date
%{perl_vendorarch}/Date
%{_mandir}/man3/*

%changelog
* Sat Jan 25 2025 Ralf Corsépius <corsepiu@fedoraproject.org> - 6.1-46
- Add 0001-Fix-bool-detection.patch (F42FTBS, RHBZ#2341027).

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-43
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-39
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-36
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-33
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-30
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-27
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-24
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-23
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-19
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-18
- Fix building on Perl 5.26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-13
- Perl 5.22 rebuild

* Wed Jan 07 2015 Petr Šabata <contyk@redhat.com> - 6.1-12
- Adapt the test suite for the 2015-2115 era

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.1-11
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 6.1-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.1-4
- Perl 5.16 rebuild
- Fix boolean definition (RT #76442)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 6.1-2
- Perl mass rebuild

* Tue Apr 05 2011 Petr Sabata <psabata@redhat.com> - 6.1-1
- 6.1 bump
- Removing obsolete Buildroot stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2-10
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.2-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2-5.1
Rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep 07 2006 Mike McGrath <imlinux@gmail.com> - 1.2-4
- Release bump

* Mon Mar 20 2006 Mike McGrath <imlinux@gmail.com> - 1.2-3
- Minor fixes and formatting in spec file

* Sun Mar 19 2006 Mike McGrath <imlinux@gmail.com> - 1.2-2
- Include license and credits
- Convert manpage to utf-8

* Sat Mar 18 2006 Mike McGrath <imlinux@gmail.com> - 1.2-1
- First attempt at a Fedora friendly spec file
