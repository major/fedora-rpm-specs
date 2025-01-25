%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}

%define GPG_CHECK 1
%define BASE_VERSION %(echo "%{version}" | sed 's/^\\([^.]\\+\\.[^.]\\+\\).*/\\1/')
%define repodir %{_builddir}/%{name}-%{version}

Summary:	High-performance authoritative DNS server
Name:		knot
Version:	3.4.4
Release:	1%{?dist}
License:	GPL-3.0-or-later
URL:		https://www.knot-dns.cz
Source0:	https://secure.nic.cz/files/knot-dns/%{name}-%{version}.tar.xz

%if 0%{?GPG_CHECK}
Source1:	https://secure.nic.cz/files/knot-dns/%{name}-%{version}.tar.xz.asc
# PGP keys used to sign upstream releases
# Export with --armor using command from https://fedoraproject.org/wiki/PackagingDrafts:GPGSignatures
# Don't forget to update %%prep section when adding/removing keys
Source100:	gpgkey-742FA4E95829B6C5EAC6B85710BB7AF6FEBBD6AB.gpg.asc
BuildRequires:	gnupg2
%endif

# Required dependencies
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(liburcu)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libedit)

# Optional dependencies
BuildRequires:	pkgconfig(libcap-ng)
BuildRequires:	pkgconfig(libidn2)
BuildRequires:	pkgconfig(libmnl)
BuildRequires:	pkgconfig(libnghttp2)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(systemd)
# dnstap dependencies
BuildRequires:	pkgconfig(libfstrm)
BuildRequires:	pkgconfig(libprotobuf-c)
# geoip dependencies
BuildRequires:	pkgconfig(libmaxminddb)
# XDP dependencies
BuildRequires:	pkgconfig(libbpf)

# Distro-dependent dependencies
%if 0%{?suse_version}
BuildRequires:	python3-Sphinx
BuildRequires:	lmdb-devel
BuildRequires:	protobuf-c
Requires(pre):	pwdutils
%if 0%{?sle_version} != 150400
BuildRequires:	pkgconfig(libxdp)
%endif
%endif
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:	python3-sphinx
BuildRequires:	pkgconfig(lmdb)
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:	pkgconfig(libxdp)
%endif
%endif

%if 0%{?rhel} >= 9 || 0%{?suse_version} || 0%{?fedora}
%define configure_quic --enable-quic=yes
%endif

Requires(post):		systemd %{_sbindir}/runuser
Requires(preun):	systemd
Requires(postun):	systemd

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%if 0%{?suse_version}
Provides:	group(knot)
%endif

%description
Knot DNS is a high-performance authoritative DNS server implementation.

%package libs
Summary:	Libraries used by the Knot DNS server and client applications
# Knot DNS 3.4+ isn't compatible with earlier knot-resolver
Conflicts:	knot-resolver < 5.7.4-2

%description libs
The package contains shared libraries used by the Knot DNS server and
utilities.

%package devel
Summary:	Development header files for the Knot DNS libraries
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The package contains development header files for the Knot DNS libraries
included in knot-libs package.

%package utils
Summary:	DNS client utilities shipped with the Knot DNS server
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# Debian package compat
Provides:	%{name}-dnsutils = %{version}-%{release}

%description utils
The package contains DNS client utilities shipped with the Knot DNS server.

%package dnssecutils
Summary:	DNSSEC tools shipped with the Knot DNS server
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description dnssecutils
The package contains DNSSEC tools shipped with the Knot DNS server.

%package module-dnstap
Summary:	dnstap module for Knot DNS
Requires:	%{name} = %{version}-%{release}

%description module-dnstap
The package contains dnstap Knot DNS module for logging DNS traffic.

%package module-geoip
Summary:	geoip module for Knot DNS
Requires:	%{name} = %{version}-%{release}

%description module-geoip
The package contains geoip Knot DNS module for geography-based responses.

%package doc
Summary:	Documentation for the Knot DNS server
BuildArch:	noarch
Provides:	bundled(jquery)

%description doc
The package contains documentation for the Knot DNS server.
On-line version is available on https://www.knot-dns.cz/documentation/

%prep
%if 0%{?GPG_CHECK}
export GNUPGHOME=./gpg-keyring
[ -d ${GNUPGHOME} ] && rm -r ${GNUPGHOME}
mkdir --mode=700 ${GNUPGHOME}
gpg2 --import %{SOURCE100}
gpg2 --verify %{SOURCE1} %{SOURCE0}
%endif
%autosetup -p1

%build
# disable debug code (causes unused warnings)
CFLAGS="%{optflags} -DNDEBUG -Wno-unused"

%ifarch armv7hl i686
# 32-bit architectures sometimes do not have sufficient amount of
# contiguous address space to handle default values
%define configure_db_sizes --with-conf-mapsize=64
%endif

%configure \
  --sysconfdir=/etc \
  --localstatedir=/var/lib \
  --libexecdir=/usr/lib/knot \
  --with-rundir=/run/knot \
  --with-moduledir=%{_libdir}/knot/modules-%{BASE_VERSION} \
  --with-storage=/var/lib/knot \
  %{?configure_db_sizes} \
  %{?configure_quic} \
  --disable-static \
  --enable-dnstap=yes \
  --with-module-dnstap=shared \
  --with-module-geoip=shared
make %{?_smp_mflags}
make html

%install
make install DESTDIR=%{buildroot}

