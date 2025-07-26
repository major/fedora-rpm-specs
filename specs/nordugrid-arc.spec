%global with_xrootd %{!?_without_xrootd:1}%{?_without_xrootd:0}

%global with_pylint 0

%global with_s3 1

%if %{?fedora}%{!?fedora:0} >= 43 || %{?rhel}%{!?rhel:0} >= 10
%global with_gfal 0
%else
%global with_gfal 1
%endif

%global with_xmlsec1 %{!?_without_xmlsec1:1}%{?_without_xmlsec1:0}

%global with_ldns 1

%global with_ldap_service 1

%global pkgdir arc

# bash-completion
%global _bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo %{_sysconfdir}/bash_completion.d)

Name:		nordugrid-arc
Version:	7.0.0
Release:	5%{?dist}
Summary:	Advanced Resource Connector Middleware
#		Apache-2.0: most files
#		MIT: src/external/cJSON/cJSON.c src/external/cJSON/cJSON.h
License:	Apache-2.0 AND MIT
URL:		http://www.nordugrid.org/
Source:		http://download.nordugrid.org/packages/%{name}/releases/%{version}/src/%{name}-%{version}.tar.gz
#		https://source.coderefinery.org/nordugrid/arc/-/merge_requests/1903
Patch0:		0001-Update-the-VOMS-attribute-certificate-signing-hash-a.patch
#		https://source.coderefinery.org/nordugrid/arc/-/merge_requests/1892
Patch1:		0001-Fix-shell-syntax-errors-reported-by-lintian.patch
#		https://source.coderefinery.org/nordugrid/arc/-/merge_requests/1926
Patch2:		0001-ValueError-action-store_true-is-not-valid-for-positi.patch

#		Packages dropped without replacements
Obsoletes:	%{name}-arcproxyalt < 6.0.0
Obsoletes:	%{name}-java < 6.0.0
Obsoletes:	%{name}-egiis < 6.0.0
Obsoletes:	%{name}-acix-cache < 6.0.0
Obsoletes:	%{name}-acix-core < 7.0.0
Obsoletes:	%{name}-acix-scanner < 7.0.0
Obsoletes:	%{name}-acix-index < 7.0.0
Obsoletes:	%{name}-arex-python-lrms < 7.0.0
Obsoletes:	%{name}-gridftpd < 7.0.0
Obsoletes:	python2-%{name} < 7.0.0
Obsoletes:	%{name}-nordugridmap < 7.0.0
Obsoletes:	%{name}-gridmap-utils < 6.0.0
Obsoletes:	%{name}-plugins-gridftpjob < 7.0.0
Obsoletes:	%{name}-plugins-ldap < 7.0.0
%if ! %{with_ldap_service}
Obsoletes:	%{name}-infosys-ldap < %{version}-%{release}
Obsoletes:	%{name}-ldap-infosys < 6.0.0
Obsoletes:	%{name}-aris < 6.0.0
%endif
%if ! %{with_gfal}
Obsoletes:	%{name}-plugins-gfal < %{version}-%{release}
%endif

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cppunit-devel
BuildRequires:	pkgconfig
BuildRequires:	systemd-rpm-macros
BuildRequires:	systemd-devel
BuildRequires:	libuuid-devel
BuildRequires:	gettext-devel
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-pip
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-wheel
%if %{with_pylint}
BuildRequires:	pylint
%endif
BuildRequires:	glibmm24-devel
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl
BuildRequires:	openssl-devel
%if %{with_xmlsec1}
BuildRequires:	xmlsec1-devel >= 1.2.4
BuildRequires:	xmlsec1-openssl-devel >= 1.2.4
%endif
BuildRequires:	nss-devel
BuildRequires:	globus-common-devel
BuildRequires:	globus-ftp-client-devel
BuildRequires:	globus-ftp-control-devel
BuildRequires:	globus-gssapi-gsi-devel >= 12.2
%if %{with_xrootd}
BuildRequires:	xrootd-client-devel >= 1:4.5.0
%endif
%if %{with_gfal}
BuildRequires:	gfal2-devel
%endif
%if %{with_s3}
BuildRequires:	libs3-devel
%endif
BuildRequires:	perl-generators
# Needed for Boinc backend testing during make check
BuildRequires:	perl(DBI)
# Needed for infoprovider testing during make check
BuildRequires:	perl(English)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(XML::Simple)
# Needed for LRMS testing during make check
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::Simple)
BuildRequires:	swig
BuildRequires:	libtool-ltdl-devel
BuildRequires:	sqlite-devel >= 3.6
%if %{with_ldns}
BuildRequires:	ldns-devel >= 1.6.8
%endif
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	help2man
Requires:	hostname
Requires:	openssl

%description
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC middleware is a software solution that uses distributed
computing technologies to enable sharing and federation of computing
resources across different administrative and application domains.
ARC is used to create distributed infrastructures of various scope and
complexity, from campus to national and global deployments.

%package client
Summary:	ARC command line clients
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}

%description client
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This client package contains all the CLI tools that are needed to
operate with x509 proxies, submit and manage jobs and handle data
transfers.

%package hed
Summary:	ARC Hosting Environment Daemon
Requires:	%{name} = %{version}-%{release}
%{?systemd_requires}

%description hed
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC Hosting Environment Daemon (HED) is a Web Service container
for ARC services.

%package datadelivery-service
Summary:	ARC data delivery service
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-hed = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
Requires:	%{name}-arcctl-service = %{version}-%{release}
Requires:	logrotate
%{?systemd_requires}

%description datadelivery-service
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC data delivery service.

%if %{with_ldap_service}
%package infosys-ldap
Summary:	ARC LDAP-based information services
BuildArch:	noarch
Requires:	openldap-servers
Requires:	bdii
Requires:	glue-schema >= 2.0.10
Requires:	%{name}-arcctl-service = %{version}-%{release}
Requires:	logrotate
Provides:	%{name}-ldap-infosys = %{version}-%{release}
Obsoletes:	%{name}-ldap-infosys < 6.0.0
Provides:	%{name}-aris = %{version}-%{release}
Obsoletes:	%{name}-aris < 6.0.0
%{?systemd_requires}
Requires(post):		policycoreutils-python-utils
Requires(postun):	policycoreutils-python-utils

%description infosys-ldap
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC information services relying on BDII and
LDAP technologies to publish ARC CE information according to various
LDAP schemas. Please note that the information collectors are part of
another package, the nordugrid-arc-arex.
%endif

%package monitor
Summary:	ARC LDAP monitor web application
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	php
Requires:	php-gd
Requires:	php-ldap
Obsoletes:	%{name}-ldap-monitor < 6.0.0
Obsoletes:	%{name}-ws-monitor < 6.0.0

%description monitor
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the PHP web application that is used to set up a
web-based monitor which pulls information from the LDAP information
system and visualizes it.

%package arcctl
Summary:	ARC Control Tool
Requires:	%{name} = %{version}-%{release}
Requires:	python3-jwcrypto

%description arcctl
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC Control Tool with basic set of control
modules suitable for both server and client side.

