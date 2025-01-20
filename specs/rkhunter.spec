# In f20+ use unversioned docdirs, otherwise the old versioned one
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           rkhunter
Version:        1.4.6
Release:        27%{?dist}
Summary:        A host-based tool to scan for rootkits, backdoors and local exploits

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://rkhunter.sourceforge.net/
Source0:        http://downloads.sourceforge.net/rkhunter/rkhunter-%{version}.tar.gz
Source2:        01-rkhunter
Source3:        rkhunter.sysconfig
Patch0:         rkhunter-1.4.6-fedoraconfig.patch
# libkeyutils is an actual legit library now, so this old check is a false positive.
Patch1:         rkhunter-1.4.6-drop-libkeyutils-check.patch
# have ssh checks use the sshd.d directoy config files too.
Patch2:         rkhunter-1.4.6-ssh.d.patch
# Fix grep/egrep changes in f38+
Patch3:         rkhunter-1.4.6-grep.patch
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       coreutils, binutils, kmod, findutils, grep
Requires:       e2fsprogs, procps, lsof, iproute, wget
Requires:       perl-interpreter, perl(strict), perl(IO::Socket), s-nail, logrotate
Requires:       crontabs

%description
Rootkit Hunter (RKH) is an easy-to-use tool which checks
computers running UNIX (clones) for the presence of rootkits
and other unwanted tools.

%prep

%autosetup -p1

%{__cat} <<'EOF' >%{name}.logrotate
%{_localstatedir}/log/%{name}/%{name}.log {
    weekly
    notifempty
    create 640 root root
}
EOF

%build
# Nothing to be built

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_bindir}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_sysconfdir}/{cron.daily,sysconfig,logrotate.d}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_datadir}/%{name}/scripts
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_mandir}/man8
%{__mkdir} -m700 -p ${RPM_BUILD_ROOT}%{_var}/lib/%{name}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_var}/log/%{name}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/i18n

%{__install} -m755 -p files/%{name}             ${RPM_BUILD_ROOT}%{_bindir}/

%{__install} -m644 -p files/backdoorports.dat   ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/
%{__install} -m644 -p files/mirrors.dat         ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/
%{__install} -m644 -p files/programs_bad.dat    ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/
%{__install} -m644 -p files/i18n/cn             ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/i18n/
%{__install} -m644 -p files/i18n/en             ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/i18n/

