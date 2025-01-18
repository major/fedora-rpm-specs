%global cachedir %{_localstatedir}/cache/ddclient
%global rundir   %{_rundir}/ddclient

Summary:           Client to update dynamic DNS host entries
Name:              ddclient
Version:           3.11.2
Release:           6%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:           GPL-2.0-or-later
URL:               https://ddclient.net/
Source0:           https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:           ddclient.rwtab
Source2:           ddclient.service
Source3:           ddclient.sysconfig
Source4:           ddclient.NetworkManager
Source5:           ddclient-tmpfiles.conf
Patch0:            skip-tests.patch

BuildArch:         noarch

BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     make
BuildRequires:     perl-generators
BuildRequires:     perl(Sys::Hostname)
BuildRequires:     perl(version)
BuildRequires:     systemd
Requires(pre):     shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

# For tests
BuildRequires:     iproute
BuildRequires:     perl(HTTP::Daemon)
BuildRequires:     perl(HTTP::Daemon::SSL)
BuildRequires:     perl(HTTP::Message::PSGI)
BuildRequires:     perl(HTTP::Request)
BuildRequires:     perl(HTTP::Response)
BuildRequires:     perl(IO::Socket::INET6)
BuildRequires:     perl(Test::MockModule)
BuildRequires:     perl(Test::TCP)
BuildRequires:     perl(Test::Warnings)
BuildRequires:     perl(Time::HiRes)

Requires:          perl(Data::Validate::IP)
Requires:          perl(Digest::SHA1)
Requires:          perl(IO::Socket::INET6)
Requires:          perl(IO::Socket::SSL)
Requires:          perl(JSON::PP)

# Old NetworkManager expects the dispatcher scripts in a different place
Conflicts:         NetworkManager < 1.20

%description
ddclient is a Perl client used to update dynamic DNS entries for accounts
on many different dynamic DNS services. Features include: Operating as a
daemon, manual and automatic updates, static and dynamic updates, optimized
updates for multiple addresses, MX, wildcards, abuse avoidance, retrying
the failed updates and sending update status to syslog and through e-mail.

%prep
%autosetup -p 1
# Send less mail by default, eg. not on every shutdown.
sed -e 's|^mail=|#mail=|' -i ddclient.conf.in
./autogen


%configure \
 --runstatedir=%{rundir}

%build
make


%install
install -D -p -m 755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -p -m 600 ddclient.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -D -p -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/%{name}

install -D -p -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 755 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d/50-%{name}
install -D -p -m 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf

mkdir -p $RPM_BUILD_ROOT%{cachedir}
mkdir -p $RPM_BUILD_ROOT%{rundir}
touch $RPM_BUILD_ROOT%{cachedir}/%{name}.cache

# Correct permissions for later usage in %doc
chmod 644 sample-*


%check
make VERBOSE=1 check


%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/cache/%{name} -s /sbin/nologin -c "Dynamic DNS Client" %{name}
exit 0

%post
%systemd_post %{name}.service
if [ $1 == 1 ]; then
    mkdir -p %{rundir}
    chown %{name}:%{name} %{rundir}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license COPYING COPYRIGHT
%doc README* ChangeLog.md sample-etc_ppp_ip-up.local
%doc sample-etc_dhclient-exit-hooks sample-etc_cron.d_ddclient
%doc sample-ddclient-wrapper.sh sample-etc_dhcpc_dhcpcd-eth0.exe

