%global _hardened_build 1
%global backends %{nil}

Name: pdns
Version: 4.9.3
Release: 1%{?dist}
Summary: A modern, advanced and high performance authoritative-only name server
License: GPL-2.0-only
URL: http://powerdns.com
Source0: http://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
Patch0: pdns-gcc15.patch
ExcludeArch: %{arm} %{ix86}

Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

BuildRequires: make
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: krb5-devel
BuildRequires: libcurl-devel
BuildRequires: libsodium-devel
%if 0%{?rhel} == 9
BuildRequires: lua-devel
%define lua_implementation lua
%else
%ifarch ppc64le riscv64
%define lua_implementation lua
BuildRequires: lua-devel
%else
BuildRequires: luajit-devel
%define lua_implementation luajit
%endif
%endif
%if 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine
%else
BuildRequires: openssl-devel
%endif
BuildRequires: p11-kit-devel
BuildRequires: perl
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: libcurl-devel
BuildRequires: systemd
BuildRequires: systemd-devel
Provides: powerdns = %{version}-%{release}
%global backends %{backends} bind

%description
The PowerDNS Nameserver is a modern, advanced and high performance
authoritative-only name server. It is written from scratch and conforms
to all relevant DNS standards documents.
Furthermore, PowerDNS interfaces with almost any database.

%package tools
Summary: Extra tools for %{name}

%description tools
This package contains the extra tools for %{name}

%package backend-mysql
Summary: MySQL backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mariadb-connector-c-devel openssl-devel
%global backends %{backends} gmysql

%description backend-mysql
This package contains the gmysql backend for %{name}

%package backend-postgresql
Summary: PostgreSQL backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpq-devel
%global backends %{backends} gpgsql

%description backend-postgresql
This package contains the gpgsql backend for %{name}

%package backend-pipe
Summary: Pipe backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} pipe

%description backend-pipe
This package contains the pipe backend for %{name}

%package backend-remote
Summary: Remote backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} remote

%description backend-remote
This package contains the remote backend for %{name}

%package backend-ldap
Summary: LDAP backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: openldap-devel
%global backends %{backends} ldap

%description backend-ldap
This package contains the ldap backend for %{name}

%package backend-lua2
Summary: LUA2 backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} lua2

%description backend-lua2
This package contains the lua2 backend for %{name}

%package backend-sqlite
Summary: SQLite backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel
%global backends %{backends} gsqlite3

%description backend-sqlite
This package contains the SQLite backend for %{name}

%package backend-tinydns
Summary: TinyDNS backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: tinycdb-devel
%global backends %{backends} tinydns

%description backend-tinydns
This package contains the TinyDNS backend for %{name}

%package ixfrdist
Summary: A program to redistribute zones over AXFR and IXFR
BuildRequires: yaml-cpp-devel

%description ixfrdist
This package contains the ixfrdist program.

%prep
%autosetup -p1

%build
export CPPFLAGS="-DLDAP_DEPRECATED"

%configure \
	--enable-option-checking=fatal \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--disable-static \
	--disable-dependency-tracking \
	--disable-silent-rules \
	--with-modules='' \
	--with-lua=%{lua_implementation} \
	--with-dynmodules='%{backends}' \
	--enable-tools \
	--with-libsodium \
	--enable-ixfrdist \
	--enable-unit-tests \
	--enable-lua-records \
	--enable-experimental-pkcs11 \
	--enable-dns-over-tls \
	--enable-systemd

%make_build

%install
%make_install

