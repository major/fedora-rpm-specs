Name:           perl-Text-Autoformat
Version:        1.750000
Release:        17%{?dist}
Summary:        Automatic text wrapping and reformatting
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Autoformat
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Text::Reform)
BuildRequires:  perl(Text::Tabs)
# Tests only
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)

%description
Text::Autoformat provides intelligent formatting of plain text without the
need for any kind of embedded mark-up. The module recognizes Internet
quoting conventions, a wide range of bulleting and number schemes, centered
text, and block quotations, and reformats each appropriately. Other options
allow the user to adjust inter-word and inter-paragraph spacing, justify
text, and impose various capitalization schemes.

The module also supplies a re-entrant, highly configurable replacement for
the built-in Perl format() mechanism.

%prep
%setup -q -n Text-Autoformat-1.75
chmod -c -x config.*

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build}

%files
%license LICENSE
%doc Changes README config.emacs config.vim
%{perl_vendorlib}/Text
%{_mandir}/man3/Text::Autoformat.3pm*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1.750000-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.750000-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.750000-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.750000-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.750000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.750000-1
- Update to 1.75
- Minor cleanup of the spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.740000-12
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.740000-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.740000-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.740000-4
- Perl 5.24 rebuild

* Fri Mar 11 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.740000-3
- Stop using a variable in the version number

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.740000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Petr Šabata <contyk@redhat.com> - 1.740000-1
- 1.74 bump, perl5.22 fixes

* Wed Nov 25 2015 Petr Šabata <contyk@redhat.com> - 1.730000-1
- 1.73 bump
- Don't filter out Text::Autoformat::Hang and ::NullHang provides,
  we depend on them (and others may too, somehow)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.720000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Petr Šabata <contyk@redhat.com> - 1.720000-1
- 1.72 bump

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.669007-2
- Perl 5.22 rebuild

* Tue Feb 10 2015 Petr Šabata <contyk@redhat.com> - 1.669007-1
- 1.669007 bump

* Fri Nov 14 2014 Petr Pisar <ppisar@redhat.com> - 1.669006-1
- 1.669006 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.669004-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.669004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Paul Howarth <paul@city-fan.org> - 1.669004-1
- Update to 1.669004
  - Tweaked widow handling to avoid a nasty edge case
- Specify all dependencies
- Replace provides filter with a patch that works right back to EL-5
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Don't use macros for commands

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.669002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.669002-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.669002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.669002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.669002-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.669002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.669002-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.669002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Steven Pritchard <steve@kspei.com> 1.669002-1
- Update to 1.669002.
- BR version and Module::Build (and build with that).
- Include config.emacs and config.vim in docs.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.14.0-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.14.0-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14.0-3
- Rebuild for perl 5.10 (again)

* Wed Jan 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-2
- add BR: Test::More

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-1
- rebuild for new perl
- upstream changed license to GPL+ or Artistic

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 1.13-5
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Fri Sep 01 2006 Steven Pritchard <steve@kspei.com> 1.13-4
- Rework spec to look more like current cpanspec output.

* Mon Sep 05 2005 Steven Pritchard <steve@kspei.com> 1.13-3
- Minor spec cleanup.
- Add Artistic.

* Sat Aug 20 2005 Steven Pritchard <steve@kspei.com> 1.13-2
- Fix permissions (#166406).

* Tue May 24 2005 Steven Pritchard <steve@kspei.com> 1.13-1
- Update to 1.13 final.
- Filter bogus perl(Hang) and perl(NullHang) auto-provides.

* Tue May 10 2005 Steven Pritchard <steve@kspei.com> 1.13-0.3.beta
- Drop Epoch and change Release for Fedora Extras.

* Wed Feb 09 2005 Steven Pritchard <steve@kspei.com> 0:1.13-0.fdr.0.2.beta
- Minor update to 0.13beta source, from
  http://rt.cpan.org/NoAuth/Bug.html?id=8018 (pointed out by jpo@di.uminho.pt)

* Wed Jun 09 2004 Steven Pritchard <steve@kspei.com> 0:1.13-0.fdr.0.1.beta
- Specfile regenerated.
- Update to 0.13beta, which includes the upstream fix for a bug reported to
  the author.