# install documentation
install -d -m 0755 %{buildroot}%{_pkgdocdir}/samples
install -p -m 0644 -t %{buildroot}%{_pkgdocdir}/samples samples/*.zone*
install -p -m 0644 NEWS README.md %{buildroot}%{_pkgdocdir}
cp -av doc/_build/html %{buildroot}%{_pkgdocdir}
[ -r %{buildroot}%{_pkgdocdir}/html/index.html ] || exit 1
rm -f %{buildroot}%{_pkgdocdir}/html/.buildinfo

# install daemon and dbus configuration files
rm %{buildroot}%{_sysconfdir}/%{name}/*
install -p -m 0644 -D %{repodir}/samples/%{name}.sample.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
%if 0%{?fedora} || 0%{?rhel} > 7
install -p -m 0644 -D %{repodir}/distro/common/cz.nic.knotd.conf %{buildroot}%{_datadir}/dbus-1/system.d/cz.nic.knotd.conf
%endif

# install systemd files
install -p -m 0644 -D %{repodir}/distro/common/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
%if 0%{?suse_version}
ln -s service %{buildroot}/%{_sbindir}/rcknot
%endif

# create storage dir
install -d %{buildroot}%{_sharedstatedir}
install -d -m 0770 -D %{buildroot}%{_sharedstatedir}/knot

# remove libarchive files
find %{buildroot} -type f -name "*.la" -delete -print

%check
V=1 make check

%pre
getent group knot >/dev/null || groupadd -r knot
getent passwd knot >/dev/null || \
  useradd -r -g knot -d %{_sharedstatedir}/knot -s /sbin/nologin \
  -c "Knot DNS server" knot
%if 0%{?suse_version}
%service_add_pre knot.service
%endif

%post
%if 0%{?suse_version}
%service_add_post knot.service
%else
%systemd_post knot.service
%endif

%preun
%if 0%{?suse_version}
%service_del_preun knot.service
%else
%systemd_preun knot.service
%endif

%postun
%if 0%{?suse_version}
%service_del_postun knot.service
%else
%systemd_postun_with_restart knot.service
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
# https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
%else
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%endif

%files
%license COPYING
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/html
%attr(750,root,knot) %dir %{_sysconfdir}/knot
%config(noreplace) %attr(640,root,knot) %{_sysconfdir}/knot/knot.conf
%if 0%{?fedora} || 0%{?rhel} > 7
%config(noreplace) %attr(644,root,root) %{_datadir}/dbus-1/system.d/cz.nic.knotd.conf
%endif
%attr(770,root,knot) %dir %{_sharedstatedir}/knot
%dir %{_libdir}/knot
%dir %{_libdir}/knot/modules-*
%{_unitdir}/knot.service
%{_sbindir}/kcatalogprint
%{_sbindir}/kjournalprint
%{_sbindir}/keymgr
%{_sbindir}/knotc
%{_sbindir}/knotd
%if 0%{?suse_version}
%{_sbindir}/rcknot
%endif
%{_mandir}/man5/knot.conf.*
%{_mandir}/man8/kcatalogprint.*
%{_mandir}/man8/kjournalprint.*
%{_mandir}/man8/keymgr.*
%{_mandir}/man8/knotc.*
%{_mandir}/man8/knotd.*
%ghost %attr(770,root,knot) %dir %{_rundir}/knot

%files utils
%{_bindir}/kdig
%{_bindir}/khost
%{_bindir}/knsupdate
%{_sbindir}/kxdpgun
%{_mandir}/man8/kxdpgun.*
%{_mandir}/man1/kdig.*
%{_mandir}/man1/khost.*
%{_mandir}/man1/knsupdate.*

%files dnssecutils
%{_bindir}/knsec3hash
%{_bindir}/kzonecheck
%{_bindir}/kzonesign
%{_mandir}/man1/knsec3hash.*
%{_mandir}/man1/kzonecheck.*
%{_mandir}/man1/kzonesign.*

%files module-dnstap
%{_libdir}/knot/modules-*/dnstap.so

%files module-geoip
%{_libdir}/knot/modules-*/geoip.so

%files libs
%license COPYING
%doc NEWS
%doc README.md
%{_libdir}/libdnssec.so.*
%{_libdir}/libknot.so.*
%{_libdir}/libzscanner.so.*

%files devel
%{_includedir}/libdnssec
%{_includedir}/knot
%{_includedir}/libknot
%{_includedir}/libzscanner
%{_libdir}/libdnssec.so
%{_libdir}/libknot.so
%{_libdir}/libzscanner.so
%{_libdir}/pkgconfig/knotd.pc
%{_libdir}/pkgconfig/libdnssec.pc
%{_libdir}/pkgconfig/libknot.pc
%{_libdir}/pkgconfig/libzscanner.pc

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html

%changelog
* Thu Jan 23 2025 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.4.4-1
- Update to 3.4.4

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.4.3-1
- Update to 3.4.3

* Mon Nov 25 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.4.2-1
- Update to 3.4.2

* Mon Aug 26 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.9-1
- Update to 3.3.9

* Mon Jul 22 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.8-1
- Update to 3.3.8

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.7-1
- Update to 3.3.7

* Thu Jun 13 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.6-1
- Update to 3.3.6

* Thu Mar 07 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.5-1
- Update to 3.3.5

* Wed Jan 24 2024 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.4-1
- Update to 3.3.4

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.3-1
- Update to 3.3.3

* Fri Oct 20 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.2-1
- Update to 3.3.2

* Tue Sep 12 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.1-1
- Update to 3.3.1

* Mon Aug 28 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 27 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.9-1
- Update to 3.2.9

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.8-1
- Update to 3.2.8

* Tue Jun 06 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.7-1
- Update to 3.2.7
- Remove unneeded tests patch
- Use _datadir for config

* Fri May 12 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.2.6-2
- Add BR on libxdp on RHEL >= 9 to use with libbpf-1.x

* Thu Apr 06 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.6-1
- Update to 3.2.6
- Sync upstream packaging improvements

* Thu Feb 02 2023 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.5-1
- Update to 3.2.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.4-1
- Update to 3.2.4

* Mon Nov 28 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.3-2
- Rebuilt for libbpf 1.0 transition

* Mon Nov 21 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.3-1
- Update to 3.2.3

* Fri Nov 04 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.2-2
- New BuildRequires: libxdp (needed for libbpf >= 1.0)

* Tue Nov 01 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.2-1
- Update to 3.2.2

* Fri Sep 09 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.1-1
- Update to 3.2.1
- Remove patches included upstream
- Update Conflicts and move to knot-libs

* Mon Aug 22 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.2.0-1
- Update to 3.2.0
- Patch: fix tests on 32-bit platforms
- Patch: revert problematic hardening of service file
- Enable QUIC
- New knot-dnssecutils subpackage
- Debian compat (knot-utils vs knot-dnsutils)
- Remove bundled(jquery) version as it differes between distros

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 28 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.8-1
- Update to 3.1.8