%package arcctl-service
Summary:	ARC Control Tool - service control modules
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-arcctl = %{version}-%{release}

%description arcctl-service
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the service control modules for ARC Contol Tool
that allow working with server-side config and manage ARC services.

%package arex
Summary:	ARC Resource-coupled EXecution service
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-hed = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
Requires:	%{name}-arcctl = %{version}-%{release}
Requires:	%{name}-arcctl-service = %{version}-%{release}
Requires:	logrotate
Requires:	findutils
Requires:	procps
Provides:	%{name}-cache-service = %{version}-%{release}
Obsoletes:	%{name}-cache-service < 6.0.0
Provides:	%{name}-candypond = %{version}-%{release}
Obsoletes:	%{name}-candypond < 6.0.0

Requires(post):		%{name}-arcctl = %{version}-%{release}
Requires(preun):	%{name}-arcctl = %{version}-%{release}
Requires(post):		hostname
Requires(post):		openssl
%{?systemd_requires}

%description arex
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC Resource-coupled EXecution service (AREX) is the Computing
Element of the ARC middleware. AREX offers a full-featured middle
layer to manage computational tasks including interfacing to local
batch systems, taking care of complex environments such as data
staging, data caching, software environment provisioning, information
collection and exposure, accounting information gathering and
publishing.

%package arex-lrms-contrib
Summary:	ARC Resource-coupled EXecution service - contributed LRMS backends
BuildArch:	noarch
Requires:	%{name}-arex = %{version}-%{release}
#		Split from AREX package
Obsoletes:	%{name}-arex < 7.0.0

%description arex-lrms-contrib
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The AREX contributed LRMS backends package contains additional LRMS
support script contributed by the ARC user community.

%package community-rtes
Summary:	ARC community defined RTEs support
Requires:	%{name}-arex = %{version}-%{release}
Requires:	%{name}-arcctl = %{version}-%{release}
Requires:	gnupg2
Requires:	python3-dns

%description community-rtes
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

Community RTEs is the framework that allows deploying software packages
(tarballs, containers, etc) provided by trusted communities to ARC CE
using simple arcctl commands.
It is released as a technology preview.

%package plugins-needed
Summary:	ARC base plugins
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-plugins-arcrest = %{version}-%{release}
Obsoletes:	%{name}-plugins-arcrest < 7.0.0

%description plugins-needed
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC base plugins. This includes the Message Chain Components (MCCs)
and Data Manager Components (DMCs).

%package plugins-globus
Summary:	ARC Globus plugins (compat)
Requires:	%{name}-plugins-gridftp = %{version}-%{release}
Requires:	%{name}-plugins-lcas-lcmaps = %{version}-%{release}

%description plugins-globus
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC Globus plugins. This compat metapackage brings all Globus
dependent plugins at once, including: Data Manager Components (DMCs)
and LCAS/LCMAPS tools.

This package is meant to allow smooth transition and will be removed from
the upcoming releases.

%package plugins-globus-common
Summary:	ARC Globus plugins common libraries
Requires:	%{name} = %{version}-%{release}

%description plugins-globus-common
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC Globus plugins common libraries package includes the bundle of
necessary Globus libraries needed for all other globus-dependent ARC
components.

%package plugins-gridftp
Summary:	ARC Globus dependent DMCs
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-globus-common = %{version}-%{release}

%description plugins-gridftp
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC Globus GridFTP plugins. These allow access to data through the
gridftp protocol.

%package plugins-lcas-lcmaps
Summary:	ARC LCAS/LCMAPS plugins
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-globus-common = %{version}-%{release}
Requires:	globus-gssapi-gsi >= 12.2

%description plugins-lcas-lcmaps
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC LCAS/LCMAPS tools allow configuring ARC CE to use LCAS/LCMAPS
services for authorization and mapping.

%if %{with_xrootd}
%package plugins-xrootd
Summary:	ARC xrootd plugins
Requires:	%{name} = %{version}-%{release}

%description plugins-xrootd
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC xrootd plugins. These allow access to data through the xrootd
protocol.
%endif

%if %{with_gfal}
%package plugins-gfal
Summary:	ARC GFAL2 plugins
Requires:	%{name} = %{version}-%{release}

%description plugins-gfal
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC plugins for GFAL2. This allows third-party transfer and adds
support for several extra transfer protocols (rfio, dcap, gsidcap).
Support for specific protocols is provided by separate 3rd-party GFAL2
plugin packages.
%endif

%if %{with_s3}
%package plugins-s3
Summary:	ARC S3 plugins
Requires:	%{name} = %{version}-%{release}

%description plugins-s3
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC plugins for S3. These allow access to data through the S3
protocol.
%endif

%package plugins-internal
Summary:	ARC internal plugin
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-arex = %{version}-%{release}

%description plugins-internal
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC internal plugin. A special interface aimed for restrictive HPC
sites, to be used with a local installation of the ARC Control Tower.

%package plugins-python
Summary:	ARC Python dependent plugin
Requires:	%{name} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-%{name} = %{version}-%{release}

%description plugins-python
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC plugins dependent on Python.

%package devel
Summary:	ARC development files
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm24-devel
Requires:	glib2-devel
Requires:	libxml2-devel
Requires:	openssl-devel

%description devel
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

Header files and libraries needed to develop applications using ARC.

