%global _hardened_build 1
Summary: Fast and lean authoritative DNS Name Server
Name: nsd
Version: 4.8.0
Release: 1%{?dist}
License: BSD
Url: http://www.nlnetlabs.nl/nsd/
Source0: http://www.nlnetlabs.nl/downloads/%{name}/%{name}-%{version}%{?prever}.tar.gz
Source1: nsd.conf
Source2: nsd.service
Source3: tmpfiles-nsd.conf
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: openssl-devel
BuildRequires: libevent-devel
Requires(pre): shadow-utils
BuildRequires: systemd-units
BuildRequires: systemd-devel
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
NSD is a complete implementation of an authoritative DNS name server.
For further information about what NSD is and what NSD is not please
consult the REQUIREMENTS document which is a part of this distribution.

%prep
%setup -q -n %{name}-%{version}%{?prever}

%build
CFLAGS="%{optflags} -fPIE -pie"
LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS LDFLAGS
%configure \
    --enable-bind8-stats \
    --enable-zone-stats \
    --enable-checking \
    --enable-nsec3 \
    --with-pidfile="" \
    --with-zonelistfile=%{_sharedstatedir}/nsd/zone.list \
    --with-ssl \
    --with-user=nsd \
    --with-xfrdfile=%{_sharedstatedir}/nsd/ixfr.state \
    --with-dbfile="" \
    --enable-ratelimit \
    --enable-pie \
    --enable-relro-now \
    --enable-recvmmsg \
    --enable-packed \
    --enable-memclean \
    --enable-systemd

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/nsd.conf
mkdir -p %{buildroot}%{_rundir}/nsd
mkdir -p %{buildroot}%{_sharedstatedir}/nsd

# Install ghost files
for name in control server; do
    for extension in key pem; do
        touch %{buildroot}%{_sysconfdir}/nsd/nsd_${name}.${extension}
    done
done

# Take care of the configuration
mkdir -p %{buildroot}%{_sysconfdir}/nsd/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/nsd/server.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nsd/nsd.conf
rm %{buildroot}%{_sysconfdir}/nsd/nsd.conf.sample

%files
%license LICENSE
%doc doc/*
%doc contrib/nsd.zones2nsd.conf
%dir %{_sysconfdir}/nsd
%config(noreplace) %{_sysconfdir}/nsd/nsd.conf
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_server.key
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_server.pem
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_control.key
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_control.pem
%dir %{_sysconfdir}/nsd/conf.d
%dir %{_sysconfdir}/nsd/server.d
%attr(0644,root,root) %{_unitdir}/nsd.service
%attr(0644,root,root) %{_tmpfilesdir}/nsd.conf
%attr(0755,nsd,nsd) %dir %{_rundir}/nsd
%attr(0750,nsd,nsd) %dir %{_sharedstatedir}/nsd
%{_sbindir}/*
%{_mandir}/*/*

%pre
getent group nsd >/dev/null || groupadd -r nsd
getent passwd nsd >/dev/null || \
useradd -r -g nsd -d /etc/nsd -s /sbin/nologin \
    -c "nsd daemon account" nsd
exit 0

%post
%systemd_post nsd.service

%preun
%systemd_preun nsd.service

%postun
%systemd_postun_with_restart nsd.service

%changelog
* Mon Dec 25 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.8.0-1
- Update to 4.8.0
- Resolves: rhbz#2252122

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 17 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0
- Resolves: rhbz#2211783

* Sun Feb 19 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1

* Wed Feb 01 2023 Florian Weimer <fweimer@redhat.com> - 4.3.9-5
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Paul Wouters <paul.wouters@aiven.io> - 4.3.9-1
- Resolves rhbz#2028586 Update to nsd 4.3.9

* Fri Oct 15 2021 Paul Wouters <paul.wouters@aiven.io> - 4.3.8-1
- Resolves: rhbz#2010311 nsd-4.3.8 is available
- Do not require nsd.keygen service anymore

