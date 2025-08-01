%global _hardened_build 1

Name:    ppp
# Please be careful when bumping the ppp version. Several packages
# have version-tied dependencies on it, including NetworkManager-ppp
# (from NetworkManager) and NetworkManager-pptp , which are core
# packages. They may need code changes to build against new ppp
# versions. Please only bump ppp on a side tag and ensure it also
# contains rebuilds of at least those two packages before merging.
# Several other less important packages are also tied to the ppp
# version, as of 2023-04-19 the list is:
# NetworkManager-fortisslvpn
# NetworkManager-l2tp
# NetworkManager-ppp
# NetworkManager-pptp
# NetworkManager-sstp
# sstp-client
# These all need to be patched (if necessary) and rebuilt for new
# versions of ppp.
Version: 2.5.1
Release: 6%{?dist}
Summary: The Point-to-Point Protocol daemon
License: bsd-3-clause AND zlib AND licenseref-fedora-public-domain AND bsd-attribution-hpnd-disclaimer AND bsd-4.3tahoe AND bsd-4-clause-uc AND apache-2.0 AND lgpl-2.0-or-later AND (gpl-2.0-or-later OR bsd-2-clause OR bsd-3-clause OR bsd-4-clause) AND gpl-2.0-or-later AND xlock AND gpl-1.0-or-later AND mackerras-3-clause-acknowledgment AND mackerras-3-clause AND hpnd-fenneberg-Livingston AND sun-ppp AND hpnd-inria-imag AND sun-ppp-2000
URL:     http://www.samba.org/ppp

Source0: https://github.com/paulusmack/ppp/archive/ppp-%{version}.tar.gz
Source1: ppp-pam.conf
Source2: ppp-logrotate.conf
Source3: ppp-tmpfiles.conf
Source4: ip-down
Source5: ip-down.ipv6to4
Source6: ip-up
Source7: ip-up.ipv6to4
Source8: ipv6-down
Source9: ipv6-up
Source12: ppp-watch.tar.xz
Source13: ipv6-up.initscripts
Source14: ipv6-down.initscripts

# Fedora-specific
Patch0: ppp-2.5.0-use-change-resolv-function.patch
# Fix build with GCC 15
Patch1: ppp-2.5.1-gcc15.patch

BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: gcc
BuildRequires: pam-devel
BuildRequires: libpcap-devel
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: glib2-devel
BuildRequires: openssl-devel
BuildRequires: libxcrypt-devel
%if %{defined rhel}
Provides: bundled(linux-atm) = 2.4.1
%else
BuildRequires: linux-atm-libs-devel
%endif

Requires: glibc >= 2.0.6
Requires: /etc/pam.d/system-auth
Requires: libpcap >= 14:0.8.3-6
Requires: systemd

# Subpackage removed and obsoleted in F40
Obsoletes: network-scripts-ppp < %{version}-%{release}

%description
The ppp package contains the PPP (Point-to-Point Protocol) daemon and
documentation for PPP support. The PPP protocol provides a method for
transmitting datagrams over serial point-to-point links. PPP is
usually used to dial in to an ISP (Internet Service Provider) or other
organization over a modem and phone line.

%package devel
Summary: Headers for ppp plugin development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconf-pkg-config

%description devel
This package contains the header files for building plugins for ppp.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

tar -xJf %{SOURCE12}

# Create a sysusers.d config file
cat >ppp.sysusers.conf <<EOF
g dip 40
EOF

%build
autoreconf -fi
export CFLAGS="%{build_cflags} -fno-strict-aliasing"
%configure --enable-systemd --enable-cbcp --with-pam --disable-openssl-engine
%make_build
%make_build -C ppp-watch LDFLAGS="%{?build_ldflags} -pie"

%install
%make_install
find scripts -type f | xargs chmod a-x
make ROOT=%{buildroot} -C ppp-watch install

# create log files dir
install -d %{buildroot}%{_localstatedir}/log/ppp

# install pam config
install -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/ppp

# install logrotate script
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/ppp

# install tmpfiles drop-in
install -d %{buildroot}%{_tmpfilesdir}
install -m 644 -p %{SOURCE3} %{buildroot}%{_tmpfilesdir}/ppp.conf

