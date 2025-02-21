%global git_commit 051e1c4ccdec8041c508452253701fb7c07f9be5
%global _hardened_build 1

%global EXCLUDE_MODULES cachedb_cassandra %{!?_with_oracle:db_oracle} launch_darkly osp python sngtc tls_wolfssl

Summary:  Open Source SIP Server
Name:     opensips
Version:  3.5.4
Release:  %autorelease
License:  GPL-2.0-or-later
Source0:  https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source3:  opensips.sysusers
# Fedora-specific patches
Patch001: opensips-0001-Consistently-use-rtpproxy-switches.patch
Patch002: opensips-0002-Cleanup-Oracle-s-makefiles.patch
Patch003: opensips-0003-db_ora-null-terminating-string-is-more-safely-most-m.patch
Patch004: opensips-0004-Return-actual-payload-ID-in-case-of-a-dynamic-payloa.patch
Patch005: opensips-0005-Add-support-for-upcoming-json-c-0.14.0.patch
Patch006: opensips-0006-libcouchbase-API-v3.patch
Patch007: opensips-0007-Guard-VERSIONTYPE.patch
Patch008: opensips-0008-A-new-string-transformation.patch
Patch009: opensips-0009-Fix-pointer-type.patch

URL:      https://opensips.org

BuildRequires: bison
BuildRequires: docbook-xsl
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libxslt
BuildRequires: lynx
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre-devel
BuildRequires: systemd-units

# Users and groups
Requires(post): systemd
Requires(preun): systemd

Obsoletes: %{name}-auth_diameter
Obsoletes: %{name}-event_datagram
Obsoletes: %{name}-event_jsonrpc
Obsoletes: %{name}-mi_xmlrpc
Obsoletes: %{name}-python < 2.4.6-4
Obsoletes: %{name}-seas
Obsoletes: %{name}-sms
Obsoletes: %{name}-xmlrpc
Obsoletes: python2-%{name} < 2.4.6-4

%description
OpenSIPS or Open SIP Server is a very fast and flexible SIP (RFC3261)
proxy server. Written entirely in C, opensips can handle thousands calls
per second even on low-budget hardware. A C Shell like scripting language
provides full control over the server's behaviour. It's modular
architecture allows only required functionality to be loaded.
Currently the following modules are available: digest authentication,
CPL scripts, instant messaging, MySQL and UNIXODBC support, a presence agent,
radius authentication, record routing, an SMS gateway, a jabber gateway, a
transaction and dialog module, OSP module, statistics support,
registrar and user location.

%package  aaa_diameter
Summary:  Diameter backend for AAA API
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: freeDiameter-devel

%description aaa_diameter
This module provides the Diameter backend for the AAA API - group, auth, uri
module use the AAA API for performing Diameter ops.

%package  aaa_radius
Summary:  RADIUS backend for AAA API
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: radcli-devel

%description aaa_radius
This module provides the RADIUS backend for the AAA API - group, auth, uri
module use the AAA API for performing RADIUS ops.

%package  acc
Summary:  Accounts transactions information to different backends
Requires: %{name}%{?_isa} = %{version}-%{release}

%description acc
ACC module is used to account transactions information to different backends
like syslog, SQL, AAA.

%package  aka_av_diameter
Summary:  Diameter AKA AV Manager
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-aaa_diameter%{?_isa} = %{version}-%{release}

%description aka_av_diameter
This module is an extension to the AKA_AUTH module providing a Diameter AKA AV
Manager that implements the Multimedia-Auth-Request and Multimedia-Auth-Answer
Diameter commands defined in the Cx interface of the ETSI TS 129 229
specifications in order to fetch a set of authentication vectors and feed them
in the AKA authentication process.

%package  auth_aaa
Summary:  Performs authentication using an AAA server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description auth_aaa
This module contains functions that are used to perform authentication using
an AAA server.  Basically the proxy will pass along the credentials to the
AAA server which will in turn send a reply containing result of the
authentication. So basically the whole authentication is done in the AAA
server.

%package  auth_jwt
Summary:  Performs authentication over JSON Web Tokens
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libjwt-devel
BuildRequires: pkgconfig(openssl)

%description auth_jwt
The module implements authentication over JSON Web Tokens. Any database module
(currently mysql, postgres, dbtext), must be loaded before this module in case
the db_url parameter is set.

%package  b2bua
Summary:  Back-2-Back User Agent
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description b2bua
B2BUA is an implementation of the behavior of a B2BUA as defined in RFC 3261
that offers the possibility to build certain services on top of it.

%package  cachedb_couchbase
Summary:  Couchbase connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libcouchbase-devel

%description cachedb_couchbase
Couchbase module is an implementation of a cache system designed to
work with a Couchbase server.

%package  cachedb_memcached
Summary:  Memcached connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-memcached%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-memcached
BuildRequires: libmemcached-devel

%description cachedb_memcached
Memcached module is an implementation of a cache system designed to
work with a memcached server.

%package  cachedb_mongodb
Summary:  MongoDB connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: json-c-devel
BuildRequires: mongo-c-driver-devel
BuildRequires: snappy-devel

%description cachedb_mongodb
MongoDB module is an implementation of a cache system designed to
work with a MongoDB server.

%package  cachedb_redis
Summary:  Redis connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-redis%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-redis
BuildRequires: hiredis-devel

%description cachedb_redis
This module is an implementation of a cache system designed to work
with a Redis server.

%package  call_center
Summary:  An inbound call center system
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}

%description call_center
The Call Center module implements an inbound call center system with call flows
(for queueing the received calls) and agents (for answering the calls).

%package  carrierroute
Summary:  Routing extension suitable for carriers
BuildRequires: libconfuse-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description carrierroute
A module which provides routing, balancing and blacklisting capabilities.

%package  cgrates
Summary:  Billing module for CGRates engine
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cgrates
This module can be used to communicate with the CGRates engine in order to do
call authorization and accounting for billing purposes. The OpenSIPS module
does not do any billing by itself, but provides an interface to communicate
with the CGRateS engine using efficient JSON-RPC APIs in both synchronous and
asynchronous ways.

