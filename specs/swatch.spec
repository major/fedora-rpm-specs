Name:           swatch
Version:        3.2.3
Release:        42%{?dist}
Summary:        Tool for actively monitoring log files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://swatch.sourceforge.net/
Source0:        http://download.sf.net/swatch/swatch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(File::Tail)
BuildRequires:  perl(ExtUtils::MakeMaker)
Patch0:         swatch-3.2.3-manpage-fix.patch
Patch1:		swatch-3.2.3-no-more-zombies.patch
Patch2:		swatch-3.2.3-more-cleanups.patch
Patch3:		swatch-3.2.3-mail-at-fix.patch

%description
The Simple WATCHer is an automated monitoring tool that is capable
of alerting system administrators of anything that matches the
patterns described in the configuration file, whilst constantly
searching logfiles using perl.

%prep
%setup -q
%patch -P0 -p1 -b .fix
%patch -P1 -p1 -b .zombies
%patch -P2 -p1 -b .more-cleanups
%patch -P3 -p1 -b .mail-at-fix
chmod -v 644 tools/*

%{?filter_from_requires: %filter_from_requires /^perl(Mail:Sendmail)$/d }
%{?filter_from_requires: %filter_from_requires /^perl(Sys:Hostname)$/d }
%{?perl_default_filter}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist  -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES COPYRIGHT COPYING KNOWN_BUGS README examples/ tools/
%{_bindir}/swatch
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Swatch/
%{perl_vendorlib}/auto/Swatch/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.3-41
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-35
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-32
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-29
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-26
- Perl 5.30 rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov  8 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.3-24
- fix @ handling in mail (bz1646480)

* Wed Oct  3 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.3-23
- more cleanups, see bz1622187 for details

* Thu Aug 23 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.3-22
- apply fix to exec to prevent zombie processes (bz1621238)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-20
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-17
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-15
- Perl 5.24 rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-12
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.3-11
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 3.2.3-8
- Perl 5.18 rebuild

* Fri Feb  8 2013 Tom Callaway <spot@fedoraproject.org> - 3.2.3-7
- fix manpage (bz 909120)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 3.2.3-5
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 3.2.3-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.3-1
- update to 3.2.3

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.2.1-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.2.1-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.1-2.1
Rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.1-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Sep  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.1-1
- Update to 3.2.1.
- Dropped patch: swatch-3.1.1.patch.
- Filtered doc requirements.

* Thu Mar  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.1.1-5
- Rebuild for FC5 (perl 5.8.8).

* Thu Jan  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.1.1-4
- Patch supplied by John Horne: doc updates and $0 handling (#160817).

* Thu May 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.1.1-3
- Add dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.1.1-2
- rebuilt

* Thu Aug 26 2004 Gavin Henry <ghenry[AT]suretecsystems.com> - 0:3.1.1-1
- Retaking ownership, thanks jpo and updating for version 3.1.1

* Tue May 25 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:3.1-0.fdr.3
- Taking temporary ownership.
- Synced specfile suggestions.
- Cleared the requirements.

* Mon May 10 2004 Gavin Henry <ghenry@suretecsystems.com> - 0:3.1-0.fdr.2
- Updated with bugzilla changes.

* Wed Apr 28 2004 Gavin Henry <ghenry@suretecsystems.com> - 0:3.1-0.fdr.1
- Updated for version 3.1

* Thu Mar 18 2004 Gavin Henry <ghenry@suretecsystems.com> - 0:3.0.8-0.fdr.1
- Updated with QA comments and added BuildRequires. Fedora.us - Bug 1346

* Sat Mar 06 2004 Gavin Henry <ghenry@suretecsystems.com> - 0:3.0.8-0
- Initial package release.
