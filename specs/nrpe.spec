%define nsport 5666

%global commit 4f7dd1199f1f3f72f9197e8565da339a4a2490b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commdate 20200423
%global fromgit 0

Name: nrpe
Version: 4.1.3
%if 0%{?fromgit}
Release: 2%{?dist}
%else
Release: 2%{?dist}
%endif
Summary: Host/service/network monitoring agent for Nagios

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://www.nagios.org
%if 0%{?fromgit}
Source0: https://github.com/NagiosEnterprises/nrpe/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0: https://github.com/NagiosEnterprises/nrpe/archive/%{name}-%{version}.tar.gz
%endif
Source1: nrpe.sysconfig
Source2: nrpe-tmpfiles.conf
Source3: nrpe.README.SELinux.rst
Source5: nrpe_epel7.te
Source6: nrpe_epel.fc
Source7: nrpe.service.epel

Patch3: nrpe-0003-Include-etc-npre.d-config-directory.patch
Patch5: nrpe-0005-systemd-service.patch
Patch6: nrpe-configure-c99.patch

# For reconfiguration
BuildRequires: make
BuildRequires: autoconf, automake, libtool
BuildRequires: gcc
BuildRequires: checkpolicy, selinux-policy-devel
BuildRequires: systemd-units
BuildRequires: openssl, openssl-devel
%if 0%{?fedora} >= 40
BuildRequires: openssl-devel-engine
%endif

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
BuildRequires: tcp_wrappers-devel
%endif

Requires(pre): %{_sbindir}/useradd, %{_sbindir}/usermod

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# owns /etc/nagios
Requires: nagios-common
Provides: nagios-nrpe = %{version}-%{release}

%description
Nrpe is a system daemon that will execute various Nagios plugins
locally on behalf of a remote (monitoring) host that uses the
check_nrpe plugin. Various plugins that can be executed by the
daemon are available at:
http://sourceforge.net/projects/nagiosplug

This package provides the core agent.

%package -n nagios-plugins-nrpe
Summary: Provides nrpe plugin for Nagios
Requires: nagios-plugins
Provides: check_nrpe = %{version}-%{release}

%description -n nagios-plugins-nrpe
Nrpe is a system daemon that will execute various Nagios plugins
locally on behalf of a remote (monitoring) host that uses the
check_nrpe plugin. Various plugins that can be executed by the
daemon are available at:
http://sourceforge.net/projects/nagiosplug

This package provides the nrpe plugin for Nagios-related applications.

%if 0%{?rhel} > 5
%package selinux
Summary:          SELinux context for %{name}
Requires:         %name = %version-%release
Requires(post):   policycoreutils
Requires(postun): policycoreutils


%description selinux
SElinux context for %{name}.
%endif

%prep
%if 0%{fromgit}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{name}-%{version}
%endif

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{?__global_ldflags}" \
%configure \
    --with-nrpe-port=%{nsport} \
    --with-nrpe-user=nrpe \
    --with-nrpe-group=nrpe \
    --with-piddir=/run/nrpe \
    --bindir=%{_sbindir} \
    --libdir=/doesnt/matter/ \
    --libexecdir=%{_libdir}/nagios/plugins \
    --datadir=%{_datadir}/nagios \
    --sysconfdir=%{_sysconfdir}/nagios \
    --localstatedir=%{_localstatedir}/run/ \
    --enable-command-args

make %{?_smp_mflags} all

%if 0%{?rhel} > 5
## SELinux configs
mkdir selinux
install -pm 644 %{SOURCE3} README.SELinux.rst
cp -p %{SOURCE5} selinux/%{name}_epel.te
cp -p %{SOURCE6} selinux/%{name}_epel.fc
touch selinux/%{name}_epel.if
make -f %{_datadir}/selinux/devel/Makefile
%endif