%package  compression
Summary:  Message compression/decompression and base64 encoding
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: zlib-devel

%description compression
This module provides message compression/decompression and base64 encoding for
sip messages using deflate and gzip algorithm/headers. Another feature of this
module is reducing headers to compact for as specified in SIP RFC's, sdp body
codec unnecessary description removal (for codecs 0-97), whitelist for headers
not be removed (excepting necessary headers).

%package  cpl_c
Summary:  Call Processing Language interpreter
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-cpl-c%{?_isa} = %{version}-%{release}
Provides: %{name}-cpl-c = %{version}-%{release}
Obsoletes:%{name}-cpl-c < 2.2.2-1

%description cpl_c
This module implements a CPL (Call Processing Language) interpreter.
Support for uploading/downloading/removing scripts via SIP REGISTER method
is present.

%package  db_berkeley
Summary:  Berkeley DB backend support
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libdb-devel

%description db_berkeley
This is a module which integrates the Berkeley DB into OpenSIPS. It implements
the DB API defined in OpenSIPS.

%package  db_http
Summary:  HTTP DB backend support
Requires: %{name}%{?_isa} = %{version}-%{release}

%description db_http
This module provides access to a database that is implemented as a
HTTP server.

%package  db_mysql
Summary:  MySQL storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-mysql%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-mysql
BuildRequires: mariadb-connector-c-devel

%description db_mysql
This module contains the MySQL plugin for %{name}, which allows
a MySQL database to be used for persistent storage.

%if 0%{?_with_oracle}
%package  db_oracle
Summary:  Oracle storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-oracle%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-oracle
BuildRequires: oracle-instantclient-devel

%description db_oracle
This module package contains the Oracle plugin for %{name}, which allows
a Oracle database to be used for persistent storage.
%endif

%package  db_perlvdb
Summary:  Perl virtual database engine
# require perl-devel for >F7 and perl for <=F6
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-perl%{?_isa} = %{version}-%{release}
Provides: %{name}-perlvdb%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-perlvdb

%description db_perlvdb
The Perl Virtual Database (VDB) provides a virtualization framework for
OpenSIPS's database access. It does not handle a particular database engine
itself but lets the user relay database requests to arbitrary Perl functions.

%package  db_postgresql
Summary:  PostgreSQL storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-postgresql%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-postgresql
BuildRequires: libpq-devel

%description db_postgresql
This module contains the PostgreSQL plugin for %{name},
which allows a PostgreSQL database to be used for persistent storage.

%package  db_sqlite
Summary:  SQLite sorage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel

%description db_sqlite
This module contains the SQLite plugin for %{name}, which
allows SQLite to be used for persistent storage.

%package  db_unixodbc
Summary:  OpenSIPS unixODBC Storage support
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-unixodbc%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-unixodbc
BuildRequires: unixODBC-devel

%description db_unixodbc
This module contains the unixODBC plugin for %{name}, which
allows unixODBC to be used for persistent storage.

%package  event_kafka
Summary:  Event Kafka module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librdkafka-devel

%description event_kafka
This module provides the implementation of a Kafka client for the Event
Interface. It is used to send AMQP messages to a Kafka server each time the
Event Interface triggers an event subscribed for.

%package  event_rabbitmq
Summary:  Event RabbitMQ module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel

%description event_rabbitmq
This module provides the implementation of a RabbitMQ client for the Event Interface.
It is used to send AMQP messages to a RabbitMQ server each time the Event Interface
triggers an event subscribed for.

%package  emergency
Summary:  Emergency call treatment
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel

%description emergency
This module provides emergency call treatment for OpenSIPS, following the
architecture i2 specification of the American entity NENA. (National Emergency
Number Association).

%package  h350
Summary:  H350 implementation
BuildRequires: openldap-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description h350
The OpenSIPS H350 module enables an OpenSIPS SIP proxy server to access SIP
account data stored in an LDAP [RFC4510] directory  containing H.350 [H.350]
commObjects.

%package  httpd
Summary:  HTTP transport layer implementation
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmicrohttpd-devel

%description httpd
This module provides an HTTP transport layer for OpenSIPS.

%package  http2d
Summary:  HTTP/2 server implementation
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libnghttp2-devel
BuildRequires: libevent-devel

%description http2d
This module provides an RFC 7540/9113 HTTP/2 server implementation with "h2"
ALPN support.

%package  identity
Summary:  Support for SIP Identity (see RFC 4474)
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description identity
This module provides support for SIP Identity (see RFC 4474).

%package  jabber
Summary:  Gateway between OpenSIPS and a jabber server
BuildRequires: expat-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description jabber
Jabber module that integrates XODE XML parser for parsing Jabber messages.

%package  json
Summary:  A JSON variables within the script
BuildRequires: json-c-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description json
This module introduces a new type of variable that provides both serialization and
de-serialization from JSON format.

%package  ldap
Summary:  LDAP connector
BuildRequires: openldap-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description ldap
The LDAP module implements an LDAP search interface for OpenSIPS.

%package  lua
Summary:  Helps implement your own OpenSIPS extensions in Lua
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: compat-lua-devel
BuildRequires: libmemcached-devel

%description lua
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Lua module, you can
easily implement your own OpenSIPS extensions in Lua.

%package  media_exchange
Summary:  Lets exchange SDP between calls
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}

%description media_exchange
This module provides the means to exchange media SDP between different SIP
proxied calls, and calls started or received from a Media Server. The module
itself does not have any media capabilities, it simply exposes primitives to
exchange the SDP body between two or more different calls.

The module can both originate calls, pushing an existing SDP to a media server,
to playback, or simply record an existing RTP, as well as take the SDP of a new
call and inject the SDP into an existing, proxied sip call. In order to
manipulate the new calls, either generated, or terminated, the module behaves
as a back-to-back user agent with the aim of the OpenSIPS B2B entities module.

%package  mi_html
Summary:  A minimal web user interface for the Management Interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description mi_html
This module implements a minimal web user interface for the OpenSIPS's
Management Interface.

%package  mi_http
Summary:  A JSON REST interface for the Management Interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description mi_http
This module implements a JSON server for the Management Interface that handles
GET requests and generates JSON responses.

