%global ivykis_ver 0.42.3

%global syslog_ng_major_ver 4
%global syslog_ng_minor_ver 8
%global syslog_ng_patch_ver 1
%global syslog_ng_major_minor_ver %{syslog_ng_major_ver}.%{syslog_ng_minor_ver}
%global syslog_ng_ver %{syslog_ng_major_ver}.%{syslog_ng_minor_ver}.%{syslog_ng_patch_ver}

Name:    syslog-ng
Version: %{syslog_ng_ver}
Release: 2%{?dist}
Summary: Next-generation syslog server

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://www.syslog-ng.com/products/open-source-log-management/
Source0: https://github.com/balabit/syslog-ng/releases/download/syslog-ng-%{version}/%{name}-%{version}.tar.gz
Source1: syslog-ng.conf
Source2: syslog-ng.logrotate
Source3: syslog-ng.service

BuildRequires: make
BuildRequires: bison
BuildRequires: cyrus-sasl-devel
BuildRequires: flex
BuildRequires: glib2-devel
BuildRequires: hiredis-devel
BuildRequires: ivykis-devel >= %{ivykis_ver}
BuildRequires: json-c-devel
BuildRequires: libcap-devel
BuildRequires: libcurl-devel
BuildRequires: libdbi-devel
BuildRequires: libesmtp-devel
BuildRequires: libmaxminddb-devel
BuildRequires: libnet-devel
BuildRequires: librabbitmq-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: libxslt
BuildRequires: mongo-c-driver-devel
BuildRequires: net-snmp-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: riemann-c-client-devel
BuildRequires: snappy-devel
BuildRequires: systemd-devel
BuildRequires: systemd-units
BuildRequires: librdkafka-devel
BuildRequires: zlib-devel
BuildRequires: paho-c-devel

BuildRequires: python3-pip
BuildRequires:  python3-cachetools
BuildRequires:  python3-certifi
BuildRequires:  python3-charset-normalizer
BuildRequires:  python3-google-auth
BuildRequires:  python3-idna
BuildRequires:  python3-kubernetes
BuildRequires:  python3-oauthlib
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-dateutil
BuildRequires:  python3-PyYAML
BuildRequires:  python3-requests
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-rsa
BuildRequires:  python3-six
BuildRequires:  python3-urllib3
BuildRequires:  python3-websocket-client
BuildRequires:  python3-boto3
BuildRequires:  python3-botocore

%ifarch i686
%bcond_with bpf
%bcond_with grpc
%bcond_with examples
%else
%bcond_without bpf
%bcond_without grpc
%bcond_without examples
%endif

%if %{with bpf}
BuildRequires: libbpf-devel
BuildRequires: bpftool
BuildRequires: clang
%endif

%if %{with grpc}
BuildRequires:  grpc-devel
BuildRequires:  protobuf-devel
BuildRequires:  gcc-c++
%endif

Requires: logrotate
Requires: ivykis >= %{ivykis_ver}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

Provides: syslog

# Fedora 17’s unified filesystem (/usr-move)
Conflicts: filesystem < 3

Obsoletes: syslog-ng-json < 3.8


%description
syslog-ng is an enhanced log daemon, supporting a wide range of input and
output methods: syslog, unstructured text, message queues, databases (SQL
and NoSQL alike) and more.

Key features:

 * receive and send RFC3164 and RFC5424 style syslog messages
 * work with any kind of unstructured data
 * receive and send JSON formatted messages
 * classify and structure logs with builtin parsers (csv-parser(),
   db-parser(), ...)
 * normalize, crunch and process logs as they flow through the system
 * hand on messages for further processing using message queues (like
   AMQP), files or databases (like PostgreSQL or MongoDB).


%package slog
Summary: secure logging support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description slog
This module supports secure message transfer and storage (experimental).

%package libdbi
Summary: Libdbi support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libdbi
This module supports a large number of database systems via libdbi.


%package mongodb
Summary: MongoDB support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mongodb
This module supports the mongodb database via libmongo-client.

%package kafka
Summary: Kafka support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description kafka
This module supports sending logs to Kafka through librdkafka.


%package smtp
Summary: SMTP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description smtp
This module supports sending e-mail alerts through an smtp server.


%package snmp
Summary: SNMP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description snmp
This module adds support for SNMP destination.


%package geoip
Summary: GeoIP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description geoip
This template function returns the 2-letter country code of
any IPv4 address or host.


%package redis
Summary: Redis support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description redis
This module supports the redis key-value store via hiredis.


%package riemann
Summary: Riemann support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description riemann
This module supports the riemann monitoring server.


%package http
Summary: HTTP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-curl < 3.10

%description http
This module supports the http destination.

%package grpc
Summary: GRPC support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description grpc
This module supports the GRPC, a common requirement
for OpenTelemetry and Loki support.


%package opentelemetry
Summary: OpenTelemetry support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description opentelemetry
This module adds OpenTelemetry support.

%package loki
Summary: Loki support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description loki
This module adds loki support.

%package bigquery
Summary: Google BigQuery support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description bigquery
This module adds Google BigQuery support.


%package bpf
Summary: Faster UDP log collection for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description bpf
This module provides faster UDP log collection using bpf.


%package amqp
Summary: AMQP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description amqp
This module supports the AMQP destination.

%package mqtt
Summary: mqtt support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mqtt
This module supports sending logs to MQTT through paho-c.

%package python
Summary: Python support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: python3-syslog-ng < 3.22

%description python
This package provides python support for syslog-ng.

%package python-modules
Summary:        Python-based drivers for syslog-ng
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       %{name}-python
Requires:  python3-cachetools
Requires:  python3-certifi
Requires:  python3-charset-normalizer
Requires:  python3-google-auth
Requires:  python3-idna
Requires:  python3-kubernetes
Requires:  python3-oauthlib
Requires:  python3-pyasn1
Requires:  python3-pyasn1-modules
Requires:  python3-dateutil
Requires:  python3-PyYAML
Requires:  python3-requests
Requires:  python3-requests-oauthlib
Requires:  python3-rsa
Requires:  python3-six
Requires:  python3-urllib3
Requires:  python3-websocket-client