%install
%if 0%{?el7}
## If we are EL7 we want the home crafted systemd service due to problems
install -D -m 0644 -p %{SOURCE7} %{buildroot}%{_unitdir}/%{name}.service
%else
## If we are Fedora we want the upstream systemd service file
install -D -m 0644 -p startup/default-service %{buildroot}%{_unitdir}/%{name}.service
%endif
install -D -p -m 0644 sample-config/nrpe.cfg %{buildroot}/%{_sysconfdir}/nagios/%{name}.cfg
install -D -p -m 0755 src/nrpe %{buildroot}/%{_sbindir}/nrpe
install -D -p -m 0755 src/check_nrpe %{buildroot}/%{_libdir}/nagios/plugins/check_nrpe
install -D -p -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -d %{buildroot}%{_sysconfdir}/nrpe.d
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%if 0%{?rhel} > 5
# Selinux configs
install -p -m 644 -D %{name}_epel.pp $RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{name}/%{name}_epel.pp
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
%{_sbindir}/useradd -c "NRPE user for the NRPE service" -d %{_localstatedir}/run/%{name} -r -g %{name} -s /sbin/nologin %{name} 2> /dev/null || :
getent group nagios >/dev/null && %{_sbindir}/usermod -a -G nagios %{name} || :

%preun
%systemd_preun nrpe.service

%post
%systemd_post nrpe.service

%postun
%systemd_postun_with_restart nrpe.service

%if 0%{?rhel} > 5
%post selinux
if [ "$1" -le "1" ]; then # First install
   semodule -i %{_datadir}/selinux/packages/%{name}/%{name}_epel.pp 2>/dev/null || :
   fixfiles -R %{name} restore || :
   %systemd_postun_with_restart %{name}.service
fi
%endif

%if 0%{?rhel} > 5
%preun selinux
if [ "$1" -lt "1" ]; then # Final removal
    semodule -r %{name}_epel 2>/dev/null || :
    fixfiles -R %{name} restore || :
    %systemd_postun_with_restart %{name}.service
fi
%endif

%if 0%{?rhel} > 5
%postun selinux
if [ "$1" -ge "1" ]; then # Upgrade
    # Replaces the module if it is already loaded
    semodule -i %{_datadir}/selinux/packages/%{name}/%{name}_epel.pp 2>/dev/null || :
    # no need to restart the daemon
fi
%endif

%files
%{_unitdir}/%{name}.service
%{_sbindir}/nrpe
%dir %{_sysconfdir}/nrpe.d
%config(noreplace) %{_sysconfdir}/nagios/nrpe.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_tmpfilesdir}/%{name}.conf
%license LICENSE.md
%doc CHANGELOG.md LEGAL README.md README.SSL.md SECURITY.md docs/NRPE.pdf
%dir %attr(775, %{name}, %{name}) %{_localstatedir}/run/%{name}

%files -n nagios-plugins-nrpe
%{_libdir}/nagios/plugins/check_nrpe
%license LICENSE.md
%doc CHANGELOG.md LEGAL README.md

%if 0%{?rhel} > 5
%files selinux
%doc README.SELinux.rst
%{_datadir}/selinux/packages/%{name}/%{name}_epel.pp
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.1.3-1
- Update to upstream.

* Tue Dec 10 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.1.2-2
- Use openssl-devel-engine only on Fedora

* Tue Dec 10 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.1.2-1
- Update to upstream

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.0-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec  3 2022 Florian Weimer <fweimer@redhat.com> - 4.1.0-3
- Port configure script to C99

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.1.0-1
- Update to upstream
- Hardened build is default for Fedora 23+

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Xavier Bachelot <xavier@bachelot.org> - 4.0.3-10
- Drop EL6 support
- Fix EL9 build
- Use %%license

* Thu Nov 11 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.0.3-9
- Don't use get_dh on Fedora 36 - OpenSSL 3. (bz#2021958)
- Remove unknown --with-init-dir configure parameter.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.0.3-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 11 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.0.3-6
- Fix build for EPEL7.

