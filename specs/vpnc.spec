%define snapshot .svn550

Name:		vpnc
Version:	0.5.3
Release:	50%{snapshot}%{?dist}
Summary:	IPSec VPN client compatible with Cisco equipment
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.unix-ag.uni-kl.de/~massar/vpnc/

Source0:	http://www.unix-ag.uni-kl.de/~massar/vpnc/%{name}-%{version}%{snapshot}.tar.gz
Source1:	generic-vpnc.conf
Source2:	vpnc.consolehelper
Source3:	vpnc-disconnect.consolehelper
Source4:	vpnc.pam
Source5:	vpnc-helper
Source8:	%{name}-tmpfiles.conf
# script used to generate the svn snapshot, not used in the actual build process
Source99:	fetch-sources.sh

Patch1:		vpnc-0.5.1-dpd.patch
Patch2:		vpnc-0.5.3-use-autodie.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libgcrypt-devel > 1.1.90
BuildRequires:	gnutls-devel
# required for ./makeman.pl
BuildRequires:	perl-interpreter
BuildRequires:	perl(autodie)
BuildRequires:	perl(filetest)
BuildRequires:	perl(if)
BuildRequires: systemd
Requires:	iproute vpnc-script

%description
A VPN client compatible with Cisco's EasyVPN equipment.

Supports IPSec (ESP) with Mode Configuration and Xauth.  Supports only
shared-secret IPSec authentication, 3DES, MD5, and IP tunneling.

%package consoleuser
Summary:	Allows console user to run the VPN client directly
Requires:	vpnc = %{version}-%{release}
Requires:	usermode

%description consoleuser
Allows the console user to run the IPSec VPN client directly without
switching to the root account.

%prep
%autosetup

%build
CFLAGS="$RPM_OPT_FLAGS -fPIE" LDFLAGS="$RPM_OPT_FLAGS -pie" make PREFIX=/usr

%install
make install DESTDIR="$RPM_BUILD_ROOT" PREFIX=/usr
rm -f $RPM_BUILD_ROOT%{_bindir}/pcf2vpnc
chmod 0644 pcf2vpnc
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pcf2vpnc.1
chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man8/vpnc.8
install -m 0600 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/vpnc/default.conf
install -Dp -m 0644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/vpnc
install -Dp -m 0644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/vpnc-disconnect
install -Dp -m 0644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vpnc
install -Dp -m 0644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vpnc-disconnect
install -m 0755 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sbindir}/vpnc-helper
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -sf consolehelper $RPM_BUILD_ROOT%{_bindir}/vpnc
ln -sf consolehelper $RPM_BUILD_ROOT%{_bindir}/vpnc-disconnect
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/vpnc/COPYING
# vpnc-script is packaged in a separate package
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/vpnc/vpnc-script

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%files
%license COPYING
%doc README pcf2vpnc pcf2vpnc.1

%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/vpnc/default.conf
%{_sbindir}/vpnc
%{_bindir}/cisco-decrypt
%{_sbindir}/vpnc-disconnect
%{_mandir}/man8/vpnc.*
%{_mandir}/man1/cisco-decrypt.*

%files consoleuser
%config(noreplace) %{_sysconfdir}/security/console.apps/vpnc*
%config(noreplace) %{_sysconfdir}/pam.d/vpnc*
%{_bindir}/vpnc*
%{_sbindir}/vpnc-helper


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-50.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-49.svn550
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-48.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-47.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-46.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-45.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-44.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-43.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-42.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-41.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 0.5.3-40.svn550
- add missing perl dependencies for makeman.pl

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-39.svn550
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-38.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-37.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-36.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 0.5.3-35.svn550
- avoid legacy warning from systemd (rhbz 1691908)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-34.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug  2 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.3-33.svn550
- Spec updates: drop group, use %%license, drop initscipts

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-32.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-31.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-30.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-29.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-28.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-27.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-26.svn550
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Felix Schwarz <fschwarz@fedoraproject.org> - 0.5.3-25.svn550
- remove "-script" subpackage as this was split off (bz 1128147)

* Thu Nov 06 2014 Felix Schwarz <fschwarz@fedoraproject.org> - 0.5.3-24.svn550
- update to svn revision 550 (bz 1016215)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-23.svn457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-22.svn457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tomáš Mráz <tmraz@redhat.com> - 0.5.3-21.svn457
- Rebuild for new libgcrypt

* Fri Nov 15 2013 Paul Wouters <pwouters@redhat.com> - 0.5.3-20.svn457
- Actually patch the vpnc-script we ship with the unbound patch

