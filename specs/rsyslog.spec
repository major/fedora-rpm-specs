%define rsyslog_statedir %{_sharedstatedir}/rsyslog
%define rsyslog_pkidir %{_sysconfdir}/pki/rsyslog
%define rsyslog_docdir %{_docdir}/rsyslog
%define qpid_proton_v 0.40.0
# The following packages are not enabled on rhel:
#   hiredis, libdbi, mongodb, rabbitmq, impstats_push
# The omamqp1 plugin is built differently as qpid-proton is not available on rhel
%if 0%{?rhel}
%bcond_with hiredis
%bcond_with libdbi
%bcond_with mongodb
%bcond_with rabbitmq
%bcond_with impstats_push
%else
%bcond_without hiredis
%bcond_without libdbi
%bcond_without mongodb
%bcond_without rabbitmq
%bcond_without impstats_push
%endif

# Add options to not build with features listed below,
# the default is to build with them.
%bcond_without clickhouse
%bcond_without imdocker
%bcond_without improg
%bcond_without gnutls
%bcond_without openssl
%bcond_without gssapi
%bcond_without omamqp1
%bcond_without rdkafka
%bcond_without relp
%bcond_without mysql
%bcond_without pgsql
%bcond_without snmp
%bcond_without udpspoof
%bcond_without mmtaghostname

Summary: Enhanced system logging and kernel message trapping daemon
Name: rsyslog
Version: 8.2604.0
Release: %autorelease
License: GPL-3.0-or-later AND Apache-2.0
URL: http://www.rsyslog.com/
Source0: http://www.rsyslog.com/files/download/rsyslog/%{name}-%{version}.tar.gz
Source1: rsyslog.conf
Source2: rsyslog.sysconfig
Source3: rsyslog.log
Source4: rsyslog.service
# Add qpid-proton as another source, enable omamqp1 module in a
# separatae sub-package with it statically linked(see rhbz#1713427)
Source5: https://archive.apache.org/dist/qpid/proton/%{qpid_proton_v}/qpid-proton-%{qpid_proton_v}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: dos2unix
BuildRequires: flex
BuildRequires: libfastjson-devel >= 0.99.8
BuildRequires: libestr-devel >= 0.1.9
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: pkgconfig
BuildRequires: python3-docutils
# make sure systemd is in a version that isn't affected by rhbz#974132
BuildRequires: systemd-devel >= 204-8
BuildRequires: systemd-rpm-macros
BuildRequires: zlib-devel
BuildRequires: libcap-ng-devel
BuildRequires: libyaml-devel
%if %{with impstats_push}
BuildRequires: protobuf-c-devel
BuildRequires: protobuf-c-compiler
BuildRequires: snappy-devel
%endif

Recommends: logrotate
Obsoletes: rsyslog-logrotate < 8.2310.0-2
Provides: rsyslog-logrotate = %{version}-%{release}
Requires: bash >= 2.0
%{?systemd_ordering}

Provides: syslog
Obsoletes: sysklogd < 1.5-11

%package crypto
Summary: Encryption support
Requires: %name = %version-%release

%package doc
Summary: HTML documentation for rsyslog
BuildArch: noarch

%package elasticsearch
Summary: ElasticSearch output module for rsyslog
Requires: %name = %version-%release
BuildRequires: libcurl-devel

%package mmjsonparse
Summary: JSON enhanced logging support
Requires: %name = %version-%release

%package mmnormalize
Summary: Log normalization support for rsyslog
Requires: %name = %version-%release
BuildRequires: libestr-devel liblognorm-devel >= 1.0.2

%package mmaudit
Summary: Message modification module supporting Linux audit format
Requires: %name = %version-%release

%package mmfields
Summary: Fields extraction module
Requires: %name = %version-%release

%if %{with mmtaghostname}
%package mmtaghostname
Summary: Message modification module supporting adding tags
Requires: %name = %version-%release
%endif

%if %{with snmp}
%package mmsnmptrapd
Summary: Message modification module for snmptrapd generated messages
Requires: %name = %version-%release
%endif

%if %{with mysql}
%package mysql
Summary: MySQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: mariadb-connector-c-devel
%endif

%if %{with pgsql}
%package pgsql
Summary: PostgresSQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: libpq-devel
%endif

%if %{with gssapi}
%package gssapi
Summary: GSSAPI authentication and encryption support for rsyslog
Requires: %name = %version-%release
BuildRequires: krb5-devel
%endif

%if %{with relp}
%package relp
Summary: RELP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: librelp-devel >= 1.2.16
%endif

%if %{with gnutls}
%package gnutls
Summary: TLS protocol support for rsyslog via GnuTLS library
Requires: %name = %version-%release
BuildRequires: gnutls-devel
%endif

%if %{with openssl}
%package openssl
Summary: TLS protocol support for rsyslog via OpenSSL library
Group: System Environment/Daemons
Requires: %name = %version-%release
Requires: openssl-libs
BuildRequires: openssl-devel
%endif

%if %{with snmp}
%package snmp
Summary: SNMP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: net-snmp-devel
%endif

%if %{with udpspoof}
%package udpspoof
Summary: Provides the omudpspoof module
Requires: %name = %version-%release
BuildRequires: libnet-devel
%endif

%if %{with omamqp1}
%package omamqp1
Summary: Provides the omamqp1 module
Requires: %name = %version-%release
Requires: cyrus-sasl-lib
Requires: openssl-libs
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cyrus-sasl-devel
BuildRequires: openssl-devel
BuildRequires: python3
%endif

%if %{with rdkafka}
%package kafka
Summary: Provides the omkafka module
Requires: %name = %version-%release
BuildRequires: librdkafka-devel
%endif

%package mmkubernetes
Summary: Provides the mmkubernetes module
Requires: %name = %version-%release
BuildRequires: libcurl-devel

%if %{with hiredis}
%package hiredis
Summary: Redis support for rsyslog
Requires: %name = %version-%release
BuildRequires: hiredis-devel
%endif

%if %{with libdbi}
%package libdbi
Summary: Libdbi database support for rsyslog
Requires: %name = %version-%release
BuildRequires: libdbi-devel
%endif

%if %{with mongodb}
%package mongodb
Summary: MongoDB support for rsyslog
Requires: %name = %version-%release
BuildRequires: mongo-c-driver-devel snappy-devel cyrus-sasl-devel
%endif

%if %{with rabbitmq}
%package rabbitmq
Summary: RabbitMQ support for rsyslog
Requires: %name = %version-%release
BuildRequires: librabbitmq-devel >= 0.2
%endif


%description
Rsyslog is an enhanced, multi-threaded syslog daemon. It supports MySQL,
syslog/TCP, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is compatible with stock sysklogd
and can be used as a drop-in replacement. Rsyslog is simple to set up, with
advanced features suitable for enterprise-class, encryption-protected syslog
relay chains.

%description crypto
This package contains a module providing log file encryption and a
command line tool to process encrypted logs.

%description doc
This subpackage contains documentation for rsyslog.

%description elasticsearch
This module provides the capability for rsyslog to feed logs directly into
Elasticsearch.

%description mmjsonparse
This module provides the capability to recognize and parse JSON enhanced
syslog messages.

%description mmnormalize
This module provides the capability to normalize log messages via liblognorm.

%description mmaudit
This module provides message modification supporting Linux audit format
in various settings.

%description mmfields
The mmfield module permits to extract fields. Using this module is of special
advantage if a field-based log format is to be processed, like for example CEF
and either a large number of fields is needed or a specific field is used multiple
times inside filters.

%description mmtaghostname
This module provides message modification for changing or adding the host name.

%if %{with snmp}
%description mmsnmptrapd
This message modification module takes messages generated from snmptrapd and
modifies them so that they look like they originated from the read originator.
%endif

%if %{with mysql}
%description mysql
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.
%endif

%if %{with pgsql}
%description pgsql
The rsyslog-pgsql package contains a dynamic shared object that will add
PostgreSQL database support to rsyslog.
%endif

%if %{with gssapi}
%description gssapi
The rsyslog-gssapi package contains the rsyslog plugins which support GSSAPI
authentication and secure connections. GSSAPI is commonly used for Kerberos
authentication.
%endif

%if %{with relp}
%description relp
The rsyslog-relp package contains the rsyslog plugins that provide
the ability to receive syslog messages via the reliable RELP
protocol.
%endif

%if %{with gnutls}
%description gnutls
The rsyslog-gnutls package contains the rsyslog plugins that provide the
ability to send and receive syslog messages via TCP or RELP using TLS
encryption via GnuTLS library. For details refer to rsyslog doc on imtcp
and omfwd modules.
%endif

%if %{with openssl}
%description openssl
The rsyslog-openssl package contains the rsyslog plugins that provide the
ability to send and receive syslog messages via TCP or RELP using TLS
encryption via OpenSSL library. For details refer to rsyslog doc on imtcp
and omfwd modules.
%endif

%if %{with snmp}
%description snmp
The rsyslog-snmp package contains the rsyslog plugin that provides the
ability to send syslog messages as SNMPv1 and SNMPv2c traps.
%endif

%if %{with udpspoof}
%description udpspoof
This module is similar to the regular UDP forwarder, but permits to
spoof the sender address. Also, it enables to circle through a number
of source ports.
%endif

%if %{with omamqp1}
%description omamqp1
The omamqp1 output module can be used to send log messages via an AMQP
1.0-compatible messaging bus.
%endif

%if %{with rdkafka}
%description kafka
The rsyslog-kafka package provides module for Apache Kafka output.
%endif

%description mmkubernetes
The rsyslog-mmkubernetes package provides module for adding kubernetes
container metadata.

%if %{with hiredis}
%description hiredis
This module provides output to Redis.
%endif

%if %{with libdbi}
%description libdbi
This module supports a large number of database systems via
libdbi. Libdbi abstracts the database layer and provides drivers for
many systems. Drivers are available via the libdbi-drivers project.
%endif

%if %{with mongodb}
%description mongodb
The rsyslog-mongodb package contains a dynamic shared object that will add
MongoDB database support to rsyslog.
%endif

%if %{with rabbitmq}
%description rabbitmq
This module allows rsyslog to send messages to a RabbitMQ server.
%endif

%prep
# set up rsyslog sources
%setup -q -D

%if %{with omamqp1}
# Unpack qpid-proton
%setup -q -D -T -b 5
%endif

%build
%ifarch sparc64
#sparc64 need big PIC
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif

%if %{with omamqp1}
# build the proton first
(
	cd %{_builddir}/qpid-proton-%{qpid_proton_v}
	mkdir bld
	cd bld

	# Need ENABLE_FUZZ_TESTING=NO to avoid a link failure
	# Modern approach for Python discovery in CMake
	cmake .. \
		-DBUILD_BINDINGS="" \
		-DBUILD_STATIC_LIBS=YES \
		-DENABLE_FUZZ_TESTING=NO \
		-DPython_FIND_STRATEGY=LOCATION \
		-DPython_ROOT_DIR=/usr \
		-DCMAKE_AR="/usr/bin/gcc-ar" -DCMAKE_NM="/usr/bin/gcc-nm" -DCMAKE_RANLIB="/usr/bin/gcc-ranlib"
	make -j8
)
%endif

%ifarch sparc64
#sparc64 need big PIE
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpie"
%endif
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"

%if %{with hiredis}
# the hiredis-devel package doesn't provide a pkg-config file
export HIREDIS_CFLAGS=-I/usr/include/hiredis
export HIREDIS_LIBS="-L%{_libdir} -lhiredis"
%endif

sed -i 's/%{version}/%{version}-%{release}/g' configure.ac

autoreconf -if
%configure \
	--prefix=/usr \
	--disable-static \
	--disable-testbench \
%if %{with clickhouse}
	--enable-clickhouse \
%endif
%if %{with imdocker}
	--enable-imdocker \
%endif
%if %{with improg}
	--enable-improg \
%endif
  --enable-libcap-ng \
%if %{with libdbi}
	--enable-libdbi \
%endif
%if %{with hiredis}
	--enable-omhiredis \
%endif
%if %{with mongodb}
	--enable-ommongodb \
%endif
%if %{with rabbitmq}
	--enable-omrabbitmq \
%endif
%if %{with omamqp1}
	--enable-omamqp1 PROTON_PROACTOR_LIBS="%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-core-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-proactor-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-static.a -lssl -lsasl2 -lcrypto" PROTON_PROACTOR_CFLAGS="-I%{_builddir}/qpid-proton-%{qpid_proton_v}/c/include -I%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/include" PROTON_LIBS="%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-core-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-proactor-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-static.a -lssl -lsasl2 -lcrypto" PROTON_CFLAGS="-I%{_builddir}/qpid-proton-%{qpid_proton_v}/c/include -I%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/include" \
%endif
	--enable-elasticsearch \
	--enable-generate-man-pages \
%if %{with gnutls}
	--enable-gnutls \
%endif
%if %{with openssl}
	--enable-openssl \
%endif
%if %{with gssapi}
	--enable-gssapi-krb5 \
%endif
	--enable-imfile \
	--enable-imjournal \
%if %{with rdkafka}
	--enable-imkafka \
	--enable-omkafka \
%endif
	--enable-impstats \
%if %{with impstats_push}
	--enable-impstats-push \
%else
	--disable-impstats-push \
%endif
	--enable-imptcp \
	--enable-mail \
	--enable-mmanon \
	--enable-mmaudit \
	--enable-mmcount \
	--enable-mmfields \
	--enable-mmkubernetes \
	--enable-mmjsonparse \
	--enable-mmnormalize \
%if %{with mmtaghostname}
	--enable-mmtaghostname \
%endif
%if %{with snmp}
	--enable-mmsnmptrapd \
%endif
	--enable-mmutf8fix \
%if %{with mysql}
	--enable-mysql \
%endif
	--enable-omhttp \
	--enable-omjournal \
	--enable-omprog \
	--enable-omstdout \
%if %{with udpspoof}
	--enable-omudpspoof \
%endif
	--enable-omuxsock \
%if %{with pgsql}
	--enable-pgsql \
%endif
	--enable-pmaixforwardedfrom \
	--enable-pmcisconames \
	--enable-pmlastmsg \
	--enable-pmsnare \
%if %{with relp}
	--enable-relp \
%endif
%if %{with snmp}
	--enable-snmp \
%endif
	--enable-unlimited-select \
	--enable-usertools \
	--disable-libgcrypt \
	--enable-openssl_crypto_provider

make V=1

%check
make V=1 check

%install
make V=1 DESTDIR=%{buildroot} install

install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -d -m 700 %{buildroot}%{rsyslog_statedir}
install -d -m 700 %{buildroot}%{rsyslog_pkidir}
install -d -m 755 %{buildroot}%{rsyslog_docdir}/html

install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rsyslog.conf
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/rsyslog
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/rsyslog
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/rsyslog.service

%if %{with mysql}
install -p -m 644 plugins/ommysql/createDB.sql %{buildroot}%{rsyslog_docdir}/mysql-createDB.sql
%endif

%if %{with pgsql}
install -p -m 644 plugins/ompgsql/createDB.sql %{buildroot}%{rsyslog_docdir}/pgsql-createDB.sql
%endif

dos2unix tools/recover_qi.pl
install -p -m 644 tools/recover_qi.pl %{buildroot}%{rsyslog_docdir}/recover_qi.pl
install -p -m 644 contrib/mmkubernetes/*.rulebase %{buildroot}%{rsyslog_docdir}
# extract documentation
cp -r doc/* %{buildroot}%{rsyslog_docdir}/html
# get rid of libtool libraries
rm -f %{buildroot}%{_libdir}/rsyslog/*.la
# imdiag and liboverride is only used for testing
rm -f %{buildroot}%{_libdir}/rsyslog/imdiag.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_gethostname.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_getaddrinfo.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_gethostname_nonfqdn.so

%post
for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	umask 066 && touch $n
done
%systemd_post rsyslog.service

%preun
%systemd_preun rsyslog.service

%postun
%systemd_postun_with_restart rsyslog.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS ChangeLog README.md
%exclude %{rsyslog_docdir}/html
%exclude %{rsyslog_docdir}/recover_qi.pl
%if %{with mysql}
%exclude %{rsyslog_docdir}/mysql-createDB.sql
%endif
%if %{with pgsql}
%exclude %{rsyslog_docdir}/pgsql-createDB.sql
%endif
%dir %{_libdir}/rsyslog
%dir %{_sysconfdir}/rsyslog.d
%dir %{rsyslog_statedir}
%dir %{rsyslog_pkidir}
%{_sbindir}/rsyslogd
%{_mandir}/man5/rsyslog.conf.5.gz
%{_mandir}/man8/rsyslogd.8.gz
%{_unitdir}/rsyslog.service
%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/rsyslog
%config(noreplace) %{_sysconfdir}/logrotate.d/rsyslog
# plugins
%{_libdir}/rsyslog/fmhash.so
%{_libdir}/rsyslog/fmhttp.so
%{_libdir}/rsyslog/imfile.so
%{_libdir}/rsyslog/imjournal.so
%{_libdir}/rsyslog/imklog.so
%{_libdir}/rsyslog/immark.so
%{_libdir}/rsyslog/impstats.so
%{_libdir}/rsyslog/imptcp.so
%{_libdir}/rsyslog/imtcp.so
%{_libdir}/rsyslog/imudp.so
%{_libdir}/rsyslog/imuxsock.so
%{_libdir}/rsyslog/lmnet.so
%{_libdir}/rsyslog/lmnetstrms.so
%{_libdir}/rsyslog/lmnsd_ptcp.so
%{_libdir}/rsyslog/lmregexp.so
%{_libdir}/rsyslog/lmtcpclt.so
%{_libdir}/rsyslog/lmtcpsrv.so
%{_libdir}/rsyslog/lmzlibw.so
%{_libdir}/rsyslog/mmanon.so
%{_libdir}/rsyslog/mmcount.so
%{_libdir}/rsyslog/mmexternal.so
%{_libdir}/rsyslog/mmleefparse.so
%{_libdir}/rsyslog/mmutf8fix.so
%{_libdir}/rsyslog/omhttp.so
%{_libdir}/rsyslog/omjournal.so
%{_libdir}/rsyslog/ommail.so
%{_libdir}/rsyslog/omprog.so
%{_libdir}/rsyslog/omstdout.so
%{_libdir}/rsyslog/omtesting.so
%{_libdir}/rsyslog/omuxsock.so
%{_libdir}/rsyslog/pmaixforwardedfrom.so
%{_libdir}/rsyslog/pmcisconames.so
%{_libdir}/rsyslog/pmlastmsg.so
%{_libdir}/rsyslog/pmsnare.so
%if %{with imdocker}
%{_libdir}/rsyslog/imdocker.so
%endif
%if %{with improg}
%{_libdir}/rsyslog/improg.so
%endif
%if %{with clickhouse}
%{_libdir}/rsyslog/omclickhouse.so
%endif

%files crypto
%{_bindir}/rscryutil
%{_mandir}/man1/rscryutil.1.gz
%{_libdir}/rsyslog/lmcry_ossl.so

%files doc
%{rsyslog_docdir}/html
%{rsyslog_docdir}/recover_qi.pl

%files elasticsearch
%{_libdir}/rsyslog/omelasticsearch.so

%files mmaudit
%{_libdir}/rsyslog/mmaudit.so

%files mmfields
%{_libdir}/rsyslog/mmfields.so

%files mmjsonparse
%{_libdir}/rsyslog/mmjsonparse.so

%files mmnormalize
%{_libdir}/rsyslog/mmnormalize.so

%files mmtaghostname
%{_libdir}/rsyslog/mmtaghostname.so

%if %{with snmp}
%files mmsnmptrapd
%{_libdir}/rsyslog/mmsnmptrapd.so
%endif

%if %{with mysql}
%files mysql
%doc %{rsyslog_docdir}/mysql-createDB.sql
%{_libdir}/rsyslog/ommysql.so
%endif

%if %{with pgsql}
%files pgsql
%doc %{rsyslog_docdir}/pgsql-createDB.sql
%{_libdir}/rsyslog/ompgsql.so
%endif

%if %{with gssapi}
%files gssapi
%{_libdir}/rsyslog/lmgssutil.so
%{_libdir}/rsyslog/imgssapi.so
%{_libdir}/rsyslog/omgssapi.so
%endif

%if %{with relp}
%files relp
%{_libdir}/rsyslog/imrelp.so
%{_libdir}/rsyslog/omrelp.so
%endif

%if %{with gnutls}
%files gnutls
%{_libdir}/rsyslog/lmnsd_gtls.so
%endif

%if %{with openssl}
%files openssl
%{_libdir}/rsyslog/lmnsd_ossl.so
%endif

%if %{with snmp}
%files snmp
%{_libdir}/rsyslog/omsnmp.so
%endif

%if %{with udpspoof}
%files udpspoof
%{_libdir}/rsyslog/omudpspoof.so
%endif

%if %{with omamqp1}
%files omamqp1
%{_libdir}/rsyslog/omamqp1.so
%endif

%if %{with rdkafka}
%files kafka
%{_libdir}/rsyslog/imkafka.so
%{_libdir}/rsyslog/omkafka.so
%endif

%files mmkubernetes
%{_libdir}/rsyslog/mmkubernetes.so
%doc %{rsyslog_docdir}/k8s_filename.rulebase
%doc %{rsyslog_docdir}/k8s_container_name.rulebase

%if %{with hiredis}
%files hiredis
%{_libdir}/rsyslog/omhiredis.so
%endif

%if %{with libdbi}
%files libdbi
%{_libdir}/rsyslog/omlibdbi.so
%endif

%if %{with mongodb}
%files mongodb
%{_bindir}/logctl
%{_libdir}/rsyslog/ommongodb.so
%endif

%if %{with rabbitmq}
%files rabbitmq
%{_libdir}/rsyslog/omrabbitmq.so
%endif


%changelog
%autochangelog