%package -n python%{python3_pkgversion}-%{name}
Summary:	ARC Python 3 wrapper
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Requires:	%{name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

Python 3 bindings for ARC.

%package test-utils
Summary:	ARC test tools
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
Obsoletes:	%{name}-misc-utils < 6.0.0

%description test-utils
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains a few utilities useful to test various ARC
subsystems. The package is not required by users or sysadmins and it
is mainly for developers.

%package archery-manage
Summary:	ARCHERY administration tool
BuildArch:	noarch
Requires:	python3-dns
Requires:	python3-ldap

%description archery-manage
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the archery-manage utility for administration of
an ARCHERY DNS-embedded service endpoint registry.

%package wn
Summary:	ARC optional worker nodes components

%description wn
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the optional components that provide new job
management features on the worker nodes (WN).

%package -n python%{python3_pkgversion}-arcrest
Summary:	ARC REST client
%{?python_provide:%python_provide python%{python3_pkgversion}-arcrest}
BuildArch:	noarch

%description -n python%{python3_pkgversion}-arcrest
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC REST client.

%package arc-exporter
Summary:	ARC Prometheus exporter service
BuildArch:	noarch
Requires:	python3-prometheus_client

%description arc-exporter
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the Prometheus arc-exporter which collects and
publishes metrics about jobs and datastaging on the ARC-CE.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
autoreconf -v -f -i
%configure --disable-static \
%if %{with_gfal}
     --enable-gfal \
%endif
%if %{with_s3}
     --enable-s3 \
%endif
     --with-python=python3 \
%if ! %{with_pylint}
     --disable-pylint \
%endif
%if ! %{with_xrootd}
     --disable-xrootd \
%endif
%if ! %{with_ldns}
     --disable-ldns \
%endif
     --enable-internal \
     --enable-systemd \
     --with-systemd-units-location=%{_unitdir} \
%if ! %{with_ldap_service}
     --disable-ldap-service \
%endif
     --disable-doc \
     --docdir=%{_pkgdocdir}

%make_build

%check
%make_build check

%install
%make_install

# Install Logrotate.
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 debian/%{name}-arex.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-arex
%if %{with_ldap_service}
install -p -m 644 debian/%{name}-infosys-ldap.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-infosys-ldap
%endif
install -p -m 644 debian/%{name}-datadelivery-service.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-datadelivery-service

find %{buildroot} -type f -name \*.la -exec rm -fv '{}' ';'

# libarcglobusutils is not part of the ARC api.
find %{buildroot} -name libarcglobusutils.so -exec rm -fv '{}' ';'

rm -f %{buildroot}%{python3_sitelib}/pyarcrest-*.*-info/direct_url.json

# Create log directory
mkdir -p %{buildroot}%{_localstatedir}/log/arc

# Create spool directories for Jura
mkdir -p %{buildroot}%{_localstatedir}/spool/arc
mkdir -p %{buildroot}%{_localstatedir}/spool/arc/ssm
mkdir -p %{buildroot}%{_localstatedir}/spool/arc/urs

# create config directory
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/arc.conf.d

%find_lang %{name}

# Remove examples and let RPM package them under /usr/share/doc using the doc macro
rm -rf %{buildroot}%{_datadir}/%{pkgdir}/examples
make -C src/libs/data-staging/examples	DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/hed/libs/compute/examples	DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/hed/libs/data/examples	DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/hed/acc/PythonBroker	DESTDIR=$PWD/docdir/python pkgdatadir= install-exampleDATA
make -C python/examples			DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/tests/echo			DESTDIR=$PWD/docdir/hed	   pkgdatadir= install-exampleDATA
make -C src/hed				DESTDIR=$PWD/docdir/hed	   pkgdatadir= install-profileDATA

# client.conf needs special handling
make -C src/clients DESTDIR=%{buildroot} install-exampleDATA

# Link to client.conf from doc
ln -s %{_datadir}/%{pkgdir}/examples/client.conf $PWD/docdir/client.conf

%post hed
%systemd_post arched.service

%preun hed
%systemd_preun arched.service

%postun hed
%systemd_postun_with_restart arched.service

%pre arex
# Service renamed - remove old files
systemctl --no-reload disable a-rex.service > /dev/null 2>&1 || :
systemctl stop a-rex.service > /dev/null 2>&1 || :

%post arex
%systemd_post arc-arex.service
%systemd_post arc-arex-ws.service

# out-of-package testing host certificate
if [ $1 -eq 1 ]; then
  arcctl test-ca init
  arcctl test-ca hostcert
fi

%preun arex
%systemd_preun arc-arex.service
%systemd_preun arc-arex-ws.service

if [ $1 -eq 0 ]; then
  arcctl test-ca cleanup
fi

%postun arex
%systemd_postun_with_restart arc-arex.service
%systemd_postun_with_restart arc-arex-ws.service

%post datadelivery-service
%systemd_post arc-datadelivery-service.service

%preun datadelivery-service
%systemd_preun arc-datadelivery-service.service

%postun datadelivery-service
%systemd_postun_with_restart arc-datadelivery-service.service

%if %{with_ldap_service}

%post infosys-ldap
%systemd_post arc-infosys-ldap.service
semanage port -a -t ldap_port_t -p tcp 2135 2>/dev/null || :
semanage fcontext -a -t slapd_etc_t "/var/run/arc/infosys/bdii-slapd\.conf" 2>/dev/null || :
semanage fcontext -a -t slapd_db_t "/var/lib/arc/bdii/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "/var/run/arc/bdii/db(/.*)?" 2>/dev/null || :

%preun infosys-ldap
%systemd_preun arc-infosys-ldap.service

%postun infosys-ldap
%systemd_postun_with_restart arc-infosys-ldap.service
if [ $1 -eq 0 ]; then
  semanage port -d -t ldap_port_t -p tcp 2135 2>/dev/null || :
  semanage fcontext -d -t slapd_etc_t "/var/run/arc/infosys/bdii-slapd\.conf" 2>/dev/null || :
  semanage fcontext -d -t slapd_db_t "/var/lib/arc/bdii/db(/.*)?" 2>/dev/null || :
  semanage fcontext -d -t slapd_var_run_t "/var/run/arc/bdii/db(/.*)?" 2>/dev/null || :
fi

%triggerun infosys-ldap -- bdii
systemctl try-restart arc-infosys-ldap.service > /dev/null 2>&1 || :

%triggerpostun infosys-ldap -- %{name}-ldap-infosys
# Uninstalling the old %{name}-ldap-infosys will remove some selinux config
# for %{name}-infosys-ldap - put them back in this triggerpostun script
semanage port -a -t ldap_port_t -p tcp 2135 2>/dev/null || :
semanage fcontext -a -t slapd_etc_t "/var/run/arc/infosys/bdii-slapd\.conf" 2>/dev/null || :

%triggerpostun infosys-ldap -- %{name}-aris
# Uninstalling the old %{name}-aris will remove some selinux config
# for %{name}-infosys-ldap - put them back in this triggerpostun script
semanage fcontext -a -t slapd_db_t "/var/lib/arc/bdii/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "/var/run/arc/bdii/db(/.*)?" 2>/dev/null || :

%endif

%files -f %{name}.lang
%doc src/doc/arc.conf.reference src/doc/arc.conf.DELETED
%doc README AUTHORS
%license LICENSE NOTICE
%{_libdir}/libarccompute.so.*
%{_libdir}/libarccommunication.so.*
%{_libdir}/libarccommon.so.*
%{_libdir}/libarccredential.so.*
%{_libdir}/libarccredentialstore.so.*
%{_libdir}/libarccrypto.so.*
%{_libdir}/libarcdata.so.*
%{_libdir}/libarcdatastaging.so.*
%{_libdir}/libarcloader.so.*
%{_libdir}/libarcmessage.so.*
%{_libdir}/libarcsecurity.so.*
%{_libdir}/libarcotokens.so.*
%{_libdir}/libarcinfosys.so.*
%{_libdir}/libarcwsaddressing.so.*
%{_libdir}/libarcwssecurity.so.*
%if %{with_xmlsec1}
%{_libdir}/libarcxmlsec.so.*
%endif
%dir %{_libdir}/%{pkgdir}
# We need to have libmodcrypto.so close to libarccrypto
%{_libdir}/%{pkgdir}/libmodcrypto.so
%{_libdir}/%{pkgdir}/libmodcrypto.apd
# We need to have libmodcredential.so close to libarccredential
%{_libdir}/%{pkgdir}/libmodcredential.so
%{_libdir}/%{pkgdir}/libmodcredential.apd
%{_libdir}/%{pkgdir}/arc-file-access
%{_libdir}/%{pkgdir}/arc-hostname-resolver
%{_libdir}/%{pkgdir}/DataStagingDelivery
%{_libdir}/%{pkgdir}/arc-dmc
%dir %{_libexecdir}/%{pkgdir}
%{_libexecdir}/%{pkgdir}/arcconfig-parser
%dir %{python3_sitearch}/%{pkgdir}
%{python3_sitearch}/%{pkgdir}/__init__.py
%{python3_sitearch}/%{pkgdir}/paths.py
%{python3_sitearch}/%{pkgdir}/paths_dist.py
%dir %{python3_sitearch}/%{pkgdir}/__pycache__
%{python3_sitearch}/%{pkgdir}/__pycache__/__init__.*
%{python3_sitearch}/%{pkgdir}/__pycache__/paths.*
%{python3_sitearch}/%{pkgdir}/__pycache__/paths_dist.*
%{python3_sitearch}/%{pkgdir}/utils
%dir %{_datadir}/%{pkgdir}
%{_datadir}/%{pkgdir}/arc.parser.defaults
%dir %{_datadir}/%{pkgdir}/test-jobs
%{_datadir}/%{pkgdir}/test-jobs/test-job-*
%{_datadir}/%{pkgdir}/schema

%files client
%doc docdir/client.conf
%{_bindir}/arccat
%{_bindir}/arcclean
%{_bindir}/arccp
%{_bindir}/arcget
%{_bindir}/arcinfo
%{_bindir}/arckill
%{_bindir}/arcls
%{_bindir}/arcmkdir
%{_bindir}/arcrename
%{_bindir}/arcproxy
%{_bindir}/arcrenew
%{_bindir}/arcresume
%{_bindir}/arcrm
%{_bindir}/arcstat
%{_bindir}/arcsub
%{_bindir}/arcsync
%{_bindir}/arctest
%dir %{_datadir}/%{pkgdir}/examples
%{_datadir}/%{pkgdir}/examples/client.conf
%dir %{_sysconfdir}/%{pkgdir}
%config(noreplace) %{_sysconfdir}/%{pkgdir}/client.conf
%doc %{_mandir}/man1/arccat.1*
%doc %{_mandir}/man1/arcclean.1*
%doc %{_mandir}/man1/arccp.1*
%doc %{_mandir}/man1/arcget.1*
%doc %{_mandir}/man1/arcinfo.1*
%doc %{_mandir}/man1/arckill.1*
%doc %{_mandir}/man1/arcls.1*
%doc %{_mandir}/man1/arcmkdir.1*
%doc %{_mandir}/man1/arcrename.1*
%doc %{_mandir}/man1/arcproxy.1*
%doc %{_mandir}/man1/arcrenew.1*
%doc %{_mandir}/man1/arcresume.1*
%doc %{_mandir}/man1/arcrm.1*
%doc %{_mandir}/man1/arcstat.1*
%doc %{_mandir}/man1/arcsub.1*
%doc %{_mandir}/man1/arcsync.1*
%doc %{_mandir}/man1/arctest.1*
%dir %{_bashcompdir}
%{_bashcompdir}/arc-client-tools

%files hed
%doc docdir/hed/*
%{_unitdir}/arched.service
%{_sbindir}/arched
%{_libdir}/%{pkgdir}/libecho.so
%{_libdir}/%{pkgdir}/libecho.apd
%{_datadir}/%{pkgdir}/arched-start
%{_datadir}/%{pkgdir}/profiles
%doc %{_mandir}/man8/arched.8*
%doc %{_mandir}/man5/arc.conf.5*

%files datadelivery-service
%{_unitdir}/arc-datadelivery-service.service
%{_libdir}/%{pkgdir}/libdatadeliveryservice.so
%{_libdir}/%{pkgdir}/libdatadeliveryservice.apd
%{_datadir}/%{pkgdir}/arc-datadelivery-service-start
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-datadelivery-service

%if %{with_ldap_service}
%files infosys-ldap
%{_unitdir}/arc-infosys-ldap.service
%{_unitdir}/arc-infosys-ldap-slapd.service
%{_datadir}/%{pkgdir}/create-bdii-config
%{_datadir}/%{pkgdir}/create-slapd-config
%{_datadir}/%{pkgdir}/ldap-schema
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-infosys-ldap
%endif

%files monitor
%{_datadir}/%{pkgdir}/monitor
%doc %{_mandir}/man7/monitor.7*

%files arcctl
%{_sbindir}/arcctl
%dir %{python3_sitearch}/%{pkgdir}/control
%{python3_sitearch}/%{pkgdir}/control/__init__.py
%{python3_sitearch}/%{pkgdir}/control/CertificateGenerator.py
%{python3_sitearch}/%{pkgdir}/control/ControlCommon.py
%{python3_sitearch}/%{pkgdir}/control/OSPackage.py
%{python3_sitearch}/%{pkgdir}/control/TestCA.py
%{python3_sitearch}/%{pkgdir}/control/TestJWT.py
%{python3_sitearch}/%{pkgdir}/control/ThirdPartyDeployment.py
%dir %{python3_sitearch}/%{pkgdir}/control/__pycache__
%{python3_sitearch}/%{pkgdir}/control/__pycache__/__init__.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/CertificateGenerator.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/ControlCommon.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/OSPackage.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/TestCA.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/TestJWT.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/ThirdPartyDeployment.*
%doc %{_mandir}/man1/arcctl.1*

%files arcctl-service
%{python3_sitearch}/%{pkgdir}/control/Cleanup.py
%{python3_sitearch}/%{pkgdir}/control/Config.py
%{python3_sitearch}/%{pkgdir}/control/ServiceCommon.py
%{python3_sitearch}/%{pkgdir}/control/Services.py
%{python3_sitearch}/%{pkgdir}/control/OSService.py
%{python3_sitearch}/%{pkgdir}/control/Validator.py
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Cleanup.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Config.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/ServiceCommon.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Services.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/OSService.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Validator.*

%files arex
%{_unitdir}/arc-arex.service
%{_unitdir}/arc-arex-ws.service
%{_libexecdir}/%{pkgdir}/arc-blahp-logger
%{_libexecdir}/%{pkgdir}/cache-clean
%{_libexecdir}/%{pkgdir}/cache-list
%{_libexecdir}/%{pkgdir}/gm-jobs
%{_libexecdir}/%{pkgdir}/gm-kick
%{_libexecdir}/%{pkgdir}/inputcheck
%{_libexecdir}/%{pkgdir}/jura-ng
%{_libexecdir}/%{pkgdir}/smtp-send
%{_libexecdir}/%{pkgdir}/smtp-send.sh
%{_libdir}/%{pkgdir}/libarex.so
%{_libdir}/%{pkgdir}/libarex.apd
%{_libdir}/%{pkgdir}/libcandypond.so
%{_libdir}/%{pkgdir}/libcandypond.apd
%{_datadir}/%{pkgdir}/cancel-condor-job
%{_datadir}/%{pkgdir}/cancel-fork-job
%{_datadir}/%{pkgdir}/cancel-SLURM-job
%{_datadir}/%{pkgdir}/scan-condor-job
%{_datadir}/%{pkgdir}/scan-fork-job
%{_datadir}/%{pkgdir}/scan-SLURM-job
%{_datadir}/%{pkgdir}/submit-condor-job
%{_datadir}/%{pkgdir}/submit-fork-job
%{_datadir}/%{pkgdir}/submit-SLURM-job
%{_datadir}/%{pkgdir}/CEinfo.pl
%{_datadir}/%{pkgdir}/ARC0mod.pm
%{_datadir}/%{pkgdir}/Condor.pm
%{_datadir}/%{pkgdir}/Fork.pm
%{_datadir}/%{pkgdir}/FORKmod.pm
%{_datadir}/%{pkgdir}/SLURM.pm
%{_datadir}/%{pkgdir}/SLURMmod.pm
%{_datadir}/%{pkgdir}/XmlPrinter.pm
%{_datadir}/%{pkgdir}/InfosysHelper.pm
%{_datadir}/%{pkgdir}/LdifPrinter.pm
%{_datadir}/%{pkgdir}/GLUE2xmlPrinter.pm
%{_datadir}/%{pkgdir}/GLUE2ldifPrinter.pm
%{_datadir}/%{pkgdir}/NGldifPrinter.pm
%{_datadir}/%{pkgdir}/ARC0ClusterInfo.pm
%{_datadir}/%{pkgdir}/ARC1ClusterInfo.pm
%{_datadir}/%{pkgdir}/ConfigCentral.pm
%{_datadir}/%{pkgdir}/GMJobsInfo.pm
%{_datadir}/%{pkgdir}/HostInfo.pm
%{_datadir}/%{pkgdir}/RTEInfo.pm
%{_datadir}/%{pkgdir}/InfoChecker.pm
%{_datadir}/%{pkgdir}/IniParser.pm
%{_datadir}/%{pkgdir}/LRMSInfo.pm
%{_datadir}/%{pkgdir}/Sysinfo.pm
%{_datadir}/%{pkgdir}/LogUtils.pm
%{_datadir}/%{pkgdir}/condor_env.pm
%{_datadir}/%{pkgdir}/cancel_common.sh
%{_datadir}/%{pkgdir}/configure-*-env.sh
%{_datadir}/%{pkgdir}/submit_common.sh
%{_datadir}/%{pkgdir}/scan_common.sh
%{_datadir}/%{pkgdir}/lrms_common.sh
%{_datadir}/%{pkgdir}/perferator
%{_datadir}/%{pkgdir}/PerfData.pl
%{_datadir}/%{pkgdir}/arc-arex-start
%{_datadir}/%{pkgdir}/arc-arex-ws-start
%dir %{_datadir}/%{pkgdir}/sql-schema
%{_datadir}/%{pkgdir}/sql-schema/arex_accounting_db_schema_v2.sql
%doc %{_mandir}/man1/cache-clean.1*
%doc %{_mandir}/man1/cache-list.1*
%doc %{_mandir}/man8/a-rex-backtrace-collect.8*
%doc %{_mandir}/man8/arc-blahp-logger.8*
%doc %{_mandir}/man8/gm-jobs.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-arex
%dir %{_localstatedir}/log/arc
%dir %{_localstatedir}/spool/arc
%dir %{_localstatedir}/spool/arc/ssm
%dir %{_localstatedir}/spool/arc/urs
%{python3_sitearch}/%{pkgdir}/control/AccountingDB.py
%{python3_sitearch}/%{pkgdir}/control/AccountingPublishing.py
%{python3_sitearch}/%{pkgdir}/control/Accounting.py
%{python3_sitearch}/%{pkgdir}/control/Cache.py
%{python3_sitearch}/%{pkgdir}/control/DataStaging.py
%{python3_sitearch}/%{pkgdir}/control/Jobs.py
%{python3_sitearch}/%{pkgdir}/control/RunTimeEnvironment.py
%{python3_sitearch}/%{pkgdir}/control/__pycache__/AccountingDB.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/AccountingPublishing.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Accounting.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Cache.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/DataStaging.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/Jobs.*
%{python3_sitearch}/%{pkgdir}/control/__pycache__/RunTimeEnvironment.*
%{_libexecdir}/%{pkgdir}/arccandypond
%dir %{_datadir}/%{pkgdir}/rte
%dir %{_datadir}/%{pkgdir}/rte/ENV
%{_datadir}/%{pkgdir}/rte/ENV/LRMS-SCRATCH
%{_datadir}/%{pkgdir}/rte/ENV/PROXY
%{_datadir}/%{pkgdir}/rte/ENV/RTE
%{_datadir}/%{pkgdir}/rte/ENV/CANDYPOND
%{_datadir}/%{pkgdir}/rte/ENV/SINGULARITY
%dir %{_datadir}/%{pkgdir}/rte/ENV/CONDOR
%{_datadir}/%{pkgdir}/rte/ENV/CONDOR/DOCKER
%{_sbindir}/a-rex-backtrace-collect
%config(noreplace) %{_sysconfdir}/arc.conf
%dir %{_sysconfdir}/arc.conf.d

%files arex-lrms-contrib
%{_datadir}/%{pkgdir}/cancel-boinc-job
%{_datadir}/%{pkgdir}/cancel-ll-job
%{_datadir}/%{pkgdir}/cancel-lsf-job
%{_datadir}/%{pkgdir}/cancel-pbs-job
%{_datadir}/%{pkgdir}/cancel-pbspro-job
%{_datadir}/%{pkgdir}/cancel-sge-job
%{_datadir}/%{pkgdir}/scan-boinc-job
%{_datadir}/%{pkgdir}/scan-ll-job
%{_datadir}/%{pkgdir}/scan-lsf-job
%{_datadir}/%{pkgdir}/scan-pbs-job
%{_datadir}/%{pkgdir}/scan-pbspro-job
%{_datadir}/%{pkgdir}/scan-sge-job
%{_datadir}/%{pkgdir}/submit-boinc-job
%{_datadir}/%{pkgdir}/submit-ll-job
%{_datadir}/%{pkgdir}/submit-lsf-job
%{_datadir}/%{pkgdir}/submit-pbs-job
%{_datadir}/%{pkgdir}/submit-pbspro-job
%{_datadir}/%{pkgdir}/submit-sge-job
%{_datadir}/%{pkgdir}/Boinc.pm
%{_datadir}/%{pkgdir}/LL.pm
%{_datadir}/%{pkgdir}/LSF.pm
%{_datadir}/%{pkgdir}/PBS.pm
%{_datadir}/%{pkgdir}/PBSPRO.pm
%{_datadir}/%{pkgdir}/SGE.pm
%{_datadir}/%{pkgdir}/SGEmod.pm

%files community-rtes
%{_datadir}/%{pkgdir}/community_rtes.sh
%{python3_sitearch}/%{pkgdir}/control/CommunityRTE.py
%{python3_sitearch}/%{pkgdir}/control/__pycache__/CommunityRTE.*

%files plugins-needed
%dir %{_libdir}/%{pkgdir}/test
%{_libdir}/%{pkgdir}/test/libaccTEST.so
%{_libdir}/%{pkgdir}/test/libaccTEST.apd
%if %{with_ldns}
%{_libdir}/%{pkgdir}/libaccARCHERY.so
%endif
%{_libdir}/%{pkgdir}/libaccARCREST.so
%{_libdir}/%{pkgdir}/libaccBroker.so
%{_libdir}/%{pkgdir}/libaccJobDescriptionParser.so
%{_libdir}/%{pkgdir}/libarcshc.so
%{_libdir}/%{pkgdir}/libarcshclegacy.so
%{_libdir}/%{pkgdir}/libarcshcotokens.so
%{_libdir}/%{pkgdir}/libdmcfile.so
%{_libdir}/%{pkgdir}/libdmchttp.so
%{_libdir}/%{pkgdir}/libdmcsrm.so
%{_libdir}/%{pkgdir}/libdmcrucio.so
%{_libdir}/%{pkgdir}/libidentitymap.so
%{_libdir}/%{pkgdir}/libmcchttp.so
%{_libdir}/%{pkgdir}/libmccmsgvalidator.so
%{_libdir}/%{pkgdir}/libmccsoap.so
%{_libdir}/%{pkgdir}/libmcctcp.so
%{_libdir}/%{pkgdir}/libmcctls.so
%if %{with_ldns}
%{_libdir}/%{pkgdir}/libaccARCHERY.apd
%endif
%{_libdir}/%{pkgdir}/libaccARCREST.apd
%{_libdir}/%{pkgdir}/libaccBroker.apd
%{_libdir}/%{pkgdir}/libaccJobDescriptionParser.apd
%{_libdir}/%{pkgdir}/libarcshc.apd
%{_libdir}/%{pkgdir}/libarcshclegacy.apd
%{_libdir}/%{pkgdir}/libarcshcotokens.apd
%{_libdir}/%{pkgdir}/libdmcfile.apd
%{_libdir}/%{pkgdir}/libdmchttp.apd
%{_libdir}/%{pkgdir}/libdmcsrm.apd
%{_libdir}/%{pkgdir}/libdmcrucio.apd
%{_libdir}/%{pkgdir}/libidentitymap.apd
%{_libdir}/%{pkgdir}/libmcchttp.apd
%{_libdir}/%{pkgdir}/libmccmsgvalidator.apd
%{_libdir}/%{pkgdir}/libmccsoap.apd
%{_libdir}/%{pkgdir}/libmcctcp.apd
%{_libdir}/%{pkgdir}/libmcctls.apd

%files plugins-globus

%files plugins-globus-common
%{_libdir}/libarcglobusutils.so.*

%files plugins-gridftp
%{_libdir}/%{pkgdir}/arc-dmcgridftp
%{_libdir}/%{pkgdir}/libdmcgridftpdeleg.so
%{_libdir}/%{pkgdir}/libdmcgridftpdeleg.apd

%files plugins-lcas-lcmaps
%{_libexecdir}/%{pkgdir}/arc-lcas
%{_libexecdir}/%{pkgdir}/arc-lcmaps

%if %{with_xrootd}
%files plugins-xrootd
%dir %{_libdir}/%{pkgdir}/external
%{_libdir}/%{pkgdir}/external/libdmcxrootd.so
%{_libdir}/%{pkgdir}/external/libdmcxrootd.apd
%{_libdir}/%{pkgdir}/libdmcxrootddeleg.so
%{_libdir}/%{pkgdir}/libdmcxrootddeleg.apd
%endif

%if %{with_gfal}
%files plugins-gfal
%dir %{_libdir}/%{pkgdir}/external
%{_libdir}/%{pkgdir}/external/libdmcgfal.so
%{_libdir}/%{pkgdir}/external/libdmcgfal.apd
%{_libdir}/%{pkgdir}/libdmcgfaldeleg.so
%{_libdir}/%{pkgdir}/libdmcgfaldeleg.apd
%endif

%if %{with_s3}
%files plugins-s3
%{_libdir}/%{pkgdir}/libdmcs3.so
%{_libdir}/%{pkgdir}/libdmcs3.apd
%endif

%files plugins-internal
%{_libdir}/%{pkgdir}/libaccINTERNAL.so
%{_libdir}/%{pkgdir}/libaccINTERNAL.apd

%files plugins-python
%doc docdir/python/*
%{_libdir}/%{pkgdir}/libaccPythonBroker.so
%{_libdir}/%{pkgdir}/libaccPythonBroker.apd
%{_libdir}/%{pkgdir}/libpythonservice.so
%{_libdir}/%{pkgdir}/libpythonservice.apd

%files devel
%doc docdir/devel/* src/hed/shc/arcpdp/*.xsd
%{_includedir}/%{pkgdir}
%{_libdir}/lib*.so
%{_bindir}/wsdl2hed
%doc %{_mandir}/man1/wsdl2hed.1*
%{_bindir}/arcplugin
%doc %{_mandir}/man1/arcplugin.1*

%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/_arc.*so
%{python3_sitearch}/%{pkgdir}/[^_p]*.py
%{python3_sitearch}/%{pkgdir}/__pycache__/[^_p]*.*

%files test-utils
%{_bindir}/arcperftest
%doc %{_mandir}/man1/arcperftest.1*

%files archery-manage
%{_sbindir}/archery-manage

%files wn
%attr(4755,root,root) %{_bindir}/arc-job-cgroup

%files -n python%{python3_pkgversion}-arcrest
%{python3_sitelib}/pyarcrest
%{python3_sitelib}/pyarcrest-*.*-info
%{_bindir}/arcrest

%files arc-exporter
%{_sbindir}/arc-exporter

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 11 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.0.0-4
- Disable pylint
- Fix a python argument parsing issue in arcctl

* Wed Apr 30 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.0.0-3
- Update the VOMS attribute certificate signing hash algorithm
- Re-enable the VOMSUtilTest on Fedora 43 (after above fix)
- Fix unowned directory /etc/arc.conf.d

* Wed Apr 16 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.0.0-2
- Drop the GFAL plugin for Fedora 43+ and EPEL 10+
- Drop old obsoletes

* Tue Apr 01 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.0.0-1
- Update to version 7.0.0
- Disable the VOMSUtilTest on Fedora 43 (OpenSSL 3.5)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.21.1-1
- Update to version 6.21.1

* Mon Dec 09 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.21.0-2
- Add BuildRequires python3-setuptools

* Sun Nov 10 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.21.0-1
- Update to version 6.21.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 08 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.20.1-1
- Update to version 6.20.1

* Wed Jul 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.20.0-1
- Update to version 6.20.0
- Drop EPEL 7 support from spec file (EOL)

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 6.19.0-2
- Rebuilt for Python 3.13

* Fri Apr 12 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.19.0-1
- Update to version 6.19.0
- Drop patches accepted upstream

* Mon Feb 19 2024 Jitka Plesnikova <jplesnik@redhat.com> - 6.18.0-6
- Fix compilation with SWIG 4.2

* Wed Feb 07 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.0-5
- Disable test incompatible with SWIG 4.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.0-2
- Fix compilation with libxml2 2.12

* Wed Oct 25 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.0-1
- Update to version 6.18.0
- Run autoreconf during build (following upstream)
- Drop xmlsec related patches accepted upstream

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.17.0-5
- Update py-compile script for Python 3.12

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 6.17.0-4
- Rebuilt for Python 3.12

* Thu May  4 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.17.0-3
- Adapt to xmlsec1 1.3.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.17.0-1
- Update to version 6.17.0
- Drop swig 4.1 patch accepted upstream

* Thu Oct 27 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.1-2
- Support SWIG 4.1
- Patch by Jitka Plesnikova <jplesnik@redhat.com> from RHBZ 2128189

* Fri Sep 09 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.1-1
- Update to version 6.16.1

* Sat Sep 03 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.0-1
- Update to version 6.16.0
- Drop patch adding missing include accepted upstream
- Build gfal2 plugin for EPEL 9 (dependency now available)
- Enable xmlsec for EPEL 9 (ARC now avoids SHA1 and tests succeed)
- Enable pylint for EPEL 9 (dependency now available)
- Enable pylint for Fedora 37+ (pylint now python 3.11 compatible)

* Sun Aug 21 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.1-8
- Add BR systemd (no longer a dependency of systemd-devel)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.1-6
- Disable acix for Fedora 35 (new python twisted not supported)

* Sun Jul 03 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.1-5
- Disable acix for Fedora 36 (new python twisted not supported)

* Thu Jun 30 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.1-4
- Add missing include

* Fri Jun 24 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.1-3
- Disable acix for Fedora 37 (new python twisted not supported)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 6.15.1-2
- Rebuilt for Python 3.11
- Disable pylint for Fedora 37 (it is broken)

* Mon Apr 04 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.1-1
- Update to version 6.15.1

* Thu Mar 17 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.15.0-1
- Update to version 6.15.0
- First build for EPEL 9 - Some components disabled
  * Due to missing dependencies: acix, gfal, python LRMS and pylint
  * Due to failures from using SHA1 hashes: xmlsec

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.0-1
- Update to version 6.14.0
- Drop patch nordugrid-arc-openssl3.patch (accepted upstream)

* Wed Sep 15 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.13.0-1
- Update to version 6.13.0
- Fix compilation with OpenSSL 3.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 6.12.0-4
- Rebuilt with OpenSSL 3.0.0

* Sat Aug 28 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.12.0-3
- Enable Python LRMS for EPEL 8 (perl-Inline-Python now available)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.12.0-1
- Update to version 6.12.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.11.0-2
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Paul Wouters <paul.wouters@aiven.io> - 6.11.0-1.1
- rebuilt for ldns so bump

* Sat Apr 24 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.11.0-1
- Update to version 6.11.0

* Fri Mar 12 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.2-3
- Revert the hash change (at upstream's request)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.10.2-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 24 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.2-1
- Update to version 6.10.2

* Mon Feb 15 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.1-1
- Update to version 6.10.1

* Wed Feb 10 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.0-1
- Update to version 6.10.0
- Drop RHEL6 support from spec file (EOL)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 awilliam@redhat.com - 6.9.0-2
- Rebuild for libldns soname bump

* Fri Dec 04 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.9.0-1
- Update to version 6.9.0
- Don't force C++14. Code now compiles with C++17.

* Mon Oct 12 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.8.1-1
- Update to version 6.8.1

* Wed Oct 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.8.0-1
- Update to version 6.8.0

* Fri Aug 28 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.7.0-4
- xrootd 5 compatibility

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 6.7.0-2
- Always specify C++11 or C++14 rather than using the default
  (which will be C++17 in the near future and this code is not C++17
  ready).

* Fri Jul 03 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.7.0-1
- Update to version 6.7.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.6.0-2
- Rebuilt for Python 3.9

* Mon Apr 27 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.6.0-1
- Update to version 6.6.0
- Drop patch nordugrid-arc-openssl-1.1.1f.patch (previously backported)
- Split out package arcctl-service package from arcctl package
- Split out plugins-python from main ARC python module pacakage

* Thu Apr 16 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5.0-3
- Adapt to openssl 1.1.1f

* Tue Mar 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5.0-2
- Adapt to new perl rpm package split in rawhide
- perl(English) and perl(Sys::Hostname) now in separate packages

* Tue Feb 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5.0-1
- Update to version 6.5.0
- Put the arcctl tool in a separate nordugrid-arc-arcctl package
- Add nordugrid-arc-community-rtes package (tech preview)
- Split the nordugrid-arc-plugins-globus package into several packages
  - nordugrid-arc-plugins-globus-common
  - nordugrid-arc-plugins-gridftp
  - nordugrid-arc-plugins-lcas-lcmaps
  - nordugrid-arc-plugins-gridftpjob

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.4.1-1
- Update to version 6.4.1

* Mon Nov 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.4.0-1
- Update to version 6.4.0

* Thu Oct 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-1
- Update to version 6.3.0
- Build infosys-ldap package for Fedora 32+ and EPEL 8+ again
  (bdii was ported to Python 3)
- Build gfal2 plugin for EPEL 8 (dependency now available)

* Sat Aug 31 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.0-1
- Update to version 6.2.0
- Drop Python 2 bindings for Fedora 32+ and EPEL 8+
- Drop infosys-ldap package for Fedora 32+ and EPEL 8+
  (requires bdii which is not ported to Python 3)
- Build for EPEL 8 (pylint, gfal2 and python-lrms disabled - missing deps)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1.0-1
- Update to version 6.1.0

* Mon Jun 03 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.0-1
- Update to ARC version 6

* Sat May 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.4-2
- Update for SWIG 4

* Sat Mar 16 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.4-1
- 5.4.4 Final Release
- Drop previously backported patches

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 5.4.3-2
- Rebuilt to change main python from 3.4 to 3.6

* Sun Feb 03 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.3-4
- Fix compilation with gcc 9 (Fedora 30+)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.3-2
- Fix for changed default initialization options in OpenSSL 1.1.1

* Sun Nov 11 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.3-1
- 5.4.3 Final Release
- Drop previously backported patches

* Fri Aug 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-9
- Various bugfixes from upstream
  - Respect s3 port number (nordugrid bugz 3701)
  - Adding support for RTE arguments in xRSL (nordugrid bugz 3705)
  - Small fix for Perl warnings (nordugrid bugz 3704, GGUS #132829)
  - Add empty Default-Start LSB keyword to avoid warnings
  - Fix shebangs to request python2
  - Use consistent 'unused' python shebangs
  - Handle twisted API change in v18.4 (nordugrid bugz 3733)
  - Run sub-process with the same python executable as main process
  - Relax FQDN demands in condor history file (GGUS #134645)
  - Fix -h processing in options parser (nordugrid bugz 3725)

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-8
- Explicitly request --with-python=python2
- Fix pylint error with new pylint

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.4.2-6
- Rebuilt for Python 3.7

* Thu May 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-5
- Create python34-nordugrid-arc package on EPEL 7
- Add BuildRequires on gcc-c++
- Use pylint in EPEL 7 (it's back)
- Adjust python dependencies for old releases

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.4.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-2
- Fix out-of-bounds errors causing test failures

* Thu Dec 14 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-1
- 5.4.2 Final Release

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.4.1-2
- Remove old crufty coreutils requires

* Fri Oct 13 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.1-1
- 5.4.1 Final Release

* Mon Sep 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.0-1
- 5.4.0 Final Release
- Drop patches nordugrid-arc-32769.patch and nordugrid-arc-32782-32784.patch
  (previously backported)

* Tue Aug 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.2-7
- Use pythonX-nordugrid-arc instead of pythonX-arc for the python package
  names to avoid a naming conflict with the python-arc package

* Thu Aug 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.2-6
- Rename python packages

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.2-3
- Fix some compiler warnings (backport from svn)
- Fix processes hanging on exit (backport from svn)

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 5.3.2-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Jul 06 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.2-1
- 5.3.2 Final Release

* Wed May 31 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.1-1
- 5.3.1 Final Release

* Fri Apr 07 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.0-1
- 5.3.0 Final Release
- Drop patch nordugrid-arc-s3.patch (previously backported)
- EPEL 5 End-Of-Life specfile clean-up

* Fri Mar 24 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.0-0.5.rc1
- Change stomppy Requires to python2-stomppy (Fedora 26+)

* Wed Feb 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.2-2
- Don't use pylint for EPEL builds (retired)

* Tue Feb 21 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.0-0.4.rc1
- Port to libs3 version 4 (backport from upstream svn)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 07 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.2-1
- 5.2.2 Final Release

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-0.2.rc1
- Rebuild for Python 3.6

* Thu Dec 15 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.1-1
- 5.2.1 Final Release

* Sat Nov 19 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.0-0.1.rc1
- 5.3.0 Release Candidate 1
- Supports openssl 1.1.0
- Drop canl-c++ support and the nordugrid-arc-arcproxyalt package for
  Fedora >= 26 - canl-c++ not ported to openssl 1.1.0

* Wed Oct 26 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.0-1
- 5.2.0 Final Release

* Tue Aug 30 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.1.3-1
- 5.1.3 Final Release
- Convert to systemd (Fedora 25+)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 06 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.1.2-1
- 5.1.2 Final Release
- Drop patch nordugrid-arc-5.1.1-Fix-to-work-swig-3010.patch (applied upstream)

* Mon Jun 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.1.1-2
- Fix Python code to work with SWIG 3.0.10 (bz #1346169)

* Wed May 25 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.1-1
- 5.1.1 Final Release

* Fri May 20 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.0-1
- 5.1.0 Final Release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.5-1
- 5.0.5 Final Release

* Mon Nov 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.4-1
- 5.0.4 Final Release
- Drop patch nordugrid-arc-stdpair-c++11.patch
- Add workaround for old py-compile script

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 28 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.3-1
- 5.0.3 Final Release
- Add workaround for too new libsigc++/glibmm in Fedora 23+ (-std=c++11)

* Sat Jul 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.2-2
- Adapt to new policycore packaging (Fedora 23+)

* Tue Jun 30 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.2-1
- 5.0.2 Final Release
- Drop patch nordugrid-arc-unbalanced-quotes.patch

* Fri Jun 26 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.1-2
- Fix unbalanced quotes in scan-SLURM-job

* Fri Jun 26 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.1-1
- 5.0.1 Final Release
- Drop patch nordugrid-arc-pytest.patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.0.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 29 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.0-2
- Fix python build conditionals

* Sat Mar 28 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.0-1
- 5.0.0 Final Release
- Drop patches nordugrid-arc-init.patch, -sedfix.patch and -python-print.patch

* Sat Mar 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.2.0-5
- Backport removal of python print statements (fixes pylint errors)

* Mon Dec 22 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.2.0-4
- Backport fix for broken sed statement in configure.ac

* Sat Aug 23 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.2.0-3
- Enable xmlsec1 support for EPEL 7

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 4.2.0-2
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.2.0-1
- 4.2.0 Final Release
- Drop patch nordugrid-arc-twisted.patch
- Build for EPEL 7 (without xmlsec)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.1.0-4
- Rebuilt for xrootd 4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 01 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.1.0-1
- 4.1.0 Final Release

* Thu Nov 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0.0-1
- 4.0.0 Final Release

* Mon Sep 23 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.3-4
- Rebuild for gridsite 2 update

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 3.0.3-2
- Add a missing requirement on crontabs to spec file

* Thu Jul 25 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.3-1
- 3.0.3 Final Release
- Drop patch accepted upstream nordugrid-arc-find-syntax.patch
- Add support for _pkgdocdir

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 3.0.2-2
- Perl 5.18 rebuild

* Thu Jun 13 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.2-1
- 3.0.2 Final Release

* Wed May 08 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.1-1
- 3.0.1 Final Release

* Tue Apr 16 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.0-2
- Fix python module build logic

* Mon Apr 15 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.0-1
- 3.0.0 Final Release
- Drop obsolete patches nordugrid-arc-swig-209.patch and
  nordugrid-arc-xrootd-private.patch

* Fri Mar 08 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.1-4
- Rebuild for xrootd 3.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.1-2
- Additional selinux contexts
- Fix for python wrappers using swig 2.0.9

* Fri Nov 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.1-1
- 2.0.1 Final Release
- Drop patches accepted upstream: nordugrid-arc-unistd.patch,
  nordugrid-arc-pypara.patch, nordugrid-arc-xmlns.patch,
  nordugrid-arc-recursive.patch

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 2.0.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.0-2
- Fix problem with directory hierarchies during job retrieval

* Wed May 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.0-1
- 2.0.0 Final Release
- Disable chelonia, hopi, isis and janitor

* Tue Mar 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.1-1
- 1.1.1 Bugfix Release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.0-2
- Backport fixes for endian independent md5 checksum

* Mon Oct 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.0-1
- 1.1.0 Final Release
- Drop patches accepted upstream: nordugrid-arc-perl-switch.patch and
  nordugrid-arc-run-full.patch

* Mon Oct 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-3.1
- rebuild (java), rel-eng#4932

* Sat Aug 27 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.1-3
- Move large files away from /var/run in order not to fill up /run partition
- Move arc-lcas and arc-lcmaps to plugins-globus package

* Sun Aug 07 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.1-2
- Remove perl switch statements

* Sun Jul 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.1-1.1
- Disable python module on RHEL6 ppc64

* Sat Jul 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.1-1
- 1.0.1 Final Release
- Remove Provides/Obsoletes for pre-Fedora packages

* Mon Jul 11 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.0-3
- Fix American English spelling

* Sun Jun 26 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.0-2
- Add missing include <stddef.h> for new gcc

* Mon Apr 18 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.0.0-1
- Initial release