* Mon Sep 23 2013 Paul Wouters <pwouters@redhat.com> - 0.5.3-19.svn457
- Add support for dynamically reconfiguring unbound DNS (rhbz#865092)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-18.svn457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar  7 2013 Tomáš Mráz <tmraz@redhat.com> - 0.5.3-17.svn457
- Make it build
- Remove vpnc-cleanup upstart configuration file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-16.svn457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-15.svn457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-14.svn457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 11 2011 Christian Krause <chkr@fedoraproject.org> - 0.5.3-13.svn457
- Use tmpfiles.d service to correctly handle /var/run/vpnc (#656719)
- Update vpnc-script:
  - fix negative MTU (#693235)
  - use restorecon to relabel /dev/net and /var/run/vpnc (#731382)
- Various minor spec file cleanup

* Thu Jul 21 2011 Dan Williams <dcbw@redhat.com> - 0.5.3-12.svn457
- Update to svn snapshot r457
- Enable support for Hybrid XAUTH (see rh #677419)

* Sat May 28 2011 David Woodhouse <David.Woodhouse@intel.com> - 0.5.3-11
- Update vpnc-script to cope with 'ipid' in route list.

* Sun Feb 27 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.3-10
- Move /etc/vpnc dir ownership to vpnc-script (#680783).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Dan Williams <dcbw@redhat.com> - 0.5.3-8
- Remove dependency on upstart since we use systemd now

* Wed Dec  9 2009 Bill Nottingham <notting@redhat.com> - 0.5.3-7
- Adjust for upstart 0.6

* Tue Nov 17 2009 David Woodhouse <David.Woodhouse@intel.com> - 0.5.3-6
- Update vpnc-script to support IPv6 properly

* Tue Nov  3 2009 David Woodhouse <David.Woodhouse@intel.com> - 0.5.3-5
- Split vpnc-script out into separate package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tomas Mraz <tmraz@redhat.com> - 0.5.3-2
- upgrade to new version
- fix race in vpnc-cleanup (#465315)

* Thu Jul 24 2008 Tomas Mraz <tmraz@redhat.com> - 0.5.1-6
- do not modify domain in resolv.conf (#446404)
- clean up modified resolv.conf on startup (#455899)

* Sat Apr  5 2008 Michal Schmidt <mschmidt@redhat.com> - 0.5.1-5
- vpnc-script: fix 'ip link ...' syntax.

* Thu Apr  3 2008 Tomas Mraz <tmraz@redhat.com> - 0.5.1-4
- drop autogenerated perl requires (#440304)
- compute MTU based on default route device (#433846)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.1-3
- Autorebuild for GCC 4.3

* Tue Nov 13 2007 Tomas Mraz <tmraz@redhat.com> - 0.5.1-2
- try to make DPD less sensitive (#345281)

* Thu Sep 20 2007 Tomas Mraz <tmraz@redhat.com> - 0.5.1-1
- upgrade to latest upstream

* Mon Sep  3 2007 Tomas Mraz <tmraz@redhat.com> - 0.4.0-4
- fix long standing bug causing problems on x86_64 (#232565) now for real

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> - 0.4.0-3
- license tag fix

* Tue Mar 20 2007 Tomas Mraz <tmraz@redhat.com> - 0.4.0-2
- -fstack-protector miscompilation on x86_64 is back (#232565)

* Mon Feb 26 2007 Tomas Mraz <tmraz@redhat.com> - 0.4.0-1
- upgrade to new upstream version

* Wed Jan 17 2007 Tomas Mraz <tmraz@redhat.com> - 0.3.3-15
- do not overwrite personalized vpnc scripts (#195842)
- we must not allow commandline options to vpnc when run through consolehelper

* Wed Jan 17 2007 Tomas Mraz <tmraz@redhat.com> - 0.3.3-14
- add consoleuser subpackage (#160571)
- fix permissions on manpage (#222578)

* Tue Nov  7 2006 Tomas Mraz <tmraz@redhat.com> - 0.3.3-13
- don't leak socket fds

* Tue Sep 12 2006 Tomas Mraz <tmraz@redhat.com> - 0.3.3-12
- drop hoplimit from ip route output (#205923)
- let's try enabling -fstack-protector again, seems to work now

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 0.3.3-11
- rebuilt for FC6

* Wed Jun  7 2006 Tomas Mraz <tmraz@redhat.com> 0.3.3-9
- drop the -fstack-protector not -f-stack-protector

* Tue May 30 2006 Tomas Mraz <tmraz@redhat.com> 0.3.3-8
- drop -fstack-protector from x86_64 build (workaround for #172145)
- make rekeying a little bit better

* Thu Mar  9 2006 Tomas Mraz <tmraz@redhat.com> 0.3.3-7
- add basic rekeying support (the patch includes NAT keepalive support
  by Brian Downing)
- dropped disconnect patch (solved differently)

* Wed Feb 15 2006 Tomas Mraz <tmraz@redhat.com> 0.3.3-6
- rebuild with new gcc

* Tue Jan 24 2006 Tomas Mraz <tmraz@redhat.com> 0.3.3-5
- send the disconnect packet properly (patch by Laurence Moindrot)

* Thu Sep 22 2005 Tomas Mraz <tmraz@redhat.com> 0.3.3-4
- improve compatibility with some Ciscos

* Wed Jun 15 2005 Tomas Mraz <tmraz@redhat.com> 0.3.3-3
- improve fix_ip_get_output in vpnc-script (#160364)

* Mon May 30 2005 Tomas Mraz <tmraz@redhat.com> 0.3.3-2
- package /var/run/vpnc and ghost files it can contain (#159015)
- add /sbin /usr/sbin to the path in vpnc-script (#159099)

* Mon May 16 2005 Tomas Mraz <tmraz@redhat.com> 0.3.3-1
- new upstream version

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Jan 05 2005 Warren Togami <wtogami@redhat.com> 0.3.2-3
- Fix 64bit

* Thu Dec 23 2004 Warren Togami <wtogami@redhat.com> 0.3.2-2
- make PIE (davej)

* Mon Dec 20 2004 Warren Togami <wtogami@redhat.com> 0.3.2-1
- 0.3.2
