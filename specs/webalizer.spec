%define ver 2.23
%define patchlevel 08

%if 0%{?fedora} < 18 && 0%{?rhel} < 7
%global db_devel  db4-devel
%else
%global db_devel  libdb-devel
%endif

Name: webalizer
Summary: A flexible Web server log file analysis program
Version: 2.23_08
Release: 27%{?dist}
URL: http://www.mrunix.net/webalizer/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlevel}-src.tgz
Source1: webalizer.conf
Source2: webalizer.cron
Source3: webalizer-httpd.conf
Source4: webalizer.sysconfig
Patch4: webalizer-2.21-02-underrun.patch
Patch6: webalizer-2.23-05-confuser.patch
Patch9: webalizer-2.23-05-groupvisit.patch
Patch10: webalizer-2.23-08-memmove.patch
# From Debian
Patch21: 02_fix_a_spelling_error.diff
Patch22: 04_Fix_cast_warnings_in_output.c.diff
Patch23: 14_add_search_engines.diff
Patch24: 17_fix_typo_supress_suppress_in_sample.conf.diff
Patch25: 27_fix_compilation_with_gcc-10.diff
BuildRequires: make
BuildRequires:  gcc
BuildRequires: gd-devel, %{db_devel}, bzip2-devel
BuildRequires: GeoIP-devel
Requires(pre): shadow-utils
Requires: httpd, crontabs

%description
The Webalizer is a Web server log analysis program. It is designed to
scan Web server log files in various formats and produce usage
statistics in HTML format for viewing through a browser. It produces
professional looking graphs which make analyzing when and where your
Web traffic is coming from easy.

%prep
%setup -q -n %{name}-%{ver}-%{patchlevel}
%patch -P4 -p1 -b .underrun
%patch -P6 -p1 -b .confuser
%patch -P9 -p1 -b .groupvisit
%patch -P10 -p1 -b .memmove
%patch -P21 -p1 -b .spelling_error
%patch -P22 -p1 -b .cast_warnings
%patch -P23 -p1 -b .sample_add_search_engines
%patch -P24 -p1 -b .sample_typo
%patch -P25 -p1 -b .gcc10_common_support

%build
#CPPFLAGS="-I%{_includedir}/db4" ; export CPPFLAGS
#CFLAGS="$RPM_OPT_FLAGS $CPPFLAGS -D_GNU_SOURCE" ; export CFLAGS
%configure --enable-dns --enable-bz2 --enable-geoip

%make_build

%install
mkdir -p %{buildroot}%{_localstatedir}/www/usage \
         %{buildroot}%{_sysconfdir}/cron.daily

mkdir -p %{buildroot}%{_localstatedir}/lib/webalizer

%make_install

install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}
install -p -m 644 *.png %{buildroot}%{_localstatedir}/www/usage
install -p -m 755 %{SOURCE2} \
         %{buildroot}%{_sysconfdir}/cron.daily/00webalizer
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 644 %{SOURCE3} \
        %{buildroot}%{_sysconfdir}/httpd/conf.d/webalizer.conf
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 %{SOURCE4} \
        %{buildroot}%{_sysconfdir}/sysconfig/webalizer

rm -f %{buildroot}%{_sysconfdir}/webalizer.conf.sample

%pre
getent group webalizer >/dev/null || groupadd -r webalizer
getent passwd webalizer >/dev/null || \
    useradd -r -g webalizer -d %{_localstatedir}/www/usage -s /sbin/nologin \
    -c "Webalizer" webalizer
exit 0

