Name:           cloud-init
Version:        23.1.1
Release:        1%{?dist}
Summary:        Cloud instance init scripts
License:        ASL 2.0 or GPLv3
URL:            http://launchpad.net/cloud-init

Source0:        https://launchpad.net/cloud-init/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        cloud-init-tmpfiles.conf

# https://github.com/canonical/cloud-init/pull/2073
Patch1:         2073.patch
# Cherry pick of https://github.com/canonical/cloud-init/pull/2086
# and part of https://github.com/canonical/cloud-init/pull/2036
Patch2:         Fedora-Enable-CA-handling.patch

BuildArch:      noarch

BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  iproute
BuildRequires:  passwd
BuildRequires:  python3-configobj
# https://bugzilla.redhat.com/show_bug.cgi?id=1695953
BuildRequires:  python3-distro
# https://bugzilla.redhat.com/show_bug.cgi?id=1417029
BuildRequires:  python3-httpretty >= 0.8.14-2
BuildRequires:  python3-jinja2
BuildRequires:  python3-jsonpatch
BuildRequires:  python3-jsonschema
BuildRequires:  python3-tox
BuildRequires:  python3-oauthlib
BuildRequires:  python3-prettytable
BuildRequires:  python3-pyserial
BuildRequires:  python3-PyYAML
BuildRequires:  python3-requests
BuildRequires:  python3-responses
BuildRequires:  python3-six
BuildRequires:  python3-netifaces
# dnf is needed to make cc_ntp unit tests work
# https://bugs.launchpad.net/cloud-init/+bug/1721573
BuildRequires:  /usr/bin/dnf

Requires:       dhcp-client
Requires:       hostname
Requires:       e2fsprogs
Requires:       iproute
Requires:       python3-libselinux
Requires:       net-tools
Requires:       policycoreutils-python3
Requires:       procps
Requires:       python3-configobj
# https://bugzilla.redhat.com/show_bug.cgi?id=1695953
Requires:       python3-distro
Requires:       python3-jinja2
Requires:       python3-jsonpatch
Requires:       python3-jsonschema
Requires:       python3-oauthlib
Requires:       python3-prettytable
Requires:       python3-pyserial
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-six
Requires:       shadow-utils
Requires:       util-linux
Requires:       xfsprogs
# https://bugzilla.redhat.com/show_bug.cgi?id=1974262
Requires:       gdisk
Requires:       openssl

%{?systemd_requires}


%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.


%prep
%autosetup -p1

