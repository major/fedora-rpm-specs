# TODO, maybe sometime:
# * Allow for nginx?
# * Consider using systemd's ReadWriteDirectories

#TODO: systemctl reload seems to be necessary after switching with Alternatives
#TODO: If the DB path for a Sqlite proxy is configured wrong, it requires systemctl restart. Start doesn't work.

%global srcname zabbix
%global with_selinux 1
%global selinuxtype targeted
# go is needed for agent2, but there are missing deps
%bcond_with go
# Missing dependencies for the java connector
%bcond_with java
#%%global prerelease rc2

Name:           zabbix
Epoch:          1
Version:        7.2.2
Release:        1%{?dist}
Summary:        Open-source monitoring solution for your IT infrastructure

# TODO - Note additional licenses in src/go when we start building with go
# src/libs/zbxembed/duktape.c: MIT License
# src/libs/zbxembed/duktape.h: MIT License
# src/libs/zbxgetopt/getopt.c: GNU General Public License v2.0 or later
# src/libs/zbxhash/md5.c: zlib License
# ui/vendor/composer/LICENSE: MIT License
# ui/js/vendors/D3/LICENSE: ISC License
# ui/js/vendors/Leaflet/LICENSE: BSD 2-Clause License
# ui/js/vendors/Leaflet.markercluster/LICENSE: MIT License
# ui/js/vendors/jQueryUI/LICENSE: MIT License
# ui/js/vendors/qrcode/LICENSE: MIT License
# ui/vendor/duosecurity/duo_universal_php/LICENSE: BSD 3-Clause License
# ui/vendor/firebase/php-jwt/LICENSE: BSD 3-Clause License
# ui/vendor/onelogin/php-saml/LICENSE: MIT License
# ui/vendor/paragonie/constant_time_encoding/LICENSE.txt: MIT License
# ui/vendor/pragmarx/google2fa/LICENSE.md: MIT License
# ui/vendor/symfony/deprecation-contracts/LICENSE: MIT License
# ui/vendor/symfony/polyfill-ctype/LICENSE: MIT License
# ui/vendor/symfony/yaml/LICENSE: MIT License
# ui/assets/styles/vendors/Leaflet/LICENSE: BSD 2-Clause License
# ui/vendor/paragonie/constant_time_encoding/src/*.php: MIT License
License:        AGPL-3.0-only AND MIT AND GPL-2.0-or-later AND Zlib AND BSD-3-Clause AND BSD-2-Clause AND ISC
URL:            https://www.zabbix.com
Source0:        https://cdn.zabbix.com/zabbix/sources/stable/7.2/zabbix-%{version}.tar.gz
Source1:        %{srcname}-web.conf
Source2:        %{srcname}-php-fpm.conf
Source5:        %{srcname}-logrotate.in
Source9:        %{srcname}-tmpfiles-zabbix.conf
# systemd units -- Alternatives switches between them (they state their dependencies)
# https://support.zabbix.com/browse/ZBXNEXT-1593
Source10:       %{srcname}-agent.service
Source11:       %{srcname}-proxy-mysql.service
Source12:       %{srcname}-proxy-pgsql.service
Source13:       %{srcname}-proxy-sqlite3.service
Source14:       %{srcname}-server-mysql.service
Source15:       %{srcname}-server-pgsql.service
Source16:       %{srcname}-fedora-epel.README
Source17:       %{srcname}-tmpfiles-zabbixsrv.conf
Source18:       %{srcname}.te
Source19:       %{srcname}.if
Source20:       %{srcname}.fc

# This is not a symlink, because we don't want the webserver to possibly ever serve it.
# local rules for config files
Patch0:         %{srcname}-config.patch
# Allow out-of-tree builds
# https://support.zabbix.com/browse/ZBXNEXT-6077
Patch1:         %{srcname}-out-of-tree.patch
# Enforce Fedora Crypto Policy
Patch2:         %{srcname}-crypto-policy.patch
# Add <stdio> to sscanf check
# https://support.zabbix.com/browse/ZBX-21946
Patch3:         %{srcname}-configure-sscanf.patch

# Patch1 patches automake files so we need to autoreconf
BuildRequires:   libtool
BuildRequires:   make
BuildRequires:   mariadb-connector-c-devel
BuildRequires:   libpq-devel
BuildRequires:   sqlite-devel
BuildRequires:   net-snmp-devel
BuildRequires:   openldap-devel
BuildRequires:   openssl-devel
BuildRequires:   gnutls-devel
BuildRequires:   unixODBC-devel
BuildRequires:   curl-devel
BuildRequires:   OpenIPMI-devel
BuildRequires:   libssh2-devel
BuildRequires:   libxml2-devel
BuildRequires:   libevent-devel
BuildRequires:   pcre2-devel
BuildRequires:   gcc
# For Agent 2 - has missing deps
%if %{with go}
BuildRequires:   gcc-go
#BuildRequires:   golang(github.com/alimy/mc/v2)
BuildRequires:   golang(github.com/docker/go-connections)
#BuildRequires:   golang(github.com/dustin/gomemcached)
BuildRequires:   golang(github.com/fsnotify/fsnotify)
BuildRequires:   golang(github.com/go-ldap/ldap)
#BuildRequires:   golang(github.com/go-ole/go-ole)
BuildRequires:   golang(github.com/go-sql-driver/mysql)
BuildRequires:   golang(github.com/godbus/dbus)
#BuildRequires:   golang(github.com/jackc/pgx/v4)
BuildRequires:   golang(github.com/mattn/go-sqlite3)
#BuildRequires:   golang(github.com/mediocregopher/radix/v3)
#BuildRequires:   golang(github.com/natefinch/npipe)
#BuildRequires:   golang(github.com/testcontainers/testcontainers-go)
#BuildRequires:   golang(golang.org/x/sys)
%endif
BuildRequires:   systemd
# Needed to determine path to link to
BuildRequires:   dejavu-sans-fonts

