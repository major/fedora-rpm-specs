Name:           coturn
Version:        4.6.3
Release:        2%{?dist}
Summary:        TURN/STUN & ICE Server
# MIT (src/{apps/relay/acme.c,server/ns_turn_khash.h} and BSD-3-Clause (the rest)
License:        BSD-3-Clause AND MIT
URL:            https://github.com/coturn/coturn/
Source0:        https://github.com/coturn/coturn/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        coturn.service
Source2:        coturn.tmpfilesd
Source3:        coturn.logrotate
Source4:        coturn.sysusersd

BuildRequires:  gcc
BuildRequires:  hiredis-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
Recommends:     perl-interpreter
Recommends:     perl(DBI)
Recommends:     perl(HTTP::Request::Common)
Recommends:     perl(strict)
Recommends:     perl(warnings)
Recommends:     telnet
Provides:       turnserver = %{version}
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
The Coturn TURN Server is a VoIP media traffic NAT traversal server and gateway.
It can be used as a general-purpose network traffic TURN server/gateway, too.

This implementation also includes some extra features. Supported RFCs:

TURN specs:
- RFC 5766 - base TURN specs
- RFC 6062 - TCP relaying TURN extension
- RFC 6156 - IPv6 extension for TURN
- Experimental DTLS support as client protocol.

STUN specs:
- RFC 3489 - "classic" STUN
- RFC 5389 - base "new" STUN specs
- RFC 5769 - test vectors for STUN protocol testing
- RFC 5780 - NAT behavior discovery support

The implementation fully supports the following client-to-TURN-server protocols:
- UDP (per RFC 5766)
- TCP (per RFC 5766 and RFC 6062)
- TLS (per RFC 5766 and RFC 6062); TLS1.0/TLS1.1/TLS1.2
- DTLS (experimental non-standard feature)

Supported relay protocols:
- UDP (per RFC 5766)
- TCP (per RFC 6062)

Supported user databases (for user repository, with passwords or keys, if
authentication is required):
- SQLite
- MySQL
- PostgreSQL
- Redis

Redis can also be used for status and statistics storage and notification.

Supported TURN authentication mechanisms:
- long-term
- TURN REST API (a modification of the long-term mechanism, for time-limited
  secret-based authentication, for WebRTC applications)

The load balancing can be implemented with the following tools (either one or a
combination of them):
- network load-balancer server
- DNS-based load balancing
- built-in ALTERNATE-SERVER mechanism.


%package        utils
Summary:        Coturn utils

%description    utils
This package contains the TURN client utils.


%package        client-libs
Summary:        TURN client static library

%description    client-libs
This package contains the TURN client static library.


%package        client-devel
Summary:        Coturn client development headers

%description    client-devel
This package contains the TURN client development headers.


%prep
%setup -q

# NOTE: Use Fedora Default Ciphers
sed -i \
    -e 's|#define DEFAULT_CIPHER_LIST "DEFAULT"|#define DEFAULT_CIPHER_LIST "PROFILE=SYSTEM"|g' \
    src/apps/relay/mainrelay.h
sed -i \
    -e 's|*csuite = "ALL"; //"AES256-SHA" "DH"|*csuite = "PROFILE=SYSTEM"; // Fedora Defaults|g' \
    src/apps/uclient/mainuclient.c


%build
%configure \
    --confdir=%{_sysconfdir}/%{name} \
    --examplesdir=%{_docdir}/%{name} \
    --schemadir=%{_datadir}/%{name} \
    --manprefix=%{_datadir} \
    --docdir=%{_docdir}/%{name} \
    --turndbdir=%{_localstatedir}/lib/%{name} \
    --disable-rpath
%make_build


%install
%make_install
mkdir -p %{buildroot}{%{_sysconfdir}/pki/coturn/{public,private},{%{_rundir},%{_localstatedir}/{lib,log}}/%{name}}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/coturn.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/coturn.conf
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/coturn.conf
sed -i \
    -e "s|^syslog$|#syslog|g" \
    -e "s|^#*log-file=.*|log-file=/var/log/coturn/turnserver.log|g" \
    -e "s|^#*simple-log|simple-log|g" \
    -e "s|^#*cert=.*|#cert=/etc/pki/coturn/public/turn_server_cert.pem|g" \
    -e "s|^#*pkey=.*|#pkey=/etc/pki/coturn/private/turn_server_pkey.pem|g" \
    %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
touch -c -r examples/etc/turnserver.conf %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
mv %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf
# NOTE: Removing sqlite db, certs and keys
rm %{buildroot}%{_localstatedir}/lib/%{name}/turndb
rm %{buildroot}%{_docdir}/%{name}/etc/{cacert,turn_{client,server}_{cert,pkey}}.pem
rm %{buildroot}%{_docdir}/%{name}/etc/coturn.service


%check
make test

# Check if turnserver is really linked against MariaDB, PostgreSQL and systemd,
# because ./configure unfortunately has no proper failure mechanism...
ldd %{buildroot}%{_bindir}/turnserver | grep -q libmariadb.so
ldd %{buildroot}%{_bindir}/turnserver | grep -q libpq.so
ldd %{buildroot}%{_bindir}/turnserver | grep -q libsystemd.so


