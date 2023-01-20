%global _hardened_build 1

#%%global snapshot 20150714

Summary: Tool for dynamic reconfiguration of validating resolver Unbound
Name: dnssec-trigger
Version: 0.17
Release: 10%{?snapshot:.%{snapshot}git}%{?dist}
License: BSD
Url: https://www.nlnetlabs.nl/projects/dnssec-trigger/

%if 0%{?snapshot:1}
# generated using './makedist.sh -s' in the cloned upstream trunk
Source0: %{name}-%{version}_%{snapshot}.tar.gz
%else
Source0: https://www.nlnetlabs.nl/downloads/dnssec-trigger/%{name}-%{version}.tar.gz
Source1: https://www.nlnetlabs.nl/downloads/dnssec-trigger/%{name}-%{version}.tar.gz.asc
Source2: https://keys.openpgp.org/vks/v1/by-fingerprint/EDFAA3F2CA4E6EB05681AF8E9F6F1C2D7E045F8D#/wouter.asc
%endif
Source3: dnssec-trigger.tmpfiles.d
Source4: dnssec-trigger-default.conf
Source5: dnssec-trigger-workstation.conf
Source6: ssh_config.conf

# Patches
Patch3: 0003-Move-the-NetworkManager-dispatcher-script-out-of-etc.patch
# https://github.com/NLnetLabs/dnssec-trigger/pull/7
Patch4: 0004-Add-options-edns0-and-trust-ad.patch
Patch5: dnssec-trigger-configure-c99.patch

# to obsolete the version in which the panel was in main package
Obsoletes: %{name} < 0.12-22
Suggests: %{name}-panel
# Require a version of NetworkManager that doesn't forget to issue dhcp-change
# https://bugzilla.redhat.com/show_bug.cgi?id=1112248
%if 0%{?rhel} >= 9 || 0%{?fedora} >= 31
Requires: NetworkManager >= 1.20
%elif 0%{?rhel} >= 7
Requires: NetworkManager >= 0.9.9.1-13
%elif 0%{?fedora} >= 21
Requires: NetworkManager >= 0.9.9.95-1
%else
Requires: NetworkManager >= 0.9.9.0-40
%endif
Requires: ldns >= 1.6.10, NetworkManager-libnm, unbound
# needed by /usr/sbin/dnssec-trigger-control-setup
# otherwise it ends with error: /usr/sbin/dnssec-trigger-control-setup: line 180: openssl: command not found
Requires: openssl
# needed for /usr/bin/chattr
Requires: e2fsprogs
BuildRequires: openssl-devel, ldns-devel, python3-devel, gcc
BuildRequires: NetworkManager-libnm-devel
%if 0%{?fedora} && ! 0%{?snapshot:1}
BuildRequires: gnupg2
%endif

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# Provides Workstation specific configuration
# - No captive portal detection and no action available on Captive portal (No UI)
Provides: variant_config(Workstation)

%description
dnssec-trigger reconfigures the local Unbound DNS server. Unbound is a
resolver performing DNSSEC validation. dnssec-trigger is a set of daemon
and script. On every network configuration change dnssec-trigger performs
set of tests and configures Unbound based on the current NetworkManager
configuration, its own configuration and results of performed tests.


%package panel
Summary: Applet for interaction between the user and dnssec-trigger
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name} < 0.12-22
Requires: xdg-utils
BuildRequires: gtk2-devel, desktop-file-utils
BuildRequires: make

%description panel
This package provides the GTK panel for interaction between the user
and dnssec-trigger daemon. It is able to show the current state and
results of probing performed by dnssec-trigger daemon. Also in case
some user input is needed, the panel creates a dialog window.


%prep
%if 0%{?fedora} && ! 0%{?snapshot:1}
%gpgverify -d 0 -s 1 -k 2
%endif
%autosetup %{?snapshot:-n %{name}-%{version}_%{snapshot}} -p1

# don't use DNSSEC for forward zones for now
sed -i "s/validate_connection_provided_zones=yes/validate_connection_provided_zones=no/" dnssec.conf


%build
%configure  \
    --with-keydir=%{_sysconfdir}/dnssec-trigger \
    --with-hooks=networkmanager \
%if 0%{?rhel} < 9 && 0%{?fedora} < 31
    --with-networkmanager-dispatch=%{_sysconfdir}/NetworkManager/dispatcher.d \
%endif
    --with-python=%{__python3} \
    --with-pidfile=%{_rundir}/%{name}d.pid

%{__make} %{?_smp_mflags}


%install
rm -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

install -d 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/

mkdir -p %{buildroot}%{_libexecdir}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications dnssec-trigger-panel.desktop