%package  mi_xmlrpc_ng
Summary:  A xmlrpc server for the Management Interface (new version)
BuildRequires: libxml2-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
Provides: %{name}-xmlrpc_ng%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-xmlrpc_ng

%description mi_xmlrpc_ng
This module implements a xmlrpc server that handles xmlrpc requests and generates
xmlrpc responses. When a xmlrpc message is received a default method is executed.

%package  mmgeoip
Summary:  Wrapper for the MaxMind GeoIP API
BuildRequires: GeoIP-devel
BuildRequires: libmaxminddb-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mmgeoip
Mmgeoip is a lightweight wrapper for the MaxMind GeoIP API. It adds
IP address-to-location lookup capability to OpenSIPS scripts.

%package  msrp
Summary:  MSRP support
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}

%description msrp
This module provides the MSRP support for OpenSIPS. This includes MSRP UA, MSRP
gateway between SIP MESSAGE and MSRP, MSRP relay as describned in RFC 4976.

%package  peering
Summary:  Radius peering
Requires: %{name}%{?_isa} = %{version}-%{release}

%description peering
Peering module allows SIP providers (operators or organizations)
to verify from a broker if source or destination  of a SIP request
is a trusted peer.

%package  perl
Summary:  Helps implement your own OpenSIPS extensions in Perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed), perl-devel
BuildRequires: perl-generators
Requires: %{name}%{?_isa} = %{version}-%{release}

%description perl
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Perl module, you can
easily implement your own OpenSIPS extensions in Perl.  This allows for
simple access to the full world of CPAN modules. SIP URI rewriting could be
implemented based on regular expressions; accessing arbitrary data backends,
e.g. LDAP or Berkeley DB files, is now extremely simple.

%package  pi_http
Summary:  A HTTP provisioning interface for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description pi_http
This module provides an HTTP provisioning interface for OpenSIPS. It is using
the OpenSIPS's internal database API to provide a simple way of manipulating
records inside OpenSIPS's tables.

%package  presence
Summary:  Presence server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description presence
This module implements a presence server. It handles PUBLISH and SUBSCRIBE
messages and generates NOTIFY messages. It offers support for aggregation
of published presence information for the same presentity using more devices.
It can also filter the information provided to watchers according to privacy
rules.

%package  presence_callinfo
Summary:  SIMPLE Presence extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_callinfo
The module enables the handling of "call-info" and "line-seize" events inside
the presence module. It is used with the general event handling module:
presence and it constructs and adds "Call-Info" headers to notification events.
To send "call-info" notification to watchers, a third-party application must
publish "call-info" events to the presence server.

%package  presence_dfks
Summary:  Extension to Presence server for Broadsoft's DFKS
BuildRequires: libxml2-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_dfks
The module enables handling of the "as-feature-event" event package (as defined
by Broadsoft's Device Feature Key Synchronization protocol) by the presence
module.

%package  presence_dialoginfo
Summary:  Extension to Presence server for Dialog-Info
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_dialoginfo
The module enables the handling of "Event: dialog" (as defined
in RFC 4235) inside of the presence module. This can be used
distribute the dialog-info status to the subscribed watchers.

%package  presence_mwi
Summary:  Extension to Presence server for Message Waiting Indication
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_mwi
The module does specific handling for notify-subscribe message-summary
(message waiting indication) events as specified in RFC 3842. It is used
with the general event handling module, presence. It constructs and adds
message-summary event to it.

%package  presence_reginfo
Summary:  Handles of "Event: reg" inside of the presence module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_reginfo
The module enables the handling of "Event: reg" (as defined in RFC 3680) inside
of the presence module. This can be used distribute the registration-info
status to the subscribed watchers.

%package  presence_xcapdiff
Summary:  Extension to Presence server for XCAP-DIFF event
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-pua_mi%{?_isa} = %{version}-%{release}

%description presence_xcapdiff
The presence_xcapdiff is an OpenSIPS module that adds support
for the "xcap-diff" event to presence and pua.

%package  presence_xml
Summary:  SIMPLE Presence extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xcap_client%{?_isa} = %{version}-%{release}

%description presence_xml
The module does specific handling for notify-subscribe events using xml bodies.
It is used with the general event handling module, presence.

%package  prometheus
Summary:  A HTTP interface for the Prometheus monitoring system
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description prometheus
This module provides a HTTP interface for the Prometheus monitoring system,
allowing it to fetch different statistics from OpenSIPS.

%package  proto_bins
Summary:  A secure Binary clustering protocol
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-tlsops

%description proto_bins
This module provides a secure Binary communication protocol
over TLS, to be used by the OpenSIPS clustering engine provided
by the clusterer module.

%package  proto_ipsec
Summary:  IPSec sockets for establishing secure communication channels
BuildRequires: libmnl-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description proto_ipsec
This module provides IPSec sockets for establishing secure communication
channels. It relies on RFC 3329 (Security Mechanism Agreement for the Session
Initiation Protocol (SIP)) to establish the IPSec parameters necessary for
creating dynamic Security Associations (SAs) for each connection.

%package  proto_sctp
Summary:  An optional SCTP transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lksctp-tools-devel

%description proto_sctp
This module is an optional transport module (shared library) which exports the
required logic in order to handle SCTP-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "sctp:" listeners in your
script.

%package  proto_tls
Summary:  An optional TLS transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-tlsops

%description proto_tls
This module is an optional transport module (shared library) which exports the
required logic in order to handle TLS-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "tls:" listeners in your
script.

%package  proto_wss
Summary:  An optional Secure WebSocket transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}

%description proto_wss
This module is an optional transport module (shared library) which exports the
required logic in order to handle Secure WebSocket-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "wss:" listeners in your
script.

%package  pua
Summary:  Offer the functionality of a presence user agent client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pua
This module offer the functionality of a presence user agent client, sending
Subscribe and Publish messages.

%package  pua_bla
Summary:  BLA extension for PUA
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description pua_bla
The pua_bla module enables Bridged Line Appearances support according to the
specifications in draft-anil-sipping-bla-03.txt.

