# Copyright (c) 2008, 2009, 2010 David Sugar, Tycho Softworks.
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

%global _hardened_build 1

Name:          sipwitch
Summary:       A secure peer-to-peer VoIP server for the SIP protocol
Version:       1.9.15
Release:       18%{?dist}

License:       GPLv3+
URL:           http://www.gnu.org/software/sipwitch
Source:        https://ftp.gnu.org/gnu/sipwitch/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ucommon-devel >= 6.6.0
BuildRequires: libeXosip2-devel >= 3.0.0
BuildRequires: avahi-devel
BuildRequires: gnutls-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires:      %{name}-runtime%{?_isa} = %{version}-%{release}


%description
GNU SIP Witch is a secure peer-to-peer VoIP server.  Calls can be made even
behind NAT firewalls, and without needing a service provider.  SIP Witch can
be used on the desktop to create bottom-up secure calling networks as a
free software alternative to Skype.  SIP Witch can also be used as a stand-
alone SIP-based office telephone server, or to create secure VoIP networks
for an existing IP-PBX such as Asterisk, FreeSWITCH, or Yate.


%package runtime
Summary: Runtime library support for sipwitch

%description runtime
Runtime library required for sipwitch development and for using the server.
This is available as a separate package so that one building sipwitch plugins
with the required devel package does not also require installing a server
image.


%package devel
Summary: Headers for building sipwitch plugins
Requires: ucommon-devel%{?_isa} >= 6.0.0
Requires: %{name}-runtime%{?_isa} = %{version}-%{release}

%description devel
Header files for building plugins that interface with sipwitch. This might be
used for externally creating sipwitch modules, though normally modules are
found or added to the core distribution directly.  This may also be for
developing external application services which need to communicate with a
running sipwitch daemon instance.


%package cgi
Summary: cgi web interface to control sipwitch server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cgi
This package offers a means to perform remote management of a sipwitch
server using the cgi interface of an installed web server.  The primary
service this offers is xmlrpc access to sipwitch shared memory and
control interfaces in a manner analgolous to the sipwitch command utility.


%package plugin-zeroconf
Summary: Zeroconf plugin for sipwitch
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugin-zeroconf
This plugin activates zeroconf network services for sipwitch and publishes
sipwitch as a sip server.


%package plugin-scripting
Summary: Scripting plugin for sipwitch
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugin-scripting
This plugin enables shell scripting in connection with specific sipwitch
events.


%package plugin-forward
Summary: Forward registration and routing plugin
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugin-forward
This plugin enables forwarding of registration requests and destination routes
for unknown numbers so that one can create a "secure" peer to peer media
domain managed by sipwitch and still access an "insecure" b2bua based ip-pbx.


%package plugin-subscriber
Summary: Subscriber gateway plugin for sipwitch
Requires: %{name}%{?_isa} = %{version}-%{release}

%description plugin-subscriber
This module is meant to eventually offer generic support for premise
routers when used by providers to offer sip/voip service to a subscriber.
It offers rtp proxying and routing based on the assumption that all calls
will be handed off to an external voip provider and automatic rtp
proxy bridging between a subscribers local subnet and an isp.  In theory
this would be deployed in an isp supplied premise router to enable a
local user to subscribe a series of local softphone/sip devices with a
remote voip service provider.


%prep
%setup -q

%build
%cmake \
      -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
      -DCMAKE_INSTALL_CGIBINDIR=/var/www/cgi-bin \
      -DSYSTEM_CONFIG:BOOL=TRUE
%cmake_build


%install
%cmake_install


%post
%systemd_post sipwitch.service

%preun
%systemd_preun sipwitch.service

%postun
%systemd_postun_with_restart sipwitch.service

%ldconfig_scriptlets runtime


