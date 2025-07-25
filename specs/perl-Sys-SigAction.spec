Name:           perl-Sys-SigAction
Version:        0.24
Release:        2%{?dist}
Summary:        Perl extension for Consistent Signal Handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-SigAction
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-SigAction-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >=  5.5
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# threads not helpful
BuildRequires:  perl(Time::HiRes)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
Requires:       perl(Time::HiRes)

%description
Sys::SigAction provides EASY access to POSIX::sigaction() for signal
handling on systems that support sigaction().
It is hoped that with the use of this module, your signal handling 
behavior can be coded in a way that does not change from one perl 
version to the next, and that sigaction() will be easier for you to use.

%prep
%setup -q -n Sys-SigAction-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
pod2man --name=dbd-oracle-timeout < dbd-oracle-timeout.POD \
    > dbd-oracle-timeout.man

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README dbd-oracle-timeout.man
%dir %{perl_vendorlib}/Sys
%{perl_vendorlib}/Sys/SigAction
%{perl_vendorlib}/Sys/SigAction.pm
%{_mandir}/man3/Sys::SigAction.*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Apr 01 2025 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Petr Pisar <ppisar@redhat.com> - 0.23-21
- Convert a license tag to an SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- 0.23 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Petr Pisar <ppisar@redhat.com> - 0.21-2
- Fix converting POD to manual page with podlators >= 4

* Mon Jul 20 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- 0.21 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-4
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Paul Howarth <paul@city-fan.org> - 0.20-1
- Update to 0.20
- BR:/R: perl(Time::HiRes)
- BR: perl(Config), perl(POSIX), /usr/bin/pod2man
- Don't need to remove empty directories from the buildroot

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.11-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-10
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 0.11-8
- Perl mass rebuild in dist-f16-perl (d'oh)

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 0.11-7
- Perl mass rebuild
- Remove now obsolete Buildroot and defattr

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.11-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 23 2009 Andreas Thienemann <andreas@bawue.net> - 0.11-1
- Update to 0.11

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10-3
- Rebuild for new perl

* Sun Jan 27 2008 Andreas Thienemann <andreas@bawue.net> 0.10-2
- Added Test::More to the BuildReqs

* Thu Mar 15 2007 Andreas Thienemann <andreas@bawue.net> 0.10-1
- Specfile autogenerated by cpanspec 1.69.1.
- Cleaned up for FE