%description python-modules
This package provides Python-based (Kubernetes, Hypr) drivers for syslog-ng.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p 1

# Remove bundled libraries
rm -rf lib/ivykis
rm -rf modules/afamqp/rabbitmq-c
rm -rf modules/afmongodb/mongo-c-driver

# fix perl path
sed -i 's|^#!/usr/local/bin/perl|#!%{__perl}|' contrib/relogger.pl

# fix executable perms on contrib files
chmod -c a-x contrib/syslog2ng

# fix authors file
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
    mv -f AUTHORS.conv AUTHORS

# Fix python shebang
%py3_shebang_fix lib/merge-grammar.py
touch -r lib/cfg-grammar.y lib/merge-grammar.py

%build
%configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --localstatedir=%{_sharedstatedir}/%{name} \
    --datadir=%{_datadir} \
    --with-module-dir=%{_libdir}/%{name} \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-ivykis=system \
    --with-mongoc=system \
    --with-embedded-crypto \
    --enable-manpages \
    --enable-ipv6 \
    --enable-spoof-source \
    --with-linux-caps=auto \
    --enable-sql \
    --enable-kafka \
    --enable-mqtt \
    --enable-json \
    --enable-ssl \
    --enable-smtp \
    --enable-geoip \
    --enable-shared \
    --disable-static \
    --enable-dynamic-linking \
    --enable-systemd \
    --enable-redis \
    --enable-amqp \
    --enable-python \
    --with-python=3 \
    --with-python-packages=system \
    --disable-java \
    --disable-java-modules \
    --enable-afsnmp \
%if %{with examples}
    --enable-example-modules \
%else
    --disable-example-modules \
%endif
%if %{with grpc}
    --enable-cpp --enable-grpc \
%endif
%if %{with bpf}
    --enable-ebpf \
%endif
    --enable-riemann

%make_build


%install
%make_install

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/syslog-ng.conf

install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/syslog

install -d -m 755 %{buildroot}%{_prefix}/lib/systemd/system
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service

# create the local state dir
install -d -m 755 %{buildroot}/%{_sharedstatedir}/%{name}