* Thu Oct 07 2021 Paul Wouters <paul.wouters@aiven.io> - 4.3.7-4
- Resolves: rhbz#2011757 nsd spec file scriptlets still used obsoleted conditional on systemd, causing sysvinit style exection

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.3.7-3
- Rebuilt with OpenSSL 3.0.0

* Wed Aug 11 2021 Paul Wouters <paul.wouters@aiven.io> - 4.3.7-2
- Resolves: rhbz#1992399 nsd: recently added TLS support should support system wide crypto policies

* Tue Aug 10 2021 Paul Wouters <paul.wouters@aiven.io> - 4.3.7-1
- Resolves: rhbz#1982585 nsd-4.3.7 is available
- Clean out legacy sysvinit / trigger support
- Update nsd.conf with new TLS (XFR over TLS) options

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Paul Wouters <paul.wouters@aiven.io> - 4.3.6-1
- Resolves: rhbz#1944233 nsd-4.3.6 is available
- Resolves: rhbz#1943122 nsd: FTBFS with upcoming autoconf-2.71

* Thu Mar 25 2021 Paul Wouters <pwouters@redhat.com> - 4.3.5-1
- Resolves: rhbz#1884189 nsd-4.3.5 is available
- Change default to not use TLS/keygen, but the unix domain socket

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.3.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:38:53 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.3.2-2
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Paul Wouters <pwouters@redhat.com> - 4.3.2-1
- Resolves: rhbz#1854415 nsd-4.3.2 is available

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.3.1-1
- Update to current version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Paul Wouters <pwouters@redhat.com> - 4.2.4-1
- Resolves: rhbz#1772468 nsd-4.2.4 is available
- Updated nsd.conf page for new upstream option(s)
- Properly mark license file.

* Fri Aug 30 2019 Paul Wouters <pwouters@redhat.com> - 4.2.2-1
- Resolves: rhbz#1609774 nsd-4.2.2 is available
- Resolves: rhbz#1727689 CVE-2019-13207 nsd: stack-based overflow
- Update rundir to /run/
- Updated nsd.conf for new features
- Added --enable-recvmmsg --enable-packed --enable-memclean --enable-zone-stats

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Paul Wouters <pwouters@redhat.com> - 4.1.24-2
- Resolves: rhbz#1645743 Fix syntax error at control-interface in nsd.conf

* Mon Aug 13 2018 Paul Wouters <pwouters@redhat.com> - 4.1.24-1
- Resolves: rhbz#1609774 Updated to 4.1.24)
- Enable systemd for readiness signalling
- Enable local unix domain socket /run/nsd/nsd.ctl for nsd-control
- Resolves: rhbz#1468477 nsd-keygen unit does not generate keys if it's already started

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Paul Wouters <pwouters@redhat.com> - 4.1.22-1
- Resolves rhbz#1575608 nsd 4.1.22 is available
- Enable round-robin, minimal-responses and refuse-any in nsd.conf

* Wed Feb 21 2018 Paul Wouters <pwouters@redhat.com> - 4.1.20-1
- Updated to 4.1.20 (fixup memory leaks)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Paul Wouters <pwouters@redhat.com> - 4.1.19-1
- Updated to 4.1.19 (fixup of 4.1.18 for IPv6 issues)

* Fri Dec 01 2017 Paul Wouters <pwouters@redhat.com> - 4.1.18-1
- Updated to 4.1.18

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Paul Wouters <pwouters@redhat.com> - 4.1.16-1
- Updated to 4.1.16 (minimum response option)
- Disable on-disk database per default (use ram only)
- Minor updates to nsd.conf

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Paul Wouters <pwouters@redhat.com> - 4.1.14-2
- Ensure nsd only starts after network is fully up

* Thu Dec 08 2016 Paul Wouters <pwouters@redhat.com> - 4.1.14-1
- Updated to 4.1.14 (various XFR fixes)