Requires:        logrotate

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:        (%{srcname}-selinux if selinux-policy-%{selinuxtype})
%endif

Provides:        bundled(md5-deutsch)
# Could alternatively be conditional on Fedora/EL
%if "x%{?srcname}" != "x%{name}"
Provides:        %{srcname} = %{version}-%{release}
Conflicts:       %{srcname} < 6.0
%endif

%description
Zabbix is software that monitors numerous parameters of a network and the
health and integrity of servers. Zabbix uses a flexible notification mechanism
that allows users to configure e-mail based alerts for virtually any event.
This allows a fast reaction to server problems. Zabbix offers excellent
reporting and data visualization features based on the stored data.
This makes Zabbix ideal for capacity planning.

Zabbix supports both polling and trapping. All Zabbix reports and statistics,
as well as configuration parameters are accessed through a web-based front end.
A web-based front end ensures that the status of your network and the health of
your servers can be assessed from any location. Properly configured, Zabbix can
play an important role in monitoring IT infrastructure. This is equally true
for small organizations with a few servers and for large companies with a
multitude of servers.

%package dbfiles-mysql
Summary:             Zabbix database schemas, images, data and patches
BuildArch:           noarch

%description dbfiles-mysql
Zabbix database schemas, images, data and patches necessary for creating
and/or updating MySQL databases

%package dbfiles-pgsql
Summary:             Zabbix database schemas, images, data and patches
BuildArch:           noarch

%description dbfiles-pgsql
Zabbix database schemas, images, data and patches necessary for creating
and/or updating PostgreSQL databases

%package dbfiles-sqlite3
Summary:             Zabbix database schemas and patches
BuildArch:           noarch

%description dbfiles-sqlite3
Zabbix database schemas and patches necessary for creating
and/or updating SQLite databases

%package server
Summary:             Zabbix server common files
BuildArch:           noarch
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            fping
Requires:            traceroute
Requires(pre):       shadow-utils
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd

%description server
Zabbix server common files

%package server-mysql
Summary:             Zabbix server compiled to use MySQL
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-mysql
Requires:            %{name}-server = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
Provides:            %{name}-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description server-mysql
Zabbix server compiled to use MySQL

%package server-pgsql
Summary:             Zabbix server compiled to use PostgreSQL
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-server = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-pgsql
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
Provides:            %{name}-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description server-pgsql
Zabbix server compiled to use PostgreSQL

%package agent
Summary:             Zabbix agent
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(pre):       shadow-utils
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd

%description agent
Zabbix agent, to be installed on monitored systems

%package proxy
Summary:             Zabbix proxy common files
BuildArch:           noarch
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(pre):       shadow-utils
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd
Requires:            fping

%description proxy
Zabbix proxy commmon files

%package proxy-mysql
Summary:             Zabbix proxy compiled to use MySQL
Requires:            %{name}-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-mysql
Provides:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives

%description proxy-mysql
Zabbix proxy compiled to use MySQL

%package proxy-pgsql
Summary:             Zabbix proxy compiled to use PostgreSQL
Requires:            %{name}-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-pgsql
Provides:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives

%description proxy-pgsql
Zabbix proxy compiled to use PostgreSQL

%package proxy-sqlite3
Summary:             Zabbix proxy compiled to use SQLite
Requires:            %{name}-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-sqlite3
Provides:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives

%description proxy-sqlite3
Zabbix proxy compiled to use SQLite

%package web
Summary:         Zabbix Web Frontend
BuildArch:       noarch
Requires:        php-bcmath
Requires:        php-fpm
Requires:        php-gd
Requires:        php-gettext
Requires:        php-json
Requires:        php-ldap
Requires:        php-mbstring
Requires:        php-xml
# jquery 3.6.0 and jquery-ui 1.13.2 in the sources
Requires:        js-jquery >= 3.6.0
Provides:        bundled(js-jquery-ui) = 1.13.2
# prototype 1.6.1 in the sources, Fedora package is dead
#Requires:        prototype
Requires:        dejavu-sans-fonts
Requires:        %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:        %{name}-web-database = %{?epoch:%{epoch}:}%{version}-%{release}

%description web
The php frontend to display the Zabbix web interface.

%package web-mysql
Summary:         Zabbix web frontend for MySQL
BuildArch:       noarch
Requires:        %{name}-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:        php-mysqli
Provides:        %{name}-web-database = %{?epoch:%{epoch}:}%{version}-%{release}

%description web-mysql
Zabbix web frontend for MySQL

%package web-pgsql
Summary:         Zabbix web frontend for PostgreSQL
BuildArch:       noarch
Requires:        %{name}-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:        php-pgsql
Provides:        %{name}-web-database = %{?epoch:%{epoch}:}%{version}-%{release}

%description web-pgsql
Zabbix web frontend for PostgreSQL

%if %{with java}
%package -n java-%{srcname}
Summary:         Zabbix Java connector
BuildArch:       noarch
BuildRequires:   java-devel
BuildRequires:   osgi(org.junit)
BuildRequires:   osgi(slf4j.api)
BuildRequires:   osgi(logback)

%description -n java-%{srcname}
Zabbix Java connector.
%endif

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             Zabbix SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module
%endif


%prep
%autosetup -p1
autoreconf

# Remove bundled java libs
find -name \*.jar -delete

# Remove prebuilt Windows binaries
rm -rf bin

# Override creation of statically named directory for alertscripts and externalscripts
# https://support.zabbix.com/browse/ZBX-6159
sed -i '/CURL_SSL_.*_LOCATION\|SCRIPTS_PATH/s|\${datadir}/zabbix|/var/lib/zabbixsrv|' \
    configure