%pre
%sysusers_create_compat %{SOURCE4}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%{_bindir}/turnserver
%{_bindir}/turnadmin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.redis
%{_datadir}/%{name}/*.sql
%{_datadir}/%{name}/*.sh
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.*
%exclude %{_docdir}/%{name}/README.turnutils
%exclude %{_docdir}/%{name}/INSTALL
%exclude %{_docdir}/%{name}/LICENSE
%exclude %{_docdir}/%{name}/postinstall.txt
%dir %{_docdir}/%{name}/etc
%doc %{_docdir}/%{name}/etc/*
%dir %{_docdir}/%{name}/scripts
%dir %{_docdir}/%{name}/scripts/*
%{_docdir}/%{name}/scripts/*.sh
%{_docdir}/%{name}/scripts/readme.txt
%doc %{_docdir}/%{name}/scripts/*/*
# NOTE: These schema files are installed twice. Excluding copies in docs.
%exclude %doc %{_docdir}/%{name}/schema.mongo.sh
%exclude %doc %{_docdir}/%{name}/schema.sql
%exclude %doc %{_docdir}/%{name}/schema.stats.redis
%exclude %doc %{_docdir}/%{name}/schema.userdb.redis
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/turnserver.1.*
%{_mandir}/man1/turnadmin.1.*
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/turnserver.conf
%dir %{_sysconfdir}/pki/%{name}
%dir %{_sysconfdir}/pki/%{name}/public
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/private
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}


%files utils
%license LICENSE
%{_bindir}/turnutils_peer
%{_bindir}/turnutils_stunclient
%{_bindir}/turnutils_uclient
%{_bindir}/turnutils_oauth
%{_bindir}/turnutils_natdiscovery
%doc %{_docdir}/%{name}/README.turnutils
%{_mandir}/man1/turnutils.1.*
%{_mandir}/man1/turnutils_*.1.*


%files client-libs
%license LICENSE
%{_libdir}/libturnclient.a


%files client-devel
%license LICENSE
%dir %{_includedir}/turn
%{_includedir}/turn/*.h
%dir %{_includedir}/turn/client
%{_includedir}/turn/client/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Robert Scheck <robert@fedoraproject.org> - 4.6.3-1
- Upgrade to 4.6.3 (#2331737)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 11 2024 Kevin Fenzi <kevin@scrye.com> - 4.6.2-7
- rebuild for hiredis soname bump

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Robert Scheck <robert@fedoraproject.org> - 4.6.2-4
- Build on Fedora and modern EPEL against mariadb-connector-c-devel
  and libpq-devel packages (#2241091, thanks to Michal Schorm)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 01 2023 Robert Scheck <robert@fedoraproject.org> - 4.6.2-2
- Change systemd start-up type from forking to notify (#2207847)

* Sat Apr 15 2023 Robert Scheck <robert@fedoraproject.org> - 4.6.2-1
- Upgrade to 4.6.2 (#2186297)

* Thu Jan 19 2023 Robert Scheck <robert@fedoraproject.org> - 4.6.1-3
- Added upstream patch to fix OpenSSL 3 support 

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 04 2022 Robert Scheck <robert@fedoraproject.org> - 4.6.1-1
- Upgrade to 4.6.1 (#2150608)

* Tue Nov 22 2022 Robert Scheck <robert@fedoraproject.org> - 4.6.0-2
- Include CAP_NET_BIND_SERVICE in the ambient capability set (to
  bind to privileged ports due to restrictive corporate firewalls)

* Wed Sep 14 2022 Robert Scheck <robert@fedoraproject.org> - 4.6.0-1
- Upgrade to 4.6.0 (#2126875)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 04 2022 Christian Glombek <lorbus@fedoraproject.org> - 4.5.2-10
- Provide a sysusers.d file to get user() and group() provides
  (see https://fedoraproject.org/wiki/Changes/Adopting_sysusers.d_format).

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Kevin Fenzi <kevin@scrye.com> - 4.5.2-8
- Rebuild for hiredis 1.0.2

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.5.2-7
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 10 2021 Robert Scheck <robert@fedoraproject.org> - 4.5.2-6
- Unbreak MariaDB/PostgreSQL support on RHEL/CentOS 7 (#1991456)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.5.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 4.5.2-3
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Robert Scheck <robert@fedoraproject.org> - 4.5.2-1
- Upgrade to 4.5.2 (#1914861)

* Sun Sep 27 2020 Christian Glombek <lorbus@fedoraproject.org> - 4.5.1.3-3
- Rebuilt for libevent 2.1.12 soname bump

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Robert Scheck <robert@fedoraproject.org> - 4.5.1.3-1
- Update to 4.5.1.3

* Sat May 16 2020 Robert Scheck <robert@fedoraproject.org> - 4.5.1.2-1
- Update to 4.5.1.2

* Mon Mar 23 2020 Robert Scheck <robert@fedoraproject.org> - 4.5.1.1-3
- Added upstream patch for CVE-2020-6061 (#1816159)
- Backported upstream patch for CVE-2020-6062 (#1816163)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Robert Scheck <robert@fedoraproject.org> - 4.5.1.1-1
- Update to 4.5.1.1

* Fri Jul 26 2019 Robert Scheck <robert@fedoraproject.org> - 4.5.1.0-3
- Added patch to append only to log files rather to override always
- Relocate SQLite database to FHS conform /var/lib/coturn/turndb path
- Include default log file directory with logrotate configuration
- Provide /run/coturn and correct PID file handling (#1705146)
- Ensure private keys for SSL certs can be only read by coturn user
- Ensure /etc/coturn/turnserver.conf can be only read by coturn user
- Correct subpackage licensing as per Fedora Packaging Guidelines

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Christian Glombek <lorbus@fedoraproject.org> - 4.5.1.0-1
- Initial Fedora Package
- Update to 4.5.1.0
- Introduce consistent naming, rename service to coturn
- Add configure, make and systemd macros
- Remove dependencies on mariadb, mysql, postgresql and sqlite
- Forked from https://github.com/coturn/coturn/blob/af674368d120361603342ff4ff30b44f147a38ff/rpm/turnserver.spec