* Tue Mar 09 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.0.3-5
- Wait for network-online.target (bz#1898469).
- Apply /etc/sysconfig/nrpe settings (bz#1806659).
- Changed /var/run to /run (bz#1870146).

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.0.3-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Martin Jackson <mhjacks@swbell.net> - 4.0.1-1
- New upstream version

* Sun Apr 26 2020 Martin Jackson <mhjacks@swbell.net> - 4.0.2-3.20200423git4f7dd11
- Fix regression with nasty_metacharacters
- Update Patch3
- Drop patch13 (trees have diverged)

* Sun Apr  5 2020 Martin Jackson <mhjacks@swbell.net> - 4.0.2-2
- New upstream version
- Update patch for indlude_dir
- Fix BZ#1816816 - CVE-2020-6582 nrpe: heap-based buffer overflow due to a wrong integer type conversion
- Fix BZ#1816805 - CVE-2020-6581 nrpe: insufficient filtering and incorrect parsing of the configuration file may lead to command injection

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.1-9
- Try to make this work on el8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.1-6
- Fix BZ#1546264
- Fix potential FTBFS for gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.1-4
- Remove other el5 items. Update spec

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.1-3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.1-1
- Update to nrpe-3.2.1
- Fix BZ#1485361

* Fri Aug  4 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-6
- Found the problem. Fixed and ready to push

* Fri Aug  4 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-5
- Make sure nrpe works with different selinux names between 5,6 and 7
- For some reason the selinux module still does not install unless by force on EL6.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-4
- Forgot to up the release.

* Fri Jul 21 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-3
- Clean out nrpe.fc as that breaks silently

* Wed Jul 19 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-3
- Remove git from release name
- Fix selinux lines.

* Fri Jul 14 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-2git
- Remember to put in a patch so the /etc/nrpe.d/ is used.

* Fri Jul 14 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0
- Add patches for 321 openssl items
- Remove old patches no longer needed

* Tue Jul 11 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.1-6
- Put in fix for 1204683

* Tue Jul 11 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.1-5
- Add comments to nrpe.cfg to alert user on RHBZ #1318773
- Backport ipv6 patch for problem

* Fri Jul  7 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.1-4
- Fix patch name. Silly human. Do a fedpkg srpm before build.

* Fri Jul  7 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.1-3
- Fix crashing bug if username is not defined.

* Wed Jul  5 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.1-2
- Fix bug due to /etc/nrpe.d/ includes was above other defined entries BZ# 1467971
- I am not updating to 3.2.0 for a bit in order to smush out problems here.

* Wed Jun 14 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1
- Remove git patch
- Add pid_dir configure statement.

* Tue May  2 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.0-3
- Grab updates from upstream to see why nrpe fails on fedora but not rhel

* Wed Apr 26 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.0-2
- Move to using original nirik nrpe service file for systemd. It worked and the others dont
- NRPE fails to run using a /var/run/nrpe/ directory so trying to build without it.

* Thu Apr 20 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.0-1
- update to 3.1.0
- put in fix for format-error
- remove patches not needed.

* Thu Mar 23 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-6
- Redo the nagios policy to lower its all the permissions.

* Wed Mar 22 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-5
- Put in patches from GIT to fix noise problems
- Put in patch for RHEL6 systems to regain vars
- Put in initial patch for selinux on EPEL
- Remove el4 macros as this won't work there anyway.

* Fri Mar  3 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-5
- Remember to add the patch so it can build.

* Fri Mar  3 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-4
- Fix systemd to use correct service file.
- Add reload rule

* Fri Mar  3 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-3
- fix the systemd service file to better match needs.

* Fri Mar  3 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-2
- fix the statedir to look at /var/run/nrpe

* Mon Feb  6 2017 Stephen Smoogen <smooge@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1
- Add a temp patch to get it to work with openssl v110 for F25

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  8 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.15-7
- Use %%configure macro as it deals with config.sub/guess and various flags properly

* Fri Sep 04 2015 Scott Wilkerson <swilkerson@fedoraproject.org> - 2.15-6
- Fix spec file for missing /usr/share/libtool/config/config.guess

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 1 2014 Sam Kottler <skottler@fedoraproject.org> - 2.15.2
- Add patch to mitigate CVE-2014-2913

* Mon Jan 27 2014 Sam Kottler <skottler@fedoraproject.org> - 2.15.1
- Update to 2.15

* Wed Oct 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.14-5
- Allow building for aarch64 (rhbz #926244)
- Allow user to redefine default commands (rhbz #963703)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Kevin Fenzi <kevin@scrye.com> 2.14-3
- Apply patch from bug 860988 to handle RHEL versions and systemd
- Apply patch from bug 957567 to fix condrestart so nrpe restarts on upgrade.
- Rework systemd and service scriptlets and requires.
- Harden Fedora 19+ builds

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Mark Chappell <tremble@tremble.org.uk> - 2.14
- Version 2.14

* Mon Jan 14 2013 Mark Chappell <tremble@tremble.org.uk> - 2.13-2
- #860982 Mistake in service file
- #860985 nrpe shouldn't own /etc/nagios (from nagios-common)

* Mon Sep 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.13-1
- Ver. 2.13

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.12-19
- Disable systemd stuff in EPEL

* Sat Sep 17 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> - 2.12-18
- Let systemd create /var/run/nrpe. Fixes rhbz #656641

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 25 2010 Peter Lemenkov <lemenkov@gmail.com> - 2.12-16
- Issue with SELinux was resolved (see rhbz #565220#c25). 2nd try.

* Wed Sep 29 2010 jkeating - 2.12-15
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Peter Lemenkov <lemenkov@gmail.com> - 2.12-14
- Issue with SELinux was resolved (see rhbz #565220).

* Fri Jun 18 2010 Peter Lemenkov <lemenkov@gmail.com> - 2.12-13
- Init-script enhancements (see rhbz #247001, #567141 and #575544)

* Mon Oct 26 2009 Peter Lemenkov <lemenkov@gmail.com> - 2.12-12
- Do not own %%{_libdir}/nagios/plugins ( bz# 528974 )
- Fixed building against tcp_wrappers in Fedora ( bz# 528974 )

* Thu Sep 24 2009 Peter Lemenkov <lemenkov@gmail.com> - 2.12-11
- Fixed BZ# 515324

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.12-10
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Mike McGrath <mmcgrath@redhat.com> - 2.12-7
- Re-fix for 477527

* Mon Feb  2 2009 Peter Lemenkov <lemenkov@gmail.com> - 2.12-6
- Fixed BZ# 449174
- Clean up (in order to disable rpmlint warnings)

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 2.12-5
- rebuild with new openssl

* Sun Dec 21 2008 Mike McGrath <mmcgrath@redhat.com> - 2.12-4
- Added some doc lines for ticket 477527

* Fri Dec 19 2008 Mike McGrath <mmcgrath@redhat.com> - 2.12-3
- Added Provides: nagios-nrpe

* Fri Dec 19 2008 Mike McGrath <mmcgrath@redhat.com> - 2.12-2
- Upstreamreleased new version

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> - 2.7-6
- Rebuild for gcc43

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.7-5
 - Rebuild for deps

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> 2.7-4
- License Change
- Rebuild for BuildID

* Fri Feb 23 2007 Mike McGrath <mmcgrath@redhat.com> 2.7-1
- Upstream released new version

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 2.5.2-3
- no longer owns libdir/nagios
- buildrequires tcp_wrappers

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 2.5.2-2
- Specify bogus libdir so rpmlint won't complain

* Mon Jul 03 2006 Mike McGrath <imlinux@gmail.com> 2.5.2-1
- Upstream released new version

* Sun Mar 12 2006 Mike McGrath <imlinux@gmail.com> 2.4-3
- Added description to useradd statement

* Sun Mar 05 2006 Mike McGrath <imlinux@gmail.com> 2.4-2
- Added proper SMP build flags
- Added %%{?dist} tag
- Added reload to nrpe script
- Updated to 2.4, changes include:
- Added option to allow week random seed (Gerhard Lausser)
- Added optional command line prefix (Sean Finney)
- Added ability to reload config file with SIGHUP
- Fixed bug with location of dh.h include file
- Fixed bug with disconnect message in debug mode

* Sat Feb 04 2006 Mike McGrath <imlinux@gmail.com> 2.3-1
- Created a Fedora friendly spec file

* Mon Jan 23 2006 Andreas Kasenides ank<@>cs.ucy.ac.cy
- fixed nrpe.cfg relocation to sample-config
- replaced Copyright label with License
- added --enable-command-args to enable remote arg passing (if desired can be disabled by commenting out)

* Wed Nov 12 2003 Ingimar Robertsson <iar@skyrr.is>
- Added adding of nagios group if it does not exist.

* Tue Jan 07 2003 James 'Showkilr' Peterson <showkilr@showkilr.com>
- Removed the lines which removed the nagios user and group from the system
- changed the patch release version from 3 to 1

* Mon Jan 06 2003 James 'Showkilr' Peterson <showkilr@showkilr.com>
- Removed patch files required for nrpe 1.5
- Update spec file for version 1.6 (1.6-1)

* Sat Dec 28 2002 James 'Showkilr' Peterson <showkilr@showkilr.com>
- First RPM build (1.5-1)