* Wed Mar 30 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.7-1
- Update to 3.1.7

* Thu Feb 10 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.6-1
- Update to 3.1.6
- Add dbus config
- Use _sharedstatedir for home

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Jakub Ružička <jakub.ruzicka@nic.cz> 3.1.5-1
- Update to 3.1.5

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 3.1.4-2
- Rebuilt for protobuf 3.19.0

* Thu Nov 04 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.4-1
- Update to 3.1.4

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 3.1.3-2
- Rebuilt for protobuf 3.18.1

* Tue Oct 19 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.3-1
- Update to 3.1.3

* Thu Sep 09 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.2-1
- Update to 3.1.2

* Tue Aug 10 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.1-1
- Update to 3.1.1
- Enable XDP on ARM and improve XDP config macros
- Remove patch included upstream

* Wed Aug 04 2021 Jakub Ružička <jakub.ruzicka@nic.cz> 3.1.0-2
- Introduce a patch to fix tests on ppc64le
- Use autosetup macro to apply patches

* Mon Aug 02 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.1.0-1
- Update to 3.1.0
- Add missing BuildRequires including new libmnl for kxdpgun
- Temporarily disable XDP on ARM until issues are resolved

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.8-1
- Update to 3.0.8
- Print failed tests during check

* Thu Jun 17 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.7-1
- Update to 3.0.7

* Fri May 14 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.6-1
- Update to 3.0.6

* Tue Mar 30 2021 Jakub Ružička <jakub.ruzicka@nic.cz> 3.0.5-1
- Update to 3.0.5
- Properly escape BASE_VERSION macro
- Include module dirs in main package

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.4-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 01 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.4-1
- Update to 3.0.4
- Move dnstap module to subpackage
- Move geoip module to subpackage
- Remove redundant VERSION macro

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:45:48 CET 2021 Adrian Reber <adrian@lisas.de> - 3.0.3-2
- Rebuilt for protobuf 3.14

* Thu Dec 17 2020 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.3-1
- Update to 3.0.3

* Wed Nov 11 2020 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.2-2
- Remove patch included in upstream release

* Wed Nov 11 2020 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.2-1
- Update to 3.0.2

* Thu Oct 29 2020 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.1-2
- Respect GnuTLS insecure algorithms

* Mon Oct 12 2020 Jakub Ružička <jakub.ruzicka@nic.cz> - 3.0.1-1
- Update to 3.0.1
- Sync packaging from upstream

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 3.0.0-2
- Rebuilt for protobuf 3.13

* Thu Sep 10 2020 Jakub Ružička <jakub.ruzicka@nic.cz> 3.0.0-1
- New major upstream release 3.0.0
- Sync packaging from upstream

* Wed Sep 02 2020 Jakub Ružička <jakub.ruzicka@nic.cz> 2.9.6-1
- Update to 2.9.6

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 2.9.5-2
- Rebuilt for protobuf 3.12

* Mon May 25 2020 Tomas Krizek <tomas.krizek@nic.cz> - 2.9.5-1
- new upstream release 2.9.5

* Tue May 05 2020 Tomas Krizek <tomas.krizek@nic.cz> - 2.9.4-1
- new upstream release 2.9.4

* Tue Mar 03 2020 Tomas Krizek <tomas.krizek@nic.cz> - 2.9.3-1
- new upstream release 2.9.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.9.2-1
- new upstream release 2.9.2

* Tue Nov 12 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.9.1-1
- New upstream release 2.9.1
- add EPEL8 compatibility
- fix unsafe PGP keyring permissions

* Tue Sep 24 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.8.4-1
- new upstream release 2.8.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.8.3-1
- New upstream release 2.8.3

* Wed Jun 26 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.8.2-1
- New upstream release 2.8.2

* Wed May 29 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.8.1-1
- New upstream release 2.8.1
- Resolves BZ#1700251

* Thu Feb 28 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.6-3
- Added 01-test_net-disable-udp-send-on-unconnected.patch to disable
  unnecessary failing test. Fixes BZ#1675235

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.6-1
Knot DNS 2.7.6 (2019-01-23)
===========================

Improvements:
-------------
 - Zone status also shows when the zone load is scheduled
 - Server workers status also shows background workers utilization
 - Default control timeout for knotc was increased to 10 seconds
 - Pkg-config files contain auxiliary variable with library filename

Bugfixes:
---------
 - Configuration commit or server reload can drop some pending zone events
 - Nonempty zone journal is created even though it's disabled #635
 - Zone is completely re-signed during empty dynamic update processing
 - Server can crash when storing a big zone difference to the journal
 - Failed to link on FreeBSD 12 with Clang

* Mon Jan 07 2019 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.5-1
Knot DNS 2.7.5 (2019-01-07)
===========================

Features:
---------
 - Keymgr supports NSEC3 salt handling

Improvements:
-------------
 - Zone history in journal is dropped apon AXFR-like zone update
 - Libdnssec is no longer linked against libm #628
 - Libdnssec is explicitly linked against libpthread if PKCS #11 enabled #629
 - Better support for libknot packaging in Python
 - Manually generated KSK is 'ready' by default
 - Kdig supports '+timeout' as an alias for '+time'
 - Kdig supports '+nocomments' option
 - Kdig no longer prints empty lines between retries
 - Kdig returns failure if operations not successfully resolved #632
 - Fixed repeating of the 'KSK submission, waiting for confirmation' log
 - Various improvements in documentation, Dockerfile, and tests

Bugfixes:
---------
 - Knotc fails to unset huge configuration section
 - Kjournalprint sometimes fails to display zone journal content
 - Improper timing of ZSK removal during ZSK rollover
 - Missing UTC time zone indication in the 'iso' keymgr list output
 - A race condition in the online signing module

* Tue Nov 13 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.4-1
Knot DNS 2.7.4 (2018-11-13)
===========================

Features:
---------
 - Added SNI configuration for TLS in kdig (Thanks to Alexander Schultz)