%package  pua_dialoginfo
Summary:  Dialog-Info extension for PUA
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_dialoginfo
The pua_dialoginfo retrieves dialog state information from the dialog module
and PUBLISHes the dialog-information using the pua module. Thus, in combination
with the presence_xml module this can be used to derive dialog-info from the
dialog module and NOTIFY the subscribed watchers about dialog-info changes.

%package  pua_mi
Summary:  Connector between usrloc and MI interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_mi
The pua_mi sends offer the possibility to publish presence information
via MI transports.  Using this module you can create independent
applications/scripts to publish not sip-related information (e.g., system
resources like CPU-usage, memory, number of active subscribers ...)

%package  pua_reginfo
Summary:  Publishes information about "reg"-events according to to RFC 3680
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_reginfo
This module publishes information about "reg"-events according to to RFC 3680.
This can be used distribute the registration-info status to the subscribed
watchers.

This module "PUBLISH"es information when a new user registers at this server
(e.g. when "save()" is called) to users, which have subscribed for the reg-info
for this user.

This module can "SUBSCRIBE" for information at another server, so it will
receive "NOTIFY"-requests, when the information about a user changes.

And finally, it can process received "NOTIFY" requests and it will update the
local registry accordingly.

%package  pua_usrloc
Summary:  Connector between usrloc and pua modules
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_usrloc
This module is the connector between usrloc and pua modules. It creates the
environment to send PUBLISH requests for user location records, on specific
events (e.g., when new record is added in usrloc, a PUBLISH with status open
(online) is issued; when expires, it sends closed (offline)). Using this
module, phones which have no support for presence can be seen as
online/offline.

%package  pua_xmpp
Summary:  SIMPLE-XMPP Presence gateway
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xmpp%{?_isa} = %{version}-%{release}

%description pua_xmpp
This module is a gateway for presence between SIP and XMPP. It translates one
format into another and uses xmpp, pua and presence modules to manage the
transmition of presence state information.

# FIXME disable python2 until upstream adds support for Py3
#%package  -n python2-opensips
#BuildRequires: python2-devel
#%{?python_provide:%python_provide python2-opensips}
# Remove before F30
#Provides: %{name}-python = %{version}-%{release}
#Provides: %{name}-python%{?_isa} = %{version}-%{release}
#Obsoletes: %{name}-python < %{version}-%{release}
#Summary:  Python scripting support
#Requires: %{name}%{?_isa} = %{version}-%{release}

#%description -n python2-opensips
#Helps implement your own OpenSIPS extensions in Python

%package  rabbitmq
Summary:  RabbitMQ module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel

%description rabbitmq
This module allows sending AMQP messages to a RabbitMQ server. Messages can be
easily customized according to the AMQP specifications, as well the RabbitMQ
extensions.

%package  rabbitmq_consumer
Summary:  RabbitMQ message receiver
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel

%description rabbitmq_consumer
This module allows managing received messages in queues, taking advantage of
the flexible AMQP protocol.

%package  regex
Summary:  RegExp via PCRE library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description regex
This module offers matching operations against regular
expressions using the powerful PCRE library.

%package  rest_client
Summary:  HTTP client module for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}

%description rest_client
This module provides a means of interacting with an HTTP server by doing
RESTful queries, such as GET and POST.

%package  rls
Summary:  Resource List Server
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xcap%{?_isa} = %{version}-%{release}

%description rls
The modules is a Resource List Server implementation following the
specification in RFC 4662 and RFC 4826.

%package  siprec
Summary:  Call recording using SIPREC protocol
BuildRequires: libuuid-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}

%description siprec
This module provides the means to do calls recording using an external recorder
- the entity that records the call is not in the media path between the caller
and callee, but it is completely separate, thus it can not affect by any means
the quality of the conversation. This is done in a standardized manner, using
the SIPREC Protocol, thus it can be used by any recorder that implements this
protocol.

%package  snmpstats
Summary:  SNMP management interface for the OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: net-snmp-devel

%description snmpstats
The %{name}-snmpstats package provides an SNMP management interface to
OpenSIPS.  Specifically, it provides general SNMP queryable scalar statistics,
table representations of more complicated data such as user and contact
information, and alarm monitoring capabilities.

%package  stir_shaken
Summary:  Support for implementing STIR/SHAKEN
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}

%description stir_shaken
This module provides support for implementing STIR/SHAKEN (RFC 8224, RFC 8588)
Authentication and Verification services in OpenSIPS.

%package  tls_mgm
Summary:  Management for TLS certificates and parameters
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_openssl%{?_isa} = %{version}-%{release}

%description tls_mgm
This module provides an interfaces for all the modules that use the TLS
protocol. It also implements TLS related functions to use in the routing
script, and exports pseudo variables with certificate and TLS parameters.

%package  tls_openssl
Summary:  OpenSSL low level API for tls_mgm module
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tls_openssl
This module provides an OpenSSL backend for tls_mgm module.

%package  uuid
Summary:  Generates UUIDs as specified in RFC 4122
BuildRequires: libuuid-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description uuid
The module generates universally unique identifiers (UUID) as specified in RFC
4122.

%package  xcap
Summary:  XCAP common functions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xcap
The module contains several parameters and functions common to all modules
using XCAP capabilities.

%package  xcap_client
Summary:  XCAP client
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel

%description xcap_client
The modules is an XCAP client for OpenSIPS that can be used by other modules.
It fetches XCAP elements, either documents or part of them, by sending HTTP
GET requests. It also offers support for conditional queries. It uses libcurl
library as a client-side HTTP transfer library.

%package  xml
Summary:  Basic XML parsing and manipulation
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xml
This module exposes a script variable that provides basic parsing and
manipulation of XML documents or blocks of XML data. The processing does not
take into account any DTDs or schemas in terms of validation.

%package  xmpp
Summary:  Gateway between OpenSIPS and a jabber server
BuildRequires: expat-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xmpp
This modules is a gateway between Openser and a jabber server. It enables
the exchange of instant messages between SIP clients and XMPP(jabber)
clients.

%prep
%autosetup -p1