# install scripts (previously owned by initscripts package)
install -d %{buildroot}%{_sysconfdir}/ppp
install -p %{SOURCE4} %{buildroot}%{_sysconfdir}/ppp/ip-down
install -p %{SOURCE5} %{buildroot}%{_sysconfdir}/ppp/ip-down.ipv6to4
install -p %{SOURCE6} %{buildroot}%{_sysconfdir}/ppp/ip-up
install -p %{SOURCE7} %{buildroot}%{_sysconfdir}/ppp/ip-up.ipv6to4
install -p %{SOURCE8} %{buildroot}%{_sysconfdir}/ppp/ipv6-down
install -p %{SOURCE9} %{buildroot}%{_sysconfdir}/ppp/ipv6-up
install -p %{SOURCE13} %{buildroot}%{_sysconfdir}/ppp/ipv6-down.initscripts
install -p %{SOURCE14} %{buildroot}%{_sysconfdir}/ppp/ipv6-up.initscripts

# ghosts
mkdir -p %{buildroot}%{_rundir}/pppd/lock

# fix configuration files suffix
pushd %{buildroot}%{_sysconfdir}/ppp
for f in `ls *.example`
do
  mv "$f" "${f%%.example}"
done
popd

%if "%{_sbindir}" == "%{_bindir}"
mv %{buildroot}/usr/sbin/ppp-watch %{buildroot}%{_bindir}/
%endif

install -m0644 -D ppp.sysusers.conf %{buildroot}%{_sysusersdir}/ppp.conf


%post
%tmpfiles_create ppp.conf

%files
%doc FAQ README README.cbcp README.linux README.MPPE README.MSCHAP80 README.MSCHAP81 README.pwfd README.pppoe scripts sample README.eap-tls
%{_sbindir}/chat
%{_sbindir}/pppd
%{_sbindir}/pppdump
%{_sbindir}/pppoe-discovery
%{_sbindir}/pppstats
%{_sbindir}/ppp-watch
%dir %{_sysconfdir}/ppp
%{_sysconfdir}/ppp/ip-up
%{_sysconfdir}/ppp/ip-down
%{_sysconfdir}/ppp/ip-up.ipv6to4
%{_sysconfdir}/ppp/ip-down.ipv6to4
%{_sysconfdir}/ppp/ipv6-up
%{_sysconfdir}/ppp/ipv6-up.initscripts
%{_sysconfdir}/ppp/ipv6-down
%{_sysconfdir}/ppp/ipv6-down.initscripts
%{_sysconfdir}/ppp/openssl.cnf
%{_mandir}/man8/chat.8*
%{_mandir}/man8/pppd.8*
%{_mandir}/man8/pppdump.8*
%{_mandir}/man8/pppd-radattr.8*
%{_mandir}/man8/pppd-radius.8*
%{_mandir}/man8/pppstats.8*
%{_mandir}/man8/pppoe-discovery.8*
%{_mandir}/man8/ppp-watch.8*
%{_libdir}/pppd
%ghost %dir %{_rundir}/pppd
%ghost %dir %{_rundir}/pppd/lock
%dir %{_sysconfdir}/logrotate.d
%attr(700, root, root) %dir %{_localstatedir}/log/ppp
%config(noreplace) %{_sysconfdir}/ppp/eaptls-client
%config(noreplace) %{_sysconfdir}/ppp/eaptls-server
%config(noreplace) %{_sysconfdir}/ppp/chap-secrets
%config(noreplace) %{_sysconfdir}/ppp/options
%config(noreplace) %{_sysconfdir}/ppp/pap-secrets
%config(noreplace) %{_sysconfdir}/pam.d/ppp
%config(noreplace) %{_sysconfdir}/logrotate.d/ppp
%{_tmpfilesdir}/ppp.conf
%{_sysusersdir}/ppp.conf

%files devel
%{_includedir}/pppd
%doc PLUGINS
%{_libdir}/pkgconfig/pppd.pc

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.1-5
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 2.5.1-4
- Add explicit BR: libxcrypt-devel

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.1-2
- Rebuilt for the bin-sbin merge (2nd attempt)

* Sat Nov 16 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.1-1
- New version
  Resolves: rhbz#2313209

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.0-12
- Rebuilt for the bin-sbin merge

* Mon Jun 24 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-11
- Fixed radiusclient parser

* Wed Jun 12 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-10
- Openssl engine API is deprecated for a while thus disable it

* Thu May  9 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-9
- Pre-created upstream default lock dir

* Sun Apr 14 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-8
- Added missing and recently approved SPDX licenses

* Wed Feb 21 2024 Kalev Lember <klember@redhat.com> - 2.5.0-7
- Obsolete dropped network-scripts-ppp subpackage

* Tue Feb 13 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-6
- Dropped network scripts
  Resolves: rhbz#2262981

* Wed Jan 24 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-5
- Converted license to SPDX

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.5.0-3
- Use bundled ATM in RHEL builds

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-1
- New version
  Resolves: rhbz#2184291

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 05 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.4.9-7
- Backport patches from master for SSTP to connect using EAP-TLS to Azure VnetGWay and Windows RAS server

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.4.9-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.9-3
- Keep lock files in /var/lock (https://github.com/ppp-project/ppp/pull/227)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.9-1
- New version
  Resolves: rhbz#1912617

* Mon Aug 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.8-8
- Added workaround for Windows Server 2019
  Resolves: rhbz#1867047

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.8-6
- Added missing options to man pages

* Tue Apr  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.8-5
- Updated EAP-TLS patch to v1.300

* Mon Apr  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.8-4
- Updated EAP-TLS patch to v1.201

* Fri Feb 28 2020 Tom Stellard <tstellar@redhat.com> - 2.4.8-3
- Use make_build macro
- https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make

* Wed Feb 26 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.8-2
- Fixed ghost directories verification

* Fri Feb 21 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.8-1
- New version
- Changed sources to github
- Dropped 0028-pppoe-include-netinet-in.h-before-linux-in.h,
  ppp-2.4.7-DES-openssl, ppp-2.4.7-honor-ldflags,
  ppp-2.4.7-coverity-scan-fixes  patches (all upstreamed)
- Fixed buffer overflow in the eap_request and eap_response functions
  Resolves: CVE-2020-8597

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.4.7-30
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Dec  3 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-29
- Fixed some issues found by coverity scan

* Tue Nov 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-28
- Fixed network scripts related regression caused by release 26

* Mon Nov  5 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-27
- Updated EAP-TLS patch to v1.102

* Tue Jul 24 2018 Lubomir Rintel <lkundrak@v3.sk> - 2.4.7-26
- Split out the network-scripts

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.7-24
- Remove group/defattr, minor spec cleanups

* Wed Jun 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-23
- Replaced initscripts requirement by the network-scripts
  Resolves: rhbz#1592384

* Tue Jun  5 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-22
- Updated EAP-TLS patch to v1.101
  Resolves: CVE-2018-11574

* Mon Apr  9 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-21
- Link with -E not to break plugins
  Resolves: rhbz#1564459

* Fri Apr  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-20
- Also build all DSOs with distro's LDFLAGS
  Related: rhbz#1563157

* Wed Apr  4 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-19
- Build with distro's LDFLAGS
  Resolves: rhbz#1563157

* Tue Mar 27 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-18
- Used openssl for the DES instead of the libcrypt / glibc
  Resolves: rhbz#1556132

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.7-17
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.4.7-15
- Rebuilt for switch to libxcrypt

* Mon Aug 21 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.7-14
- EAP-TLS patch updated to version 0.999
- Switched to openssl-1.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.4.7-10
- Fix FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 09 2015 Michal Sekletar <msekleta@redhat.com> - 2.4.7-7
- prevent running into issues caused by undefined behavior (pointers of incompatible types aliasing the same object)

* Wed Dec 10 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.7-6
- fix logical expression in eap_client_active macro (#1023620)

* Wed Nov 19 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.7-5
- don't mark logrotate config as executable (#1164435)

* Tue Sep  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.7-4
- devel package should depend on base package as per guidelines

* Tue Aug 19 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.7-3
- don't mark tmpfiles dropin as executable (#1131293)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.7-1
- rebase to 2.4.7. Includes fix for CVE-2014-3158 (#1128716)

* Fri Jun 20 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.6-6
- version 0.997 of EAP-TLS patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.6-4
- move ppp initscripts to ppp package (#1088220)

* Mon Apr 14 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.6-3
- don't require perl and expect (#1086846)

* Thu Apr 10 2014 Michal Sekletar <msekleta@redhat.com> - 2.4.6-2
- rebase to 2.4.6

* Thu Aug 01 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-33
- fix post installation scriptlet

* Fri Jul 12 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-32
- don't ship /var/lock/ppp in rpm payload and create it in %%post instead
- fix installation of tmpfiles.d configuration
- enable hardened build
- fix bogus dates in changelog
- compile all binaries with hardening flags

* Thu Jul 04 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-31
- fix possible NULL pointer dereferencing

* Wed May 29 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-30
- make radius plugin config parser less strict
- resolves : #906913

* Wed Mar 20 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-29
- Add creation of dip system group

* Wed Mar 20 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-28
- Add /etc/logrotate.d to files section since we no longer hard depend on logrotate

* Wed Mar 20 2013 Michal Sekletar <msekleta@redhat.com> - 2.4.5-27
- Don't hard depend on logrotate

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Michal Sekletar <msekleta@redhat.com> - 2.4.5-25
- Resolves: #840190 - install configuration file in /usr/lib/tmpfiles.d

* Tue Sep 11 2012 Michal Sekletar <msekleta@redhat.com> - 2.4.5-24
- Removed unnecessary dependency on systemd-unit

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Michal Sekletar <msekleta@redhat.com>
- Resolves: #817011 - fixed ppp-2.4.5-eaptls-mppe-0.99 patch, added variable definition

* Mon May 21 2012 Michal Sekletar <msekleta@redhat.com>
- Resolves: #817013 - fixed support for multilink channels in pppol2tp plugin

* Thu May 17 2012 Michal Sekletar <msekleta@redhat.com>
- Resolves: #771340 - fixed compilation of pppd without USE_EAPTLS

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 30 2011 Jiri Skala <jskala@redhat.com> - 2.4.5-18
- fixes #682381 - hardcodes eth0
- fixes #708260 - SELinux is preventing access on the file LCK..ttyUSB3

* Mon Apr 04 2011 Jiri Skala <jskala@redhat.com> - 2.4.5-17
- fixes #664282 and #664868 - man page fixes

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-15
- corrected tmpfiles.d conf
- replaced remaining /etc by macros

* Tue Nov 30 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-14
- fixes #656671 - /var/run and /var/lock on tmpfs
- replaced paths /var /etc by macros

* Tue Nov 16 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-13
- fixes #565294 - SELinux is preventing /sbin/consoletype access to a leaked packet_socket fd

* Wed Sep 29 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-12
- fixes #637513 - Missing: README.eap-tls
- updated to latest eaptls upstream
- fixes #637886 - EAP-TLS not working with enabled PPP Multilink Framing option

* Thu Aug 05 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-11
- fixes #617625 - FTBFS in ppp due to change in kernel-headers
- fixes pppol2tp Makefile

* Tue Jul 13 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-10
- fixes #613717 - Missing line in example script ip-up.local.add
- removed /usr/kerberos/include from eaptls patch

* Wed Jun 16 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-9
- included eap-tls patch

* Wed Apr 07 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-8
- added pppoe-discovery(8)

* Fri Mar 05 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-7
- removed duplicities from patches (ip-*.local.add)

* Fri Feb 12 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-6
- fixes #560014 - SELinux is preventing /usr/sbin/pppd "read write" access on pppd2.tdb

* Thu Feb 04 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-5
- one line correction in fd_leak patch

* Wed Feb 03 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-4
- applied patch fd_leak

* Fri Jan 22 2010 Jiri Skala <jskala@redhat.com> - 2.4.5-3
- fixed some rpmlint complains

* Sun Nov 22 2009 Jiri Skala <jskala@redhat.com>  - 2.4.5-2
- updated patches (make local succeeded, koji failed)

* Fri Nov 20 2009 Jiri Skala <jskala@redhat.com>  - 2.4.5-1
- updated to latest upstream sources (#538058)

* Thu Oct 08 2009 Jiri Skala <jskala@redhat.com>  - 2.4.4-14
- fixed #519042 - ppp package is missing URL in spec
- fixed #524575 - ppp: no_strip patch modifies backup files created by previous patches

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> 2.4.4-13
- use password-auth common PAM configuration instead of system-auth

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 06 2009 - Jiri Skala <jskala@redhat.com> 2.4.4-11
- fixed #488764 - package upgrade should not replace configuration files

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Jiri Skala <jskala@redhat.com> 2.4.4.-9
- fixed #467004 PPP sometimes gets incorrect DNS servers for mobile broadband connections

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.4.4-8
- fix license tag

* Tue May 13 2008 Martin Nagy <mnagy@redhat.com> 2.4.4-7
- add new speeds, patch by Jason Vas Dias (#446132)

* Thu Mar 06 2008 Martin Nagy <mnagy@redhat.com> 2.4.4-6
- call closelog earlier (#222295)
- fix ChapMS2 (#217076)
- moving header files to new -devel package (#203542)

* Mon Mar 03 2008 Martin Nagy <mnagy@redhat.com> 2.4.4-5
- put logs into /var/log/ppp (#118837)

* Mon Feb 11 2008 Martin Nagy <mnagy@redhat.com> 2.4.4-4
- rebuild for gcc-4.3

* Fri Nov 09 2007 Martin Nagy <mnagy@redhat.com> 2.4.4-3
- removed undesired files from the package (#241753)

* Fri Dec  1 2006 Thomas Woerner <twoerner@redhat.com> 2.4.4-2
- fixed build requirement for libpcap (#217661)

* Wed Jul 19 2006 Thomas Woerner <twoerner@redhat.com> 2.4.4-1
- new version 2.4.4 with lots of fixes
- fixed reesolv.conf docs (#165072)
  Thanks to Matt Domsch for the initial patch
- enabled CBCP (#199278)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.4.3-6.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.3-6.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.3-6.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 12 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Fri Nov  4 2005 David Woodhouse <dwmw2@redhat.com> 2.4.3-5
- Implement ipv6cp-accept-remote option

* Fri Oct  7 2005 Tomas Mraz <tmraz@redhat.com> 2.4.3-4
- use include instead of pam_stack in pam config

* Sun Jul 31 2005 Florian La Roche <laroche@redhat.com>
- rebuild for libpcap of the day

* Tue Jul 19 2005 Thomas Woerner <twoerner@redhat.com> 2.4.3-2.1
- additional patch for the scripts, thanks to Sammy (#163621)

* Tue Jul 19 2005 Thomas Woerner <twoerner@redhat.com> 2.4.3-2
- dropped all executable bits in scripts directory to prevent rpm requiring
  programs used in there

* Mon Jul 18 2005 Thomas Woerner <twoerner@redhat.com> 2.4.3-1
- new version 2.4.3
  - updated patches: make, lib64, dontwriteetc, fix, fix64, no_strip,
    radiusplugin
  - dropped patches: bpf, signal, pcap, pppoatm, pkgcheck

* Tue Nov  2 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-7
- fixed out of bounds memory access, possible DOS

* Thu Oct  7 2004 David Woodhouse <dwmw2@redhat.com> 2.4.2-6.3
- Fix use of 'demand' without explicit MTU/MRU with pppoatm

* Tue Oct  5 2004 David Woodhouse <dwmw2@redhat.com> 2.4.2-6.2
- Link pppoatm plugin against libresolv.
- Revert to linux-atm headers without the workaround for #127098

* Mon Oct  4 2004 David Woodhouse <dwmw2@redhat.com> 2.4.2-6.1
- Include atmsap.h for pppoatm plugin.

* Mon Oct  4 2004 David Woodhouse <dwmw2@redhat.com> 2.4.2-6
- Add pppoatm plugin (#131555)

* Thu Sep 16 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-5.1
- fixed subscript out of range (#132677)

* Wed Sep 15 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-5
- example scripts are using change_resolv_conf to modify /etc/resolv.conf
  (#132482)
- require new libpcap library (>= 0.8.3-6) with a fix for inbound/outbound
  filter processing
- not using internal libpcap structures anymore, fixes inbound/outbound
  filter processing (#128053)

* Fri Aug  6 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-4
- fixed signal handling (#29171)

* Mon Jun 21 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-3.1
- fixed compiler warnings
- fixed 64bit problem with ms-chap (#125501)
- enabled pie again

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 24 2004 David Woodhouse <dwmw2@redhat.com> 2.4.2-2.3
- Enable IPv6 support. Disable PIE to avoid bogus Provides:

* Fri May 14 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-2.2
- compiled pppd and chat PIE

* Thu May 13 2004 Thomas Woerner <twoerner@redhat.com> 2.4.2-2.1
- added 'missingok' to ppp.logrotate (#122911)

* Fri May 07 2004 Nils Philippsen <nphilipp@redhat.com> 2.4.2-2
- don't write to /etc (#118837)

* Wed Mar 10 2004 Nalin Dahyabhai <nalin@redhat.com> 2.4.2-1
- update to 2.4.2

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep  5 2003 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-15
- rebuild

* Fri Sep  5 2003 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-14
- apply the patch from -11

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-12
- rebuild

* Tue Jun  3 2003 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-11
- check for libcrypt in the right directory at compile-time

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Elliot Lee <sopwith@redhat.com> 2.4.1-9
- Fix build failure by rebuilding

* Tue Nov 19 2002 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-8
- rebuild
- set x86_64 to use varargs the way s390 does

* Mon Jul 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add patch:
	* Thu Jun 06 2002 Phil Knirsch <pknirsch@redhat.com>
	- Fixed varargs problem for s390/s390x.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-4
- rebuild in new environment

* Wed Feb 27 2002 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-3
- revert cbcp patch, it's wrong (#55367)

* Thu Aug  9 2001 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-2
- add buildprereq on pam-devel (#49559)
- add patch to respond to CBCP LCP requests (#15738)
- enable cbcp support at build-time
- change the Copyright: tag to a License: tag

* Wed May 23 2001 Nalin Dahyabhai <nalin@redhat.com> 2.4.1-1
- update to 2.4.1

* Fri Dec  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Thu Nov  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.4.0

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- move man pages to %%{_mandir}

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- change perms using defattr
- modify PAM setup to use system-auth

* Sun Mar 26 2000 Florian La Roche <Florian.La Roche@redhat.com>
- change to root:root perms

* Mon Mar 06 2000 Nalin Dahyabhai <nalin@redhat.com>
- reaper bugs verified as fixed
- check pam_open_session result code (bug #9966)

* Mon Feb 07 2000 Nalin Dahyabhai <nalin@redhat.com>
- take a shot at the wrong reaper bugs (#8153, #5290)

* Thu Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- free ride through the build system (release 2)

* Tue Jan 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- Update to 2.3.11

* Sat Nov 06 1999 Michael K. Johnson <johnsonm@redhat.com>
- Better fix for both problems

* Fri Nov 05 1999 Michael K. Johnson <johnsonm@redhat.com>
- fix for double-dial problem
- fix for requiring a controlling terminal problem

* Sun Sep 19 1999 Preston Brown <pbrown@redhat.com>
- 2.3.10 bugfix release

* Fri Aug 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- New version 2.3.9 required for kernel 2.3.13 and will be required
  for new initscripts.  auth patch removed; 2.3.9 does the same thing
  more readably than the previous patch.

* Thu Jun 24 1999 Cristian Gafton <gafton@redhat.com>
- add pppdump

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- force pppd use the glibc's logwtmp instead of implementing its own

* Thu Apr 01 1999 Preston Brown <pbrown@redhat.com>
- version 2.3.7 bugfix release

* Tue Mar 23 1999 Cristian Gafton <gafton@redhat.com>
- version 2.3.6

* Mon Mar 22 1999 Michael Johnson <johnsonm@redhat.com>
- auth patch

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Jun  5 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.3.5.

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Fri May  8 1998 Jakub Jelinek <jj@ultra.linux.cz>
- make it run with kernels 2.1.100 and above.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Mar 18 1998 Cristian Gafton <gafton@redhat.com>
- requires glibc 2.0.6 or later

* Wed Mar 18 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated PAM patch to not turn off wtmp/utmp/syslog logging.

* Wed Jan  7 1998 Cristian Gafton <gafton@redhat.com>
- added the /etc/pam.d config file
- updated PAM patch to include session support

* Tue Jan  6 1998 Cristian Gafton <gafton@redhat.com>
- updated to ppp-2.3.3, build against glibc-2.0.6 - previous patches not
  required any more.
- added buildroot
- fixed the PAM support, which was really, completely broken and against any
  standards (session support is still not here... :-( )
- we build against running kernel and pray that it will work
- added a samples patch; updated glibc patch

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- added a patch to use our own route.h, rather then glibc's (which has
  alignment problems on Alpha's) -- I only applied this patch on the Alpha,
  though it should be safe everywhere

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- turned off the execute bit for scripts in /usr/doc

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Integrated new patch from David Mosberger
- Improved description