# Kill off .htaccess files, options set in SOURCE1
find -name .htaccess -delete

# Fix path to traceroute utility (on all Linux targets)
find database -name 'data.sql' -exec sed -i 's|/usr/bin/traceroute|/bin/traceroute|' {} \;

# Common
# Settings with hard-coded defaults that are not suitable for Fedora
# are explicitly set, leaving the comment with the default value in place.
# Settings without hard-coded defaults are simply replaced -- be they
# comments or explicit settings!

# Also replace the datadir placeholder that is not expanded, but effective
sed -i \
    -e '\|^# LogFileSize=.*|a LogFileSize=0' \
    -e 's|^DBUser=root|DBUser=zabbix|' \
    -e 's|^# DBSocket=.*|DBSocket=%{_sharedstatedir}/mysql/mysql.sock|' \
    -e '\|^# ExternalScripts=|a ExternalScripts=%{_sharedstatedir}/zabbixsrv/externalscripts' \
    -e '\|^# AlertScriptsPath=|a AlertScriptsPath=%{_sharedstatedir}/zabbixsrv/alertscripts' \
    -e '\|^# TmpDir=\/tmp|a TmpDir=%{_sharedstatedir}/zabbixsrv/tmp' \
    -e 's|/usr/local||' \
    -e 's|\${datadir}|/usr/share|' \
    conf/zabbix_agentd.conf conf/zabbix_proxy.conf conf/zabbix_server.conf

# Specific
sed -i \
    -e '\|^# PidFile=.*|a PidFile=%{_rundir}/zabbix/zabbix_agentd.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_agentd.log|' \
    conf/zabbix_agentd.conf

sed -i \
    -e '\|^# PidFile=.*|a PidFile=%{_rundir}/zabbixsrv/zabbix_proxy.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbixsrv/zabbix_proxy.log|' \
    conf/zabbix_proxy.conf

sed -i \
    -e '\|^# PidFile=.*|a PidFile=%{_rundir}/zabbixsrv/zabbix_server.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbixsrv/zabbix_server.log|' \
    conf/zabbix_server.conf

# Install README file
install -m 0644 -p %{SOURCE16} .


%build

common_flags="
    --enable-dependency-tracking
    --enable-proxy
    --enable-ipv6
    --with-net-snmp
    --with-ldap
    --with-libcurl
    --with-openipmi
    --with-unixodbc
    --with-ssh2
    --with-libxml2
    --with-libevent
    --with-libpcre2
    --with-openssl
"
# Setup out of tree builds
%global _configure ../configure

%if %{with java}
export CLASSPATH=$(build-classpath junit slf4j-api logback-core logback-classic android-json)
%endif

# Frontend doesn't work for SQLite, thus don't build server
mkdir -p build-frontend
cd build-frontend
%configure $common_flags --enable-agent --with-sqlite3 %{?with_go:--enable-agent2} %{?with_java:--enable-java}
%make_build
cd -

mkdir -p build-server-mysql
cd build-server-mysql
%configure $common_flags --with-mysql --enable-server
%make_build
cd -

mkdir -p build-server-postgresql
cd build-server-postgresql
%configure $common_flags --with-postgresql --enable-server
%make_build
cd -

%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
mkdir selinux
cp -p %{SOURCE18} selinux/
cp -p %{SOURCE19} selinux/
cp -p %{SOURCE20} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{srcname}.pp
bzip2 -9 %{srcname}.pp
%endif


%install
# Install binaries
%make_install -C build-frontend
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy{,_sqlite3}
%make_install -C build-server-mysql
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy{,_mysql}
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_server{,_mysql}
%make_install -C build-server-postgresql
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy{,_pgsql}
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_server{,_pgsql}

# Ghosted alternatives
touch $RPM_BUILD_ROOT%{_sbindir}/zabbix_{proxy,server}

# Home directory for the agent;
# The other home directory is created during installation
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/zabbix

# Log directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbix
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbixsrv

# systemd tmpfiles
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
install -m 0644 -p %{SOURCE9} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix.conf
install -m 0644 -p %{SOURCE17} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbixsrv.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}
install -d -m 0755 $RPM_BUILD_ROOT%{_rundir}/zabbix/
install -d -m 0755 $RPM_BUILD_ROOT%{_rundir}/zabbixsrv/