* Wed Sep 28 2016 Paul Wouters <pwouters@redhat.com> - 4.1.13-1
- Updated to 4.1.13 (CVE-2016-6173, OPENPGPKEY support)
- Resolves: rhbz#1353577

* Fri Sep 02 2016 Paul Wouters <pwouters@redhat.com> - 4.1.12-1
- Updated to 4.1.12 for assertion failure in malformed edns query

* Wed Aug 10 2016 Paul Wouters <pwouters@redhat.com> - 4.1.11-1
- Updated to 4.1.11 for the unlimited AXFR vulnerability
- Updated nsd.conf with new options

* Sun Jul 03 2016 Paul Wouters <pwouters@redhat.com> - 4.1.10-2
- Do not use db files anymore, use --with-zonelistfile
- Documentation utf fixes are upstreamed
- Empty sysconfig file removed (still supported on epel6)
- Remove timer/cron entry - now done by nsd itself
- Update nsd.conf file

* Wed Jun 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.1.10-1
- Update to 4.1.10

* Tue Mar 15 2016 Paul Wouters <pwouters@redhat.com> - 4.1.9-1
- Update to 4.1.9 which fixes restart failures on nsd.db change

* Sat Mar 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.1.8-1
- Update to 4.1.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Paul Wouters <pwouters@redhat.com> - 4.1.7-4
- Remove cronjob and enable zonefiles-write: in nsd.conf instead
- Do not manually run nsd-control notify - daemon already does when needed
- Do not remove xfrd.state state information

* Mon Dec 28 2015 Paul Wouters <pwouters@redhat.com> - 4.1.7-3
- Removed Mass rebuild changelogs causing chronological order error
- Bump EVR required due to epel7 build

