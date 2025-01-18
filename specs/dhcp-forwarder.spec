Summary: DHCP relay agent
Name: dhcp-forwarder
Version: 0.11
Release: 23%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: http://www.nongnu.org/dhcp-fwd/
Source0: http://savannah.nongnu.org/download/dhcp-fwd/%name-%version.tar.xz
Source1: http://savannah.nongnu.org/download/dhcp-fwd/%name-%version.tar.xz.asc
Source2: dhcp-forwarder.service

BuildRequires:  gcc
BuildRequires: systemd-units
BuildRequires: make
Requires(post): coreutils bash systemd
Requires(preun): systemd
Requires(postun): systemd

# required to update the old packages which had init system sub packages
Obsoletes: dhcp-forwarder-systemd

%description
dhcp-fwd forwards DHCP messages between subnets with different sublayer
broadcast domains. It is similar to the DHCP relay agent dhcrelay of
ISC's DHCP, but has the following important features:

* Runs as non-root in a chroot-environment
* Uses AF_INET sockets which makes it possible to filter incoming
  messages with packetfilters
* The DHCP agent IDs can be defined freely
* Has a small memory footprint when using dietlibc

%prep
%setup -q

%build
%configure \
 --enable-release \
 --with-systemd-unitdir=%_unitdir \
 --disable-dietlibc

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{_sharedstatedir}/dhcp-fwd \
 %{buildroot}/%{_unitdir} %{buildroot}/%{_sysconfdir}
make DESTDIR=%{buildroot} install
install %{SOURCE2} %{buildroot}/%{_unitdir}/dhcp-forwarder.service
install contrib/dhcp-fwd.conf %{buildroot}/%{_sysconfdir}

%check
make check

%pre
getent group dhcp-fwd >/dev/null || groupadd -r dhcp-fwd
getent passwd dhcp-fwd >/dev/null || \
    useradd -r -g dhcp-fwd -d %{_sharedstatedir}/dhcp-fwd -s /sbin/nologin \
    -c "DHCP Forwarder user" dhcp-fwd
exit 0

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %attr(0755,root,root) %{_sharedstatedir}/dhcp-fwd
%_sbindir/*
%_mandir/*/*
%attr(0644,root,root) %{_unitdir}/dhcp-forwarder.service
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/dhcp-fwd.conf

%post
%systemd_post dhcp-forwarder.service

%preun
%systemd_preun dhcp-forwarder.service

%postun
%systemd_postun_with_restart dhcp-forwarder.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11-13
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 20 2016 Paul Wouters <pwouters@redhat.com> - 0.11-1
- Upgrade to 0.11
- Remove non-fedora hacks from spec file
- Resolves: rhbz#856667 Introduce new systemd-rpm macros in dhcp-forwarder spec file
- Rename systemd service (which never worked) dhcp-fwd.service to dhcp-forwarder.service

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-1909
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-1908
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-1907
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-1906
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-1905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 0.10-1904
- Migrate from fedora-usermgmt to guideline scriptlets.

* Tue Apr 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.10-1903
- Switch from dietlibc to glibc.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-1902
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.10-1901
- rebuilt

* Sun Aug 19 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.10-1900
- disabled upstart
- removed old sysv cruft

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-1801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.10-1800
- updated to 0.10; fixed build in recent environemnts (#817292)
- removed local systemd unit; it is shipped upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-1502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-1501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.9-1500
- updated to 0.9
- fixed source url and switched to .xz tarball
- added systemd initscripts and disabled generation of the old sysv ones
- minor specfile cleanups
- updated upstart script to wait for SIGSTOP

* Sun Dec  6 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8-1300
- updated -upstart to upstart 0.6.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  1 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8-4
- added upstart %%scriplets

* Sun Mar  1 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8-3
- added -upstart subpackage
- renamed -sysv subpackage to -sysvinit to make -upstart win the
  default dependency resolving

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8-1
- updated to 0.8
- license is now GPLv3, not GPLv2

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7-15
- fix license tag

* Fri Feb 22 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-14
- rebuilt with new dietlibc

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7-13
- Autorebuild for GCC 4.3

* Thu Jan 18 2007 David Woodhouse <dwmw2@infradead.org> 0.7-12
- rebuilt with PPC support

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.7-11
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-10
- rebuilt

* Sun Jul  9 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-9
- rebuilt with dietlibc-0.30
- use new fedora-usermgmt code
- use %%bcond_* macros

* Mon Feb 20 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-8
- exclude PPC arch because dietlibc is not available there anymore

* Wed Jun  8 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-7
- do not build against dietlibc on non-i386 archs running FC3
- added sanity check for builds with mach
- buildrequire 'which'

* Thu May 19 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-4
- use %%dist instead of %%disttag

* Sun Mar  6 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7-2
- fixed bigendian builds (backported from 0.8)
- s!%%define!%%global! to workaround bugs in rpm's macro-engine

* Thu Nov 11 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.7-0.fdr.1
- fedora'ized it

* Thu Aug 19 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.6.1-0
- added support for 'fedora-usermgmt' (enabled with '--with fedora' switch)

* Thu Jun 17 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.6.1-0
- conditionalized build of -minit subpackage

* Thu Aug  7 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.5.1-0
- added minit support
- removed superfluous %%doc attribute of %%_mandir entries
- removed superfluous curlies
- use 'install-contrib' and cleaned up %%install section
- moved /etc/sysconfig/* file into -sysv subpackage; it is not used by
  -minit anymore
- minor cleanups

* Wed Jul 30 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.5-0.fdr.1
- updated to version 0.5

* Tue May 27 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4-0.fdr.2
- create and remove group explicitely
- s/adduser/useradd/
- removed dependency on initscripts by calling the service-script in
  the %%post/%%preun scriptlets directly
- do not call '--install-contrib' anymore; it creates too much
  clutter to make sure that the initscripts will be installed into
  %%_initrddir but not in /etc/init.d. Instead of, install the
  scripts manually.

* Fri May  2 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4-0.fdr.1
- cleanups
- applied fedora.us naming scheme

* Wed Aug 28 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.3.1-1
- Added /etc/sysconfig/dhcp-fwd file

* Fri Jul 12 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.2.5-2
- Renamed username from dhcpfwd to dhcp-fwd
- Adjusted URL

* Fri Jul 12 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.2.5-1
- version 0.2.5
- Fixed some typos
- Added some PreReq's
- Enhanced %%postun script

* Mon Jun 17 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.2-2
- Described purpose of the %%homedir and its handling

* Fri Jun 14 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.2-1
- Added manpage

* Thu Jun 13 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.1-0.3
- Added --without dietlibc option

* Sat Jun  1 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- Initial build.
