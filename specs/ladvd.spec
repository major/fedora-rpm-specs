
%define selinux_variants mls strict targeted
%define modulename ladvd

Name:           ladvd
Version:        1.1.4
Release:        2%{?dist}
Summary:        CDP/LLDP sender for UNIX

License:        ISC
URL:            http://www.blinkenlights.nl/software/ladvd/
Source0:        https://github.com/sspans/ladvd/archive/v%{version}.tar.gz
Source1:        %{name}.conf.sysusers
# 2016-11 TODO: rewrite selinux policy using CIL
Source3:        %{modulename}.te
Source4:        %{modulename}.fc
Source5:        %{modulename}.if

Recommends:	%{name}-selinux

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libevent-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libpcap-devel
BuildRequires:  libteam-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  systemd

%{?systemd_requires}

%description
ladvd uses CDP / LLDP frames to inform switches about connected hosts, which
simplifies Ethernet switch management. Every 30 seconds it will transmit CDP/
LLDP packets reflecting the current system state. Interfaces (bridge, bonding,
wireless), capabilities (bridging, forwarding, wireless) and addresses (IPv4,
IPv6) are detected dynamically.


%package selinux
Summary:        SELinux policy module supporting %{name}
BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
%if "%{_selinux_policy_version}" != ""
Requires:       selinux-policy >= %{_selinux_policy_version}
%endif
Requires:       %{name} = %{version}-%{release}
Requires(post):   /usr/sbin/semodule, /sbin/restorecon
Requires(postun): /usr/sbin/semodule, /sbin/restorecon


%description selinux
SELinux policy module supporting %{name}


%prep
%setup -q
mkdir SELinux
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} SELinux

%build
autoreconf -fi
%configure \
        --with-user=ladvd \
        --with-pid-dir=%{_rundir}
make %{?_smp_mflags}

cd SELinux
for selinuxvariant in %{selinux_variants}
do
make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
mv %{modulename}.pp %{modulename}.pp.${selinuxvariant}
make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_docdir}/ladvd
mkdir -p %{buildroot}%{_unitdir}
install -m 0444 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf


cd SELinux
for selinuxvariant in %{selinux_variants}
do
install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
install -p -m 644 %{modulename}.pp.${selinuxvariant} \
%{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp
done
cd -

/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux


%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%post selinux
for selinuxvariant in %{selinux_variants}
do
/usr/sbin/semodule -s ${selinuxvariant} -i \
%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp &> /dev/null || :
done

%postun selinux
if [ $1 -eq 0 ] ; then
for selinuxvariant in %{selinux_variants}
do
/usr/sbin/semodule -s ${selinuxvariant} -r %{modulename} &> /dev/null || :
done
fi

%files
%doc doc/README doc/TODO
%license doc/LICENSE
%{_sbindir}/%{name}
%{_sbindir}/%{name}c
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}c.8*
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf


%files selinux
%doc SELinux/*
%{_datadir}/selinux/*/%{modulename}.pp


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 04 2025 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.4-1
- New version 1.1.4 (rhbz#2335498)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-16
- verified SPDX license tag
- allow using netlink generic socket in SELinux policy (patch from Zdenek Pytela)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-12
- remove old trigerun

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.2-12
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-10
- rebuild for libevent soname change

* Wed Aug 05 2020 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-9
- further SELinux fixes (rhbz#1855163 and other stuff)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-7
- fixes to SELinux policy from Milos Malik (rhbz#1834325)
- /var/run → /run cleanup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-4
- fix FTBFS due to changed hardlink location (rhbz#1721950)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.2-1
- update to latest 1.1.2 (rhbz#1554568)
- use newer sysuser create macro

* Mon Feb 19 2018 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.1-5
- rebuilt for libevent soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.1-1
- bump to latest release (rhbz#1460436)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 23 2016 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.0-6
- enable on TUN/TAP devices; this way KVM virtual machines become visible by default.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.0-4
- Fix ladvd SELinux policy. Removed wrong allow rules and replaced it with correct macros.
  Patch from Lukas Vrabec <lvrabec@redhat.com> (fixes rhbz#1248395)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.0-2
- use systemd-sysusers to create 'ladvd' user

* Mon Apr 20 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.1.0-1
- new upstream version: https://github.com/sspans/ladvd/releases/tag/v1.1.0
- drop custom systemd unit, upstream was updated

* Tue Oct 14 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-14
- replace tmpfiles snippet with RuntimeDirectory=

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-11
- further SELinux policy fixes (#1018493, #1018497, #1018502, #1018503, #1018504, #1018505, #1018506)

* Tue Sep 17 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-10
- use macro for determining SELinux policy version

* Tue Sep 17 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-9
- apply SELinux policy patch by Daniel J Walsh (#975959)

* Mon Aug 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.4-8
- Address FTBFS, RHBZ#992031:
  - Fix typo in spec (Use %%_tmpfilesdir instead of ${_tmpfilesdir}).
  - Use %%{?systemd_requires} instead of %%{systemd_requires}.

* Mon Aug 05 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-7
- add BR: systemd, as it not longer pulled by default
  (https://lists.fedoraproject.org/pipermail/devel/2013-August/187299.html)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-5
- remove unnecessary parts for -selinux posts
- selinux policy: allow /etc/passwd read to find out about unpriviledged user (#975959)
- modernize tmpfiles snippets

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.4-4
- Migrate from fedora-usermgmt to guideline scriptlets.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-2
- add m4 to buildreq
- switch to systemd macros
- remove chkconfig from fedora package

* Wed Nov 07 2012 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.4-1
- create chroot() dir on package install
- update to vesion 1.0.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.2-1
- new upstream version

* Tue Jan 24 2012 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.0.0-1
- version 1.0.0
- spec: 
  - drop patch for GCC issue fixed upstream
  - drop BuildRoot: tag
- unit file: 
  - remove StandardOutput=syslog (it is default now)
  - add "-z" option, to have upstream switch name put in interface's ifAlias

* Mon Aug 15 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.9.2-6
- remove sysconfig mention from unit file

* Sat Aug 13 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.9.2-5
- place tmpfiles.d conf in /usr/lib/tmpfiles.d
- drop SysV init script and sysconfig file

* Fri May 6 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.9.2-4
- Fix systemd-related scriptlets (from Bill Nottingham):

    - since we install a systemd service file, run 'systemctl daemon-reload'
    - chkconfig without a level forwards to systemctl, which is not useful for
      SysV migrations. Pass an explicit level.

* Sun Feb 13 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.9.2-3
- fix FTBFS caused by -Werror=unused-but-set-variable 

* Sun Feb 13 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.9.2-2
- provide systemd and tmpfiles integration bits

* Sun Feb 13 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.9.2-1
- new upstream version 0.9.2
- package ladvdc - client command
- simplify initscript, rely on protocol autodetection like upstream suggests
- move homedir to /var/run/ladvd

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 26 2009 Andreas Thienemann <andreas@bawue.net> - 0.8-1
- Rebase to new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Andreas Thienemann <andreas@bawue.net> 0.6.1-2
- Added SElinux support package
- Added patch to make it build on EL-4
- Added separate ladvd user

* Sat Oct 18 2008 Andreas Thienemann <andreas@bawue.net> 0.6.1-1
- Initial package
