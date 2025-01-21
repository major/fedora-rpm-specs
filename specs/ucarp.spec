Summary: Common Address Redundancy Protocol (CARP) for Unix
Name: ucarp
Version: 1.5.2
Release: 40%{?dist}
# See the COPYING file which details everything
License: ISC AND BSD-2-Clause
URL: http://www.ucarp.org/
Source0: http://download.pureftpd.org/pub/ucarp/ucarp-%{version}.tar.bz2
Source1: ucarp@.service
Source2: vip-001.conf.example
Source3: vip-common.conf
Source4: vip-up
Source5: vip-down
#Source6: vip-helper.sh
Source7: ucarp
Source8: vip-001.pwd.example
Patch0: ucarp-1.5.2-sighup.patch
BuildRequires: make
BuildRequires: gettext
BuildRequires: autoconf, automake, libtool
BuildRequires: libpcap-devel
BuildRequires: systemd
Requires:      initscripts

%description
UCARP allows a couple of hosts to share common virtual IP addresses in order
to provide automatic failover. It is a portable userland implementation of the
secure and patent-free Common Address Redundancy Protocol (CARP, OpenBSD's
alternative to the patents-bloated VRRP).
Strong points of the CARP protocol are: very low overhead, cryptographically
signed messages, interoperability between different operating systems and no
need for any dedicated extra network link between redundant hosts.


%prep
%setup -q

%patch -P0 -p0

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Install the unit file
%{__install} -D -p -m 0755 %{SOURCE1} \
    %{buildroot}%{_unitdir}/ucarp@.service

%{__mkdir_p} %{buildroot}/etc/ucarp
%{__mkdir_p} %{buildroot}%{_libexecdir}/ucarp

# Install the example config files
%{__install} -D -p -m 0600 %{SOURCE2} %{SOURCE3} %{SOURCE8} \
    %{buildroot}/etc/ucarp/

# Install helper scripts
%{__install} -D -p -m 0700 %{SOURCE4} %{SOURCE5} %{SOURCE7} \
    %{buildroot}%{_libexecdir}/ucarp/



%pre
# Legacy, in case we update from an older package where the service was "carp"
if [ -f /etc/rc.d/init.d/carp ]; then
    /sbin/service carp stop &>/dev/null || :
    /sbin/chkconfig --del carp
fi

%post
%systemd_post ucarp@.service

%preun
%systemd_preun ucarp@.service

%postun
%systemd_postun_with_restart ucarp@.service


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_unitdir}/ucarp@.service
%attr(0700,root,root) %dir /etc/ucarp/
%config(noreplace) /etc/ucarp/vip-common.conf
/etc/ucarp/vip-001.conf.example
/etc/ucarp/vip-001.pwd.example
%config(noreplace) %{_libexecdir}/ucarp/
%{_sbindir}/ucarp

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-39
- Require initscripts

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-35
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.2-30
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-27
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.5.2-22
- Incorporate systemd tweaks from Hans-Werner Jouy.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.5.2-20
- Correct unit file target.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 1.5.2-17
- systemd cleanup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 1.5.2-13
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 1.5.2-10
- Fix FTBFS, BZ 992829.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Jon Ciesla <limburgher@gmail.com> - 1.5.2-7
- Patch to fix crash, BZ 693762.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 1.5.2-5
- Add hardened build.

* Wed Mar 14 2012 Jon Ciesla <limburgher@gmail.com> - 1.5.2-4
- Migrate to systemd, BZ 800498.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.2-1
- New upstream.
- Uses arc4random() if available.
- Avoids adverts that might be twice as what they should be.
- Marked vip-up and vip-down config(noreplace), BZ 586893.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.1-1
- New upstream.
- New option (--nomcast / -M) to use broadcast 
- advertisements instead of multicast ones.

* Mon Apr 13 2009 Jon Ciesla <limb@jcomserv.net> - 1.5-1
- Update to 1.5 BZ 458767.
- Added LSB header to init script, BZ 247082.
- New upstream should address BZ 427495, 449266, 455394.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 1.4-1
- Update to 1.4.
- Rip out all of the "list" stuff and 255.255.255.255 address hack (#427495).
- Change from INITLOG (now deprecated) to LOGGER in the init script.
- Move helper scripts to /usr/libexec/ucarp/.

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.2-9
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.2-8
- Update License field.

* Fri Feb  2 2007 Matthias Saou <http://freshrpms.net/> 1.2-7
- Rename service from carp to ucarp, to be more consistent.
- Move /etc/sysconfig/carp to /etc/ucarp since it has become a config directory
  of its own.

* Wed Nov 29 2006 Matthias Saou <http://freshrpms.net/> 1.2-6
- Rebuild against new libpcap.

* Mon Nov 13 2006 Matthias Saou <http://freshrpms.net/> 1.2-5
- Include all improvements from Denis Ovsienko (#200395).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.2-4
- FC6 rebuild.

* Tue Aug 22 2006 Matthias Saou <http://freshrpms.net/> 1.2-3
- Update to 1.3 snapshot, which includes the ARP fix, as well as fixes for the
  segfaults reported in #200400 and #201596.
- Add autoconf, automake and libtool build reqs for the 1.3 patch.

* Thu Jul 27 2006 Matthias Saou <http://freshrpms.net/> 1.2-3
- Fix init script for recent find versions (#200395).

* Thu Jun 22 2006 Matthias Saou <http://freshrpms.net/> 1.2-2
- Include ARP patch backported from 1.3 snapshot (#196095).
- Make libpcap build requirement conditional to be able to share spec file.

* Wed Jun 21 2006 Matthias Saou <http://freshrpms.net/> 1.2-1
- Update to 1.2.
- BuildRequire libpcap-devel instead of libpcap now that it has been split.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.1-5
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.1-4
- Rebuild for new gcc/glibc.

* Thu Nov 17 2005 Matthias Saou <http://freshrpms.net/> 1.1-3
- Rebuild against new libpcap library.

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.1-2
- Add %%dir entry for /etc/sysconfig/carp directory.

* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 1.1-1
- Update to 1.1.
- Update source location.

* Fri Jul  9 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Initial RPM release.

