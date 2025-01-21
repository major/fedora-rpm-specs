Summary: Automatic mail answering program
Summary(de): Programm zum automatisierten Beantworten von Mails
Name: vacation
Version: 1.2.7.1
Release: 29%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source: http://downloads.sourceforge.net/vacation/%{name}-1.2.7.1.tar.gz
Source1: license-clarification
Requires: smtpdaemon perl(GDBM_File)
URL: http://sourceforge.net/projects/vacation/
BuildRequires: make
BuildRequires: gdbm-devel
BuildRequires: perl-generators
BuildRequires: gcc

%description 
Vacation is the automatic mail answering program found
on many Unix systems.

%description	-l de
Vacation beantwortet automatisch alle eingehenden EMails
mit einer Standard-Antwort und ist auf vielen Unix-Systemen
vorhanden.

%prep
%setup -q -n vacation-1.2.7.1
cp -p %SOURCE1 .

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

install -D -p -m 755 vacation        $RPM_BUILD_ROOT%{_bindir}/vacation
install -D -p -m 755 vaclook         $RPM_BUILD_ROOT%{_bindir}/vaclook
install -D -p -m 444 vaclook.man     $RPM_BUILD_ROOT%{_mandir}/man1/vaclook.1
install -D -p -m 444 vacation-en.man $RPM_BUILD_ROOT%{_mandir}/man1/vacation.1
install -D -p -m 444 vacation-de.man $RPM_BUILD_ROOT%{_mandir}/de/man1/vacation.1

%files
%{_bindir}/vacation
%{_bindir}/vaclook
%{_mandir}/man*/*
%lang(de) %{_mandir}/de/man*/*

%doc COPYING README README.smrsh ChangeLog license-clarification

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.7.1-28
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.2.7.1-15
- Fixed missing GCC BuildReq

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.7.1-4
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.1-1
- updated to vacation-1.2.7.1
- added german manual page

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-0.5.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.1-0.4.beta2
- updated to vacation-1.2.7.1-beta2

* Tue Oct 04 2011 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.1-0.3.beta1
- Added requirement perl(GDBM)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7.1-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.1-0.1.beta1
- update from upstreams
- Add the Auto-Submitted: header as per RFC3834.
- Stop Vacation from munging the GECOS information of users and 
  instead pass it quoted to the MTA for it to deal with.

* Wed Aug 05 2009 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.0-7
- changed license to BSD as upstream told me
  (corresponding mail is included in doc).

* Mon Aug 03 2009 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.0-6
- changed license to GPLv2 until licensing is clarified with upstream
- changed source URL to "downloads" instead of "download".
  (bz #474802)

* Mon Jul 06 2009 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.0-5
- Fixes according comments from bz #474802

* Wed Jun 24 2009 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.0-4
- repackaged for Fedora 11.
- Fixed bugs from bz #474802

* Fri Dec 05 2008 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.2.7.0-1
- Upgraded to 1.2.7.0
- repackaged for Fedora 10.

* Tue Sep 03 2002 Pete O'Hara <pete@guardiandigital.com>
- Version 1.2.7.rc1, Release 1.2.1
  - Upgraded to 1.2.7.rc1

* Mon Aug 26 2002 Pete O'Hara <pete@guardiandigital.com>
- Version 1.2.6.1, Release 1.2.0
  - Initial release for Mail Suite

* Sun Nov 11 2001 Devon <devon@tuxfan.homeip.net>
- upgrade to version 1.2.7.rc1
* Sat Nov 10 2001 Devon <devon@tuxfan.homeip.net>
- upgrade to version 1.2.6
* Wed Sep 19 2001 Devon <devon@tuxfan.homeip.net>
- added %%post link /etc/smrsh to /usr/bin/vacation
- added %%postun deletion of /etc/smrsh/vacation
- defined a umask of 022 fix permissions on created files.
  $HOME/.forward was created group writable, smrsh refused
  to run in that case. See vacation-1.2.2-permissions.patch

* Mon Aug 07 2000 Than Ngo <than@redhat.de>
- fix specfile and patch file to rebuilt

* Mon Aug 07 2000 Michael Stefaniuc <mstefani@redhat.com>
- upgraded to 1.2.2
- fixed security fix

* Wed Aug 02 2000 Than Ngo <than@redhat.de>
- fix manpath (Bug #15070)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Sun Jul 16 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add security fix

* Mon Jul 10 2000 Than Ngo <than@redhat.de>
- fix problem (it won't include the .vacation.msg) (bug #13572)
- use RPM macros

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun May 28 2000 Ngo Than <than@redhat.de>
- rebuild for 7.0
- put man pages in correct place
- cleanup specfile
- fix Summary

* Fri Dec 10 1999 Ngo Than <than@redhat.de>
- initial RPM for powertools-6.2