%build
LOCALBASE=/usr NICER=0 CFLAGS="%{optflags} -fgnu89-inline" LDFLAGS="%{?__global_ldflags}" %{?_with_oracle:ORAHOME="$ORACLE_HOME"} %{__make} all modules-readme %{?_smp_mflags} TLS=1 VERSIONTYPE=git THISREVISION=%{sub %git_commit 0 9} \
  exclude_modules="%EXCLUDE_MODULES" \
  PYTHON=/usr/bin/python3 \
  cfg_target=%{_sysconfdir}/opensips/

%install
make install TLS=1 LIBDIR=%{_lib} \
  exclude_modules="%EXCLUDE_MODULES" \
  basedir=%{buildroot} prefix=%{_prefix} \
  cfg_prefix=%{buildroot} \
  DBTEXTON=yes # fixed dbtext documentation installation

# clean some things
mkdir -p %{buildroot}/%{perl_vendorlib}
if [ -d "%{buildroot}/%{_prefix}/perl" ]; then
  # for fedora>=11
  mv %{buildroot}/%{_prefix}/perl/* \
    %{buildroot}/%{perl_vendorlib}/
else
  # for fedora<=10
  mv %{buildroot}/%{_libdir}/opensips/perl/* \
    %{buildroot}/%{perl_vendorlib}/
fi
mv %{buildroot}/%{_sysconfdir}/opensips/tls/README \
  %{buildroot}/%{_docdir}/opensips/README.tls
rm -f %{buildroot}%{_docdir}/opensips/INSTALL
mv %{buildroot}/%{_docdir}/opensips docdir

# install systemd files
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 -p packaging/redhat_fedora/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p packaging/redhat_fedora/%{name}.tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}

#install sysconfig file
install -D -p -m 644 packaging/redhat_fedora/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}



%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%{_sbindir}/opensips
%{_sbindir}/osipsconfig

%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/rootCA
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/rootCA/certs
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/rootCA/private
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/user
%dir %{_libdir}/opensips/
%dir %{_libdir}/opensips/modules/

%{_sysusersdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755, opensips, opensips) %{_localstatedir}/run/%{name}

%config(noreplace) %{_sysconfdir}/opensips/dictionary.opensips
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(640,%{name},%{name}) %config(noreplace) %{_sysconfdir}/opensips/opensips.cfg
# these files are just an examples so no need to restrict access to them
%config(noreplace) %{_sysconfdir}/opensips/tls/ca.conf
%config(noreplace) %{_sysconfdir}/opensips/tls/request.conf
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/cacert.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/certs/01.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/index.txt
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/private/cakey.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/serial
%config(noreplace) %{_sysconfdir}/opensips/tls/user.conf
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-calist.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-cert.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-cert_req.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-privkey.pem

%dir %{_datadir}/opensips/
%dir %{_datadir}/opensips/dbtext/
%dir %{_datadir}/opensips/dbtext/opensips/
%dir %{_datadir}/opensips/menuconfig_templates/

%{_datadir}/opensips/dbtext/opensips/*
%{_datadir}/opensips/menuconfig_templates/*.m4

%{_mandir}/man5/opensips.cfg.5*
%{_mandir}/man8/opensips.8*

%doc docdir/AUTHORS
%doc docdir/NEWS
%doc docdir/README
%doc docdir/README.tls
%license COPYING

%{_libdir}/opensips/modules/acc.so
%{_libdir}/opensips/modules/alias_db.so
%{_libdir}/opensips/modules/auth.so
%{_libdir}/opensips/modules/auth_aka.so
%{_libdir}/opensips/modules/auth_db.so
%{_libdir}/opensips/modules/benchmark.so
%{_libdir}/opensips/modules/cachedb_local.so
%{_libdir}/opensips/modules/cachedb_sql.so
%{_libdir}/opensips/modules/call_control.so
%{_libdir}/opensips/modules/callops.so
%{_libdir}/opensips/modules/cfgutils.so
%{_libdir}/opensips/modules/clusterer.so
%{_libdir}/opensips/modules/db_cachedb.so
%{_libdir}/opensips/modules/db_flatstore.so
%{_libdir}/opensips/modules/db_text.so
%{_libdir}/opensips/modules/db_virtual.so
%{_libdir}/opensips/modules/dialog.so
%{_libdir}/opensips/modules/dialplan.so
%{_libdir}/opensips/modules/dispatcher.so
%{_libdir}/opensips/modules/diversion.so
%{_libdir}/opensips/modules/dns_cache.so
%{_libdir}/opensips/modules/domain.so
%{_libdir}/opensips/modules/domainpolicy.so
%{_libdir}/opensips/modules/drouting.so
%{_libdir}/opensips/modules/enum.so
%{_libdir}/opensips/modules/event_datagram.so
%{_libdir}/opensips/modules/event_flatstore.so
%{_libdir}/opensips/modules/event_route.so
%{_libdir}/opensips/modules/event_routing.so
%{_libdir}/opensips/modules/event_stream.so
%{_libdir}/opensips/modules/event_virtual.so
%{_libdir}/opensips/modules/event_xmlrpc.so
%{_libdir}/opensips/modules/exec.so
%{_libdir}/opensips/modules/fraud_detection.so
%{_libdir}/opensips/modules/freeswitch.so
%{_libdir}/opensips/modules/freeswitch_scripting.so
%{_libdir}/opensips/modules/gflags.so
%{_libdir}/opensips/modules/group.so
%{_libdir}/opensips/modules/imc.so
%{_libdir}/opensips/modules/jsonrpc.so
%{_libdir}/opensips/modules/load_balancer.so
%{_libdir}/opensips/modules/mangler.so
%{_libdir}/opensips/modules/mathops.so
%{_libdir}/opensips/modules/maxfwd.so
%{_libdir}/opensips/modules/mediaproxy.so
%{_libdir}/opensips/modules/mi_datagram.so
%{_libdir}/opensips/modules/mi_fifo.so
%{_libdir}/opensips/modules/mi_script.so
%{_libdir}/opensips/modules/mid_registrar.so
%{_libdir}/opensips/modules/mqueue.so
%{_libdir}/opensips/modules/msilo.so
%{_libdir}/opensips/modules/nat_traversal.so
%{_libdir}/opensips/modules/nathelper.so
%{_libdir}/opensips/modules/options.so
%{_libdir}/opensips/modules/path.so
%{_libdir}/opensips/modules/permissions.so
%{_libdir}/opensips/modules/pike.so
%{_libdir}/opensips/modules/proto_bin.so
%{_libdir}/opensips/modules/proto_hep.so
%{_libdir}/opensips/modules/proto_smpp.so
%{_libdir}/opensips/modules/proto_ws.so
%{_libdir}/opensips/modules/qos.so
%{_libdir}/opensips/modules/qrouting.so
%{_libdir}/opensips/modules/rate_cacher.so
%{_libdir}/opensips/modules/ratelimit.so
%{_libdir}/opensips/modules/registrar.so
%{_libdir}/opensips/modules/rr.so
%{_libdir}/opensips/modules/rtp_relay.so
%{_libdir}/opensips/modules/rtpengine.so
%{_libdir}/opensips/modules/rtpproxy.so
%{_libdir}/opensips/modules/script_helper.so
%{_libdir}/opensips/modules/signaling.so
%{_libdir}/opensips/modules/sip_i.so
%{_libdir}/opensips/modules/sipcapture.so
%{_libdir}/opensips/modules/sipmsgops.so
%{_libdir}/opensips/modules/sl.so
%{_libdir}/opensips/modules/speeddial.so
%{_libdir}/opensips/modules/sql_cacher.so
%{_libdir}/opensips/modules/sqlops.so
%{_libdir}/opensips/modules/sst.so
%{_libdir}/opensips/modules/statistics.so
%{_libdir}/opensips/modules/status_report.so
%{_libdir}/opensips/modules/stun.so
%{_libdir}/opensips/modules/tcp_mgm.so
%{_libdir}/opensips/modules/textops.so
%{_libdir}/opensips/modules/tm.so
%{_libdir}/opensips/modules/topology_hiding.so
%{_libdir}/opensips/modules/tracer.so
%{_libdir}/opensips/modules/uac.so
%{_libdir}/opensips/modules/uac_auth.so
%{_libdir}/opensips/modules/uac_redirect.so
%{_libdir}/opensips/modules/uac_registrant.so
%{_libdir}/opensips/modules/userblacklist.so
%{_libdir}/opensips/modules/usrloc.so

%doc docdir/README.acc
%doc docdir/README.alias_db
%doc docdir/README.auth
%doc docdir/README.auth_aka
%doc docdir/README.auth_db
%doc docdir/README.benchmark
%doc docdir/README.cachedb_local
%doc docdir/README.cachedb_sql
%doc docdir/README.call_control
%doc docdir/README.callops
%doc docdir/README.cfgutils
%doc docdir/README.clusterer
%doc docdir/README.db_cachedb
%doc docdir/README.db_flatstore
%doc docdir/README.db_text
%doc docdir/README.db_virtual
%doc docdir/README.dialog
%doc docdir/README.dialplan
%doc docdir/README.dispatcher
%doc docdir/README.diversion
%doc docdir/README.dns_cache
%doc docdir/README.domain
%doc docdir/README.domainpolicy
%doc docdir/README.drouting
%doc docdir/README.enum
%doc docdir/README.event_datagram
%doc docdir/README.event_flatstore
%doc docdir/README.event_route
%doc docdir/README.event_routing
%doc docdir/README.event_stream
%doc docdir/README.event_virtual
%doc docdir/README.event_xmlrpc
%doc docdir/README.exec
%doc docdir/README.fraud_detection
%doc docdir/README.freeswitch
%doc docdir/README.freeswitch_scripting
%doc docdir/README.gflags
%doc docdir/README.group
%doc docdir/README.imc
%doc docdir/README.jsonrpc
%doc docdir/README.load_balancer
%doc docdir/README.mangler
%doc docdir/README.mathops
%doc docdir/README.maxfwd
%doc docdir/README.mediaproxy
%doc docdir/README.mi_datagram
%doc docdir/README.mi_fifo
%doc docdir/README.mi_script
%doc docdir/README.mid_registrar
%doc docdir/README.mqueue
%doc docdir/README.msilo
%doc docdir/README.nat_traversal
%doc docdir/README.nathelper
%doc docdir/README.options
%doc docdir/README.path
%doc docdir/README.permissions
%doc docdir/README.pike
%doc docdir/README.proto_bin
%doc docdir/README.proto_hep
%doc docdir/README.proto_smpp
%doc docdir/README.proto_ws
%doc docdir/README.qos
%doc docdir/README.qrouting
%doc docdir/README.rate_cacher
%doc docdir/README.ratelimit
%doc docdir/README.registrar
%doc docdir/README.rr
%doc docdir/README.rtp_relay
%doc docdir/README.rtpengine
%doc docdir/README.rtpproxy
%doc docdir/README.script_helper
%doc docdir/README.signaling
%doc docdir/README.sip_i
%doc docdir/README.sipcapture
%doc docdir/README.sipmsgops
%doc docdir/README.sl
%doc docdir/README.speeddial
%doc docdir/README.sql_cacher
%doc docdir/README.sqlops
%doc docdir/README.sst
%doc docdir/README.statistics
%doc docdir/README.status_report
%doc docdir/README.stun
%doc docdir/README.tcp_mgm
%doc docdir/README.textops
%doc docdir/README.tm
%doc docdir/README.topology_hiding
%doc docdir/README.tracer
%doc docdir/README.uac
%doc docdir/README.uac_auth
%doc docdir/README.uac_redirect
%doc docdir/README.uac_registrant
%doc docdir/README.userblacklist
%doc docdir/README.usrloc

%files aaa_diameter
%{_libdir}/opensips/modules/aaa_diameter.so
%doc docdir/README.aaa_diameter

%files aaa_radius
%{_libdir}/opensips/modules/aaa_radius.so
%doc docdir/README.aaa_radius

%files acc
%{_libdir}/opensips/modules/acc.so
%doc docdir/README.acc

%files aka_av_diameter
%{_libdir}/opensips/modules/aka_av_diameter.so
%doc docdir/README.aka_av_diameter

%files auth_aaa
%{_libdir}/opensips/modules/auth_aaa.so
%doc docdir/README.auth_aaa

%files auth_jwt
%{_libdir}/opensips/modules/auth_jwt.so
%doc docdir/README.auth_jwt

%files b2bua
%{_libdir}/opensips/modules/b2b_entities.so
%{_libdir}/opensips/modules/b2b_logic.so
%{_libdir}/opensips/modules/b2b_sca.so
%{_libdir}/opensips/modules/b2b_sdp_demux.so
%doc docdir/README.b2b_entities
%doc docdir/README.b2b_logic
%doc docdir/README.b2b_sca
%doc docdir/README.b2b_sdp_demux

%files cachedb_couchbase
%{_libdir}/opensips/modules/cachedb_couchbase.so
%doc docdir/README.cachedb_couchbase

%files cachedb_memcached
%{_libdir}/opensips/modules/cachedb_memcached.so
%doc docdir/README.cachedb_memcached

%files cachedb_mongodb
%{_libdir}/opensips/modules/cachedb_mongodb.so
%doc docdir/README.cachedb_mongodb

%files cachedb_redis
%{_libdir}/opensips/modules/cachedb_redis.so
%doc docdir/README.cachedb_redis

%files call_center
%attr(640,%{name},%{name}) %config(noreplace) %{_sysconfdir}/opensips/scenario_callcenter.xml
%{_libdir}/opensips/modules/call_center.so
%doc docdir/README.call_center

%files carrierroute
%{_libdir}/opensips/modules/carrierroute.so
%doc docdir/README.carrierroute

%files cgrates
%{_libdir}/opensips/modules/cgrates.so
%doc docdir/README.cgrates

%files compression
%{_libdir}/opensips/modules/compression.so
%doc docdir/README.compression

%files cpl_c
%{_libdir}/opensips/modules/cpl_c.so
%doc docdir/README.cpl_c

%files db_berkeley
%{_sbindir}/bdb_recover
%{_libdir}/opensips/modules/db_berkeley.so
%dir %{_datadir}/opensips/db_berkeley
%dir %{_datadir}/opensips/db_berkeley/opensips
%{_datadir}/opensips/db_berkeley/opensips/*
%doc docdir/README.db_berkeley

%files db_http
%{_libdir}/opensips/modules/db_http.so
%doc docdir/README.db_http

%files db_mysql
%{_libdir}/opensips/modules/db_mysql.so
%dir %{_datadir}/opensips/mysql
%{_datadir}/opensips/mysql/*.sql
%doc docdir/README.db_mysql

%if 0%{?_with_oracle}
%files db_oracle
%{_sbindir}/opensips_orasel
%{_libdir}/opensips/modules/db_oracle.so
%dir %{_datadir}/opensips/oracle
%{_datadir}/opensips/oracle/*
%doc docdir/README.db_oracle
%endif

%files db_perlvdb
%dir %{perl_vendorlib}/OpenSIPS/VDB
%dir %{perl_vendorlib}/OpenSIPS/VDB/Adapter
%{_libdir}/opensips/modules/db_perlvdb.so
%{perl_vendorlib}/OpenSIPS/VDB.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/AccountingSIPtrace.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Alias.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Auth.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Describe.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Speeddial.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/TableVersions.pm
%{perl_vendorlib}/OpenSIPS/VDB/Column.pm
%{perl_vendorlib}/OpenSIPS/VDB/Pair.pm
%{perl_vendorlib}/OpenSIPS/VDB/ReqCond.pm
%{perl_vendorlib}/OpenSIPS/VDB/Result.pm
%{perl_vendorlib}/OpenSIPS/VDB/VTab.pm
%{perl_vendorlib}/OpenSIPS/VDB/Value.pm
%doc docdir/README.db_perlvdb

%files db_postgresql
%{_libdir}/opensips/modules/db_postgres.so
%dir %{_datadir}/opensips/postgres
%{_datadir}/opensips/postgres/*.sql
%doc docdir/README.db_postgres

%files db_sqlite
%{_libdir}/opensips/modules/db_sqlite.so
%dir %{_datadir}/opensips/sqlite
%{_datadir}/opensips/sqlite/*.sql
%doc docdir/README.db_sqlite

%files db_unixodbc
%{_libdir}/opensips/modules/db_unixodbc.so
%doc docdir/README.db_unixodbc

%files event_kafka
%{_libdir}/opensips/modules/event_kafka.so
%doc docdir/README.event_kafka

%files emergency
%{_libdir}/opensips/modules/emergency.so
%doc docdir/README.emergency

%files event_rabbitmq
%{_libdir}/opensips/modules/event_rabbitmq.so
%doc docdir/README.event_rabbitmq

%files h350
%{_libdir}/opensips/modules/h350.so
%doc docdir/README.h350

%files httpd
%{_libdir}/opensips/modules/httpd.so
%doc docdir/README.httpd

%files http2d
%{_libdir}/opensips/modules/http2d.so
%doc docdir/README.http2d

%files identity
%{_libdir}/opensips/modules/identity.so
%doc docdir/README.identity

%files jabber
%{_libdir}/opensips/modules/jabber.so
%doc docdir/README.jabber

%files json
%{_libdir}/opensips/modules/json.so
%doc docdir/README.json

%files ldap
%{_libdir}/opensips/modules/ldap.so
%doc docdir/README.ldap

%files lua
%{_libdir}/opensips/modules/lua.so
%doc docdir/README.lua

%files media_exchange
%{_libdir}/opensips/modules/media_exchange.so
%doc docdir/README.media_exchange

%files mi_html
%{_libdir}/opensips/modules/mi_html.so
%doc docdir/README.mi_html

%files mi_http
%{_libdir}/opensips/modules/mi_http.so
%doc docdir/README.mi_http

%files mi_xmlrpc_ng
%{_libdir}/opensips/modules/mi_xmlrpc_ng.so
%doc docdir/README.mi_xmlrpc_ng

%files mmgeoip
%{_libdir}/opensips/modules/mmgeoip.so
%doc docdir/README.mmgeoip

%files msrp
%{_libdir}/opensips/modules/msrp_gateway.so
%{_libdir}/opensips/modules/msrp_relay.so
%{_libdir}/opensips/modules/msrp_ua.so
%{_libdir}/opensips/modules/proto_msrp.so
%doc docdir/README.msrp_gateway
%doc docdir/README.msrp_relay
%doc docdir/README.msrp_ua
%doc docdir/README.proto_msrp

%files peering
%{_libdir}/opensips/modules/peering.so
%doc docdir/README.peering

%files perl
%dir %{perl_vendorlib}/OpenSIPS
%dir %{perl_vendorlib}/OpenSIPS/LDAPUtils
%dir %{perl_vendorlib}/OpenSIPS/Utils
%{_libdir}/opensips/modules/perl.so
%{perl_vendorlib}/OpenSIPS.pm
%{perl_vendorlib}/OpenSIPS/Constants.pm
%{perl_vendorlib}/OpenSIPS/LDAPUtils/LDAPConf.pm
%{perl_vendorlib}/OpenSIPS/LDAPUtils/LDAPConnection.pm
%{perl_vendorlib}/OpenSIPS/Message.pm
%{perl_vendorlib}/OpenSIPS/Utils/PhoneNumbers.pm
%{perl_vendorlib}/OpenSIPS/Utils/Debug.pm
%doc docdir/README.perl

%files pi_http
%{_libdir}/opensips/modules/pi_http.so
%{_datadir}/opensips/pi_http/
%doc docdir/README.pi_http

%files presence
%{_libdir}/opensips/modules/presence.so
%doc docdir/README.presence

%files presence_callinfo
%{_libdir}/opensips/modules/presence_callinfo.so
%doc docdir/README.presence_callinfo

%files presence_dfks
%{_libdir}/opensips/modules/presence_dfks.so
%doc docdir/README.presence_dfks

%files presence_dialoginfo
%{_libdir}/opensips/modules/presence_dialoginfo.so
%doc docdir/README.presence_dialoginfo

%files presence_mwi
%{_libdir}/opensips/modules/presence_mwi.so
%doc docdir/README.presence_mwi

%files presence_reginfo
%{_libdir}/opensips/modules/presence_reginfo.so
%doc docdir/README.presence_reginfo

%files presence_xcapdiff
%{_libdir}/opensips/modules/presence_xcapdiff.so

%files presence_xml
%{_libdir}/opensips/modules/presence_xml.so
%doc docdir/README.presence_xml

%files prometheus
%{_libdir}/opensips/modules/prometheus.so
%doc docdir/README.prometheus

%files proto_bins
%{_libdir}/opensips/modules/proto_bins.so
%doc docdir/README.proto_bins

%files proto_ipsec
%{_libdir}/opensips/modules/proto_ipsec.so
%doc docdir/README.proto_ipsec

%files proto_sctp
%{_libdir}/opensips/modules/proto_sctp.so
%doc docdir/README.proto_sctp

%files proto_tls
%{_libdir}/opensips/modules/proto_tls.so
%doc docdir/README.proto_tls

%files proto_wss
%{_libdir}/opensips/modules/proto_wss.so
%doc docdir/README.proto_wss

%files pua
%{_libdir}/opensips/modules/pua.so
%doc docdir/README.pua

%files pua_bla
%{_libdir}/opensips/modules/pua_bla.so
%doc docdir/README.pua_bla

%files pua_dialoginfo
%{_libdir}/opensips/modules/pua_dialoginfo.so
%doc docdir/README.pua_dialoginfo

%files pua_mi
%{_libdir}/opensips/modules/pua_mi.so
%doc docdir/README.pua_mi

%files pua_reginfo
%{_libdir}/opensips/modules/pua_reginfo.so
%doc docdir/README.pua_reginfo

%files pua_usrloc
%{_libdir}/opensips/modules/pua_usrloc.so
%doc docdir/README.pua_usrloc

%files pua_xmpp
%{_libdir}/opensips/modules/pua_xmpp.so
%doc docdir/README.pua_xmpp

# FIXME disable python2 until upstream adds support for Py3
#%files -n python2-opensips
#%{_libdir}/opensips/modules/python.so

%files rabbitmq
%{_libdir}/opensips/modules/rabbitmq.so
%doc docdir/README.rabbitmq

%files rabbitmq_consumer
%{_libdir}/opensips/modules/rabbitmq_consumer.so
%doc docdir/README.rabbitmq_consumer

%files regex
%{_libdir}/opensips/modules/regex.so
%doc docdir/README.regex

%files rest_client
%{_libdir}/opensips/modules/rest_client.so
%doc docdir/README.rest_client

%files rls
%{_libdir}/opensips/modules/rls.so
%doc docdir/README.rls

%files siprec
%{_libdir}/opensips/modules/siprec.so
%doc docdir/README.siprec

%files snmpstats
%{_libdir}/opensips/modules/snmpstats.so
%doc docdir/README.snmpstats
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/OPENSER-MIB
%{_datadir}/snmp/mibs/OPENSER-REG-MIB
%{_datadir}/snmp/mibs/OPENSER-SIP-COMMON-MIB
%{_datadir}/snmp/mibs/OPENSER-SIP-SERVER-MIB
%{_datadir}/snmp/mibs/OPENSER-TC

%files stir_shaken
%{_libdir}/opensips/modules/stir_shaken.so
%doc docdir/README.stir_shaken

%files tls_mgm
%{_libdir}/opensips/modules/tls_mgm.so
%doc docdir/README.tls_mgm

%files tls_openssl
%{_libdir}/opensips/modules/tls_openssl.so
%doc docdir/README.tls_openssl

%files uuid
%{_libdir}/opensips/modules/uuid.so
%doc docdir/README.uuid

%files xcap
%{_libdir}/opensips/modules/xcap.so
%doc docdir/README.xcap

%files xcap_client
%{_libdir}/opensips/modules/xcap_client.so
%doc docdir/README.xcap_client

%files xml
%{_libdir}/opensips/modules/xml.so
%doc docdir/README.xml

%files xmpp
%{_libdir}/opensips/modules/xmpp.so
%doc docdir/README.xmpp


%changelog
%autochangelog