%{__install} -m644 -p files/CHANGELOG           ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__install} -m644 -p files/LICENSE             ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__install} -m644 -p files/README              ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__install} -m755 -p files/check_modules.pl    ${RPM_BUILD_ROOT}%{_datadir}/%{name}/scripts/
%{__install} -m644 -p files/*.8                 ${RPM_BUILD_ROOT}%{_mandir}/man8/
# Don't ship these unless we want to Require the perl modules
#%{__install} -m750 -p files/filehashmd5.pl      ${RPM_BUILD_ROOT}%{_prefix}/lib/%{name}/scripts/
#%{__install} -m750 -p files/filehashsha1.pl     ${RPM_BUILD_ROOT}%{_prefix}/lib/%{name}/scripts/
%{__install} -m755 -p %{SOURCE2}                ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/%{name}
%{__install} -m644 -p %{name}.logrotate         ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -m640 -p files/%{name}.conf        ${RPM_BUILD_ROOT}%{_sysconfdir}/
%{__install} -m640 -p %{SOURCE3}                ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

%files
%doc %{_pkgdocdir}/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
%{_sysconfdir}/cron.daily/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/db
%ghost %{_var}/lib/%{name}/db/mirrors.dat
%ghost %{_var}/lib/%{name}/db/programs_bad.dat
%ghost %{_var}/lib/%{name}/db/backdoorports.dat
%{_var}/lib/%{name}/db/i18n
%dir %{_var}/log/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_pkgdocdir}
%{_mandir}/man8/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.6-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Kevin Fenzi <kevin@scrye.com> - 1.4.6-21
- More complete fix for egrep changes.

* Mon Apr 10 2023 Kevin Fenzi <kevin@scrye.com> - 1.4.6-20
- Patch grep/egrep changes to avoid warnings in F38+

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Kevin Fenzi <kevin@scrye.com> - 1.4.6-17
- Switch to using s-nail instead of mailx.

* Sat Jun 11 2022 Kevin Fenzi <kevin@scrye.com> - 1.4.6-16
- Whitelist .dockerignore man page ( rhbz#2050551 )

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Kevin Fenzi <kevin@scrye.com> - 1.4.6-14
- Add exclude for containers-common man page ( rhbz#2020015 )

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 07 2021 Kevin Fenzi <kevin@scrye.com> - 1.4.6-12
- Fix bug around ssh protocol detection ( rhbz#1597635 )

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.4.6-10
- Drop check on libkeyutils, it's a legit library now. Fixes rhbz#1914662
- Look for and use the ssh.d config snippet direction. Thanks John Dodson for patch. Fixes rhbz#1851620

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Kevin Fenzi <kevin@scrye.com> - 1.4.6-8
- Add allow for podman's /dev/shm files (fixes bug #1828698 )

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Kevin Fenzi <kevin@scrye.com> - 1.4.6-6
- Adjust config for PermitRootLogin change in f31+. Fixes bug #1756593

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 1.4.6-4
- Drop ifup/ifdown since network-scripts is now deprecated. Fixes bug #1698920

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 25 2018 Kevin Fenzi <kevin@scrye.com> - 1.4.6-1
- Update to 1.4.6. Fixes bug #1547315
- Allow KRA vault log files. Fixes bug #1541472
- ipc_shared_mem warning fixed upstream. Fixes bug #1524456

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-6
- Escape macros in %%changelog

* Mon Nov 27 2017 Kevin Fenzi <kevin@scrye.com> - 1.4.4-5
- Add fix for new rpm queryformat and ARCH. Fixes bug #1517387

* Sat Aug 12 2017 Kevin Fenzi <kevin@scrye.com> - 1.4.4-4
- Disable ipc_shared_mem test for now due to false positives. Bug #1472299

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.4.4-2
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Thu Jun 29 2017 Kevin Fenzi <kevin@scrye.com> - 1.4.4-1
- Update to 1.4.4. Fixes bug #1466318
- Fix for logger and spaces. Fixes bug #1284403

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-12
- Add /dev/shm/qb* files to whitelist. Fixes bug #1403602
- Add /dev/shm/squid-ssl_session_cache.shm to whitelist. Fixes bug #1411130

* Wed Apr 20 2016 Kevin Fenzi <kevin@scrye.com> - 1.4.2-11
- Add /dev/shm/lldpad files to whitelist. Fixes bug #1293059

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Kevin Fenzi <kevin@scrye.com> - 1.4.2-9
- Add /dev/shm/squid files to whitelist. Fixes bug #1279632

* Tue Oct 13 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-8
- Change config patch to account for change in default SSH config

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 20 2014 Kevin Fenzi <kevin@scrye.com> 1.4.2-6
- Add /etc/.updated systemd file to whitelist. Fixes bug #1173481
- Add patch to fix grep -a issue with too many arguments output. 

* Mon Oct 27 2014 Kevin Fenzi <kevin@scrye.com> 1.4.2-5
- Set /var/lib/rkhunter to be mode 700. fixes bug #1154428

* Fri Sep 26 2014 Kevin Fenzi <kevin@scrye.com> 1.4.2-4
- Fix cron script to work with non bash shells. Fixes bug #1146717

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Kevin Fenzi <kevin@scrye.com> 1.4.2-2
- Add patch to fix ipcs command in non en locales
- Add config to fix freeipa installs. Fixes bug #994567

* Fri Mar 14 2014 Kevin Fenzi <kevin@scrye.com> 1.4.2-1
- Update to 1.4.2

* Sun Sep 01 2013 Kevin Fenzi <kevin@scrye.com> 1.4.0-9
- Add patch for now to help spaces in allowdev file handling. Fixes bug #984180

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.4.0-9
- Perl 5.18 rebuild

* Sat Jul 27 2013 Kevin Fenzi <kevin@scrye.com> 1.4.0-8
- Fix for unversioned docs
- Requires: crontabs. Fixes bug #989110

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.0-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Kevin Fenzi <kevin@scrye.com> 1.4.0-5
- Add /dev/md/autorebuild.pid to whitelist. Fixes bug #857315

* Sat Aug 18 2012 Kevin Fenzi <kevin@scrye.com> 1.4.0-4
- Add /var/log/pki-ca/system to whitelist for FreeIPA. Fixes bug #849251

* Wed Aug 15 2012 Kevin Fenzi <kevin@scrye.com> 1.4.0-3
- Fix /bin/ad false positive. Fixes bug #831989

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Kevin Fenzi <kevin@scrye.com> - 1.4.0-1
- Update to 1.4.0

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.3.8-15
- Add workaround for /lib/java false positive. Fixes bug #806972

* Wed Feb  8 2012 Kay Sievers <kay@redhat.com> - 1.3.8-14
- modutils are for Linux 2.4 and no longer provided; depend on kmod

* Fri Jan 27 2012 Kevin Fenzi <kevin@scrye.com> 1.3.8-13
- Drop net-tools, no longer needed. Fixes bug #784803
- Add /dev/shm/spice.* to whitelist. Fixes bug #784882

* Fri Jan 06 2012 Kevin Fenzi <kevin@scrye.com> 1.3.8-12
- Add /etc/.java to whitelist. Fixes bug #770972

* Fri Nov 25 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-11
- Add /usr/share/man/man5/.k5identity.5.gz to whitelisted hidden files. 

* Wed Oct 12 2011 Jim Pirzyk <jim+rpm@pirzyk.org> - 1.3.8-10
- Update %%files section so that some .dat files are marked %%ghost

* Fri Aug 05 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-9
- Add patch to fix ALLOWPROCDELFILE config option. fixes bug #727524

* Fri Jul 08 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-8
- Fix typo

* Fri Jul 08 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-7
- Add patch to fix out of the box warning on rkhunter script. 
- Fixes bug #719270
- Add etckeeper and tomboy files. Fixes bug #719265 and #719259

* Tue Jun 21 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-6
- Change ssh check back to 2 - bug #596775
- Drop hard Requires on prelink. It will be used if present - bug #714067

* Thu Apr 21 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-5
- Add /dev/.mount to ALLOW_HIDDENDIR - bug #697599

* Wed Apr 13 2011 Kevin Fenzi <kevin@scrye.com> - 1.3.8-4
- Don't send warning emails anymore. They cause selinux issues and are not very helpful.
- Fixes bug #660544

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.8-2
- Adjust config some - bug #596775

* Fri Nov 26 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.8-1
- Update to 1.3.8

* Wed Nov 24 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-9
- Drop /var/run as it's not used anymore - bug #656684

* Wed Oct 06 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-8
- Add patch to make rkhunter use unhide if installed - bug #636396

* Sat Jun 05 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-7
- Add ipsec.hmac exclude - bug #560594

* Fri May 28 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-6
- Add exclude for md-device-map - bug #596731
- Supress ssh version check - bug #596775

* Sat Mar 06 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-5
- Change config to not specify XINETD_PATH - bug #560562

* Sat Jan 23 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-4
- Change email to just root instead of root@localhost - bug #553179
- Add .k5login.5.gz to files whitelist - bug #553134

* Tue Jan 05 2010 Kevin Fenzi <kevin@tummy.com> - 1.3.6-3
- Add some more ssh hmac files to whitelist - bug #552621
- Re-add /dev/.mdadm.map to whitelisted files - bug #539405

* Tue Dec 01 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.6-2
- Disable apps check by default - bug #543065

* Sun Nov 29 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.6-1
- Update to 1.3.6

* Thu Nov 26 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-9
- Add exception for /dev/.mdadm file - bug #539405

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-7
- Add exception for software raid udev file - bug #509253

* Sat Jun 06 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-6
- Add /usr/bin/.fipscheck.hmac to ok files - bug #494096

* Sun Mar 08 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-5
- Fix typo in patch file

* Wed Mar 04 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-4
- Rework spec file
- Add check for the new hmac ssh files 

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-3
- Update cron job to include hostname (thanks  Manuel Wolfshant)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 02 2009 Kevin Fenzi <kevin@tummy.com> - 1.3.4-1
- Update to 1.3.4
- Use libdir as tmp dir - bug #456340

* Sat Dec 13 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.2-6
- Fix cron job sending as attachment - bug #472679
- Fix cron job trying to send with colors - bug #475916

* Wed Sep 03 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.2-5
- Patch debug tmp file issue - bug #460628

* Mon Jun 16 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.2-4
- Fix cron script to only mail on warn/error - bug #450703
- Fix conditional to account for fc10 rsyslog

* Mon Apr 28 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.2-3
- Change cron to run after prelink - bug #438622

* Wed Mar 26 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.2-2
- Move things to more standard locations for selinux - bug #438184
- Add exception for pulseaudio file - bug #438622

* Thu Feb 28 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.2-1
- Update to 1.3.2
- Fix cron script

* Thu Feb 28 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.0-2
- Use /etc/redhat-release for EPEL and /etc/fedora release for Fedora.
- Add conditionals to support EPEL
- Fix man page warning. 

* Sun Feb 03 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.0-1
- Revive package, clean up spec
- Update to 1.3.0

* Sat Mar 18 2006 Greg Houlette <tamaster@pobox.com> - 1.2.8-3
- Made an RPM transparent change to move the sha1 canary check
  file out of CVS and into the external lookaside cache (whose
  filename changes with every new package release anyway...)

* Fri Mar 17 2006 Greg Houlette <tamaster@pobox.com> - 1.2.8-2
- Fixed architectural dependency during package creation eliminating
  use of _libdir configure macro (x86_64 /usr/lib64 mis-targeting)

* Tue Mar 7 2006 Greg Houlette <tamaster@pobox.com> - 1.2.8-1
- New package version release
- reworked the .spec file to support optional dist tag
- Updated the application check default patchfile (chunk failure)
- Changed to SHA1 for optional message digest (canary check)
- Added a couple of suggested skip entries to rkhunter.conf

* Sat Jun 11 2005 Greg Houlette <tamaster@pobox.com> - 1.2.7-1
- Added signature auto-updating to CRON scan (new script)
- Removed BOOTSCAN pending rewrite to full SysV Init scan in background
- Added the --append-log command line option
- Added Date Stamping to output
- Fixed bug in /etc/group missing report
- New package version release

* Sun Jan 2 2005 Greg Houlette <tamaster@tekarmory.com> - 0:1.1.9-1
- New package version release
- Added the --run-application-check command line option
  to listing in command help
- Replaced 'Here' Doc editing of rkhunter.conf file
  with in-place Perl edit
- tweaked rpmbuild -bb Autoclean

* Fri Oct 15 2004 Greg Houlette - 0:1.1.8-0.fdr.1 (revisited)
- Removed redundant buildrequires /bin/sh, coreutils and perl
- Revise postun scriptlet
- Added /usr/share/doc/rkhunter-1.1.8/ to files list

* Mon Oct 11 2004 Greg Houlette - 0:1.1.8-0.fdr.1
- Changed Release Tag to 0.fdr.1 (testing) for QA
- Removed wget from dependencies
- Hid (temporarily) the --skip-application-check command
  line option from being listed in help
- Fixed the spec files list, again!

* Fri Oct 8 2004 Greg Houlette - 0:1.1.8-0.fdr.0.2.beta2
- Unified and disabled the md5 canary check in prep
  (check is now optional) removing the sha1 cross-check
- Fixed the spec files list, adding the /var/rkhunter
  directory and the /usr/bin/rkhunter executable
- Fixed missing dependencies (rkh uses runtime checks)
- Disabled "auto-clean" for rpmbuild -bb
- Changed Application version scan default to
  disabled awaiting backport fix in upstream sources
- Fixed shared_man_search.patch, configuration files
  verify and added postun(install) cleanup

* Fri Oct 1 2004 Greg Houlette - 0:1.1.8-0.fdr.0.1.beta1
- More cosmetic patchwork
- Changed Release Tag to beta1 (pre-release) for QA submit

* Tue Sep 28 2004 Greg Houlette - 0:1.1.8-0.fdr.1
- Removed hidden_search.patch (1.1.7) after it was
  merged into upstream source by Michael Boelen
- Removed .spec file from md5 and sha1 file checks
  (it must be modifiable by Fedora QA release build)
- Added BOOTSCAN description file to documentation
- Restructured dynamic file creation ('Here' Docs)
  moving them to the "prep" stage so that *_ALL_*
  files are available prior to the "build" stage
  (for inspection purposes)
- Added a /etc/sysconfig/rkhunter parameters file

* Sun Aug 29 2004 Greg Houlette - 0:1.1.7-0.fdr.1
- Cosmetic patchwork

* Sat Aug 21 2004 Greg Houlette - 0:1.1.6-0.fdr.1
- Moderate reworking of .spec file for packaging standards
- Added md5 and sha1 file checks to prep procedure for source .rpm
- Included an optional rc.local replacement for scan on boot (with full logging)

* Tue Aug 10 2004 Michael Boelen - 1.1.5
- Added update script
- Extended description

* Sun Aug 08 2004 Greg Houlette - 1.1.5
- Changed the install procedure eliminating the specification of
  destination filenames (only needed if you are renaming during install)
- Changed the permissions for documentation files (root only overkill)
- Added the installation of the rkhunter Man Page
- Added the installation of the programs_{bad, good}.dat database files
- Added the installation of the LICENSE documentation file
- Added the chmod for root only to the /var/rkhunter/db directory

* Sun May 23 2004 Craig Orsinger (cjo) <cjorsinger@earthlink.net>
- version 1.1.0-1.cjo
- changed installation in accordance with new rootkit installation
  procedure
- changed installation root to conform to LSB. Use standard macros.
- added recursive remove of old build root as prep for install phase

* Wed Apr 28 2004 Doncho N. Gunchev - 1.0.9-0.mr700
- dropped Requires: perl - rkhunter works without it 
- dropped the bash alignpatch (check the source or contact me)
- various file mode fixes (.../tmp/, *.db)
- optimized the %%files section - any new files in the
  current dirs will be fine - just %%{__install} them.

* Mon Apr 26 2004 Michael Boelen - 1.0.8-0
- Fixed missing md5blacklist.dat

* Mon Apr 19 2004 Doncho N. Gunchev - 1.0.6-1.mr700
- added missing /usr/local/rkhunter/db/md5blacklist.dat
- patched to align results in --cronjob, I think rpm based
  distros have symlink /bin/sh -> /bin/bash
- added --with/--without alignpatch for conditional builds
  (in case previous patch breaks something)

* Sat Apr 03 2004 Michael Boelen / Joe Klemmer - 1.0.6-0
- Update to 1.0.6

* Mon Mar 29 2004 Doncho N. Gunchev - 1.0.0-0
- initial .spec file