# install the configuration for /var/run/dnssec-trigger into tmpfiles.d dir
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}.conf
# we must create the /var/run/dnssec-trigger directory
mkdir -p %{buildroot}%{_localstatedir}/run
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}

# supress the panel name everywhere including the gnome3 panel at the bottom
ln -s dnssec-trigger-panel %{buildroot}%{_bindir}/dnssec-trigger

# Make dnssec-trigger.8 manpage available under names of all dnssec-trigger-*
# executables
for all in dnssec-trigger-control dnssec-trigger-control-setup dnssec-triggerd; do
    ln -s %{_mandir}/man8/dnssec-trigger.8 %{buildroot}/%{_mandir}/man8/"$all".8
done
ln -s %{_mandir}/man8/dnssec-trigger.8 %{buildroot}/%{_mandir}/man8/dnssec-trigger.conf.8

install -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/ssh_config.d
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/ssh/ssh_config.d/10-%{name}.conf

%post
%systemd_post %{name}d.service

%preun
%systemd_preun %{name}d.service

%postun
%systemd_postun_with_restart %{name}d.service

%posttrans
# If we don't yet have a symlink or existing file for dnssec-trigger.conf,
# create it..
if [ ! -e %{_sysconfdir}/%{name}/dnssec-trigger.conf ]; then
    # Import /etc/os-release to get the variant definition
    . /etc/os-release || :

    case "$VARIANT_ID" in
        workstation)
            ln -sf %{name}-workstation.conf %{_sysconfdir}/%{name}/dnssec-trigger.conf || :
            ;;
        *)
            ln -sf %{name}-default.conf %{_sysconfdir}/%{name}/dnssec-trigger.conf || :
            ;;
        esac
fi



