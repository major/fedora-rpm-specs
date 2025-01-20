Name:           perl-Unix-Statgrab
Version:        0.112
Release:        25%{?dist}
Summary:        Perl extension for collecting information about the machine
License:        (LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl))
URL:            https://metacpan.org/release/Unix-Statgrab
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Unix-Statgrab-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf) >= 0.316
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libstatgrab) >= 0.90
# Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::LeakTrace)

%description
Unix::Statgrab is a wrapper for libstatgrab as available from
<http://www.i-scream.org/libstatgrab/>. It is a reasonably portable attempt
to query interesting stats about your computer. It covers information on the
operating system, CPU, memory usage, network interfaces, hard-disks etc. 

%prep
%setup -q -n Unix-Statgrab-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unix*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-23
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-19
- Perl 5.38 rebuild

* Sun Mar 12 2023 Tim Orling <ticotimo@gmail.com> - 0.112-18
- correct license https://rt.cpan.org/Public/Bug/Display.html?id=125519

* Sun Mar 12 2023 Tim Orling <ticotimo@gmail.com> - 0.112-17
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-2
- Perl 5.28 rebuild

* Mon Jun 25 2018 Tim Orling <ticotimo@gmail.com> - 0.112-1
- Drop patch Unix-Statgrab-0.111-Adapt-to-Config-AutoConf-0.316.patch
  bug #1574910, CPAN RT#125204, upstream has fixed
- Upgrade to version 0.112 (bug #1589408)

* Fri Jun 08 2018 Petr Pisar <ppisar@redhat.com> - 0.111-9
- Adapt to Config::AutoConf 0.316 (bug #1574910)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.111-8
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.111-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.111-2
- Perl 5.24 rebuild

* Mon May 02 2016 Tim Orling <ticotimo@gmail.com> - 0.111-1
- Drop patch, renenabling user_data tests, upstream has fixed rt#10721
- Upgrade to version 0.111

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Petr Šabata <contyk@redhat.com> - 0.109-1
- 0.109 bump
- Disabling user_data tests as they seem to be broken at the moment (rt#107241)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-25.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-24.1
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-23.1
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-22.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-21.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Oliver Falk <oliver@linux-kernel.at> - 0.04-20.1
- Rebuild for new libstatgrab

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.04-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Oliver Falk <oliver@linux-kernel.at> - 0.04-17
- Remove segfaulting tests

* Mon Aug 06 2012 Oliver Falk <oliver@linux-kernel.at> - 0.04-16
- Rebuilt for Perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.04-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-12
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Oliver Falk <oliver@linux-kernel.at> - 0.04-10
- Rebuild with new perl-5.12.3

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.04-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-4
Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.04-3
- Autorebuild for GCC 4.3

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.04-2
- BR ExtUtils::MakeMaker.
- Reformat to more closely resemble cpanspec output.
- Use fixperms macro instead of our own chmod incantation.
- Remove some macro other usage.

* Tue Sep 26 2006 Steven Pritchard <steve@kspei.com> 0.04-1
- Update to 0.04.
- Drop compile fix patch.
- Fix find option order.

* Wed Aug 24 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-7
- Try if Ralf's %%files section works

* Wed Aug 24 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-6
- Again

* Wed Aug 24 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-5
- Fix filelist

* Tue Aug 23 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-4
- Bug #165533, thanks to Paul Howarth

* Wed Aug 10 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-3
- Add compile fix, since libstatgrab 0.12 API changes dup to
  duplex

* Wed Aug 10 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-2
- Cleanup specfile
- Try to make it ready for FE

* Mon May 09 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-1.2
- Rebuild

* Wed Apr 13 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-1.1
- Remove the pkgname define

* Wed Apr 13 2005 Oliver Falk <oliver@linux-kernel.at> - 0.03-1
- Update

* Tue Feb 15 2005 Oliver Falk <oliver@linux-kernel.at> - 0.02-1
- Initial build for Fedora Core
- Used cpan2rpm for initial specfile

# vim: ts=4 sw=4