Improvements:
-------------
 - Added warning log when DNSSEC events not successfully scheduled
 - New semantic check on timer values in keymgr
 - DS query no longer asks other addresses if got a negative answer
 - Reintroduced 'rollover' configuration option for CDS/CDNSKEY publication
 - Extended logging for zone loading
 - Various documentation improvements

Bugfixes:
---------
 - Failed to import module configuration #613
 - Improper Cflags value in libknot.pc if built with embedded LMDB #615
 - IXFR doesn't fall back to AXFR if malformed reply
 - DNSSEC events not correctly scheduled for empty zone updates
 - During algorithm rollover old keys get removed before DS TTL expires #617
 - Maximum zone's RRSIG TTL not considered during algorithm rollover #620

* Fri Oct 12 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.3-1
Knot DNS 2.7.3 (2018-10-11)
===========================

Features:
---------
 - New queryacl module for query access control
 - Configurable answer rrset rotation #612
 - Configurable NSEC bitmap in online signing

Improvements:
-------------
 - Better error logging for KASP DB operations #601
 - Some documentation improvements

Bugfixes:
---------
 - Keymgr "list" output doesn't show key size for ECDSA algorithms #602
 - Failed to link statically with embedded LMDB
 - Configuration commit causes zone reload for all zones
 - The statistics module overlooks TSIG record in a request
 - Improper processing of an AXFR-style-IXFR response consisting of one-record messages
 - Race condition in online signing during key rollover #600
 - Server can crash if geoip module is enabled in the geo mode

* Wed Aug 29 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.2-1
Knot DNS 2.7.2 (2018-08-29)
===========================

Improvements:
-------------
 - Keymgr list command displays also key size
 - Kjournalprint displays total occupied size in the debug mode
 - Server doesn't stop if failed to load a shared module from the module directory
 - Libraries libcap-ng, pthread, and dl are linked selectively if needed

Bugfixes:
---------
 - Sometimes incorrect result from dnssec_nsec_bitmap_contains (libdnssec)
 - Server can crash when loading zone file difference and zone-in-journal is set
 - Incorrect treatment of specific queries in the module RRL
 - Failed to link module Cookies as a shared library

* Wed Aug 15 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.7.1-1
Knot DNS 2.7.1 (2018-08-14)
===========================

Improvements:
-------------
 - Added zone wire size information to zone loading log message
 - Added debug log message for each unsuccessful remote address operation
 - Various improvements for packaging

Bugfixes:
---------
 - Incompatible handling of RRSIG TTL value when creating a DNS message
 - Incorrect RRSIG TTL value in zone differences and knotc zone operation outputs
 - Default configure prefix is ignored

Knot DNS 2.7.0 (2018-08-03)
===========================

Features:
---------
 - New DNS Cookies module and related '+cookie' kdig option
 - New module for response tailoring according to client's subnet or geographic location
 - General EDNS Client Subnet support in the server
 - OSS-Fuzz integration (Thanks to Jonathan Foote)
 - New '+ednsopt' kdig option (Thanks to Jan Včelák)
 - Online Signing support for automatic key rollover
 - Non-normal file (e.g. pipe) loading support in zscanner #542
 - Automatic SOA serial incrementation if non-empty zone difference
 - New zone file load option for ignoring zone file's SOA serial
 - New build-time option for alternative malloc specification
 - Structured logging for DNSSEC key submission event
 - Empty QNAME support in kdig

Improvements:
-------------
 - Various library and server optimizations
 - Reduced memory consumption of outgoing IXFR processing
 - Linux capabilities use overhaul #546 (Thanks to Robert Edmonds)
 - Online Signing properly signs delegations and CNAME records
 - CDS/CDNSKEY rrset is signed with KSK instead of ZSK
 - DNSSEC-related records are ignored when loading zone difference with signing enabled
 - Minimum allowed RSA key length was increased to 1024
 - Removed explicit dependency on Nettle

Bugfixes:
---------
 - Possible uninitialized address buffer use in zscanner
 - Possible index overflow during multiline record parsing in zscanner
 - kdig +tls sometimes consumes 100 % CPU #561
 - Single-Type Signing doesn't work with single ZSK key #566
 - Zone not flushed after re-signing during zone load #594
 - Server crashes when committing empty zone transaction
 - Incoming IXFR with on-slave signing sometimes leads to memory corruption #595

Compatibility:
--------------
 - Removed obsolete RRL configuration
 - Removed obsolete module names 'mod-online-sign' and 'mod-synth-record'
 - Removed obsolete 'ixfr-from-differences' configuration option
 - Removed old journal migration
 - Removed module rosedb


* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.6.8-1
Knot DNS 2.6.8 (2018-07-10)
===========================

Features:
---------
 - New 'import-pkcs11' command in keymgr

Improvements:
-------------
 - Unixtime serial policy mimics Bind – increment if lower #593

Bugfixes:
---------
 - Creeping memory consuption upon server reload #584
 - Kdig incorrectly detects QNAME if 'notify' is a prefix
 - Server crashes when zone sign fails #587
 - CSK->KZSK rollover retires CSK early #588
 - Server crashes when zone expires during outgoing multi-message transfer
 - Kjournalprint doesn't convert zone name argument to lower-case
 - Cannot switch to a previously used ksk-shared dnssec policy #589

* Thu May 17 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.6.7-1
Knot DNS 2.6.7 (2018-05-17)
===========================

Features:
---------
 - Added 'dateserial' (YYYYMMDDnn) serial policy configuration (Thanks to Wolfgang Jung)

Improvements:
-------------
 - Trailing data indication from the packet parser (libknot)
 - Better configuration check for a problematical option combination

Bugfixes:
---------
 - Incomplete configuration option item name check
 - Possible buffer overflow in 'knot_dname_to_str' (libknot)
 - Module dnsproxy doesn't preserve letter case of QNAME
 - Module dnsproxy duplicates OPT and TSIG in the non-fallback mode

* Wed Apr 11 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.6.6-1
Knot DNS 2.6.6 (2018-04-11)
===========================

Features:
---------
 - New EDNS option counters in the statistics module
 - New '+orphan' filter for the 'zone-purge' operation

Improvements:
-------------
 - Reduced memory consuption of disabled statistics metrics
 - Some spelling fixes (Thanks to Daniel Kahn Gillmor)
 - Server no longer fails to start if MODULE_DIR doesn't exist
 - Configuration include doesn't fail if empty wildcard match
 - Added a configuration check for a problematical option combination

Bugfixes:
---------
 - NSEC3 chain not re-created when SOA minimum TTL changed
 - Failed to start server if no template is configured
 - Possibly incorrect SOA serial upon changed zone reload with DNSSEC signing
 - Inaccurate outgoing zone transfer size in the log message
 - Invalid dname compression if empty question section
 - Missing EDNS in EMALF responses

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6.5-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 12 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.6.5-1
- New upstream release 2.6.5

Knot DNS 2.6.5 (2018-02-12)
===========================

Features:
---------
 - New 'zone-notify' command in knotc
 - Kdig uses '@server' as a hostname for TLS authenticaion if '+tls-ca' is set

Improvements:
-------------
 - Better heap memory trimming for zone operations
 - Added proper polling for TLS operations in kdig
 - Configuration export uses stdout as a default output
 - Simplified detection of atomic operations
 - Added '--disable-modules' configure option
 - Small documentation updates

Bugfixes:
---------
 - Zone retransfer doesn't work well if more masters configured
 - Kdig can leak or double free memory in corner cases
 - Inconsistent error outputs from dynamic configuration operations
 - Failed to generate documentation on OpenBSD

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.4-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Tomas Krizek <tomas.krizek@nic.cz> - 2.6.4-1
- Added PGP signature verification
- Added integration test

- New upstream release 2.6.4

Knot DNS 2.6.4 (2018-01-02)
===========================

Features:
---------
 - Module synthrecord allows multiple 'network' specification
 - New CSK handling support in keymgr

Improvements:
-------------
 - Allowed configuration for infinite zsk lifetime
 - Increased performance and security of the module synthrecord
 - Signing changeset is stored into journal even if 'zonefile-load' is whole

Bugfixes:
---------
 - Unintentional zone re-sign during reload if empty NSEC3 salt
 - Inconsistent zone names in journald structured logs
 - Malformed outgoing transfer for big zone with TSIG
 - Some minor DNSSEC-related issues

Knot DNS 2.6.3 (2017-11-24)
===========================

Bugfixes:
---------
 - Wrong detection of signing scheme rollover

Knot DNS 2.6.2 (2017-11-23)
===========================

Features:
---------
 - CSK algorithm rollover and (KSK, ZSK) <-> CSK rollover support

Improvements:
-------------
 - Allowed explicit configuration for infinite ksk lifetime
 - Proper error messages instead of unclear error codes in server log
 - Better support for old compilers

Bugfixes:
---------
 - Unexpected reply for DS query with an owner below a delegation point
 - Old dependencies in the pkg-config file


* Mon Nov 06 2017 Petr Špaček <petr.spacek@nic.cz> - 2.6.1-1
- New upstream release 2.6.1

Knot DNS 2.6.1 (2017-11-02)
===========================

Features:
---------
 - NSEC3 Opt-Out support in the DNSSEC signing
 - New CDS/CDNSKEY publish configuration option

Improvements:
-------------
 - Simplified DNSSEC log message with DNSKEY details
 - +tls-hostname in kdig implies +tls-ca if neither +tls-ca nor +tls-pin is given
 - New documentation sections for DNSSEC key rollovers and shared keys
 - Keymgr no longer prints useless algorithm number for generated key
 - Kdig prints unknown RCODE in a numeric format
 - Better support for LLVM libFuzzer

Bugfixes:
---------
 - Faulty DNAME semantic check if present in the zone apex and NSEC3 is used
 - Immediate zone flush not scheduled during the zone load event
 - Server crashes upon dynamic zone addition if a query module is loaded
 - Kdig fails to connect over TLS due to SNI is set to server IP address
 - Possible out-of-bounds memory access at the end of the input
 - TCP Fast Open enabled by default in kdig breaks TLS connection

Knot DNS 2.6.0 (2017-09-29)
===========================

Features:
---------
 - On-slave (inline) signing support
 - Automatic DNSSEC key algorithm rollover
 - Ed25519 algorithm support in DNSSEC (requires GnuTLS 3.6.0)
 - New 'journal-content' and 'zonefile-load' configuration options
 - keymgr tries to run as user/group set in the configuration
 - Public-only DNSSEC key import into KASP DB via keymgr
 - NSEC3 resalt and parent DS query events are persistent in timer DB
 - New processing state for a response suppression within a query module
 - Enabled server side TCP Fast Open if supported
 - TCP Fast Open support in kdig

Improvements:
-------------
 - Better record owner compression if related to the previous rdata dname
 - NSEC(3) chain is no longer recomputed whole on every update
 - Remove inconsistent and unnecessary quoting in log files
 - Avoiding of overlapping key rollovers at a time
 - More DNSSSEC-related semantic checks
 - Extended timestamp format in keymgr

Bugfixes:
---------
 - Incorrect journal free space computation causing inefficient space handling
 - Interface-automatic broken on Linux in the presence of asymmetric routing

Knot DNS 2.5.5 (2017-09-29)
===========================

Improvements:
-------------
 - Constant time memory comparison in the TSIG processing
 - Proper use of the ctype functions
 - Generated RRSIG records have inception time 90 minutes in the past

Bugfixes:
---------
 - Incorrect online signature for NSEC in the case of a CNAME record
 - Incorrect timestamps in dnstap records
 - EDNS Subnet Client validation rejects valid payloads
 - Module configuration semantic checks are not executed
 - Kzonecheck segfaults with unusual inputs

Knot DNS 2.5.4 (2017-08-31)
===========================

Improvements:
-------------
 - New minimum and maximum refresh interval config options (Thanks to Manabu Sonoda)
 - New warning when unforced flush with disabled zone file synchronization
 - New 'dnskey' keymgr command
 - Linking with libatomic on architectures that require it (Thanks to Pierre-Olivier Mercier)
 - Removed 'OK' from listing keymgr command outputs
 - Extended journal and keymgr documentation and logging

