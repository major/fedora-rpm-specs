Name:           perl-GnuPG-Interface
Version:        1.04
Release:        6%{?dist}
Summary:        Perl interface to GnuPG
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GnuPG-Interface
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/GnuPG-Interface-%{version}.tar.gz
# https://github.com/bestpractical/gnupg-interface/issues/8
Patch0:         version-stdin.patch
BuildArch:      noarch
BuildRequires:  gpg

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(MooX::late)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

Requires:       gpg

%{?perl_default_filter}

%description
%{summary}.

%prep
%autosetup -p1 -n GnuPG-Interface-%{version}
perldoc -t perlgpl > GPL
perldoc -t perlartistic > Artistic
# gpg as being used by the testsuite requires test to be 0700
chmod 0700 test

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license GPL Artistic
%doc Changes README
%{perl_vendorlib}/GnuPG
%{_mandir}/man3/*.3*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.04-2
- Migrate to SPDX license

* Wed Dec 13 2023 Xavier Bachelot <xavier@bachelot.org> - 1.04-1
- Update to 1.0.4 (RHBZ#2239168, RHBZ#2208967)
- Update Source0 URL
- Distribute licenses
- Add patch to add stdin handler to _version sub

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-2
- Perl 5.34 rebuild

* Mon Apr 12 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.02-1
- Update to 1.02

* Sun Jan 31 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.01-1
- Update to 1.01
- Remove Patch* declarations since patches are not applied

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.32 rebuild

* Sun May 17 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00-1
- Update to 1.00
- Drop upstreamed patches
- Pass NO_PACKLIST and NO_PERLLOCAL to Makefile.PL
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-16
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-2
- Perl 5.22 rebuild

* Sun Feb 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.52-1
- Update to 0.52

* Fri Dec 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.51-1
- Update to 0.51

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-5
- Perl 5.20 rebuild

* Thu Aug 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-3
- Add BR perl(Pod::Perldoc) (perldoc is now in separate package)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.50-2
- Rework BR:s (RHBZ #1079473).
- Reactivate tests.

* Sun Mar 16 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.50-1
- Update to 0.50

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.46-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.46-1
- Update to 0.46

* Sun Sep 30 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.45-1
- Update to 0.45
- Remove BuildRoot definition

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.44-5
- Perl 5.16 rebuild

* Mon Jan 16 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.44-1
- Add Pod::Perldoc (perldoc) as a BR
- Clean up spec file
- Add perl default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.44-2
- Perl mass rebuild

* Tue May 03 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.44-1
- Update to 0.44

* Thu Mar 10 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.43-2
- Bump to build the release

* Thu Mar 10 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.43-1
- Update to 0.43

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.42-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.42-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.42-3
- rebuild against perl 5.10.1

* Sun Oct 04 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.42-2
- Disable tests because they need /dev/tty to run

* Fri Oct 02 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.42-1
- Update to 0.42
- Fix rpmlint errors

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Apr 20 2008 Matt Domsch <Matt_Domsch@dell.com> 0.36-1
- new upstream, alreadly includes our patches

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.33-10
- rebuild for new perl

* Sun Aug 12 2007 Matt Domsch <Matt_Domsch@dell.com> - 0.33-9
- add BR perl(ExtUtils::MakeMaker)

* Mon Oct 02 2006 Matt Domsch <Matt_Domsch@dell.com> - 0.33-8
- rebuild

* Sat Sep  2 2006 Matt Domsch <Matt_Domsch@dell.com> 0.33-7
- rebuild for FC6

* Mon Feb 13 2006 Matt Domsch <Matt_Domsch@dell.com> 0.33-6
- add 10 years to expiry date of test gpg keys,
  lets 'make test' succeed after 2006-02-05.
- rebuild for FC5

* Thu Oct 06 2005 Ralf Corsepius <rc040203@freenet.de> - 0.33-5
- Requires: perl(Class::MethodMaker) (PR #169976).

* Tue Sep 13 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.33-4
- FC-3 doesn't use the patch1

* Sun Sep 11 2005 Matt Domsch <matt@domsch.com> 0.33-3
- use perldoc -t and the _smp_mflags macro

* Sun Aug 28 2005 Matt Domsch <matt@domsch.com> 0.33-2
- add Requires: gpg, always apply secret-key-output-1.patch, as it works on
  both gpg 1.4 and gpg2.

* Thu Aug 25 2005 Matt Domsch <matt@domsch.com> 0.33-1
- specfile changes per Paul Howarth's comments
- added GnuPG-Interface-0.33.tru-record-type.txt patch,
  borrowed from Mail-GPG-1.0.1

* Wed Aug 24 2005 Matt Domsch <matt@domsch.com> 0.33-0
- Initial package for Fedora Extras
