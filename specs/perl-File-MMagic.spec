Name:           perl-File-MMagic
Version:        1.30
Release:        35%{?dist}
Summary:        A Perl module emulating the file(1) command
# MMagic.pm and COPYING files contain identical license texts of App-s2p
# license, BSD license, and ASL 1.0 license.
License:        App-s2p AND Apache-1.0 AND Spencer-94
URL:            https://metacpan.org/release/File-MMagic
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-MMagic-%{version}.tar.gz
Patch0:         File-MMagic-1.30-rt109673.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
%if 0%{?fedora} > 34 || 0%{?rhel} > 8
BuildRequires:  glibc-gconv-extra
%endif
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Runtime

%description
This module attempts to guess a file's type from its contents like the file(1)
command.

%prep
%setup -q -n File-MMagic-%{version}

# Fix "Redundant argument in sprintf" warning (CPAN RT#109673)
%patch -P0

# Re-code README.ja as UTF-8
iconv -f ISO-2022-JP -t utf8 README.ja > README.ja.utf8 && mv README.ja.utf8 README.ja

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
%license COPYING
%doc ChangeLog README.en README.ja
%{perl_vendorlib}/File/
%{_mandir}/man3/File::MMagic.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-28
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Paul Howarth <paul@city-fan.org> - 1.30-25
- BR: glibc-gconv-extra to fix FTBFS on Fedora 34 onwards
- Use %%license unconditionally
- Fix permissions verbosely
- Use author-independent source URL

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-24
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-21
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Petr Pisar <ppisar@redhat.com> - 1.30-16
- Correct license to "App-s2p and ASL 1.0 and BSD"

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-10
- Perl 5.24 rebuild

* Tue May  3 2016 Paul Howarth <paul@city-fan.org> - 1.30-9
- Fix "Redundant argument in sprintf" warning (CPAN RT#109673)
- Classify buildreqs by usage
- Simplify find command using -delete
- Use %%license where possible

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.30-2
- Perl 5.18 rebuild

* Mon Jul 08 2013 Petr Šabata <contyk@redhat.com> - 1.30-1
- 1.30 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Paul Howarth <paul@city-fan.org> - 1.29-1
- Update to 1.29
  - MMagic.pm (checktype_contents): fix infinite loop bug (CPAN RT#77836)
- BR: perl(base) and perl(Test::More)
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't need to remove empty directories from the buildroot
- Make %%files list more explicit
- Tweak %%description

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.28-2
- Perl 5.16 rebuild

* Tue Jun 05 2012 Petr Šabata <contyk@redhat.com> - 1.28-1
- 1.28 bump
- Modernizing spec (removing buildroot, defattr, and command macros)
- Removing trailing whitespace
- Packaging README.ja

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.27-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-10
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.27-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.27-5
- rebuild for new perl

* Fri Oct 26 2007 Robin Norwood <rnorwood@redhat.com> - 1.27-4
- Remove BR: perl for package review
- Resolves: bz#226257

* Wed Aug 29 2007 Robin Norwood <rnorwood@redhat.com> - 1.27-3
- Update license tag
- Add BuildRequires: perl(ExtUtils::MakeMaker)

* Fri Jul 20 2007 Robin Norwood <rnorwood@redhat.com> - 1.27-2.fc8
- Add fixes from EPEL branch
- Fix minor specfile issues

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 1.27-1
- Upgrade to 1.27

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.26-1
- Upgrade to 1.26
- rebuild for new perl-5.8.8

* Tue Jan 10 2006 Jason Vas Dias <jvdias@redhat.com> - 1.25-1
- fix bug 176717: upgrade to 1.25

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Sat Apr 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.22-1
- Update to 1.22
- Spec cleanup (#153204)

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.21-2
- rebuild

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 1.21-1
- move to 1.21

* Tue Dec 10 2002 Chip Turner <cturner@redhat.com>
- update to latest version from CPAN

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Aug  6 2002 Chip Turner <cturner@localhost.localdomain>
- update to 1.15

* Fri Dec 7 2001 root <root@redhat.com>
- Spec file was autogenerated.