Bugfixes:
---------
 - Incorrect handling of specific corner-cases with zone-in-journal
 - The 'share' keymgr command doesn't work
 - Server crashes if configured with query-size and reply-size statistics options
 - Malformed big integer configuration values on some 32-bit platforms
 - Keymgr uses local time when parsing date inputs
 - Memory leak in kdig upon IXFR query

* Mon Jul 31 2017 Petr Spacek <petr.spacek@nic.cz> - 2.5.3-1
- new upstream release
WARNING: Automatic upgrade from versions 1.y.z is no longer possible.
To migrate, upgrade your packages gradually or use contacts listed on
https://www.knot-dns.cz/support/ (if you are in trouble).

Knot DNS 2.5.3 (2017-07-14)
===========================

Features:
---------
 - CSK rollover support for Single-Type Signing Scheme

Improvements:
-------------
 - Allowed binding to non-local adresses for TCP (Thanks to Julian Brost!)
 - New documentation section for manual DNSSEC key algorithm rollover
 - Initial KSK also generated in the submission state
 - The 'ds' keymgr command with no parameter uses all KSK keys
 - New debug mode in kjournalprint
 - Updated keymgr documentation

Bugfixes:
---------
 - Sometimes missing RRSIG by KSK in submission state.
 - Minor DNSSEC-related issues

Knot DNS 2.5.2 (2017-06-23)
===========================

Security:
---------
 - CVE-2017-11104: Improper TSIG validity period check can allow TSIG forgery (Thanks to Synacktiv!)

Improvements:
-------------
 - Extended debug logging for TSIG errors
 - Better error message for unknown module section in the configuration
 - Module documentation compilation no longer depends on module configuration
 - Extended policy section configuration semantic checks
 - Improved python version compatibility in pykeymgr
 - Extended migration section in the documentation
 - Improved DNSSEC event timing on 32-bit systems
 - New KSK rollover start log info message
 - NULL qtype support in kdig

Bugfixes:
---------
 - Failed to process included configuration
 - dnskey_ttl policy option in the configuration has no effect on DNSKEY TTL
 - Corner case journal fixes (huge changesets, OpenWRT operation)
 - Confusing event timestamps in knotc zone-status output
 - NSEC/NSEC3 bitmap not updated for CDS/CDNSKEY
 - CDS/CDNSKEY RRSIG not updated

Knot DNS 2.5.1 (2017-06-07)
===========================

Bugfixes:
---------
 - pykeymgr no longer crash on empty json files in the KASP DB directory
 - pykeymgr no longer imports keys in the "removed" state
 - Imported keys in the "removed" state no longer makes knotd to crash
 - Including an empty configuration directory no longer makes knotd to crash
 - pykeymgr is distributed and installed to the distribution tarball

Knot DNS 2.5.0 (2017-06-05)
===========================

Features:
---------
 - KASP database switched from JSON files to LMDB database
 - KSK rollover support using CDNSKEY and CDS in the automatic DNSSEC signing
 - Dynamic module loading support with proper module API
 - Journal can store full zone contents (not only differences)
 - Zone freeze/thaw support
 - Updated knotc zone-status output with optional column filters
 - New '[no]crypto' option in kdig
 - New keymgr implementation reflecting KASP database changes
 - New pykeymgr for JSON-based KASP database migration
 - Removed obsolete knot1to2 utility

Improvements:
-------------
 - Added libidn2 support to kdig (with libidn fallback)
 - Maximum timer database switched from configure to the server configuration

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Petr Spacek <petr.spacek@nic.cz> - 2.4.5-1
New upstream release: 2.4.5

Knot DNS 2.4.5 (2017-06-23)
===========================

Security:
---------
 - Improper TSIG validity period check can allow TSIG forgery (Thanks to Synacktiv!)

Bugfixes:
---------
 - Corner case journal fixes (huge changesets, OpenWRT operation)

Knot DNS 2.4.4 (2017-06-05)
===========================

Improvements:
-------------
 - Improved error handling in kjournalprint

Bugfixes:
---------
 - Zone flush not replanned upon unsuccessful flush
 - Journal inconsistency after deleting deleted zone
 - Zone events not rescheduled upon server reload (Thanks to Mark Warren)
 - Unreliable LMDB mapsize detection in kjournalprint
 - Some minor issues found by AddressSanitizer

Knot DNS 2.4.3 (2017-04-11)
===========================

Improvements:
-------------
 - New 'journal-db-mode' optimization configuration option
 - The default TSIG algorithm for utilities input is HMAC-SHA256
 - Implemented sensible default EDNS(0) padding policy (Thanks to D. K. Gillmor)
 - Added some more semantic checks on the knotc configuration operations

Bugfixes:
---------
 - Missing 'zone' keyword in the YAML output
 - Missing trailing dot in the keymgr DS owner output
 - Journal logs 'invalid parameter' in several cases
 - Some minor journal-related problems

Knot DNS 2.4.2 (2017-03-23)
===========================

Features:
---------
 - Zscanner can store record comments placed on the same line
 - Knotc status extension with version, configure, and workers parameters

Improvements:
-------------
 - Significant incoming XFR speed-up in the case of many zones

Bugfixes:
---------
 - Double OPT RR insertion when a global module returns KNOT_STATE_FAIL
 - User-driven zscanner parsing logic inconsistency
 - Lower serial at master doesn't trigger any errors
 - Queries with too long DNAME substitution do not return YXDOMAIN response
 - Incorrect elapsed time in the DDNS log
 - Failed to process forwarded DDNS request with TSIG