%{_sbindir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service

# sysconfdir
%config(noreplace) %{_sysconfdir}/rwtab.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(600,%{name},%{name}) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/NetworkManager/dispatcher.d/50-%{name}

# localstatedir
%attr(0700,%{name},%{name}) %dir %{cachedir}
%attr(0600,%{name},%{name}) %ghost %{cachedir}/%{name}.cache
%ghost %attr(0755,%{name},%{name}) %dir %{rundir}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.11.2-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Scott Talbert <swt@techie.net> - 3.11.2-1
- Update to new upstream release 3.11.2 (#2251294)

* Sat Nov 18 2023 Scott Talbert <swt@techie.net> - 3.11.1-1
- Update to new upstream release 3.11.1 (#2244514)

* Thu Sep 14 2023 kenneth topp <toppk@bllue.org>  - 3.10.0-1
- Update to new upstream release 3.10.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.9.1-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Scott Talbert <swt@techie.net> - 3.9.1-3
- Move pidfile from /var/run to /run (#1876265)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Scott Talbert <swt@techie.net> - 3.9.1-1
- Update to new upstream release 3.9.1 (#1796923)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 3.9.0-4
- Move the NetworkManager dispatcher script out of /etc

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Scott Talbert <swt@techie.net> - 3.9.0-1
- New upstream release 3.9.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Scott Talbert <swt@techie.net> - 3.8.3-5
- Start after network-online.target rather than network.target (#1476999)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Scott Talbert <swt@techie.net> - 3.8.3-2
- Prevent NetworkManager from starting ddclient if it is disabled (#1409178)

* Mon Mar 28 2016 Scott Talbert <swt@techie.net> - 3.8.3-1
- New upstream release 3.8.3 (#1226537)
- Change NetworkManager dispatcher to look for PID file (#1316149)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.8.2-1
- update to upstream release 3.8.2
- remove old EPEL 6 related macros
- remove all logic for older versions of Fedora/EPEL
- make spec more readable

* Wed Dec 25 2013 Robert Scheck <robert@fedoraproject.org> 3.8.1-9
- Use the new systemd macros (#850084, thanks to Lukáš Nykrýn)
- Adapted the spec file to handle systemd and SysV initscripts

* Sat Aug 10 2013 Paul Howarth <paul@city-fan.org> - 3.8.1-8
- BR: systemd-units for %%{_unitdir} macro definition (fixes FTBFS #992118)
- Put tmpfiles config in %%{_tmpfilesdir}, not under /etc
- Package installation creates %%{_localstatedir}/run/%%{name} (#909272, #957355)
- Service files are not executable
- Require perl(Digest::SHA1) (#909258)
- Wait for name resolution to be available before starting (#905553)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.8.1-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Jon Ciesla <limburgher@gmail.com> - 3.8.1-3
- Add ghost to /var/run/ddclient

* Mon May 14 2012 Jon Ciesla <limburgher@gmail.com> - 3.8.1-2
- Add tmpfiles.d.

* Thu Mar 29 2012 Jon Ciesla <limburgher@gmail.com> - 3.8.1-1
- Latest upstream.
- Migrate to systemd, 718756.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 10 2011 Robert Scheck <robert@fedoraproject.org> 3.8.0-4
- Replaced Requires(hint) by Requires as RPM 4.9 dropped support

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 29 2010 Robert Scheck <robert@fedoraproject.org> 3.8.0-2
- Fixed wrong permissions at NetworkManager dispatcher (#506286)
- Updated %%description to be more verbose and detailed (#588053)

* Sat May 01 2010 Robert Scheck <robert@fedoraproject.org> 3.8.0-1
- Upgrade to 3.8.0 and several spec file cleanups (#551906)
- Rewrote initscript to match LSB standards and headers (#246903)
- Added dispatcher to NetworkManager to avoid failures (#506286)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 23 2008 Robert Scheck <robert@fedoraproject.org> 3.7.3-1
- Upgrade to 3.7.3 (#429438)
- Updated the license tag according to the guidelines

* Thu Jun 14 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.2-1
- 3.7.2.
- Tweak default config to send less mail (eg. not on every shutdown).

* Fri Mar  2 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.7.1-1
- 3.7.1, cache file moved to /var/cache/ddclient.
- Run as a dedicated ddclient user (#220539).
- Add read only root/temporary state config (#220540).
- Create/chmod cache in init script instead of %%post.
- Add scriptlet dependencies, try-restart action and other minor tweaks.

* Sat Jul 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.6.6-1
- 3.6.6, update URLs (#165272).
- Restart service on future package upgrades (still manually needed this time).
- Don't set service to autostart on "chkconfig --add".
- Fix sysconfig/ddclient permissions.
- Drop non-useful samples.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.6.3-5
- rebuilt

* Mon Apr 05 2004 Toshio Kuratomi <toshio[+]tiki-lounge.com> - 0:3.6.3-0.fdr.4.fc1
- Fix %%doc %%attr ownership
- Touch the cache file in %%post

* Mon Sep 08 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:3.6.3-0.fdr.3
- Add own Fedora-style initscript and /etc/sysconfig/ddclient file.
- Fix file permissions of config file and example files.
- Since ddclient.cache.patch uses hardcoded /var, don't use
  %%_localstatedir in spec file either.

* Sun Sep 07 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:3.6.3-0.fdr.2: fixed ghostness of cache file
