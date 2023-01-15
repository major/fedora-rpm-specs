Name:           perl-Config-Augeas
Version:        1.000
Release:        25%{?dist}
Summary:        Edit configuration files through Augeas C library
License:        LGPLv2+
URL:            https://metacpan.org/release/Config-Augeas
Source0:        https://cpan.metacpan.org/modules/by-module/Config/Config-Augeas-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  augeas-devel

%description
Augeas is a library and command line tool that focuses on the most basic
problem in handling Linux configurations programmatically: editing actual
configuration files in a controlled manner.

%prep
%setup -q -n Config-Augeas-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
LANG=C ./Build test verbose=1

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Config*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-24
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-21
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-18
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-12
- Perl 5.28 rebuild

* Thu Mar 01 2018 Petr Pisar <ppisar@redhat.com> - 1.000-11
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-2
- Perl 5.22 rebuild

* Sun Sep 28 2014 Alan Pevec <apevec@redhat.com> - 1.000-1
- Update to 1.000
  * Added methods text_store, text_retrieve and rename

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.903-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.903-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.903-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.903-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.903-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.903-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.903-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.903-2
- Perl 5.16 rebuild

* Mon Mar 19 2012 Alan Pevec <apevec@redhat.com> 0.903-1
- new upstream release 0.903

* Fri Feb 24 2012 Alan Pevec <apevec@redhat.com> 0.902-1
- new upstream release 0.902
    * Added method aug_srun
    * Added method aug_span

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.701-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.701-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.701-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.701-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.701-2
- Mass rebuild with perl-5.12.0

* Sat Feb 20 2010 Alan Pevec <apevec@redhat.com> 0.701-1
- new upstream release 0.701
    * lib/Config/Augeas.pm: Added new error strings from Augeas 0.7.0
    * lib/Config/Augeas.xs: fix core dump in get (initialise RETVAL
      before calling aug_get). Added new error constants from Augeas 0.7.0

* Sun Jan 03 2010 Alan Pevec <apevec@redhat.com> 0.601-1
- new upstream release 0.601
  * lib/Config/Augeas.pm : Added methods load, error, error_message,
    error_minor_message and error_details
  * lib/Config/Augeas.xs : Added interface for aug_load and
    aug_error* from Augeas 0.6.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.501-3
- rebuild against perl 5.10.1

* Tue Nov 24 2009 Alan Pevec <apevec@redhat.com> 0.501-2
- workaround in %%check for https://fedorahosted.org/augeas/ticket/35

* Tue Nov 24 2009 Alan Pevec <apevec@redhat.com> 0.501-1
- new upstream release 0.501
  * Build.PL: modified gcc options to issue more warnings (and fixed them)
  * lib/Config/Augeas.xs: Fixed compiler warnings (Thanks to Guillaume Rousse)
- new upstream release 0.500
  * lib/Config/Augeas.pm
    (new): added no_load, save => noop, no_std_inc options
    (defvar): new method for Augeas 0.5.0
    (defnode): new method for Augeas 0.5.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Alan Pevec <apevec@redhat.com> - 0.400-1
- new upstream release 0.400
  * lib/Config/Augeas.xs (match): dies if aug_match returns -1. Perl
    programmer can choose to trap this failure with eval or Error
    module.
  * lib/Config/Augeas.pm (match): cleanup trailing slashes in
    path (required by new behavior of Augeas 0.4.0)

- new upstream release 0.305
  * t/Config-AugeasC.t: Removed test involving AUGROOT environment
    variable (Lead to FTBS on Debian amd64). The removed tests are
    already performed passing augeas root through aug_init.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Alan Pevec <apevec@redhat.com> 0.304-1
- new upstream release 0.304
  * lib/Config/Augeas.pm (print): Improved print method.
  * lib/Config/Augeas.pm (set): no longer dies when trying to set a
    value to 0. Only dies when the value to set is undefined.

* Mon Sep 01 2008 Alan Pevec <apevec@redhat.com> 0.301-2
- fix test failure

* Mon Sep 01 2008 Alan Pevec <apevec@redhat.com> 0.301-1
- new upstream release 0.301
  * lib/Config/Augeas.pm (move): New method for Augeas 0.3.0
    aug_mv function. 'move' can also be called with 'mv'

* Fri Aug 01 2008 Alan Pevec <apevec@redhat.com> 0.203-1
- new upstream release 0.203

* Wed Jul 30 2008 Alan Pevec <apevec@redhat.com> 0.202-1
- new upstream release 0.202

* Wed Jul 02 2008 Alan Pevec <apevec@redhat.com> 0.201-1
- new upstream release 0.201

* Mon Jun 30 2008 Alan Pevec <apevec@redhat.com> 0.200-1
- Specfile autogenerated by cpanspec 1.77.
- temporary patch to remove /usr/local references

