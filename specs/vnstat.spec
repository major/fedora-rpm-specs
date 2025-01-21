Summary: Console-based network traffic monitor
Name: vnstat
Version: 2.10
Release: 7%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://humdi.net/vnstat/
Source0: http://humdi.net/vnstat/vnstat-%{version}.tar.gz
Patch0: vnstat.service.patch
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: systemd
BuildRequires: sqlite-devel

%description
vnStat is a console-based network traffic monitor that keeps a log of daily
network traffic for the selected interface(s). vnStat isn't a packet sniffer.
The traffic information is analyzed from the /proc file-system, so vnStat can
be used without root permissions. See the web-page for few 'screenshots'.

%package vnstati
Summary: Image output support for vnstat
Recommends: %{name} = %{version}-%{release}

%description vnstati
The purpose of vnstati is to provide image output support for statistics
collected using vnstat. The image file format is limited to png. All basic
outputs of vnStat are supported excluding live traffic features. The image can
be outputted either to a file or to standard output.

%prep
%setup -q
%patch -P0 -p1

# disable maximum bandwidth setting and change pidfile location
sed -i -e "s,/var/run/,/run/vnstat/,g; \
	s,MaxBandwidth 100,MaxBandwidth 0,g;" \
	cfg/vnstat.conf

%build
%{configure}
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" all

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_tmpfilesdir}

%{__mkdir_p} %{buildroot}/run/
%{__install} -d -m 0700 %{buildroot}/run/%{name}/

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__install} -p -m 644 examples/systemd/vnstat.service $RPM_BUILD_ROOT%{_unitdir}/
%{__rm} -rf examples/init.d
%{__rm} -rf examples/systemd
%{__rm} -rf examples/launchd
%{__rm} -rf examples/upstart

%{__cat} >> $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf << END
D /run/vnstat 0700 vnstat vnstat
END

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} -M \
  -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "vnStat user" %{name}
exit 0

%post
%systemd_post vnstat.service

%preun
%systemd_preun vnstat.service

%postun
%systemd_postun_with_restart vnstat.service

%files
%license COPYING
%doc CHANGES FAQ README INSTALL examples
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man1/vnstat.1*
%{_mandir}/man5/vnstat.conf.5*
%{_mandir}/man8/vnstatd.8*
%{_bindir}/vnstat
%{_sbindir}/vnstatd
%attr(-,vnstat,vnstat)%dir /run/%{name}/
%attr(-,vnstat,vnstat)%{_localstatedir}/lib/%{name}

%files vnstati
%license COPYING
%{_mandir}/man1/vnstati.1*
%{_bindir}/vnstati

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Adrian Reber <adrian@lisas.de> - 2.10-1
- Upgrade to 2.10 (#2137399)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Adrian Reber <adrian@lisas.de> - 2.9-2
- Upgrade to 2.9 (#2044224)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Adrian Reber <adrian@lisas.de> - 2.8-1
- Upgrade to 2.8 (#1961015)
- Create sub-package for vnstati and its libgd dependency (#1993650)

* Mon Aug 30 2021 Adrian Reber <adrian@lisas.de> - 2.7-1
- Upgrade to 2.7 (#1961015)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Adrian Reber <adrian@lisas.de> - 2.6-1
- Upgrade to 2.6 (#1791158)

* Wed Jan 15 2020 Adrian Reber <adrian@lisas.de> - 2.5-1
- Upgrade to 2.5 (#1791158)

* Wed Nov 06 2019 Adrian Reber <adrian@lisas.de> - 2.4-1
- Upgrade to 2.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 12 2019 Adrian Reber <adrian@lisas.de> -2.3-1
- Upgrade to 2.3

* Sun Apr 28 2019 Adrian Reber <adrian@lisas.de> -2.2-1
- Upgrade to 2.2 (#1703811)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Adrian Reber <adrian@lisas.de> - 1.18-1
- Upgrade to 1.18 (#1551364)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Adrian Reber <adrian@lisas.de> - 1.17-1
- Upgrade to 1.17 (#1423060)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Adrian Reber <adrian@lisas.de> - 1.16-1
- Upgrade to 1.16 (#1408565)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Adrian Reber <adrian@lisas.de> - 1.15-1
- Upgrade to 1.15 (#1296771)

* Tue Dec 01 2015 Adrian Reber <adrian@lisas.de> - 1.14-3
- Fixed "Service fails to start because it's run as root" (#1278027)

* Tue Aug 11 2015 Adrian Reber <adrian@lisas.de> - 1.14-2
- Use %%license for COPYING

* Tue Aug 11 2015 Adrian Reber <adrian@lisas.de> - 1.14-1
- Upgrade to 1.14
- Remove cron based setup (removed functionality)
- Remove systemd unit file (now included)
- Remove unnecessary patches

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Adrian Reber <adrian@lisas.de> - 1.11-22
- install unit file as 644 and not 755 (fixes #1157199)

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 1.11-21
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Adrian Reber <adrian@lisas.de> - 1.11-18
- fix bogus dates
- added patch for
  "vnstat.c:489:22: warning: iteration 12u invokes undefined behavior [-Waggressive-loop-optimizations]"

* Wed Aug 07 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.11-17
- Fix the build by adding the missing BR on systemd.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 1.11-15
- rebuild for new GD 2.1.0

* Fri Mar 08 2013 Adrian Reber <adrian@lisas.de> - 1.11-14
- spec cleanup

* Thu Mar 07 2013 Adrian Reber <adrian@lisas.de> - 1.11-13
- fixed "/usr/sbin/vnstat.cron is incorrect" (#919157)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Adrian Reber <adrian@lisas.de> - 1.11-11
- fixed "Introduce new systemd-rpm macros in vnstat spec file" (#850361)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Jon Ciesla <limburgher@gmail.com> - 1.11-8
- Update to systemd, BZ 661325.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Adrian Reber <adrian@lisas.de> - 1.11-6
- fixed /run/%%{name}/ permissions

* Thu Dec 22 2011 Adrian Reber <adrian@lisas.de> - 1.11-5
- added /run/%%{name}/ directory to file list

* Thu Dec 22 2011 Adrian Reber <adrian@lisas.de> - 1.11-4
- added patch to check for pidfile in /run/vnstat

* Tue Nov 29 2011 Adrian Reber <adrian@lisas.de> - 1.11-3
- create file in tmpfiles.d for pidfile (#750141)

* Tue Jun 28 2011 Adrian Reber <adrian@lisas.de> - 1.11-2
- do not run vnstatd as the root user but as the vnstat user (#711995)

* Thu Jun 02 2011 Robert Scheck <robert@fedoraproject.org> - 1.11-1
- Upgrade to 1.11

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 03 2010 Robert Scheck <robert@fedoraproject.org> - 1.10-1
- Upgrade to 1.10

* Sat Dec 26 2009 Robert Scheck <robert@fedoraproject.org> - 1.9-2
- Work around a buffer overflow in vnstati until 1.10 (#550635)

* Sat Dec 26 2009 Robert Scheck <robert@fedoraproject.org> - 1.9-1
- Upgrade to 1.9 and make rpmlint more silent
- Make %%pre script with useradd more conform to guidelines
- Replace %%{_initddir} macro for more easy EPEL support
- Preserve timestamps when using sed to manipulate files

* Wed Nov 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.8-7
- Prevent upstream build from stripping binaries before rpmbuild does it.

* Mon Nov 09 2009 Adrian Reber <adrian@lisas.de> - 1.8-6
- to not activate vnstatd by default
- remove executable bit from perl cgi example
- do not package example startup scripts

* Wed Aug  5 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.8-5
- update to 1.8
- add vnstatd, vnstati (by using default Makefile install target)
- add initscript for vnstatd

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6-2
- Autorebuild for GCC 4.3

* Sun Jan 13 2008 Adrian Reber <adrian@lisas.de> - 1.6-1
- updated to 1.6
- added vnstat.conf to %%{_sysconfdir}
- fixed a few rpmlint warnings

* Thu Oct 11 2007 Adrian Reber <adrian@lisas.de> - 1.4-10
- rebuilt for BuildID
- updated license tag

* Mon Feb 26 2007 Adrian Reber <adrian@lisas.de> - 1.4-9
- applied patch for spec file cleanup (#229037)

* Fri Sep 15 2006 Adrian Reber <adrian@lisas.de> - 1.4-8
- rebuilt

* Fri Mar 17 2006 Adrian Reber <adrian@lisas.de> - 1.4-7
- rebuilt; fixed dist tag

* Fri Mar 17 2006 Adrian Reber <adrian@lisas.de> - 1.4-6
- rebuilt

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.4-5
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 28 2005 Adrian Reber <adrian@lisas.de> 1.4-3
- removed occurences of VNSTAT_DISABLED in
  %%{_sysconfdir}/sysconfig/%%{name} and
  %%{_sbindir}/%%{name}.cron

* Thu Feb 24 2005 Adrian Reber <adrian@lisas.de> 1.4-2
- removed "#--------------"
- added %%{version} to Source0
- replaced almost empty FAQ with the one from the web
- added INSTALL to %%doc
- added %%{_sysconfdir}/sysconfig/%%{name}
  and %%{_sbindir}/%%{name}.cron to allow flexible configuration
- cron script and configuration file defaults to vnstat disabled
- added example scripts from cron/* and pppd/* to %%doc

* Wed Jul 21 2004 Adrian Reber <adrian@lisas.de> 1.4-1
- initial build
