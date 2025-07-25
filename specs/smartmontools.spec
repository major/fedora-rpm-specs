# defining macros needed by SELinux
%global with_selinux 1
%global selinuxtype targeted
%global moduletype contrib
%global modulename smartmon

Summary:	Tools for monitoring SMART capable hard disks
Name:		smartmontools
Version:	7.5
Release:	3%{?dist}
Epoch:		1
License:	GPL-2.0-or-later
URL:		https://www.smartmontools.org/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:	smartmontools.sysconf
Source4:	smartdnotify
#semi-automatic update of drivedb.h
%global		UrlSource5	https://sourceforge.net/p/smartmontools/code/HEAD/tree/trunk/smartmontools/drivedb.h?format=raw
Source5:	drivedb.h
Source6:	%{modulename}.te
Source7:	%{modulename}.if
Source8:	%{modulename}.fc

#fedora/rhel specific
Patch1:		smartmontools-5.38-defaultconf.patch

BuildRequires: make
BuildRequires:	gcc-c++ readline-devel ncurses-devel automake util-linux groff gettext
BuildRequires:	libselinux-devel libcap-ng-devel
BuildRequires:	systemd systemd-devel
%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:	(%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/smartctl
%endif

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

%description
The smartmontools package contains two utility programs (smartctl
and smartd) to control and monitor storage systems using the Self-
Monitoring, Analysis and Reporting Technology System (SMART) built
into most modern ATA and SCSI hard disks. In many cases, these
utilities will provide advanced warning of disk degradation and
failure.

%if 0%{?with_selinux}
%package selinux
Summary:	SELinux policies for smartmontools
BuildArch:	noarch
Requires:	selinux-policy-%{selinuxtype}
Requires(post):	selinux-policy-%{selinuxtype}
BuildRequires:	selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module for smartmontools
%endif

%prep
%setup -q 
%patch -P1 -p1 -b .defaultconf
cp %{SOURCE5} .
%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE6} %{SOURCE7} %{SOURCE8} selinux/
%endif

%build
autoreconf -i
%configure --with-selinux --with-libcap-ng=yes --with-libsystemd --with-systemdsystemunitdir=%{_unitdir} --sysconfdir=%{_sysconfdir}/%{name}/ --with-systemdenvfile=%{_sysconfdir}/sysconfig/%{name}

# update SOURCE5 on maintainer's machine prior commiting, there's no internet connection on builders
%make_build update-smart-drivedb
./update-smart-drivedb -s - -u sf drivedb.h ||:
cp drivedb.h %{SOURCE5} ||:

%make_build CXXFLAGS="$RPM_OPT_FLAGS -fpie" LDFLAGS="-pie -Wl,-z,relro,-z,now"

%if 0%{?with_selinux}
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif


%install
%make_install

rm -f examplescripts/Makefile*
chmod a-x -R examplescripts/*
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/smartmontools
install -D -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/smartdnotify
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/smartd_warning.d
rm -rf $RPM_BUILD_ROOT/etc/{rc.d,init.d}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}

%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%endif

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   # the daemon needs to be restarted for the custom label to be applied
   %systemd_postun_with_restart smartd.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
    # the daemon needs to be restarted for the custom label to be removed
    %systemd_postun_with_restart smartd.service
fi
%endif

%preun
%systemd_preun smartd.service

%post
%systemd_post smartd.service

%postun
%systemd_postun_with_restart smartd.service

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%doc TODO examplescripts smartd.conf
%license COPYING
%dir %{_sysconfdir}/%name
%dir %{_sysconfdir}/%name/smartd_warning.d
%config(noreplace) %{_sysconfdir}/%{name}/smartd.conf
%config(noreplace) %{_sysconfdir}/%{name}/smartd_warning.sh
%config(noreplace) %{_sysconfdir}/sysconfig/smartmontools
%{_unitdir}/smartd.service
%{_sbindir}/smartd
%{_sbindir}/update-smart-drivedb
%{_sbindir}/smartctl
%{_mandir}/man?/smart*.*
%{_mandir}/man?/update-smart*.*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_sharedstatedir}/%{name}

%files selinux
%license COPYING
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed May 14 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:7.5-2
- fix automation updating drivedb and update it (rhbz#2366204)

* Wed Apr 30 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:7.5-1
- updated to 7.5

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:7.4-7
- Rebuilt for the bin-sbin merge (2nd attempt)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:7.4-5
- Rebuilt for the bin-sbin merge

* Tue Mar 26 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:7.4-4
- drop i686 build as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Alessandro Astone <ales.astone@gmail.com> - 1:7.4-2
- Amend SELinux to run hostname in its domain

* Tue Aug 01 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:7.4-1
- updated to 7.4

* Fri Jul 21 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-9
- more selinux changes

* Fri Jul 21 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-8
- use new selinux context for smartdnotify

* Thu Jul 20 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-7
- use different selinux context for notification scripts (#2139199)

* Wed Apr 05 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-6
- update license tag format (SPDX migration) for https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_1

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-4
- fix selinux directory permissions

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-2
- use --capabilities=mail for exim mail notification (#2060526)

* Tue Mar 01 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3-1
- updated to 7.3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-11
- fix /dev/megaraid_sas_ioctl_node mknode permissions (#1936824)

* Mon Aug 23 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-10
- more selinux fixes

* Mon Aug 16 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-9
- selinux should allow access to nvme devices (#1990463)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-7
- make notification work with capabilities (#1954015)

* Wed Apr 28 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-6
- simplify selinux policy path for ci tests

* Mon Apr 19 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-5
- add selinux sub-package

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:7.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-2
- make sure correct version of drivedb.h is used (#1918946)

* Mon Jan 18 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.2-1
- smartmontools updated to 7.2

* Mon Jan 18 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:7.1-10
- use capabilites by default

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Michal Hlavinka <mhlavink@redhat.com> - 1:7.1-7
- smartmontools updated to 7.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Daniel Axelrod <daxelrod@datto.com> - 1:7.0-6
- Remove unused patches
- Drop pre script for migrating from unsupported Fedora versions
- Replace sed with configure switch

* Wed Apr 03 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:7.0-5
- revert smartd_warning related changes

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:7.0-3
- update default config

* Thu Jan 03 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:7.0-2
- use smartd_warning plugin to notify users (bug #1647534)
- spec cleanup

* Thu Jan 03 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:7.0-1
- smartmontools updated to 7.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Michal Hlavinka <mhlavink@redhat.com> - 1:6.6-4
- add gcc-c++ buildrequire

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:6.6-2
- Remove old crufty coreutils requires

* Mon Nov 06 2017 Michal Hlavinka <mhlavink@redhat.com> - 1:6.6-1
- smartmontools updated to 6.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:6.5-2
- enable location for persistence data(#1291928)

* Mon May 09 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:6.5-1
- smartmontools updated to 6.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:6.4-3
- it is no longer necessary to do utf-8 conversion of the AUTHORS and ChangeLog (#1228825)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:6.4-1
- smartmontools updated to 6.4

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:6.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 14 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:6.3-3
- do not require sendmail

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:6.3-1
- smartmontools updated to 6.3

* Thu Jul 17 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2-7
- update drivedb database (#954162)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2-5
- require /usr/sbin/sendmail as MTA is not provided by all packages (#1048618)

* Tue Apr 15 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2-4
- use MTA instead of sendmail as a requirement (#1048614)

* Thu Apr 10 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2-3
- add mail requires (#1048614)

* Mon Sep 16 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2-2
- smartd service file wrong path to environment file (#998225)

* Tue Jul 30 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2-1
- smartmontools updated to 6.2

* Mon Jul 22 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:6.1-2
- spec cleanup

* Wed Mar 20 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:6.1-1
- smartmontools updated to 6.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Michal Hlavinka <mhlavink@redhat.com> - 1:6.0-1
- smartmontools updated to 6.0

* Tue Aug 21 2012 Michal Hlavinka <mhlavink@redhat.com> - 1:5.43-3
- use new systemd rpm macros (#850316)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Michal Hlavinka <mhlavink@redhat.com> - 1:5.43-1
- smartmontools updated to 5.43

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.42-2
- enable smartd after installation

* Fri Oct 21 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.42-1
- smartmontools updated to 5.42

* Mon Jun 13 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.41-2
- make F-14 (sysv init) -> F-15 (systemd) transition more robust

* Fri Jun 10 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.41-1
- updated to 5.41

* Mon May 16 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-10
- fix path to notify script (#675778)

* Fri Mar 11 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-9
- fix typos in man page

* Fri Mar 04 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-8
- don't call chkconfig add, we use systemd now
 
* Thu Mar 03 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-7
- own %%{_datadir}/%%{name} and %%{_libexecdir}/%%{name} dirs

* Thu Feb 17 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-6
- notify users when disk is failing

* Wed Feb 09 2011 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-5
- move to systemd

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-3
- megaraid: Fix segfault on non-data commands (#577935)

* Tue Nov 09 2010 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-2
- don't forget to restart smartd service after update (#651211)

* Mon Oct 18 2010 Michal Hlavinka <mhlavink@redhat.com> - 1:5.40-1
- updated to 5.40 final

* Mon Sep 27 2010 Michal Hlavinka <mhlavink@redhat.com> - 1:5.39.1-2.r3169
- updated to r3169
- ddds riverdb support for new devices (#637171)

* Fri Jan 29 2010 Michal Hlavinka <mhlavink@redhat.com> - 1:5.39.1-1
- updated to 5.39.1
- Fix spin-up of SATA drive if '-n standby' is used.

* Wed Jan 20 2010 Michal Hlavinka <mhlavink@redhat.com> - 1:5.39-2
- fix DEVICESCAN -d sat
- fix directive '-l selftest'
- fix option '-q, --quietmode'

* Thu Dec 10 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.39-1
- update to 5.39

* Wed Dec 02 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.39-0.1.rc1
- update to 5.39-rc1

* Wed Nov 25 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-25.20091119svn
- spec cleanup

* Mon Nov 23 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-24.20091119svn
- move powermode option from sysconfig to smartd.conf (#539760)

* Thu Nov 19 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-23.20091119svn
- update to svn snapshot 2009-11-19
- remove upstreamed patches

* Mon Nov 02 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-22
- spec cleanup

* Mon Oct 12 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-21 
- warn about disabled mail only if capabilities are enabled

* Fri Oct 09 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-20
- fix init script for case when no action was specified

* Fri Oct 09 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-19
- make init script lsb compliant (#528016)

* Mon Oct 05 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-18
- bump release for rebuild

* Mon Oct 05 2009 Michal Hlaivnka <mhlavink@redhat.com> - 1:5.38-17
- make capabilities optional
- fix capabilities for 3ware contollers (#526626)

* Wed Aug 26 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-16
- extend capability scanning devices

* Wed Aug 26 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-15
- updated patch for lower capabilities (#517728)
- added buildrequires libcap-ng-devel

* Fri Aug 21 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-14
- drop all unnecessary capabilities (#517728)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.38-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-12
- drop autogen call 

* Sat Apr 11 2009 Dennis Gilmore <dennis@ausil.us> - 1:5.38-11
- remove ExclusiveArch use -fPIE on sparc64  
- tested builds on sparcv9 sparc64 and s390x

* Mon Mar 09 2009 Michal Hlavinka <mhlavink@redhat.com> - 1:5.38-10
- cleanup for merge review

* Fri Feb 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:5.38-9
- fix ExclusiveArch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-7
- fix #458549 - obsolete smartmontools-config
- change the default configuration file

* Fri Aug 08 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-6
- correct CXXFLAGS so the PIE code is produced

* Mon May 12 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-5
- remove config subpackage

* Mon May 05 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-4.1
- add libselinux-devel to BR

* Mon May 05 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-4
- fix #232218 character devices /dev/twa* for 3ware 9000 series RAID
  controllers are not created

* Thu Mar 27 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-3
- don't attempt to query DELL PERC controllers -- they'd go offline

* Tue Mar 18 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-2
- fix FD_CLOEXEC on SCSI device file descriptors not being set

* Mon Mar 10 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.38-1
- new upstream version

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-8.5
- rebuild (gcc-4.3)

* Tue Jan 15 2008 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-8.4
- change '-d ata' to '-d sat' in the config script for SATA drives

* Wed Dec 12 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-8.3
- fix #375791 - parameter warning for smartd in logwatch output

* Wed Oct 31 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-8.2
- rebuild (one more error in autogen.sh)

* Wed Oct 31 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-8.1
- fix build with new automake

* Wed Oct 31 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-8
- fix #359561 - typo in smartd-conf.py causes smartd to skip all disks

* Mon Oct 15 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-7.1
- improved patch for getaddrinfo

* Fri Oct 12 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-7
- replace gethostbyname with getaddrinfo

* Tue Sep 04 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-6
- fix #271741 - smartd-conf.py should allow customization of parameters
- fix #253753 - service starting by default, perhaps shouldn't
- update initscript (related #247058 - initscript review)

* Mon Aug 20 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-5
- add support for 24 disks on 3ware RAID controllers (related #252055)
- fix #245442 - add %%{arm} to smartmontools's set of build archs
- update license tag

* Thu Jun 21 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-4
- fix #241389 - smartd-conf.py pulls in a big dependency chain, so
  build a separate config package
  
* Tue Jun 05 2007 Tomas Smetana <tsmetana@redhat.com> - 1:5.37-3
- fix #241385 - smartmontools missing dependency on mailx
- fix #241388 - unneeded smartd-conf.py[co] installed in /usr/sbin

* Wed Mar  7 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 1:5.37-2
- re-add cloexec patch
- re-add one erased changelog entry
- compile with -fpie (instead of -fpic)

* Tue Feb 27 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 1:5.37-1
- new upstream version

* Thu Feb 22 2007 Tomas Mraz <tmraz@redhat.com> - 1:5.36-8
- enable SMART on disks when smartd-conf.py runs (fix
  by Calvin Ostrum) (#214502)

* Mon Feb 12 2007 Tomas Mraz <tmraz@redhat.com> - 1:5.36-7
- redirect service script output to null (#224566)

* Sun Feb 11 2007 Florian La Roche <laroche@redhat.com> - 1:5.36-6
- make sure the preun script does not fail

* Tue Nov  7 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.36-5
- set cloexec on device descriptor so it doesn't leak to sendmail (#214182)
- fixed minor bug in initscript (#213683)
- backported SATA disk detection from upstream

* Fri Aug 18 2006 Jesse Keating <jkeating@redhat.com> - 1:5.36-3
- rebuilt with latest binutils to pick up 64K -z commonpagesize on ppc*
  (#203001)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:5.36-2.1
- rebuild

* Tue Jun 27 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.36-2
- kudzu is deprecated, replace it with HAL (#195752)
- moved later in the boot process so haldaemon is already running
  when drives are being detected

* Thu May 11 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.36-1
- new upstream version
- included patch with support for cciss controllers (#191288)

* Tue May  2 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.33-8
- regenerate smartd.conf on every startup if the config file
  is autogenerated (#190065)

* Fri Mar 24 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.33-7
- add missing quotes to /etc/sysconfig/smartmontools

* Wed Mar 22 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.33-6
- test SATA drives correctly

* Wed Mar 22 2006 Tomas Mraz <tmraz@redhat.com> - 1:5.33-5
- add default /etc/sysconfig/smartmontools file
- ignore errors on startup (#186130)
- test drive for SMART support before adding it to smartd.conf

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:5.33-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:5.33-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 16 2005 Tomas Mraz <tmraz@redhat.com> 1:5.33-4
- mail should be sent to root not root@localhost (#174252)

* Fri Nov 25 2005 Tomas Mraz <tmraz@redhat.com> 1:5.33-3
- add libata disks with -d ata if the libata version
  is new enough otherwise do not add them (#145859, #174095)

* Thu Nov  3 2005 Tomas Mraz <tmraz@redhat.com> 1:5.33-2
- Spec file cleanup by Robert Scheck <redhat@linuxnetz.de> (#170959)
- manual release numbering
- remove bogus patch of non-installed file
- only non-removable drives should be added to smartd.conf
- smartd.conf should be owned (#171498)

* Tue Oct 25 2005 Dave Jones <davej@redhat.com>
- Add comments to generated smartd.conf (#135397)

* Thu Aug 04 2005 Karsten Hopp <karsten@redhat.de>
- package all python files

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Wed Feb  9 2005 Dave Jones <davej@redhat.com>
- Build on PPC32 too (#147090)

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils.