# install the main library header files
install -d -m 755 %{buildroot}%{_includedir}/%{name}
install -p -m 644 config.h %{buildroot}%{_includedir}/%{name}
install -p -m 644 lib/*.h %{buildroot}%{_includedir}/%{name}

find %{buildroot} -name "*.la" -exec rm -f {} \;

# remove some extra testing related files
rm %{buildroot}%{_unitdir}/%{name}@.service


%post
ldconfig
%systemd_post syslog-ng.service


%preun
%systemd_preun syslog-ng.service


%postun
ldconfig
%systemd_postun_with_restart syslog-ng.service


%triggerun -- syslog-ng < 3.2.3
if /sbin/chkconfig --level 3 %{name} ; then
    /bin/systemctl enable %{name}.service >/dev/null 2>&1 || :
fi

%files
%doc AUTHORS COPYING NEWS.md
%doc contrib/{relogger.pl,syslog2ng,syslog-ng.conf.doc}

%dir %{_sysconfdir}/syslog-ng
%dir %{_sysconfdir}/syslog-ng/conf.d
%dir %{_sysconfdir}/syslog-ng/patterndb.d
%config(noreplace) %{_sysconfdir}/logrotate.d/syslog
%config(noreplace) %{_sysconfdir}/syslog-ng/syslog-ng.conf

%{_unitdir}/syslog-ng.service

%dir %{_sharedstatedir}/syslog-ng

%{_sbindir}/syslog-ng
%{_sbindir}/syslog-ng-ctl
%{_sbindir}/syslog-ng-debun

%{_bindir}/dqtool
%{_bindir}/loggen
%{_bindir}/pdbtool
%{_bindir}/persist-tool
%{_bindir}/update-patterndb
%{_bindir}/syslog-ng-update-virtualenv

%{_libdir}/libevtlog-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libevtlog-%{syslog_ng_major_minor_ver}.so.0.0.0
%{_libdir}/libloggen_helper-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libloggen_helper-%{syslog_ng_major_minor_ver}.so.0.0.0
%{_libdir}/libloggen_plugin-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libloggen_plugin-%{syslog_ng_major_minor_ver}.so.0.0.0
%{_libdir}/libsecret-storage.so.0
%{_libdir}/libsecret-storage.so.0.0.0
%{_libdir}/libsyslog-ng-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libsyslog-ng-%{syslog_ng_major_minor_ver}.so.0.0.0

%dir %{_libdir}/syslog-ng
%{_libdir}/syslog-ng/*.so

%dir %{_libdir}/syslog-ng/loggen
%{_libdir}/syslog-ng/loggen/libloggen_socket_plugin.so
%{_libdir}/syslog-ng/loggen/libloggen_ssl_plugin.so

%exclude %{_libdir}/syslog-ng/libafamqp.so
%exclude %{_libdir}/syslog-ng/libafmongodb.so
%exclude %{_libdir}/syslog-ng/libafsmtp.so
%exclude %{_libdir}/syslog-ng/libafsql.so
%exclude %{_libdir}/syslog-ng/libgeoip2-plugin.so
%exclude %{_libdir}/syslog-ng/libhttp.so
%exclude %{_libdir}/syslog-ng/libmod-python.so
%exclude %{_libdir}/syslog-ng/libredis.so
%exclude %{_libdir}/syslog-ng/libriemann.so
%exclude %{_libdir}/syslog-ng/libafsnmp.so
%exclude %{_libdir}/syslog-ng/libkafka.so
%exclude %{_libdir}/syslog-ng/libotel.so
%exclude %{_libdir}/syslog-ng/libmqtt.so
%exclude %{_libdir}/syslog-ng/libebpf.so
%exclude %{_libdir}/syslog-ng/libotel.so
%exclude %{_libdir}/syslog-ng/libloki.so
%exclude %{_libdir}/syslog-ng/libbigquery.so
%exclude %{_libdir}/syslog-ng/libcloud_auth.so

%dir %{_datadir}/%{name}

# scl files
%{_datadir}/syslog-ng/include/

# uhm, some better places for those?
%{_datadir}/syslog-ng/xsd/

%{_datadir}/syslog-ng/smart-multi-line.fsm

%{_mandir}/man1/loggen.1*
%{_mandir}/man1/pdbtool.1*
%{_mandir}/man1/syslog-ng-ctl.1*
%{_mandir}/man1/syslog-ng-debun.1*
%{_mandir}/man1/dqtool.1*
%{_mandir}/man5/syslog-ng.conf.5*
%{_mandir}/man8/syslog-ng.8*
%{_mandir}/man1/persist-tool.1*


%files slog
%{_bindir}/slogkey
%{_bindir}/slogencrypt
%{_bindir}/slogverify
%{_libdir}/syslog-ng/libsecure-logging.so
%{_mandir}/man1/slogkey.1*
%{_mandir}/man1/slogencrypt.1*
%{_mandir}/man1/slogverify.1*
%{_mandir}/man7/secure-logging.7*

%if %{with grpc}

%files grpc
%{_libdir}/libgrpc-protos.*

%files opentelemetry
%{_libdir}/%{name}/libotel.so

%files loki
%{_libdir}/%{name}/libloki.so

%files bigquery
%{_libdir}/%{name}/libbigquery.so
%endif

%if %{with cloudauth}
%files cloudauth
%{_libdir}/%{name}/libcloud_auth.so

%endif


%files libdbi
%{_libdir}/syslog-ng/libafsql.so

%files kafka
%{_libdir}/%{name}/libkafka.so

%files mongodb
%{_libdir}/syslog-ng/libafmongodb.so


%files redis
%{_libdir}/syslog-ng/libredis.so

%files mqtt
%{_libdir}/%{name}/libmqtt.so

%files smtp
%{_libdir}/syslog-ng/libafsmtp.so

%files snmp
%{_libdir}/%{name}/libafsnmp.so


%files geoip
%{_libdir}/syslog-ng/libgeoip2-plugin.so


%files riemann
%{_libdir}/syslog-ng/libriemann.so


%files http
%{_libdir}/syslog-ng/libhttp.so


%files amqp
%{_libdir}/syslog-ng/libafamqp.so

%if %{with bpf}
%files bpf
%{_libdir}/%{name}/libebpf.so
%endif

%files python
%{_libdir}/%{name}/libmod-python.so
%dir %{_sysconfdir}/%{name}/python
%{_sysconfdir}/%{name}/python/README.md
%{_libdir}/%{name}/python/syslogng-1.0-py%{python3_version}.egg-info
%{_libdir}/%{name}/python/syslogng/*
%{_libdir}/%{name}/python/requirements.txt
%exclude %{_libdir}/syslog-ng/python/syslogng/modules/

%files python-modules
%dir %{_libdir}/syslog-ng/python/syslogng/modules/
%{_libdir}/syslog-ng/python/syslogng/modules/*

%files devel
%{_datadir}/syslog-ng/tools/
%{_includedir}/syslog-ng/
%{_libdir}/libevtlog.so
%{_libdir}/libloggen_helper.so
%{_libdir}/libloggen_plugin.so
%{_libdir}/libsecret-storage.so
%{_libdir}/libsyslog-ng-native-connector.a
%{_libdir}/libsyslog-ng.so
%{_libdir}/pkgconfig/syslog-ng-native-connector.pc
%{_libdir}/pkgconfig/syslog-ng.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Peter Czanik <peter@czanik.hu> - 4.8.1-1
- update to 4.8.1
- it is a bug fix release fixing many bugs reported upstream

* Mon Sep 02 2024 Peter Czanik <peter@czanik.hu> - 4.8.0-3
- re-enable modules based on GRPC
- merge spec modernization fixes from carlwgeorge

* Wed Aug 14 2024 Peter Czanik <peter@czanik.hu> - 4.8.0-2
- disable modules based on GRPC (rhbz#2304731)

* Fri Jul 26 2024 Peter Czanik <peter@czanik.hu> - 4.8.0-1
- update to 4.8.0
- re-enable eBPF support
- remove patch fixing 32 builds (it was mreged upstream)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.6.0-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.6.0-6
- Rebuilt for Python 3.13

* Sat May 11 2024 Kevin Fenzi <kevin@scrye.com> - 4.6.0-5
- rebuild for hiredis soname bump

* Sat Feb 24 2024 Paul Wouters <paul.wouters@aiven.io> - 4.6.0-4
- Rebuilt for libre2.so.11 bump

* Tue Feb 06 2024 Peter Czanik <peter@czanik.hu> - 4.6.0-3
- fix 32bit problem with 4816.patch

* Mon Feb 05 2024 Peter Czanik <peter@czanik.hu> - 4.6.0-2
- rebuild for abseil-cpp-20240116.0-1

* Mon Feb 05 2024 Peter Czanik <peter@czanik.hu> - 4.6.0-1
- update to 4.6.0
- disable eBPF support for now as bpftool is removed from Fedora :/
- updated Python dependencies
- added many new parsers (SCL)
- new GRPC-based drivers, reorganized support
- removed VIM support, as it was removed upstream. Now available
  separately at: https://github.com/syslog-ng/vim-syslog-ng
- excludeArch x86 until a 32bit compile bug is fixed

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Peter Czanik <peter@czanik.hu> - 4.3.1-3
- fix excludes, making sure that the base package pulls
  only minimal dependencies

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.3.1-2
- Rebuilt for abseil-cpp 20230802.0

* Mon Jul 31 2023 Peter Czanik <peter@czanik.hu> - 4.3.1-1
- update to 4.3.1 (bugfix release)
- add opensearch support to SCL

* Mon Jul 24 2023 Peter Czanik <peter@czanik.hu> - 4.3.0-3
- update to 4.3.0
- pcre -> pcre2
- add bpf and opentelemetry support
- make bpf and opentelemetry conditional, exclude on i686

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.12

* Thu Jun 01 2023 Peter Czanik <peter@czanik.hu> - 4.2.0-1
- update to 4.2.0
- update vim support
- split Python-based drivers from the Python plugin

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Peter Czanik <peter@czanik.hu> - 4.0.1-1
- update to 4.0.1
- add Python dependencies

* Mon Aug 15 2022 Peter Czanik <peter@czanik.hu> - 3.37.1-1
- update to 3.37.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.35.1-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Kevin Fenzi <kevin@scrye.com> - 3.35.1-2
- Rebuild for hiredis 1.0.2

* Mon Dec 06 2021 Peter Czanik <peter@czanik.hu> - 3.35.1-1
- update to 3.35.1

* Sun Nov 07 2021 Björn Esser <besser82@fedoraproject.org> - 3.33.2-3
- Rebuild (riemann-c-client)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.33.2-2
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 28 2021 Peter Czanik <peter@czanik.hu> - 3.33.2-1
- update to 3.33.2
- enabled MQTT support

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 3.30.1-7
- Rebuild for versioned symbols in json-c

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.30.1-6
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.30.1-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Feb  5 2021 Peter Czanik <peter@czanik.hu> - 3.30.1-4
- fix Kafka support packaging

* Mon Feb  1 2021 Peter Czanik <peter@czanik.hu> - 3.30.1-3
- enabled Kafka support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 8 2020 Peter Czanik <peter@czanik.hu> - 3.30.1-0
- update to 3.30.1

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 3.27.1-5
- Rebuilt for new net-snmp release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.27.1-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 15 2020 Peter Czanik <peter@czanik.hu> - 3.27.1-2
- do not mask syslog-ng modules to fix rhbz#1846777

* Wed Jun 10 2020 Peter Czanik <peter@czanik.hu> - 3.27.1-1
- update to 3.27.1
- add secure logging files
- add persist-tool man page
- fix snmp support
- disable Java bindings (requires ancient JDK)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.25.1-4
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 3.25.1-3
- Rebuild (json-c)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Peter Czanik <peter@czanik.hu> - 3.25.1-1
- update to version 3.25.1
- removed GeoIP support: geoip2 (MaxMindDB) stays

* Sun Sep 01 2019 My Karlsson <mk@acc.umu.se> - 3.23.1-1
- Update to version 3.23.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.22.1-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 My Karlsson <mk@acc.umu.se> - 3.22.1-1
- Update to version 3.22.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 My Karlsson <mk@acc.umu.se> - 3.21.1-2
- Exclude unversioned private libraries from Provides: metadata. (rhbz#1726732)

* Sun May 12 2019 My Karlsson <mk@acc.umu.se> - 3.21.1-1
- Update to version 3.21.1

* Sat Mar 02 2019 My Karlsson <mk@acc.umu.se> - 3.20.1-1
- Update to version 3.20.1

* Sun Feb 17 2019 My Karlsson <mk@acc.umu.se> - 3.19.1-2
- Put Python extensions into its own subpackage

* Sat Feb 02 2019 My Karlsson <mk@acc.umu.se> - 3.19.1-1
- Update to version 3.19.1

* Mon Jan 07 2019 My Karlsson <mk@acc.umu.se> - 3.18.1-2
- Backport fix for use after free in affile_dw_reap (rhbz#1663936)

* Sat Nov 17 2018 My Karlsson <mk@acc.umu.se> - 3.18.1-1
- Update to version 3.18.1

* Sun Oct 07 2018 My Karlsson <mk@acc.umu.se> - 3.17.2-2
- Fix ambiguous python shebang

* Sat Aug 11 2018 My Karlsson <mk@acc.umu.se> - 3.17.2-1
- Update to version 3.17.2 (rhbz#1614997)

* Fri Aug 10 2018 My Karlsson <mk@acc.umu.se> - 3.17.1-1
- Update to version 3.17.1 (rhbz#1614581)

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.16.1-6
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.16.1-5
- Rebuild for new binutils

* Thu Jul 26 2018 My Karlsson <mk@acc.umu.se> - 3.16.1-4
- Build with python as /usr/bin/python2 (rhbz#1606471)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 My Karlsson <mk@acc.umu.se> - 3.16.1-2
- Enable the AMQP destination

* Wed Jun 20 2018 My Karlsson <mk@acc.umu.se> - 3.16.1-1
- Update to version 3.16.1

* Fri Jun  8 2018 Remi Collet <remi@remirepo.net> - 3.15.1-3
- rebuild with libbson and libmongc 1.10.2 (soname back to 0)

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 3.15.1-2
- rebuild with libbson and libmongc 1.10.0

* Sat May 05 2018 My Karlsson <mk@acc.umu.se> - 3.15.1-1
- Update to version 3.15.1

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 3.14.1-4
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Thu Mar 01 2018 My Karlsson <mk@acc.umu.se> - 3.14.1-3
- Remove bundled libraries at build time

* Thu Mar 01 2018 My Karlsson <mk@acc.umu.se> - 3.14.1-2
- Disable configuring of rabbitmq-c

* Wed Feb 28 2018 My Karlsson <mk@acc.umu.se> - 3.14.1-1
- Update to upstream release 3.14.1

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.11.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.11.1-6
- Escape macros in %%changelog

* Sat Jan 06 2018 My Karlsson <mk@acc.umu.se> - 3.11.1-5
- Drop support for TCP wrappers (rhbz#1518790)

* Mon Dec 11 2017 Björn Esser <besser82@fedoraproject.org> - 3.11.1-4
- Fix patch for json-c

* Mon Dec 11 2017 Björn Esser <besser82@fedoraproject.org> - 3.11.1-3
- Add patch for building cleanly against json-c v0.13

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 3.11.1-2
- Rebuilt for libjson-c.so.3

* Mon Sep 04 2017 My Karlsson <mk@acc.umu.se> - 3.11.1-1
- Update to upstream release 3.11.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 My Karlsson <mk@acc.umu.se> - 3.10.1-1
- Update to upstream release 3.10.1

* Wed Feb 15 2017 Peter Czanik <peter@czanik.hu> - 3.9.1-1
- update to 3.9.1 (resolves openssl 1.1 compatibility)
- switch mongodb driver
- disable "make check" temporarily
- add pkgconfig file for add-contextual-data

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Peter Czanik <peter@czanik.hu> - 3.8.1-1
- update to 3.8.1
- new URL and source URL (moved to GitHub)
- remove/update obsolated patches
- enable java, curl (HTTP) destinations
- python destination added, but disabled
- merge JSON support to core
- added dependencies for "make test" and new features


* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.6.2-4
- rebuild (hiredis)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Peter Czanik <czanik@balabit.hu> - 3.6.2-2
- rebuild against new hiredis

* Tue Dec 16 2014 Peter Czanik <czanik@balabit.hu> - 3.6.2-1
- update to syslog-ng 3.6.2 (bugfix release)
- disabled "make check" temporarily due to a false positive

* Fri Nov 14 2014 Peter Czanik <czanik@balabit.hu> - 3.6.1-1
- update to syslog-ng 3.6.1
- enable riemann-c-client support

* Fri Sep 26 2014 Peter Czanik <czanik@balabit.hu> - 3.6.0rc1-1
- update to syslog-ng 3.6.0rc1
- removed --enable-pcre, as it's always required
- configuration file version bump to 3.6

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 3.5.6-3
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Peter Czanik <czanik@balabit.hu> - 3.5.6-1
- Update to syslog-ng 3.5.6 (bugfix release)

* Wed Jul 23 2014 Peter Czanik <czanik@balabit.hu> - 3.5.5-1
- Update to syslog-ng 3.5.5 (bugfix release)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Peter Czanik <czanik@balabit.hu> - 3.5.4.1-2
- enable SCL in syslog-ng.conf
- use system() in syslog-ng.conf
- move JSON, SMTP and GeoIP support to separate subpackages
  due to dependencies

* Tue Mar 18 2014 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 3.5.4.1-1
- Update to syslog-ng 3.5.4.1

* Sat Feb 22 2014 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.3-4
- Upstream patch:  add support for the Tzif3 timezone files
  (syslog-ng-3.5.3-support-Tzif3-format-timezone-files.patch)

* Tue Feb 11 2014 Matthias Runge <mrunge@redhat.com> - 3.5.3-3
- rebuild due libdbi bump

* Wed Jan 22 2014 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.3-2
- Bump configuration file version to 3.5
- Rebuild for libdbi soname bump

* Wed Dec 25 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.3-1
- Update to syslog-ng 3.5.3

* Fri Nov 29 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.2-1
- Update to syslog-ng 3.5.2

* Thu Nov 21 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.1-2
- New upstream package description (Balabit; Peter Czanik)

* Mon Nov  4 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.1-1
- Update to syslog-ng 3.5.1 (first stable release of branch 3.5)
- New build requirement: libxslt (--enable-man-pages)

* Thu Oct 24 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.0-0.rc1.1
- Update to syslog-ng 3.5.0 rc 1
- Re-enabled parallel build

* Sat Oct 19 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.5.0-0.beta3.1
- Update to syslog-ng 3.5.0 beta 3
- Updated source0 URL
- syslog-ng.service patch rebased (syslog-ng-3.5.0-syslog-ng.service.patch)
- New BR: systemd-devel
- New subpackage: syslog-ng-redis (new BR: hiredis-devel)
- Disabled parallel build (currently fails)

* Thu Oct 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.4.4-1
- Update to syslog-ng 3.4.4

* Tue Aug 13 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.4.3-1
- Update to syslog-ng 3.4.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.4.1-1
- Update to syslog-ng 3.4.1 (first stable version of branch 3.4)

* Sat Jan 19 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.4.0-0.1.rc2
- Update to syslog-ng 3.4.0 rc2
- Bumped the eventlog version requirement to 0.2.13
- Bumped the ivykis version requirement to 0.36.1
- New build requirement: GeoIP-devel (--enable-geoip)
- New build requirement: libuuid-devel
- New build requirement: libesmtp-devel (--enable-smtp)
- New build requirement: libmongo-client--devel (--with-libmongo-client=system)
- Splitted the mongodb support into a subpackage
- Rebased the syslog-ng-3.2.5-tests-functional-control.py.patch patch
- Disable the AMQP support (until it builds with an external librabbitmq library)

* Sat Jan 19 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.8-2
- Corrected bogus dates in the changelog section

* Thu Jan 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.8-1
- Update to 3.3.8
- Use the new --with-embedded-crypto configure's option in order to
  avoid shipping a ld.so.conf file

* Fri Nov 30 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.7-3
- Introduce the new systemd-rpm macros (#850332)

* Fri Nov 30 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.7-2
- Rename ivykis-ver to ivykis_ver (invalid character)

* Tue Oct 30 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.7-1
- Update to 3.3.7

* Thu Oct 18 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.7-0.1.rc2
- Update to 3.3.7 RC2 (aka syslog-ng-3.3.6.91-20121008-v3.3.6.91.tar.gz)
- Create and own the /etc/syslog-ng/conf.d directory
- syslog-ng.conf: now sources additional configuration files located at
  /etc/syslog-ng/conf.d ; these files must have a .conf extension
- syslog-ng.conf: make the s_sys source more compliant with the one
  generated by generate-system-source.sh
- syslog-ng.conf: retab
- Bump the minimal ivykis version requirement to 0.30.4

* Mon Aug 27 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.3.6-1
- Update to 3.3.6
- Now builds with an external (and unpatched) version of the ivykis library (>= 0.30.1)
- Enable JSON support (BR json-c-devel).
- Enable Linux caps (BR libcap-devel).
- BR bison and flex
- syslog-ng.conf: rename the now obsolete long_hostnames option to chain_hostnames
- install a ld.so conf file so that the private shared library -
  libsyslog-ng-crypto - can be found.
- Unconditionally run "systemctl daemon-reload" on the %%postun scriptlet
  (https://bugzilla.redhat.com/show_bug.cgi?id=700766#c25)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-15
- Remove the ExecStartPre line from the service file (#833551)

* Thu Apr 26 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-14
- Improve syslog-ng-3.2.5-tests-functional-sql-test.patch

* Thu Apr 26 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-13
- Add a conflict with the filesystem package (due to the /usr-move)

* Mon Apr 16 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-12
- No longer disable the SSL tests.

* Mon Apr 16 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-11
- Correct the path in syslog-ng-3.2.5-syslog-ng.service.patch.

* Mon Apr 16 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-10
- Enable SSL.

* Sun Apr 15 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-9
- Fedora 17’s unified filesystem (/usr-move)
  http://fedoraproject.org/wiki/Features/UsrMove

* Sun Apr 15 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-8
- Resolve the file conflict with rsyslog (#811058).
- Don't tag the syslog-ng.service file as a configuration file.

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 3.2.5-7
- Rebuild for updated libnet.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 3.2.5-6
- Rebuild against PCRE 8.30

* Sun Jan 15 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-5
- Improve test coverage: remove a couple of errors and really run the SQL test.
  Patches: syslog-ng-3.2.5-tests-functional-control.py.patch and
  syslog-ng-3.2.5-tests-functional-sql-test.patch.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-3
- Drop the sysconfig configuration file (use syslog-ng.service instead)
- Make the syslog-ng.service file a configuration file
- Drop Vim 7.2 support

* Wed Dec 14 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-2
- Fix the freeze problems caused by the /dev/log unix socket type mismatch (#742624)
  + syslog-ng.conf: change /dev/log from unix-stream to unix-dgram
  + upstream patch syslog-ng-3.3.4-afunix.c-diagnostic-messages.patch
- Move the SCL files to the main RPM (#742624 comments >= 28)

* Tue Nov  1 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.5-1
- Update to 3.2.5

* Tue Oct 25 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-11
- New 3.2.5 pre-release tarball
  https://lists.balabit.hu/pipermail/syslog-ng/2011-October/017491.html
- Updated patch syslog-ng-3.2.5-syslog-ng.service.patch

* Sat Oct 22 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-10
- 3.2.5 pre-release: changelog and tarball from
  https://lists.balabit.hu/pipermail/syslog-ng/2011-October/017462.html
  Patches dropped:
  syslog-ng-3.2.4-systemd-acquired-fd.patch
  syslog-ng-3.2.4-chain-hostnames-processing.patch
- New configure option: --with-systemdsystemunitdir
- Patched the included syslog-ng.service file
  syslog-ng-3.2.5-syslog-ng.service.patch

* Mon Oct 10 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-9
- Patch syslog-ng-3.2.4-systemd-acquired-fd.patch (see bug #742624)

* Mon Oct 10 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-8
- disable linux-caps support for the time being (see bug #718439)

* Wed Aug 31 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-7
- Fixed the syslog-ng.service configuration file:
  * Sockets setting (#734569)
  * StandardOutput setting (#734591)

* Mon Jun 27 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-6
- Patch syslog-ng-3.2.4-chain-hostnames-processing.patch (#713965)

* Mon Jun 20 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-5
- Enabled support for capability management (--enable-linux-caps)

* Tue May 17 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-4
- Enabled SQL support (subpackage syslog-ng-libdbi)

* Mon May 16 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-3
- Updated the homepage URL
- Syslog-ng data directory in %%{_datadir}/%%{name}
- Include the main library header files in the devel subpackage

* Thu May 12 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-2
- No need to create the directory /etc/syslog-ng in the install section
- Enable the test suite (but excluding the SQL and SSL tests)

* Wed May 11 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.4-1
- Update to 3.2.4

* Mon May  9 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-5
- Overrided the default _localstatedir value (configure --localstatedir)
  (value hardcoded in update-patterndb)
- Manually created the patterndb.d configuration directory (update-patterndb)
  (see also https://bugzilla.balabit.com/show_bug.cgi?id=119 comments >= 4)
- Dropped support for Vim 7.0 and 7.1

* Mon May  9 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-4
- Dropped the bison and flex build requirements
- Corrected a couple of macro references in changelog entries (rpmlint)

* Mon May  9 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-3
- Added the build requirement systemd-units (macro %%_unitdir)
  https://fedoraproject.org/wiki/Packaging:Guidelines:Systemd
- Dropped the redefinition of the %%_localstatedir macro
- Use %%global instead of %%define
- Minor modifications of the %%post, %%preun and %%postun scripts
  https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
- Expanded tabs to spaces (also added a vim modeline)

* Fri May  6 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-2
- Fix systemd-related scriptlets (Bill Nottingham)
- Explicitly add --enable-systemd to configure's command line

* Mon May  2 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-1
- updated to 3.2.3 final
- cleaned the sysconfig file

* Thu Apr 28 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-0.20110424.4
- downgrade the pcre minimal required version from 7.3 to 6.1 (#651823#c26)
- better compliance with the package guidelines
  (https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd)

* Thu Apr 28 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.3-0.20110424.3
- honor pidfile
- disable ssl
- disable sql

* Tue Apr 26 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.3-0.20110424.2
- drop support for fedora without systemd

* Mon Apr 25 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.3-0.20110424.1
- change NVR to alert users that we have been using a syslog-ng v3.2 git snapshot
  (for systemd support)

* Mon Apr 25 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.2.2-4
- re-introduces the "Provides: syslog" (#651823 comments 13, 15 and 21)
- rename the logrotate.d file back to syslog (#651823 comments 12, 15, 16 and 21)
- cleans the sysconfig and logrotate file mess (#651823 comments 17, 20 and 21)
- spec code cleanup (#651823 comments 10 and 11)
- dropped duplicated eventlog-devel BR

* Thu Apr 21 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.2-3
- systemd fixup
- more spec file cleanup,
- incorporate fixes from Jose Pedro Oliveira (#651823 comments 7 and 8)

* Wed Apr 20 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.2-2
- spec cleanup

* Wed Apr 13 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.2-1
- update to 3.2.2
- built from git snapshot

* Wed Apr 06 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.1-3
- install to /sbin
- native systemd start script

* Thu Mar 17 2011 Matthias Runge <mrunge@matthias-runge.de> - 3.2.1-2
- finally move libs to correct place
- split out -devel subpackage

* Fri Mar 04 2011 Matthias Runge <mrunge@fedoraproject.org> - 3.2.1-1
- update to syslog-ng 3.2.1

* Sat Jul 24 2010 Doug Warner <silfreed@fedoraproject.org> - 3.1.1-1
- update for syslog-ng 3.1.1
- supports the new syslog protocol standards
- log statements can be embedded into each other
- the encoding of source files can be set for proper character conversion
- can read, process, and rewrite structured messages (e.g., Apache webserver
  logs) using templates and regular expressions
- support for patterndb v2 and v3 format, along with a bunch of new
  parsers: ANYSTRING, IPv6, IPvANY and FLOAT.
- added a new "pdbtool" utility to manage patterndb files: convert them
  from v1 or v2 format, merge mulitple patterndb files into one and look
  up matching patterns given a specific message.
- support for message tags: tags can be assigned to log messages as they
  enter syslog-ng: either by the source driver or via patterndb.
  Later it these tags can be used for efficient filtering.
- added support for rewriting structured data
- added pcre support in the binary packages of syslog-ng

* Tue Sep 15 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-8
- Adjust eventlog build requirement

* Tue Sep 15 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-7
- Branch sync

* Tue Sep 15 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-6
- Branch sync

* Tue Sep 15 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-5
- Rebuilding for tag issue

* Thu Aug 20 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-4
- libnet linking (bug#518150)

* Tue Aug 18 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-3
- Init script fix (bug#517339)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Douglas E. Warner <silfreed@silfreed.net> - 2.1.4-1
- update to 2.1.4
- enabling mixed linking to compile only non-system libs statically
- lots of packaging updates to be able to build on RHEL4,5, Fedora9+ and be
  parallel-installable with rsyslog and/or sysklogd on those platforms
- removing BR for flex & byacc to try to prevent files from being regenerated
- fixing build error with cfg-lex.l and flex 2.5.4
- Fixed a possible DoS condition triggered by a destination port unreachable
  ICMP packet received from a UDP destination.  syslog-ng started eating all
  available memory and CPU until it crashed if this happened.
- Fixed the rate at which files regular were read using the file() source.
- Report connection breaks as a write error instead of reporting POLLERR as
  the write error path reports more sensible information in the logs.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 02 2008 Douglas E. Warner <silfreed@silfreed.net> 2.0.10-1
- update to 2.0.10
- fix for CVE-2008-5110

* Mon Sep 15 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.8-3
- do not conflicts with rsyslog, both rsyslog and syslog-ng use
  same pidfile and logrotate file (#441664)

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.8-2
- fix license tag

* Thu Jan 31 2008 Douglas E. Warner <silfreed@silfreed.net> 2.0.8-1
- updated to 2.0.8
- removed logrotate patch

* Tue Jan 29 2008 Douglas E. Warner <silfreed@silfreed.net> 2.0.7-2
- added patch from git commit a8b9878ab38b10d24df7b773c8c580d341b22383
  to fix log rotation (bug#430057)

* Tue Jan 08 2008 Douglas E. Warner <silfreed@silfreed.net> 2.0.7-1
- updated to 2.0.7
- force regeneration to avoid broken paths from upstream (#265221)
- adding loggen binary

* Mon Dec 17 2007 Douglas E. Warner <silfreed@silfreed.net> 2.0.6-1
- updated to 2.0.6
- fixes DoS in ZSA-2007-029

* Thu Nov 29 2007 Peter Vrabec <pvrabec@redhat.com> 2.0.5-3
- add conflicts (#400661)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.0.5-2
- Rebuild for selinux ppc32 issue.

* Thu Jul 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.5-1
- Update to 2.0.5

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.4-4
- Add support for vim 7.1.

* Thu May 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.4-3
- Increase the number of unix-stream max-connections (10 -> 32).

* Sat May 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.4-2
- New upstream download location
  (https://lists.balabit.hu/pipermail/syslog-ng/2007-May/010258.html)

* Tue May 22 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.4-1
- Update to 2.0.4.

* Mon Mar 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.3-1
- Update to 2.0.3.

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.3-0.20070323
- Update to latest snapshot (2007-03-23).

* Fri Mar  9 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.3-0.20070309
- Enable support for TCP wrappers (--enable-tcp-wrapper).
- Optional support for spoofed source addresses (--enable-spoof-source)
  (disabled by default; build requires libnet).

* Sun Feb 25 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.2-2
- Dynamic link glib2 and eventlog (--enable-dynamic-linking).
  For Fedora Core 6 (and above) both packages install their dynamic
  libraries in /lib.

* Mon Jan 29 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.2-1
- Update to 2.0.2.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.1-1
- Update to 2.0.1.

* Fri Dec 15 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.0-1
- Updated the init script patch: LSB Description and Short-Description.

* Fri Nov  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.0.0-0
- Update to 2.0.0.

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.11-3
- Rebuild for FC6.

* Sun Jun  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.11-2
- Install the vim syntax file.

* Fri May  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.11-1
- Update to 1.6.11.

* Sun Apr  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.10-2
- Build option to support the syslog-ng spoof-source feature
  (the feature spoof-source is disabled by default).

* Thu Mar 30 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.10-1
- Update to 1.6.10.
- The postscript documentation has been dropped (upstream).

* Wed Feb 15 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.9-3
- Rebuild.

* Mon Dec 19 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.9-2
- Provides syslog instead of sysklogd (#172885).

* Wed Nov 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.9-1
- Build conflict statement
  (see: https://lists.balabit.hu/pipermail/syslog-ng/2005-June/007630.html)

* Wed Nov 23 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.9-0
- Update to 1.6.9.
- The libol support library is now included in the syslog-ng tarball.

* Wed Jun 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.8-2
- BuildRequire which, since it's not part of the default buildgroup
  (Konstantin Ryabitsev).

* Fri May 27 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.8-1
- Update to 1.6.8.

* Thu May 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.7-3
- Shipping the sysklogd logrotate file and using the same pidfile
  as suggested by Jeremy Katz.
- Patching the init script: no default runlevels.
- Removed the triggers to handle the logrotate file (no longer needed).
- The SELinux use_syslogng boolean has been dropped (rules enabled).

* Sat May 07 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.7-2.fc4
- Increased libol required version to 0.3.16
  (https://lists.balabit.hu/pipermail/syslog-ng/2005-May/007385.html).

* Sat Apr 09 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.7-0.fdr.1
- Update to 1.6.7.
- The Red Hat/Fedora Core configuration files are now included in the
  syslog-ng tarball (directory: contrib/fedora-packaging).

* Fri Mar 25 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.6-0.fdr.4
- Logrotate file conflict: just comment/uncomment contents of the syslog
  logrotate file using triggers.

* Tue Feb 15 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.6-0.fdr.3
- Require logrotate.
- Documentation updates (upstream).

* Sat Feb 05 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.6-0.fdr.2
- Added contrib/relogger.pl (missing in syslog-ng-1.6.6).
- Requires libol 0.3.15.
- Added %%trigger scripts to handle the logrotate file.

* Fri Feb 04 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.6-0.fdr.1
- Update to 1.6.6.
- Patches no longer needed.

* Fri Feb 04 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.5-0.fdr.7
- Took ownership of the configuration directory (/etc/syslog-ng/).
- Updated the syslog-ng(8) manpage (upstream patch).
- Updated the configuration file: /proc/kmsg is a file not a pipe.
- Patched two contrib files: syslog2ng and syslog-ng.conf.RedHat.
- Logrotate file inline replacement: perl --> sed (bug 1332 comment 23).

* Tue Jan 25 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.5-0.fdr.6
- Logrotate problem: only one logrotate file for syslog and syslog-ng.
- Configuration file: don't sync d_mail destination (/var/log/maillog).

* Mon Jan 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.5-0.fdr.5
- SIGHUP handling upstream patch (syslog-ng-1.6.5+20050121.tar.gz).
- Static linking /usr libraries (patch already upstream).

* Thu Sep 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.6.5-0.fdr.4
- make: do not strip the binaries during installation (install vs install-strip)
  (bug 1332 comment 18).
- install: preserve timestamps (option -p) (bug 1332 comment 18).

* Wed Sep  1 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.5-0.fdr.3
- use the tcp_wrappers static library instead (bug 1332 comment 15).

* Wed Sep  1 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.5-0.fdr.2
- added missing build requirement: flex (bug 1332 comment 13).

* Wed Aug 25 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.5-0.fdr.1
- update to 1.65.
- removed the syslog-ng.doc.patch patch (already upstream).
- removed the syslog-ng.conf.solaris documentation file.

* Wed Apr 21 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.2-0.fdr.3
- removed Conflits:
- changed the %%post and %%preun scripts
- splitted Requires( ... , ... ) into Requires( ... )

* Fri Mar  5 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.2-0.fdr.2
- corrected the source URL

* Sat Feb 28 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.2-0.fdr.1
- changed packaged name to be compliant with fedora.us naming conventions

* Fri Feb 27 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.2-0.fdr.0.2
- updated to version 1.6.2
- undo "Requires: tcp_wrappers" - tcp_wrappers is a static lib

* Sat Feb  7 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.1-0.fdr.2
- make %%{?_smp_mflags}
- Requires: tcp_wrappers

* Sat Jan 10 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 0:1.6.1-0.fdr.1
- first release for fedora.us

* Fri Jan  9 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.1-1.1tux
- updated to version 1.6.1

* Tue Oct  7 2003 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.0rc4-1.1tux
- updated to version 1.6.0rc4

* Tue Aug 26 2003 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.0rc3-1.4tux
- installation scripts improved
- conflits line

* Sat Aug 16 2003 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.0rc3-1.3tux
- install-strip

* Tue Jul 22 2003 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.0rc3-1.2tux
- missing document: contrib/syslog-ng.conf.doc

* Thu Jun 12 2003 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.0rc3-1.1tux
- Version 1.6.0rc3

* Sat Apr 12 2003 Jose Pedro Oliveira <jpo at di.uminho.pt> 1.6.0rc2 snapshot
- Reorganized specfile
- Corrected the scripts (%%post, %%postun, and %%preun)
- Commented the mysql related lines; create an option for future inclusion

* Thu Feb 27 2003 Richard E. Perlotto II <richard@perlotto.com> 1.6.0rc1-1
- Updated for new version

* Mon Feb 17 2003 Richard E. Perlotto II <richard@perlotto.com> 1.5.26-1
- Updated for new version

* Fri Dec 20 2002 Richard E. Perlotto II <richard@perlotto.com> 1.5.24-1
- Updated for new version

* Fri Dec 13 2002 Richard E. Perlotto II <richard@perlotto.com> 1.5.23-2
- Corrected the mass of errors that occured with rpmlint
- Continue to clean up for the helpful hints on how to write to a database

* Sun Dec 08 2002 Richard E. Perlotto II <richard@perlotto.com> 1.5.23-1
- Updated file with notes and PGP signatures

# vim:set ai ts=4 sw=4 sts=4 et:
