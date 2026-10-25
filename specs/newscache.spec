
Name: 		newscache
Summary: 	Free cache server for USENET News
Version: 	1.3.22
Release: 	1%{?dist}
License:	GPL-2.0-or-later
URL:		https://github.com/go-while/NewsCache
Source0: 	https://github.com/go-while/NewsCache/releases/download/%{version}/NewsCache-%{version}.tar.gz

Patch1:		newscache-1.3.22-config.patch

BuildRequires:	make
BuildRequires:	libxcrypt-devel
BuildRequires:  gcc-c++
BuildRequires:	libtool, texinfo, pam-devel
BuildRequires:	systemd-units

Requires(post):	systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units



%description
NewsCache is a free cache server for USENET News. NewsCache acts to
news reading clients like a news server, except that it stores only
those articles that have been requested by at least one client.
NewsCache targets problems of the current News System like network
bandwidth consumption or the IO load caused by news clients.


%prep
%setup -q -n NewsCache-%{version}

cp etc/newscache.conf-dist newscache.conf
%patch -P1 -p0


cat >%{name}.service <<'EOF'
[Unit]
Description=NewsCache caching news server
After=syslog.target network.target remote-fs.target

[Service]
Type=forking
ExecStart=/usr/sbin/newscache
PIDFile=/var/run/newscache.pid
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
EOF


cat >newscacheclean.service <<'EOF'
[Unit]
Description=NewsCache spool cleanup

[Service]
Type=oneshot
ExecStart=/usr/sbin/newscacheclean
EOF


cat >newscacheclean.timer <<'EOF'
[Unit]
Description=Daily NewsCache spool cleanup

[Timer]
OnCalendar=daily
RandomizedDelaySec=3hours
Persistent=true

[Install]
WantedBy=timers.target
EOF


#  sysusers.d config file
cat >newscache.sysusers.conf <<EOF
u news - 'News user' /var/cache/newscache -
EOF

#  pam.d config file
cat >newscache.pam <<EOF
#%PAM-1.0
auth    include		password-auth
account include		password-auth

EOF


%build

%configure --with-pam
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/newscache.conf-dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/newscache.auth-dist

# info stuff is too obsolete
rm -f $RPM_BUILD_ROOT%{_infodir}/*


install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m644 newscache.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

install -d $RPM_BUILD_ROOT%{_localstatedir}/cache/newscache
install -d $RPM_BUILD_ROOT%{_sysusersdir}
install -p -m644 newscache.sysusers.conf $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

install -d $RPM_BUILD_ROOT%{_unitdir}
install -p -m644 %{name}.service newscacheclean.service newscacheclean.timer $RPM_BUILD_ROOT%{_unitdir}/

install -d $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m644 newscache.pam $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/%{name}


%post
%systemd_post %{name}.service
%systemd_post newscacheclean.timer


%preun
%systemd_preun %{name}.service
%systemd_preun newscacheclean.timer


%postun
%systemd_postun_with_restart %{name}.service
%systemd_postun newscacheclean.timer



%files
%attr(755,news,news) %dir %{_localstatedir}/cache/newscache
%{_sysusersdir}/newscache.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/pam.d/*
%{_unitdir}/*
%{_bindir}/*
%{_sbindir}/*
%doc AUTHORS COPYING NEWS README README.md THANKS
%doc doc/newscache*.txt etc/*-dist
%{_mandir}/*/*


%changelog
* Sat Oct 24 2026 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.3.22-1
- Upgrade to 1.3.22

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.55.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.54.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Oct  4 2025 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.53.rc6
- update URL (#2401403)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.52.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2-0.51.rc6
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.2-0.50.rc6
- Add explicit BR: libxcrypt-devel

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.49.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-0.48.rc6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.47.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.46.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.45.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.44.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.43.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.42.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.41.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.40.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2-0.39.rc6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.38.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.37.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhat.com> - 1.2-0.36.rc6
- Use strsignal and strerror rather than sys_siglist and sys_errlist

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.35.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.34.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.33.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.2-0.32.rc6
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.31.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.30.rc6
- Fix compiling with g++ >= 8.0 (#1583363)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.29.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.2-0.28.rc6
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.27.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.26.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.25.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.24.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.23.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-0.22.rc6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.21.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.20.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  8 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.19.rc6
- update socket++ to 1.12.13
- fix socket++ autotool stuff
- avoid building socket++ docs (seems broken with makeinfo >= 5.0)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.18.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.17.rc6
- new systemd_rpm macros (#850226)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.16.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.15.rc6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.14.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.13.rc6
- Migration from SysV to Systemd init system (#699038)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.12.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 1.2-0.11.rc6
- Use password-auth common PAM configuration instead of system-auth

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.10.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.9.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan  6 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.8.rc6
- Fix autotools stuff in socket++ for libtool >= 2

* Mon Jan  5 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.7.rc6
- Add news user and group (#478785) since Fedora 10

* Fri Feb 15 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.6.rc6
- change initscript to comply with the LSB standards

* Thu Feb 14 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.5.rc6
- add patch for gcc43

* Tue Aug 28 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Correct Source0 and Source1 urls

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Tue Nov  7 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.4.rc6
- spec file cleanups
- use "include" instead of pam_stack in pam file generated

* Wed Feb 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.3.rc6
- rebuild for FC5

* Wed Nov  2 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.2.rc6
- spec file cleanups
- accepted for Fedora Extra
  (review by John Mahowald <jpmahowald@gmail.com>)

* Mon Sep 19 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2-0.1.rc6
- cleanups for Fedora Extra
- add correct init script and initial config file
- create pam and cron files just at install stage
- don't include .info file -- it is too old

* Thu Mar  3 2005 Dmitry Butskoy <Dmitry@Butskoy.name>
- include libsocket++ into source package and build with them,
  do not want an extra package used by newscache only (for a while...)
- some fixes for Fedora Core 3

* Sun Sep 26 2004 Herbert Straub <herbert@linuxhacker.at>
- Changing permission from 4775 to 0775 (updatenews)
- New upstream version: 1.2rc6

* Thu Sep 23 2004 Herbert Straub <herbert@linuxhacker.at>
- Conditional rpmbuild for SuSE
- restart on upgrade
- update the runlevel information
- New upstream version 1.2rc5

* Thu Jul 22 2004 Herbert Straub <herbert@linuxhacker.at>
- Updated to version 1.2rc4

* Tue Mar 18 2003 Carles Arjona <nospammer@bigfoot.com>
- version 0.99.22p1-1 RPM

* Sat Oct 26 2002 Carles Arjona <nospammer@bigfoot.com>
- fixed up spec file
- version 0.99.22-1 RPM

* Mon Jul 29 2002 Carles Arjona <nospammer@bigfoot.com>
- version 0.99.19-1 RPM
- added chkconfig support to init script
- added /etc/cron.daily/newscache
- fixed up both setguid.cc , version number and man pages
- built SPEC from scratch