%{__rm} -f %{buildroot}%{_libdir}/%{name}/*.la
%{__mv} %{buildroot}%{_sysconfdir}/%{name}/pdns.conf{-dist,}

# rename zone2ldap to pdns-zone2ldap (#1193116)
%{__mv} %{buildroot}/%{_bindir}/zone2ldap %{buildroot}/%{_bindir}/pdns_zone2ldap
%{__mv} %{buildroot}/%{_mandir}/man1/zone2ldap.1 %{buildroot}/%{_mandir}/man1/pdns_zone2ldap.1

# change user/group to pdns
# change default backend to bind
sed -i \
    -e 's/# setuid=/setuid=pdns/' \
    -e 's/# setgid=/setgid=pdns/' \
    -e 's/# launch=/launch=bind/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %{buildroot}%{_sysconfdir}/%{name}/pdns.conf

%{__rm} %{buildroot}/%{_bindir}/stubquery
%{__install} -d %{buildroot}/%{_sharedstatedir}/%{name}

%check
make %{?_smp_mflags} -C pdns check

%pre
getent group pdns >/dev/null || groupadd -r pdns
getent passwd pdns >/dev/null || \
	useradd -r -g pdns -d /var/lib/pdns -s /sbin/nologin \
	-c "PowerDNS Authoritative Server" pdns

%post
%systemd_post pdns.service

%preun
%systemd_preun pdns.service

%postun
%systemd_postun_with_restart pdns.service

%files
%doc README
%license COPYING
%{_bindir}/pdns_control
%{_bindir}/pdnsutil
%{_bindir}/pdns_zone2ldap
%{_bindir}/zone2sql
%{_bindir}/zone2json
%{_sbindir}/pdns_server
%{_mandir}/man1/pdns_control.1.gz
%{_mandir}/man1/pdns_server.1.gz
%{_mandir}/man1/zone2sql.1.gz
%{_mandir}/man1/zone2json.1.gz
%{_mandir}/man1/pdns_zone2ldap.1.gz
%{_mandir}/man1/pdnsutil.1.gz
%{_unitdir}/pdns.service
%{_unitdir}/pdns@.service
%{_libdir}/%{name}/libbindbackend.so
%dir %{_libdir}/%{name}/
%dir %attr(-,pdns,pdns) %{_sharedstatedir}/%{name}
%dir %attr(-,root,pdns) %{_sysconfdir}/%{name}/
%attr(0640,root,pdns) %config(noreplace) %{_sysconfdir}/%{name}/pdns.conf

%files tools
%{_bindir}/calidns
%{_bindir}/dnsbulktest
%{_bindir}/dnsgram
%{_bindir}/dnspcap2calidns
%{_bindir}/dnspcap2protobuf
%{_bindir}/dnsreplay
%{_bindir}/dnsscan
%{_bindir}/dnsscope
%{_bindir}/dnstcpbench
%{_bindir}/dnswasher
%{_bindir}/dumresp
%{_bindir}/ixplore
%{_bindir}/pdns_notify
%{_bindir}/nproxy
%{_bindir}/nsec3dig
%{_bindir}/saxfr
%{_bindir}/sdig
%{_mandir}/man1/calidns.1.gz
%{_mandir}/man1/dnsbulktest.1.gz
%{_mandir}/man1/dnsgram.1.gz
%{_mandir}/man1/dnspcap2calidns.1.gz
%{_mandir}/man1/dnspcap2protobuf.1.gz
%{_mandir}/man1/dnsreplay.1.gz
%{_mandir}/man1/dnsscan.1.gz
%{_mandir}/man1/dnsscope.1.gz
%{_mandir}/man1/dnstcpbench.1.gz
%{_mandir}/man1/dnswasher.1.gz
%{_mandir}/man1/dumresp.1.gz
%{_mandir}/man1/ixplore.1.gz
%{_mandir}/man1/pdns_notify.1.gz
%{_mandir}/man1/nproxy.1.gz
%{_mandir}/man1/nsec3dig.1.gz
%{_mandir}/man1/saxfr.1.gz
%{_mandir}/man1/sdig.1.gz
%{_pkgdocdir}/bind-dnssec.4.2.0_to_4.3.0_schema.sqlite3.sql
%{_pkgdocdir}/bind-dnssec.schema.sqlite3.sql

%files backend-mysql
%{_pkgdocdir}/schema.mysql.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.mysql.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.mysql.sql
%{_pkgdocdir}/3.4.0_to_4.1.0_schema.mysql.sql
%{_pkgdocdir}/4.1.0_to_4.2.0_schema.mysql.sql
%{_pkgdocdir}/4.2.0_to_4.3.0_schema.mysql.sql
%{_pkgdocdir}/4.3.0_to_4.7.0_schema.mysql.sql
%{_pkgdocdir}/enable-foreign-keys.mysql.sql
%{_libdir}/%{name}/libgmysqlbackend.so

%files backend-postgresql
%{_pkgdocdir}/schema.pgsql.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.pgsql.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.pgsql.sql
%{_pkgdocdir}/3.4.0_to_4.1.0_schema.pgsql.sql
%{_pkgdocdir}/4.1.0_to_4.2.0_schema.pgsql.sql
%{_pkgdocdir}/4.2.0_to_4.3.0_schema.pgsql.sql
%{_pkgdocdir}/4.3.0_to_4.7.0_schema.pgsql.sql
%{_libdir}/%{name}/libgpgsqlbackend.so

%files backend-pipe
%{_libdir}/%{name}/libpipebackend.so

%files backend-remote
%{_libdir}/%{name}/libremotebackend.so

%files backend-ldap
%{_libdir}/%{name}/libldapbackend.so
%{_pkgdocdir}/dnsdomain2.schema
%{_pkgdocdir}/pdns-domaininfo.schema

%files backend-lua2
%{_libdir}/%{name}/liblua2backend.so

%files backend-sqlite
%{_pkgdocdir}/schema.sqlite3.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.sqlite3.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.sqlite3.sql
%{_pkgdocdir}/3.4.0_to_4.0.0_schema.sqlite3.sql
%{_pkgdocdir}/4.0.0_to_4.2.0_schema.sqlite3.sql
%{_pkgdocdir}/4.2.0_to_4.3.0_schema.sqlite3.sql
%{_pkgdocdir}/4.3.0_to_4.3.1_schema.sqlite3.sql
%{_pkgdocdir}/4.3.1_to_4.7.0_schema.sqlite3.sql
%{_libdir}/%{name}/libgsqlite3backend.so

%files backend-tinydns
%{_libdir}/%{name}/libtinydnsbackend.so

%files ixfrdist
%{_bindir}/ixfrdist
%{_mandir}/man1/ixfrdist.1.gz
%{_mandir}/man5/ixfrdist.yml.5.gz
%{_sysconfdir}/%{name}/ixfrdist.example.yml
%{_unitdir}/ixfrdist.service
%{_unitdir}/ixfrdist@.service

%changelog
* Mon Jan 20 2025 Morten Stevens <mstevens@fedoraproject.org> - 4.9.3-1
- Update to 4.9.3

* Mon Jan 20 2025 Morten Stevens <mstevens@fedoraproject.org> - 4.9.2-4
- Fix missing include for gcc15

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 4.9.2-2
- Rebuild for yaml-cpp 0.8

* Tue Oct 01 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.9.2-1
- Update to 4.9.2

* Mon Sep 09 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.9.1-2
- Fixed typo in %__install macro
- Remove outdated obsoletes entries
- Remove temporary migration of pdns home directory

* Wed Sep 04 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.9.1-1
- Update to 4.9.1

* Tue Aug 06 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.8.4-4
- Switch to openssl-devel-engine

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.8.4-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.8.4-1
- Update to 4.8.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 4.8.3-2
- Rebuilt for Boost 1.83

* Tue Oct 10 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.8.3-1
- Update to 4.8.3

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 4.8.2-2
- rebuild for new libsodium

* Thu Oct 05 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.8.2-1
- Update to 4.8.2

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 4.8.1-3
- rebuild for new libsodium

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.8.1-1
- Update to 4.8.1

* Thu Jun 01 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.8.0-1
- Update to 4.8.0

* Mon Apr 17 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4

* Tue Apr 04 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 4.7.2-5
- Rebuilt for Boost 1.81

* Mon Jan 23 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.7.2-4
- Fix missing include for gcc13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Richard Shaw <hobbes1069@gmail.com> - 4.7.2-2
- Rebuild for yaml-cpp 0.7.0.

* Tue Nov 01 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Mon Oct 31 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1

* Sat Oct 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 4.6.2-2
- Rebuilt for Boost 1.78

* Tue Apr 12 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2

* Sun Apr 10 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1

* Tue Jan 25 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0

* Sat Jan 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.5.3-1
- Update to 4.5.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.5.2-3
- Use lua instead of luajit for RHEL9

* Thu Nov 11 2021 Morten Stevens <mstevens@fedoraproject.org> - 4.5.2-2
- Use lua instead of luajit for ppc64le and s390x

* Wed Nov 10 2021 Morten Stevens <mstevens@fedoraproject.org> - 4.5.2-1
- Update to 4.5.2

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.5.1-3
- Rebuilt with OpenSSL 3.0.0

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 4.5.1-2
- Rebuilt for Boost 1.76

* Mon Jul 26 2021 Morten Stevens <mstevens@fedoraproject.org> - 4.5.1-1
- Update to 4.5.1
- PowerDNS Security Advisory 2021-01 (CVE-2021-36754)

* Sat Jul 24 2021 Morten Stevens <mstevens@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0
- Upstream dropped support for 32-bit arches

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 4.4.1-3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.4.1-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 10 2021 Morten Stevens <mstevens@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 4.4.0-6
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 4.4.0-4
- Rebuilt for Boost 1.75

* Wed Jan 13 16:40:36 CET 2021 Adrian Reber <adrian@lisas.de> - 4.4.0-3
- Rebuilt for protobuf 3.14

* Mon Dec 21 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.4.0-2
- Fix building on RHEL8

* Mon Dec 21 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0

* Sat Dec 05 2020 Jeff Law <law@redhat.com> - 4.3.1-3
- Fix missing #include for gcc-11

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 4.3.1-2
- Rebuilt for protobuf 3.13

* Wed Sep 23 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1
- PowerDNS Security Advisory 2020-05 (CVE-2020-17482)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.0-5
- Updated file permissions

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 4.3.0-4
- Rebuilt for protobuf 3.12

* Thu Jun 04 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.0-3
- Rebuilt for Boost 1.73

* Wed May 27 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.0-2
- Updated file permissions

* Thu Apr 09 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.2.1-3
- Fix build with GCC 10.0

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 4.2.1-2
- Rebuild for protobuf 3.11

* Fri Dec 06 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Wed Oct 30 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.2.0-3
- Drop support for backend lua and mydns

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 4.2.0-2
- Rebuild for yaml-cpp 0.6.3.

* Fri Aug 30 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0
- Enable LUA records
- Enable lua2 backend
- Enable luajit
- Enable experimental pkcs11 support
- Added ixfrdist subpackage

* Thu Aug 08 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.13-1
- Update to 4.1.13

* Mon Aug 05 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.11-3
- Obsolete backend GeoIP

* Sun Aug 04 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.11-2
- Drop support for backend GeoIP

* Fri Aug 02 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.11-1
- Update to 4.1.11
- PowerDNS Security Advisory 2019-06 (CVE-2019-10203)

* Fri Jul 26 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.10-3
- Drop unused build dependency on python2-virtualenv

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.10-1
- Update to 4.1.10
- PowerDNS Security Advisory 2019-04 (CVE-2019-10162)
- PowerDNS Security Advisory 2019-05 (CVE-2019-10163)

* Wed Mar 27 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.8-1
- Update to 4.1.8

* Tue Mar 19 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.7-1
- Update to 4.1.7
- PowerDNS Security Advisory 2019-03 (CVE-2019-3871)

* Sun Feb 03 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.1.6-1
- Update to 4.1.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 4.1.5-3
- Rebuilt for Boost 1.69

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.5-2
- Rebuild for protobuf 3.6

* Tue Nov 06 2018 Morten Stevens <mstevens@fedoraproject.org> - 4.1.5-1
- Update to 4.1.5
- PowerDNS Security Advisory 2018-03 (CVE-2018-10851)
- PowerDNS Security Advisory 2018-05 (CVE-2018-14626)

* Wed Sep 19 2018 Morten Stevens <mstevens@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Morten Stevens <mstevens@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Wed May 16 2018 Morten Stevens <mstevens@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.1.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 19 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.1-2
- BuildRequire gcc-c++ (https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequire)

* Fri Feb 16 2018 Morten Stevens <mstevens@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1

* Wed Feb 14 2018 Richard Shaw <hobbes1069@gmail.com> - 4.1.0-5
- Rebuild for yaml-cpp 0.6.0.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.0-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-2
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.1.0-0.8.rc3
- Rebuild for protobuf 3.5

* Fri Nov 17 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-0.7.rc3
- Update to 4.1.0-rc3

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.0-0.6.rc2
- Rebuild for protobuf 3.4

* Mon Nov 06 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-0.5.rc2
- Update to 4.1.0-rc2
- Dropped support for backend opendbx and zeromq

* Mon Oct 23 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-0.4.rc1
- Removed Fedora specific systemd patch

* Sun Oct 15 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-0.3.rc1
- Added Fedora specific systemd patch
- Added upstream patch to fix an issue with MariaDB 10.2
- Enabled upstream systemd (--enable-systemd) support

* Thu Sep 21 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-0.2.rc1
- Switch to mariadb-connector-c-devel
- Spec file improvements

* Thu Aug 31 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.1.0-0.1.rc1
- Update to 4.1.0-rc1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.4-5
- Rebuilt for Boost 1.64

* Thu Jul 13 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.4-4
- Rebuilt for MariaDB 10.2

* Mon Jun 26 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.4-3
- Updated patch to fix building on ppc64

* Fri Jun 23 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.4-2
- Fix building on ppc64

* Fri Jun 23 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.4-1
- Update to 4.0.4

* Mon Jun 19 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.3-7
- Rebuilt for pandoc

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-6
- Rebuild for protobuf 3.3.1

* Tue Feb 14 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.3-5
- Fix for GCC 7.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.3-3
- Rebuilt for Boost 1.63

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-2
- Rebuild for protobuf 3.2.0

* Tue Jan 17 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3

* Tue Jan 17 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.2-2
- Fix for building on armv7hl

* Mon Jan 16 2017 Morten Stevens <mstevens@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2
- Security fix for CVE-2016-2120, CVE-2016-7068, CVE-2016-7072, CVE-2016-7073, CVE-2016-7074

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.1-3
- Add upstream patch to fix build with openssl 1.1.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.1-3
- Rebuild for protobuf 3.1.0

* Tue Aug 23 2016 Richard Shaw <hobbes1069@gmail.com> - 4.0.1-2
- Rebuild for updated yaml-cpp

* Fri Jul 29 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Mon Jul 11 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.0.0-2
- Enable reproducible builds

* Mon Jul 11 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Wed Jun 29 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.8.rc2
- Update to 4.0.0 RC2

* Fri May 27 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.7.beta1
- Update to 4.0.0 beta 1

* Fri May 13 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.6.alpha3
- Update to 4.0.0 alpha 3

* Wed Mar 02 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.5.alpha2
- Added mariadb-devel build dependency
- Added own systemd unit file
- Remove cryptopp-devel build dependency
- Reenable %%check

* Fri Feb 26 2016 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.4.alpha2
- Update to 4.0.0 alpha 2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.3.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 4.0.0-0.2.alpha1
- Rebuilt for Boost 1.60

* Sun Dec 27 2015 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.1.alpha1
- Update to 4.0.0 (Technical Preview)
- Backend geo and lmdb has been deprecated
- Reenable mbedtls build dependency
- Temporary disable %%check

* Sat Nov 07 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.7-1
- Update to 3.4.7

* Thu Sep 03 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.6-2
- Rebuilt for Boost 1.59

* Wed Sep 02 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.4.6-1
- Upstream released new version, containing fix for CVE-2015-5230
- Remove dnsdist, it is now a separate project

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.5-9
- Rebuilt for Boost 1.59

* Wed Aug 26 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.5-8
- Rebuilt for NVR bump on F23 branch

* Fri Jul 31 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.5-7
- Switch to pkgdocdir

* Fri Jul 31 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.5-6
- Mbedtls build dep temporary disabled due build issues

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.4.5-4
- rebuild for Boost 1.58

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 3.4.5-3
- rebuilt for new zeromq 4.1.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.5-1
- Update to 3.4.5
- Added mbedtls-devel as build dep

* Mon Apr 27 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.4-1
- Update to 3.4.4
- CVE-2015-1868
- Remove polarssl-devel as build dependency

* Mon Mar 02 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.3-1
- Update to 3.4.3

* Tue Feb 17 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.2-2
- Rename zone2ldap to pdns-zone2ldap (#1193116)
- Remove rpath workaround

* Sat Feb 07 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.4.2-1
- Update to 3.4.2
- Disable security status polling by default

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.4.1-2
- Rebuild for boost 1.57.0

* Mon Nov 03 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1
- Enable security status polling

* Fri Oct 10 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.4.0-5
- Run the unit tests during check

* Mon Oct 06 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.0-4
- Enable backend LMDB

* Mon Oct 06 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.0-3
- Remove unused build dependency

* Thu Oct 02 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.0-2
- Enable backend: GeoIP, MyDNS, TinyDNS

* Tue Sep 30 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Tue Sep 23 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.0-0.3.rc2
- Update to 3.4.0-rc2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.4.0-0.1.rc1
- Update to 3.4.0-rc1
- Enable zeromq remote backend

* Mon Jul 14 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.3.1-6
- Rebuild for PolarSSL 1.3.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.3.1-4
- Rebuild for boost 1.55.0

* Fri May 02 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.3.1-3
- Rebuild for PolarSSL 1.3.6

* Mon Mar 17 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.3.1-2
- Enable OpenDBX backend, thanks to Jean-Eudes Onfray (rhbz#1075490)

* Tue Dec 17 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3.1-1
- Update to latest upstream release 3.3.1
- Add LUA backend
- Add polarssl-devel as build dependency

* Sun Oct 13 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-6
- Enable remotebackend-http

* Sat Aug 31 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-5
- Add patch to fix Remote backend

* Wed Aug 21 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-4
- Add Remote backend

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 3.3-2
- Rebuild for boost 1.54.0

* Fri Jul 05 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-1
- Update to 3.3

* Fri Jun 28 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-0.3.rc2
- Update to 3.3-rc2
- Add extra tools package for pdns

* Tue Jun 04 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-0.2.rc1
- Update systemd unit file
- Spec cleanup

* Tue May 28 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-0.1.rc1
- Update to 3.3-rc1

* Mon Apr 22 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.2-7
- Disarm dead code that causes gcc crashes on ARM (rhbz#954191)

* Tue Apr 09 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.2-6
- Add support for aarch64 (rhbz#926316)

* Tue Mar 05 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.2-5
- Enable hardened build as per http://fedoraproject.org/wiki/Packaging:Guidelines#PIE

* Mon Feb 11 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.2-4
- Enable PrivateTmp as per http://fedoraproject.org/wiki/Features/ServicesPrivateTmp
- Fix bogus date in changelog

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.2-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.2-2
- Rebuild for Boost-1.53.0

* Thu Jan 17 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.2-1
- Update to 3.2

* Mon Jan 07 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.1-7
- Disable pdns guardian by default (rhbz#883852)
- Drop backend MongoDB as it does not work (upstream commit 3017)

* Thu Nov 22 2012 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1-6
- Add example schemas to documentation

* Fri Oct 19 2012 Morten Stevens <mstevens@fedoraproject.org> - 3.1-5
- Fixed permissions of pdns.conf file (rhbz#646510)
- Set bind as default backend

* Mon Sep 24 2012 Morten Stevens <mstevens@fedoraproject.org> - 3.1-4
- use new systemd rpm macros (rhbz#850266)

* Mon Sep 24 2012 Morten Stevens <mstevens@fedoraproject.org> - 3.1-3
- Fix pdns daemon exit code (rhbz#859898)
- Update systemd unit file

* Tue Sep 18 2012 Morten Stevens <mstevens@fedoraproject.org> - 3.1-2
- Fix MongoDB backend

* Mon Sep 17 2012 Morten Stevens <mstevens@fedoraproject.org> - 3.1-1
- Update to 3.1
- Remove MongoDB backend due build problems

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for c++ ABI breakage

* Mon Jan 09 2012 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0.1-1
- CVE-2012-0206

* Sun Aug 07 2011 Dan Horák <dan@danny.cz> - 3.0-7
- mongodb supports only x86

* Mon Jul 25 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0-6
- Upstream released new version

* Wed Jul 20 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0-5.rc3
- New release candidate
- Add MongoDB backend
- Enable LUA support
- Convert to systemd

* Sat Apr 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0-4.pre.20110327.2103.fc16
- Rebuilt for new boost

* Mon Mar 28 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0-3.pre.20110327.2103
- License file moved a directory up
- Add pdnssec and dnsreplay commands

* Mon Mar 28 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0-2.pre.20110327.2103
- Add lua BuildRequires

* Mon Mar 28 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.0-1.pre.20110327.2103
- Upstream released new pre-release version
- Now with DNSSEC support
- Drop merged patches

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 2.9.22-13
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Mar 23 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-12
- Rebuilt for new mysqlclient

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-10
- Fix crash on SIGSTOP and SIGCONT, thanks to Anders Kaseorg (#652841)

* Thu Jan 14 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-9
- Fix changelog entry

* Thu Jan 14 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-8
- Fix postgres lib detection (#555462)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.9.22-7
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 2.9.22-5
- Fix build with gcc4.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-3
- Upstream released new version

* Fri Jan 23 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-2.rc3
- Rebuild for new libmysqlclient

* Mon Jan 19 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-1.rc3
- New release candidate

* Wed Dec 03 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.22-1.rc2
- Upstream released new release candidate
- Drop patches which are upstreamed

* Mon Nov 17 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21.2-1
- Upstream released new version

* Fri Sep 12 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21.1-2
- Fix handling of AAAA records (bz #461768)

* Wed Aug 06 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21.1-1
- CVE-2008-3337

* Sat Feb 09 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21-4
- GCC 4.3 fixes

* Wed Dec 05 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21-3
- Rebuild to pick up new openldap

* Tue Sep 11 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21-2
- Fix license tag
- Add README for geo backend to docs

* Tue Apr 24 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.9.21-1
- Upstream released 2.9.21
- Enabled new SQLite backend

* Tue Apr 10 2007 <ruben@rubenkerkhof.com> 2.9.20-9
- Add Requires for chkconfig, service and useradd (#235582)

* Mon Jan 1 2007 <ruben@rubenkerkhof.com> 2.9.20-8
- Add the pdns user and group to the config file
- Don't restart pdns on an upgrade
- Minor cleanups in scriptlets

* Mon Jan 1 2007 <ruben@rubenkerkhof.com> 2.9.20-7
- Fixed typo in scriptlet

* Mon Jan 1 2007 <ruben@rubenkerkhof.com> 2.9.20-6
- Check if user pdns exists before adding it

* Sat Dec 30 2006 <ruben@rubenkerkhof.com> 2.9.20-5
- Strip rpath from the backends as well

* Fri Dec 29 2006 <ruben@rubenkerkhof.com> 2.9.20-4
- Disable rpath

* Thu Dec 28 2006 <ruben@rubenkerkhof.com> 2.9.20-3
- More fixes as per review #219973

* Wed Dec 27 2006 <ruben@rubenkerkhof.com> 2.9.20-2
- A few changes for FE review (bz #219973):
- Renamed package to pdns, since that's how upstream calls it
- Removed calls to ldconfig
- Subpackages now require %%{version}-%%{release}

* Sat Dec 16 2006 <ruben@rubenkerkhof.com> 2.9.20-1
- Initial import
