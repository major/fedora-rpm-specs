%define pcscver 1.3.0
%define pcsclib libpcsclite.so.1
%if 0%{?__isa_bits} == 64
%define mark64  ()(64bit)
%endif

%global upstream_name Chipcard-PCSC

Name:           pcsc-perl
Version:        1.4.16
Release:        5%{?dist}
Summary:        Perl interface to the PC/SC smart card library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pcsc-perl.apdu.fr/
Source0:        %{url}%{upstream_name}-v%{version}.tar.gz
Source1:        %{url}%{upstream_name}-v%{version}.tar.gz.asc

BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  pcsc-lite-devel >= %{pcscver}
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
Requires:       %{pcsclib}%{?mark64}
Provides:       perl-pcsc = %{version}-%{release}

%description
This library allows to communicate with a smart card using PC/SC
interface (pcsc-lite) from a Perl script.

%prep
%setup -q -n %{upstream_name}-v%{version}
chmod 644 examples/* # avoid dependencies
f=Changelog ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" DEFINE=-Wall
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# tests need configured readers etc
if ! grep -qF 'dlopen("%{pcsclib}"' PCSCperl.h ; then # sanity check
    echo "ERROR: pcsc lib name mismatch in PCSCperl.h/dependencies" ; exit 1
fi


%files
%license LICENCE
%doc Changelog README examples/
%{perl_vendorarch}/auto/Chipcard/
%{perl_vendorarch}/Chipcard/
%{_mandir}/man3/Chipcard::PCSC*.3*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.16-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.16-2
- Perl 5.40 rebuild

* Wed Feb 21 2024 Jakub Jelen <jjelen@redhat.com - 1.4.16-1
- New upstream release (#2265317)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-23
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-20
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-17
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.14-2
- Perl 5.24 rebuild

* Fri Mar 11 2016 Petr Pisar <ppisar@redhat.com> - 1.4.14-1
- 1.4.14 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.4.13-5
- Fix use of __isa_bits macro

* Mon Sep 14 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.4.13-4
- Use __isa_bits macro instead of list of 64-bit architectures

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-2
- Perl 5.22 rebuild

* Thu Apr 30 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-1
- 1.4.13 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.12-11
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.12-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.4.12-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.12-2
- Perl mass rebuild

* Tue Jun  7 2011 Tomas Mraz <tmraz@redhat.com> - 1.4.12-1
- New upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep  7 2010 Tomas Mraz <tmraz@redhat.com> - 1.4.10-1
- New upstream version

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.4.8-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.4.8-2
- rebuild against perl 5.10.1

* Fri Sep 25 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.8-1
- New upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 27 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.4.7-1
- 1.4.7.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.6-4
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.6-3
- Autorebuild for GCC 4.3

* Tue Aug  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.6-2
- Apply #defines patch only when building with pcsc-lite < 1.4.0.
- License: GPLv2+

* Tue Apr 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.6-1
- 1.4.6 + PCSCperl.h #defines fixes.
- BuildRequire perl(ExtUtils::MakeMaker).

* Sun Dec 24 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.4-3
- Eliminate file based dependencies.

* Thu Nov  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.4-2
- Rebuild with pcsc-lite 1.3.2 for extended APDU support.

* Tue Aug 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.4-1
- 1.4.4.

* Wed May 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.3-1
- 1.4.3.

* Mon Mar  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-1
- 1.4.1.
- Don't hardcode required pcsc-lite-libs version, use shared lib file instead.
- Convert docs to UTF-8.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.1-8
- Rebuild, cosmetics.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3.1-7
- rebuild on all arches

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.1-6
- Provide perl-pcsc, fixate required pcsc-lite version to 1.2.0.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.3.1-5
- rebuilt

* Fri Jan  7 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.1-4
- Honor $RPM_OPT_FLAGS, remove (some) extra include dirs from build (#1281).
- Improve summary and description.

* Wed May 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.1-0.fdr.3
- BuildRequire perl >= 1:5.6.1 for vendor install dir support.
- Use pure_install to avoid perllocal.pod workarounds.

* Sun Apr 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.1-0.fdr.2
- Require perl(:MODULE_COMPAT_*).

* Fri Apr  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.1-0.fdr.1
- Update to 1.3.1.

* Sun Feb  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.0-0.fdr.2
- Reduce directory ownership bloat.

* Wed Dec 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3.0-0.fdr.1
- Update to 1.3.0.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.2-0.fdr.4
- More spec cleanups.

* Wed Aug 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.2-0.fdr.3
- Spec cleanups, install into vendor dirs.

* Fri Jul  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.2-0.fdr.2
- Fix dir ownerships, non-root strip during build.

* Thu May 29 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.2-0.fdr.1
- Update to 1.2.2.
- Drop patch and hacks, already applied/fixed upstream.

* Sun May 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.1-0.fdr.1
- Update to 1.2.1.
- Fix build and runtime dependencies.

* Thu May 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2.0-0.fdr.1
- First build.