* Mon Feb 27 2017 Petr Spacek <petr.spacek@nic.cz> - 2.4.1-1
- new upstream release:
  + fix: Transfer of a huge rrset goes into an infinite loop
  + fix: Huge response over TCP contains useless TC bit instead of SERVFAIL
  + fix: Failed to build utilities with disabled daemon
  + fix: Memory leaks during keys removal
  + fix: Rough TSIG packet reservation causes early truncation
  + fix: Minor out-of-bounds string termination write in rrset dump
  + fix: Server crash during stop if failed to open timers DB
  + fix: Failed to compile on OS X older than Sierra
  + fix: Poor minimum UDP-max-size configuration check
  + fix: Failed to receive one-record-per-message IXFR-style AXFR
  + fix: Kdig timeouts when receiving RCODE != NOERROR on subsequent transfer message
  + improvement: Speed-up of rdata addition into a huge rrset
  + improvement: Introduce check of minumum timeout for next refresh
  + improvement: Dnsproxy module can forward all queries without local resolving

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Petr Spacek <petr.spacek@nic.cz> - 2.4.0-1
- new upstream release:
 + fix: False positive semantic-check warning about invalid bitmap in NSEC
 + fix: Unnecessary SOA queries upon notify with up to date serial
 + fix: Timers for expired zones are reset on reload
 + fix: Zone doesn't expire when the server is down
 + fix: Failed to handle keys with duplicate keytags
 + fix: Per zone module and global module insconsistency
 + fix: Obsolete online signing module configuration
 + fix: Malformed output from kjournalprint
 + fix: Redundant SO_REUSEPORT activation on the TCP socket
 + fix: Failed to use higher number of background workers
 + improvement: Lower memory consumption with qp-trie
 + improvement: Zone events and zone timers improvements
 + improvement: Print all zone names in the FQDN format
 + improvement: Simplified query module interface
 + improvement: Shared TCP connection between SOA query and transfer
 + improvement: Response Rate Limiting as a module with statistics support
 + improvement: Key filters in keymgr
 + features: New unified LMDB-based zone journal
 + features: Server statistics support
 + features: New statistics module for traffic measuring
 + features: Automatic deletion of retired DNSSEC keys
 + features: New control logging category

* Fri Dec 09 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.3.3-1
- new upstream release:
  + fix: double free when failed to apply zone journal
  + fix: zone bootstrap retry interval not preserved upon zone reload
  + fix: DNSSEC related records not flushed if not signed
  + fix: false semantic checks warning about incorrect type in NSEC bitmap
  + fix: memory leak in kzonecheck
  + improvement: all zone names are fully-qualified in log
  + features: new kjournalprint utility

* Thu Nov 17 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.3.2-1
- new upstream release:
  + fix: missing glue in some responses
  + fix: knsupdate prompt printing on non-terminal
  + fix: configuration policy item names in documentation
  + fix: segfault on OS X Sierra
  + fix: incorrect %%s expansion for the root zone
  + fix: refresh not existing slave zone after restart
  + fix: immediate zone refresh upon restart if refresh already scheduled
  + fix: early zone transfer after restart if transfer already scheduled
  + fix: not ignoring empty non-terminal parents during delegation lookup
  + fix: CD bit clearing in responses
  + fix: compilation error on GNU/kFreeBSD
  + fix: server crash after double zone-commit if journal error
  + improvement: significant speed-up of conf-commit and conf-diff operations
  + improvement: new EDNS Client Subnet API
  + improvement: better semantic-checks error messages
  + improvement: speed-up of knotc if control operation and known socket
  + improvement: zone purge operation purges also zone timers
  + feature: print TLS certificate hierarchy in kdig verbose mode
  + feature: new +subnet alias for +client
  + feature: new mod-whoami and mod-noudp modules
  + feature: new zone-purge control command
  + feature: new log-queries and log-responses options for mod-dnstap
  + feature: simple modules don't require empty configuration section
  + feature: new zone journal path configuration option
  + feature: new timeout configuration option for module dnsproxy