* Sun Dec 27 2015 Tuomo Soini <tis@foobar.fi> - 4.1.7-2
- Enable PrivateTmp for nsd.service
- Rename /etc/nsd/local.d/ to /etc/nsd/server.d/
- Add /etc/nsd/local.d for local server config
- Add ghost entries for nsd_control and nsd_server key and certificate
- Fix sysv init script by removing nsd3 specific NSDC_PROG options
- Use signals whenever possible instead of using nsd-control
- Use cron script on sysvinit systems only
- Add nsd-write.service and nsd-write.timer (not enabled by default)
- Remove old options from /etc/sysconfig/nsd
- Install /etc/sysconfig/nsd on sysvinit systems only
- Remove all example files from /etc/nsd/conf.d/ - don't belong to package
- Add nsd-keygen.service to generate nsd-control keys
- Add creation of nsd_control.key to nsd.init
- nsd.service depends on nsd-keygen.service
- Change nsd.service to use KillMode=mixed
- Add triggerin for older nsd package to chown /var/lib/nsd/*
- Update nsd.conf from upstream and add nsd-control section

* Sun Dec 20 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.1.7-1
- Update to last upstream
- Multiple tests and fixes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Paul Wouters <pwouters@redhat.com> - 4.1.1-1
- Updated to 4.1.1
- Updated cron job for new nsd-control
- Updated nsd.conf
- Updated nsd init script for use of nsd-control
- Renamed --max_interfaces to --max-ips
- Added BuildRequires for libevent-devel
- Fix buglet in nsd user creation's exit command
- Create nsd4 remote-control pem files for nsd-control
- chown /var/lib/nsd/nsd.db to the nsd user required for nsd4
- Add logrotate support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Paul Wouters <pwouters@redhat.com> - 3.2.18-1
- Updated to 3.2.18 - improved TXT parsing, new NSID option
- Fix nsd.service daemonize option (rhbz#1089505)

* Sun Mar 30 2014 Paul Wouters <pwouters@redhat.com> - 3.2.17-1
- Updated to 3.2.17
- Added --with-max-ips=1024
- Removed merged in patch

* Thu Apr 18 2013 Paul Wouters <pwouters@redhat.com> - 3.2.15-4
- Enable hardened build
- rhbz#850231 - Introduce new systemd-rpm macros in nsd spec file
- Added -D option to nsd to allow us to use systemd service Type=simple
- Switch from Fork to Simple systemd service
- Use /run and not /var/run for pid
- The cronjon now uses systemctl reload, which also triggers notifies
  (should speed up notifications to secondaries)

* Mon Mar 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.15-3
- Bump so rawhide/F19 has bigger NVR that older releases

* Mon Feb 04 2013 Paul Wouters <pwouters@redhat.com> - 3.2.15-1
- Updates to 3.2.15 which contains rate limit code
  (fixes rhbz#842036 - nsd fails to start in fips mode)

* Fri Nov 23 2012 Paul Wouters <pwouters@redhat.com> - 3.2.14-2
- Updated to 3.2.14 with minor bugfixes and TCP writev support
- Only run nsdc rebuild hourly cronjob when nsd service is running

* Fri Jul 27 2012 Paul Wouters <pwouters@redhat.com> - 3.2.13-1
- Updated to 3.2.13, addresses VU#517036 CVE-2012-2979
  (note Fedora/EPEL packages are not vulnerable to this)

* Mon Jul 23 2012 Paul Wouters <pwouters@redhat.com> - 3.2.12-2
- Add /var/run/nsd via tmpfiles (rhbz#842021)

* Thu Jul 19 2012 Paul Wouters <pwouters@redhat.com> - 3.2.12-1
- Upgraded to 3.2.12 which fixes CVE-2012-2978 (rhbz#841268)

* Mon Jul 16 2012 Paul Wouters <pwouters@redhat.com> - 3.2.11-1
- Updated to 3.2.11
- Remove execute perm from unitdir file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Paul Wouters <paul@xelerance.com> - 3.2.9-2
- Change spec and initscript to chown /var/run/nsd to nsd user to work around
  the "nsdc restart" problem where it cannot update its own pid file

* Sun Nov 27 2011 Paul Wouters <paul@xelerance.com> - 3.2.9-1
- Updated to 3.2.9

* Mon Sep 12 2011 Tom Callaway <spot@fedoraproject.org> - 3.2.8-7
- fix tmpfiles.d creation of /var/run/nsd to be owned by root

* Mon Sep 12 2011 Tom Callaway <spot@fedoraproject.org> - 3.2.8-6
- convert to systemd, tmpfiles.d

* Fri Jun  3 2011 Paul Wouters <paul@xelerance.com> - 3.2.8-5
- fix /var/run/nsd to be owned by root, not nsd

* Fri Jun  3 2011 Tuomo Soini <tis@foobar.fi> - 3.2.8-4
- fix init status to work as expected (bz#525107)
- fix nsd.conf and nsd.conf.5 to have correct logfile
- fix nsd.init syntax error by piddir change
- fix initscript to create /var/run/nsd if missing (bz#710376)

* Sun Mar 27 2011 Paul Wouters <paul@xelerance.com> - 3.2.8-1
- updated to 3.2.8

* Wed Mar 09 2011 Paul Wouters <paul@xelerance.com> - 3.2.7-5
- Fix misnamed variable NSD_AUTORELOAD which should be NSD_AUTOREBUILD
- Fix for init script properly returning OK/Failed (bz#535107) by Noa Resare
- Add ghost directive to /var/run/nsd (bz#656642)
- Bump release for EVR

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Paul Wouters <paul@xelerance.com> - 3.2.7-1
- Updated to 3.2.7

* Mon Aug 02 2010 Paul Wouters <paul@xelerance.com> - 3.2.6-1
- Updated to 3.2.6
- Removed obsolete --enable-nsid

* Wed Jan 06 2010 Paul Wouters <paul@xelerance.com> - 3.2.4-1
- Updated to nsd 3.2.4

* Tue Jan 05 2010 Paul Wouters <paul@xelerance.com> - 3.2.3-4
- Incorporated Ville Mattila's fixes  to nsd.cron
- Support for NSD_AUTOREBUILD in /etc/sysconfig/nsd [Ville]

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.2.3-3
- rebuilt with new openssl

* Thu Aug 20 2009 Ville Mattila <vmattila@csc.fi> - 3.2.3-2
- The 'nsdc patch' and 'nsdc rebuild' commands wrote a %%1 file by mistake

* Mon Aug 17 2009 Paul Wouters <paul@xelerance.com> - 3.2.3-1
-Updated to version 3.2.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 06 2009 Paul Wouters <paul@xelerance.com> - 3.2.2-3
- Fixed /dev/nul which cause a file \%%1 to be written by cron
- Bump for EVR.

* Mon May 18 2009 Paul Wouters <paul@xelerance.com> - 3.2.2-1
- Upgraded to 3.2.2 security release
  http://www.nlnetlabs.nl/publications/NSD_vulnerability_announcement.html

* Thu Apr 09 2009 Ville Mattila <vmattila@csc.fi> - 3.2.1-6
- Make various file paths used by the nsd.init script configurable
  from /etc/sysconfig/nsd.
- Add template /etc/sysconfig/nsd.

* Sun Mar 08 2009 Paul Wouters <paul@xelerance.com> - 3.2.1-5
- nsd used the 'named' subsystem in one call in the init script

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Paul Wouters <paul@xelerance.com> - 3.2.1-3
- Fix init script 'unary operator' error.

* Mon Jan 26 2009 Paul Wouters <paul@xelerance.com> - 3.2.1-1
- Updated to new version 3.2.1

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 3.2.0-4
- rebuild with new openssl

* Mon Nov 24 2008 Paul Wouters <paul@xelerance.com> - 3.2.0-3
- Updates summary as per Richard Hughes guidelines

* Mon Nov 10 2008 Paul Wouters <paul@xelerance.com> - 3.2.0-2
- Bump version after pre-release version correction.

* Mon Nov 10 2008 Paul Wouters <paul@xelerance.com> - 3.2.0-1
- 3.2.0-1

* Thu Oct  9 2008 Paul Wouters <paul@xelerance.com> - 3.1.1-1
- updated to 3.1.1

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1.0-2
- fix license tag
- fix static user creation

* Mon Jun 30 2008 Paul Wouters <paul@xelerance.com> - 3.1.0-1
- Updated to 3.1.0

* Tue May  6 2008 Paul Wouters <paul@xelerance.com> - 3.0.8-2
- Fix /dev/null redirection [Venkatesh Krishnamurthi]

* Tue May  6 2008 Paul Wouters <paul@xelerance.com> - 3.0.8-1
- Updated to 3.0.8

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.7-3
- Autorebuild for GCC 4.3

* Wed Dec  5 2007 Paul Wouters <paul@xelerance.com> - 3.0.7-2
- Rebuild for new libcrypto

* Tue Nov 13 2007 Paul Wouters <paul@xelerance.com> - 3.0.7-1
- Updated to new version
- fix RELNOTES/README to be utf8
- Fix path to nsd.db in cron job.

* Thu Nov  8 2007 Paul Wouters <paul@xelerance.com> - 3.0.6-7
- Modified cron to only rebuild/reload when zone updates
  have been received

* Wed Nov  7 2007 Paul Wouters <paul@xelerance.com> - 3.0.6-6
- Added hourly cron job to do various maintenance tasks
- Added nsd rebuild to create the proper nsd.db file on startup
- Added nsd patch on shutdown to ensure zonefiles are up to date

* Tue Oct  2 2007 Paul Wouters <paul@xelerance.com> - 3.0.6-5
- nsdc update and nsdc notify are no longer needed in initscript.

* Mon Sep 24 2007 Jesse Keating <jkeating@redhat.com> - 3.0.6-4
- Bump release for upgrade path.

* Fri Sep 14 2007 Paul Wouters <paul@xelerance.com> 3.0.6-3
- Do not include examples from nsd.conf.sample that causes
  bogus network traffic.

* Fri Sep 14 2007 Paul Wouters <paul@xelerance.com> 3.0.6-2
- Change locations of ixfr.db and xfrd.state to /var/lib/nsd
- Enable NSEC3
- Delay running nsdc update until after nsd has started
- Delete xfrd.state on nsd stop
- Run nsdc notify in the background, since it can take
  a very long time when remote servers are unavailable.

* Tue Sep 11 2007 Paul Wouters <paul@xelerance.com> 3.0.6-1
- Upgraded to 3.0.6
- Do not include bind2nsd, since it didn't compile for me

* Fri Jul 13 2007 Paul Wouters <paul@xelerance.com> 3.0.5-2
- Fix init script, bug #245546

* Fri Mar 23 2007 Paul Wouters <paul@xelerance.com> 3.0.5-1
- Upgraded to 3.0.5

* Thu Dec  7 2006 Paul Wouters <paul@xelerance.com> 3.0.3-1
- Upgraded to 3.0.3

* Mon Nov 27 2006 Paul Wouters <paul@xelerance.com> 3.0.2-1
- Upgraded to 3.0.2.
- Use new configuration file nsd.conf. Still needs migration script.
  patch from Farkas Levente <lfarkas@bppiac.hu>

* Mon Oct 16 2006  Paul Wouters <paul@xelerance.com> 2.3.6-2
- Bump version for upgrade path

* Thu Oct 12 2006  Paul Wouters <paul@xelerance.com> 2.3.6-1
- Upgraded to 2.3.6
- Removed obsolete workaround in nsd.init
- Fixed spec file so daemon gets properly restarted on upgrade

* Mon Sep 11 2006 Paul Wouters <paul@xelerance.com> 2.3.5-4
- Rebuild requested for PT_GNU_HASH support from gcc
- Removed dbaccess.c from doc section

* Mon Jun 26 2006 Paul Wouters <paul@xelerance.com> - 2.3.5-3
- Bump version for FC-x upgrade path

* Mon Jun 26 2006 Paul Wouters <paul@xelerance.com> - 2.3.5-1
- Upgraded to nsd-2.3.5

* Sun May  7 2006 Paul Wouters <paul@xelerance.com> - 2.3.4-3
- Upgraded to nsd-2.3.4.
- Removed manual install targets because DESTDIR is now supported
- Re-enabled --checking, checking patch no longer needed and removed.
- Work around in nsd.init for nsd failing to start when there is no ipv6

* Thu Dec 15 2005 Paul Wouters <paul@xelerance.com> - 2.3.3-7
- chkconfig and attribute  changes as proposed by Dmitry Butskoy

* Thu Dec 15 2005 Paul Wouters <paul@xelerance.com> - 2.3.3-6
- Moved pid file to /var/run/nsd/nsd.pid.
- Use _localstatedir instead of "/var"

* Tue Dec 13 2005 Paul Wouters <paul@xelerance.com> - 2.3.3-5
- Added BuildRequires for openssl-devel, removed Requires for openssl.

* Mon Dec 12 2005 Paul Wouters <paul@xelerance.com> - 2.3.3-4
- upgraded to nsd-2.3.3

* Wed Dec  7 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 2.3.2-2
- minor cleanups

* Mon Dec  5 2005 Paul Wouters <paul@xelerance.com> - 2.3.2-1
- Upgraded to 2.3.2. Changed post scripts to comply to Fedora
  Extras policies (eg do not start daemon on fresh install)

* Tue Oct  4 2005 Paul Wouters <paul@xelerance.com> - 2.3.1-1
- Initial version
