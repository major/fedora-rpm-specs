# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif

Summary: Alternative packet radio system for Linux
Name: uronode
Version: 2.15
Release: 9%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://uronode.sourceforge.net
BuildRequires: make
BuildRequires: gcc, zlib-devel, libax25-devel, systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: flexd.service
Source2: uronode@.service
Source3: uronode.socket
Source4: uronode.xinetd
Source5: uronode-README.fedora
# Sent upstream
Patch0: uronode-2.7-install-fix.patch
# Sent upstream
Patch1: uronode-2.7-configure-non-interactive.patch

%description
URONode is an alternative packet radio system for Linux. It supports
cross-port digipeating, automatic importing of flexnet routing,
various IP functions, and ANSI colors.

%prep
%setup -qn %{name}-%{version}
%patch -P0 -p1 -b .install-fix
%patch -P1 -p1 -b .configure-non-interactive

# Copy Fedora readme into place
cp -p %{SOURCE5} README.fedora

# Removing bundled libax25, using system one.
rm -rf include

%build
export NON_INTERACTIVE=1
export ETC_DIR=/etc/ax25
export SBIN_DIR=/usr/sbin
export BIN_DIR=/usr/bin
export LIB_DIR=/usr/lib
export DATA_DIR=/usr/share
export MAN_DIR=$DATA_DIR/man
export VAR_DIR=/var
./configure
make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

# Systemd
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/flexd.service
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/uronode@.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/uronode.socket

# xinetd
install -Dpm 644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/xinetd.d/uronode

# ghost files
touch %{buildroot}/%{_var}/lib/flexd/destinations
# assert for case upstream would add default content
[ -s %{buildroot}%{_var}/lib/flexd/gateways ] && exit 1
[ -s %{buildroot}%{_var}/log/uronode/lastlog ] && exit 1
[ -s %{buildroot}%{_var}/lib/uronode/loggedin ] && exit 1

%post
%systemd_post flexd.service uronode.socket

# Create empty database of current users
[ -f %{_var}/lib/uronode/loggedin ] || touch %{_var}/lib/uronode/loggedin

%preun
%systemd_preun flexd.service uronode.socket

%postun
%systemd_postun_with_restart flexd.service uronode.socket

%files
%doc README.fedora README URONode.his FAQ COLORS CHANGES.1 CHANGES.2 COPYING

%{_sbindir}/*
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/ax25/flexd.conf
%config(noreplace) %{_sysconfdir}/ax25/uronode.announce
%config(noreplace) %{_sysconfdir}/ax25/uronode.conf
%config(noreplace) %{_sysconfdir}/ax25/uronode.info
%config(noreplace) %{_sysconfdir}/ax25/uronode.motd
%config(noreplace) %{_sysconfdir}/ax25/uronode.perms
%config(noreplace) %{_sysconfdir}/ax25/uronode.routes
%config(noreplace) %{_sysconfdir}/ax25/uronode.users
%{_datadir}/%{name}/xinetd.d/uronode
%{_unitdir}/flexd.service
%{_unitdir}/uronode@.service
%{_unitdir}/uronode.socket
%{_datadir}/%{name}
%dir %{_var}/log/uronode
%dir %{_var}/lib/flexd
%dir %{_var}/lib/uronode
%ghost %{_var}/lib/uronode/loggedin
%ghost %{_var}/lib/flexd/gateways
%ghost %{_var}/log/uronode/lastlog
%ghost %{_var}/lib/flexd/destinations

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.15-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.15-1
- New version
  Resolves: rhbz#2016589

* Fri Oct 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14-1
- New version
  Resolves: rhbz#2014224

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.13-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.13-1
- New version
  Resolves: rhbz#1917180

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.12-1
- New version
  Resolves: rhbz#1855006

* Wed Mar  4 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.11-1
- New version
  Resolves: rhbz#1809815

* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.10-4
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1800224

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb  5 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.10-1
- New version
  Resolves: rhbz#1669879

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.9-4
- Create empty database of current users

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.9-3
- Fixed FTBFS by adding gcc requirement
  Resolves: rhbz#1606621
- Cleaned leftover files

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.9-1
- New version
  Resolves: rhbz#1582969

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec  8 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.1-1
- New version
  Resolves: rhbz#1523435

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun  1 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7-1
- New version
  Resolves: rhbz#1457860

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6-1
- New version
  Resolves: rhbz#1398623

* Tue Apr 12 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.1-1
- New version
  Resolves: rhbz#1326416
- Switched to tgz suffix which seems to be the default
- Dropped override-dirs-in-unattended-install patch (upstreamed)
- Updated install-fix patch
- Optimized patch numbering

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail.com> 3.2.1-6
- Rebuilt for updated libax25.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-4
- Fixed flexd tmp path

* Wed Apr  1 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-3
- Fixed mheard.dat location and not provided it

* Tue Feb 17 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-2
- Pointed URLs to sourceforge.net

* Mon Feb 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-1
- New version
- Rebased install-fix patch
- Allowed to override installation directories in configure script
  (by override-dirs-in-unattended-install patch)
- Dropped downstream license file, license file provided by upstream
- Dropped non-interactive-configure patch (upstreamed)
- Dropped no-md2 patch (upstreamed)
- Dropped ax25-build-fix patch (upstreamed)

* Wed Dec  3 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-1
- New version
- Updated ax25-build-fix patch, now flexd.c is affected
- Dropped flexd-pidfile, ipv6 patches (all upstreamed)
- Dropped md2 code (cherry-picked from upstream, by no-md2 patch)
- Fixed debuginfo
- Switched description to American English
- Switched to systemd socket activation from xinetd (xinetd is optional)

* Wed Jul 30 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-2
- Fixed FHS issues related to var directory

* Tue Jul 15 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-1
- Initial release