* Mon Aug 29 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.3.0-3
- fix post-installation scriptlet (RHBZ #1370939)

* Thu Aug 11 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.3.0-2
- endian independent DNS cookies (fixes build on ppc64 and s390x)

* Tue Aug 09 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.3.0-1
- new upstream release:
  + fix: No wildcard expansion below empty non-terminal for NSEC signed zone
  + fix: Don't ignore non-existing records to be removed in IXFR
  + fix: Fix kdig IXFR response processing if the transfer content is empty
  + fix: Avoid multiple loads of the same PKCS #11 module
  + improvement: Refactored semantic checks and better error messages
  + improvement: Set TC flag in delegation only if mandatory glue doesn't fit the response
  + improvement: Separate EDNS(0) payload size configuration for IPv4 and IPv6
  + feature: Zone size limit restriction for DDNS, AXFR, and IXFR (CVE-2016-6171)
  + feature: DNS-over-TLS support in kdig (RFC 7858)
  + feature: EDNS(0) padding and alignment support in kdig (RFC 7830)

* Fri Jun 24 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.2.1-2
- rebuild for updated userspace-rcu

* Mon May 30 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.2.1-1
- new upstream release:
  + fix: Separate logging of server and zone events
  + fix: Concurrent zone file flushing with many zones
  + fix: Control timeout parsing in knotc
  + fix: "Environment maxreaders limit reached" error in knotc
  + fix: Don't apply journal changes on modified zone file
  + fix: Enable multiple zone names completion in interactive knotc
  + fix: Set the TC flag in a response if a glue doesn't fit the response
  + fix: Disallow server reload when there is an active configuration transaction
  + improvement: Distinguish unavailable zones from zones with zero serial in log messages
  + improvement: Log warning and error messages to standard error output in all utilities
  + improvement: Document tested PKCS #11 devices
  + improvement: Extended Python configuration interface
- update requirements for Fedora 25

* Sun May 29 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.2.0-3
- update default configuration file

* Sun May 08 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.2.0-2
- fix: systemd service starting

* Tue Apr 26 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.2.0-1
- new upstream release:
  + fix: Query/response message type setting in dnstap module
  + fix: Remote address retrieval from dnstap capture in kdig
  + fix: Global modules execution for queries hitting existing zones
  + fix: Execution of semantic checks after an IXFR transfer
  + fix: kdig failure when the first AXFR message contains just the SOA record
  + fix: Exclude non-authoritative types from NSEC/NSEC3 bitmap at a delegation
  + fix: Mark PKCS#11 generated keys as sensitive
  + fix: Error when removing the only zone from the server
  + fix: Don't abort knotc transaction when some check fails
  + feature: URI and CAA resource record types support
  + feature: RRL client address based white list
  + feature: knotc interactive mode
  + improvement: Consistent IXFR error messages
  + improvement: Various fixes for better compatibility with PKCS#11 devices
  + improvement: Various keymgr user interface improvements
  + improvement: Better zone event scheduler performance with many zones
  + improvement: New server control interface
  + improvement: kdig uses local resolver if resolv.conf is empty

* Wed Feb 10 2016 Jan Vcelak <jvcelak@fedoraproject.org> 2.1.1-1
- new upstream release:
  + fix: Allow import of duplicate private key into the KASP
  + fix: Avoid duplicate NSEC for Wildcard No Data answer
  + fix: Server crash when an incomming transfer is in progress and reload is issued
  + fix: Socket polling when configured with many interfaces and threads
  + improvement: Use correct source address for UDP messages recieved on ANY address
  + improvement: Extend documentation of knotc commands

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jan Vcelak <jvcelak@fedoraproject.org> 2.1.0-1
- new upstream release:
  + improvement: Remove implementation limit for the number of network interfaces
  + improvement: Remove possibly insecure server control over a network socket
  + fix: Schedule zone bootstrap after slave zone fails to load from disk

* Sun Dec 20 2015 Jan Vcelak <jvcelak@fedoraproject.org> 2.1.0-0.1.rc1
- new upstream pre-release:
  + feature: Per-thread UDP socket binding using SO_REUSEPORT
  + feature: Support for dynamic configuration database
  + feature: DNSSEC, Support for cryptographic tokens via PKCS #11 interface
  + feature: DNSSEC, Experimental support for online signing
  + improvement: Support for zone file name patterns
  + improvement: Configurable location of zone timer database
  + improvement: Non-blocking network operations and better timeout handling
  + improvement: Caching of Critical configuration values for better performance
  + improvement: Logging of ACL failures
  + improvement: RRL: Add rate-limit-slip zero support to drop all responses
  + improvement: RRL: Document behavior for different rate-limit-slip options
  + improvement: kdig: Warning instead of error on TSIG validation failure
  + improvement: Cleanup of support libraries interfaces (libknot, libzscanner, libdnssec)
  + fix: synth-record module: Fix application of default configuration options
  + fix: TSIG: Allow compressed TSIG name when forwarding DDNS updates

* Wed Nov 25 2015 Jan Vcelak <jvcelak@fedoraproject.org> 2.0.2-1
- new upstream release:
  + security fix: out-of-bound read in packet parser for malformed NAPTR record

* Thu Sep 03 2015 Jan Vcelak <jvcelak@fedoraproject.org> 2.0.1-1
- new upstream release:
  + fix: do not reload expired zones on 'knotc reload' and server startup
  + fix: rare race-condition in event scheduling causing delayed event execution
  + fix: skipping of non-authoritative nodes in NSEC proofs
  + fix: TC flag setting in RRL slipped answers
  + fix: disable domain name compression for root label
  + fix: fix CNAME following when quering for NSEC RR type
  + fix: fix refreshing of DNSSEC signatures for zone keys
  + fix: fix binding an unavailable IPv6 address (IP_FREEBIND)
  + fix: fix infinite loop in knotc zonestatus and memstats
  + fix: fix memory leak in configuration on server shutdown
  + fix: fix broken dnsproxy module
  + fix: fix multi value parsing on big-endian
  + fix: adapt to Nettle 3 API break causing base64 decoding failures on big-endian
  + feature: add 'keymgr zone key ds' to show key's DS record
  + feature: add 'keymgr tsig generate' to generate TSIG keys
  + feature: add query module scoping to process either all queries or zone queries only
  + feature: add support for file name globbing in config file includes
  + feature: add 'request-edns-option' config option to add custom EDNS0 option into server initiated queries
  + improvement: send minimal responses (remove NS from Authority section for NOERROR)
  + improvement: update persistent timers only on shutdown for better performance
  + improvement: allow change of RR TTL over DDNS
  + improvement: documentation fixes, updates, and improvements in formatting
  + improvement: install yparser and zscanner header files

* Mon Jul 20 2015 Jan Vcelak <jvcelak@fedoraproject.org> 2.0.0-1
- new upstream release:
  + feature: possibility to disable zone file synchronization
  + feature: knsupdate, add input prompt in interactive mode
  + feature: knsupdate, TSIG algorithm specification in interactive mode

* Thu Jun 18 2015 Jan Vcelak <jvcelak@fedoraproject.org> 2.0.0-0.1.rc1
- new upstream pre-release:
  + fix: lost NOTIFY message if received during zone transfer
  + fix: kdig, record correct dnstap SocketProtocol when retrying over TCP
  + fix: kdig, hide TSIG section with +noall
  + fix: do not set AA flag for AXFR/IXFR queries
  + feature: new configuration format in YAML, binary store im LMDB
  + feature: DNSSEC, separate library, switch to GnuTLS, new utilities
  + feature: DNSSEC, basic KASP support (generate initial keys, ZSK rollover)
  + feature: zone parser, split long TXT/SPF strings into multiple strings
  + feature: kdig, add generic dump style option (+generic)
  + feature: try all master servers on failure in multi-master environment
  + feature: improved remotes and ACLs (multiple addresses, multiple keys)
  + feature: basic support for zone file patterns (%%s to substitute zone name)
  + improvement: do not write class for SOA record (unified with other RR types)
  + improvement: do not write master server address into the zone file
  + documentation: manual pages also in HTML and PDF format

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.99.1-3
- Rebuilt for nettle soname bump

* Fri Feb 13 2015 Jan Vcelak <jvcelak@fedoraproject.org> 1.99.1-2
- fix BuildRequires for systemd integration

* Fri Feb 13 2015 Jan Vcelak <jvcelak@fedoraproject.org> 1.99.1-1
- new upstream pre-release version:
  + DNSSEC: switch from OpenSSL to GnuTLS
  + DNSSEC: initial support for KASP
- split package into subpackages
- add documentation building
- restart daemon on updated