%files
%license COPYING
%doc README NEWS FEATURES SUPPORT TODO NOTES AUTHORS MODULES ChangeLog
%{_mandir}/man1/sipcontrol.1*
%{_mandir}/man1/sippasswd.1*
%{_mandir}/man1/sipquery.1*
%{_mandir}/man8/sipw.8*
%{_sbindir}/sipw
%{_bindir}/sipcontrol
%{_bindir}/sipquery
%attr(04755,root,root) %{_bindir}/sippasswd
%dir %{_libdir}/sipwitch
%config(noreplace) %{_sysconfdir}/logrotate.d/sipwitch
%attr(0644,root,root) %{_unitdir}/sipwitch.service
%attr(0755,root,root) %{_sysconfdir}/cron.hourly/sipwitch
%attr(0775,root,root) %dir %{_sysconfdir}/sipwitch.d
%attr(0664,root,root) %config(noreplace) %{_sysconfdir}/sipwitch.conf
%attr(0664,root,root) %config(noreplace) %{_sysconfdir}/default/sipwitch
%attr(0664,root,root) %config(noreplace) %{_sysconfdir}/sipwitch.d/*.xml*

%files devel
%{_libdir}/*.so
%{_includedir}/sipwitch/
%{_libdir}/pkgconfig/*.pc

%files cgi
%{_mandir}/man8/sipwitch.cgi.8*
/var/www/cgi-bin/sipwitch.cgi

%files runtime
%{_libdir}/*.so.*

%files plugin-zeroconf
%{_libdir}/sipwitch/zeroconf.so

%files plugin-forward
%{_libdir}/sipwitch/forward.so

%files plugin-scripting
%{_libdir}/sipwitch/scripting.so

%files plugin-subscriber
%{_libdir}/sipwitch/subscriber.so


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.15-15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 1.9.15-8
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 23 2017 David Sugar <tychosoft@gmail.com> - 1.9.15-4
- Updated to new source repository

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Sandro Mani <manisandro@gmail.com> - 1.9.15-1
- Update to 1.9.15

* Wed Oct 14 2015 Sandro Mani <manisandro@gmail.com> - 1.9.14-1
- Update to 1.9.14

* Mon Oct 05 2015 Sandro Mani <manisandro@gmail.com> - 1.9.12-1
- Update to 1.9.12

* Mon Oct 05 2015 Sandro Mani <manisandro@gmail.com> - 1.9.11-1
- Update to 1.9.11

* Wed Sep 09 2015 Sandro Mani <manisandro@gmail.com> - 1.9.10-1
- Update to 1.9.10

* Wed Aug 05 2015 Sandro Mani <manisandro@gmail.com> - 1.9.9-1
- Update to 1.9.9

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.9.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 David Sugar <dyfet@gnutelephony.org> - 1.9.1-3
- Reverted per Peter Robinson to re-enable aarch64

* Sat May 03 2014 David Sugar <dyfet@gnutelephony.org> - 1.9.1-1
- Using cmake for package build
- Added setgroups to squash permission bleed
- Cleaned up systemd unit; removed obsolete syslog.target
- New upstream with complete cmake package build support
- Removed obsolete config scripts upstream

* Mon Mar 10 2014 David Sugar <dyfet@gnutelephony.org> - 1.9.0-1
- Now operates as a systemd notify daemon service

* Sat Jan 25 2014 David Sugar <dyfet@gnutelephony.org> - 1.8.7-1
- fixed systemd multi-arch pathing issue
- improved systemd unit based on Michael Scherer <misc@zarb.org>

* Fri Oct 11 2013 David Sugar <dyfet@gnutelephony.org> - 1.8.6-1
- Upstream fixes for eXosip2 api support
- full multi-protocol context support with exosip2 4.0 and later

* Sun Sep 08 2013 David Sugar <dyfet@gnutelephony.org> - 1.8.0-1
- Initial multi-protocol context support, for registration only so far

* Mon Aug 12 2013 David Sugar <dyfet@gnutelephony.org> - 1.6.1-1
- migrated to systemd support (finally!)
- removed sipwitch-gui subpackage; now separated into switchview pkg.
- latest upstream 1.6.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 David Sugar <dyfet@gnutelephony.org> - 1.4.0-3
- Added PIE hardened flags per #965484

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 David Sugar <dyfet@gnutelephony.org> - 1.4.0-1
- Updated for new version 6 ucommon api

* Mon Sep 24 2012 David Sugar <dyfet@gnutelephony.org> - 1.3.2-1
- public access hotspot mode support added

* Tue Aug 07 2012 David Sugar <dyfet@gnutelephony.org> 1.3.1-1
- future proofing with support for building with 4.x exosip2 releases
- autoconfig event api for switchview client

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 David Sugar <dyfet@gnutelephony.org> - 1.2.5-1
- fix for group permissions and overlinking
- new interface options through config for nat

* Wed Feb 29 2012 David Sugar <dyfet@gnutelephony.org> - 1.2.3-1
- new policy command
- bug fix for xml parsing
- new user config options for testing
- improved management

* Sun Jan 15 2012 David Sugar <dyfet@gnutelephony.org> - 1.2.1-1
- new upstream release
- essential fix for cpu loading in subscriber plugin
- new usercache api functionality

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-1
- sipwitch-1.1.4

* Sun Nov 20 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-1
- sipwitch-1.1.3

* Wed Oct 12 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.2-1
- sipwitch-1.1.2
- renaming and reorg of sipwitch cgi binary

* Fri Sep  2 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.1-1
- sipwitch-1.1.1
- add BR: qt4-devel
- add -gui subpkg

* Wed Jun 29 2011 David Sugar <dyfet@gnutelephony.org> - 1.0.3-0
- fixed init script issue, per bug #712546
- new internal redirection api simplifies plugin linking
- extended header documentation

* Sun May 22 2011 David Sugar <dyfet@gnutelephony.org> - 1.0.1-0
- 1.0 baseline release
- updated for ucommon 5.0 api
- fixes for plugin paths and reporting load-time plugin errors

* Sun Mar 20 2011 David Sugar <dyfet@gnutelephony.org> - 0.10.3-0
- consolidated and reorganized utilities

* Thu Feb 24 2011 David Sugar <dyfet@gnutelephony.org> - 0.9.3-0
- fixed default domain as hostname

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 David Sugar <dyfet@gnutelephony.org> - 0.9.2-0
- updated for newer ucommon.
- configuration of tls support added.
- fix for registration with contact info.

* Thu Aug 12 2010 David Sugar <dyfet@gnutelephony.org> - 0.9.0-0
- requires ucommon 3.3.4 or later.

* Sun Jul 11 2010 David Sugar <dyfet@gnutelephony.org> - 0.8.4-2
- better tracking of invalid request uri's.
- interface state change notification support.
- better prack support.
- libnotify plugin temporarily disabled for rawhide gtk build issues.

* Sun Apr 11 2010 David Sugar <dyfet@gnutelephony.org> - 0.8.0-0
- support for new ucommon abi.
- libnotify plugin added.

* Sun Mar 21 2010 David Sugar <dyfet@gnutelephony.org> - 0.7.5-0
- fixed init script for systems without init lock directories.
- push PLUGINS=auto to sysconfig defaults.

* Sun Mar 14 2010 David Sugar <dyfet@gnutelephony.org> - 0.7.4-0
- fixed sippasswd to send digest rather than realm to running server.
- separated packaging and install of cgi webservice.
- new runtime server debug and monitoring operations.

* Fri Feb 12 2010 David Sugar <dyfet@gnutelephony.org> - 0.7.1-0
- Moved lab.xml to lab.xml-example so not part of default config.
- Removed config conflict when started in pure user mode.

* Sun Feb 07 2010 David Sugar <dyfet@gnutelephony.org> - 0.7.0-0
- NAT media functionality and internodal remote.
- merger of domain and realm server definitions.
- clearer source aliasing of remote calls between network domains.

* Sat Jan 23 2010 David Sugar <dyfet@gnutelephony.org> - 0.6.2-0
- use uuid for unset authentication realms.
- saner default configuration file.

* Wed Jan 20 2010 David Sugar <dyfet@gnutelephony.org> - 0.6.1-0
- user account integration with sip accounts.
- exec hook for packaging systems that done use fakeroot.

* Sun Jan 17 2010 David Sugar <dyfet@gnutelephony.org> - 0.5.13-0
- sip realm fully externalized and new siprealm utility added.

* Wed Dec 09 2009 David Sugar <dyfet@gnutelephony.org> - 0.5.12-0
- redefined internal user & service permissions and profiles.
- fixed anonymous inbound.
- added missing manpages.

* Thu Nov 19 2009 David Sugar <dyfet@gnutelephony.org> - 0.5.9-0
- removed snmp/mib from this package
- removed unused swig support and complex packaging it required.

* Fri Aug 14 2009 David Sugar <duyfet@gnutelephony.org> - 0.5.7-1
- memory corruption issue in allocating subnet access objects fixed

* Mon Jul 13 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.5.6-1
- rebuild for new PHP 5.3.0 ABI (20090626)
- add PHP ABI check
- add php configuration file (/etc/php.d/sipwitch.ini)

* Sat Jul 04 2009 - David Sugar <dyfet@gnutelephony.org> - 0.5.6-0
- split runtime from server to build plugins without requiring server.
- removed separate rtp proxy, functionality will be integrated into server.

* Wed Jun 10 2009 - David Sugar <dyfet@gnutelephony.org> - 0.5.5-0
- upstream fixed in rel 0.5.5, no patches now needed for rpm distros.

* Sun May 10 2009 - David Sugar <dyfet@gnutelephony.org> - 0.5.4-3
- new generic init script layout as a patch until next upstream release.

* Fri May 08 2009 - David Sugar <dyfet@gnutelephony.org> - 0.5.4-2
- some fixups until upstream is changed, and new init scriptlets.

* Wed May 06 2009 - David Sugar <dyfet@gnutelephony.org> - 0.5.4-1
- temporary patch file added until upstream catches up, other cleanup.

* Sat May 02 2009 - David Sugar <dyfet@gnutelephony.org> - 0.5.4-0
- spec file updated for redhat/fedora submission.

* Fri Jul 25 2008 - David Sugar <dyfet@gnutelephony.org> - 0.2.0-0
- spec file updated for plugins and new library naming.

* Mon Jul 21 2008 - David Sugar <dyfet@gnutelephony.org> - 0.1.0-0
- initial spec file distribution.