# Change shebangs
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
       -e 's|#!/usr/bin/python|#!/usr/bin/python3|' tools/* cloudinit/ssh_util.py

# Removing shebang manually because of rpmlint, will update upstream later
sed -i -e 's|#!/usr/bin/python||' cloudinit/cmd/main.py

# Use unittest from the standard library. unittest2 is old and being
# retired in Fedora. See https://bugzilla.redhat.com/show_bug.cgi?id=1794222
find tests/ -type f | xargs sed -i s/unittest2/unittest/
find tests/ -type f | xargs sed -i s/assertItemsEqual/assertCountEqual/

%build
%py3_build


%install
%py3_install -- --init-system=systemd

# Generate cloud-config file
python3 tools/render-cloudcfg --variant %{?rhel:rhel}%{!?rhel:fedora} > $RPM_BUILD_ROOT/%{_sysconfdir}/cloud/cloud.cfg

mkdir -p $RPM_BUILD_ROOT/var/lib/cloud

# /run/cloud-init needs a tmpfiles.d entry
mkdir -p $RPM_BUILD_ROOT/run/cloud-init
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d
cp -p tools/21-cloudinit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf

# installing man pages
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/
for man in cloud-id.1 cloud-init.1 cloud-init-per.1; do
    install -c -m 0644 doc/man/${man} ${RPM_BUILD_ROOT}%{_mandir}/man1/${man}
    chmod -x ${RPM_BUILD_ROOT}%{_mandir}/man1/*
done

# Put files in /etc/systemd/system in the right place
cp -a %{buildroot}/etc/systemd %{buildroot}/usr/lib
rm -rf %{buildroot}/etc/systemd

%check
python3 -m pytest tests/unittests

%post
%systemd_post cloud-config.service cloud-config.target cloud-final.service cloud-init.service cloud-init.target cloud-init-local.service


%preun
%systemd_preun cloud-config.service cloud-config.target cloud-final.service cloud-init.service cloud-init.target cloud-init-local.service


%postun
%systemd_postun cloud-config.service cloud-config.target cloud-final.service cloud-init.service cloud-init.target cloud-init-local.service


%files
%license LICENSE LICENSE-Apache2.0 LICENSE-GPLv3
%doc ChangeLog
%doc doc/*
%doc %{_sysconfdir}/cloud/clean.d/README
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg
%dir               %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d/*.cfg
%doc               %{_sysconfdir}/cloud/cloud.cfg.d/README
%dir               %{_sysconfdir}/cloud/templates
%config(noreplace) %{_sysconfdir}/cloud/templates/*
%dir               %{_sysconfdir}/rsyslog.d
%config(noreplace) %{_sysconfdir}/rsyslog.d/21-cloudinit.conf
%{_sysconfdir}/NetworkManager/dispatcher.d/hook-network-manager
%{_sysconfdir}/dhcp/dhclient-exit-hooks.d/hook-dhclient
%{_udevrulesdir}/66-azure-ephemeral.rules
%{_unitdir}/cloud-config.service
%{_unitdir}/cloud-final.service
%{_unitdir}/cloud-init.service
%{_unitdir}/cloud-init-local.service
%{_unitdir}/cloud-config.target
%{_unitdir}/cloud-init.target
/usr/lib/systemd/system-generators/cloud-init-generator
%{_unitdir}/cloud-init-hotplugd.service
%{_unitdir}/cloud-init-hotplugd.socket
%{_unitdir}/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf
%{_tmpfilesdir}/%{name}.conf
%{python3_sitelib}/*
%{_libexecdir}/%{name}
%{_bindir}/cloud-init*
%{_bindir}/cloud-id
%dir /run/cloud-init
%dir /var/lib/cloud
%{_datadir}/bash-completion/completions/cloud-init


%changelog
* Wed Mar 22 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 23.1.1-1
- Rebase to 23.1.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 22.2-3
- Rebuilt for Python 3.11

* Thu Jun 16 2022 Neal Gompa <ngompa@fedoraproject.org> - 22.2-2
- Add dhcp-client dependency for Azure and OCI network bootstrap

* Thu May 19 2022 Neal Gompa <ngompa@fedoraproject.org> - 22.2-1
- Rebase to 22.2

* Thu Mar 10 2022 Dusty Mabe <dusty@dustymabe.com> - 22.1-3
- Drop requirement on NetworkManager-config-server

* Tue Feb 22 2022 Neal Gompa <ngompa@fedoraproject.org> - 22.1-2
- Drop extra tests search in prep

* Tue Feb 22 2022 Neal Gompa <ngompa@fedoraproject.org> - 22.1-1
- Rebase to 22.1
- Backport cloud-init PR to add proper NetworkManager support [bz#2014701]
- Add patch to prefer NetworkManager [bz#2014701]

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Neal Gompa <ngompa@fedoraproject.org> - 21.3-4
- Add gdisk and openssl deps to fix UEFI / Azure initialization [bz#1974262]

* Wed Dec 15 2021 Neal Gompa <ngompa@fedoraproject.org> - 21.3-3
- Backport fix for tests running with new pyyaml

* Wed Sep 08 2021 Eduardo Otubo <otubo@redhat.com> - 21.3-2
- Adding man pages [bz#1952568]

* Thu Sep 02 2021 Eduardo Otubo <otubo@redhat.com> - 21.3-1
- Updated to 20.4 [bz#2000540]

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 20.4-6
- Fix collections import to work with Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20.4-5
- Rebuilt for Python 3.10

* Mon Feb 08 2021 Eduardo Otubo <otubo@redhat.com> - 20.4-4
- Reverting commit b0e7381 [bz#1924588]

* Wed Feb 03 2021 Eduardo Otubo <otubo@redhat.com> - 20.4-3
- Adding requirement hostname to specfile [bz#1925118]

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Eduardo Otubo <otubo@redhat.com> - 20.4-2
- Updated to 20.4 [bz#1902250]

* Mon Sep 07 2020 Eduardo Otubo <otubo@redhat.com> - 19.4-7
- Fix execution fail with backtrace

* Mon Sep 07 2020 Eduardo Otubo <otubo@redhat.com> - 19.4-6
- Adding missing patches to spec file

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 19.4-4
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Eduardo Otubo <otubo@redhat.com> - 19.4-3
- Fix BZ#1798729 - CVE-2020-8632 cloud-init: Too short random password length
  in cc_set_password in config/cc_set_passwords.py
- Fix BZ#1798732 - CVE-2020-8631 cloud-init: Use of random.choice when
  generating random password

* Sun Feb 23 2020 Dusty Mabe <dusty@dustymabe.com> - 19.4-2
- Fix sed substitutions for unittest2 and assertItemsEqual
- Fix failing unittests by including `BuildRequires: passwd`
    - The unittests started failing because of upstream commit
      7c07af2 where cloud-init can now support using `usermod` to
      lock an account if `passwd` isn't installed. Since `passwd`
      wasn't installed in our mock buildroot it was choosing to
      use `usermod` and the unittests were failing. See:
      https://github.com/canonical/cloud-init/commit/7c07af2
- Add missing files to package
    - /usr/bin/cloud-id
    - /usr/share/bash-completion/completions/cloud-init

* Fri Feb 14 2020 Eduardo Otubo <otubo@redhat.com> - 19.4-1
- Updated to 19.4
- Rebasing the Fedora specific patches but removing patches that don't apply anymore

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Miro Hrončok <mhroncok@redhat.com> - 17.1-14
- Drop unneeded build dependency on python3-unittest2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 17.1-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 17.1-12
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Björn Esser <besser82@fedoraproject.org> - 17.1-10
- Add patch to replace platform.dist() [RH:1695953]
- Add (Build)Requires: python3-distro

* Tue Apr 23 2019 Björn Esser <besser82@fedoraproject.org> - 17.1-9
- Fix %%systemd_postun macro [RH:1695953]
- Add patch to fix failing test for EPOCHREALTIME bash env [RH:1695953]

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 17.1-6
- Rebuilt for Python 3.7

* Sat Apr 21 2018 Lars Kellogg-Stedman <lars@redhat.com> - 17.1-5
- Enable dhcp on EC2 interfaces with only local ipv4 addresses [RH:1569321]
  (cherry pick upstream commit eb292c1)

* Mon Mar 26 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 17.1-4
- Make sure the patch does not add infinitely many entries

* Mon Mar 26 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 17.1-3
- Add patch to retain old values of /etc/sysconfig/network

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct  4 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 17.1-1
- Updated to 17.1

* Fri Sep 15 2017 Dusty Mabe <dusty@dustymabe.com> - 0.7.9-9
- Fix issues with growing xfs filesystems [RH:1490505]
- Add in hook-dhclient to help enable azure [RH:1477333]

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.9-7
- Fixed broken sysconfig file writing on DigitalOcean [RH:1465440]

* Wed Jun 21 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.9-6
- Fixed NameError in package module [RH:1447708]
- Resolved a conflict between cloud-init and NetworkManager writing resolv.conf [RH:1454491 RH:1461959 LP:1693251]
- Fixed broken fs_setup cmd option [LP:1687712]

* Fri Apr 14 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.9-5
- Made DigitalOcean DNS server handling consistent with OpenStack [RH:1442463, LP:1675571]
- Improved handling of multiple NICs on DigitalOcean [RH:1442463]
- Assign link-local IPV4 addresses in DigitalOcean based on interface indexes [RH:1442463]

* Tue Mar 14 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.9-4
- Fixed systemd dependency cycle with cloud-final and os-collect-config [RH:1420946, RH:1428492]
- Fixed systemd dependency cycle with cloud-init and multi-user.target [RH:1428492, RH:1430511]
- Fixed errors in network sysconfig handling [RH:1389530, LP:1665441]
- Made > 3 name servers a warning, not a fatal error, unbreaking IPv6 setups [LP:1670052]
- Fixed IPv6 gateways in network sysconfig [LP:1669504]
- Ordered cloud-init.service after network.service and NetworkManager.service [RH:1400249]

* Tue Mar 14 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.8-6
- Ordered cloud-init.service after network.service and NetworkManager.service [RH:1400249]
- Stopped caching IAM instance profile credentials on disk [LP:1638312]

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.9-2
- Fixed hostnamectl running before dbus is up [RH:1417025]

* Fri Jan 27 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.8-5
- Re-applied rsyslog configuration fixes
- Disabled GCE tests broken by python-httpretty-0.8.14-1.20161011git70af1f8
- Fixed systemd dependency loop for cloud-init.target [RH:1393094]

* Fri Jan 20 2017 Colin Walters <walters@verbum.org> - 0.7.9-1
- New upstream version [RH:1393094]

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.7.8-4
- Rebuild for Python 3.6

* Tue Oct 25 2016 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.8-3
- Enabled the DigitalOcean metadata provider by default [RH:1388568]

* Fri Oct 14 2016 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.8-2
- Stopped writing NM_CONTROLLED=no to interface config files [RH:1385172]

* Thu Sep 29 2016 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.8-1
- Updated to 0.7.8
- Dropped run-parts dependency [RH:1355917]
- Ordered cloud-init-local before NetworkManager
- Backported DigitalOcean network configuration support [RH:1380489]
- Added xfsprogs dependency for Fedora Server's default filesystem

* Tue Aug 30 2016 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.7-1
- Updated to 0.7.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-10.20160622bzr1245
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul  6 2016 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.6-20160622bzr1245
- Updated to bzr snapshot 1245

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-8.20150813bzr1137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-7.20150813bzr1137
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 13 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.6-6.20150813bzr1137
- Updated to bzr snapshot 1137

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5.20140218bzr1060
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.6-4.20140218bzr1060
- Updated to bzr snapshot 1060 for python 3 support
- Switched to python 3 [RH:1024357]
- Added %%check
- Dropped dmidecode dependency, switched back to noarch

* Thu Feb 19 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.6-3
- Stopped depending on git to build
- Stopped implicitly listing doc files twice
- Added recognition of 3 ecdsa-sha2-nistp* ssh key types [RH:1151824]
- Fixed handling of user group lists that contain spaces [RH:1126365 LP:1354694]
- Changed network.target systemd deps to network-online.target [RH:1110731 RH:1112817 RH:1147613]
- Fixed race condition between cloud-init.service and the login prompt
- Stopped enabling services in %%post (now done by kickstart) [RH:850058]
- Switched to dnf instead of yum when available [RH:1194451]

* Fri Nov 14 2014 Colin Walters <walters@redhat.com> - 0.7.6-2
- New upstream version [RH:974327]
- Drop python-cheetah dependency (same as above bug)

* Fri Nov  7 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.5-8
- Dropped python-boto dependency [RH:1161257]
- Dropped rsyslog dependency [RH:986511]

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Dennis Gilmore <dennis@ausil.us> - 0.7.5-6
- fix typo in settings.py preventing metadata being fecthed in ec2

* Mon Jun  9 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.5-5
- Stopped calling ``udevadm settle'' with --quiet since systemd 213 removed it

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.5-3
- Make dmidecode dependency arch-dependent [RH:1025071 RH:1067089]

* Mon Jun  2 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.2-9
- Write /etc/locale.conf instead of /etc/sysconfig/i18n [RH:1008250]
- Add tmpfiles.d configuration for /run/cloud-init [RH:1103761]
- Use the license rpm macro
- BuildRequire python-setuptools, not python-setuptools-devel

* Fri May 30 2014 Matthew Miller <mattdm@fedoraproject.org> - 0.7.5-2
- add missing python-jsonpatch dependency [RH:1103281]

* Tue Apr 29 2014 Sam Kottler <skottler@fedoraproject.org> - 0.7.5-1
- Update to 0.7.5 and remove patches which landed in the release

* Sat Jan 25 2014 Sam Kottler <skottler@fedoraproject.org> - 0.7.2-8
- Remove patch to the Puppet service unit nane [RH:1057860]

* Tue Sep 24 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.2-7
- Dropped xfsprogs dependency [RH:974329]

* Tue Sep 24 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.2-6
- Added yum-add-repo module

* Fri Sep 20 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.2-5
- Fixed puppet agent service name [RH:1008250]
- Let systemd handle console output [RH:977952 LP:1228434]
- Fixed restorecon failure when selinux is disabled [RH:967002 LP:1228441]
- Fixed rsyslog log filtering
- Added missing modules [RH:966888]

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Matthew Miller <mattdm@fedoraproject.org> - 0.7.2-3
- switch ec2-user to "fedora" --  see bugzilla #971439. To use another
  name, use #cloud-config option "users:" in userdata in cloud metadata
  service
- add that user to systemd-journal group

* Fri May 17 2013 Steven Hardy <shardy@redhat.com> - 0.7.2
- Update to the 0.7.2 release

* Thu May 02 2013 Steven Hardy <shardy@redhat.com> - 0.7.2-0.1.bzr809
- Rebased against upstream rev 809, fixes several F18 related issues
- Added dependency on python-requests

* Sat Apr  6 2013 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-4
- Don't ship tests

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.1-2
- Added default_user to cloud.cfg (this is required for ssh keys to work)

* Wed Nov 21 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.1-1
- Rebased against version 0.7.1
- Fixed broken sudoers file generation
- Fixed "resize_root: noblock" [LP:1080985]

* Tue Oct  9 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.0-1
- Rebased against version 0.7.0
- Fixed / filesystem resizing

* Sat Sep 22 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.0-0.3.bzr659
- Added dmidecode dependency for DataSourceAltCloud

* Sat Sep 22 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.0-0.2.bzr659
- Rebased against upstream rev 659
- Fixed hostname persistence
- Fixed ssh key printing
- Fixed sudoers file permissions

* Mon Sep 17 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.7.0-0.1.bzr650
- Rebased against upstream rev 650
- Added support for useradd --selinux-user

* Thu Sep 13 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.3-0.5.bzr532
- Use a FQDN (instance-data.) for instance data URL fallback [RH:850916 LP:1040200]
- Shut off systemd timeouts [RH:836269]
- Send output to the console [RH:854654]

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-0.4.bzr532
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Pádraig Brady <P@draigBrady.com> - 0.6.3-0.3.bzr532
- Add support for installing yum packages

* Sat Mar 31 2012 Andy Grimm <agrimm@gmail.com> - 0.6.3-0.2.bzr532
- Fixed incorrect interpretation of relative path for
  AuthorizedKeysFile (BZ #735521)

* Mon Mar  5 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.3-0.1.bzr532
- Rebased against upstream rev 532
- Fixed runparts() incompatibility with Fedora

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-0.8.bzr457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct  5 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.7.bzr457
- Disabled SSH key-deleting on startup

* Wed Sep 28 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.6.bzr457
- Consolidated selinux file context patches
- Fixed cloud-init.service dependencies
- Updated sshkeytypes patch
- Dealt with differences from Ubuntu's sshd

* Sat Sep 24 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.5.bzr457
- Rebased against upstream rev 457
- Added missing dependencies

* Fri Sep 23 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.4.bzr450
- Added more macros to the spec file

* Fri Sep 23 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.3.bzr450
- Fixed logfile permission checking
- Fixed SSH key generation
- Fixed a bad method call in FQDN-guessing [LP:857891]
- Updated localefile patch
- Disabled the grub_dpkg module
- Fixed failures due to empty script dirs [LP:857926]

* Fri Sep 23 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.2.bzr450
- Updated tzsysconfig patch

* Wed Sep 21 2011 Garrett Holmstrom <gholms@fedoraproject.org> - 0.6.2-0.1.bzr450
- Initial packaging