# Install the frontend after removing backup files from patching
find ui -name '*.orig' -delete
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{srcname}
cp -a ui/* $RPM_BUILD_ROOT%{_datadir}/%{srcname}/

# Prepare ghosted config file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{srcname}/web
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{srcname}/web/zabbix.conf.php

# Replace bundled font
[ -d %{_fontbasedir}/dejavu ] &&
  ln -sf ../../../fonts/dejavu/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/%{srcname}/assets/fonts/
[ -d %{_fontbasedir}/dejavu-sans-fonts ] &&
  ln -sf ../../../fonts/dejavu-sans-fonts/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/%{srcname}/assets/fonts/

# Replace JS libraries
# There is no jquery-ui package yet
ln -sf ../../../javascript/jquery/3/jquery.min.js $RPM_BUILD_ROOT%{_datadir}/%{srcname}/js/vendors/jquery.js
#ln -sf ../../../javascript/jquery-ui/1/jquery-ui.min.js $RPM_BUILD_ROOT%{_datadir}/%{srcname}/js/vendors/jquery-ui.js

# This file is used to switch the frontend to maintenance mode
mv $RPM_BUILD_ROOT%{_datadir}/%{srcname}/conf/maintenance.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/%{srcname}/web/maintenance.inc.php || :

# Drop Apache config file in place
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{srcname}.conf

# Drop php-fpm config file in place
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/%{srcname}.conf

# Install log rotation
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
sed -e 's|COMPONENT|agentd|g; s|USER|zabbix|g' %{SOURCE5} > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
sed -e 's|COMPONENT|server|g; s|USER|zabbixsrv|g' %{SOURCE5} > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
sed -e 's|COMPONENT|proxy|g; s|USER|zabbixsrv|g' %{SOURCE5} > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy

# Install different systemd units because of the requirements for DBMS daemons
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_unitdir}/zabbix-agent.service
install -m 0644 -p %{SOURCE11} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy-mysql.service
install -m 0644 -p %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy-pgsql.service
install -m 0644 -p %{SOURCE13} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy-sqlite3.service
install -m 0644 -p %{SOURCE14} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server-mysql.service
install -m 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server-pgsql.service

# Ghosted alternatives 
touch $RPM_BUILD_ROOT%{_unitdir}/zabbix-server.service
touch $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy.service

# Directory for fping spooling files 
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/zabbixsrv/tmp

# Install sql files
for db in postgresql mysql; do
    mkdir $RPM_BUILD_ROOT%{_datadir}/%{srcname}-$db
    cp -p database/$db/*.sql $RPM_BUILD_ROOT%{_datadir}/%{srcname}-$db
done

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{srcname}-sqlite3
cp -p database/sqlite3/schema.sql $RPM_BUILD_ROOT%{_datadir}/%{srcname}-sqlite3

%if 0%{?with_selinux}
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif


%post server
%systemd_post zabbix-server.service

if [ $1 -gt 1 ] ; then
  # Apply permissions also in *.rpmnew upgrades from old permissive ones
  chmod 0640 %{_sysconfdir}/zabbix_server.conf
  chown root:zabbixsrv %{_sysconfdir}/zabbix_server.conf
fi
:

%post server-mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_mysql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-mysql.service
# This needs to be run twice to rename from old slave name in zabbix < 6.0.33-2
# due to a bug in alternatives. Remove in F45
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_mysql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-mysql.service

%post server-pgsql
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_pgsql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-pgsql.service
# This needs to be run twice to rename from old slave name in zabbix < 6.0.33-2
# due to a bug in alternatives. Remove in F45
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_pgsql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-pgsql.service

%post proxy
%systemd_post zabbix-proxy.service

if [ $1 -gt 1 ] ; then
  # Apply permissions also in *.rpmnew upgrades from old permissive ones
  chmod 0640 %{_sysconfdir}/zabbix_proxy.conf
  chown root:zabbixsrv %{_sysconfdir}/zabbix_proxy.conf
fi
:

%post proxy-mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_mysql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-mysql.service
# This needs to be run twice to rename from old slave name in zabbix < 6.0.33-2
# due to a bug in alternatives. Remove in F45
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_mysql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-mysql.service

%post proxy-pgsql
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_pgsql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-pgsql.service
# This needs to be run twice to rename from old slave name in zabbix < 6.0.33-2
# due to a bug in alternatives. Remove in F45
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_pgsql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-pgsql.service

%post proxy-sqlite3
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_sqlite3 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-sqlite3.service
# This needs to be run twice to rename from old slave name in zabbix < 6.0.33-2
# due to a bug in alternatives. Remove in F45
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_sqlite3 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-sqlite3.service

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
%endif

%pre agent
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
    useradd -r -g zabbix -d %{_sharedstatedir}/zabbix -s /sbin/nologin \
    -c "Zabbix Monitoring System" zabbix
:

%post agent
%systemd_post zabbix-agent.service

%pre server
getent group zabbixsrv > /dev/null || groupadd -r zabbixsrv
# The zabbixsrv group is introduced by 2.2 packaging
# The zabbixsrv user was a member of the zabbix group in 2.0
if getent passwd zabbixsrv > /dev/null; then
    if [[ $(id -gn zabbixsrv) == "zabbix" ]]; then
        usermod -c "Zabbix Monitoring System -- Proxy or server" -g zabbixsrv zabbixsrv
    fi
else
    useradd -r -g zabbixsrv -d %{_sharedstatedir}/zabbixsrv -s /sbin/nologin \
    -c "Zabbix Monitoring System -- Proxy or server" zabbixsrv
fi
:

%preun server
  %systemd_preun zabbix-server.service

%pre proxy
getent group zabbixsrv > /dev/null || groupadd -r zabbixsrv
# The zabbixsrv group is introduced by 2.2 packaging
# The zabbixsrv user was a member of the zabbix group in 2.0
if getent passwd zabbixsrv > /dev/null; then
    if [[ $(id -gn zabbixsrv) == "zabbix" ]]; then
        usermod -c "Zabbix Monitoring System -- Proxy or server" -g zabbixsrv zabbixsrv
    fi
else
    useradd -r -g zabbixsrv -d %{_sharedstatedir}/zabbixsrv -s /sbin/nologin \
    -c "Zabbix Monitoring System -- Proxy or server" zabbixsrv
fi
:

%preun proxy
%systemd_preun zabbix-proxy.service

%preun agent
%systemd_preun zabbix-agent.service

%postun server
%systemd_postun_with_restart zabbix-server.service

%postun server-mysql
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-server %{_sbindir}/%{srcname}_server_mysql
fi

%postun server-pgsql
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-server %{_sbindir}/%{srcname}_server_pgsql
fi

%postun proxy
%systemd_postun_with_restart zabbix-proxy.service

%postun proxy-mysql
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_mysql
fi

%postun proxy-pgsql
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_pgsql
fi

%postun proxy-sqlite3
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_sqlite3
fi

%postun agent
%systemd_postun_with_restart zabbix-agent.service


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README zabbix-fedora-epel.README
%dir %{_sysconfdir}/%{srcname}
%config(noreplace) %{_sysconfdir}/zabbix_agentd.conf
%{_bindir}/zabbix_get
%{_bindir}/zabbix_js
%{_bindir}/zabbix_sender
%{_mandir}/man1/zabbix_get.1*
%{_mandir}/man1/zabbix_sender.1*

%files dbfiles-mysql
%license COPYING
%{_datadir}/%{srcname}-mysql/

%files dbfiles-pgsql
%license COPYING
%{_datadir}/%{srcname}-postgresql/

%files dbfiles-sqlite3
%license COPYING
%{_datadir}/%{srcname}-sqlite3/

%files server
%doc misc/snmptrap/zabbix_trap_receiver.pl
%attr(0755,zabbixsrv,zabbixsrv) %dir %{_rundir}/zabbixsrv/
%{_prefix}/lib/tmpfiles.d/zabbixsrv.conf
%attr(0640,root,zabbixsrv) %config(noreplace) %{_sysconfdir}/zabbix_server.conf
%attr(0775,root,zabbixsrv) %dir %{_localstatedir}/log/zabbixsrv
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%ghost %{_sbindir}/zabbix_server
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv/tmp
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv/alertscripts
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv/externalscripts
%ghost %{_unitdir}/zabbix-server.service
%{_mandir}/man8/zabbix_server.8*

%files server-mysql
%{_sbindir}/zabbix_server_mysql
%{_unitdir}/zabbix-server-mysql.service

%files server-pgsql
%{_sbindir}/zabbix_server_pgsql
%{_unitdir}/zabbix-server-pgsql.service

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

%files agent
%doc conf/zabbix_agentd/*.conf
%attr(0755,zabbix,zabbix) %dir %{_rundir}/zabbix/
%{_prefix}/lib/tmpfiles.d/zabbix.conf
%attr(0775,root,zabbix) %dir %{_localstatedir}/log/zabbix
%config(noreplace) %{_sysconfdir}/zabbix_agentd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%attr(750,zabbix,zabbix) %dir %{_sharedstatedir}/zabbix
%{_unitdir}/zabbix-agent.service
%{_sbindir}/zabbix_agentd
%{_mandir}/man8/zabbix_agentd.8*

%files proxy
%doc misc/snmptrap/zabbix_trap_receiver.pl
%attr(0755,zabbixsrv,zabbixsrv) %dir %{_rundir}/zabbixsrv/
%{_prefix}/lib/tmpfiles.d/zabbixsrv.conf
%attr(0640,root,zabbixsrv) %config(noreplace) %{_sysconfdir}/zabbix_proxy.conf
%attr(0775,root,zabbixsrv) %dir %{_localstatedir}/log/zabbixsrv
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%ghost %{_sbindir}/zabbix_proxy
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv/tmp
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv/alertscripts
%attr(0750,zabbixsrv,zabbixsrv) %dir %{_sharedstatedir}/zabbixsrv/externalscripts
%ghost %{_unitdir}/zabbix-proxy.service
%{_mandir}/man8/zabbix_proxy.8*

%files proxy-mysql
%{_sbindir}/zabbix_proxy_mysql
%{_unitdir}/zabbix-proxy-mysql.service

%files proxy-pgsql
%{_sbindir}/zabbix_proxy_pgsql
%{_unitdir}/zabbix-proxy-pgsql.service

%files proxy-sqlite3
%{_sbindir}/zabbix_proxy_sqlite3
%{_unitdir}/zabbix-proxy-sqlite3.service

%files web
%dir %attr(0750,apache,apache) %{_sysconfdir}/%{srcname}/web
%ghost %attr(0644,apache,apache) %config(noreplace) %{_sysconfdir}/%{srcname}/web/zabbix.conf.php
%attr(0644,apache,apache) %config(noreplace) %{_sysconfdir}/%{srcname}/web/maintenance.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/zabbix.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/zabbix.conf
%{_datadir}/%{srcname}/

%files web-mysql

%files web-pgsql

%changelog
* Mon Jan 06 2025 Orion Poplawski <orion@nwra.com> - 1:7.2.2-1
- Update to 7.2.2

* Thu Dec 12 2024 Orion Poplawski <orion@nwra.com> - 1:7.2.0-1
- Update to 7.2.0

* Sat Nov 30 2024 Orion Poplawski <orion@nwra.com> - 1:7.0.6-1
- Update to 7.0.6

* Tue Oct 22 2024 Orion Poplawski <orion@nwra.com> - 1:7.0.5-1
- Update to 7.0.5

* Mon Oct 07 2024 Orion Poplawski <orion@nwra.com> - 1:7.0.4-2
- Fix typo in crypto policy patch that broke SSL connections

* Thu Sep 26 2024 Orion Poplawski <orion@nwra.com> - 1:7.0.4-1
- Update to 7.0.4

* Sat Aug 24 2024 Orion Poplawski <orion@nwra.com> - 1:7.0.3-1
- Update to 7.0.3
- License changed upstream to AGPL-3.0-only, note other licenses in source

* Mon Aug 19 2024 Orion Poplawski <orion@nwra.com> - 1:6.0.33-2
- Use alternatives name that systemd likes for units (bz#2305855)

* Thu Aug 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.33-1
- 6.0.33

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1:6.0.30-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.30-1
- 6.0.30

* Fri May 03 2024 Orion Poplawski <orion@nwra.com> - 1:6.0.29-1
- Update to 6.0.29
- Hopefully really get the zabbix_run_sudo SELinux boolean working for
  zabbix-agent and allow it to run lvm when enabled

* Wed Feb 28 2024 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.27-1
- Update to 6.0.27

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Orion Poplawski <orion@nwra.com> - 1:6.0.25-1
- Update to 6.0.25

* Fri Dec 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.22-3
- Patch for libxml2 2.12.x

* Sat Oct 28 2023 Orion Poplawski <orion@nwra.com> - 1:6.0.22-2
- Add dontaudit SELinux rules for spurious AVC denial messages (bz#2170630)

* Wed Oct 04 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.22-1
- Update to 6.0.22

* Mon Aug 07 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.20-1
- Update to 6.0.20

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.19-1
- Update to 6.0.19

* Thu Jun 15 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.18-1
- Update to 6.0.18

* Tue Apr 25 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.17-1
- Update to 6.0.17

* Tue Apr 11 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.16-1
- Update to 6.0.16

* Tue Apr 04 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.15-1
- Update to 6.0.15

* Tue Mar 21 2023 Morten Stevens <mstevens@fedoraproject.org> - 1:6.0.14-1
- Update to 6.0.14

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.13-2
- migrated to SPDX license

* Thu Feb 16 2023 Orion Poplawski <orion@nwra.com> - 1:6.0.13-1
- Update to 6.0.13
- Add policy to allow zabbix scripts to run chronyc as chronyc_t (bz#2160180)
- Add policy to allow zabbix agent to run rpm read-only

* Sun Jan 22 2023 Orion Poplawski <orion@nwra.com> - 1:6.0.12-1
- Update to 6.0.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Florian Weimer <fweimer@redhat.com> - 1:6.0.8-2
- Include <stdio.h> in configure for sscanf prototype

* Wed Sep 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.8-1
- 6.0.8

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> -1:6.0.6-2
- Move to pcre2

* Fri Jul 08 2022 Orion Poplawski <orion@nwra.com> - 1:6.0.6-1
- Update to 6.0.6

* Tue May 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.5-1
- 6.0.5

* Mon May 09 2022 Orion Poplawski <orion@cora.nwra.com> - 1:6.0.4-1
- Update to 6.0.4

* Mon Apr 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.3-1
- 6.0.3

* Wed Mar 23 2022 Orion Poplawski <orion@nwra.com> - 1:6.0.2-1
- Update to 6.0.2

* Fri Mar 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:5.0.21-1
- 5.0.21

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:5.0.19-1
- 5.0.19
- Fixed CVE-2022-23132, CVE-2022-23133, CVE-2022-23134.

* Wed Dec 01 2021 Orion Poplawski <orion@nwra.com> - 1:5.0.18-1
- Update to 5.0.18

* Mon Nov 01 2021 Orion Poplawski <orion@cora.nwra.com> - 1:5.0.17-1
- Update to 5.0.17

* Sat Oct 16 2021 Morten Stevens <mstevens@fedoraproject.org> - 1:5.0.16-1
- Update to 5.0.16

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:5.0.14-2
- Rebuilt with OpenSSL 3.0.0

* Mon Jul 26 2021 Morten Stevens <mstevens@fedoraproject.org> - 1:5.0.14-1
- Update to 5.0.14

* Mon Jul 26 2021 Morten Stevens <mstevens@fedoraproject.org> - 1:5.0.10-3
- Dropped support for DES

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Orion Poplawski <orion@nwra.com> - 1:5.0.10-1
- Update to 5.0.10
- SELinux: Allow fping to read the zabbix ping list

* Fri Mar 05 2021 Orion Poplawski <orion@nwra.com> - 1:5.0.9-1
- Update to 5.0.9

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:5.0.8-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 15 2021 Orion Poplawski <orion@nwra.com> - 1:5.0.8-1
- Update to 5.0.8
- Update php configuration for php-fpm (bz#1928386)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1:5.0.7-4
- rebuild for libpq ABI fix rhbz#1908268

* Thu Jan 28 2021 Orion Poplawski <orion@nwra.com> - 1:5.0.7-3
- Handle new dejavu-sans-fonts directory (bz#1921010)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Orion Poplawski <orion@nwra.com> - 1:5.0.7-1
- Update to 5.0.7

* Sun Dec 13 2020 Orion Poplawski <orion@nwra.com> - 1:5.0.6-1
- Update to 5.0.6

* Tue Sep 15 2020 Volker Froehlich <volker27@gmx.at> - 1:5.0.3-2
- Rebuild for libevent soname bump

* Tue Sep  1 2020 Orion Poplawski <orion@nwra.com> - 1:5.0.3-1
- Update to 5.0.3

* Tue Sep  1 2020 Orion Poplawski <orion@nwra.com> - 1:5.0.2-1
- Update to 5.0.2
- Enforce Fedora crypto policy

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 1:4.0.22-3
- Rebuilt for new net-snmp release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Orion Poplawski <orion@nwra.com> - 1:4.0.22-1
- Update to 4.0.22 (bz#1858259) CVE-2020-15803
- Fix alert/external scripts directories

* Mon Apr 20 2020 Orion Poplawski <orion@nwra.com> - 1:4.0.19-3
- Fix chmod/chown in scriptlet

* Mon Apr 20 2020 Vit Mojzis <vmojzis@redhat.com> - 1:4.0.19-2
- Add SELinux subpackage

* Sun Apr 19 2020 Orion Poplawski <orion@nwra.com> - 1:4.0.19-1
- Update to 4.0.19
- Upstream now uses jquery 3, so link to that

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1:4.0.16-3
- Fix string quoting for rpm >= 4.16

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Volker Froehlich <volker27@gmx.at> - 1:4.0.16-1
- New upstream release

* Thu Nov 28 2019 Volker Froehlich <volker27@gmx.at> - 1:4.0.15-1
- New upstream release

* Thu Nov 14 2019 Volker Froehlich <volker27@gmx.at> - 1:4.0.14-1
- New upstream release

* Tue Oct 29 2019 Volker Froehlich <volker27@gmx.at> - 1:4.0.13-1
- New upstream release

* Sat Aug  3 2019 Volker Froehlich <volker27@gmx.at> - 1:4.0.11-1
- New upstream release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul  3 2019 Volker Froehlich <volker27@gmx.at> - 4.0.10-1
- New upstream release

* Fri Jun 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:4.0.9-1
- 4.0.9

* Thu May 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:4.0.7-3
- Correct Epoch in Requires.

* Thu May 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:4.0.7-2
- revert to 4.0.7 LTS

* Fri Apr 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 4.2.1-1
- 4.2.1

* Tue Apr 23 2019 Volker Froehlich <volker27@gmx.at> - 4.0.7-1
- New upstream release

* Sun Mar 31 2019 Volker Froehlich <volker27@gmx.at> - 4.0.6-1
- New upstream release

* Tue Feb 26 2019 Volker Froehlich <volker27@gmx.at> - 4.0.5-1
- New upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Volker Froehlich <volker27@gmx.at> - 3.0.24-1
- New upstream release

* Fri Sep 14 2018 Volker Froehlich <volker27@gmx.at> - 3.0.22-1
- New upstream release

* Tue Jul 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.0.16-4
- Rebuild for unannounced net-snmp suversion bump.
- Add build dependency on gcc.

* Tue Jul 24 2018 Volker Froehlich <volker27@gmx.at> - 3.0.16-3
- Build without iksemel (jabber) support -- package is retired

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Volker Froehlich <volker27@gmx.at> - 3.0.16-1
- New upstream release

* Tue Mar 20 2018 Volker Froehlich <volker27@gmx.at> - 3.0.15-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Volker Fröhlich <volker27@gmx.at> - 3.0.14-2
- Remove group keyword

* Thu Dec 28 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.14-1
- New upstream release
- Remove mariadb-connector patch

* Sat Nov 11 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.13-1
- New upstream release

* Wed Oct 18 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.12-1
- New upstream release

* Mon Sep 25 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.11-1
- New upstream release

* Fri Sep 22 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.10-4
- Replace mysql-devel with mariadb-connector-c-devel, resolves BZ #1493663

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.10-1
- New upstream release

* Thu Jul 13 2017 Adam Williamson <awilliam@redhat.com> - 3.0.9-2
- Fix build with MariaDB 10.2+

* Fri Jun 23 2017 Volker Fröhlich <volker27@gmx.at> - 3.0.9-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.7-1
- New upstream release

* Thu Dec 08 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.6-1
- New upstream release

* Wed Oct 05 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.5-1
- New upstream release

* Sat Jul 23 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.4-1
- New upstream release

* Mon Jul 11 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.3-2
- Fix php mysql requires

* Mon Jul 04 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.3-1
- New upstream release

* Mon May 09 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.2-1
- New upstream release
- Remove now-obsolete fping3 patch

* Tue Mar 29 2016 Volker Fröhlich <volker27@gmx.at> - 3.0.1-1
- Un-bundle jquery and prototype; remove the font patch and use a symlink instead
- Add PHP configuration to Apache config file (BZ#1074292)
- Fix the duplicate definition of a pidfile (BZ#1220392)
- Change logrotate mode to truncate

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Volker Fröhlich <volker27@gmx.at> - 2.4.7-1
- New release

* Mon Aug 10 2015 Volker Fröhlich <volker27@gmx.at> - 2.4.6-1
- New release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Volker Fröhlich <volker27@gmx.at> - 2.4.5-1
- New release

* Tue Feb 24 2015 Volker Fröhlich <volker27@gmx.at> - 2.4.4-1
- New release

* Sat Dec 20 2014 Volker Fröhlich <volker27@gmx.at> - 2.4.3-1
- New release

* Wed Oct  8 2014 Volker Fröhlich <volker27@gmx.at> - 2.4.1-1
- New release

* Thu Sep 11 2014 Volker Fröhlich <volker27@gmx.at> - 2.4.0-1
- New major version release

* Mon Sep  1 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.6-2
- Install tmpfiles configuration in the proper location per guidelines,
  thus solving the startup trouble due to missing directories
  (respectively BZ 1115251, 1081584, 982001, 1135696)
- Clean between builds, otherwise zabbix_{proxy,server} are compiled
  again on install; make server and proxy package noarch now
- Set the service type to forking in unit files (BZ 1132437),
  add PIDFile entry, remove RemainAfterExit, change /var/run to /run
- Correct path to traceroute in DB dumps again
- Leave database-specific datadir subdirectories to the dbfiles sub-packages
- Harmonize package descriptions and summaries

* Wed Aug 27 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.6-1
- New upstream release
- Use the upstream tarball, now that non-free json was replaced with android-json

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.5-1
- New upstream release

* Tue Jun 24 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.4-1
- New upstream release
- Remove obsolete patches

* Fri Jun 20 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.3-4
- Patch for ZBX-8151 (Local file inclusion via XXE attack) -- CVE-2014-3005

* Sun Jun  8 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.3-3
- Patch for ZBX-8238 (logrt may continue reading an old file repeatedly)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.3-1
- New upstream release

* Sun Feb 16 2014 Volker Fröhlich <volker27@gmx.at> - 2.2.2-1
- New major release
- Preserve timestamp on all install commands
- Provide bundled md5-deutsch
- Add noarch sub-packages for DB files
- Correct directory permissions
- Correct Conflicts directives
- Correct /var/lib/zabbixsrv owner and permissions
- Use dir directive for home directories and their sub-directories
- Update config patch
- Provide "zabbix"
- Add libxml2-devel as BR for VMware monitoring and --with-libxml2 flag
- Move user zabbixsrv to his own group
  - Split tmpfiles.d, thus solve BZ#982001 
  - Split lock, log and run locations
  - Adapt ownership and permissions
- Update README

* Sun Feb 16 2014 Volker Fröhlich <volker27@gmx.at> - 2.0.11-2
- Remove if clauses for Fedora/RHEL as they are obsolete in EL 7
- Use systemd scriplet macros (BZ#850378)
- Remove init scripts

* Wed Feb 12 2014 Volker Fröhlich <volker27@gmx.at> - 2.0.11-1
- New upstream release
- Truncate changelog

* Sun Dec 15 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.10-2
- The start function of the proxy init script had a typo causing failure
- Improved the section on running multiple instances in the README

* Fri Dec 13 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.10-1
- New upstream release
- Drop obsolete patch ZBX-7479
- Improve init scripts to not kill other instances (BZ#1018293)
- General overhaul of init scripts and documentation in README
- Harmonize scriptlet if-clause style

* Sun Nov  3 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.9-2
- Fix vulnerability for remote command execution injection
  (ZBX-7479, CVE-2013-6824)

* Wed Oct  9 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.9-1
- New upstream release
- Drop obsolete patches ZBX-6804, ZBX-7091, ZBX-6922, ZBX-6992

* Mon Sep 23 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.8-3
- Add SQL speed-up patch (ZBX-6804)
- Add SQL injection vulnerability patch (ZBX-7091, CVE-2013-5743)
- Add patch for failing XML host import (ZBX-6922)

* Fri Sep 13 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.8-2
- Add php-ldap as a requirement for the frontend
- Add patch for ZBX-6992

* Fri Aug 23 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.8-1
- New upstream release
- Create and configure a spooling directory for fping files outside of /tmp
- Update README to reflect that and add a SELinux section
- Drop PrivateTmp from systemd unit files
- Drop patch for ZBX-6526 (solved upstream)
- Drop patch for CVE-2012-6086 (solved upstream)
- Correct path for the flash applet when removing
- Truncate changelog

* Tue Jul 30 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.6-3
- Backport fix for CVE-2012-6086

* Tue May 07 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.6-2
- Add patch for ZBX-6526
- Solve permission problem with /var/run/zabbix in Fedora (BZ#904041)
- Remove origin of directories BZ#867159, comment 14 and 16

* Mon Apr 22 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.6-1
- New upstream release
- Drop ZBX-6290 and ZBX-6318 patches

* Tue Mar 19 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.5-3
- Include patch for ZBX-6318

* Tue Feb 12 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.5-2
- Include patch for ZBX-6290

* Tue Feb 12 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.5-1
- New upstream release
- Drop now-included patches
- Init file comments point to the actual configuration files now

* Sat Feb  9 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.4-5
- Dispensable version of COPYING is no more
- Correct path to traceroute in DB dumps again

* Tue Jan 22 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.4-4
- Remove zabbix_get plus manpage from the proxy files section
- Solve conflict for externalscripts symlink between proxy and
  server package

* Thu Jan 17 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.4-3
- Patch for CVE-2013-1364

* Mon Jan 14 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.4-2
- Apply patch for ZBX-6101
- Add su line to logrotate config file
- Do not own /var/run/zabbix on Fedora, systemd manages it
- Add forgotten chkconfig and service commands on agent preun script

* Sat Dec  8 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.4-1
- New upstream release

* Fri Dec  7 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-7
- Add SNMP source IP address patch

* Mon Nov 26 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-6
- Apply fping 3 patch only for Fedora

* Tue Nov 13 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-5
- Adapt httpd configuration file for Apache 2.4 (BZ#871498)

* Thu Nov  8 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-4
- Require php explicitly again
- Remove traces of /usr/local in configuration files
- Improve Fedora README file

* Sun Oct 14 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-3
- Correct capitalization in unit files, init scripts and package description
- Improve sysconfig sourcing in init scripts
- Correct post-script permissions and owner on rpmnew files
- Obsolete sqlite web and server sub-package

* Sun Oct 14 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-2
- Include agent configuration file in base package for zabbix_sender
- Stricter permissions for server config file
- Adapt DB patches to our file layout
- Remove conditional around Source9
- doc-sub-package obsolete only for Fedora, where the package keeps
  the name "zabbix"
- Add missing requirement for proxy scriplet
- Remove Requires php because the PHP modules serve this purpose
- Use systemd's PrivateTmp only for F17 and up
- Correct proxy and server pre-scriplet (usergroup)

* Fri Oct  5 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.3-1
- New upstream release
- Add Fedora specific README

* Mon Aug 27 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.2-3
- Eliminate Sqlite server and web sub-package
  They never worked and are considered experimental by upstream
- Harmonize conditionals
- Put maintenance configuration in web configuration directory
- Adapt man pages to file layout
- Remove backup files from frontend
- Move maintenance configuration file to /etc/...
- Move ExternalScripts and AlertScripts to daemon home directory
- Don't ship SQL scripts as documentation

* Sun Aug 26 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.2-2
- Use separate daemon users, so the agent can not parse the 
  database password
- Use PrivateTmp in unit files

* Wed Aug 15 2012 Volker Fröhlich <volker27@gmx.at> - 2.0.2-1
- New upstream release
- Unified specfile for sys-v-init scripts and systemd
- Switch to Alternatives system
- Source from systemconfig in init scripts

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Dan Horák <dan[at]danny.cz> - 2.0.1-1
- update to 2.0.1
- rebased patches
- upstream location (/etc) for config files is used with symlinks to the old /etc/zabbix
- dropped our own SNMP trap processor, upstream one running directly under net-snmp daemon is used instead
- moved zabbix_get and zabbix_sender tools to the main package