%files
%license LICENSE
%doc README
%{_bindir}/dnssec-trigger
%{_sbindir}/dnssec-trigger*
%{_libexecdir}/dnssec-trigger-script
%{_unitdir}/%{name}d.service
%{_unitdir}/%{name}d-keygen.service
%if 0%{?rhel} >= 9 || 0%{?fedora} >= 31
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/01-dnssec-trigger
%else
%attr(0755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/01-dnssec-trigger
%endif
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/dnssec.conf
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/%{name}/dnssec-trigger.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/dnssec-trigger-default.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/dnssec-trigger-workstation.conf
%attr(0755,root,root) %dir %{_sysconfdir}/ssh/ssh_config.d
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config.d/10-%{name}.conf
%dir %{_localstatedir}/run/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man8/dnssec-trigger*

%files panel
%{_bindir}/dnssec-trigger-panel
%attr(0755,root,root) %dir %{_datadir}/%{name}
%attr(0644,root,root) %{_datadir}/%{name}/*
%attr(0644,root,root) %{_datadir}/applications/dnssec-trigger-panel.desktop
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/xdg/autostart/dnssec-trigger-panel.desktop


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Florian Weimer <fweimer@redhat.com> - 0.17-9
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.17-6
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Adam Williamson <awilliam@redhat.com> - 0.17-2
- Rebuild for libldns soname bump

* Tue Oct 13 2020 Petr Menšík <pemensik@redhat.com> - 0.17-1
- Update to 0.17

* Mon Oct 12 2020 Petr Menšík <pemensik@redhat.com> - 0.15-14
- Add edns0 option to resolv.conf
- Add VerifyHostKeyDNS to ssh config

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Jeff Law <law@redhat.com> - 0.15-11
- Fix typo in last change

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.15-10
- Move the NetworkManager dispatcher script out of /etc

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.15-6
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Petr Menšík <pemensik@redhat.com> - 0.15-5
- Accept NXDOMAIN for NSEC probe (#1555355)

* Mon Feb 19 2018 Tomas Hozza <thozza@redhat.com> - 0.15-4
- Added explicit BuildRequires on gcc as required by packaging guidelines
- Added explicit Requires on e2fsprogs, so that /usr/bin/chattr is available
- Remove redundant removal of immutable bit in %%preun scriptlet (#1542400)

* Mon Feb 19 2018 Tomas Hozza <thozza@redhat.com> - 0.15-3
- use NetworkManager-libnm instead of NetworkManager-glib

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Tomas Hozza <thozza@redhat.com> - 0.15-1
- Update to stable 0.15 upstream release

* Fri Aug 18 2017 Petr Menšík <pemensik@redhat.com> - 0.13-6
- Skip always failing kr.com, update root IPs (#1482939)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 Tomas Hozza <thozza@redhat.com> - 0.13-3
- Rebuild against new ldns

* Wed Mar 01 2017 Tomas Hozza <thozza@redhat.com> - 0.13-2
- Include fix for runtime issues with OpenSSL 1.1.0 (#1427561)

* Fri Feb 17 2017 Tomas Hozza <thozza@redhat.com> - 0.13-1
- Update to stable 0.13 upstream release
- Dropped merged patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-0.6.20150714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13-0.5.20150714svn
- Rebuild for Python 3.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-0.4.20150714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 20 2015 Tomas Hozza <thozza@redhat.com> - 0.13-0.2.20150714svn
- Provide Workstation specific configuration

* Wed Jul 15 2015 Tomas Hozza <thozza@redhat.com> - 0.13-0.1.20150714svn
- split dnssec-trigger panel into separate subpackage (#1236363)
- SPEC file cleanup based on rpmlint and fedora-review issues
- implement some suggestions (#1236363)
- rebase to the latest svn trunk snapshot 0.13_20150714
- Script is not searching local user directories any more (#1213062)
- Script now doesn't restart NM if version is >= 1.0.3, but sends just signal
- Script now specifies the NMClient version for GI (#1242430)
- Script now sets negative-cache-ttl in unbound to 5 seconds (#1229596)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Tomas Hozza <thozza@redhat.com> - 0.12-20
- Fix issue when installing private address range zone without global forwarders (#1205864)
- Fix configuration of private address range zones (#1128310#c20)

* Fri Mar 13 2015 Tomas Hozza <thozza@redhat.com> - 0.12-19
- Fix typo in the dnssec-trigger-script (#1187371)
- Use Python3 by default

* Mon Jan 26 2015 Pavel Šimerda <psimerda@redhat.com> - 0.12-18
- Resolves: #1185796, #1130502, #1105685, #1128310 – update

* Tue Jan 20 2015 Pavel Šimerda <psimerda@redhat.com> - 0.12-17
- Resolves: #1183975 - systemd cgroup check fails

* Tue Jan 20 2015 Pavel Šimerda <psimerda@redhat.com> - 0.12-16
- Resolves: #1165126, #1125267, #1089766, #1112248, #824219 - update

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-14
- Resolves: #1125261 - dnssec-trigger-script: use fcntl.flock instead of
  lockfile

* Mon Aug 11 2014 Tomas Hozza <thozza@redhat.com> - 0.12-13
- One Fedora fallback server changed IP address (#1125440)

* Mon Jun 30 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-12
- Resolves: #1112248 - require a version of NetworkManager with #1113122 fixed

* Tue Jun 24 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-11
- Resolves: #1112248 - serialize the script instances

* Tue Jun 24 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-10
- Resolves: #1112248 - fix a typo

* Tue Jun 24 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-9
- Resolves: #1112248 - fix systemd race condition

* Mon Jun 23 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-8
- Resolves: #1112248 - don't block on systemctl restart NetworkManager

* Mon Jun 23 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-7
- Resolves: #1112248, #1111143 - update dnssec-trigger-script and dnssec-triggerd.service

* Fri Jun 20 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-6
- Resolves: #1111143 - fix for python2

* Fri Jun 20 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-5
- Related: #842455 - remove a patch that is now redundant

* Fri Jun 20 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-4
- update dnssec-trigger-script to current development submitted upstream

* Wed Jun 18 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-3
- Resolves: #1105896 - the new script doesn't call dnssec-trigger-control submit

* Fri Jun 06 2014 Pavel Šimerda <psimerda@redhat.com> - 0.12-2
- fix various dnssec-trigger-script issues

* Fri May 23 2014 Tomas Hozza <thozza@redhat.com> - 0.12-1
- Update to 0.12 version
- Drop merged patches
- Drop downstream files (systemd, dispatcher scripts)

* Tue May 13 2014 Paul Wouters <pwouters@redhat.com> - 0.11-21
- Enable full hardening (includig PIE)
- Resolves: rhbz#1045689 dnssec-trigger creates long-time RSA key with inappropriate size

* Wed Feb 19 2014 Tomas Hozza <thozza@redhat.com> - 0.11-20
- Restart NM on dnssec-trigger shutdown (let NM handle the resolv.conf content)
- HN-hook: Handle situation when connection does not have a device

* Wed Jan 29 2014 Tomas Hozza <thozza@redhat.com> - 0.11-19
- Use new Python dispatcher script and ship /etc/dnssec.conf

* Tue Jan 28 2014 Tomas Hozza <thozza@redhat.com> - 0.11-18
- Use systemd macros instead of directly calling systemctl
- simplify the systemd unit file for generating keys

* Thu Nov 21 2013 Tomas Hozza <thozza@redhat.com> - 0.11-17
- Add script to backup and restore resolv.conf on dnssec-trigger start/stop

* Mon Nov 18 2013 Tomas Hozza <thozza@redhat.com> - 0.11-16
- Improve GUI dialogs texts

* Tue Nov 12 2013 Tomas Hozza <thozza@redhat.com> - 0.11-15
- Fix NM dispatcher script to work with NM >= 0.9.9.0 (#1029571)

* Mon Aug 26 2013 Tomas Hozza <thozza@redhat.com> - 0.11-14
- Fix errors found by static analysis of source

* Fri Aug 09 2013 Tomas Hozza <thozza@redhat.com> - 0.11-13
- Use improved NM dispatcher script from upstream
- Added tmpfiles.d config due to improved NM dispatcher script

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Adam Tkac <atkac redhat com> - 0.11-11
- link dnssec-trigger.conf.8 to dnssec-trigger.8
- build dnssec-triggerd with full RELRO

* Mon Mar 04 2013 Adam Tkac <atkac redhat com> - 0.11-10
- remove deprecated "Application" keyword from desktop file

* Mon Mar 04 2013 Adam Tkac <atkac redhat com> - 0.11-9
- install various dnssec-trigger-* symlinks to dnssec-trigger.8 manpage

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Paul Wouters <pwouters@redhat.com> - 0.11-7
- Use full path for systemd (rhbz#842455)

* Tue Jul 24 2012 Paul Wouters <pwouters@redhat.com> - 0.11-6
- Patched daemon to remove immutable attr (rhbz#842455) as the
  systemd ExecStopPost= target does not seem to work

* Tue Jul 24 2012 Paul Wouters <pwouters@redhat.com> - 0.11-5
- On service stop, remove immutable attr from resolv.conf (rhbz#842455)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Paul Wouters <pwouters@redhat.com> - 0.11-3
- Fix DHCP hook for f17+ version of nmcli (rhbz#835298)

* Sun Jun 17 2012 Paul Wouters <pwouters@redhat.com> - 0.11-2
- Small textual changes to some popup windows

* Fri Jun 15 2012 Paul Wouters <pwouters@redhat.com> - 0.11-1
- Updated to 0.11
- http Hotspot detection via fedoraproject.org/static/hotspot.html
- http Hotspot Login page via uses hotspot-nocache.fedoraproject.org

* Thu Feb 23 2012 Paul Wouters <pwouters@redhat.com> - 0.10-4
- Require: unbound

* Wed Feb 22 2012 Paul Wouters <pwouters@redhat.com> - 0.10-3
- Fix the systemd startup to require unbound
- dnssec-triggerd no longer forks, giving systemd more control
- Fire NM dispatcher in ExecStartPost of dnssec-triggerd.service
- Fix tcp80 entries in dnssec-triggerd.conf
- symlink dnssec-trigger-panel to dnssec-trigger to supress the
  "-panel" in the applet name shown in gnome3


* Wed Feb 22 2012 Paul Wouters <pwouters@redhat.com> - 0.10-2
- The NM hook was not modified at the right time during build

* Wed Feb 22 2012 Paul Wouters <pwouters@redhat.com> - 0.10-1
- Updated to 0.10
- The NM hook lacks /usr/sbin in path, resulting in empty resolv.conf on hotspot

* Wed Feb 08 2012 Paul Wouters <pwouters@redhat.com> - 0.9-4
- Updated tls443 / tls80 resolver instances supplied by Fedora Hosted

* Mon Feb 06 2012 Paul Wouters <pwouters@redhat.com> - 0.9-3
- Convert from SysV to systemd for initial Fedora release
- Moved configs and pem files to /etc/dnssec-trigger/
- No more /var/run/dnssec-triggerd/
- Fix Build-requires
- Added commented tls443 port80 entries of pwouters resolvers
- On uninstall ensure there is no immutable bit on /etc/resolv.conf

* Sat Jan 07 2012 Paul Wouters <paul@xelerance.com> - 0.9-2
- Added LICENCE to doc section

* Mon Dec 19 2011 Paul Wouters <paul@xelerance.com> - 0.9-1
- Upgraded to 0.9

* Fri Oct 28 2011 Paul Wouters <paul@xelerance.com> - 0.7-1
- Upgraded to 0.7

* Fri Sep 23 2011 Paul Wouters <paul@xelerance.com> - 0.4-1
- Upgraded to 0.4

* Sat Sep 17 2011 Paul Wouters <paul@xelerance.com> - 0.3-5
- Start 01-dnssec-trigger-hook in daemon start
- Ensure dnssec-triggerd starts after NetworkManager

* Fri Sep 16 2011 Paul Wouters <paul@xelerance.com> - 0.3-4
- Initial package