%files
%doc README
%{_mandir}/man1/*.1*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/webalizer.conf
%{_sysconfdir}/cron.daily/00webalizer
%config(noreplace) %{_sysconfdir}/httpd/conf.d/webalizer.conf
%config(noreplace) %{_sysconfdir}/sysconfig/webalizer
%attr(-, webalizer, root) %dir %{_localstatedir}/www/usage
%attr(-, webalizer, root) %dir %{_localstatedir}/lib/webalizer
%attr(-, webalizer, root) %{_localstatedir}/www/usage/*.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.23_08-26
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 15 2022 Sérgio Basto <sergio@serjux.com> - 2.23_08-19
- Add some patches from Debian, fix gcc10 common support

* Sat Jan 15 2022 Sérgio Basto <sergio@serjux.com> - 2.23_08-18
- Fix warning message (#2040985)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Sérgio Basto <sergio@serjux.com> - 2.23_08-6
- Add patch to fix some undefined behaviour by switching to memmove() (#1409349)

* Tue Dec 20 2016 Robert Scheck <robert@fedoraproject.org> - 2.23_08-5
- Build on EPEL >= 7 against libdb-devel to enable DNS/GeoDB code

* Thu Dec 01 2016 Sérgio Basto <sergio@serjux.com> - 2.23_08-4
- Package review (#226536)
- Fix bogus date in changelog
- Enable-geoip
- Clean-up spec

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.23_08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Jan Kaluza <jkaluza@redhat.com> - 2.23_08-1
- update to new version 2.23-08 (#1119536)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 2.23_05-8
- rebuild for new GD 2.1.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Joe Orton <jorton@redhat.com> - 2.23_05-6
- fix config for 2.4 (#871494)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Joe Orton <jorton@redhat.com> - 2.23_05-4
- build (conditionally) against libdb-devel

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23_05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.23_05-2
- Rebuild for new libpng

* Thu Jul 14 2011 Joe Orton <jorton@redhat.com> - 2.23_05-1
- update to 2.23_05

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21_02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 17 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.21_02-4
- Don't run cronjob unless configured in /etc/sysconfig/webalizer (merge review #298203)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21_02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Joe Orton <jorton@redhat.com> 2.21_02-2
- update to 2.21-02 (thanks to Robert Scheck)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20_01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 Joe Orton <jorton@redhat.com> 2.20_01-1
- update to 2.20_01

* Mon Jul 14 2008 Joe Orton <jorton@redhat.com> 2.01_10-37
- rebuild for new BDB

* Thu Feb  7 2008 Joe Orton <jorton@redhat.com> 2.01_10-36
- fix build with new glibc, use _GNU_SOURCE 

* Thu Feb  7 2008 Joe Orton <jorton@redhat.com> 2.01_10-35
- use %%{_localestatedir}, remove tabs, require httpd not
  webserver, mark webalizer.conf config(noreplace) (#226536)

* Thu Aug 30 2007 Joe Orton <jorton@redhat.com> 2.01_10-34
- clarify License tag

* Wed Aug 22 2007 Joe Orton <jorton@redhat.com> 2.01_10-33
- rebuild

* Mon Mar 19 2007 Joe Orton <jorton@redhat.com> 2.01_10-32
- spec file cleanups (#226536):
 * convert to UTF-8
 * fix BuildRoot, Summary
 * add Requires(pre) for shadow-utils, remove Prereqs
 * trim BuildRequires to png-devel, db4-devel
 * use smp_mflags in make
 * use sysconfdir macro throughout
 * preserve file timestamps on installation

* Mon Jan 29 2007 Joe Orton <jorton@redhat.com> 2.01_10-31
- rebuild to pick up new db4 soname

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.01_10-30.1
- rebuild

* Fri Jun 16 2006 Joe Orton <jorton@redhat.com> 2.01_10-30
- add patch set from Jarkko Ala-Louvesniemi (#187344, #187726, #188248)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.01_10-29.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.01_10-29.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Sep 21 2005 Joe Orton <jorton@redhat.com> 2.01_10-29
- run with -Q from cron (#120913)
- remove ancient trigger and post scriptlets
- only read webalizer.conf from $PWD if owner matches user (#158174)

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 2.01_10-28
- rebuild

* Mon Jan 24 2005 Joe Orton <jorton@redhat.com> 2.01_10-27
- don't package /etc/webalizer.conf.sample (#145980)

* Fri Nov 19 2004 Joe Orton <jorton@redhat.com> 2.01_10-26
- rebuild

* Wed Aug 18 2004 Joe Orton <jorton@redhat.com> 2.01_10-25
- rebuild

* Fri Jun 18 2004 Alan Cox <alan@redhat.com>
- Added IPv6 patch from PLD c/o Robert Scheck
- Added tests to trap bogus logfiles with negative times/dates
- Fixed leap seconds

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Mar 27 2004 Joe Orton <jorton@redhat.com> 2.0_10-22
- allow access to /usage from ::1 and 127.0.0.1 by default
- require crontabs

* Sun Mar 21 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- keep apps owned by root:root

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 12 2004 Florian La Roche <Florian.LaRoche@redhat.de> 2.0_10-19
- add an "exit 0" to post script

* Thu Jan  8 2004 Joe Orton <jorton@redhat.com> 2.01_10-18
- update default config

* Thu Jan  8 2004 Joe Orton <jorton@redhat.com> 2.01_10-17
- add fix for #111433

* Fri Nov 28 2003 Joe Orton <jorton@redhat.com> 2.01_10-16
- merge from Taroon

* Tue Oct 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add %%clean specfile target

* Fri Aug  1 2003 Joe Orton <jorton@redhat.com> 2.01_10-15.ent
- support large (>2gb) log files on 32-bit platforms
- move default output directory to /var/www/usage
- add conf.d/webalizer.conf to add alias for /usage
- only allow access to usage stats from localhost by default
- change default config: don't ignore out-of-sequence log entries,
  count .php and .shtml as "page" extensions.

* Thu Jul  3 2003 Joe Orton <jorton@redhat.com> 
- rebuilt

* Thu Jun 05 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 05 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- fix owner in /var/www/html/usage for "rpm -Va"

* Tue May 06 2003 Phil Knirsch <pknirsch@redhat.com> 2.01_10-12
- Bumped release and rebuilt due to new gd version.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2.01_10-11
- rebuilt

* Thu Nov  7 2002 Than Ngo <than@redhat.com> 2.01_10-10
- requires webserver (bug #74006)
- unpackaged file issue

* Tue Jul 02 2002 Than Ngo <than@redhat.com> 2.01_10-9
- fix a bug in post

* Mon Jul 01 2002 Than Ngo <than@redhat.com> 2.01_10-8
- fix a bug in pre (bug #67634)

* Thu Jun 27 2002 Than Ngo <than@redhat.com> 2.01_10-7
- add shadow-utils in prereq 

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 21 2002 Than Ngo <than@redhat.com> 2.01_10-5
- fixed bug #62062, #64392, #63685

* Thu May 30 2002 Nalin Dahyabhai <nalin@redhat.com> 2.01_10-4
- fixup some linkage problems (was getting db2, which shouldn't happen)

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.01_10-2
- Use db4

* Wed Apr 17 2002 Than Ngo <than@redhat.com> 2.01_10-1
- 2.01_10 fixes a posible buffer overflow bug in DNS resolver code

* Thu Mar 21 2002 Preston Brown <pbrown@redhat.com>
- put transient files in /var/lib/webalizer
- removed sysconfig runtime option.  Remove the package or cron script if 
  you do not want it to run (#59752)
- make default quiet operation

* Mon Feb 25 2002 Than Ngo <than@redhat.com> 2.01_09-5
- allows multiple partial log files to be used instead of one huge one.(bug #60295)

* Thu Feb 21 2002 Than Ngo <than@redhat.com> 2.01_09-4
- add function to enable/disable webalizer (bug #59752)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Nov 14 2001 Than Ngo <than@redhat.com> 2.01_09-2
- make cron jobs quiet (bug #56249)

* Wed Oct 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.01_09-1
- Update to 2.01-09, fixing security bugs

* Thu Sep 20 2001 Than Ngo <than@redhat.com> 2.01_06-13
- update config file (bug #53881)

* Sun Sep 16 2001 Than Ngo <than@redhat.com> 2.01_06-12
- add patch from author to fix Webalizer dumps core when MangleAgents is set to 1

* Mon Jul 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Remove empty post
- Mark the crontab file as config(noreplace) 

* Fri Jul 13 2001 Than Ngo <than@redhat.com> 2.01_06-10
- fix build dependencies (bug #48939)
- Copyright->License

* Fri Jun 15 2001 Than Ngo <than@redhat.com>
- add missing icons (bug #43220)

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- rebuilt for the distro

* Fri May 18 2001 Than Ngo <than@redhat.com>
- don't run webalizer when access log file is empty (Bug #41322)

* Wed Feb 14 2001 Tim Powers <timp@redhat.com>
- enable dns-lookups (patched to use correct db header) (bug #27612)

* Thu Feb  1 2001 Tim Powers <timp@redhat.com>
- make the cronjob called 00webalizer, so that it runs before everything else

* Wed Jan 31 2001 Tim Powers <timp@redhat.com>
- fixed bug 25351, where webalizer was being run after apache is
  logrotated.

* Tue Oct 17 2000 Than Ngo <than@redhat.com>
- update to 2.01-06

* Tue Oct 17 2000 Than Ngo <than@redhat.com>
- fixed wrong OutputDir (bug #19180)

* Thu Aug 3 2000 Tim Powers <timp@redhat.com>
- rebuilt against libpng-1.0.8

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt

* Mon Jun 19 2000 Karsten Hopp <karsten@redhat.de>
- rebuild for 7.0
- changed mandir
- changed graph output to png instead of gif
- changed path to apache root (/var/www)

* Mon Nov 08 1999 Bernhard Rosenkränzer <bero@redhat.com>
- handle RPM_OPT_FLAGS

* Tue Sep 28 1999 Preston Brown <pbrown@redhat.com>
- updated for Secure Web Server 3.1

* Mon May 03 1999 Preston Brown <pbrown@redhat.com>
- initial build for Secure Web Server 3.0
