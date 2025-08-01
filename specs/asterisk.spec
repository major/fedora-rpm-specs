#%%global _rc 1
#%%global _beta 3

%global           pjsip_version   2.12
%global           jansson_version 2.14

%global           optflags        %{optflags} -Werror-implicit-function-declaration -DLUA_COMPAT_MODULE -fPIC
%ifarch s390 %{arm} aarch64 %{mips} riscv64
%global           ldflags         -Wl,--as-needed,--library-path=%{_libdir} %{__global_ldflags}
%else
%global           ldflags         -m%{__isa_bits} -Wl,--as-needed,--library-path=%{_libdir} %{__global_ldflags}
%endif

%global           astvarrundir     /run/asterisk
%global           tmpfilesd        1

%global           apidoc     0
%global           mysql      1
%global           odbc       1
%global           postgresql 1
%global           radius     1
%global           snmp       1
%global           misdn      0
%global           ldap       1
%global           gmime      1
%global           corosync   1
%if 0%{?fedora} >= 34 || 0%{?rhel} >8
%global           imap       0
%else
%global           imap       1
%endif
%if 0%{?fedora} >= 21 || 0%{?rhel} >=7
%global           jack       0
%else
%global           jack       1
%endif
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 7
%global           phone      0
%global           xmpp       0
%global           ices       0
%else
%global           phone      1
%global           xmpp       1
%global           ices       1
%endif
%global           meetme     0
%global           ooh323     0

%global           makeargs        DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{astvarrundir} ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

Summary:          The Open Source PBX
Name:             asterisk
Version:          18.12.1
Release:          %{?_rc||?_beta:0.}1%{?_rc:.rc%{_rc}}%{?_beta:.beta%{_beta}}%{?dist}.15
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              http://www.asterisk.org/

Source0:          http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}.tar.gz
Source1:          http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}.tar.gz.asc
Source2:          asterisk-logrotate
Source3:          menuselect.makedeps
Source4:          menuselect.makeopts
Source5:          asterisk.service
Source6:          asterisk-tmpfiles
# GPG keyring with Asterisk developer signatures
# Created by running:
#gpg2 --no-default-keyring --keyring ./asterisk-gpgkeys.gpg \
#--keyserver=hkp://pool.sks-keyservers.net --recv-keys \
#0x21A91EB1F012252993E9BF4A368AB332B59975F3 \
#0x80CEBC345EC9FF529B4B7B808438CBA18D0CAA72 \
#0xCDBEE4CC699E200EB4D46BB79E76E3A42341CE04 \
#0x639D932D5170532F8C200CCD9C59F000777DCC45 \
#0x551F29104B2106080C6C2851073B0C1FC9B2E352 \
#0x57E769BC37906C091E7F641F6CB44E557BD982D8 \
#0x0F77FB5D216A02390B4C51DB7C2C8A8BCB3F61BD \
#0xF2FC93DB7587BD1FB49E045A5D984BE337191CE7
Source7:          asterisk-gpgkeys.gpg

# Now building Asterisk with bundled pjproject, because they apply custom patches to it
Source8:          https://raw.githubusercontent.com/asterisk/third-party/master/pjproject/%{pjsip_version}/pjproject-%{pjsip_version}.tar.bz2

# Bundling jansson on EL7 and EL8, because the version in CentOS is too old
Source9:          http://www.digip.org/jansson/releases/jansson-%{jansson_version}.tar.bz2

%if 0%{?fedora} || 0%{?rhel} >= 8
Patch0:           asterisk-mariadb.patch
%endif

%if 0%{?fedora} || 0%{?rhel} >=7
Patch1:           asterisk-16.1.0-explicit-python3.patch
%endif

Patch2:           asterisk-18.4.0-astmm_ignore_for_console_board.patch

# Removed macros from ilbc library for RFC 3951 compatibility.
Patch3:           asterisk-18.12.1-ilbc_macros.patch

Patch4:           asterisk-configure-c99.patch

# Fix pjproject build failure on RISC-V architecture
# https://github.com/pjsip/pjproject/pull/4173.patch
Patch5:           pjproject-add-riscv-support.patch

# Asterisk now builds against a bundled copy of pjproject, as they apply some patches
# directly to pjproject before the build against it
Provides:         bundled(pjproject) = %{pjsip_version}

# Does not build on s390x: https://bugzilla.redhat.com/show_bug.cgi?id=1465162
#ExcludeArch:      s390x

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    libxcrypt-devel
BuildRequires:    ncurses
BuildRequires:    perl

# core build requirements
BuildRequires:    openssl-devel
BuildRequires:    newt-devel
BuildRequires:    ncurses-devel
BuildRequires:    libcap-devel
%if 0%{?gmime}
BuildRequires:    gtk2-devel
%endif
BuildRequires:    libsrtp-devel
BuildRequires:    perl-interpreter
BuildRequires:    perl-generators
BuildRequires:    popt-devel
%{?systemd_requires}
BuildRequires:    systemd
BuildRequires:    kernel-headers

# for res_http_post
%if 0%{?gmime}
BuildRequires:    pkgconfig(gmime-3.0)
%endif

# for building docs
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    libxml2-devel
BuildRequires:    latex2html

# for building res_calendar_caldav
BuildRequires:    neon-devel
BuildRequires:    libical-devel
BuildRequires:    libxml2-devel

# for codec_speex
BuildRequires:    speex-devel >= 1.2
%if (0%{?fedora} > 21 || 0%{?rhel} > 7)
BuildRequires:    speexdsp-devel >= 1.2
%endif


# for format_ogg_vorbis
BuildRequires:    libogg-devel
BuildRequires:    libvorbis-devel

# codec_gsm
BuildRequires:    gsm-devel

# additional dependencies
BuildRequires:    SDL-devel
BuildRequires:    SDL_image-devel

# cli
BuildRequires:    libedit-devel

# codec_ilbc
BuildRequires:    ilbc-devel

# res_rtp_asterisk
BuildRequires:    libuuid-devel

# res_resolver_unbound
BuildRequires:    unbound-devel

%if 0%{?corosync}
BuildRequires:    corosynclib-devel
%endif

BuildRequires:    alsa-lib-devel
BuildRequires:    libcurl-devel
BuildRequires:    dahdi-tools-devel >= 2.0.0
BuildRequires:    dahdi-tools-libs >= 2.0.0
BuildRequires:    libpri-devel >= 1.4.12
BuildRequires:    libss7-devel >= 1.0.1
BuildRequires:    spandsp-devel >= 0.0.5-0.1.pre4
BuildRequires:    libtiff-devel
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    lua-devel
%if 0%{?jack}
BuildRequires:    jack-audio-connection-kit-devel
%endif
BuildRequires:    libresample-devel
BuildRequires:    bluez-libs-devel
BuildRequires:    libtool-ltdl-devel
BuildRequires:    portaudio-devel >= 19
BuildRequires:    sqlite-devel
BuildRequires:    freetds-devel

%if 0%{?misdn}
BuildRequires:    mISDN-devel
%endif

%if 0%{?ldap}
BuildRequires:    openldap-devel
%endif

%if 0%{?mysql}
%if 0%{?rhel} >= 7
BuildRequires:    mariadb-devel
%else
BuildRequires:    mariadb-connector-c-devel
%endif
%endif

%if 0%{?odbc}
BuildRequires:    libtool-ltdl-devel
BuildRequires:    unixODBC-devel
%endif

%if 0%{?postgresql}
%if 0%{?rhel}
BuildRequires:    postgresql-devel
%else
BuildRequires:    libpq-devel
%endif
%endif

%if 0%{?radius}
%if 0%{?fedora} || 0%{?rhel} < 7
BuildRequires:    freeradius-client-devel
%else
BuildRequires:    radcli-compat-devel
%endif
%endif

%if 0%{?snmp}
BuildRequires:    net-snmp-devel
BuildRequires:    lm_sensors-devel
%endif

%if 0%{?imap}
BuildRequires:    uw-imap-devel
%endif

%if 0%{?fedora}
BuildRequires:    jansson-devel
%else
Provides:         bundled(jansson) = 2.11
%endif

# for gpg to be able to verify the signature
BuildRequires:    libgcrypt
BuildRequires: make


Requires(post):   systemd-units
Requires(post):   systemd-sysv
Requires(preun):  systemd-units
Requires(postun): systemd-units


# chan_phone headers no longer in kernel headers
Obsoletes:        asterisk-phone < %{version}

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

%package ael
Summary: AEL (Asterisk Extension Logic) modules for Asterisk
Requires: asterisk = %{version}-%{release}

%description ael
AEL (Asterisk Extension Logic) mdoules for Asterisk

%package alsa
Summary: Modules for Asterisk that use Alsa sound drivers
Requires: asterisk = %{version}-%{release}

%package alembic
Summary: Alembic scripts for the Asterisk DB (realtime)
Requires: asterisk = %{version}-%{release}

%description alembic
Alembic scripts for the Asterisk DB


%description alsa
Modules for Asterisk that use Alsa sound drivers.

%if 0%{?apidoc}
%package apidoc
Summary: API documentation for Asterisk
Requires: asterisk = %{version}-%{release}

%description apidoc
API documentation for Asterisk.
%endif

%package calendar
Summary: Calendar applications for Asterisk
Requires: asterisk = %{version}-%{release}

%description calendar
Calendar applications for Asterisk.

%if 0%{?corosync}
%package corosync
Summary: Modules for Asterisk that use Corosync
Requires: asterisk = %{version}-%{release}

%description corosync
Modules for Asterisk that use Corosync.
%endif

%package curl
Summary: Modules for Asterisk that use cURL
Requires: asterisk = %{version}-%{release}

%description curl
Modules for Asterisk that use cURL.

%package dahdi
Summary: Modules for Asterisk that use DAHDI
Requires: asterisk = %{version}-%{release}
Requires: dahdi-tools >= 2.0.0
Requires(pre): %{_sbindir}/usermod
Provides: asterisk-zaptel = %{version}-%{release}

%description dahdi
Modules for Asterisk that use DAHDI.

%package devel
Summary: Development files for Asterisk
Requires: asterisk = %{version}-%{release}

%description devel
Development files for Asterisk.

%package fax
Summary: FAX applications for Asterisk
Requires: asterisk = %{version}-%{release}

%description fax
FAX applications for Asterisk

%package festival
Summary: Festival application for Asterisk
Requires: asterisk = %{version}-%{release}
Requires: festival

%description festival
Application for the Asterisk PBX that uses Festival to convert text to speech.

%package iax2
Summary: IAX2 channel driver for Asterisk
Requires: asterisk = %{version}-%{release}

%description iax2
IAX2 channel driver for Asterisk

%package hep
Summary: Modules for capturing SIP traffic using Homer (HEPv3)
Requires: asterisk = %{version}-%{release}

%description hep
Modules for capturing SIP traffic using Homer (HEPv3)

%if 0%{?ices}
%package ices
Summary: Stream audio from Asterisk to an IceCast server
Requires: asterisk = %{version}-%{release}
Requires: ices

%description ices
Stream audio from Asterisk to an IceCast server.
%endif

%if 0%{?jack}
%package jack
Summary: JACK resources for Asterisk
Requires: asterisk = %{version}-%{release}

%description jack
JACK resources for Asterisk.
%endif

%package lua
Summary: Lua resources for Asterisk
Requires: asterisk = %{version}-%{release}

%description lua
Lua resources for Asterisk.

%if 0%{?ldap}
%package ldap
Summary: LDAP resources for Asterisk
Requires: asterisk = %{version}-%{release}

%description ldap
LDAP resources for Asterisk.
%endif

%if 0%{?misdn}
%package misdn
Summary: mISDN channel for Asterisk
Requires: asterisk = %{version}-%{release}
Requires(pre): %{_sbindir}/usermod

%description misdn
mISDN channel for Asterisk.
%endif

%package mgcp
Summary: MGCP channel driver for Asterisk
Requires: asterisk = %{version}-%{release}

%description mgcp
MGCP channel driver for Asterisk

%package mobile
Summary: Mobile (BlueTooth) channel for Asterisk
Requires: asterisk = %{version}-%{release}
Requires(pre): %{_sbindir}/usermod

%description mobile
Mobile (BlueTooth) channel for Asterisk.

%package minivm
Summary: MiniVM applicaton for Asterisk
Requires: asterisk = %{version}-%{release}

%description minivm
MiniVM application for Asterisk.

%package mwi-external
Summary: Support for developing external voicemail applications
Requires: asterisk = %{version}-%{release}
Conflicts: asterisk-voicemail = %{version}-%{release}
Conflicts: asterisk-voicemail-implementation = %{version}-%{release}

%description mwi-external
Support for developing external voicemail applications

%if 0%{?mysql}
%package mysql
Summary: Applications for Asterisk that use MySQL
Requires: asterisk = %{version}-%{release}

%description mysql
Applications for Asterisk that use MySQL.
%endif

%if 0%{?odbc}
%package odbc
Summary: Applications for Asterisk that use ODBC (except voicemail)
Requires: asterisk = %{version}-%{release}

%description odbc
Applications for Asterisk that use ODBC (except voicemail)
%endif

%if 0%{?ooh323}
%package ooh323
Summary: H.323 channel for Asterisk using the Objective Systems Open H.323 for C library
Requires: asterisk = %{version}-%{release}

%description ooh323
H.323 channel for Asterisk using the Objective Systems Open H.323 for C library.
%endif

%package oss
Summary: Modules for Asterisk that use OSS sound drivers
Requires: asterisk = %{version}-%{release}

%description oss
Modules for Asterisk that use OSS sound drivers.

%package phone
Summary: Channel driver for Quicknet Technologies, Inc.'s Telephony cards
Requires: asterisk = %{version}-%{release}

%description phone
Quicknet Technologies, Inc.'s Telephony cards including the Internet
PhoneJACK, Internet PhoneJACK Lite, Internet PhoneJACK PCI, Internet
LineJACK, Internet PhoneCARD and SmartCABLE.

%package pjsip
Summary: SIP channel based upon the PJSIP library
Requires: asterisk = %{version}-%{release}

%description pjsip
SIP channel based upon the PJSIP library

%package portaudio
Summary: Modules for Asterisk that use the portaudio library
Requires: asterisk = %{version}-%{release}

%description portaudio
Modules for Asterisk that use the portaudio library.

%if 0%{?postgresql}
%package postgresql
Summary: Applications for Asterisk that use PostgreSQL
Requires: asterisk = %{version}-%{release}

%description postgresql
Applications for Asterisk that use PostgreSQL.
%endif

%if 0%{?radius}
%package radius
Summary: Applications for Asterisk that use RADIUS
Requires: asterisk = %{version}-%{release}

%description radius
Applications for Asterisk that use RADIUS.
%endif

%package skinny
Summary: Modules for Asterisk that support the SCCP/Skinny protocol
Requires: asterisk = %{version}-%{release}

%description skinny
Modules for Asterisk that support the SCCP/Skinny protocol.

%package sip
Summary: Legacy SIP channel driver for Asterisk
Requires: asterisk = %{version}-%{release}

%description sip
Legacy SIP channel driver for Asterisk

%if 0%{?snmp}
%package snmp
Summary: Module that enables SNMP monitoring of Asterisk
Requires: asterisk = %{version}-%{release}
# This subpackage depends on perl-libs, this Requires tracks versioning.

%description snmp
Module that enables SNMP monitoring of Asterisk.
%endif

%package sqlite
Summary: Sqlite modules for Asterisk
Requires: asterisk = %{version}-%{release}

%description sqlite
Sqlite modules for Asterisk.

%package tds
Summary: Modules for Asterisk that use FreeTDS
Requires: asterisk = %{version}-%{release}

%description tds
Modules for Asterisk that use FreeTDS.

%package unistim
Summary: Unistim channel for Asterisk
Requires: asterisk = %{version}-%{release}

%description unistim
Unistim channel for Asterisk

%package voicemail
Summary: Common Voicemail Modules for Asterisk
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail-implementation = %{version}-%{release}
Requires: /usr/bin/sox
Requires: /usr/sbin/sendmail
Conflicts: asterisk-mwi-external <= %{version}-%{release}

%description voicemail
Common Voicemail Modules for Asterisk.

%if 0%{?imap}
%package voicemail-imap
Summary: Store voicemail on an IMAP server
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}
Conflicts: asterisk-voicemail-odbc <= %{version}-%{release}
Conflicts: asterisk-voicemail-plain <= %{version}-%{release}

%description voicemail-imap
Voicemail implementation for Asterisk that stores voicemail on an IMAP
server.
%endif

%package voicemail-odbc
Summary: Store voicemail in a database using ODBC
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}
Conflicts: asterisk-voicemail-imap <= %{version}-%{release}
Conflicts: asterisk-voicemail-plain <= %{version}-%{release}

%description voicemail-odbc
Voicemail implementation for Asterisk that uses ODBC to store
voicemail in a database.

%package voicemail-plain
Summary: Store voicemail on the local filesystem
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}
Conflicts: asterisk-voicemail-imap <= %{version}-%{release}
Conflicts: asterisk-voicemail-odbc <= %{version}-%{release}

%description voicemail-plain
Voicemail implementation for Asterisk that stores voicemail on the
local filesystem.

%if 0%{?xmpp}
%package xmpp
Summary: Jabber/XMPP resources for Asterisk
Requires: asterisk = %{version}-%{release}

%description xmpp
Jabber/XMPP resources for Asterisk.
%endif

%prep
%if 0%{?fedora} || 0%{?rhel} >=8
# only verifying on Fedora and RHEL >=8 due to version of gpg
rpm -q libgcrypt
gpgv2 --keyring %{SOURCE7} %{SOURCE1} %{SOURCE0}
%endif
%setup -q -n asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}


# copy the pjproject tarball to the cache/ directory
mkdir cache
cp %{SOURCE8} cache/

%if 0%{?rhel} >= 7
cp %{SOURCE9} cache/
%endif

echo '*************************************************************************'
ls -altr cache/
pwd
echo '*************************************************************************'

%if 0%{?fedora} || 0%{?rhel} >=8
%patch -P0 -p1
%endif

%if 0%{?fedora} || 0%{?rhel} >=7
%patch -P1 -p1
%endif

%patch -P2 -p1

%patch -P3 -p1

%patch -P4 -p1

%patch -P5 -p1
cp %{S:3} menuselect.makedeps
cp %{S:4} menuselect.makeopts



# Fixup makefile so sound archives aren't downloaded/installed
%{__perl} -pi -e 's/^all:.*$/all:/' sounds/Makefile
%{__perl} -pi -e 's/^install:.*$/install:/' sounds/Makefile

# convert comments in one file to UTF-8
mv main/fskmodem.c main/fskmodem.c.old
iconv -f iso-8859-1 -t utf-8 -o main/fskmodem.c main/fskmodem.c.old
touch -r main/fskmodem.c.old main/fskmodem.c
rm main/fskmodem.c.old

chmod -x contrib/scripts/dbsep.cgi

%if ! 0%{?corosync}
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_corosync/g' menuselect.makeopts
%endif

%if ! 0%{?mysql}
%{__perl} -pi -e 's/^MENUSELECT_ADDONS=(.*)$/MENUSELECT_ADDONS=\1 res_config_mysql app_mysql cdr_mysql/g' menuselect.makeopts
%endif

%if ! 0%{?postgresql}
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_config_pgsql/g' menuselect.makeopts
%{__perl} -pi -e 's/^MENUSELECT_CDR=(.*)$/MENUSELECT_CDR=\1 cdr_pgsql/g' menuselect.makeopts
%{__perl} -pi -e 's/^MENUSELECT_CEL=(.*)$/MENUSELECT_CEL=\1 cel_pgsql/g' menuselect.makeopts
%endif

%if ! 0%{?radius}
%{__perl} -pi -e 's/^MENUSELECT_CDR=(.*)$/MENUSELECT_CDR=\1 cdr_radius/g' menuselect.makeopts
%{__perl} -pi -e 's/^MENUSELECT_CEL=(.*)$/MENUSELECT_CEL=\1 cel_radius/g' menuselect.makeopts
%endif

%if ! 0%{?snmp}
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_snmp/g' menuselect.makeopts
%endif

%if ! 0%{?misdn}
%{__perl} -pi -e 's/^MENUSELECT_CHANNELS=(.*)$/MENUSELECT_CHANNELS=\1 chan_misdn/g' menuselect.makeopts
%endif

%if ! 0%{?ices}
%{__perl} -pi -e 's/^MENUSELECT_APPS=(.*)$/MENUSELECT_APPS=\1 app_ices/g' menuselect.makeopts
%endif

%if ! 0%{?jack}
%{__perl} -pi -e 's/^MENUSELECT_APPS=(.*)$/MENUSELECT_APPS=\1 app_jack/g' menuselect.makeopts
%endif

%if ! 0%{?ldap}
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_config_ldap/g' menuselect.makeopts
%endif

%if ! 0%{?gmime}
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_http_post/g' menuselect.makeopts
%endif

%if ! 0%{xmpp}
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_xmpp/g' menuselect.makeopts
%{__perl} -pi -e 's/^MENUSELECT_CHANNELS=(.*)$/MENUSELECT_CHANNELS=\1 chan_motif/g' menuselect.makeopts
%endif

%if ! 0%{meetme}
%{__perl} -pi -e 's/^MENUSELECT_APPS=(.*)$/MENUSELECT_APPS=\1 app_meetme/g' menuselect.makeopts
%endif

%if ! 0%{ooh323}
%{__perl} -pi -e 's/^MENUSELECT_ADDONS=(.*)$/MENUSELECT_ADDONS=\1 chan_ooh323/g' menuselect.makeopts
%endif

%if ! 0%{imap}
%{__perl} -pi -e 's/^MENUSELECT_APPS=(.*)$/MENUSELECT_APPS=\1 app_voicemail_imap/g' menuselect.makeopts
%endif

# Create a sysusers.d config file
cat >asterisk.sysusers.conf <<EOF
u asterisk - 'Asterisk User' /var/lib/asterisk -
EOF

%build

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"
export ASTCFLAGS=" "

sed -i '1s/env python/python3/' contrib/scripts/refcounter.py

#aclocal -I autoconf --force
#autoconf --force
#autoheader --force
./bootstrap.sh

pushd menuselect
%configure
popd


%if 0%{?fedora}
%if 0%{?imap}
%configure --with-imap=system --with-gsm=/usr --with-ilbc=/usr --with-libedit=yes --with-srtp --with-pjproject-bundled --with-externals-cache=%{_builddir}/asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}/cache LDFLAGS="%{ldflags}" NOISY_BUILD=1 CPPFLAGS="-fPIC"
%else
%configure --without-imap --with-gsm=/usr --with-ilbc=/usr --with-libedit=yes --with-srtp --with-pjproject-bundled --with-externals-cache=%{_builddir}/asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}/cache LDFLAGS="%{ldflags}" NOISY_BUILD=1 CPPFLAGS="-fPIC"
%endif
%else
%if 0%{?imap}
%configure --with-imap=system --with-gsm=/usr --with-ilbc=/usr --with-libedit=yes --with-srtp --with-jansson-bundled --with-pjproject-bundled --with-externals-cache=%{_builddir}/asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}/cache LDFLAGS="%{ldflags}" NOISY_BUILD=1 CPPFLAGS="-fPIC"
%else
%configure --without-imap --with-gsm=/usr --with-ilbc=/usr --with-libedit=yes --with-srtp --with-jansson-bundled --with-pjproject-bundled --with-externals-cache=%{_builddir}/asterisk-%{version}%{?_rc:-rc%{_rc}}%{?_beta:-beta%{_beta}}/cache LDFLAGS="%{ldflags}" NOISY_BUILD=1 CPPFLAGS="-fPIC"
%endif
%endif

%make_build menuselect-tree NOISY_BUILD=1
%{__perl} -n -i -e 'print unless /openr2/i' menuselect-tree


# Build with plain voicemail and directory
echo "### Building with plain voicemail and directory"
%make_build %{makeargs}

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_plain.so
mv apps/app_directory.so apps/app_directory_plain.so

%if 0%{?imap}
# Now build with IMAP storage for voicemail and directory
sed -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=IMAP_STORAGE/' menuselect.makeopts

echo "### Building with IMAP voicemail and directory"
%make_build %{makeargs}

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_imap.so
mv apps/app_directory.so apps/app_directory_imap.so
%endif

# Now build with ODBC storage for voicemail and directory

sed -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE/' menuselect.makeopts
echo "### Building with ODBC voicemail and directory"
%make_build %{makeargs}

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_odbc.so
mv apps/app_directory.so apps/app_directory_odbc.so

# so that these modules don't get built again
touch apps/app_voicemail.o apps/app_directory.o
touch apps/app_voicemail.so apps/app_directory.so

sed -i -e 's/^MENUSELECT_RES=\(.*\)\bres_mwi_external\b\(.*\)$/MENUSELECT_RES=\1 \2/g' menuselect.makeopts
sed -i -e 's/^MENUSELECT_RES=\(.*\)\bres_mwi_external_ami\b\(.*\)$/MENUSELECT_RES=\1 \2/g' menuselect.makeopts
sed -i -e 's/^MENUSELECT_RES=\(.*\)\bres_stasis_mailbox\b\(.*\)$/MENUSELECT_RES=\1 \2/g' menuselect.makeopts
sed -i -e 's/^MENUSELECT_RES=\(.*\)\bres_ari_mailboxes\b\(.*\)$/MENUSELECT_RES=\1 \2/g' menuselect.makeopts
sed -i -e 's/^MENUSELECT_APP=\(.*\)$/MENUSELECT_RES=\1 app_voicemail/g' menuselect.makeopts

%make_build %{makeargs}

%if 0%{?apidoc}
%make_build progdocs %{makeargs}

# fix dates so that we don't get multilib conflicts
find doc/api/html -type f -print0 | xargs --null touch -r ChangeLog
%endif

%install
rm -rf %{buildroot}

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"
export ASTCFLAGS="%{optflags}"

make install %{makeargs}
make samples %{makeargs}
make install-headers %{makeargs}

install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/asterisk.service
rm -f %{buildroot}%{_sbindir}/safe_asterisk
install -D -p -m 0644 %{S:2} %{buildroot}%{_sysconfdir}/logrotate.d/asterisk

rm %{buildroot}%{_libdir}/asterisk/modules/app_directory.so
rm %{buildroot}%{_libdir}/asterisk/modules/app_voicemail.so

%if 0%{?imap}
install -D -p -m 0755 apps/app_directory_imap.so %{buildroot}%{_libdir}/asterisk/modules/app_directory_imap.so
install -D -p -m 0755 apps/app_voicemail_imap.so %{buildroot}%{_libdir}/asterisk/modules/app_voicemail_imap.so
%endif
install -D -p -m 0755 apps/app_directory_odbc.so %{buildroot}%{_libdir}/asterisk/modules/app_directory_odbc.so
install -D -p -m 0755 apps/app_voicemail_odbc.so %{buildroot}%{_libdir}/asterisk/modules/app_voicemail_odbc.so
install -D -p -m 0755 apps/app_directory_plain.so %{buildroot}%{_libdir}/asterisk/modules/app_directory_plain.so
install -D -p -m 0755 apps/app_voicemail_plain.so %{buildroot}%{_libdir}/asterisk/modules/app_voicemail_plain.so

# create some directories that need to be packaged
mkdir -p %{buildroot}%{_datadir}/asterisk/moh
mkdir -p %{buildroot}%{_datadir}/asterisk/sounds
mkdir -p %{buildroot}%{_datadir}/asterisk/ast-db-manage
mkdir -p %{buildroot}%{_localstatedir}/lib/asterisk
mkdir -p %{buildroot}%{_localstatedir}/log/asterisk/cdr-custom
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/festival
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/monitor
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/outgoing
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/uploads

# We're not going to package any of the sample AGI scripts
rm -f %{buildroot}%{_datadir}/asterisk/agi-bin/*

# Don't package the sample voicemail user
rm -rf %{buildroot}%{_localstatedir}/spool/asterisk/voicemail/default

# Don't package example phone provision configs
rm -rf %{buildroot}%{_datadir}/asterisk/phoneprov/*

# these are compiled with -O0 and thus include unfortified code.
rm -rf %{buildroot}%{_sbindir}/hashtest
rm -rf %{buildroot}%{_sbindir}/hashtest2

#
rm -rf %{buildroot}%{_sysconfdir}/asterisk/app_skel.conf
rm -rf %{buildroot}%{_sysconfdir}/asterisk/config_test.conf
rm -rf %{buildroot}%{_sysconfdir}/asterisk/test_sorcery.conf

rm -rf %{buildroot}%{_libdir}/libasteriskssl.so
ln -s libasterisk.so.1 %{buildroot}%{_libdir}/libasteriskssl.so

%if 0%{?apidoc}
find doc/api/html -name \*.map -size 0 -delete
%endif

# copy the alembic scripts
cp -rp contrib/ast-db-manage %{buildroot}%{_datadir}/asterisk/ast-db-manage

%if %{tmpfilesd}
install -D -p -m 0644 %{SOURCE6} %{buildroot}/usr/lib/tmpfiles.d/asterisk.conf
mkdir -p %{buildroot}%{astvarrundir}
%endif

%if ! 0%{?mysql}
rm -f %{buildroot}%{_sysconfdir}/asterisk/*_mysql.conf
%endif

%if ! 0%{?postgresql}
rm -f %{buildroot}%{_sysconfdir}/asterisk/*_pgsql.conf
%endif

%if ! 0%{?misdn}
rm -f %{buildroot}%{_sysconfdir}/asterisk/misdn.conf
%endif

%if ! 0%{?snmp}
rm -f %{buildroot}%{_sysconfdir}/asterisk/res_snmp.conf
%endif

%if ! 0%{?ldap}
rm -f %{buildroot}%{_sysconfdir}/asterisk/res_ldap.conf
%endif

%if ! 0%{?corosync}
rm -f %{buildroot}%{_sysconfdir}/asterisk/res_corosync.conf
%endif

%if ! 0%{?phone}
rm -f %{buildroot}%{_sysconfdir}/asterisk/phone.conf
%endif

%if ! 0%{xmpp}
rm -f %{buildroot}%{_sysconfdir}/asterisk/xmpp.conf
rm -f %{buildroot}%{_sysconfdir}/asterisk/motif.conf
%endif

%if ! 0%{ooh323}
rm -f %{buildroot}%{_sysconfdir}/asterisk/ooh323.conf
%endif

install -m0644 -D asterisk.sysusers.conf %{buildroot}%{_sysusersdir}/asterisk.conf


%post
if [ $1 -eq 1 ] ; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ "$1" -eq "0" ]; then
	# Package removal, not upgrade
	/bin/systemctl --no-reload disable asterisk.service > /dev/null 2>&1 || :
	/bin/systemctl stop asterisk.service > /dev/null 2>&1 || :
fi


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart asterisk.service >/dev/null 2>&1 || :
fi

%triggerun -- asterisk < 1.8.2.4-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply asterisk
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save asterisk >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del asterisk >/dev/null 2>&1 || :
/bin/systemctl try-restart asterisk.service >/dev/null 2>&1 || :

%pre dahdi
%{_sbindir}/usermod -a -G dahdi asterisk

%if 0%{?misdn}
%pre misdn
%{_sbindir}/usermod -a -G misdn asterisk
%endif

%files
%doc *.txt ChangeLog BUGS CREDITS configs
%license LICENSE

%doc doc/asterisk.sgml

%{_unitdir}/asterisk.service

%{_libdir}/libasteriskssl.so.1

%{_libdir}/libasteriskpj.so
%{_libdir}/libasteriskpj.so.2
%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules
%{_libdir}/asterisk/modules/app_agent_pool.so
%{_libdir}/asterisk/modules/app_adsiprog.so
%{_libdir}/asterisk/modules/app_alarmreceiver.so
%{_libdir}/asterisk/modules/app_amd.so
%{_libdir}/asterisk/modules/app_attended_transfer.so
%{_libdir}/asterisk/modules/app_audiosocket.so
%{_libdir}/asterisk/modules/app_authenticate.so
%{_libdir}/asterisk/modules/app_blind_transfer.so
%{_libdir}/asterisk/modules/app_bridgeaddchan.so
%{_libdir}/asterisk/modules/app_bridgewait.so
%{_libdir}/asterisk/modules/app_cdr.so
%{_libdir}/asterisk/modules/app_celgenuserevent.so
%{_libdir}/asterisk/modules/app_chanisavail.so
%{_libdir}/asterisk/modules/app_channelredirect.so
%{_libdir}/asterisk/modules/app_chanspy.so
%{_libdir}/asterisk/modules/app_confbridge.so
%{_libdir}/asterisk/modules/app_controlplayback.so
%{_libdir}/asterisk/modules/app_db.so
%{_libdir}/asterisk/modules/app_dial.so
%{_libdir}/asterisk/modules/app_dictate.so
%{_libdir}/asterisk/modules/app_directed_pickup.so
%{_libdir}/asterisk/modules/app_disa.so
%{_libdir}/asterisk/modules/app_dtmfstore.so
%{_libdir}/asterisk/modules/app_dumpchan.so
%{_libdir}/asterisk/modules/app_echo.so
%{_libdir}/asterisk/modules/app_exec.so
%{_libdir}/asterisk/modules/app_externalivr.so
%{_libdir}/asterisk/modules/app_followme.so
%{_libdir}/asterisk/modules/app_forkcdr.so
%{_libdir}/asterisk/modules/app_getcpeid.so
%{_libdir}/asterisk/modules/app_image.so
%{_libdir}/asterisk/modules/app_macro.so
%{_libdir}/asterisk/modules/app_mf.so
%{_libdir}/asterisk/modules/app_milliwatt.so
%{_libdir}/asterisk/modules/app_mixmonitor.so
%{_libdir}/asterisk/modules/app_morsecode.so
%{_libdir}/asterisk/modules/app_nbscat.so
%{_libdir}/asterisk/modules/app_originate.so
%{_libdir}/asterisk/modules/app_page.so
#%%{_libdir}/asterisk/modules/app_parkandannounce.so
%{_libdir}/asterisk/modules/app_playback.so
%{_libdir}/asterisk/modules/app_playtones.so
%{_libdir}/asterisk/modules/app_privacy.so
%{_libdir}/asterisk/modules/app_queue.so
%{_libdir}/asterisk/modules/app_readexten.so
#%%{_libdir}/asterisk/modules/app_readfile.so
%{_libdir}/asterisk/modules/app_read.so
%{_libdir}/asterisk/modules/app_record.so
%{_libdir}/asterisk/modules/app_reload.so
%{_libdir}/asterisk/modules/app_saycounted.so
#%%{_libdir}/asterisk/modules/app_saycountpl.so
%{_libdir}/asterisk/modules/app_sayunixtime.so
%{_libdir}/asterisk/modules/app_senddtmf.so
%{_libdir}/asterisk/modules/app_sendtext.so
%{_libdir}/asterisk/modules/app_sf.so
#%%{_libdir}/asterisk/modules/app_setcallerid.so
%{_libdir}/asterisk/modules/app_sms.so
%{_libdir}/asterisk/modules/app_softhangup.so
%{_libdir}/asterisk/modules/app_speech_utils.so
%{_libdir}/asterisk/modules/app_stack.so
%{_libdir}/asterisk/modules/app_stasis.so
%{_libdir}/asterisk/modules/app_statsd.so
%{_libdir}/asterisk/modules/app_stream_echo.so
%{_libdir}/asterisk/modules/app_system.so
%{_libdir}/asterisk/modules/app_talkdetect.so
%{_libdir}/asterisk/modules/app_test.so
%{_libdir}/asterisk/modules/app_transfer.so
%{_libdir}/asterisk/modules/app_url.so
%{_libdir}/asterisk/modules/app_userevent.so
%{_libdir}/asterisk/modules/app_verbose.so
%{_libdir}/asterisk/modules/app_waitforcond.so
%{_libdir}/asterisk/modules/app_waitforring.so
%{_libdir}/asterisk/modules/app_waitforsilence.so
%{_libdir}/asterisk/modules/app_waituntil.so
%{_libdir}/asterisk/modules/app_while.so
%{_libdir}/asterisk/modules/app_zapateller.so
%{_libdir}/asterisk/modules/bridge_builtin_features.so
%{_libdir}/asterisk/modules/bridge_builtin_interval_features.so
%{_libdir}/asterisk/modules/bridge_holding.so
%{_libdir}/asterisk/modules/bridge_native_rtp.so
%{_libdir}/asterisk/modules/bridge_simple.so
%{_libdir}/asterisk/modules/bridge_softmix.so
%{_libdir}/asterisk/modules/cdr_csv.so
%{_libdir}/asterisk/modules/cdr_custom.so
%{_libdir}/asterisk/modules/cdr_manager.so
%{_libdir}/asterisk/modules/cdr_syslog.so
%{_libdir}/asterisk/modules/cel_custom.so
%{_libdir}/asterisk/modules/cel_manager.so
%{_libdir}/asterisk/modules/chan_audiosocket.so
%{_libdir}/asterisk/modules/chan_bridge_media.so
#%%{_libdir}/asterisk/modules/chan_multicast_rtp.so
%{_libdir}/asterisk/modules/chan_rtp.so
%{_libdir}/asterisk/modules/codec_adpcm.so
%{_libdir}/asterisk/modules/codec_alaw.so
%{_libdir}/asterisk/modules/codec_a_mu.so
%{_libdir}/asterisk/modules/codec_g722.so
%{_libdir}/asterisk/modules/codec_g726.so
%{_libdir}/asterisk/modules/codec_gsm.so
%{_libdir}/asterisk/modules/codec_ilbc.so
%{_libdir}/asterisk/modules/codec_lpc10.so
%{_libdir}/asterisk/modules/codec_resample.so
%{_libdir}/asterisk/modules/codec_speex.so
%{_libdir}/asterisk/modules/codec_ulaw.so
%{_libdir}/asterisk/modules/format_g719.so
%{_libdir}/asterisk/modules/format_g723.so
%{_libdir}/asterisk/modules/format_g726.so
%{_libdir}/asterisk/modules/format_g729.so
%{_libdir}/asterisk/modules/format_gsm.so
%{_libdir}/asterisk/modules/format_h263.so
%{_libdir}/asterisk/modules/format_h264.so
%{_libdir}/asterisk/modules/format_ilbc.so
#%%{_libdir}/asterisk/modules/format_jpeg.so
%{_libdir}/asterisk/modules/format_ogg_speex.so
%{_libdir}/asterisk/modules/format_ogg_vorbis.so
%{_libdir}/asterisk/modules/format_pcm.so
%{_libdir}/asterisk/modules/format_siren14.so
%{_libdir}/asterisk/modules/format_siren7.so
%{_libdir}/asterisk/modules/format_sln.so
%{_libdir}/asterisk/modules/format_vox.so
%{_libdir}/asterisk/modules/format_wav_gsm.so
%{_libdir}/asterisk/modules/format_wav.so
%{_libdir}/asterisk/modules/func_aes.so
#%%{_libdir}/asterisk/modules/func_audiohookinherit.so
%{_libdir}/asterisk/modules/func_base64.so
%{_libdir}/asterisk/modules/func_blacklist.so
%{_libdir}/asterisk/modules/func_callcompletion.so
%{_libdir}/asterisk/modules/func_callerid.so
%{_libdir}/asterisk/modules/func_cdr.so
%{_libdir}/asterisk/modules/func_channel.so
%{_libdir}/asterisk/modules/func_config.so
%{_libdir}/asterisk/modules/func_cut.so
%{_libdir}/asterisk/modules/func_db.so
%{_libdir}/asterisk/modules/func_devstate.so
%{_libdir}/asterisk/modules/func_dialgroup.so
%{_libdir}/asterisk/modules/func_dialplan.so
%{_libdir}/asterisk/modules/func_enum.so
%{_libdir}/asterisk/modules/func_env.so
%{_libdir}/asterisk/modules/func_evalexten.so
%{_libdir}/asterisk/modules/func_extstate.so
%{_libdir}/asterisk/modules/func_frame_drop.so
%{_libdir}/asterisk/modules/func_frame_trace.so
%{_libdir}/asterisk/modules/func_global.so
%{_libdir}/asterisk/modules/func_groupcount.so
%{_libdir}/asterisk/modules/func_hangupcause.so
%{_libdir}/asterisk/modules/func_holdintercept.so
%{_libdir}/asterisk/modules/func_iconv.so
%{_libdir}/asterisk/modules/func_jitterbuffer.so
%{_libdir}/asterisk/modules/func_json.so
%{_libdir}/asterisk/modules/func_lock.so
%{_libdir}/asterisk/modules/func_logic.so
%{_libdir}/asterisk/modules/func_math.so
%{_libdir}/asterisk/modules/func_md5.so
%{_libdir}/asterisk/modules/func_module.so
%{_libdir}/asterisk/modules/func_periodic_hook.so
%{_libdir}/asterisk/modules/func_pitchshift.so
%{_libdir}/asterisk/modules/func_presencestate.so
%{_libdir}/asterisk/modules/func_rand.so
%{_libdir}/asterisk/modules/func_realtime.so
%{_libdir}/asterisk/modules/func_sayfiles.so
%{_libdir}/asterisk/modules/func_scramble.so
%{_libdir}/asterisk/modules/func_sha1.so
%{_libdir}/asterisk/modules/func_shell.so
%{_libdir}/asterisk/modules/func_sorcery.so
%{_libdir}/asterisk/modules/func_speex.so
%{_libdir}/asterisk/modules/func_sprintf.so
%{_libdir}/asterisk/modules/func_srv.so
%{_libdir}/asterisk/modules/func_strings.so
%{_libdir}/asterisk/modules/func_sysinfo.so
%{_libdir}/asterisk/modules/func_talkdetect.so
%{_libdir}/asterisk/modules/func_timeout.so
%{_libdir}/asterisk/modules/func_uri.so
%{_libdir}/asterisk/modules/func_version.so
%{_libdir}/asterisk/modules/func_volume.so
%{_libdir}/asterisk/modules/pbx_config.so
%{_libdir}/asterisk/modules/pbx_dundi.so
%{_libdir}/asterisk/modules/pbx_loopback.so
%{_libdir}/asterisk/modules/pbx_realtime.so
%{_libdir}/asterisk/modules/pbx_spool.so
%{_libdir}/asterisk/modules/res_adsi.so
%{_libdir}/asterisk/modules/res_aeap.so
%{_libdir}/asterisk/modules/res_agi.so
%{_libdir}/asterisk/modules/res_ari.so
%{_libdir}/asterisk/modules/res_ari_applications.so
%{_libdir}/asterisk/modules/res_ari_asterisk.so
%{_libdir}/asterisk/modules/res_ari_bridges.so
%{_libdir}/asterisk/modules/res_ari_channels.so
%{_libdir}/asterisk/modules/res_ari_device_states.so
%{_libdir}/asterisk/modules/res_ari_endpoints.so
%{_libdir}/asterisk/modules/res_ari_events.so
%{_libdir}/asterisk/modules/res_ari_mailboxes.so
%{_libdir}/asterisk/modules/res_ari_model.so
%{_libdir}/asterisk/modules/res_ari_playbacks.so
%{_libdir}/asterisk/modules/res_ari_recordings.so
%{_libdir}/asterisk/modules/res_ari_sounds.so
%{_libdir}/asterisk/modules/res_audiosocket.so
%{_libdir}/asterisk/modules/res_chan_stats.so
%{_libdir}/asterisk/modules/res_clialiases.so
%{_libdir}/asterisk/modules/res_clioriginate.so
%{_libdir}/asterisk/modules/res_convert.so
%{_libdir}/asterisk/modules/res_crypto.so
%{_libdir}/asterisk/modules/res_endpoint_stats.so
%{_libdir}/asterisk/modules/res_format_attr_celt.so
%{_libdir}/asterisk/modules/res_format_attr_g729.so
%{_libdir}/asterisk/modules/res_format_attr_h263.so
%{_libdir}/asterisk/modules/res_format_attr_h264.so
%{_libdir}/asterisk/modules/res_format_attr_ilbc.so
%{_libdir}/asterisk/modules/res_format_attr_opus.so
%{_libdir}/asterisk/modules/res_format_attr_silk.so
%{_libdir}/asterisk/modules/res_format_attr_siren14.so
%{_libdir}/asterisk/modules/res_format_attr_siren7.so
%{_libdir}/asterisk/modules/res_format_attr_vp8.so
%{_libdir}/asterisk/modules/res_http_media_cache.so
%if 0%{?gmime}
%{_libdir}/asterisk/modules/res_http_post.so
%endif
%{_libdir}/asterisk/modules/res_http_websocket.so
%{_libdir}/asterisk/modules/res_limit.so
%{_libdir}/asterisk/modules/res_manager_devicestate.so
%{_libdir}/asterisk/modules/res_manager_presencestate.so
%{_libdir}/asterisk/modules/res_monitor.so
%{_libdir}/asterisk/modules/res_musiconhold.so
%{_libdir}/asterisk/modules/res_mutestream.so
%{_libdir}/asterisk/modules/res_mwi_devstate.so
%{_libdir}/asterisk/modules/res_parking.so
%{_libdir}/asterisk/modules/res_phoneprov.so
# res_pjproject is required by res_rtp_asterisk
%{_libdir}/asterisk/modules/res_pjproject.so
%{_libdir}/asterisk/modules/res_prometheus.so
%{_libdir}/asterisk/modules/res_realtime.so
%{_libdir}/asterisk/modules/res_remb_modifier.so
%{_libdir}/asterisk/modules/res_resolver_unbound.so
%{_libdir}/asterisk/modules/res_rtp_asterisk.so
%{_libdir}/asterisk/modules/res_rtp_multicast.so
#%%{_libdir}/asterisk/modules/res_sdp_translator_pjmedia.so
%{_libdir}/asterisk/modules/res_security_log.so
%{_libdir}/asterisk/modules/res_smdi.so
%{_libdir}/asterisk/modules/res_sorcery_astdb.so
%{_libdir}/asterisk/modules/res_sorcery_config.so
%{_libdir}/asterisk/modules/res_sorcery_memory.so
%{_libdir}/asterisk/modules/res_sorcery_memory_cache.so
%{_libdir}/asterisk/modules/res_sorcery_realtime.so
%{_libdir}/asterisk/modules/res_speech.so
%{_libdir}/asterisk/modules/res_speech_aeap.so
%{_libdir}/asterisk/modules/res_srtp.so
%{_libdir}/asterisk/modules/res_stasis.so
%{_libdir}/asterisk/modules/res_stasis_answer.so
%{_libdir}/asterisk/modules/res_stasis_device_state.so
%{_libdir}/asterisk/modules/res_stasis_playback.so
%{_libdir}/asterisk/modules/res_stasis_recording.so
%{_libdir}/asterisk/modules/res_stasis_snoop.so
%{_libdir}/asterisk/modules/res_statsd.so
%{_libdir}/asterisk/modules/res_stir_shaken.so
%{_libdir}/asterisk/modules/res_stun_monitor.so
%{_libdir}/asterisk/modules/res_timing_pthread.so
%{_libdir}/asterisk/modules/res_timing_timerfd.so
%{_libdir}/asterisk/modules/res_tonedetect.so

%{_sbindir}/astcanary
%{_sbindir}/astdb2sqlite3
%{_sbindir}/asterisk
%{_sbindir}/astgenkey
%{_sbindir}/astman
%{_sbindir}/astversion
%{_sbindir}/autosupport
#%%{_sbindir}/check_expr
#%%{_sbindir}/check_expr2
%{_sbindir}/muted
%{_sbindir}/rasterisk
#%%{_sbindir}/refcounter
%{_sbindir}/smsq
%{_sbindir}/stereorize
%{_sbindir}/streamplayer

%{_mandir}/man8/astdb2bdb.8*
%{_mandir}/man8/astdb2sqlite3.8*
%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*
%{_mandir}/man8/safe_asterisk.8*

%attr(0750,asterisk,asterisk) %dir %{_sysconfdir}/asterisk
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/acl.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adsi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/aeap.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/agents.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alarmreceiver.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/amd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ari.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ast_debug_tools.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ccss.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_beanstalkd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_syslog.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_beanstalkd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_aliases.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_permissions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/codecs.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/confbridge.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dnsmgr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dsp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dundi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/enum.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extconfig.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/features.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/followme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/http.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/indications.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/logger.conf
%attr(0600,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/modules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/musiconhold.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/muted.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phoneprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/prometheus.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queuerules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queues.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_parking.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_stun_monitor.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/resolver_unbound.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rtp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/say.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sla.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/smdi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sorcery.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/stasis.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/statsd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/stir_shaken.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/telcordia-1.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/udptl.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/users.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/vpb.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/asterisk

%dir %{_datadir}/asterisk
%dir %{_datadir}/asterisk/agi-bin
%{_datadir}/asterisk/documentation
%{_datadir}/asterisk/images
%attr(0750,asterisk,asterisk) %{_datadir}/asterisk/keys
%{_datadir}/asterisk/phoneprov
%{_datadir}/asterisk/static-http
%{_datadir}/asterisk/rest-api
%dir %{_datadir}/asterisk/moh
%dir %{_datadir}/asterisk/sounds

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/lib/asterisk

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-csv
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-custom

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/monitor
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/tmp
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/uploads
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/voicemail

%if %{tmpfilesd}
%attr(0644,root,root) /usr/lib/tmpfiles.d/asterisk.conf
%endif
%attr(0755,asterisk,asterisk) %dir %{astvarrundir}

%{_datarootdir}/asterisk/scripts/
%{_sysusersdir}/asterisk.conf

%files ael
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.ael
%{_sbindir}/aelparse
#%%{_sbindir}/conf2ael
%{_libdir}/asterisk/modules/pbx_ael.so
%{_libdir}/asterisk/modules/res_ael_share.so

%files alsa
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alsa.conf
%{_libdir}/asterisk/modules/chan_alsa.so

%files alembic
%{_datadir}/asterisk/ast-db-manage/

%if %{?apidoc}
%files apidoc
%doc doc/api/html/*
%endif

%files calendar
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/calendar.conf
%{_libdir}/asterisk/modules/res_calendar.so
%{_libdir}/asterisk/modules/res_calendar_caldav.so
%{_libdir}/asterisk/modules/res_calendar_ews.so
%{_libdir}/asterisk/modules/res_calendar_icalendar.so

%if 0%{?corosync}
%files corosync
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_corosync.conf
%{_libdir}/asterisk/modules/res_corosync.so
%endif

%files curl
%doc contrib/scripts/dbsep.cgi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dbsep.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_curl.conf
%{_libdir}/asterisk/modules/func_curl.so
%{_libdir}/asterisk/modules/res_config_curl.so
%{_libdir}/asterisk/modules/res_curl.so

%files dahdi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/meetme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_dahdi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ss7.timers
%{_libdir}/asterisk/modules/app_flash.so
%if 0%{?meetme} 
%{_libdir}/asterisk/modules/app_meetme.so
%endif
%{_libdir}/asterisk/modules/app_dahdiras.so
%{_libdir}/asterisk/modules/chan_dahdi.so
%{_libdir}/asterisk/modules/codec_dahdi.so
%{_libdir}/asterisk/modules/res_timing_dahdi.so
%{_datadir}/dahdi/span_config.d/40-asterisk

%files devel
%{_libdir}/libasteriskssl.so
%dir %{_includedir}/asterisk
%dir %{_includedir}/asterisk/doxygen
%{_includedir}/asterisk.h
%{_includedir}/asterisk/*.h
%{_includedir}/asterisk/doxygen/*.h

%files fax
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_fax.conf
%{_libdir}/asterisk/modules/res_fax.so
%{_libdir}/asterisk/modules/res_fax_spandsp.so

%files festival
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/festival.conf
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/festival
%{_libdir}/asterisk/modules/app_festival.so

%files iax2
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iax.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iaxprov.conf
%dir %{_datadir}/asterisk/firmware
%dir %{_datadir}/asterisk/firmware/iax
%{_libdir}/asterisk/modules/chan_iax2.so

%files hep
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/hep.conf
%{_libdir}/asterisk/modules/res_hep.so
%{_libdir}/asterisk/modules/res_hep_rtcp.so
%{_libdir}/asterisk/modules/res_hep_pjsip.so

%if 0%{?ices}
%files ices
%doc contrib/asterisk-ices.xml
%{_libdir}/asterisk/modules/app_ices.so
%endif

%if 0%{?jack}
%files jack
%{_libdir}/asterisk/modules/app_jack.so
%endif

%files lua
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.lua
%{_libdir}/asterisk/modules/pbx_lua.so

%if 0%{?ldap}
%files ldap
#doc doc/ldap.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_ldap.conf
%{_libdir}/asterisk/modules/res_config_ldap.so
%endif

%files minivm
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions_minivm.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/minivm.conf
%{_libdir}/asterisk/modules/app_minivm.so

%if 0%{misdn}
%files misdn
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%{_libdir}/asterisk/modules/chan_misdn.so
%endif

%files mgcp
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/mgcp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pktccops.conf
%{_libdir}/asterisk/modules/chan_mgcp.so
%{_libdir}/asterisk/modules/res_pktccops.so

%files mobile
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_mobile.conf
%{_libdir}/asterisk/modules/chan_mobile.so

%if 0%{mysql}
%files mysql
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/app_mysql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_mysql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_mysql.conf
%doc contrib/realtime/mysql/*.sql
%{_libdir}/asterisk/modules/app_mysql.so
%{_libdir}/asterisk/modules/cdr_mysql.so
%{_libdir}/asterisk/modules/res_config_mysql.so
%endif

%files mwi-external
%{_libdir}/asterisk/modules/res_mwi_external.so
%{_libdir}/asterisk/modules/res_mwi_external_ami.so
%{_libdir}/asterisk/modules/res_stasis_mailbox.so

%if 0%{odbc}
%files odbc
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/func_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_odbc.conf
%{_libdir}/asterisk/modules/cdr_adaptive_odbc.so
%{_libdir}/asterisk/modules/cdr_odbc.so
%{_libdir}/asterisk/modules/cel_odbc.so
%{_libdir}/asterisk/modules/func_odbc.so
%{_libdir}/asterisk/modules/res_config_odbc.so
%{_libdir}/asterisk/modules/res_odbc.so
%{_libdir}/asterisk/modules/res_odbc_transaction.so
%endif

%if 0%{?ooh323}
%files ooh323
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ooh323.conf
%{_libdir}/asterisk/modules/chan_ooh323.so
%endif

%files oss
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/oss.conf
%{_libdir}/asterisk/modules/chan_oss.so

%if 0%{phone}
%files phone
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phone.conf
%{_libdir}/asterisk/modules/chan_phone.so
%endif

%files pjsip
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/pjsip.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/pjproject.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/pjsip_notify.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/pjsip_wizard.conf
%{_libdir}/asterisk/modules/chan_pjsip.so
%{_libdir}/asterisk/modules/func_pjsip_aor.so
%{_libdir}/asterisk/modules/func_pjsip_contact.so
%{_libdir}/asterisk/modules/func_pjsip_endpoint.so
%{_libdir}/asterisk/modules/res_pjsip.so
%{_libdir}/asterisk/modules/res_pjsip_acl.so
%{_libdir}/asterisk/modules/res_pjsip_authenticator_digest.so
%{_libdir}/asterisk/modules/res_pjsip_caller_id.so
%{_libdir}/asterisk/modules/res_pjsip_config_wizard.so
%{_libdir}/asterisk/modules/res_pjsip_dialog_info_body_generator.so
%{_libdir}/asterisk/modules/res_pjsip_dlg_options.so
%{_libdir}/asterisk/modules/res_pjsip_diversion.so
%{_libdir}/asterisk/modules/res_pjsip_dtmf_info.so
%{_libdir}/asterisk/modules/res_pjsip_empty_info.so
%{_libdir}/asterisk/modules/res_pjsip_endpoint_identifier_anonymous.so
%{_libdir}/asterisk/modules/res_pjsip_endpoint_identifier_ip.so
%{_libdir}/asterisk/modules/res_pjsip_endpoint_identifier_user.so
%{_libdir}/asterisk/modules/res_pjsip_exten_state.so
%{_libdir}/asterisk/modules/res_pjsip_header_funcs.so
%{_libdir}/asterisk/modules/res_pjsip_history.so
%{_libdir}/asterisk/modules/res_pjsip_logger.so
%{_libdir}/asterisk/modules/res_pjsip_messaging.so
#%%{_libdir}/asterisk/modules/res_pjsip_multihomed.so
%{_libdir}/asterisk/modules/res_pjsip_mwi.so
%{_libdir}/asterisk/modules/res_pjsip_mwi_body_generator.so
%{_libdir}/asterisk/modules/res_pjsip_nat.so
%{_libdir}/asterisk/modules/res_pjsip_notify.so
%{_libdir}/asterisk/modules/res_pjsip_one_touch_record_info.so
%{_libdir}/asterisk/modules/res_pjsip_outbound_authenticator_digest.so
%{_libdir}/asterisk/modules/res_pjsip_outbound_publish.so
%{_libdir}/asterisk/modules/res_pjsip_outbound_registration.so
%{_libdir}/asterisk/modules/res_pjsip_path.so
%{_libdir}/asterisk/modules/res_pjsip_phoneprov_provider.so
%{_libdir}/asterisk/modules/res_pjsip_pidf_body_generator.so
%{_libdir}/asterisk/modules/res_pjsip_pidf_digium_body_supplement.so
%{_libdir}/asterisk/modules/res_pjsip_pidf_eyebeam_body_supplement.so
%{_libdir}/asterisk/modules/res_pjsip_publish_asterisk.so
%{_libdir}/asterisk/modules/res_pjsip_pubsub.so
%{_libdir}/asterisk/modules/res_pjsip_refer.so
%{_libdir}/asterisk/modules/res_pjsip_registrar.so
#%%{_libdir}/asterisk/modules/res_pjsip_registrar_expire.so
%{_libdir}/asterisk/modules/res_pjsip_rfc3326.so
%{_libdir}/asterisk/modules/res_pjsip_sdp_rtp.so
%{_libdir}/asterisk/modules/res_pjsip_send_to_voicemail.so
%{_libdir}/asterisk/modules/res_pjsip_session.so
%{_libdir}/asterisk/modules/res_pjsip_sips_contact.so
%{_libdir}/asterisk/modules/res_pjsip_stir_shaken.so
%{_libdir}/asterisk/modules/res_pjsip_t38.so
#%%{_libdir}/asterisk/modules/res_pjsip_transport_management.so
%{_libdir}/asterisk/modules/res_pjsip_transport_websocket.so
%{_libdir}/asterisk/modules/res_pjsip_xpidf_body_generator.so

%files portaudio
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/console.conf
%{_libdir}/asterisk/modules/chan_console.so

%if 0%{postgresql}
%files postgresql
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pgsql.conf
%doc contrib/realtime/postgresql/*.sql
%{_libdir}/asterisk/modules/cdr_pgsql.so
%{_libdir}/asterisk/modules/cel_pgsql.so
%{_libdir}/asterisk/modules/res_config_pgsql.so
%endif

%if 0%{radius}
%files radius
%{_libdir}/asterisk/modules/cdr_radius.so
%{_libdir}/asterisk/modules/cel_radius.so
%endif

%files sip
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip_notify.conf
%{_libdir}/asterisk/modules/chan_sip.so

%files skinny
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/skinny.conf
%{_libdir}/asterisk/modules/chan_skinny.so

%if 0%{snmp}
%files snmp
#doc doc/asterisk-mib.txt
#doc doc/digium-mib.txt
#doc doc/snmp.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
#%%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
#%%{_datadir}/snmp/mibs/DIGIUM-MIB.txt
%{_libdir}/asterisk/modules/res_snmp.so
%endif

%files sqlite
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_sqlite3_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_sqlite.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_sqlite3.conf
%{_libdir}/asterisk/modules/cdr_sqlite3_custom.so
%{_libdir}/asterisk/modules/cel_sqlite3_custom.so
%{_libdir}/asterisk/modules/res_config_sqlite3.so

%files tds
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_tds.conf
%{_libdir}/asterisk/modules/cdr_tds.so
%{_libdir}/asterisk/modules/cel_tds.so

%files unistim
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/unistim.conf
%{_libdir}/asterisk/modules/chan_unistim.so

%files voicemail
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/voicemail.conf
%{_libdir}/asterisk/modules/func_vmcount.so

%if 0%{?imap}
%files voicemail-imap
%{_libdir}/asterisk/modules/app_directory_imap.so
%{_libdir}/asterisk/modules/app_voicemail_imap.so
%endif

%files voicemail-odbc
#doc doc/voicemail_odbc_postgresql.txt
%{_libdir}/asterisk/modules/app_directory_odbc.so
%{_libdir}/asterisk/modules/app_voicemail_odbc.so

%files voicemail-plain
%{_libdir}/asterisk/modules/app_directory_plain.so
%{_libdir}/asterisk/modules/app_voicemail_plain.so

%if 0%{?xmpp}
%files xmpp
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/motif.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/xmpp.conf
%{_libdir}/asterisk/modules/chan_motif.so
%{_libdir}/asterisk/modules/res_xmpp.so
%endif

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 18.12.1-1.14
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 18.12.1-1.13
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 24 2024 Zhengyu He <hezhy472013@gmail.com> - 18.12.1-1.11
- Do not use -m32/-m64 on riscv64
- Fix pjproject build failure on RISC-V

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 18.12.1-1.10
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 18.12.1-1.9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Florian Weimer <fweimer@redhat.com> - 18.12.1-1.5
- Backport upstream patch to fix C compatibility issue

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Kalev Lember <klember@redhat.com> - 18.12.1-1.2
- Build against newer gmime 3.0 instead of 2.6

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.12.1-1
- Update to upstream 18.12.1 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.11.2-1
- Update to upstream 18.11.2 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.10.1-1
- Update to upstream 18.10.1 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.9.0-1
- Update to upstream 18.9.0 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.8.0-1
- Update to upstream 18.8.0 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.7.1-1
- Update to upstream 18.7.1 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.6.0-1
- Update to upstream 18.6.0 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.5.1-1
- Update to upstream 18.5.1 release.

* Wed Jun 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 18.4.0-1.6
- Fix build (#1977579)

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 18.4.0-1.5
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.4.0-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 18.4.0-1.3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.4.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 18.4.0-1.1
- Perl 5.34 rebuild

* Mon May 10 2021 Jared K. Smith <jsmith@fedoraproject.org> - 18.4.0-1
- Update to upstream 18.4.0 release for bug fixes

* Mon Apr 12 2021 Jared K Smith <jsmith@fedoraproject.org> - 18.3.0-1
- Update to upstream 18.3.0 release for security updates and bug fixes

* Thu Feb 18 2021 Jared K. Smith <jsmith@fedoraproject.org> - 18.2.1-1
- Update to upstream 18.2.1 release for security updates, related to:
- AST-2021-001/CVE-2020-35776: Remote crash in res_pjsip_diversion
- AST-2021-002/CVE-2021-26717: Remote crash possible when negotiating T.38
- AST-2021-003/CVE-2021-26712: Remote attacker could prematurely tear down SRTP calls
- AST-2021-004/CVE-2021-26714: An unsuspecting user could crash Asterisk with multiple hold/unhold requests
- AST-2021-005/CVE-2021-26906: Remote Crash Vulnerability in PJSIP channel driver

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 18.2.0-1.2
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jared K. Smith <jsmith@fedoraproject.org> - 18.2.0-1
- Update to upstream 18.2.0 release for security fixes, bug fixes, and features

* Thu Nov 19 2020 Jared K. Smith <jsmith@fedoraproject.org> - 18.1.0-1
- Update to upstream 18.1.0 release for bug fixes and features

* Mon Nov  9 2020 Jared K. Smith <jsmith@fedoraproject.org> - 18.0.1-2
- Add dependency on sox

* Thu Nov  5 2020 Jared K. Smith <jsmith@fedoraproject.org> - 18.0.1-1
- Update to 18.0.1 release for AST-2020-001 and AST-2020-002 security fixes

* Tue Oct 20 2020 Jared K. Smith <jsmith@fedoraproject.org> - 18.0.0-1
- Update to upstream 18.0.0 release for new features

* Thu Sep 03 2020 Josef Řídký <jridky@redhat.com> - 17.7.0-2
- Rebuilt for new net-snmp release

* Thu Sep 03 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.7.0-1
- Update to upstream 17.7.0 release

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 17.5.0-2.3
- Rebuilt for new net-snmp release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.5.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 17.5.0-2.1
- Perl 5.32 rebuild
- Add missing source files

* Thu May 28 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.5.0-0.rc1.1
- Update to upststream 7.5.0-rc1 release for testing

* Fri May 08 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.4.0-2
- app_page no longer depends on app_meetme

* Thu Apr 30 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.4.0-1
- Update to upstream 7.4.0 release for bug fixes

* Tue Apr 28 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.4.0-0.rc2.1
- Update to upstream 7.4.0-rc2

* Sat Apr 25 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.4.0-0.rc1.1
- Update to upstream 7.4.0 RC 1 

* Thu Mar 12 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.3.0-1
- Update to upstream 7.3.0 release for bug fixes

* Tue Feb 11 2020 Jared K. Smith <jsmith@fedoraproject.org> - 17.2.0-1
- Update to upstream 7.2.0 release for bug fixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.2.0-0.rc1.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Tom Callaway <spot@fdoraproject.org> - 17.1.0-2
- rebuild for libsrtp2

* Mon Dec 23 2019 Jared K. Smith <jsmith@fedoraproject.org> - 17.1.0-1
- Update to upstream 17.1.0 release for security and bug fixes

* Thu Dec 12 2019 Jared K. Smith <jsmith@fedoraproject.org> - 17.1.0-0.rc1.1
- Update to upstream 17.1.0 pre-release for security and bug fixes

* Fri Nov 22 2019 Jared K. Smith <jsmith@fedoraproject.org> - 17.0.1-1
- Update to upstream 17.0.1 release for AST-2019-006, AST-2019-007, AST-2019-008
  security updates

* Fri Nov 15 2019 Jared K. Smith <jsmith@fedoraproject.org> - 17.0.0-2
- Move from python2 to python3

* Mon Oct 28 2019 Jared K. Smith <jsmith@fedoraproject.org> - 17.0.0-1
- Update to upstream 17.0.0 release for new features

* Fri Oct 18 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.6.1-1
- Update to upstream 16.6.1 for bug fixes
- Work on building in EPEL-7 and EPEL-8

* Wed Oct 09 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.6.0-1
- Update to upstream 16.6.0 for security and bug fixes
- Update to using bundled pjproject release 2.9

* Fri Sep 06 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.5.1-1
- Update for upstream security release 16.5.1, with AST-2019-004 and
  AST-2019-005

* Thu Jul 25 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.5.0-1
- Update to upstream 16.5.0 release for security and bug fixes

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.4.1-1
- Update to upstream 16.4.1 release for security updates AST-2019-002 and
  AST-2019-003 related to remote crash vulnerabilities

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 16.4.0-2
- Perl 5.30 rebuild

* Fri May 31 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.4.0-1
- Update to upstream 16.4.0 release for bug fixes

* Fri Mar 01 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.2.1-1
- Update to upstream 16.2.1 release for security / CVE-2019-7251 / AST-2019-001

* Fri Feb 15 2019 Jared K. Smith <jsmith@fedoraproject.org> - 16.2.0-1
- Update to upstream 16.2.0 release for bug fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 16.1.0-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jan 12 2019 Björn Esser <besser82@fedoraproject.org> - 16.1.0-2
- Add patch to explicitly use python2 shebangs

* Wed Dec 12 2018 Jared Smith <jsmith@fedoraproject.org> - 16.1.0-1
- Update to upstream 16.1.0 security release

* Wed Nov 14 2018 Jared Smith <jsmith@fedoraproject.org> - 16.0.1-1
- Update to upstream 16.0.1 security release

* Tue Oct 09 2018 Jared Smith - 16.0.0-1
- Update to upstream 16.0.0 release

* Thu Jul 12 2018 Jared K. Smith <jsmith@fedoraproject.org> - 15.5.0-1
- Update to upstream 15.5.0 release for security and bug fixes

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 15.4.1-2
- Perl 5.28 rebuild

* Tue Jun 12 2018 Jared K. Smith <jsmith@fedoraproject.org> - 15.4.1-1
- Update to upstream 15.4.1 release for AST-2018-007 and AST-2018-008 security
  issues

* Sun May 06 2018 Jared K. Smith <jsmith@fedoraproject.org> - 15.4.0-1
- Update to upstream 15.4.0 release

* Thu Mar 15 2018 jsmith <jsmith.fedora@gmail.com> - 15.3.0-1
- Update to upstream 15.3.0 release

* Mon Mar 05 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.2-2
- Update asterisk.service to wait for the network to come up

* Thu Feb 22 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.2-1
- Update to upstream 15.2.2 release for security updates
- This update addresses security alerts AST-2018-001 through AST-2018-006
- Upstream changelog at https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-15.2.2

* Tue Feb 20 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.1-3
- Verify GPG signatures on source packages

* Mon Feb 19 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.1-2
- Add missing BuildRequires on gcc/gcc-c++

* Tue Feb 13 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.1-1
- Update to upstream 15.2.1 release

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 15.2.0-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.0-3
- Update requirements for systemd

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 15.2.0-2
- Rebuilt for switch to libxcrypt

* Thu Jan 11 2018 Jared Smith <jsmith@fedoraproject.org> - 15.2.0-1
- Update to upstream 15.2.0 release
- Upstream changelog at http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-15.2.0

* Wed Dec 27 2017 Jared Smith - 15.1.5-1
- Update to upstream 15.1.5 release for AST-2017-014/CVE-2017-17850 security
  issue

* Thu Dec 14 2017 Jared Smith <jsmith@fedoraproject.org> - 15.1.4-2
- Require mariadb-connector-c-devel, see RHBZ#1488483

* Wed Dec 13 2017 Jared Smith <jsmith@fedoraproject.org> - 15.1.4-1
- Update to upstream 15.1.4 release for AST-2017-012 security issue

* Tue Dec 05 2017 Jared Smith <jsmith@fedoraproject.org> - 15.1.3-1
- Update to upstream 15.1.3 release for security issue AST-2017-013

* Fri Nov 10 2017 Jared Smith <jsmith@fedoraproject.org> - 15.1.2-1
- Update to upstream 15.1.2 release

* Fri Nov 10 2017 Jared Smith <jsmith@fedoraproject.org> - 15.1.1-1
- Update to upstream 15.1.1 release for AST-2017-09, AST-2017-010, and
  AST-2017-011 security updates

* Tue Oct 31 2017 Jared Smith <jsmith@fedoraproject.org> - 15.1.0-1
- Update to upstream 15.1.0 release

* Thu Oct 05 2017 Jared Smith <jsmith@fedoraproject.org> - 15.0.0-1
- Update to upstream 15.0.0 release

* Thu Sep 21 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.2-1
- Update to upstream 14.6.2 release

* Wed Sep 13 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.1-6
- Re-enable corosync, see RHBZ#1478089

* Sun Sep 03 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.1-5
- Add dependency on unbound-devel for res_resolver_unbound

* Fri Sep 01 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.1-4
- Disable corosync modules until corosync works in ppc64le again

* Fri Sep 01 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.1-3
- Fix MySQL header path (due to change in mariadb-devel patckage)

* Fri Sep 01 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.1-1
- Update to upstream 14.6.1 release
- Solves AST-2017-005, AST-2017-006, and AST-2017-007 security issues

* Fri Sep 01 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.0-2
- Add perl to BuildRequires

* Thu Aug 31 2017 Jared Smith <jsmith@fedoraproject.org> - 14.6.0-1
- Update to upstream 14.6.0 release
- Re-enable radius sub-packages

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Till Maas <opensource@till.name> - 14.5.0-2
- Excludearch s390x

* Sat Jun 10 2017 Jared Smith <jsmith@fedoraproject.org> - 14.5.0-1
- Update to upstream 14.5.0 release

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 13.11.2-1.2
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.11.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Jared Smith <jsmith@fedoraproject.org> - 13.11.2-1
- Update to upstream 13.11.2 bug-fix release

* Fri Sep 09 2016 Jared Smith <jsmith@fedoraproject.org> - 13.11.1-1
- Stop building the -radius subpackage, due to orphaned freeradius-client dependency
- Update to upstream 13.11.1 security release for AST-2016-006 and AST-2016-007

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 13.9.1-1.1
- Perl 5.24 rebuild

* Sat May 14 2016 Jared Smith <jsmith@fedoraproject.org> - 13.9.1-1
- Update to upstream 13.9.1 release
- Use bootstrap.sh instead of calling autoconf tools manually
- Fix up shifting pjproject submodules
- Fix up requires on speexdsp-devel for EPEL7 (RHBZ#1310444)

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 13.7.2-2.1
- Fix alembic requirement

* Tue Feb 09 2016 Michal Toman <mtoman@fedoraproject.org> - 13.7.2-2
- Do not use -m32/-m64 on MIPS

* Sun Feb 07 2016 Jared Smith <jsmith@fedoraproject.org> - 13.7.2-1
- Update to upstream release 13.7.2 to fix ASTERISK-25702

* Fri Feb 05 2016 Jared Smith <jsmith@fedoraproject.org> - 13.7.1-2
- Create sub-package for alembic scripts

* Thu Feb 04 2016 Jared Smith <jsmith@fedoraproject.org> - 13.7.1-1
- Update to upstream 13.7.1 release for security fixes
- Resolves AST-2016-001: BEAST vulnerability in HTTP server
- Resolves AST-2016-002: File descriptor exhaustion in chan_sip
- Resolves AST-2016-003: Remote crash vulnerability receiving UDPTL FAX data
- Full changelog at http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.7.1
- Also build the 'radius' sub-package against freeradius-client-devel, as the
 radiusclient-ng project is dead

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.2-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jared Smith <jsmith@fedoraproject.org> - 13.3.2-3
- Remove %%defattr macro invocations, as they are no longer needed

* Sat Jan 23 2016 Robert Scheck <robert@fedoraproject.org> - 13.3.2-2
- Rebuild for libical 2.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.3.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 13.3.2-1.1
- Perl 5.22 rebuild

* Thu Apr  9 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.3.2-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.28, 11.6, and 13.1 and Asterisk 1.8, 11, 12, and 13. The available
- security releases are released as versions 1.8.28.cert-5, 1.8.32.3, 11.6-cert11,
- 11.17.1, 12.8.2, 13.1-cert2, and 13.3.2.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolves the following security vulnerability:
-
- * AST-2015-003: TLS Certificate Common name NULL byte exploit
-
-   When Asterisk registers to a SIP TLS device and and verifies the server,
-   Asterisk will accept signed certificates that match a common name other than
-   the one Asterisk is expecting if the signed certificate has a common name
-   containing a null byte after the portion of the common name that Asterisk
-   expected. This potentially allows for a man in the middle attack.
-
- For more information about the details of this vulnerability, please read
- security advisory AST-2015-003, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.28-cert5
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.32.3
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert11
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.17.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.8.2
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-13.1-cert2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.3.2
-
- The security advisory is available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2015-003.pdf

* Thu Apr  9 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.3.1-1:
- The Asterisk Development Team has announced the release of Asterisk 13.3.1.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 13.3.1 resolves an issue reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is the issue resolved in this release:
-
- * --- pjsip: resolve compatibility problem with ast_sip_session
-   (Closes issue ASTERISK-24941. Reported by Matt Jordan)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-13.3.1

* Wed Apr  1 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.3.0-1:
- The Asterisk Development Team has announced the release of Asterisk 13.3.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 13.3.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- New Features made in this release:
- -----------------------------------
-  * ASTERISK-24703 - ARI: Add the ability to "transfer" (redirect) a
-       channel (Reported by Matt Jordan)
-  * ASTERISK-17899 - Handle crypto lifetime in SDES-SRTP negotiation
-       (Reported by Dwayne Hubbard)
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-24616 - Crash in res_format_attr_h264 due to invalid
-       string copy (Reported by Yura Kocyuba)
-  * ASTERISK-24748 - res_pjsip: If wizards explicitly configured in
-       sorcery.conf false ERROR messages may occur (Reported by Joshua
-       Colp)
-  * ASTERISK-24769 - res_pjsip_sdp_rtp: Local ICE candidates leaked
-       (Reported by Matt Jordan)
-  * ASTERISK-24742 - [patch] Fix ast_odbc_find_table function in
-       res_odbc (Reported by ibercom)
-  * ASTERISK-24479 - Enable REF_DEBUG for module references
-       (Reported by Corey Farrell)
-  * ASTERISK-24701 - Stasis: Write timeout on WebSocket fails to
-       fully disconnect underlying socket, leading to events being
-       dropped with no additional information (Reported by Matt Jordan)
-  * ASTERISK-24772 - ODBC error in realtime sippeers when device
-       unregisters under MariaDB (Reported by Richard Miller)
-  * ASTERISK-24752 - Crash in bridge_manager_service_req when bridge
-       is destroyed by ARI during shutdown (Reported by Richard
-       Mudgett)
-  * ASTERISK-24741 - dtls_handler causes Asterisk to crash (Reported
-       by Zane Conkle)
-  * ASTERISK-24015 - app_transfer fails with PJSIP channels
-       (Reported by Private Name)
-  * ASTERISK-24727 - PJSIP: Crash experienced during multi-Asterisk
-       transfer scenario. (Reported by Mark Michelson)
-  * ASTERISK-24771 - ${CHANNEL(pjsip)} - segfault (Reported by
-       Niklas Larsson)
-  * ASTERISK-24716 - Improve pjsip log messages for presence
-       subscription failure (Reported by Rusty Newton)
-  * ASTERISK-24612 - res_pjsip: No information if a required sorcery
-       wizard is not loaded (Reported by Joshua Colp)
-  * ASTERISK-24768 - res_timing_pthread: file descriptor leak
-       (Reported by Matthias Urlichs)
-  * ASTERISK-24685 - "pjsip show version" CLI command (Reported by
-       Joshua Colp)
-  * ASTERISK-24632 - install_prereq script installs pjproject
-       without IPv6 support (Reported by Rusty Newton)
-  * ASTERISK-24085 - Documentation - We should remove or further
-       document the 'contact' section in pjsip.conf (Reported by Rusty
-       Newton)
-  * ASTERISK-24791 - Crash in ast_rtcp_write_report (Reported by
-       JoshE)
-  * ASTERISK-24700 - CRASH: NULL channel is being passed to
-       ast_bridge_transfer_attended() (Reported by Zane Conkle)
-  * ASTERISK-24451 - chan_iax2: reference leak in sched_delay_remove
-       (Reported by Corey Farrell)
-  * ASTERISK-24799 - [patch] make fails with undefined reference to
-       SSLv3_client_method (Reported by Alexander Traud)
-  * ASTERISK-22670 - Asterisk crashes when processing ISDN AoC
-       Events (Reported by klaus3000)
-  * ASTERISK-24689 - Segfault on hangup after outgoing PRI-Euroisdn
-       call (Reported by Marcel Manz)
-  * ASTERISK-24740 - [patch]Segmentation fault on aoc-e event
-       (Reported by Panos Gkikakis)
-  * ASTERISK-24787 - [patch] - Microsoft exchange incompatibility
-       for playing back messages stored in IMAP - play_message: No
-       origtime (Reported by Graham Barnett)
-  * ASTERISK-24814 - asterisk/lock.h: Fix syntax errors for non-gcc
-       OSX with 64 bit integers (Reported by Corey Farrell)
-  * ASTERISK-24796 - Codecs and bucket schema's prevent module
-       unload (Reported by Corey Farrell)
-  * ASTERISK-24724 - 'httpstatus' Web Page Produces Incomplete HTML
-       (Reported by Ashley Sanders)
-  * ASTERISK-24499 - Need more explicit debug when PJSIP dialstring
-       is invalid (Reported by Rusty Newton)
-  * ASTERISK-24785 - 'Expires' header missing from 200 OK on
-       REGISTER (Reported by Ross Beer)
-  * ASTERISK-24677 - ARI GET variable on channel provides unhelpful
-       response on non-existent variable (Reported by Joshua Colp)
-  * ASTERISK-24797 - bridge_softmix: G.729 codec license held
-       (Reported by Kevin Harwell)
-  * ASTERISK-24812 - ARI: Creating channels through /channels
-       resource always uses SLIN, which results in unneeded transcoding
-       (Reported by Matt Jordan)
-  * ASTERISK-24800 - Crash in __sip_reliable_xmit due to invalid
-       thread ID being passed to pthread_kill (Reported by JoshE)
-  * ASTERISK-17721 - Incoming SRTP calls that specify a key lifetime
-       fail (Reported by Terry Wilson)
-  * ASTERISK-23214 - chan_sip WARNING message 'We are requesting
-       SRTP for audio, but they responded without it' is ambiguous and
-       wrong in some cases (Reported by Rusty Newton)
-  * ASTERISK-15434 - [patch] When ast_pbx_start failed, both an
-       error response and BYE are sent to the caller (Reported by
-       Makoto Dei)
-  * ASTERISK-18105 - most of asterisk modules are unbuildable in
-       cygwin environment (Reported by feyfre)
-  * ASTERISK-24828 - Fix Frame Leaks (Reported by Kevin Harwell)
-  * ASTERISK-24751 - Integer values in json payload to ARI cause
-       asterisk to crash (Reported by jeffrey putnam)
-  * ASTERISK-24838 - chan_sip: Locking inversion occurs when
-       building a peer causes a peer poke during request handling
-       (Reported by Richard Mudgett)
-  * ASTERISK-24825 - Caller ID not recognized using
-       Centrex/Distinctive dialing (Reported by Richard Mudgett)
-  * ASTERISK-24830 - res_rtp_asterisk.c checks USE_PJPROJECT not
-       HAVE_PJPROJECT (Reported by Stefan Engström)
-  * ASTERISK-24840 - res_pjsip: conflicting endpoint identifiers
-       (Reported by Kevin Harwell)
-  * ASTERISK-24755 - Asterisk sends unexpected early BYE to
-       transferrer during attended transfer when using a Stasis bridge
-       (Reported by John Bigelow)
-  * ASTERISK-24739 - [patch] - Out of files -- call fails --
-       numerous files with inodes from under /usr/share/zoneinfo,
-       mostly posixrules (Reported by Ed Hynan)
-  * ASTERISK-23390 - NewExten Event with application AGI shows up
-       before and after AGI runs (Reported by Benjamin Keith Ford)
-  * ASTERISK-24786 - [patch] - Asterisk terminates when playing a
-       voicemail stored in LDAP (Reported by Graham Barnett)
-  * ASTERISK-24808 - res_config_odbc: Improper escaping of
-       backslashes occurs with MySQL (Reported by Javier Acosta)
-  * ASTERISK-24807 - Missing mandatory field Max-Forwards (Reported
-       by Anatoli)
-  * ASTERISK-20850 - [patch]Nested functions aren't portable.
-       Adapting RAII_VAR to use clang/llvm blocks to get the
-       same/similar functionality. (Reported by Diederik de Groot)
-  * ASTERISK-24872 - [patch] AMI PJSIPShowEndpoint closes AMI
-       connection on error (Reported by Dmitriy Serov)
-  * ASTERISK-19470 - Documentation on app_amd is incorrect (Reported
-       by Frank DiGennaro)
-  * ASTERISK-21038 - Bad command completion of "core set debug
-       channel" (Reported by Richard Kenner)
-  * ASTERISK-18708 - func_curl hangs channel under load (Reported by
-       Dave Cabot)
-  * ASTERISK-16779 - Cannot disallow unknown format '' (Reported by
-       Atis Lezdins)
-  * ASTERISK-24876 - Investigate reference leaks from
-       tests/channels/local/local_optimize_away (Reported by Corey
-       Farrell)
-  * ASTERISK-24882 - chan_sip: Improve usage of REF_DEBUG (Reported
-       by Corey Farrell)
-  * ASTERISK-24817 - init_logger_chain: unreachable code block
-       (Reported by Corey Farrell)
-  * ASTERISK-24880 - [patch]Compilation under OpenBSD  (Reported by
-       snuffy)
-  * ASTERISK-24879 - [patch]Compilation fails due to 64bit time
-       under OpenBSD (Reported by snuffy)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-24745 - [patch]Add no_answer to ARI hangup causes
-       (Reported by Ben Merrills)
-  * ASTERISK-24811 - asterisk-publication sorcery object does not
-       use realtime (Reported by Matt Hoskins)
-  * ASTERISK-24790 - Reduce spurious noise in logs from voicemail -
-       Couldn't find mailbox %%s in context (Reported by Graham Barnett)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-13.3.0

* Wed Apr  1 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.2.0-1:
- The Asterisk Development Team has announced the release of Asterisk 13.2.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 13.2.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-24342 - PJSIP: Qualifying endpoints attempts to do them
-       all at the same time. (Reported by Richard Mudgett)
-  * ASTERISK-24514 - res_pjsip_outbound_registration: stack overflow
-       when using non-default sorcery wizard (Reported by Kevin
-       Harwell)
-  * ASTERISK-24472 - Asterisk Crash in OpenSSL when calling over WSS
-       from JSSIP (Reported by Badalian Vyacheslav)
-  * ASTERISK-24607 - res_pjsip_session: re-INVITE with declined
-       media streams results in 488 (Reported by Matt Jordan)
-  * ASTERISK-24563 - Direct Media calls within private network
-       sometimes get one way audio (Reported by Kevin Harwell)
-  * ASTERISK-24604 - res_rtp_asterisk: Crash during restart due to
-       race condition in accessing codec in stored ast_frame and codec
-       core (Reported by Matt Jordan)
-  * ASTERISK-24614 - Deadlock when DEBUG_THREADS compiler flag
-       enabled (Reported by Richard Mudgett)
-  * ASTERISK-24449 - Reinvite for T.38 UDPTL fails if SRTP is
-       enabled (Reported by Andreas Steinmetz)
-  * ASTERISK-24619 - [patch]Gcc 4.10 fixes in r413589 (1.8) wrongly
-       casts char to unsigned int (Reported by Walter Doekes)
-  * ASTERISK-24536 - AMI redirect with PJSIP fails to move extra
-       channel (Reported by Niklas Larsson)
-  * ASTERISK-24459 - bridge_native_rtp: Native RTP bridging is
-       chosen for RTP compatible channels when the DTMF mode is not
-       compatible (Reported by Yaniv Simhi)
-  * ASTERISK-24337 - Spammy DEBUG message needs to be at a higher
-       level - 'Remote address is null, most likely RTP has been
-       stopped' (Reported by Rusty Newton)
-  * ASTERISK-24513 - Local channel apparently leaked in off-nominal
-       DTMF attended transfer (Reported by Mark Michelson)
-  * ASTERISK-23733 - 'reload acl' fails if acl.conf is not present
-       on startup (Reported by Richard Kenner)
-  * ASTERISK-24628 - [patch] chan_sip - CANCEL is sent to wrong
-       destination when 'sendrpid=yes' (in proxy environment) (Reported
-       by Karsten Wemheuer)
-  * ASTERISK-23841 - DTMF atxfer doesn't set CallerID for the recall
-       calls to the transferrer. (Reported by Richard Mudgett)
-  * ASTERISK-24376 - res_pjsip_refer: REFER request for remote
-       session attempts to direct channel to external_replaces
-       extension instead of context, without providing for the
-       Referred-To SIP URI (Reported by Matt Jordan)
-  * ASTERISK-24591 - Stasis() side of an ARI originated channel
-       cannot be Redirected (Reported by Kinsey Moore)
-  * ASTERISK-24049 - Asterisk Manager Interface: A number of list
-       type responses aren't using astman_send_listack (Reported by
-       Jonathan Rose)
-  * ASTERISK-24637 - Channel re-enters Stasis() when it should not
-       (Reported by John Bigelow)
-  * ASTERISK-24474 - sip_to_pjsip.py lacks documentation and does
-       not function (Reported by John Kiniston)
-  * ASTERISK-24672 - [PATCH] Memory leak in func_curl CURLOPT
-       (Reported by Kristian Høgh)
-  * ASTERISK-20744 - [patch] Security event logging does not work
-       over syslog (Reported by Michael Keuter)
-  * ASTERISK-24665 - Configure check required for
-       pjsip_get_dest_info() (Reported by Mark Michelson)
-  * ASTERISK-23850 - Park Application does not respect Return
-       Context Priority (Reported by Andrew Nagy)
-  * ASTERISK-23991 - [patch]asterisk.pc file contains a small error
-       in the CFlags returned (Reported by Diederik de Groot)
-  * ASTERISK-24655 - res_pjsip_outbound_publish: Hang on shutdown
-       while attempting to publish (Reported by Kevin Harwell)
-  * ASTERISK-24485 - res_pjsip cannot be unloaded or shutdown
-       (Reported by Corey Farrell)
-  * ASTERISK-24663 - [patch] Unnamed semaphore autoconf check fails
-       on cross compilation (Reported by abelbeck)
-  * ASTERISK-24624 - Transfer to invalid extension results in hung
-       channel. (Reported by Zane Conkle)
-  * ASTERISK-24615 - When Multiple Transports Exist in pjsip.conf,
-       Incorrect External Addresses is Used in SIP Packets When
-       Responding to INVITE (Reported by David Justl)
-  * ASTERISK-24288 - [patch] - ODBC usage with app_voicemail -
-       voicemail is not deleted after review, hangup (Reported by LEI
-       FU)
-  * ASTERISK-24048 - [patch] contrib/scripts/install_prereq selects
-       32-bit packages on 64-bit hosts (Reported by Ben Klang)
-  * ASTERISK-24600 - Stuck IAX channels, Asterisk stops responding
-       to most traffic, potential deadlock (Reported by Jeff Collell)
-  * ASTERISK-24560 - Creating a named ARI bridge twice causes a
-       crash (Reported by Kinsey Moore)
-  * ASTERISK-24682 - app_dial: Multiple DialEnd events emitted when
-       MACRO_RESULT or GOSUB_RESULT are an unexpected value (Reported
-       by Matt Jordan)
-  * ASTERISK-24640 - Registration pending stays forever after sip
-       reload (Reported by Max Man)
-  * ASTERISK-24673 - outgoing sip registers cannot be removed or
-       modified without doing restart (or doing module unload
-       chan_sip.so) (Reported by Stefan Engström)
-  * ASTERISK-24709 - [patch] msg_create_from_file used by MixMonitor
-       m() option does not queue an MWI event (Reported by Gareth
-       Palmer)
-  * ASTERISK-24649 - Pushing of channel into bridge fails; Stasis
-       fails to get app name (Reported by John Bigelow)
-  * ASTERISK-24355 - [patch] chan_sip realtime uses case sensitive
-       column comparison for 'defaultuser' (Reported by
-       HZMI8gkCvPpom0tM)
-  * ASTERISK-24693 - Investigate and fix memory leaks in Asterisk
-       (Reported by Kevin Harwell)
-  * ASTERISK-24626 - Voicemail passwords not being stored in ARA
-       (Reported by Paddy Grice)
-  * ASTERISK-24539 - Compile fails on OSX because of sem_timedwait
-       in bridge_channel.c (Reported by George Joseph)
-  * ASTERISK-24544 - Compile fails on OSX Yosemite because of
-       incorrect detection of htonll and ntohll (Reported by George
-       Joseph)
-  * ASTERISK-24723 - confbridge: CLI command 'confbridge list XXXX'
-       no longer displays user menus (Reported by Matt Jordan)
-  * ASTERISK-24721 - manager: ModuleLoad action incorrectly reports
-       'module not found' during a Reload operation (Reported by Matt
-       Jordan)
-  * ASTERISK-24719 - ConfBridge recording channels get stuck when
-       recording started/stopped more than once (Reported by Richard
-       Mudgett)
-  * ASTERISK-24715 - chan_sip: stale nonce causes failure (Reported
-       by Kevin Harwell)
-  * ASTERISK-24728 - tcptls: Bad file descriptor error when
-       reloading chan_sip (Reported by Kevin Harwell)
-  * ASTERISK-24729 - Outbound registration not occuring on new
-       registrations after reload. (Reported by Richard Mudgett)
-  * ASTERISK-24676 - Security Vulnerability: URL request injection
-       in libCURL (CVE-2014-8150) (Reported by Matt Jordan)
-  * ASTERISK-24666 - Security Vulnerability: RTP not closed after
-       sip call using unsupported codec (Reported by Y Ateya)
-  * ASTERISK-24711 - DTLS handshake broken with latest OpenSSL
-       versions (Reported by Jared Biel)
-  * ASTERISK-24646 - PJSIP changeset 4899 breaks TLS (Reported by
-       Stephan Eisvogel)
-  * ASTERISK-24736 - Memory Leak Fixes (Reported by Mark Michelson)
-  * ASTERISK-24635 - PJSIP outbound PUBLISH crashes when no response
-       is ever received (Reported by Marco Paland)
-  * ASTERISK-24737 - When agent not logged in, agent status shows
-       unavailable, queue status shows agent invalid (Reported by
-       Richard Mudgett)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-24552 - ARI: Allow associating a channel as an
-       initiator of an Origination for record keeping purposes
-       (Reported by Matt Jordan)
-  * ASTERISK-24553 - ARI/AMI: Include language in standard channel
-       snapshot output (Reported by Matt Jordan)
-  * ASTERISK-24643 - res_pjsip: Add user=phone option (Reported by
-       Matt Jordan)
-  * ASTERISK-24644 - res_pjsip_keepalive: Add keepalive module for
-       connection-oriented transports. (Reported by Matt Jordan)
-  * ASTERISK-24412 - [patch]Incomplete channel originate/continue
-       handling with ARI (Reported by Nir Simionovich (GreenfieldTech -
-       Israel))
-  * ASTERISK-24678 - [PATCH] Added atxfer* settings to
-       features.conf.sample (Reported by Niklas Larsson)
-  * ASTERISK-24575 - [patch]Make capath work for res_pjsip (Reported
-       by cloos)
-  * ASTERISK-24671 - Missing docs for the CDR AMI Event (Reported by
-       Dan Jenkins)
-  * ASTERISK-24316 - For httpd server, need option to define server
-       name for security purposes (Reported by Andrew Nagy)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-13.2.0

* Fri Jan 30 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.1.1-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.28 and 11.6 and Asterisk 1.8, 11, 12, and 13. The available
- security releases are released as versions 1.8.28.cert-4, 1.8.32.2, 11.6-cert10,
- 11.15.1, 12.8.1, and 13.1.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolves the following security vulnerabilities:
-
- * AST-2015-001: File descriptor leak when incompatible codecs are offered
-
-                 Asterisk may be configured to only allow specific audio or
-                 video codecs to be used when communicating with a
-                 particular endpoint. When an endpoint sends an SDP offer
-                 that only lists codecs not allowed by Asterisk, the offer
-                 is rejected. However, in this case, RTP ports that are
-                 allocated in the process are not reclaimed.
-
-                 This issue only affects the PJSIP channel driver in
-                 Asterisk. Users of the chan_sip channel driver are not
-                 affected.
-
- * AST-2015-002: Mitigation for libcURL HTTP request injection vulnerability
-
-                 CVE-2014-8150 reported an HTTP request injection
-                 vulnerability in libcURL. Asterisk uses libcURL in its
-                 func_curl.so module (the CURL() dialplan function), as well
-                 as its res_config_curl.so (cURL realtime backend) modules.
-
-                 Since Asterisk may be configured to allow for user-supplied
-                 URLs to be passed to libcURL, it is possible that an
-                 attacker could use Asterisk as an attack vector to inject
-                 unauthorized HTTP requests if the version of libcURL
-                 installed on the Asterisk server is affected by
-                 CVE-2014-8150.
-
- For more information about the details of these vulnerabilities, please read
- security advisory AST-2015-001 and AST-2015-002, which were released at the same
- time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.28-cert4
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.32.2
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert10
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.15.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.8.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.1.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2015-001.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2015-002.pdf

* Fri Jan 30 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.1.0-1
- The Asterisk Development Team has announced the release of Asterisk 13.1.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 13.1.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- New Features made in this release:
- -----------------------------------
-  * ASTERISK-24554 - AMI/ARI: Generate events on connected line
-       changes (Reported by Matt Jordan)
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-24436 - Missing header in res/res_srtp.c when compiling
-       against libsrtp-1.5.0 (Reported by Patrick Laimbock)
-  * ASTERISK-24455 - func_cdr: CDR_PROP leaks payload (Reported by
-       Corey Farrell)
-  * ASTERISK-24454 - app_queue: ao2_iterator not destroyed, causing
-       leak (Reported by Corey Farrell)
-  * ASTERISK-24430 - missing letter "p" in word response in
-       OriginateResponse event documentation (Reported by Dafi Ni)
-  * ASTERISK-24437 - Review implementation of ast_bridge_impart for
-       leaks and document proper usage (Reported by Scott Griepentrog)
-  * ASTERISK-24453 - manager: acl_change_sub leaks (Reported by
-       Corey Farrell)
-  * ASTERISK-24457 - res_fax: fax gateway frames leak (Reported by
-       Corey Farrell)
-  * ASTERISK-24458 - chan_phone fails to build on big endian systems
-       (Reported by Tzafrir Cohen)
-  * ASTERISK-21721 - SIP Failed to parse multiple Supported: headers
-       (Reported by Olle Johansson)
-  * ASTERISK-24304 - asterisk crashing randomly because of unistim
-       channel (Reported by dhanapathy sathya)
-  * ASTERISK-24190 - IMAP voicemail causes segfault (Reported by
-       Nick Adams)
-  * ASTERISK-24462 - res_pjsip: Stale qualify statistics after
-       disablementation (Reported by Kevin Harwell)
-  * ASTERISK-24465 - audiohooks list leaks reference to formats
-       (Reported by Corey Farrell)
-  * ASTERISK-24466 - app_queue: fix a couple leaks to struct
-       call_queue (Reported by Corey Farrell)
-  * ASTERISK-24432 - Install refcounter.py when REF_DEBUG is enabled
-       (Reported by Corey Farrell)
-  * ASTERISK-24411 - [patch] Status of outbound registration is not
-       changed upon unregistering. (Reported by John Bigelow)
-  * ASTERISK-24476 - main/app.c / app_voicemail: ast_writestream
-       leaks (Reported by Corey Farrell)
-  * ASTERISK-24480 - res_http_websockets: Module reference decrease
-       below zero (Reported by Corey Farrell)
-  * ASTERISK-24482 - func_talkdetect: Fix stasis message leak in
-       audiohook callback (Reported by Corey Farrell)
-  * ASTERISK-24487 - configuration: sections should be loadable as
-       template even when not marked (Reported by Scott Griepentrog)
-  * ASTERISK-20127 - [Regression] Config.c config_text_file_load()
-       unescapes semicolons ("\;" -> ";") turning them into comments
-       (corruption) on rewrite of a config file (Reported by George
-       Joseph)
-  * ASTERISK-24438 - res_pjsip_multihomed.so blocks Asterisk reload
-       when DNS settings invalid (Reported by Melissa Shepherd)
-  * ASTERISK-24307 - Unintentional memory retention in stringfields
-       (Reported by Etienne Lessard)
-  * ASTERISK-24491 - Memory leak in res_hep (Reported by Zane
-       Conkle)
-  * ASTERISK-24492 - main/file.c: ast_filestream sometimes causes
-       extra calls to ast_module_unref (Reported by Corey Farrell)
-  * ASTERISK-24447 - Bridge DTMF hooks: Audio doesn't pass when
-       waiting for more matching digits. (Reported by Richard Mudgett)
-  * ASTERISK-24257 - agent must dial acceptdtmf twice to bridge to
-       queue caller (Reported by Steve Pitts)
-  * ASTERISK-24504 - chan_console: Fix reference leaks to pvt
-       (Reported by Corey Farrell)
-  * ASTERISK-24250 - [patch] Voicemail with multi-recipients To:
-       header fix (Reported by abelbeck)
-  * ASTERISK-24468 - Incoming UCS2 encoded SMS truncated if SMS
-       length exceeds 50 (roughly) national symbols (Reported by
-       Dmitriy Bubnov)
-  * ASTERISK-24500 - Regression introduced in chan_mgcp by SVN
-       revision r227276 (Reported by Xavier Hienne)
-  * ASTERISK-24505 - manager: http connections leak references
-       (Reported by Corey Farrell)
-  * ASTERISK-24502 - Build fails when dev-mode, dont optimize and
-       coverage are enabled (Reported by Corey Farrell)
-  * ASTERISK-24444 - PBX: Crash when generating extension for
-       pattern matching hint (Reported by Leandro Dardini)
-  * ASTERISK-24489 - Crash: Asterisk crashes when converting RTCP
-       packet to JSON for res_hep_rtcp and report blocks are greater
-       than 1 (Reported by Gregory Malsack)
-  * ASTERISK-24498 - Segmentation fault in res_hep_rtcp on attended
-       transfer (Reported by Beppo Mazzucato)
-  * ASTERISK-24501 - ARI: Moving a channel between bridges followed
-       by a hangup can cause an ARI client to not receive an expected
-       ChannelLeftBridge event before StasisEnd (Reported by Matt
-       Jordan)
-  * ASTERISK-24336 - PJSIP timer_min_se value under 90 causes crash
-       (Reported by Leon Rowland)
-  * ASTERISK-23651 - Reloading some modules that are loaded already,
-       results in 'No such module' before a successful reload (Reported
-       by Rusty Newton)
-  * ASTERISK-24522 - ConfBridge: delay occurs between kicking all
-       endmarked users when last marked user leaves (Reported by Matt
-       Jordan)
-  * ASTERISK-15242 - transmit_refer leaks sip_refer structures
-       (Reported by David Woolley)
-  * ASTERISK-24508 - pjsip - REFER request from SNOM is rejected
-       with "400 bad request" - DEBUG shows "Received a REFER without a
-       parseable Refer-To" (Reported by Beppo Mazzucato)
-  * ASTERISK-24535 - stringfields: Fix regression from fix for
-       unintentional memory retention and another issue exposed by the
-       fix (Reported by Corey Farrell)
-  * ASTERISK-24471 - Crash - assert_fail in libc in
-       pjmedia_sdp_neg_negotiate from /usr/local/lib/libpjmedia.so.2
-       (Reported by yaron nahum)
-  * ASTERISK-24528 - res_pjsip_refer: Sending INVITE with Replaces
-       in-dialog with invalid target causes crash (Reported by Joshua
-       Colp)
-  * ASTERISK-24531 - res_pjsip_acl: ACLs not applied on initial
-       module load (Reported by Matt Jordan)
-  * ASTERISK-24469 - Security Vulnerability: Mixed IPv4/IPv6 ACLs
-       allow blocked addresses through (Reported by Matt Jordan)
-  * ASTERISK-24542 - [patch]Failure showing codecs via 'core show
-       channeltype <tech>' (Reported by snuffy)
-  * ASTERISK-24533 - 2 threads created per chan_sip entry (Reported
-       by xrobau)
-  * ASTERISK-24516 - [patch]Asterisk segfaults when playing back
-       voicemail under high concurrency with an IMAP backend (Reported
-       by David Duncan Ross Palmer)
-  * ASTERISK-24572 - [patch]App_meetme is loaded without its
-       defaults when the configuration file is missing (Reported by
-       Nuno Borges)
-  * ASTERISK-24573 - [patch]Out of sync conversation recording when
-       divided in multiple recordings (Reported by Nuno Borges)
-  * ASTERISK-24537 - Stasis: StasisStart/StasisEnd events are not
-       reliably transmitted during transfers (Reported by Matt Jordan)
-  * ASTERISK-24556 - Asterisk 13 core dumps when calling from pjsip
-       extension to another pjsip extension  (Reported by Abhay Gupta)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-24279 - Documentation: Clarify the behaviour of the CDR
-       property 'unanswered' (Reported by Matt Jordan)
-  * ASTERISK-24283 - [patch]Microseconds precision in the eventtime
-       column in the cel_odbc module (Reported by Etienne Lessard)
-  * ASTERISK-24530 - [patch] app_record stripping 1/4 second from
-       recordings (Reported by Ben Smithurst)
-  * ASTERISK-24577 - Speed up loopback switches by avoiding unneeded
-       lookups (Reported by Birger "WIMPy" Harzenetter)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-13.1.0

* Thu Jan 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 13.0.2-3
- Add speexdsp as build dep as speex_echo.h has moved - rhbz 1181021

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 13.0.2-2
- update for lua 5.3

* Wed Dec 10 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.0.2-1
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 11.6 and Asterisk 11, 12, and 13. The available security releases are
- released as versions 11.6-cert9, 11.14.2, 12.7.2, and 13.0.2.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolves the following security vulnerability:
-
- * AST-2014-019: Remote Crash Vulnerability in WebSocket Server
-
-   When handling a WebSocket frame the res_http_websocket module dynamically
-   changes the size of the memory used to allow the provided payload to fit. If a
-   payload length of zero was received the code would incorrectly attempt to
-   resize to zero. This operation would succeed and end up freeing the memory but
-   be treated as a failure. When the session was subsequently torn down this
-   memory would get freed yet again causing a crash.
-
- For more information about the details of this vulnerability, please read
- security advisory AST-2014-019, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert9
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.14.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.7.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.0.2
-
- The security advisory is available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-019.pdf

* Thu Nov 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.0.1-1
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.28 and 11.6 and Asterisk 1.8, 11, 12, and 13. The available
- security releases are released as versions 1.8.28-cert3, 11.6-cert8, 1.8.32.1,
- 11.14.1, 12.7.1, and 13.0.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolves the following security vulnerabilities:
-
- * AST-2014-012: Unauthorized access in the presence of ACLs with mixed IP
-   address families
-
-   Many modules in Asterisk that service incoming IP traffic have ACL options
-   ("permit" and "deny") that can be used to whitelist or blacklist address
-   ranges. A bug has been discovered where the address family of incoming
-   packets is only compared to the IP address family of the first entry in the
-   list of access control rules. If the source IP address for an incoming
-   packet is not of the same address as the first ACL entry, that packet
-   bypasses all ACL rules.
-
- * AST-2014-018: Permission Escalation through DB dialplan function
-
-   The DB dialplan function when executed from an external protocol, such as AMI,
-   could result in a privilege escalation. Users with a lower class authorization
-   in AMI can access the internal Asterisk database without the required SYSTEM
-   class authorization.
-
- In addition, the release of 11.6-cert8 and 11.14.1 resolves the following
- security vulnerability:
-
- * AST-2014-014: High call load with ConfBridge can result in resource exhaustion
-
-   The ConfBridge application uses an internal bridging API to implement
-   conference bridges. This internal API uses a state model for channels within
-   the conference bridge and transitions between states as different things
-   occur. Unload load it is possible for some state transitions to be delayed
-   causing the channel to transition from being hung up to waiting for media. As
-   the channel has been hung up remotely no further media will arrive and the
-   channel will stay within ConfBridge indefinitely.
-
- In addition, the release of 11.6-cert8, 11.14.1, 12.7.1, and 13.0.1 resolves
- the following security vulnerability:
-
- * AST-2014-017: Permission Escalation via ConfBridge dialplan function and
-                 AMI ConfbridgeStartRecord Action
-
-   The CONFBRIDGE dialplan function when executed from an external protocol (such
-   as AMI) can result in a privilege escalation as certain options within that
-   function can affect the underlying system. Additionally, the AMI
-   ConfbridgeStartRecord action has options that would allow modification of the
-   underlying system, and does not require SYSTEM class authorization in AMI.
-
- Finally, the release of 12.7.1 and 13.0.1 resolves the following security
- vulnerabilities:
-
- * AST-2014-013: Unauthorized access in the presence of ACLs in the PJSIP stack
-
-   The Asterisk module res_pjsip provides the ability to configure ACLs that may
-   be used to reject SIP requests from various hosts. However, the module
-   currently fails to create and apply the ACLs defined in its configuration
-   file on initial module load.
-
- * AST-2014-015: Remote crash vulnerability in PJSIP channel driver
-
-   The chan_pjsip channel driver uses a queue approach for relating to SIP
-   sessions. There exists a race condition where actions may be queued to answer
-   a session or send ringing after a SIP session has been terminated using a
-   CANCEL request. The code will incorrectly assume that the SIP session is still
-   active and attempt to send the SIP response. The PJSIP library does not
-   expect the SIP session to be in the disconnected state when sending the
-   response and asserts.
-
- * AST-2014-016: Remote crash vulnerability in PJSIP channel driver
-
-   When handling an INVITE with Replaces message the res_pjsip_refer module
-   incorrectly assumes that it will be operating on a channel that has just been
-   created. If the INVITE with Replaces message is sent in-dialog after a session
-   has been established this assumption will be incorrect. The res_pjsip_refer
-   module will then hang up a channel that is actually owned by another thread.
-   When this other thread attempts to use the just hung up channel it will end up
-   using a freed channel which will likely result in a crash.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2014-012, AST-2014-013, AST-2014-014, AST-2014-015,
- AST-2014-016, AST-2014-017, and AST-2014-018, which were released at the same
- time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.28-cert3
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert8
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.32.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.14.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.7.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.0.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-012.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-013.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-014.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-015.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-016.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-017.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-018.pdf

* Thu Nov 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 13.0.0-1
- The Asterisk Development Team is pleased to announce the release of
- Asterisk 13.0.0. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- Asterisk 13 is the next major release series of Asterisk. It is a Long Term
- Support (LTS) release, similar to Asterisk 11. For more information about
- support time lines for Asterisk releases, see the Asterisk versions page:
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- For important information regarding upgrading to Asterisk 13, please see the
- Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+13
-
- A short list of new features includes:
-
- * Asterisk security events are now provided via AMI, allowing end users to
-   monitor their Asterisk system in real time for security related issues.
-
- * Both AMI and ARI now allow external systems to control the state of a mailbox.
-   Using AMI actions or ARI resources, external systems can programmatically
-   trigger Message Waiting Indicators (MWI) on subscribed phones. This is of
-   particular use to those who want to build their own VoiceMail application
-   using ARI.
-
- * ARI now supports the reception/transmission of out of call text messages using
-   any supported channel driver/protocol stack through ARI. Users receive out of
-   call text messages as JSON events over the ARI websocket connection, and can
-   send out of call text messages using HTTP requests.
-
- * The PJSIP stack now supports RFC 4662 Resource Lists, allowing Asterisk to act
-   as a Resource List Server. This includes defining lists of presence state,
-   mailbox state, or lists of presence state/mailbox state; managing
-   subscriptions to lists; and batched delivery of NOTIFY requests to
-   subscribers.
-
- * The PJSIP stack can now be used as a means of distributing device state or
-   mailbox state via PUBLISH requests to other Asterisk instances. This is
-   analogous to Asterisk's clustering support using XMPP or Corosync; unlike
-   existing clustering mechanisms, using the PJSIP stack to perform the
-   distribution of state does not rely on another daemon or server to perform the
-   work.
-
- And much more!
-
- More information about the new features can be found on the Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+13+Documentation
-
- A full list of all new features can also be found in the CHANGES file:
-
- http://svnview.digium.com/svn/asterisk/branches/13/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.0.0

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 11.13.1-2
- rebuild for new libsrtp

* Mon Oct 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 11.13.1-1
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.28 and 11.6 and Asterisk 1.8, 11, 12, and 13. The available
- security releases are released as versions 1.8.28-cert2, 11.6-cert7, 1.8.31.1,
- 11.13.1, 12.6.1, and 13.0.0-beta3.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolves the following security vulnerability:
-
- * AST-2014-011: Asterisk Susceptibility to POODLE Vulnerability
-
-   Asterisk is susceptible to the POODLE vulnerability in two ways:
-   1) The res_jabber and res_xmpp module both use SSLv3 exclusively for their
-      encrypted connections.
-   2) The core TLS handling in Asterisk, which is used by the chan_sip channel
-      driver, Asterisk Manager Interface (AMI), and Asterisk HTTP Server, by
-      default allow a TLS connection to fallback to SSLv3. This allows for a
-      MITM to potentially force a connection to fallback to SSLv3, exposing it
-      to the POODLE vulnerability.
-
-   These issues have been resolved in the versions released in conjunction with
-   this security advisory.
-
- For more information about the details of this vulnerability, please read
- security advisory AST-2014-011, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.28-cert2
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert7
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.31.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.13.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.6.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.0.0-beta3
-
- The security advisory is available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-011.pdf

* Mon Oct 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 11.13.0-1
- The Asterisk Development Team has announced the release of Asterisk 11.13.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.13.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-24032 - Gentoo compilation emits warning:
-       "_FORTIFY_SOURCE" redefined (Reported by Kilburn)
-  * ASTERISK-24225 - Dial option z is broken (Reported by
-       dimitripietro)
-  * ASTERISK-24178 - [patch]fromdomainport used even if not set
-       (Reported by Elazar Broad)
-  * ASTERISK-22252 - res_musiconhold cleanup - REF_DEBUG reload
-       warnings and ref leaks (Reported by Walter Doekes)
-  * ASTERISK-23997 - chan_sip: port incorrectly incremented for RTCP
-       ICE candidates in SDP answer (Reported by Badalian Vyacheslav)
-  * ASTERISK-24019 - When a Music On Hold stream starts it restarts
-       at beginning of file. (Reported by Jason Richards)
-  * ASTERISK-23767 - [patch] Dynamic IAX2 registration stops trying
-       if ever not able to resolve (Reported by David Herselman)
-  * ASTERISK-24211 - testsuite: Fix the dial_LS_options test
-       (Reported by Matt Jordan)
-  * ASTERISK-24249 - SIP debugs do not stop (Reported by Avinash
-       Mohod)
-  * ASTERISK-23577 - res_rtp_asterisk: Crash in
-       ast_rtp_on_turn_rtp_state when RTP instance is NULL (Reported by
-       Jay Jideliov)
-  * ASTERISK-23634 - With TURN Asterisk crashes on multiple (7-10)
-       concurrent WebRTC (avpg/encryption/icesupport) calls (Reported
-       by Roman Skvirsky)
-  * ASTERISK-24301 - Security: Out of call MESSAGE requests
-       processed via Message channel driver can crash Asterisk
-       (Reported by Matt Jordan)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-24171 - [patch] Provide a manpage for the aelparse
-       utility (Reported by Jeremy Lainé)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.13.0

* Mon Oct 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 11.12.1-1
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 11.6 and Asterisk 11 and 12. The available security releases are
- released as versions 11.6-cert6, 11.12.1, and 12.5.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- Please note that the release of these versions resolves the following security
- vulnerability:
-
- * AST-2014-010: Remote Crash when Handling Out of Call Message in Certain
-                 Dialplan Configurations
-
- Additionally, the release of Asterisk 12.5.1 resolves the following security
- vulnerability:
-
- * AST-2014-009: Remote Crash Based on Malformed SIP Subscription Requests
-
- Note that the crash described in AST-2014-010 can be worked around through
- dialplan configuration. Given the likelihood of the issue, an advisory was
- deemed to be warranted.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2014-009 and AST-2014-010, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert6
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.12.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.5.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-009.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-010.pdf

* Mon Oct 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 11.12.0-1
- The Asterisk Development Team has announced the release of Asterisk 11.12.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.12.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-23911 - URIENCODE/URIDECODE: WARNING about passing an
-       empty string is a bit over zealous (Reported by Matt Jordan)
-  * ASTERISK-23985 - PresenceState Action response does not contain
-       ActionID; duplicates Message Header (Reported by Matt Jordan)
-  * ASTERISK-23814 - No call started after peer dialed (Reported by
-       Igor Goncharovsky)
-  * ASTERISK-24087 - [patch]chan_sip: sip_subscribe_mwi_destroy
-       should not call sip_destroy (Reported by Corey Farrell)
-  * ASTERISK-23818 - PBX_Lua: after asterisk startup module is
-       loaded, but dialplan not available (Reported by Dennis Guse)
-  * ASTERISK-18345 - [patch] sips connection dropped by asterisk
-       with a large INVITE (Reported by Stephane Chazelas)
-  * ASTERISK-23508 - Memory Corruption in
-       __ast_string_field_ptr_build_va (Reported by Arnd Schmitter)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-21178 - Improve documentation for manager command
-       Getvar, Setvar (Reported by Rusty Newton)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.12.0

* Mon Oct 20 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 11.11.0-1
- The Asterisk Development Team has announced the release of Asterisk 11.11.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.11.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-22551 - Session timer : UAS (Asterisk) starts counting
-       at Invite, UAC starts counting at 200 OK. (Reported by i2045)
-  * ASTERISK-23792 - Mutex left locked in chan_unistim.c (Reported
-       by Peter Whisker)
-  * ASTERISK-23582 - [patch]Inconsistent column length in *odbc
-       (Reported by Walter Doekes)
-  * ASTERISK-23803 - AMI action UpdateConfig EmptyCat clears all
-       categories but the requested one (Reported by zvision)
-  * ASTERISK-23035 - ConfBridge with name longer than max (32 chars)
-       results in several bridges with same conf_name (Reported by
-       Iñaki Cívico)
-  * ASTERISK-23824 - ConfBridge: Users cannot be muted via CLI or
-       AMI when waiting to enter a conference (Reported by Matt Jordan)
-  * ASTERISK-23683 - #includes - wildcard character in a path more
-       than one directory deep - results in no config parsing on module
-       reload (Reported by tootai)
-  * ASTERISK-23827 - autoservice thread doesn't exit at shutdown
-       (Reported by Corey Farrell)
-  * ASTERISK-23609 - Security: AMI action MixMonitor allows
-       arbitrary programs to be run (Reported by Corey Farrell)
-  * ASTERISK-23673 - Security: DOS by consuming the number of
-       allowed HTTP connections. (Reported by Richard Mudgett)
-  * ASTERISK-23246 - DEBUG messages in sdp_crypto.c display despite
-       a DEBUG level of zero (Reported by Rusty Newton)
-  * ASTERISK-23766 - [patch] Specify timeout for database write in
-       SQLite (Reported by Igor Goncharovsky)
-  * ASTERISK-23844 - Load of pbx_lua fails on sample extensions.lua
-       with Lua 5.2 or greater due to addition of goto statement
-       (Reported by Rusty Newton)
-  * ASTERISK-23818 - PBX_Lua: after asterisk startup module is
-       loaded, but dialplan not available (Reported by Dennis Guse)
-  * ASTERISK-23834 - res_rtp_asterisk debug message gives wrong
-       length if ICE (Reported by Richard Kenner)
-  * ASTERISK-23790 - [patch] - SIP From headers longer than 256
-       characters result in dropped call and 'No closing bracket'
-       warnings. (Reported by uniken1)
-  * ASTERISK-23917 - res_http_websocket: Delay in client processing
-       large streams of data causes disconnect and stuck socket
-       (Reported by Matt Jordan)
-  * ASTERISK-23908 - [patch]When using FEC error correction,
-       asterisk tries considers negative sequence numbers as missing
-       (Reported by Torrey Searle)
-  * ASTERISK-23921 - refcounter.py uses excessive ram for large refs
-       files  (Reported by Corey Farrell)
-  * ASTERISK-23948 - REF_DEBUG fails to record ao2_ref against
-       objects that were already freed (Reported by Corey Farrell)
-  * ASTERISK-23916 - [patch]SIP/SDP fmtp line may include whitespace
-       between attributes (Reported by Alexander Traud)
-  * ASTERISK-23984 - Infinite loop possible in ast_careful_fwrite()
-       (Reported by Steve Davies)
-  * ASTERISK-23897 - [patch]Change in SETUP ACK handling (checking
-       PI) in revision 413765 breaks working environments (Reported by
-       Pavel Troller)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-23492 - Add option to safe_asterisk to disable
-       backgrounding (Reported by Walter Doekes)
-  * ASTERISK-22961 - [patch] DTLS-SRTP not working with SHA-256
-       (Reported by Jay Jideliov)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.11.0

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 11.10.2-2.2
- Perl 5.20 rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.10.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.10.2-2:
- Drop the 389 directory server schema (1061414)

* Thu Jun 19 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.10.2-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.15, 11.6, and Asterisk 1.8, 11, and 12. The available security
- releases are released as versions 1.8.15-cert7, 11.6-cert4, 1.8.28.2, 11.10.2,
- and 12.3.2.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- These releases resolve security vulnerabilities that were previously fixed in
- 1.8.15-cert6, 11.6-cert3, 1.8.28.1, 11.10.1, and 12.3.1. Unfortunately, the fix
- for AST-2014-007 inadvertently introduced a regression in Asterisk's TCP and TLS
- handling that prevented Asterisk from sending data over these transports. This
- regression and the security vulnerabilities have been fixed in the versions
- specified in this release announcement.
-
- The security patches for AST-2014-007 have been updated with the fix for the
- regression, and are available at http://downloads.asterisk.org/pub/security
-
- Please note that the release of these versions resolves the following security
- vulnerabilities:
-
- * AST-2014-005: Remote Crash in PJSIP Channel Driver's Publish/Subscribe
-                 Framework
-
- * AST-2014-006: Permission Escalation via Asterisk Manager User Unauthorized
-                 Shell Access
-
- * AST-2014-007: Denial of Service via Exhaustion of Allowed Concurrent HTTP
-                 Connections
-
- * AST-2014-008: Denial of Service in PJSIP Channel Driver Subscriptions
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2014-005, AST-2014-006, AST-2014-007, and AST-2014-008,
- which were released with the previous versions that addressed these
- vulnerabilities.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.15-cert7
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.28.2
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert4
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.10.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.3.2
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-005.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-006.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-007.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-008.pdf

* Thu Jun 19 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.10.1-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.15, 11.6, and Asterisk 1.8, 11, and 12. The available security
- releases are released as versions 1.8.15-cert6, 11.6-cert3, 1.8.28.1, 11.10.1,
- and 12.3.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolves the following issue:
-
- * AST-2014-007: Denial of Service via Exhaustion of Allowed Concurrent HTTP
-                 Connections
-
-   Establishing a TCP or TLS connection to the configured HTTP or HTTPS port
-   respectively in http.conf and then not sending or completing a HTTP request
-   will tie up a HTTP session. By doing this repeatedly until the maximum number
-   of open HTTP sessions is reached, legitimate requests are blocked.
-
- Additionally, the release of 11.6-cert3, 11.10.1, and 12.3.1 resolves the
- following issue:
-
- * AST-2014-006: Permission Escalation via Asterisk Manager User Unauthorized
-                 Shell Access
-
-   Manager users can execute arbitrary shell commands with the MixMonitor manager
-   action. Asterisk does not require system class authorization for a manager
-   user to use the MixMonitor action, so any manager user who is permitted to use
-   manager commands can potentially execute shell commands as the user executing
-   the Asterisk process.
-
- Additionally, the release of 12.3.1 resolves the following issues:
-
- * AST-2014-005: Remote Crash in PJSIP Channel Driver's Publish/Subscribe
-                 Framework
-
-   A remotely exploitable crash vulnerability exists in the PJSIP channel
-   driver's pub/sub framework. If an attempt is made to unsubscribe when not
-   currently subscribed and the endpoint's “sub_min_expiry” is set to zero,
-   Asterisk tries to create an expiration timer with zero seconds, which is not
-   allowed, so an assertion raised.
-
- * AST-2014-008: Denial of Service in PJSIP Channel Driver Subscriptions
-
-   When a SIP transaction timeout caused a subscription to be terminated, the
-   action taken by Asterisk was guaranteed to deadlock the thread on which SIP
-   requests are serviced. Note that this behavior could only happen on
-   established subscriptions, meaning that this could only be exploited if an
-   attacker bypassed authentication and successfully subscribed to a real
-   resource on the Asterisk server.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2014-005, AST-2014-006, AST-2014-007, and AST-2014-008,
- which were released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.15-cert6
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.28.1
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert3
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.10.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.3.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-005.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-006.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-007.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-008.pdf

* Thu Jun 19 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.10.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.10.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.10.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-23547 - [patch] app_queue removing callers from queue
-       when reloading (Reported by Italo Rossi)
-  * ASTERISK-23559 - app_voicemail fails to load after fix to
-       dialplan functions (Reported by Corey Farrell)
-  * ASTERISK-22846 - testsuite: masquerade super test fails on all
-       branches (still) (Reported by Matt Jordan)
-  * ASTERISK-23545 - Confbridge talker detection settings
-       configuration load bug (Reported by John Knott)
-  * ASTERISK-23546 - CB_ADD_LEN does not do what you'd think
-       (Reported by Walter Doekes)
-  * ASTERISK-23620 - Code path in app_stack fails to unlock list
-       (Reported by Bradley Watkins)
-  * ASTERISK-23616 - Big memory leak in logger.c (Reported by
-       ibercom)
-  * ASTERISK-23576 - Build failure on SmartOS / Illumos / SunOS
-       (Reported by Sebastian Wiedenroth)
-  * ASTERISK-23550 - Newer sound sets don't show up in menuselect
-       (Reported by Rusty Newton)
-  * ASTERISK-18331 - app_sms failure (Reported by David Woodhouse)
-  * ASTERISK-19465 - P-Asserted-Identity Privacy (Reported by
-       Krzysztof Chmielewski)
-  * ASTERISK-23605 - res_http_websocket: Race condition in shutting
-       down websocket causes crash (Reported by Matt Jordan)
-  * ASTERISK-23707 - Realtime Contacts: Apparent mismatch between
-       PGSQL database state and Asterisk state (Reported by Mark
-       Michelson)
-  * ASTERISK-23381 - [patch]ChanSpy- Barge only works on the initial
-       'spy', if the spied-on channel makes a new call, unable to
-       barge. (Reported by Robert Moss)
-  * ASTERISK-23665 - Wrong mime type for codec H263-1998 (h263+)
-       (Reported by Guillaume Maudoux)
-  * ASTERISK-23664 - Incorrect H264 specification in SDP. (Reported
-       by Guillaume Maudoux)
-  * ASTERISK-22977 - chan_sip+CEL: missing ANSWER and PICKUP event
-       for INVITE/w/replaces pickup (Reported by Walter Doekes)
-  * ASTERISK-23709 - Regression in Dahdi/Analog/waitfordialtone
-       (Reported by Steve Davies)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-23649 - [patch]Support for DTLS retransmission
-       (Reported by NITESH BANSAL)
-  * ASTERISK-23564 - [patch]TLS/SRTP status of channel not currently
-       available in a CLI command (Reported by Patrick Laimbock)
-  * ASTERISK-23754 - [patch] Use var/lib directory for log file
-       configured in asterisk.conf (Reported by Igor Goncharovsky)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.10.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.9.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Dennis Gilmore <dennis@ausil.us> - 11.9.0-2
- build against gmime-devel not gmime22-devel
- do not use -m64 on aarch64

* Wed Apr 23 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.9.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.9.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.9.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-22790 - check_modem_rate() may return incorrect rate
-       for V.27 (Reported by Paolo Compagnini)
-  * ASTERISK-23034 - [patch] manager Originate doesn't abort on
-       failed format_cap allocation (Reported by Corey Farrell)
-  * ASTERISK-23061 - [Patch] 'textsupport' setting not mentioned in
-       sip.conf.sample (Reported by Eugene)
-  * ASTERISK-23028 - [patch] Asterisk man pages contains unquoted
-       minus signs (Reported by Jeremy Lainé)
-  * ASTERISK-23046 - Custom CDR fields set during a GoSUB called
-       from app_queue are not inserted (Reported by Denis Pantsyrev)
-  * ASTERISK-23027 - [patch] Spelling typo "transfered" instead of
-       "transferred" (Reported by Jeremy Lainé)
-  * ASTERISK-23008 - Local channels loose CALLERID name when DAHDI
-       channel connects (Reported by Michael Cargile)
-  * ASTERISK-23100 - [patch] In chan_mgcp the ident in transmitted
-       request and request queue may differ - fix for locking (Reported
-       by adomjan)
-  * ASTERISK-22988 - [patch]T38 , SIP 488 after Rejecting image
-       media offer due to invalid or unsupported syntax (Reported by
-       adomjan)
-  * ASTERISK-22861 - [patch]Specifying a null time as parameter to
-       GotoIfTime or ExecIfTime causes segmentation fault (Reported by
-       Sebastian Murray-Roberts)
-  * ASTERISK-17837 - extconfig.conf - Maximum Include level (1)
-       exceeded (Reported by pz)
-  * ASTERISK-22662 - Documentation fix? - queues.conf says
-       persistentmembers defaults to yes, it appears to lie (Reported
-       by Rusty Newton)
-  * ASTERISK-23134 - [patch] res_rtp_asterisk port selection cannot
-       handle selinux port restrictions (Reported by Corey Farrell)
-  * ASTERISK-23220 - STACK_PEEK function with no arguments causes
-       crash/core dump (Reported by James Sharp)
-  * ASTERISK-19773 - Asterisk crash on issuing Asterisk-CLI 'reload'
-       command multiple times on cli_aliases (Reported by Joel Vandal)
-  * ASTERISK-22757 - segfault in res_clialiases.so on reload when
-       mapping "module reload" command (Reported by Gareth Blades)
-  * ASTERISK-17727 - [patch] TLS doesn't get all certificate chain
-       (Reported by LN)
-  * ASTERISK-23178 - devicestate.h: device state setting functions
-       are documented with the wrong return values (Reported by
-       Jonathan Rose)
-  * ASTERISK-23232 - LocalBridge AMI Event LocalOptimization value
-       is opposite to what's expected (Reported by Leon Roy)
-  * ASTERISK-23098 - [patch]possible null pointer dereference in
-       format.c (Reported by Marcello Ceschia)
-  * ASTERISK-23297 - Asterisk 12, pbx_config.so segfaults if
-       res_parking.so is not loaded, or if res_parking.conf has no
-       configuration (Reported by CJ Oster)
-  * ASTERISK-23069 - Custom CDR variable not recorded when set in
-       macro called from app_queue (Reported by Bryan Anderson)
-  * ASTERISK-19499 - ConfBridge MOH is not working for transferee
-       after attended transfer (Reported by Timo Teräs)
-  * ASTERISK-23261 - [patch]Output mixup in
-       ${CHANNEL(rtpqos,audio,all)} (Reported by rsw686)
-  * ASTERISK-23279 - [patch]Asterisk doesn't support the dynamic
-       payload change in rtp mapping in the 200 OK response (Reported
-       by NITESH BANSAL)
-  * ASTERISK-23255 - UUID included for Redhat, but missing for
-       Debian distros in install_prereq script (Reported by Rusty
-       Newton)
-  * ASTERISK-23260 - [patch]ForkCDR v option does not keep CDR
-       variables for subsequent records (Reported by zvision)
-  * ASTERISK-23141 - Asterisk crashes on Dial(), in
-       pbx_find_extension at pbx.c (Reported by Maxim)
-  * ASTERISK-23336 - Asterisk warning "Don't know how to indicate
-       condition 33 on ooh323c" on outgoing calls from H323 to SIP peer
-       (Reported by Alexander Semych)
-  * ASTERISK-23231 - Since 405693 If we have res_fax.conf file set
-       to minrate=2400, then res_fax refuse to load (Reported by David
-       Brillert)
-  * ASTERISK-23135 - Crash - segfault in ast_channel_hangupcause_set
-       - probably introduced in 11.7.0 (Reported by OK)
-  * ASTERISK-23323 - [patch]chan_sip: missing p->owner checks in
-       handle_response_invite (Reported by Walter Doekes)
-  * ASTERISK-23406 - [patch]Fix typo in "sip show peer" (Reported by
-       ibercom)
-  * ASTERISK-23310 - bridged channel crashes in bridge_p2p_rtp_write
-       (Reported by Jeremy Lainé)
-  * ASTERISK-22911 - [patch]Asterisk fails to resume WebRTC call
-       from hold (Reported by Vytis Valentinavičius)
-  * ASTERISK-23104 - Specifying the SetVar AMI without a Channel
-       cause Asterisk to crash (Reported by Joel Vandal)
-  * ASTERISK-21930 - [patch]WebRTC over WSS is not working.
-       (Reported by John)
-  * ASTERISK-23383 - Wrong sense test on stat return code causes
-       unchanged config check to break with include files. (Reported by
-       David Woolley)
-  * ASTERISK-20149 - Crash when faxing SIP to SIP with strictrtp set
-       to yes (Reported by Alexandr Gordeev)
-  * ASTERISK-17523 - Qualify for static realtime peers does not work
-       (Reported by Maciej Krajewski)
-  * ASTERISK-21406 - [patch] chan_sip deadlock on monlock between
-       unload_module and do_monitor (Reported by Corey Farrell)
-  * ASTERISK-23373 - [patch]Security: Open FD exhaustion with
-       chan_sip Session-Timers (Reported by Corey Farrell)
-  * ASTERISK-23340 - Security Vulnerability: stack allocation of
-       cookie headers in loop allows for unauthenticated remote denial
-       of service attack (Reported by Matt Jordan)
-  * ASTERISK-23311 - Manager - MoH Stop Event fails to show up when
-       leaving Conference (Reported by Benjamin Keith Ford)
-  * ASTERISK-23420 - [patch]Memory leak in manager_add_filter
-       function in manager.c (Reported by Etienne Lessard)
-  * ASTERISK-23488 - Logic error in callerid checksum processing
-       (Reported by Russ Meyerriecks)
-  * ASTERISK-23461 - Only first user is muted when joining
-       confbridge with 'startmuted=yes' (Reported by Chico Manobela)
-  * ASTERISK-20841 - fromdomain not honored on outbound INVITE
-       request (Reported by Kelly Goedert)
-  * ASTERISK-22079 - Segfault: INTERNAL_OBJ (user_data=0x6374652f)
-       at astobj2.c:120 (Reported by Jamuel Starkey)
-  * ASTERISK-23509 - [patch]SayNumber for Polish language tries to
-       play empty files for numbers divisible by 100 (Reported by
-       zvision)
-  * ASTERISK-23103 - [patch]Crash in ast_format_cmp, in ao2_find
-       (Reported by JoshE)
-  * ASTERISK-23391 - Audit dialplan function usage of channel
-       variable (Reported by Corey Farrell)
-  * ASTERISK-23548 - POST to ARI sometimes returns no body on
-       success (Reported by Scott Griepentrog)
-  * ASTERISK-23460 - ooh323 channel stuck if call is placed directly
-       and gatekeeper is not available (Reported by Dmitry Melekhov)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-22980 - [patch]Allow building cdr_radius and cel_radius
-       against libfreeradius-client (Reported by Jeremy Lainé)
-  * ASTERISK-22661 - Unable to exit ChanSpy if spied channel does
-       not have a call in progress (Reported by Chris Hillman)
-  * ASTERISK-23099 - [patch] WSS: enable ast_websocket_read()
-       function to read the whole available data at first and then wait
-       for any fragmented packets (Reported by Thava Iyer)

* Tue Mar 11 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.8.1-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.15, 11.6, and Asterisk 1.8, 11, and 12. The available security
- releases are released as versions 1.8.15-cert5, 11.6-cert2, 1.8.26.1, 11.8.1,
- and 12.1.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolve the following issues:
-
- * AST-2014-001: Stack overflow in HTTP processing of Cookie headers.
-
-   Sending a HTTP request that is handled by Asterisk with a large number of
-   Cookie headers could overflow the stack.
-
-   Another vulnerability along similar lines is any HTTP request with a
-   ridiculous number of headers in the request could exhaust system memory.
-
- * AST-2014-002: chan_sip: Exit early on bad session timers request
-
-   This change allows chan_sip to avoid creation of the channel and
-   consumption of associated file descriptors altogether if the inbound
-   request is going to be rejected anyway.
-
- Additionally, the release of 12.1.1 resolves the following issue:
-
- * AST-2014-003: res_pjsip: When handling 401/407 responses don't assume a
-   request will have an endpoint.
-
-   This change removes the assumption that an outgoing request will always
-   have an endpoint and makes the authenticate_qualify option work once again.
-
- Finally, a security advisory, AST-2014-004, was released for a vulnerability
- fixed in Asterisk 12.1.0. Users of Asterisk 12.0.0 are encouraged to upgrade to
- 12.1.1 to resolve both vulnerabilities.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2014-001, AST-2014-002, AST-2014-003, and AST-2014-004,
- which were released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.15-cert5
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.26.1
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.6-cert2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.8.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-12.1.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2014-001.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-002.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-003.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2014-004.pdf

* Tue Mar  4 2014 Jeffrey Ollie <jeff@ocjtech.us> - 11.8.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.8.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.8.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- Bugs fixed in this release:
- -----------------------------------
-  * ASTERISK-22544 - Italian prompt vm-options has advertisement in
-       it (Reported by Rusty Newton)
-  * ASTERISK-21383 - STUN Binding Requests Not Being Sent Back from
-       Asterisk to Chrome (Reported by Shaun Clark)
-  * ASTERISK-22478 - [patch]Can't use pound(hash) symbol for custom
-       DTMF menus in ConfBridge (processed as directive) (Reported by
-       Nicolas Tanski)
-  * ASTERISK-12117 - chan_sip creates a new local tag (from-tag) for
-       every register message (Reported by Pawel Pierscionek)
-  * ASTERISK-20862 - Asterisk min and max member penalties not
-       honored when set with 0 (Reported by Schmooze Com)
-  * ASTERISK-22746 - [patch]Crash in chan_dahdi during caller id
-       read (Reported by Michael Walton)
-  * ASTERISK-22788 - [patch] main/translate.c: access to variable f
-       after free in ast_translate() (Reported by Corey Farrell)
-  * ASTERISK-21242 - Segfault when T.38 re-invite retransmission
-       receives 200 OK (Reported by Ashley Winters)
-  * ASTERISK-22590 - BufferOverflow in unpacksms16() when receiving
-       16 bit multipart SMS with app_sms (Reported by Jan Juergens)
-  * ASTERISK-22905 - Prevent Asterisk functions that are 'dangerous'
-       from being executed from external interfaces (Reported by Matt
-       Jordan)
-  * ASTERISK-23021 - Typos in code : "avaliable" instead of
-       "available" (Reported by Jeremy Lainé)
-  * ASTERISK-22970 - [patch]Documentation fix for QUOTE() (Reported
-       by Gareth Palmer)
-  * ASTERISK-21960 - ooh323 channels stuck (Reported by Dmitry
-       Melekhov)
-  * ASTERISK-22350 - DUNDI - core dump on shutdown - segfault in
-       sqlite3_reset from /usr/lib/libsqlite3.so.0 (Reported by Birger
-       "WIMPy" Harzenetter)
-  * ASTERISK-22942 - [patch] - Asterisk crashed after
-       Set(FAXOPT(faxdetect)=t38) (Reported by adomjan)
-  * ASTERISK-22856 - [patch]SayUnixTime in polish reads minutes
-       instead of seconds (Reported by Robert Mordec)
-  * ASTERISK-22854 - [patch] - Deadlock between cel_pgsql unload and
-       core_event_dispatcher taskprocessor thread (Reported by Etienne
-       Lessard)
-  * ASTERISK-22910 - [patch] - REPLACE() calls strcpy on overlapping
-       memory when <replace-char> is empty (Reported by Gareth Palmer)
-  * ASTERISK-22871 - cel_pgsql module not loading after "reload" or
-       "reload cel_pgsql.so" command (Reported by Matteo)
-  * ASTERISK-23084 - [patch]rasterisk needlessly prints the
-       AST-2013-007 warning (Reported by Tzafrir Cohen)
-  * ASTERISK-17138 - [patch] Asterisk not re-registering after it
-       receives "Forbidden - wrong password on authentication"
-       (Reported by Rudi)
-  * ASTERISK-23011 - [patch]configure.ac and pbx_lua don't support
-       lua 5.2 (Reported by George Joseph)
-  * ASTERISK-22834 - Parking by blind transfer when lot full orphans
-       channels (Reported by rsw686)
-  * ASTERISK-23047 - Orphaned (stuck) channel occurs during a failed
-       SIP transfer to parking space (Reported by Tommy Thompson)
-  * ASTERISK-22946 - Local From tag regression with sipgate.de
-       (Reported by Stephan Eisvogel)
-  * ASTERISK-23010 - No BYE message sent when sip INVITE is received
-       (Reported by Ryan Tilton)
-  * ASTERISK-23135 - Crash - segfault in ast_channel_hangupcause_set
-       - probably introduced in 11.7.0 (Reported by OK)
-
- Improvements made in this release:
- -----------------------------------
-  * ASTERISK-22728 - [patch] Improve Understanding Of 'Forcerport'
-       When Running "sip show peers" (Reported by Michael L. Young)
-  * ASTERISK-22659 - Make a new core and extra sounds release
-       (Reported by Rusty Newton)
-  * ASTERISK-22919 - core show channeltypes slicing  (Reported by
-       outtolunc)
-  * ASTERISK-22918 - dahdi show channels slices PRI channel dnid on
-       output (Reported by outtolunc)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.8.0

* Sat Dec 28 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.7.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.7.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.7.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- app_confbridge: Can now set the language used for announcements
-       to the conference.
-   (Closes issue ASTERISK-19983. Reported by Jonathan White)
-
- * --- app_queue: Fix CLI "queue remove member" queue_log entry.
-   (Closes issue ASTERISK-21826. Reported by Oscar Esteve)
-
- * --- chan_sip: Do not increment the SDP version between 183 and 200
-       responses.
-   (Closes issue ASTERISK-21204. Reported by NITESH BANSAL)
-
- * --- chan_sip: Allow a sip peer to accept both AVP and AVPF calls
-   (Closes issue ASTERISK-22005. Reported by Torrey Searle)
-
- * --- chan_sip: Fix Realtime Peer Update Problem When Un-registering
-       And Expires Header In 200ok
-   (Closes issue ASTERISK-22428. Reported by Ben Smithurst)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.7.0

* Sat Dec 28 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.6.1-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.15, 11.2, and Asterisk 1.8, 10, and 11. The available security
- releases are released as versions 1.8.15-cert4, 11.2-cert3, 1.8.24.1, 10.12.4,
- 10.12.4-digiumphones, and 11.6.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolve the following issues:
-
- * A buffer overflow when receiving odd length 16 bit messages in app_sms. An
-   infinite loop could occur which would overwrite memory when a message is
-   received into the unpacksms16() function and the length of the message is an
-   odd number of bytes.
-
- * Prevent permissions escalation in the Asterisk Manager Interface. Asterisk
-   now marks certain individual dialplan functions as 'dangerous', which will
-   inhibit their execution from external sources.
-
-   A 'dangerous' function is one which results in a privilege escalation. For
-   example, if one were to read the channel variable SHELL(rm -rf /) Bad
-   Things(TM) could happen; even if the external source has only read
-   permissions.
-
-   Execution from external sources may be enabled by setting 'live_dangerously'
-   to 'yes' in the [options] section of asterisk.conf. Although doing so is not
-   recommended.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2013-006 and AST-2013-007, which were
- released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.15-cert4
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.2-cert3
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.24.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.12.4
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.12.4-digiumphones
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.6.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2013-006.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2013-007.pdf

* Sat Dec 28 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.6.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.6.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.6.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Confbridge: empty conference not being torn down
-   (Closes issue ASTERISK-21859. Reported by Chris Gentle)
-
- * --- Let Queue wrap up time influence member availability
-   (Closes issue ASTERISK-22189. Reported by Tony Lewis)
-
- * --- Fix a longstanding issue with MFC-R2 configuration that
-       prevented users
-   (Closes issue ASTERISK-21117. Reported by Rafael Angulo)
-
- * --- chan_iax2: Fix saving the wrong expiry time in astdb.
-   (Closes issue ASTERISK-22504. Reported by Stefan Wachtler)
-
- * --- Fix segfault for certain invalid WebSocket input.
-   (Closes issue ASTERISK-21825. Reported by Alfred Farrugia)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.6.0

* Mon Oct 21 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.5.1-3:
- Disable hardened build, as it's apparently causing problems loading modules.

* Thu Aug 29 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.5.1-2:
- Enable hardened build BZ#954338
- Significant clean ups

* Thu Aug 29 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.5.1-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.15, 11.2, and Asterisk 1.8, 10, and 11. The available security releases
- are released as versions 1.8.15-cert2, 11.2-cert2, 1.8.23.1, 10.12.3, 10.12.3-digiumphones,
- and 11.5.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolve the following issues:
-
- * A remotely exploitable crash vulnerability exists in the SIP channel driver if
-   an ACK with SDP is received after the channel has been terminated. The
-   handling code incorrectly assumes that the channel will always be present.
-
- * A remotely exploitable crash vulnerability exists in the SIP channel driver if
-   an invalid SDP is sent in a SIP request that defines media descriptions before
-   connection information. The handling code incorrectly attempts to reference
-   the socket address information even though that information has not yet been
-   set.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2013-004 and AST-2013-005, which were
- released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.15-cert3
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-11.2-cert2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.23.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.12.3
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.12.3-digiumphones
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.5.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2013-004.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2013-005.pdf
-
- The Asterisk Development Team has announced the release of Asterisk 11.5.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.5.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Fix Segfault In app_queue When "persistentmembers" Is Enabled
-       And Using Realtime
-   (Closes issue ASTERISK-21738. Reported by JoshE)
-
- * --- IAX2: fix race condition with nativebridge transfers.
-   (Closes issue ASTERISK-21409. Reported by alecdavis)
-
- * --- Fix The Payload Being Set On CN Packets And Do Not Set Marker
-       Bit
-   (Closes issue ASTERISK-21246. Reported by Peter Katzmann)
-
- * --- Fix One-Way Audio With auto_* NAT Settings When SIP Calls
-       Initiated By PBX
-   (Closes issue ASTERISK-21374. Reported by Michael L. Young)
-
- * --- chan_sip: NOTIFYs for BLF start queuing up and fail to be sent
-       out after retries fail
-   (Closes issue ASTERISK-21677. Reported by Dan Martens)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.4.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 11.4.0-2.1
- Perl 5.18 rebuild

* Fri May 24 2013 Rex Dieter <rdieter@fedoraproject.org> 11.4.0-2
- rebuild (libical)

* Mon May 20 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.4.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.4.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.4.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Fix Sorting Order For Parking Lots Stored In Static Realtime
-   (Closes issue ASTERISK-21035. Reported by Alex Epshteyn)
-
- * --- Fix StopMixMonitor Hanging Up When Unable To Stop MixMonitor On
-       A Channel
-   (Closes issue ASTERISK-21294. Reported by daroz)
-
- * --- When a session timer expires during a T.38 call, re-invite with
-       correct SDP
-   (Closes issue ASTERISK-21232. Reported by Nitesh Bansal)
-
- * --- Fix white noise on SRTP decryption
-   (Closes issue ASTERISK-21323. Reported by andrea)
-
- * --- Fix reload skinny with active devices.
-   (Closes issue ASTERISK-16610. Reported by wedhorn)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.4.0

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 11.3.0-2:
- fix build with lua 5.2

* Tue Apr 23 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.3.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.3.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.3.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Fix issue where chan_mobile fails to bind to first available
-       port
-   (Closes issue ASTERISK-16357. Reported by challado)
-
- * --- Fix Queue Log Reporting Every Call COMPLETECALLER With "h"
-       Extension Present
-   (Closes issue ASTERISK-20743. Reported by call)
-
- * --- Retain XMPP filters across reconnections so external modules
-       continue to function as expected.
-   (Closes issue ASTERISK-20916. Reported by kuj)
-
- * --- Ensure that a declined media stream is terminated with a '\r\n'
-   (Closes issue ASTERISK-20908. Reported by Dennis DeDonatis)
-
- * --- Fix pjproject compilation in certain circumstances
-   (Closes issue ASTERISK-20681. Reported by Dinesh Ramjuttun)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.3.0

* Thu Mar 28 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.2.2-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.15 and Asterisk 1.8, 10, and 11. The available security releases
- are released as versions 1.8.15-cert2, 1.8.20.2, 10.12.2, 10.12.2-digiumphones,
- and 11.2.2.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolve the following issues:
-
- * A possible buffer overflow during H.264 format negotiation. The format
-   attribute resource for H.264 video performs an unsafe read against a media
-   attribute when parsing the SDP.
-
-   This vulnerability only affected Asterisk 11.
-
- * A denial of service exists in Asterisk's HTTP server. AST-2012-014, fixed
-   in January of this year, contained a fix for Asterisk's HTTP server for a
-   remotely-triggered crash. While the fix prevented the crash from being
-   triggered, a denial of service vector still exists with that solution if an
-   attacker sends one or more HTTP POST requests with very large Content-Length
-   values.
-
-   This vulnerability affects Certified Asterisk 1.8.15, Asterisk 1.8, 10, and 11
-
- * A potential username disclosure exists in the SIP channel driver. When
-   authenticating a SIP request with alwaysauthreject enabled, allowguest
-   disabled, and autocreatepeer disabled, Asterisk discloses whether a user
-   exists for INVITE, SUBSCRIBE, and REGISTER transactions in multiple ways.
-
-   This vulnerability affects Certified Asterisk 1.8.15, Asterisk 1.8, 10, and 11
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2013-001, AST-2013-002, and AST-2013-003, which were
- released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.15-cert2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.20.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.12.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.12.2-digiumphones
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.2.2
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2013-001.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2013-002.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2013-003.pdf

* Sun Feb 10 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.2.1-1:
- The Asterisk Development Team has announced the release of Asterisk 11.2.1.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.2.1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- * --- Fix astcanary startup problem due to wrong pid value from before
-       daemon call
-   (Closes issue ASTERISK-20947. Reported by Jakob Hirsch)
-
- * --- Update init.d scripts to handle stderr; readd splash screen for
-       remote consoles
-   (Closes issue ASTERISK-20945. Reported by Warren Selby)
-
- * --- Reset RTP timestamp; sequence number on SSRC change
-   (Closes issue ASTERISK-20906. Reported by Eelco Brolman)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.2.1

* Fri Jan 18 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.2.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.2.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.2.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- app_meetme: Fix channels lingering when hung up under certain
-       conditions
-   (Closes issue ASTERISK-20486. Reported by Michael Cargile)
-
- * --- Fix stuck DTMF when bridge is broken.
-   (Closes issue ASTERISK-20492. Reported by Jeremiah Gowdy)
-
- * --- Add missing support for "who hung up" to chan_motif.
-   (Closes issue ASTERISK-20671. Reported by Matt Jordan)
-
- * --- Remove a fixed size limitation for producing SDP and change how
-       ICE support is disabled by default.
-   (Closes issue ASTERISK-20643. Reported by coopvr)
-
- * --- Fix chan_sip websocket payload handling
-   (Closes issue ASTERISK-20745. Reported by Iñaki Baz Castillo)
-
- * --- Fix pjproject compilation in certain circumstances
-   (Closes issue ASTERISK-20681. Reported by Dinesh Ramjuttun)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.2.0

* Thu Jan  3 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.1.2-1:
- The Asterisk Development Team has announced a security release for Asterisk 11,
- Asterisk 11.1.2. This release addresses the security vulnerabilities reported in
- AST-2012-014 and AST-2012-015, and replaces the previous version of Asterisk 11
- released for these security vulnerabilities. The prior release left open a
- vulnerability in res_xmpp that exists only in Asterisk 11; as such, other
- versions of Asterisk were resolved correctly by the previous releases.
-
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolve the following two issues:
-
- * Stack overflows that occur in some portions of Asterisk that manage a TCP
-   connection. In SIP, this is exploitable via a remote unauthenticated session;
-   in XMPP and HTTP connections, this is exploitable via remote authenticated
-   sessions. The vulnerabilities in SIP and HTTP were corrected in a prior
-   release of Asterisk; the vulnerability in XMPP is resolved in this release.
-
- * A denial of service vulnerability through exploitation of the device state
-   cache. Anonymous calls had the capability to create devices in Asterisk that
-   would never be disposed of. Handling the cachability of device states
-   aggregated via XMPP is handled in this release.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2012-014 and AST-2012-015.
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.1.2
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-014.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-015.pdf
-
- Thank you for your continued support of Asterisk - and we apologize for having
- to do this twice!

* Wed Jan  2 2013 Jeffrey Ollie <jeff@ocjtech.us> - 11.1.1-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.11 and Asterisk 1.8, 10, and 11. The available security releases
- are released as versions 1.8.11-cert10, 1.8.19.1, 10.11.1, 10.11.1-digiumphones,
- and 11.1.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of these versions resolve the following two issues:
-
- * Stack overflows that occur in some portions of Asterisk that manage a TCP
-   connection. In SIP, this is exploitable via a remote unauthenticated session;
-   in XMPP and HTTP connections, this is exploitable via remote authenticated
-   sessions.
-
- * A denial of service vulnerability through exploitation of the device state
-   cache. Anonymous calls had the capability to create devices in Asterisk that
-   would never be disposed of.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2012-014 and AST-2012-015, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.11-cert10
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.19.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.11.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.11.1-digiumphones
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.1.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-014.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-015.pdf

* Wed Dec 12 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.1.0-1:
- The Asterisk Development Team has announced the release of Asterisk 11.1.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.1.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Fix execution of 'i' extension due to uninitialized variable.
-   (Closes issue ASTERISK-20455. Reported by Richard Miller)
-
- * --- Prevent resetting of NATted realtime peer address on reload.
-   (Closes issue ASTERISK-18203. Reported by daren ferreira)
-
- * --- Fix ConfBridge crash if no timing module loaded.
-   (Closes issue ASTERISK-19448. Reported by feyfre)
-
- * --- Fix the Park 'r' option when a channel parks itself.
-   (Closes issue ASTERISK-19382. Reported by James Stocks)
-
- * --- Fix an issue where outgoing calls would fail to establish audio
-       due to ICE negotiation failures.
-   (Closes issue ASTERISK-20554. Reported by mmichelson)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.1.0

* Fri Dec  7 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.2-1:
- The Asterisk Development Team has announced the release of Asterisk 11.0.2.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.0.2 resolves an issue reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is the issue resolved in this release:
-
- * --- chan_local: Fix local_pvt ref leak in local_devicestate().
-   (Closes issue ASTERISK-20769. Reported by rmudgett)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.0.2

* Wed Dec  5 2012 Dan Horák <dan[at]danny.cz> - 11.0.1-3
- simplify LDFLAGS setting

* Fri Nov 30 2012 Dennis Gilmore <dennis@ausil.us> - 11.0.1-2
- clean up things to allow building on arm arches

* Mon Nov  5 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.1-1
- The Asterisk Development Team has announced the release of Asterisk 11.0.1.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.0.1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- * --- chan_sip: Fix a bug causing SIP reloads to remove all entries
-       from the registry
-   (Closes issue ASTERISK-20611. Reported by Alisher)
-
- * --- confbridge: Fix a bug which made conferences not record with
-       AMI/CLI commands
-   (Closes issue ASTERISK-20601. Reported by Vilius)
-
- * --- Fix an issue with res_http_websocket where the chan_sip
-       WebSocket handler could not be registered.
-   (Closes issue ASTERISK-20631. Reported by danjenkins)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.0.1

* Tue Oct 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.0-1:
- The Asterisk Development Team is pleased to announce the release of
- Asterisk 11.0.0.  This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- Asterisk 11 is the next major release series of Asterisk.  It is a Long Term
- Support (LTS) release, similar to Asterisk 1.8.  For more information about
- support time lines for Asterisk releases, see the Asterisk versions page:
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- For important information regarding upgrading to Asterisk 11, please see the
- Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+11
-
- A short list of new features includes:
-
- * A new channel driver named chan_motif has been added which provides support
-   for Google Talk and Jingle in a single channel driver.  This new channel
-   driver includes support for both audio and video, RFC2833 DTMF, all codecs
-   supported by Asterisk, hold, unhold, and ringing notification. It is also
-   compliant with the current Jingle specification, current Google Jingle
-   specification, and the original Google Talk protocol.
-
- * Support for the WebSocket transport for chan_sip.
-
- * SIP peers can now be configured to support negotiation of ICE candidates.
-
- * The app_page application now no longer depends on DAHDI or app_meetme. It
-   has been re-architected to use app_confbridge internally.
-
- * Hangup handlers can be attached to channels using the CHANNEL() function.
-   Hangup handlers will run when the channel is hung up similar to the h
-   extension; however, unlike an h extension, a hangup handler is associated with
-   the actual channel and will execute anytime that channel is hung up,
-   regardless of where it is in the dialplan.
-
- * Added pre-dial handlers for the Dial and Follow-Me applications.  Pre-dial
-   allows you to execute a dialplan subroutine on a channel before a call is
-   placed but after the application performing a dial action is invoked. This
-   means that the handlers are executed after the creation of the callee
-   channels, but before any actions have been taken to actually dial the callee
-   channels.
-
- * Log messages can now be easily associated with a certain call by looking at
-   a new unique identifier, "Call Id".  Call ids are attached to log messages for
-   just about any case where it can be determined that the message is related
-   to a particular call.
-
- * Introduced Named ACLs as a new way to define Access Control Lists (ACLs) in
-   Asterisk. Unlike traditional ACLs defined in specific module configuration
-   files, Named ACLs can be shared across multiple modules.
-
- * The Hangup Cause family of functions and dialplan applications allow for
-   inspection of the hangup cause codes for each channel involved in a call.
-   This allows a dialplan writer to determine, for each channel, who hung up and
-   for what reason(s).
-
- * Two new functions have been added: FEATURE() and FEATUREMAP(). FEATURE()
-   lets you set some of the configuration options from the general section
-   of features.conf on a per-channel basis. FEATUREMAP() lets you customize
-   the key sequence used to activate built-in features, such as blindxfer,
-   and automon.
-
- * Support for DTLS-SRTP in chan_sip.
-
- * Support for named pickupgroups/callgroups, allowing any number of pickupgroups
-   and callgroups to be defined for several channel drivers.
-
- * IPv6 Support for AMI, AGI, ExternalIVR, and the SIP Security Event Framework.
-
- More information about the new features can be found on the Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+11+Documentation
-
- A full list of all new features can also be found in the CHANGES file.
-
- http://svnview.digium.com/svn/asterisk/branches/11/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog.
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.0.0

* Wed Oct 17 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.0-0.7.rc2:
- The Asterisk Development Team has announced the second release candidate of
- Asterisk 11.0.0. This release candidate is available for immediate
- download at http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 11.0.0-rc2 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release candidate:
-
- * --- Fix an issue where outgoing calls would fail to establish audio
-       due to ICE negotiation failures.
-   (Closes issue ASTERISK-20554. Reported by mmichelson)
-
- * --- Ensure Asterisk fails TCP/TLS SIP calls when certificate
-       checking fails
-   (Closes issue ASTERISK-20559. Reported by kmoore)
-
- * --- Don't make chan_sip export global symbols.
-   (Closes issue ASTERISK-20545. Reported by kmoore)
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-11.0.0-rc2

* Tue Oct  9 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.0-0.6.rc1
- The Asterisk Development Team is pleased to announce the first release candidate
- of Asterisk 11.0.0.  This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- All interested users of Asterisk are encouraged to participate in the
- Asterisk 11 testing process.  Please report any issues found to the issue
- tracker, https://issues.asterisk.org/jira.  It is also very useful to see
- successful test reports.  Please post those to the asterisk-dev mailing list.
- All Asterisk users are invited to participate in the #asterisk-testing channel
- on IRC to work together in testing the many parts of Asterisk.
-
- Asterisk 11 is the next major release series of Asterisk.  It will be a Long
- Term Support (LTS) release, similar to Asterisk 1.8.  For more information about
- support time lines for Asterisk releases, see the Asterisk versions page:
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- For important information regarding upgrading to Asterisk 11, please see the
- Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+11
-
- A short list of new features includes:
-
- * A new channel driver named chan_motif has been added which provides support
-   for Google Talk and Jingle in a single channel driver.  This new channel
-   driver includes support for both audio and video, RFC2833 DTMF, all codecs
-   supported by Asterisk, hold, unhold, and ringing notification. It is also
-   compliant with the current Jingle specification, current Google Jingle
-   specification, and the original Google Talk protocol.
-
- * Support for the WebSocket transport for chan_sip.
-
- * SIP peers can now be configured to support negotiation of ICE candidates.
-
- * The app_page application now no longer depends on DAHDI or app_meetme. It
-   has been re-architected to use app_confbridge internally.
-
- * Hangup handlers can be attached to channels using the CHANNEL() function.
-   Hangup handlers will run when the channel is hung up similar to the h
-   extension; however, unlike an h extension, a hangup handler is associated with
-   the actual channel and will execute anytime that channel is hung up,
-   regardless of where it is in the dialplan.
-
- * Added pre-dial handlers for the Dial and Follow-Me applications.  Pre-dial
-   allows you to execute a dialplan subroutine on a channel before a call is
-   placed but after the application performing a dial action is invoked. This
-   means that the handlers are executed after the creation of the callee
-   channels, but before any actions have been taken to actually dial the callee
-   channels.
-
- * Log messages can now be easily associated with a certain call by looking at
-   a new unique identifier, "Call Id".  Call ids are attached to log messages for
-   just about any case where it can be determined that the message is related
-   to a particular call.
-
- * Introduced Named ACLs as a new way to define Access Control Lists (ACLs) in
-   Asterisk. Unlike traditional ACLs defined in specific module configuration
-   files, Named ACLs can be shared across multiple modules.
-
- * The Hangup Cause family of functions and dialplan applications allow for
-   inspection of the hangup cause codes for each channel involved in a call.
-   This allows a dialplan writer to determine, for each channel, who hung up and
-   for what reason(s).
-
- * Two new functions have been added: FEATURE() and FEATUREMAP(). FEATURE()
-   lets you set some of the configuration options from the general section
-   of features.conf on a per-channel basis. FEATUREMAP() lets you customize
-   the key sequence used to activate built-in features, such as blindxfer,
-   and automon.
-
- * Support for DTLS-SRTP in chan_sip.
-
- * Support for named pickupgroups/callgroups, allowing any number of pickupgroups
-   and callgroups to be defined for several channel drivers.
-
- * IPv6 Support for AMI, AGI, ExternalIVR, and the SIP Security Event Framework.
-
- More information about the new features can be found on the Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+11+Documentation
-
- A full list of all new features can also be found in the CHANGES file.
-
- http://svnview.digium.com/svn/asterisk/branches/11/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog.
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.0.0-rc1

* Wed Sep 26 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.0-0.5.beta2
- Don't forget format_ilbc module

* Wed Sep 26 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.0-0.4.beta2
- The Asterisk Development Team is pleased to announce the second beta release of
- Asterisk 11.0.0.  This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- All interested users of Asterisk are encouraged to participate in the
- Asterisk 11 testing process.  Please report any issues found to the issue
- tracker, https://issues.asterisk.org/jira.  It is also very useful to see
- successful test reports.  Please post those to the asterisk-dev mailing list.
- All Asterisk users are invited to participate in the #asterisk-testing channel
- on IRC to work together in testing the many parts of Asterisk.
-
- Asterisk 11 is the next major release series of Asterisk.  It will be a Long
- Term Support (LTS) release, similar to Asterisk 1.8.  For more information about
- support time lines for Asterisk releases, see the Asterisk versions page:
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- For important information regarding upgrading to Asterisk 11, please see the
- Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+11
-
- A short list of new features includes:
-
- * A new channel driver named chan_motif has been added which provides support
-   for Google Talk and Jingle in a single channel driver.  This new channel
-   driver includes support for both audio and video, RFC2833 DTMF, all codecs
-   supported by Asterisk, hold, unhold, and ringing notification. It is also
-   compliant with the current Jingle specification, current Google Jingle
-   specification, and the original Google Talk protocol.
-
- * Support for the WebSocket transport for chan_sip.
-
- * SIP peers can now be configured to support negotiation of ICE candidates.
-
- * The app_page application now no longer depends on DAHDI or app_meetme. It
-   has been re-architected to use app_confbridge internally.
-
- * Hangup handlers can be attached to channels using the CHANNEL() function.
-   Hangup handlers will run when the channel is hung up similar to the h
-   extension; however, unlike an h extension, a hangup handler is associated with
-   the actual channel and will execute anytime that channel is hung up,
-   regardless of where it is in the dialplan.
-
- * Added pre-dial handlers for the Dial and Follow-Me applications.  Pre-dial
-   allows you to execute a dialplan subroutine on a channel before a call is
-   placed but after the application performing a dial action is invoked. This
-   means that the handlers are executed after the creation of the callee
-   channels, but before any actions have been taken to actually dial the callee
-   channels.
-
- * Log messages can now be easily associated with a certain call by looking at
-   a new unique identifier, "Call Id".  Call ids are attached to log messages for
-   just about any case where it can be determined that the message is related
-   to a particular call.
-
- * Introduced Named ACLs as a new way to define Access Control Lists (ACLs) in
-   Asterisk. Unlike traditional ACLs defined in specific module configuration
-   files, Named ACLs can be shared across multiple modules.
-
- * The Hangup Cause family of functions and dialplan applications allow for
-   inspection of the hangup cause codes for each channel involved in a call.
-   This allows a dialplan writer to determine, for each channel, who hung up and
-   for what reason(s).
-
- * Two new functions have been added: FEATURE() and FEATUREMAP(). FEATURE()
-   lets you set some of the configuration options from the general section
-   of features.conf on a per-channel basis. FEATUREMAP() lets you customize
-   the key sequence used to activate built-in features, such as blindxfer,
-   and automon.
-
- * Support for DTLS-SRTP in chan_sip.
-
- * Support for named pickupgroups/callgroups, allowing any number of pickupgroups
-   and callgroups to be defined for several channel drivers.
-
- * IPv6 Support for AMI, AGI, ExternalIVR, and the SIP Security Event Framework.
-
- More information about the new features can be found on the Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+11+Documentation
-
- A full list of all new features can also be found in the CHANGES file.
-
- http://svnview.digium.com/svn/asterisk/branches/11/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog.
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.0.0-beta2

* Wed Sep 26 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.8.0-1
- The Asterisk Development Team has announced the release of Asterisk 10.8.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.8.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- AST-2012-012: Resolve AMI User Unauthorized Shell Access through
-       ExternalIVR
-   (Closes issue ASTERISK-20132. Reported by Zubair Ashraf of IBM X-Force Research)
-
- * --- AST-2012-013: Resolve ACL rules being ignored during calls by
-       some IAX2 peers
-   (Closes issue ASTERISK-20186. Reported by Alan Frisch)
-
- * --- Handle extremely out of order RFC 2833 DTMF
-   (Closes issue ASTERISK-18404. Reported by Stephane Chazelas)
-
- * --- Resolve severe memory leak in CEL logging modules.
-   (Closes issue AST-916. Reported by Thomas Arimont)
-
- * --- Only re-create an SRTP session when needed
-   (Issue ASTERISK-20194. Reported by Nicolo Mazzon)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.8.0

* Tue Sep 04 2012 Dan Horák <dan[at]danny.cz> - 11.0.0-0.3.beta1
- fix build on s390

* Tue Sep 04 2012 Dan Horák <dan[at]danny.cz> - 10.7.1-2
- fix build on s390

* Thu Aug 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.7.1-1
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.11 and Asterisk 1.8 and 10. The available security releases are
- released as versions 1.8.11-cert7, 1.8.15.1, 10.7.1, and 10.7.1-digiumphones.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.8.11-cert7, 1.8.15.1, 10.7.1, and 10.7.1-digiumphones
- resolve the following two issues:
-
- * A permission escalation vulnerability in Asterisk Manager Interface.  This
-   would potentially allow remote authenticated users the ability to execute
-   commands on the system shell with the privileges of the user running the
-   Asterisk application.  Please note that the README-SERIOUSLY.bestpractices.txt
-   file delivered with Asterisk has been updated due to this and other related
-   vulnerabilities fixed in previous versions of Asterisk.
-
- * When an IAX2 call is made using the credentials of a peer defined in a
-   dynamic Asterisk Realtime Architecture (ARA) backend, the ACL rules for that
-   peer are not applied to the call attempt. This allows for a remote attacker
-   who is aware of a peer's credentials to bypass the ACL rules set for that
-   peer.
-
- These issues and their resolutions are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2012-012 and AST-2012-013, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.11-cert7
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.15.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.7.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.7.1-digiumphones
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-012.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-013.pdf

* Thu Aug 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.7.0-1
- The Asterisk Development Team has announced the release of Asterisk 10.7.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.7.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Fix deadlock potential with ast_set_hangupsource() calls.
-   (Closes issue ASTERISK-19801. Reported by Alec Davis)
-
- * --- Fix request routing issue when outboundproxy is used.
-   (Closes issue ASTERISK-20008. Reported by Marcus Hunger)
-
- * --- Set the Caller ID "tag" on peers even if remote party
-       information is present.
-   (Closes issue ASTERISK-19859. Reported by Thomas Arimont)
-
- * --- Fix NULL pointer segfault in ast_sockaddr_parse()
-   (Closes issue ASTERISK-20006. Reported by Michael L. Young)
-
- * --- Do not perform install on existing directories
-   (Closes issue ASTERISK-19492. Reported by Karl Fife)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.7.0

* Thu Aug 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.6.1-1
- The Asterisk Development Team has announced the release of Asterisk 10.6.1.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.6.1 resolves an issue reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is the issue resolved in this release:
-
- * --- Remove a superfluous and dangerous freeing of an SSL_CTX.
-   (Closes issue ASTERISK-20074. Reported by Trevor Helmsley)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.6.1

* Thu Aug 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.6.0-1
- The Asterisk Development Team has announced the release of Asterisk 10.6.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.6.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- format_mp3: Fix a possible crash in mp3_read().
-   (Closes issue ASTERISK-19761. Reported by Chris Maciejewsk)
-
- * --- Fix local channel chains optimizing themselves out of a call.
-   (Closes issue ASTERISK-16711. Reported by Alec Davis)
-
- * --- Re-add LastMsgsSent value for SIP peers
-   (Closes issue ASTERISK-17866. Reported by Steve Davies)
-
- * --- Prevent sip_pvt refleak when an ast_channel outlasts its
-       corresponding sip_pvt.
-   (Closes issue ASTERISK-19425. Reported by David Cunningham)
-
- * --- Send more accurate identification information in dialog-info SIP
-       NOTIFYs.
-   (Closes issue ASTERISK-16735. Reported by Maciej Krajewski)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.6.0

* Sat Aug 18 2012 Jeffrey Ollie <jeff@ocjtech.us> - 11.0.0-0.2.beta1
- The Asterisk Development Team is pleased to announce the first beta release of
- Asterisk 11.0.0.  This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- All interested users of Asterisk are encouraged to participate in the
- Asterisk 11 testing process.  Please report any issues found to the issue
- tracker, https://issues.asterisk.org/jira.  It is also very useful to see
- successful test reports.  Please post those to the asterisk-dev mailing list.
- All Asterisk users are invited to participate in the #asterisk-testing channel
- on IRC to work together in testing the many parts of Asterisk.
-
- Asterisk 11 is the next major release series of Asterisk.  It will be a Long
- Term Support (LTS) release, similar to Asterisk 1.8.  For more information about
- support time lines for Asterisk releases, see the Asterisk versions page:
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- For important information regarding upgrading to Asterisk 11, please see the
- Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+11
-
- A short list of new features includes:
-
- * A new channel driver named chan_motif has been added which provides support
-   for Google Talk and Jingle in a single channel driver.  This new channel
-   driver includes support for both audio and video, RFC2833 DTMF, all codecs
-   supported by Asterisk, hold, unhold, and ringing notification. It is also
-   compliant with the current Jingle specification, current Google Jingle
-   specification, and the original Google Talk protocol.
-
- * Support for the WebSocket transport for chan_sip.
-
- * SIP peers can now be configured to support negotiation of ICE candidates.
-
- * The app_page application now no longer depends on DAHDI or app_meetme. It
-   has been re-architected to use app_confbridge internally.
-
- * Hangup handlers can be attached to channels using the CHANNEL() function.
-   Hangup handlers will run when the channel is hung up similar to the h
-   extension; however, unlike an h extension, a hangup handler is associated with
-   the actual channel and will execute anytime that channel is hung up,
-   regardless of where it is in the dialplan.
-
- * Added pre-dial handlers for the Dial and Follow-Me applications.  Pre-dial
-   allows you to execute a dialplan subroutine on a channel before a call is
-   placed but after the application performing a dial action is invoked. This
-   means that the handlers are executed after the creation of the caller/callee
-   channels, but before any actions have been taken to actually dial the callee
-   channels.
-
- * Log messages can now be easily associated with a certain call by looking at
-   a new unique identifier, "Call Id".  Call ids are attached to log messages for
-   just about any case where it can be determined that the message is related
-   to a particular call.
-
- * Introduced Named ACLs as a new way to define Access Control Lists (ACLs) in
-   Asterisk. Unlike traditional ACLs defined in specific module configuration
-   files, Named ACLs can be shared across multiple modules.
-
- * The Hangup Cause family of functions and dialplan applications allow for
-   inspection of the hangup cause codes for each channel involved in a call.
-   This allows a dialplan writer to determine, for each channel, who hung up and
-   for what reason(s).
-
- * Two new functions have been added: FEATURE() and FEATUREMAP(). FEATURE()
-   lets you set some of the configuration options from the general section
-   of features.conf on a per-channel basis. FEATUREMAP() lets you customize
-   the key sequence used to activate built-in features, such as blindxfer,
-   and automon.
-
- * Support for named pickupgroups/callgroups, allowing any number of pickupgroups
-   and callgroups to be defined for several channel drivers.
-
- * IPv6 Support for AMI, AGI, ExternalIVR, and the SIP Security Event Framework.
-
- More information about the new features can be found on the Asterisk wiki:
-
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+11+Documentation
-
- A full list of all new features can also be found in the CHANGES file.
-
- http://svnview.digium.com/svn/asterisk/branches/11/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog.
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-11.0.0-beta1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.5.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 10.5.2-1.1
- Perl 5.16 rebuild

* Thu Jul  5 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.5.2-1:
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.11 and Asterisk 1.8 and 10. The available security releases are
- released as versions 1.8.11-cert4, 1.8.13.1, 10.5.2, and 10.5.2-digiumphones.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.8.11-cert4, 1.8.13.1, 10.5.2, and 10.5.2-digiumphones
- resolve the following two issues:
-
- * If Asterisk sends a re-invite and an endpoint responds to the re-invite with
-   a provisional response but never sends a final response, then the SIP dialog
-   structure is never freed and the RTP ports for the call are never released. If
-   an attacker has the ability to place a call, they could create a denial of
-   service by using all available RTP ports.
-
- * If a single voicemail account is manipulated by two parties simultaneously,
-   a condition can occur where memory is freed twice causing a crash.
-
- These issues and their resolution are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2012-010 and AST-2012-011, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.11-cert4
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.13.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.5.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.5.2-digiumphones
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-010.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-011.pdf

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 10.5.1-1.1
- Perl 5.16 rebuild

* Fri Jun 15 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.5.1-1
- The Asterisk Development Team has announced a security release for Asterisk 10.
- This security release is released as version 10.5.1.
-
- The release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 10.5.1 resolves the following issue:
-
- * A remotely exploitable crash vulnerability was found in the Skinny (SCCP)
-  Channel driver. When an SCCP client sends an Off Hook message, followed by
-  a Key Pad Button Message, a structure that was previously set to NULL is
-  dereferenced.  This allows remote authenticated connections the ability to
-  cause a crash in the server, denying services to legitimate users.
-
- This issue and its resolution is described in the security advisory.
-
- For more information about the details of this vulnerability, please read
- security advisory AST-2012-009, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.5.1
-
- The security advisory is available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-009.pdf

* Fri Jun 15 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.5.0-1
- The Asterisk Development Team has announced the release of Asterisk 10.5.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.5.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Turn off warning message when bind address is set to any.
-  (Closes issue ASTERISK-19456. Reported by Michael L. Young)
-
- * --- Prevent overflow in calculation in ast_tvdiff_ms on 32-bit
-      machines
-  (Closes issue ASTERISK-19727. Reported by Ben Klang)
-
- * --- Make DAHDISendCallreroutingFacility wait 5 seconds for a reply
-      before disconnecting the call.
-  (Closes issue ASTERISK-19708. Reported by mehdi Shirazi)
-
- * --- Fix recalled party B feature flags for a failed DTMF atxfer.
-  (Closes issue ASTERISK-19383. Reported by lgfsantos)
-
- * --- Fix DTMF atxfer running h exten after the wrong bridge ends.
-  (Closes issue ASTERISK-19717. Reported by Mario)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.5.0

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 10.4.2-1.1
- Perl 5.16 rebuild

* Wed May 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.4.2-1
- The Asterisk Development Team has announced the release of Asterisk 10.4.2.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.4.2 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- * --- Resolve crash in subscribing for MWI notifications
-  (Closes issue ASTERISK-19827. Reported by B. R)
-
- * --- Fix crash in ConfBridge when user announcement is played for
-      more than 2 users
-  (Closes issue ASTERISK-19899. Reported by Florian Gilcher)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.4.2

* Wed May 30 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.4.1-1
- The Asterisk Development Team has announced security releases for Certified
- Asterisk 1.8.11 and Asterisk 1.8 and 10. The available security releases are
- released as versions 1.8.11-cert2, 1.8.12.1, and 10.4.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.8.11-cert2, 1.8.12.1, and 10.4.1 resolve the following
- two issues:
-
- * A remotely exploitable crash vulnerability exists in the IAX2 channel
-  driver if an established call is placed on hold without a suggested music
-  class. Asterisk will attempt to use an invalid pointer to the music
-  on hold class name, potentially causing a crash.
-
- * A remotely exploitable crash vulnerability was found in the Skinny (SCCP)
-  Channel driver. When an SCCP client closes its connection to the server,
-  a pointer in a structure is set to NULL.  If the client was not in the
-  on-hook state at the time the connection was closed, this pointer is later
-  dereferenced. This allows remote authenticated connections the ability to
-  cause a crash in the server, denying services to legitimate users.
-
- These issues and their resolution are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2012-007 and AST-2012-008, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-1.8.11-cert2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.12.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.4.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-007.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-008.pdf

* Fri May  4 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.4.0-1
- The Asterisk Development Team has announced the release of Asterisk 10.4.0.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk
-
- The release of Asterisk 10.4.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- * --- Prevent chanspy from binding to zombie channels
-  (Closes issue ASTERISK-19493. Reported by lvl)
-
- * --- Fix Dial m and r options and forked calls generating warnings
-      for voice frames.
-  (Closes issue ASTERISK-16901. Reported by Chris Gentle)
-
- * --- Remove ISDN hold restriction for non-bridged calls.
-  (Closes issue ASTERISK-19388. Reported by Birger Harzenetter)
-
- * --- Fix copying of CDR(accountcode) to local channels.
-  (Closes issue ASTERISK-19384. Reported by jamicque)
-
- * --- Ensure Asterisk acknowledges ACKs to 4xx on Replaces errors
-  (Closes issue ASTERISK-19303. Reported by Jon Tsiros)
-
- * --- Eliminate double close of file descriptor in manager.c
-  (Closes issue ASTERISK-18453. Reported by Jaco Kroon)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.4.0

* Tue Apr 24 2012 Jeffrey Ollie <jeff@ocjtech.us> - 10.3.1-1
- The Asterisk Development Team has announced security releases for Asterisk 1.6.2,
- 1.8, and 10. The available security releases are released as versions 1.6.2.24,
- 1.8.11.1, and 10.3.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.6.2.24, 1.8.11.1, and 10.3.1 resolve the following two
- issues:
-
-  * A permission escalation vulnerability in Asterisk Manager Interface.  This
-   would potentially allow remote authenticated users the ability to execute
-   commands on the system shell with the privileges of the user running the
-   Asterisk application.
-
-  * A heap overflow vulnerability in the Skinny Channel driver.  The keypad
-   button message event failed to check the length of a fixed length buffer
-   before appending a received digit to the end of that buffer.  A remote
-   authenticated user could send sufficient keypad button message events that the
-   buffer would be overrun.
-
- In addition, the release of Asterisk 1.8.11.1 and 10.3.1 resolve the following
- issue:
-
-  * A remote crash vulnerability in the SIP channel driver when processing UPDATE
-   requests.  If a SIP UPDATE request was received indicating a connected line
-   update after a channel was terminated but before the final destruction of the
-   associated SIP dialog, Asterisk would attempt a connected line update on a
-   non-existing channel, causing a crash.
-
- These issues and their resolution are described in the security advisories.
-
- For more information about the details of these vulnerabilities, please read
- security advisories AST-2012-004, AST-2012-005, and AST-2012-006, which were
- released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLogs:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.24
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.11.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.3.1
-
- The security advisories are available at:
-
-  * http://downloads.asterisk.org/pub/security/AST-2012-004.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-005.pdf
-  * http://downloads.asterisk.org/pub/security/AST-2012-006.pdf

* Thu Mar 29 2012 Russell Bryant <russell@russellbryant.net> - 10.3.0-1
- Update to 10.3.0

* Fri Mar 16 2012 Russell Bryant <russell@russellbryant.net> - 10.2.1-1
- Update to 10.2.1 from upstream.
- Fix remote stack overflow in app_milliwatt.
- Fix remote stack overflow, including possible code injection, in HTTP digest
  authentication handling.
- Disable asterisk-corosync package, as it doesn't build right now.
- Resolves: rhbz#804045, rhbz#804038, rhbz#804042

* Thu Feb 16 2012 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.1.2-2
- * Add patch extracted from upstream to build with Corosync since
-   OpenAIS is no longer available.
- * Add PrivateTmp=true to systemd service file (#782478)
- * Add some macros to make it easier to build with fewer dependencies
-   (with corresponding less functionality) (#787389)
- * Add isa macros in a few places plus a few other changes to make it
-   easier to cross-compile. (#787779)

* Thu Feb 16 2012 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.1.2-1
- The Asterisk Development Team has announced the release of Asterisk 10.1.2. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 10.1.2 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following are the issues resolved in this release:
-
- * --- Fix SIP INFO DTMF handling for non-numeric codes ---
-  (Closes issue ASTERISK-19290. Reported by: Ira Emus)
-
- * --- Fix crash in ParkAndAnnounce ---
-  (Closes issue ASTERISK-19311. Reported-by: tootai)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.1.2

* Thu Feb 16 2012 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.1.1-1
- The Asterisk Development Team has announced the release of Asterisk 10.1.1. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 10.1.1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * --- Fixes deadlocks occuring in chan_agent ---
-  (Closes issue ASTERISK-19285. Reported by: Alex Villacis Lasso)
-
- * --- Ensure entering T.38 passthrough does not cause an infinite loop ---
-  (Closes issue ASTERISK-18951. Reported-by: Kristijan Vrban)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.1.1

* Thu Feb 16 2012 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.1.0-1
- The Asterisk Development Team is pleased to announce the release of
- Asterisk 10.1.0. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 10.1.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * AST-2012-001: prevent crash when an SDP offer
-  is received with an encrypted video stream when support for video
-  is disabled and res_srtp is loaded.  (closes issue ASTERISK-19202)
-  Reported by: Catalin Sanda
-
- * Allow playback of formats that don't support seeking.  ast_streamfile
-  previously did unconditional seeking on files that broke playback of
-  formats that don't support that functionality.  This patch avoids the
-  seek that was causing the problem.
-  (closes issue ASTERISK-18994) Patched by: Timo Teras
-
- * Add pjmedia probation concepts to res_rtp_asterisk's learning mode.  In
-  order to better handle RTP sources with strictrtp enabled (which is the
-  default setting in 10) using the learning mode to figure out new sources
-  when they change is handled by checking for a number of consecutive (by
-  sequence number) packets received to an rtp struct based on a new
-  configurable value called 'probation'.  Also, during learning mode instead
-  of liberally accepting all packets received, we now reject packets until a
-  clear source has been determined.
-
- * Handle AST_CONTROL_UPDATE_RTP_PEER frames in local bridge loop.  Failing
-  to handle AST_CONTROL_UPDATE_RTP_PEER frames in the local bridge loop
-  causes the loop to exit prematurely. This causes a variety of negative side
-  effects, depending on when the loop exits. This patch handles the frame by
-  essentially swallowing the frame in the local loop, as the current channel
-  drivers expect the RTP bridge to handle the frame, and, in the case of the
-  local bridge loop, no additional action is necessary.
-  (closes issue ASTERISK-19095) Reported by: Stefan Schmidt Tested
-  by: Matt Jordan
-
- * Fix timing source dependency issues with MOH.  Prior to this patch,
-  res_musiconhold existed at the same module priority level as the timing
-  sources that it depends on.  This would cause a problem when music on
-  hold was reloaded, as the timing source could be changed after
-  res_musiconhold was processed. This patch adds a new module priority
-  level, AST_MODPRI_TIMING, that the various timing modules are now loaded
-  at. This now occurs before loading other resource modules, such
-  that the timing source is guaranteed to be set prior to resolving
-  the timing source dependencies.
-  (closes issue ASTERISK-17474) Reporter: Luke H Tested by: Luke H,
-  Vladimir Mikhelson, zzsurf, Wes Van Tlghem, elguero, Thomas Arimont
-  Patched by elguero
-
- * Fix RTP reference leak.  If a blind transfer were initiated using a
-  REFER without a prior reINVITE to place the call on hold, AND if Asterisk
-  were sending RTCP reports, then there was a reference leak for the
-  RTP instance of the transferrer.
-  (closes issue ASTERISK-19192) Reported by: Tyuta Vitali
-
- * Fix blind transfers from failing if an 'h' extension
-  is present.  This prevents the 'h' extension from being run on the
-  transferee channel when it is transferred via a native transfer
-  mechanism such as SIP REFER.  (closes issue ASTERISK-19173) Reported
-  by: Ross Beer Tested by: Kristjan Vrban Patches: ASTERISK-19173 by
-  Mark Michelson (license 5049)
-
- * Restore call progress code for analog ports. Extracting sig_analog
-  from chan_dahdi lost call progress detection functionality.  Fix
-  analog ports from considering a call answered immediately after
-  dialing has completed if the callprogress option is enabled.
-  (closes issue ASTERISK-18841)
-  Reported by: Richard Miller Patched by Richard Miller
-
- * Fix regression that 'rtp/rtcp set debup ip' only works when a port
-  was also specified.
-  (closes issue ASTERISK-18693) Reported by: Davide Dal Reviewed by:
-  Walter Doekes
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.1.0

* Thu Feb 16 2012 Russell Bryant <russellb@fedoraproject.org> - 10.0.0-2
- Remove asterisk-ais.  OpenAIS was removed from Fedora.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-1
- Don't build API docs as the build never finishes

* Thu Dec 15 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-1
- The Asterisk Development Team is proud to announce the release of
- Asterisk 10.0.0. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- Asterisk 10 is the next major release series of Asterisk. It will be a
- Standard support release, similar to Asterisk 1.6.2. For more information about
- support time lines for Asterisk releases, see the Asterisk versions page:
-
-  https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- With the release of the Asterisk 10 branch, the preceding '1.' has been removed
- from the version number per the blog post available at
-
-
- http://blogs.digium.com/2011/07/21/the-evolution-of-asterisk-or-how-we-arrived-at-asterisk-10/
-
- The release of Asterisk 10 would not have been possible without the support and
- contributions of the community.
-
- You can find an overview of the work involved with the 10.0.0 release in the
- summary:
-
- http://svn.asterisk.org/svn/asterisk/tags/10.0.0/asterisk-10.0.0-summary.txt
-
- A short list of available features includes:
-
- * T.38 gateway functionality has been added to res_fax.
- * Protocol independent out-of-call messaging support. Text messages not
-  associated with an active call can now be routed through the Asterisk
-  dialplan. SIP and XMPP are supported so far.
- * New highly optimized and customizable ConfBridge application capable of mixing
-  audio at sample rates ranging from 8kHz-192kHz
- * Addition of video_mode option in confbridge.conf to provide basic video
-  conferencing in the ConfBridge() dialplan application.
- * Support for defining hints has been added to pbx_lua.
- * Replacement of Berkeley DB with SQLite for the Asterisk Database (AstDB).
- * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
-  http://svn.asterisk.org/svn/asterisk/branches/10/CHANGES
-
- Also, when upgrading a system between major versions, it is imperative that you
- read and understand the contents of the UPGRADE.txt file, which is located at:
-
-  http://svn.asterisk.org/svn/asterisk/branches/10/UPGRADE.txt

* Fri Dec  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.7.rc3
- The Asterisk Development Team has announced the third release candidate of
- Asterisk 10.0.0. This release candidate is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 10.0.0-rc3 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
- * Add ASTSBINDIR to the list of configurable paths
-
-  This patch also makes astdb2sqlite3 and astcanary use the configured
-  directory instead of relying on $PATH.
-
- * Don't crash on INFO automon request with no channel
-
-  AST-2011-014. When automon was enabled in features.conf, it was possible
-  to crash Asterisk by sending an INFO request if no channel had been
-  created yet.
-
- * Fixed crash from orphaned MWI subscriptions in chan_sip
-
-  This patch resolves the issue where MWI subscriptions are orphaned
-  by subsequent SIP SUBSCRIBE messages.
-
- * Fix a change in behavior in 'database show' from 1.8.
-
-  In 1.8 and previous versions, one could use any fullword portion of
-  the key name, including the full key, to obtain the record. Until this
-  patch, this did not work for the full key.
-
- * Default to nat=yes; warn when nat in general and peer differ
-
-  AST-2011-013.  It is possible to enumerate SIP usernames when the general and
-  user/peer nat settings differ in whether to respond to the port a request is
-  sent from or the port listed for responses in the Via header. In 1.4 and
-  1.6.2, this would mean if one setting was nat=yes or nat=route and the other
-  was either nat=no or nat=never. In 1.8 and 10, this would mean when one
-  was nat=force_rport and the other was nat=no.
-
-  In order to address this problem, it was decided to switch the default
-  behavior to nat=yes/force_rport as it is the most commonly used option
-  and to strongly discourage setting nat per-peer/user when at all
-  possible.
-
- * Fixed SendMessage stripping extension from To: header in SIP MESSAGE
-
-  When using the MessageSend application to send a SIP MESSAGE to a
-  non-peer, chan_sip stripped off the extension and failed to add it back
-  to the sip_pvt structure before transmitting. This patch adds the full
-  URI passed in from the message core to the sip_pvt structure.
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.0.0-rc3

* Wed Nov 16 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.6.rc2
- The Asterisk Development Team has announced the second release candidate of
- Asterisk 10.0.0. This release candidate is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 10.0.0-rc2 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
- * Ensure that a null vmexten does not cause a segfault
-
- * Fix issue with ConfBridge participants hanging up during DTMF feature
-  menu usage getting stuck in conference forever
-  (closes issue ASTERISK-18829)
-  Reported by: zvision
-
- * Fix app_macro.c MODULEINFO section termination
-  (closes issue ASTERISK-18848)
-  Reported by: Tony Mountifield
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-10.0.0-rc2

* Fri Nov 11 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.5.rc1
- The Asterisk Development Team is pleased to announce the first release candidate
- of Asterisk 10.0.0. This release candidate is available for immediate download
- at http://downloads.asterisk.org/pub/telephony/asterisk/
-
- All Asterisk users are encouraged to participate in the Asterisk 10 testing
- process. Please report any issues found to the issue tracker,
- https://issues.asterisk.org/jira. It is also very useful to see successful test
- reports. Please post those to the asterisk-dev mailing list.
-
- All Asterisk users are invited to participate in the #asterisk-testing
- channel on IRC to work together in testing the many parts of Asterisk.
-
- Asterisk 10 is the next major release series of Asterisk. It will be a
- Standard support release, similar to Asterisk 1.6.2. For more
- information about support time lines for Asterisk releases, see the Asterisk
- versions page: https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- A short list of features includes:
-
- * T.38 gateway functionality has been added to res_fax.
- * Protocol independent out-of-call messaging support. Text messages not
-  associated with an active call can now be routed through the Asterisk
-  dialplan. SIP and XMPP are supported so far.
- * New highly optimized and customizable ConfBridge application capable of mixing
-  audio at sample rates ranging from 8kHz-192kHz
-  (More information available at
-   https://wiki.asterisk.org/wiki/display/AST/ConfBridge+10 )
- * Addition of video_mode option in confbridge.conf to provide basic video
-  conferencing in the ConfBridge() dialplan application.
- * Support for defining hints has been added to pbx_lua.
- * Replacement of Berkeley DB with SQLite for the Asterisk Database (AstDB).
- * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svnview.digium.com/svn/asterisk/branches/10/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.0.0-rc1

* Tue Oct 18 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.4.beta2
- Add patch from upstream SVN to fix AST-2011-012

* Fri Oct 14 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.3.beta2
- Patch cleanup day

* Thu Sep 29 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.2.beta2
- The Asterisk Development Team is pleased to announce the second beta release of
- Asterisk 10.0.0. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- With the release of the Asterisk 10 branch, the preceding '1.' has been removed
- from the version number per the blog post available at
- http://blogs.digium.com/2011/07/21/the-evolution-of-asterisk-or-how-we-arrived-at-asterisk-10/
-
- All interested users of Asterisk are encouraged to participate in the
- Asterisk 10 testing process. Please report any issues found to the issue
- tracker, https://issues.asterisk.org/jira. It is also very useful to see
- successful test reports. Please post those to the asterisk-dev mailing list.
-
- All Asterisk users are invited to participate in the #asterisk-testing
- channel on IRC to work together in testing the many parts of Asterisk.
-
- Asterisk 10 is the next major release series of Asterisk. It will be a
- Standard support release, similar to Asterisk 1.6.2. For more
- information about support time lines for Asterisk releases, see the Asterisk
- versions page: https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- A short list of features includes:
-
- * T.38 gateway functionality has been added to res_fax.
-
- * Protocol independent out-of-call messaging support. Text messages not
-  associated with an active call can now be routed through the Asterisk
-  dialplan. SIP and XMPP are supported so far.
-
- * New highly optimized and customizable ConfBridge application capable of mixing
-  audio at sample rates ranging from 8kHz-192kHz
-
- * Addition of video_mode option in confbridge.conf to provide basic video
-  conferencing in the ConfBridge() dialplan application.
-
- * Support for defining hints has been added to pbx_lua.
-
- * Replacement of Berkeley DB with SQLite for the Asterisk Database (AstDB).
-
- * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svnview.digium.com/svn/asterisk/branches/10/CHANGES
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.0.0-beta2

* Mon Jul 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 10.0.0-0.1.beta1
-
- The Asterisk Development Team is pleased to announce the first beta release of
- Asterisk 10.0.0-beta1. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- With the release of the Asterisk 10 branch, the preceding '1.' has been removed
- from the version number per the blog post available at
- http://blogs.digium.com/2011/07/21/the-evolution-of-asterisk-or-how-we-arrived-at-asterisk-10/
-
- All interested users of Asterisk are encouraged to participate in the
- Asterisk 10 testing process. Please report any issues found to the issue
- tracker, https://issues.asterisk.org/jira. It is also very useful to see
- successful test reports. Please post those to the asterisk-dev mailing list.
-
- All Asterisk users are invited to participate in the #asterisk-testing
- channel on IRC to work together in testing the many parts of Asterisk.
- Additionally users can make use of the RPM and DEB packages now being built for
- all Asterisk releases. More information available at
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Packages
-
- Asterisk 10 is the next major release series of Asterisk. It will be a
- Standard support release, similar to Asterisk 1.6.2. For more
- information about support time lines for Asterisk releases, see the Asterisk
- versions page: https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- A short list of included features includes:
-
- * T.38 gateway functionality has been added to res_fax.
- * Protocol independent out-of-call messaging support.  Text messages not
-  associated with an active call can now be routed through the Asterisk
-  dialplan.  SIP and XMPP are supported so far.
- * New highly optimized and customizable ConfBridge application capable of mixing
-  audio at sample rates ranging from 8kHz-192kHz
- * Addition of video_mode option in confbridge.conf to provide basic video
-  conferencing in the ConfBridge() dialplan application.
- * Support for defining hints has been added to pbx_lua.
- * Replacement of Berkeley DB with SQLite for the Asterisk Database (AstDB).
- * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/10/CHANGES?view=checkout
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-10.0.0-beta1

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.8.5.0-1.2
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.8.5.0-1.1
- Perl mass rebuild

* Mon Jul 11 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.5.0-1
- The Asterisk Development Team announces the release of Asterisk 1.8.5.0. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.5.0 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * Fix Deadlock with attended transfer of SIP call
-  (Closes issue #18837. Reported, patched by alecdavis. Tested by Irontec, ZX81,
-  cmaj)
-
- * Fixes thread blocking issue in the sip TCP/TLS implementation.
-  (Closes issue #18497. Reported by vois. Patched by dvossel. Tested by vois,
-  rossbeer, kowalma, Freddi_Fonet)
-
- * Be more tolerant of what URI we accept for call completion PUBLISH requests.
-  (Closes issue #18946. Reported by GeorgeKonopacki. Patched by mmichelson)
-
- * Fix a nasty chanspy bug which was causing a channel leak every time a spied on
-  channel made a call.
-  (Closes issue #18742. Reported by jkister. Tested by jcovert, jrose)
-
- * This patch fixes a bug with MeetMe behavior where the 'P' option for always
-  prompting for a pin is ignored for the first caller.
-  (Closes issue #18070. Reported by mav3rick. Patched by bbryant)
-
- * Fix issue where Asterisk does not hangup a channel after endpoint hangs up. If
-  the call that the dialplan started an AGI script for is hungup while the AGI
-  script is in the middle of a command then the AGI script is not notified of
-  the hangup.
-  (Closes issue #17954, #18492. Reported by mn3250, devmod. Patched by rmudgett)
-
- * Resolve issue where leaving a voicemail, the MWI message is never sent. The
-  same thing happens when checking a voicemail and marking it as read.
-  (Closes issue ASTERISK-18002. Reported by Leif Madsen. Resolved by Richard
-  Mudgett)
-
- * Resolve issue where wait for leader with Music On Hold allows crosstalk
-  between participants. Parenthesis in the wrong position. Regression from issue
-  #14365 when expanding conference flags to use 64 bits.
-  (Closes issue #18418. Reported by MrHanMan. Patched by rmudgett)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.5.0

* Thu Jul  7 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.5-0.2
- Rebuild for net-snmp 5.7

* Fri Jul  1 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.5-0.1.rc1
- Fix systemd dependencies in EL6 and F15

* Thu Jun 30 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.5-0.1.rc1
- The Asterisk Development Team has announced the first release candidate of
- Asterisk 1.8.5. This release candidate is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.5-rc1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
- * Fix Deadlock with attended transfer of SIP call
-  (Closes issue #18837. Reported, patched by alecdavis. Tested by Irontec, ZX81,
-   cmaj)
-
- * Fixes thread blocking issue in the sip TCP/TLS implementation.
-  (Closes issue #18497. Reported by vois. Patched by dvossel. Tested by vois,
-   rossbeer, kowalma, Freddi_Fonet)
-
- * Be more tolerant of what URI we accept for call completion PUBLISH requests.
-  (Closes issue #18946. Reported by GeorgeKonopacki. Patched by mmichelson)
-
- * Fix a nasty chanspy bug which was causing a channel leak every time a spied on
-  channel made a call.
-  (Closes issue #18742. Reported by jkister. Tested by jcovert, jrose)
-
- * This patch fixes a bug with MeetMe behavior where the 'P' option for always
-  prompting for a pin is ignored for the first caller.
-  (Closes issue #18070. Reported by mav3rick. Patched by bbryant)
-
- * Fix issue where Asterisk does not hangup a channel after endpoint hangs up. If
-  the call that the dialplan started an AGI script for is hungup while the AGI
-  script is in the middle of a command then the AGI script is not notified of
-  the hangup.
-  (Closes issue #17954, #18492. Reported by mn3250, devmod. Patched by rmudgett)
-
- * Resolve issue where leaving a voicemail, the MWI message is never sent. The
-  same thing happens when checking a voicemail and marking it as read.
-  (Closes issue ASTERISK-18002. Reported by Leif Madsen. Resolved by Richard
-   Mudgett)
-
- * Resolve issue where wait for leader with Music On Hold allows crosstalk
-  between participants. Parenthesis in the wrong position. Regression from issue
-  #14365 when expanding conference flags to use 64 bits.
-  (Closes issue #18418. Reported by MrHanMan. Patched by rmudgett)
-
- * Fix timerfd locking issue.
-  (Closes ASTERISK-17867, ASTERISK-17415. Patched by kobaz)
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.5-rc1

* Thu Jun 30 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.4-2
- Fedora Directory Server -> 389 Directory Server

* Wed Jun 29 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.4-1
- The Asterisk Development Team has announced the release of Asterisk
- versions 1.4.41.2, 1.6.2.18.2, and 1.8.4.4, which are security
- releases.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.4.41.2, 1.6.2.18.2, and 1.8.4.4 resolves the
- following issue:
-
- AST-2011-011: Asterisk may respond differently to SIP requests from an
- invalid SIP user than it does to a user configured on the system, even
- when the alwaysauthreject option is set in the configuration. This can
- leak information about what SIP users are valid on the Asterisk
- system.
-
- For more information about the details of this vulnerability, please
- read the security advisory AST-2011-011, which was released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.41.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.18.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.4.4
-
- Security advisory AST-2011-011 is available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-011.pdf

* Mon Jun 27 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.3-3
- Don't forget stereorize

* Mon Jun 27 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.3-2
- Move /var/run/asterisk to /run/asterisk
- Add comments to systemd service file on how to mimic safe_asterisk functionality
- Build more of the optional binaries
- Install the tmpfiles.d configuration on Fedora 15

* Fri Jun 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.3-1
- The Asterisk Development Team has announced the release of Asterisk versions
- 1.4.41.1, 1.6.2.18.1, and 1.8.4.3, which are security releases.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.4.41.1, 1.6.2.18, and 1.8.4.3 resolves several issues
- as outlined below:
-
- * AST-2011-008: If a remote user sends a SIP packet containing a null,
-  Asterisk assumes available data extends past the null to the
-  end of the packet when the buffer is actually truncated when
-  copied.  This causes SIP header parsing to modify data past
-  the end of the buffer altering unrelated memory structures.
-  This vulnerability does not affect TCP/TLS connections.
-  -- Resolved in 1.6.2.18.1 and 1.8.4.3
-
- * AST-2011-009: A remote user sending a SIP packet containing a Contact header
-  with a missing left angle bracket (<) causes Asterisk to
-  access a null pointer.
-  -- Resolved in 1.8.4.3
-
- * AST-2011-010: A memory address was inadvertently transmitted over the
-  network via IAX2 via an option control frame and the remote party would try
-  to access it.
-  -- Resolved in 1.4.41.1, 1.6.2.18.1, and 1.8.4.3
-
- The issues and resolutions are described in the AST-2011-008, AST-2011-009, and
- AST-2011-010 security advisories.
-
- For more information about the details of these vulnerabilities, please read
- the security advisories AST-2011-008, AST-2011-009, and AST-2011-010, which were
- released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.41.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.18.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.4.3
-
- Security advisories AST-2011-008, AST-2011-009, and AST-2011-010 are available
- at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-008.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-009.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-010.pdf

* Tue Jun 21 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.2-2
- Convert to systemd

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8.4.2-1.2
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8.4.2-1.1
- Perl 5.14 mass rebuild

* Fri Jun  3 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.4.2-1:
-
- The Asterisk Development Team has announced the release of Asterisk
- version 1.8.4.2, which is a security release for Asterisk 1.8.
-
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.8.4.2 resolves an issue with SIP URI
- parsing which can lead to a remotely exploitable crash:
-
-    Remote Crash Vulnerability in SIP channel driver (AST-2011-007)
-
- The issue and resolution is described in the AST-2011-007 security
- advisory.
-
- For more information about the details of this vulnerability, please
- read the security advisory AST-2011-007, which was released at the
- same time as this announcement.
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.4.2
-
- Security advisory AST-2011-007 is available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-007.pdf
-
- The Asterisk Development Team has announced the release of Asterisk 1.8.4.1.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.4.1 resolves several issues reported by the
- community. Without your help this release would not have been possible.
- Thank you!
-
- Below is a list of issues resolved in this release:
-
-  * Fix our compliance with RFC 3261 section 18.2.2. (aka Cisco phone fix)
-   (Closes issue #18951. Reported by jmls. Patched by wdoekes)
-
-  * Resolve a change in IPv6 header parsing due to the Cisco phone fix issue.
-   This issue was found and reported by the Asterisk test suite.
-   (Closes issue #18951. Patched by mnicholson)
-
-  * Resolve potential crash when using SIP TLS support.
-   (Closes issue #19192. Reported by stknob. Patched by Chainsaw. Tested by
-    vois, Chainsaw)
-
-  * Improve reliability when using SIP TLS.
-   (Closes issue #19182. Reported by st. Patched by mnicholson)
-
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.4.1

- The Asterisk Development Team has announced the release of Asterisk 1.8.4. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.4 resolves several issues reported by the community.
- Without your help this release would not have been possible. Thank you!
-
- Below is a sample of the issues resolved in this release:
-
-  * Use SSLv23_client_method instead of old SSLv2 only.
-   (Closes issue #19095, #19138. Reported, patched by tzafrir. Tested by russell
-   and chazzam.
-
-  * Resolve crash in ast_mutex_init()
-   (Patched by twilson)
-
-  * Resolution of several DTMF based attended transfer issues.
-   (Closes issue #17999, #17096, #18395, #17273. Reported by iskatel, gelo,
-   shihchuan, grecco. Patched by rmudgett)
-
-   NOTE: Be sure to read the ChangeLog for more information about these changes.
-
-  * Resolve deadlocks related to device states in chan_sip
-   (Closes issue #18310. Reported, patched by one47. Patched by jpeeler)
-
-  * Resolve an issue with the Asterisk manager interface leaking memory when
-   disabled.
-   (Reported internally by kmorgan. Patched by russellb)
-
-  * Support greetingsfolder as documented in voicemail.conf.sample.
-   (Closes issue #17870. Reported by edhorton. Patched by seanbright)
-
-  * Fix channel redirect out of MeetMe() and other issues with channel softhangup
-   (Closes issue #18585. Reported by oej. Tested by oej, wedhorn, russellb.
-   Patched by russellb)
-
-  * Fix voicemail sequencing for file based storage.
-   (Closes issue #18498, #18486. Reported by JJCinAZ, bluefox. Patched by
-   jpeeler)
-
-  * Set hangup cause in local_hangup so the proper return code of 486 instead of
-   503 when using Local channels when the far sides returns a busy. Also affects
-   CCSS in Asterisk 1.8+.
-   (Patched by twilson)
-
-  * Fix issues with verbose messages not being output to the console.
-   (Closes issue #18580. Reported by pabelanger. Patched by qwell)
-
-  * Fix Deadlock with attended transfer of SIP call
-   (Closes issue #18837. Reported, patched by alecdavis. Tested by
-   alecdavid, Irontec, ZX81, cmaj)
-
- Includes changes per AST-2011-005 and AST-2011-006
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.4
-
- Information about the security releases are available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-005.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-006.pdf

* Thu Apr 21 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3.3-1
- The Asterisk Development Team has announced security releases for Asterisk
- branches 1.4, 1.6.1, 1.6.2, and 1.8. The available security releases are
- released as versions 1.4.40.1, 1.6.1.25, 1.6.2.17.3, and 1.8.3.3.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The releases of Asterisk 1.4.40.1, 1.6.1.25, 1.6.2.17.3, and 1.8.3.3 resolve two
- issues:
-
- * File Descriptor Resource Exhaustion (AST-2011-005)
- * Asterisk Manager User Shell Access (AST-2011-006)
-
- The issues and resolutions are described in the AST-2011-005 and AST-2011-006
- security advisories.
-
- For more information about the details of these vulnerabilities, please read the
- security advisories AST-2011-005 and AST-2011-006, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.40.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.25
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.17.3
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.3.3
-
- Security advisory AST-2011-005 and AST-2011-006 are available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-005.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-006.pdf

* Wed Mar 23 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3.2-2
- Bump release and rebuild for mysql 5.5.10 soname change.

* Thu Mar 17 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3.2-1
- The Asterisk Development Team has announced security releases for Asterisk
- branches 1.6.1, 1.6.2, and 1.8. The available security releases are
- released as versions 1.6.1.24, 1.6.2.17.2, and 1.8.3.2.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- ** This is a re-release of Asterisk 1.6.1.23, 1.6.2.17.1 and 1.8.3.1 which
-   contained a bug which caused duplicate manager entries (issue #18987).
-
- The releases of Asterisk 1.6.1.24, 1.6.2.17.2, and 1.8.3.2 resolve two issues:
-
-  * Resource exhaustion in Asterisk Manager Interface (AST-2011-003)
-  * Remote crash vulnerability in TCP/TLS server (AST-2011-004)
-
- The issues and resolutions are described in the AST-2011-003 and AST-2011-004
- security advisories.
-
- For more information about the details of these vulnerabilities, please read the
- security advisories AST-2011-003 and AST-2011-004, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.24
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.17.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.3.2
-
- Security advisory AST-2011-003 and AST-2011-004 are available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-003.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-004.pdf

* Thu Mar 17 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3.1-1
- The Asterisk Development Team has announced security releases for Asterisk
- branches 1.6.1, 1.6.2, and 1.8. The available security releases are
- released as versions 1.6.1.23, 1.6.2.17.1, and 1.8.3.1.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The releases of Asterisk 1.6.1.23, 1.6.2.17.1, and 1.8.3.1 resolve two issues:
-
-  * Resource exhaustion in Asterisk Manager Interface (AST-2011-003)
-  * Remote crash vulnerability in TCP/TLS server (AST-2011-004)
-
- The issues and resolutions are described in the AST-2011-003 and AST-2011-004
- security advisories.
-
- For more information about the details of these vulnerabilities, please read the
- security advisories AST-2011-003 and AST-2011-004, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.23
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.17.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.3.1
-
- Security advisory AST-2011-003 and AST-2011-004 are available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-003.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-004.pdf

* Mon Feb 28 2011  <jeff@ocjtech.us> - 1.8.3-1
- The Asterisk Development Team has announced the release of Asterisk 1.8.3. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.3 resolves several issues reported by the community
- and would have not been possible without your participation. Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * Resolve duplicated data in the AstDB when using DIALGROUP()
-  (Closes issue #18091. Reported by bunny. Patched by tilghman)
-
- * Ensure the ipaddr field in realtime is large enough to handle IPv6 addresses.
-  (Closes issue #18464. Reported, patched by IgorG)
-
- * Reworking parsing of mwi => lines to resolve a segfault. Also add a set of
-  unit tests for the function that does the parsing.
-  (Closes issue #18350. Reported by gbour. Patched by Marquis)
-
- * When using cdr_pgsql the billsec field was not populated correctly on
-  unanswered calls.
-  (Closes issue #18406. Reported by joscas. Patched by tilghman)
-
- * Resolve memory leak in iCalendar and Exchange calendaring modules.
-  (Closes issue #18521. Reported, patched by pitel. Tested by cervajs)
-
- * This version of Asterisk includes the new Compiler Flags option
-  BETTER_BACKTRACES which uses libbfd to search for better symbol information
-  within both the Asterisk binary, as well as loaded modules, to assist when
-  using inline backtraces to track down problems.
-  (Patched by tilghman)
-
- * Resolve issue where no Music On Hold may be triggered when using
-  res_timing_dahdi.
-  (Closes issues #18262. Reported by francesco_r. Patched by cjacobson. Tested
-  by francesco_r, rfrantik, one47)
-
- * Resolve a memory leak when the Asterisk Manager Interface is disabled.
-  (Reported internally by kmorgan. Patched by russellb)
-
- * Reimplemented fax session reservation to reverse the ABI breakage introduced
-  in r297486.
-  (Reported internally. Patched by mnicholson)
-
- * Fix regression that changed behavior of queues when ringing a queue member.
-  (Closes issue #18747, #18733. Reported by vrban. Patched by qwell.)
-
- * Resolve deadlock involving REFER.
-  (Closes issue #18403. Reported, tested by jthurman. Patched by jpeeler.)
-
- Additionally, this release has the changes related to security bulletin
- AST-2011-002 which can be found at
- http://downloads.asterisk.org/pub/security/AST-2011-002.pdf
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.3

* Wed Feb 16 2011  <jeff@ocjtech.us> - 1.8.3-0.7.rc3
-
- The Asterisk Development Team has announced the third release candidate of
- Asterisk 1.8.3. This release candidate is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.3-rc3 resolves the following issues in addition to
- those included in 1.8.3-rc1 and 1.8.3-rc2:
-
- *  Fix regression that changed behavior of queues when ringing a queue member.
-   (Closes issue #18747, #18733. Reported by vrban. Patched by qwell.)
-
- * Resolve deadlock involving REFER.
-  (Closes issue #18403. Reported, tested by jthurman. Patched by jpeeler.)
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.3-rc3

* Fri Feb 11 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3-0.6.rc2
- Bump release to build for F15

* Wed Feb  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3-0.5.rc2
- Remove isa macros

* Wed Feb  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3-0.4.rc2
- Make library dependencies architecture specific

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3-0.2.rc2
The Asterisk Development Team has announced the second release candidate of
Asterisk 1.8.3. This release candidate is available for immediate download at
http://downloads.asterisk.org/pub/telephony/asterisk/

The release of Asterisk 1.8.3-rc2 resolves the following issues in addition to
those included in 1.8.3-rc1:

 * Resolve issue where no Music On Hold may be triggered when using
  res_timing_dahdi.
  (Closes issues #18262. Reported by francesco_r. Patched by cjacobson. Tested
   by francesco_r, rfrantik, one47)

 * Resolve a memory leak when the Asterisk Manager Interface is disabled.
  (Reported internally by kmorgan. Patched by russellb)

 * Reimplemented fax session reservation to reverse the ABI breakage introduced
  in r297486.
  (Reported internally. Patched by mnicholson)

For a full list of changes in this release candidate, please see the ChangeLog:

http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.3-rc2

* Wed Jan 26 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.3-0.1.rc1
-
- The Asterisk Development Team has announced the first release candidate of
- Asterisk 1.8.3. This release candidate is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.3-rc1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
-  * Resolve duplicated data in the AstDB when using DIALGROUP()
-   (Closes issue #18091. Reported by bunny. Patched by tilghman)
-
-  * Ensure the ipaddr field in realtime is large enough to handle IPv6 addresses.
-   (Closes issue #18464. Reported, patched by IgorG)
-
-  * Reworking parsing of mwi => lines to resolve a segfault. Also add a set of
-   unit tests for the function that does the parsing.
-   (Closes issue #18350. Reported by gbour. Patched by Marquis)
-
-  * When using cdr_pgsql the billsec field was not populated correctly on
-   unanswered calls.
-   (Closes issue #18406. Reported by joscas. Patched by tilghman)
-
-  * Resolve memory leak in iCalendar and Exchange calendaring modules.
-   (Closes issue #18521. Reported, patched by pitel. Tested by cervajs)
-
-  * This version of Asterisk includes the new Compiler Flags option
-   BETTER_BACKTRACES which uses libbfd to search for better symbol information
-   within both the Asterisk binary, as well as loaded modules, to assist when
-   using inline backtraces to track down problems.
-   (Patched by tilghman)

* Wed Jan 26 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.2.3-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.8.2.3.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.2.3 resolves the following issue:
-
-  * Reimplemented fax session reservation to reverse the ABI breakage introduced
-   in r297486.
-   (Reported by Jeremy Kister on the asterisk-users mailing list. Patched by
-   mnicholson)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.2.3

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.2.2-2
- Build with SRTP support

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.2.2-1
-
- The Asterisk Development Team has announced a release for the security issue
- described in AST-2011-001.
-
- Due to a failed merge, Asterisk 1.8.2.1 which should have included the security
- fix did not. Asterisk 1.8.2.2 contains the the changes which should have been
- included in Asterisk 1.8.2.1.
-
- This releases is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The releases of Asterisk 1.4.38.1, 1.4.39.1, 1.6.1.21, 1.6.2.15.1, 1.6.2.16.2,
- 1.8.1.2, and 1.8.2.2 resolve an issue when forming an outgoing SIP request while
- in pedantic mode, which can cause a stack buffer to be made to overflow if
- supplied with carefully crafted caller ID information. The issue and resolution
- are described in the AST-2011-001 security advisory.
-
- For more information about the details of this vulnerability, please read the
- security advisory AST-2011-001, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.2.2
-
- Security advisory AST-2011-001 is available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-001.pdf

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.2.1-1
-
- The Asterisk Development Team has announced security releases for the following
- versions of Asterisk:
-
- * 1.4.38.1
- * 1.4.39.1
- * 1.6.1.21
- * 1.6.2.15.1
- * 1.6.2.16.1
- * 1.8.1.2
- * 1.8.2.1
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The releases of Asterisk 1.4.38.1, 1.4.39.1, 1.6.1.21, 1.6.2.15.1, 1.6.2.16.2,
- 1.8.1.2, and 1.8.2.1 resolve an issue when forming an outgoing SIP request while
- in pedantic mode, which can cause a stack buffer to be made to overflow if
- supplied with carefully crafted caller ID information. The issue and resolution
- are described in the AST-2011-001 security advisory.
-
- For more information about the details of this vulnerability, please read the
- security advisory AST-2011-001, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.38.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.39.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.21
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.15.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.16.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.1.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.2.1
-
- Security advisory AST-2011-001 is available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-001.pdf

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.2-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.8.2. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.2 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * 'sip notify clear-mwi' needs terminating CRLF.
-  (Closes issue #18275. Reported, patched by klaus3000)
-
- * Patch for deadlock from ordering issue between channel/queue locks in
-  app_queue (set_queue_variables).
-  (Closes issue #18031. Reported by rain. Patched by bbryant)
-
- * Fix cache of device state changes for multiple servers.
-  (Closes issue #18284, #18280. Reported, tested by klaus3000. Patched, tested
-  by russellb)
-
- * Resolve issue where channel redirect function (CLI or AMI) hangs up the call
-  instead of redirecting the call.
-  (Closes issue #18171. Reported by: SantaFox)
-  (Closes issue #18185. Reported by: kwemheuer)
-  (Closes issue #18211. Reported by: zahir_koradia)
-  (Closes issue #18230. Reported by: vmarrone)
-  (Closes issue #18299. Reported by: mbrevda)
-  (Closes issue #18322. Reported by: nerbos)
-
- * Fix reloading of peer when a user is requested. Prevent peer reloading from
-  causing multiple MWI subscriptions to be created when using realtime.
-  (Closes issue #18342. Reported, patched by nivek.)
-
- * Fix XMPP PubSub-based distributed device state. Initialize pubsubflags to 0
-  so res_jabber doesn't think there is already an XMPP connection sending
-  device state. Also clean up CLI commands a bit.
-  (Closes issue #18272. Reported by klaus3000. Patched by Marquis42)
-
- * Don't crash after Set(CDR(userfield)=...) in ast_bridge_call. Instead of
-  setting peer->cdr = NULL, set it to not post.
-  (Closes issue #18415. Reported by macbrody. Patched, tested by jsolares)
-
- * Fixes issue with outbound google voice calls not working. Thanks to az1234
-  and nevermind_quack for their input in helping debug the issue.
-  (Closes issue #18412. Reported by nevermind_quack. Patched by dvossel)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.2

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.1.1-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.8.1.1.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.1.1 resolves two issues reported by the community
- since the release of Asterisk 1.8.1.
-
-  * Don't crash after Set(CDR(userfield)=...) in ast_bridge_call. Instead of
-   setting peer->cdr = NULL, set it to not post.
-   (Closes issue #18415. Reported by macbrody. Patched, tested by jsolares)
-
-  * Fixes issue with outbound google voice calls not working. Thanks to az1234
-   and nevermind_quack for their input in helping debug the issue.
-   (Closes issue #18412. Reported by nevermind_quack. Patched by dvossel)
-
- For a full list of changes in this release candidate, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.1.1

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.1-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.8.1. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.8.1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * Fix issue when using directmedia. Asterisk needs to limit the codecs offered
-   to just the ones that both sides recognize, otherwise they may end up sending
-   audio that the other side doesn't understand.
-   (Closes issue #17403. Reported, patched by one47. Tested by one47, falves11)
-
- * Resolve issue where Party A in an analog 3-way call would continue to hear
-   ringback after party C answers.
-   (Patched by rmudgett)
-
- * Fix playback failure when using IAX with the timerfd module.
-   (Closes issue #18110. Reported, tested by tpanton. Patched by jpeeler)
-
- * Fix problem with qualify option packets for realtime peers never stopping.
-   The option packets not only never stopped, but if a realtime peer was not in
-   the peer list multiple options dialogs could accumulate over time.
-   (Closes issue #16382. Reported by lftsy. Tested by zerohalo. Patched by
-   jpeeler)
-
- * Fix issue where it is possible to crash Asterisk by feeding the curl engine
-   invalid data.
-   (Closes issue #18161. Reported by wdoekes. Patched by tilghman)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.1

* Tue Jan 18 2011 Dennis Gilmore <dennis@ausil.us> - 1.8.0-6
- dont package up the ices bits on el the client doesnt exist for us

* Tue Jan 18 2011 Dennis Gilmore <dennis@ausil.us> - 1.8.0-5
- dont build the 389 directory server package its not available on rhel6

* Fri Dec 10 2010 Dennis Gilmore <dennis@ausil.us> - 1.8.0-4
- dont always build AIS modules we dont have the BuildRequires on epel

* Fri Oct 29 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-3
- Rebuild for new net-snmp.

* Tue Oct 26 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-2
- Always build AIS modules

* Thu Oct 21 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-1
- The Asterisk Development Team is proud to announce the release of Asterisk
- 1.8.0. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- Asterisk 1.8 is the next major release series of Asterisk. It will be a Long
- Term Support (LTS) release, similar to Asterisk 1.4. For more information about
- support time lines for Asterisk releases, see the Asterisk versions page.
-
- http://www.asterisk.org/asterisk-versions
-
- The release of Asterisk 1.8.0 would not have been possible without the support
- and contributions of the community. Since Asterisk 1.6.2, we've had over 500
- reporters, more than 300 testers and greater than 200 developers contributed to
- this release.
-
- You can find a summary of the work involved with the 1.8.0 release in the
- sumary:
-
- http://svn.asterisk.org/svn/asterisk/tags/1.8.0/asterisk-1.8.0-summary.txt
-
- A short list of available features includes:
-
-     * Secure RTP
-     * IPv6 Support in the SIP channel driver
-     * Connected Party Identification Support
-     * Calendaring Integration
-     * A new call logging system, Channel Event Logging (CEL)
-     * Distributed Device State using Jabber/XMPP PubSub
-     * Call Completion Supplementary Services support
-     * Advice of Charge support
-     * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=markup
-
- For a full list of changes in the current release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0
-
- Thank you for your continued support of Asterisk!

* Mon Oct 18 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.8.rc5:
-
- The release of Asterisk 1.8.0-rc5 was triggered by some last minute platform
- compatibility IPv6 changes. In addition, the availability of the English sound
- prompts with Australian accents has been added.
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=markup
-
- For a full list of changes in the current release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-rc5
-
- This release candidate contains fixes since the last release candidate as
- reported by the community. A sampling of the changes in this release candidate
- include:
-
-  * Additional fixups in chan_gtalk that allow outbound calls to both Google
-    Talk and Google Voice recipients. Adds new chan_gtalk enhancements externip
-    and stunaddr.
-    (Closes issue #13971. Patched by dvossel)
-
-  * Resolve manager crash issue.
-    (Closes issue #17994. Reported by vrban. Patchd by dvossel)
-
-  * Documentation updates for sample configuration files.
-    (Closes issues #18107, #18101. Reported, patched by lathama, lmadsen)
-
-  * Resolve issue where faxdetect would only detect the first fax call in
-    chan_dahdi.
-    (Closes issue #18116. Reported by seandarcy. Patched by rmudgett)
-
-  * Resolve issue where a channel that is setup and torn down *very* quickly may
-    not have the right call disposition or ${DIALSTATUS}.
-    (Closes issue #16946. Reported by davidw. Review
-     https://reviewboard.asterisk.org/r/740/)
-
-  * Set TCLASS field of IPv6 header when SIP QoS options are set.
-    (Closes issue #18099. Reported by jamesnet. Patched by dvossel)
-
-  * Resolve issue where Asterisk could crash on shutdown when using SRTP.
-    (Closes issue #18085. Reported by st. Patched by twilson)
-
-  * Fix issue where peers host port would be lost on a SIP reload.
-    (Closes issue #18135. Reported, tested by lmadsen. Patched by dvossel)
-
- A short list of available features includes:
-
-   * Secure RTP
-   * IPv6 Support in the SIP channel driver
-   * Connected Party Identification Support
-   * Calendaring Integration
-   * A new call logging system, Channel Event Logging (CEL)
-   * Distributed Device State using Jabber/XMPP PubSub
-   * Call Completion Supplementary Services support
-   * Advice of Charge support
-   * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=markup
-
- For a full list of changes in the current release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-rc4

* Fri Oct  8 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.7.rc3
- This release candidate contains fixes since the release candidate as reported by
- the community. A sampling of the changes in this release candidate include:
-
-  * Still build chan_sip even if res_crypto cannot be built (use, but not depend)
-    (Reported by a user on the mailing list. Patched by tilghman)
-
-  * Get notifications for call files only when a file is closed, not when created
-    (Closes issue #17924. Reported by mkeuter. Patched by abeldeck)
-
-  * Fixes to chan_gtalk to allow outbound DTMF support to work correctly. Gtalk
-    expects the DTMF to arrive on the RTP stream and not via jingle DTMF
-    signalling.
-    (Patched by dvossel. Tested by malcolmd)
-
-  * Fixes to allow chan_gtalk to communicate with the Gmail web client.
-    (Patched by phsultan and dvossel)
-
-  * Fix to GET DATA to allow audio to be streamed via an AGI.
-    (Closes issue #18001. Reported by jamicque. Patched by tilghman)
-
-  * Resolve dnsmgr memory corruption in chan_iax2.
-    (Closes issue #17902. Reported by afried. Patched by russell, dvossel)
-
- A short list of available features includes:
-
-  * Secure RTP
-  * IPv6 Support in the SIP channel driver
-  * Connected Party Identification Support
-  * Calendaring Integration
-  * A new call logging system, Channel Event Logging (CEL)
-  * Distributed Device State using Jabber/XMPP PubSub
-  * Call Completion Supplementary Services support
-  * Advice of Charge support
-  * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=checkout
-
- For a full list of changes in the current release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-rc3

* Wed Oct  6 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.6.rc2
- This release candidate contains fixes since the last beta release as reported by
- the community. A sampling of the changes in this release candidate include:
-
-  * Add slin16 support for format_wav (new wav16 file extension)
-    (Closes issue #15029. Reported, patched by andrew. Tested by Qwell)
-
-  * Fixes a bug in manager.c where the default configuration values weren't reset
-    when the manager configuration was reloaded.
-    (Closes issue #17917. Reported by lmadsen. Patched by bbryant)
-
-  * Various fixes for the calendar modules.
-    (Patched by Jan Kalab.
-     Reviewboard: https://reviewboard.asterisk.org/r/880/
-     Closes issue #17877. Review: https://reviewboard.asterisk.org/r/916/
-     Closes issue #17776. Review: https://reviewboard.asterisk.org/r/921/)
-
-  * Add CHANNEL(checkhangup) to check whether a channel is in the process of
-    being hung up.
-    (Closes issue #17652. Reported, patched by kobaz)
-
-  * Fix a bug with MeetMe where after announcing the amount of time left in a
-    conference, if music on hold was playing, it doesn't restart.
-    (Closes issue #17408, Reported, patched by sysreq)
-
-  * Fix interoperability problems with session timer behavior in Asterisk.
-    (Closes issue #17005. Reported by alexcarey. Patched by dvossel)
-
-  * Rate limit calls to fsync() to 1 per second after astdb updates. Astdb was
-    determined to be one of the most significant bottlenecks in SIP registration
-    processing. This patch improved the speed of an astdb load test by 50000%
-    (yes, Fifty-Thousand Percent). On this particular load test setup, this
-    doubled the number of SIP registrations the server could handle.
-    (Review: https://reviewboard.asterisk.org/r/825/)
-
-  * Don't clear the username from a realtime database when a registration
-    expires. Non-realtime chan_sip does not clear the username from memory when a
-    registration expiries so realtime probably shouldn't either.
-    (Closes issue #17551. Reported, patched by: ricardolandim. Patched by
-     mnicholson)
-
-  * Don't hang up a call on an SRTP unprotect failure. Also make it more obvious
-    when there is an issue en/decrypting.
-    (Closes issue #17563. Reported by Alexcr. Patched by sfritsch. Tested by
-     twilson)
-
-  * Many more issues. This is a significant upgrade over Asterisk 1.8.0 beta 5!
-
- A short list of available features includes:
-
-  * Secure RTP
-  * IPv6 Support in the SIP channel driver
-  * Connected Party Identification Support
-  * Calendaring Integration
-  * A new call logging system, Channel Event Logging (CEL)
-  * Distributed Device State using Jabber/XMPP PubSub
-  * Call Completion Supplementary Services support
-  * Advice of Charge support
-  * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=checkout
-
- For a full list of changes in the current release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-rc2

* Thu Sep  9 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.5.beta5
- This release contains fixes since the last beta release as reported by the
- community. A sampling of the changes in this release include:
-
-  * Fix issue where TOS is no longer set on RTP packets.
-    (Closes issue #17890. Reported, patched by elguero)
-
-  * Change pedantic default value in chan_sip from 'no' to 'yes'
-
-  * Asterisk now dynamically builds the "Supported" header depending on what is
-    enabled/disabled in sip.conf. Session timers used to always be advertised as
-    being supported even when they were disabled in the configuration.
-    (Related to issue #17005. Patched by dvossel)
-
-  * Convert MOH to use generic timers.
-    (Closes issue #17726. Reported by lmadsen. Patched by tilghman)
-
-  * Fix SRTP for changing SSRC and multiple a=crypto SDP lines. Adding code to
-    Asterisk that changed the SSRC during bridges and masquerades broke SRTP
-    functionality. Also broken was handling the situation where an incoming
-    INVITE had more than one crypto offer.
-    (Closes issue #17563. Reported by Alexcr. Patched by twilson)
-
- Asterisk 1.8 contains many new features over previous releases of Asterisk.
- A short list of included features includes:
-
-     * Secure RTP
-     * IPv6 Support in the SIP Channel
-     * Connected Party Identification Support
-     * Calendaring Integration
-     * A new call logging system, Channel Event Logging (CEL)
-     * Distributed Device State using Jabber/XMPP PubSub
-     * Call Completion Supplementary Services support
-     * Advice of Charge support
-     * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=checkout
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-beta5

* Tue Aug 24 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.4.beta4
- This release contains fixes since the last beta release as reported by the
- community. A sampling of the changes in this release include:
-
-  * Fix parsing of IPv6 address literals in outboundproxy
-    (Closes issue #17757. Reported by oej. Patched by sperreault)
-
-  * Change the default value for alwaysauthreject in sip.conf to "yes".
-    (Closes issue #17756. Reported by oej)
-
-  * Remove current STUN support from chan_sip.c. This change removes the current
-    broken/useless STUN support from chan_sip.
-    (Closes issue #17622. Reported by philipp2.
-     Review: https://reviewboard.asterisk.org/r/855/)
-
-  * PRI CCSS may use a stale dial string for the recall dial string. If an
-    outgoing call negotiates a different B channel than initially requested, the
-    saved original dial string was not transferred to the new B channel. CCSS
-    uses that dial string to generate the recall dial string.
-    (Patched by rmudgett)
-
-  * Split _all_ arguments before parsing them. This fixes multicast RTP paging
-    using linksys mode.
-    (Patched by russellb)
-
-  * Expand cel_custom.conf.sample. Include the usage of CSV_QUOTE() to ensure
-    data has valid CSV formatting. Also list the special CEL variables that are
-    available for use in the mapping. There are also several other CEL fixes in
-    this release.
-    (Patched by russellb)
-
- Asterisk 1.8 contains many new features over previous releases of Asterisk.
- A short list of included features includes:
-
-     * Secure RTP
-     * IPv6 Support in the SIP Channel
-     * Connected Party Identification Support
-     * Calendaring Integration
-     * A new call logging system, Channel Event Logging (CEL)
-     * Distributed Device State using Jabber/XMPP PubSub
-     * Call Completion Supplementary Services support
-     * Advice of Charge support
-     * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=checkout
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-beta4

* Wed Aug 11 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.3.beta3
-
- This release contains fixes since the last beta release as reported by the
- community. A sampling of the changes in this release include:
-
-  * Fix a regression where HTTP would always be enabled regardless of setting.
-    (Closes issue #17708. Reported, patched by pabelanger)
-
-  * ACL errors displayed on screen when using dynamic_exclude_static in sip.conf
-    (Closes issue #17717. Reported by Dennis DeDonatis. Patched by mmichelson)
-
-  * Support "channels" in addition to "channel" in chan_dahdi.conf.
-    (https://reviewboard.asterisk.org/r/804)
-
-  * Fix parsing error in sip_sipredirect(). The code was written in a way that
-    did a bad job of parsing the port out of a URI. Specifically, it would do
-    badly when dealing with an IPv6 address.
-    (Closes issue #17661. Reported by oej. Patched by mmichelson)
-
-  * Fix inband DTMF detection on outgoing ISDN calls.
-    (Patched by russellb and rmudgett)
-
-  * Fixes issue with translator frame not getting freed. This issue prevented
-    g729 licenses from being freed up.
-    (Closes issue #17630. Reported by manvirr. Patched by dvossel)
-
-  * Fixed IPv6-related SIP parsing bugs and updated documention.
-    (Reported by oej. Patched by sperreault)
-
-  * Add new, self-contained feature FIELDNUM(). Returns a 1-based index into a
-    list of a specified item. Matches up with FIELDQTY() and CUT().
-    (Closes #17713. Reported, patched by gareth. Tested by tilghman)
-
- Asterisk 1.8 contains many new features over previous releases of Asterisk.
- A short list of included features includes:
-
-     * Secure RTP
-     * IPv6 Support
-     * Connected Party Identification Support
-     * Calendaring Integration
-     * A new call logging system, Channel Event Logging (CEL)
-     * Distributed Device State using Jabber/XMPP PubSub
-     * Call Completion Supplementary Services support
-     * Advice of Charge support
-     * Much, much more!
-
- A full list of new features can be found in the CHANGES file.
-
- http://svn.digium.com/view/asterisk/branches/1.8/CHANGES?view=checkout
-
- For a full list of changes in the current release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.8.0-beta3

* Mon Aug  2 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.2.beta2
- Rebuild against libpri 1.4.12

* Mon Aug  2 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.8.0-0.1.beta2
- Update to 1.8.0-beta2
- Disable building chan_misdn until compilation errors are figured out (https://issues.asterisk.org/view.php?id=14333)
- Start stripping tarballs again because Digium added MP3 code :(

* Sat Jul 31 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.10-1
-
- The following are a few of the issues resolved by community developers:
-
-  * Allow users to specify a port for DUNDI peers.
-    (Closes issue #17056. Reported, patched by klaus3000)
-
-  * Decrease the module ref count in sip_hangup when SIP_DEFER_BYE_ON_TRANSFER is
-    set.
-    (Closes issue #16815. Reported, patched by rain)
-
-  * If there is realtime configuration, it does not get re-read on reload unless
-    the config file also changes.
-    (Closes issue #16982. Reported, patched by dmitri)
-
-  * Send AgentComplete manager event for attended transfers.
-    (Closes issue #16819. Reported, patched by elbriga)
-
-  * Correct manager variable 'EventList' case.
-    (Closes issue #17520. Reported, patched by kobaz)
-
- In addition, changes to res_timing_pthread that should make it more stable have
- also been implemented.
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.10

* Wed Jul 14 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.8-0.3.rc1
- Add patch to remove requirement on latex2html

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.6.2.8-0.2.rc1
- Mass rebuild with perl-5.12.0

* Tue May  4 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.7-1
-  * Fix building CDR and CEL SQLite3 modules.
-    (Closes issue #17017. Reported by alephlg. Patched by seanbright)
-
-  * Resolve crash in SLAtrunk when the specified trunk doesn't exist.
-    (Reported in #asterisk-dev by philipp64. Patched by seanbright)
-
-  * Include an extra newline after "Aliased CLI command" to get back the prompt.
-    (Issue #16978. Reported by jw-asterisk. Tested, patched by seanbright)
-
-  * Prevent segfault if bad magic number is encountered.
-    (Issue #17037. Reported, patched by alecdavis)
-
-  * Update code to reflect that handle_speechset has 4 arguments.
-    (Closes issue #17093. Reported, patched by gpatri. Tested by pabelanger,
-     mmichelson)
-
-  * Resolve a deadlock in chan_local.
-    (Closes issue #16840. Reported, patched by bzing2, russell. Tested by bzing2)

* Mon May  3 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.7-0.2.rc3
- Update to 1.6.2.7-rc3

* Thu Apr 15 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.7-0.1.rc2
- Update to 1.6.2.7-rc2

* Fri Mar 12 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.6-1
- Update to final 1.6.2.6
-
- The following are a few of the issues resolved by community developers:
-
-  * Make sure to clear red alarm after polarity reversal.
-    (Closes issue #14163. Reported, patched by jedi98. Tested by mattbrown,
-     Chainsaw, mikeeccleston)
-
-  * Fix problem with duplicate TXREQ packets in chan_iax2
-    (Closes issue #16904. Reported, patched by rain. Tested by rain, dvossel)
-
-  * Fix crash in app_voicemail related to message counting.
-    (Closes issue #16921. Reported, tested by whardier. Patched by seanbright)
-
-  * Overlap receiving: Automatically send CALL PROCEEDING when dialplan starts
-    (Reported, Patched, and Tested by alecdavis)
-
-  * For T.38 reINVITEs treat a 606 the same as a 488.
-    (Closes issue #16792. Reported, patched by vrban)
-
-  * Fix ConfBridge crash when no timing module is loaded.
-    (Closes issue #16471. Reported, tested by kjotte. Patched, tested by junky)
-
- For a full list of changes in this releases, please see the ChangeLog:
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.6

* Mon Mar  8 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.6-0.1.rc2
- Update to 1.6.2.6-rc2

* Mon Mar  8 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.5-2
- Add a patch that fixes CLI history when linking against external libedit.

* Thu Feb 25 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.5-1
- Update to 1.6.2.5
-
-         * AST-2010-002: Invalid parsing of ACL rules can compromise security

* Thu Feb 18 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.4-1
- Update to 1.6.2.4
-
-        * AST-2010-002: This security release is intended to raise awareness
-          of how it is possible to insert malicious strings into dialplans,
-          and to advise developers to read the best practices documents so
-          that they may easily avoid these dangers.

* Wed Feb  3 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.2-1
- Update to 1.6.2.2
-
-	* AST-2010-001: An attacker attempting to negotiate T.38 over SIP can
-	  remotely crash Asterisk by modifying the FaxMaxDatagram field of
-	  the SDP to contain either a negative or exceptionally large value.
-	  The same crash occurs when the FaxMaxDatagram field is omitted from
-	  the SDP as well.

* Fri Jan 15 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.1-1
- Update to 1.6.2.1 final:
-
- * CLI 'queue show' formatting fix.
-   (Closes issue #16078. Reported by RoadKill. Tested by dvossel. Patched by
-    ppyy.)
-
- * Fix misreverting from 177158.
-   (Closes issue #15725. Reported, Tested by shanermn. Patched by dimas.)
-
- * Fixes subscriptions being lost after 'module reload'.
-   (Closes issue #16093. Reported by jlaroff. Patched by dvossel.)
-
- * app_queue segfaults if realtime field uniqueid is NULL
-  (Closes issue #16385. Reported, Tested, Patched by haakon.)
-
- * Fix to Monitor which previously assumed the file to write to did not contain
-   pathing.
-   (Closes issue #16377, #16376. Reported by bcnit. Patched by dant.

* Tue Jan 12 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.1-0.1.rc1
- Update to 1.6.2.1-rc1

* Sat Dec 19 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-1
- Released version of 1.6.2.0

* Wed Dec  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.16.rc8
- Update to 1.6.2.0-rc8

* Wed Dec  2 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.15.rc7
- Update to 1.6.2.0-rc7

* Tue Dec  1 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.14.rc6
- Change the logrotate and the init scripts so that Asterisk doesn't
  try and write to / or /root

* Thu Nov 19 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.13.rc6
- Make dependency on uw-imap conditional and some other changes to
  make building on RHEL5 easier.

* Fri Nov 13 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.12.rc6
- Update to 1.6.2.0-rc6

* Mon Nov  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.11.rc5
- Update to 1.6.2.0-rc5

* Fri Nov  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.10.rc4
- Update to 1.6.2.0-rc4

* Tue Oct 27 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.9.rc3
- Add patch from upstream to fix how res_http_post forms paths.

* Sat Oct 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.8.rc3
- Add an AST_EXTRA_ARGS option to the init script
- have the init script to cd to /var/spool/asterisk to prevent annoying message

* Sat Oct 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.7.rc3
- Compile against gmime 2.2 instead of gmime 2.4 because the patch to convert the API calls from 2.2 to 2.4 caused crashes.

* Fri Oct  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.6.rc3
- Require latex2html used in static-http documents

* Wed Oct  7 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.5.rc3
- Change ownership and permissions on config files to protect them.

* Tue Oct  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.4.rc3
- Update to 1.6.2.0-rc3

* Wed Sep 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.3.rc2
- Merge firmware subpackage back into the main package.

* Wed Sep 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.2.rc2
- Package internal help.
- Fix up some more paths in the configs so that everything ends up where we want them.

* Wed Sep 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.1.rc2
- Update to 1.6.2.0-rc2
- We no longer need to strip the tarball as it no longer includes non-free items.

* Wed Sep  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.6-2
- Enable building of API docs.
- Depend on version 1.2 or newer of speex

* Sun Sep  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.6-1
- Update to 1.6.1.6
- Drop patches that are too troublesome to maintain anymore or have been integrated upstream.

* Tue Sep  1 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.26.rc1
- Add a patch from Quentin Armitage and rebuld.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-0.25.rc1
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.24.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.23.rc1
- Rebuild to pick up new AIS and ODBC deps.
- Update script that strips out bad content from tarball to do the
  download and to check the GPG signature.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.22.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.21.rc1
- Update to 1.6.1-rc1
- Add backport of conference bridging that is slated for 1.6.2
- Add patches to conference bridging that implement CLI apps

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-0.13.beta4
- rebuild with new openssl

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.12.beta4
- Fedora Directory Server compatibility patch/subpackage.

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.10.beta4
- Fix up paths. BZ#477238

* Sat Jan  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.9.beta4
- Update patches

* Sat Jan  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.8.beta4
- Update to 1.6.1-beta4

* Tue Dec  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.7.beta3
- Update to 1.6.1-beta3

* Tue Dec  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.6.1-0.6.beta2
- Rebuild for new gmime

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.5.beta2
- Add patch to fix missing variable on PPC.

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.4.beta2
- Update PPC systems don't have sys/io.h patch.

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.3.beta2
- PPC systems don't have sys/io.h

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.2.beta2
- Update to 1.6.1 beta 2

* Wed Nov  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0.1-3
- Fix issue with init script giving wrong path to config file.

* Thu Oct 16 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0.1-2
- Explicitly require dahdi-tools-libs to see if we can get this to build.

* Fri Oct 10 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-1
- Update to final release.

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 1.6.0-0.22.beta9
- Rebuild

* Wed Jul 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.21.beta9
- Replace app_rxfax/app_txfax with app_fax taken from upstream SVN.

* Tue Jul 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.20.beta9
- Bump release and rebuild with new libpri and zaptel.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.19.beta9
- Add patch pulled from upstream SVN that fixes AST-2008-010 and AST-2008-011.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.18.beta9
- Add patch for LDAP extracted from upstream SVN (#442011)

* Wed Jul  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.17.beta9
- Add patch that unbreaks cdr_tds with FreeTDS 0.82.
- Properly obsolete conference subpackage.

* Thu Jun 12 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.16.beta9
- Disable building cdr_tds since new FreeTDS in rawhide no longer provides needed library.

* Wed Jun 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.15.beta9
- Bump release and rebuild to fix libtds breakage.

* Mon May 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.14.beta9
- Update to 1.6.0-beta9.
- Update patches so that they apply cleanly.
- Temporarily disable app_conference patch as it doesn't compile
- config/scripts/postgres_cdr.sql has been merged into realtime_pgsql.sql
- Re-add the asterisk-strip.sh script as a source file.

* Tue Apr 22 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.13.beta8
- Update to 1.6.0-beta8
- Contains fixes for AST-2008-006 / CVE-2008-1897

* Wed Apr  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.12.beta7.1
- Return to stripped tarballs since there's more non-free content in
  the Asterisk tarballs than I thought.

* Sun Mar 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.11.beta7.1
- Update to 1.6.0-beta7.1
- Update patches
- Back out some changes that were made because beta7 was tagged from
  the wrong branch.

* Fri Mar 28 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.10.beta7
- Update to 1.6.0-beta7
- The Asterisk tarball no longer contains the iLBC code, so we can
  directly use the upstream tarball without having to modify it.
- Get rid of the asterisk-strip.sh script since it's no longer needed.
- Diable build of codec_ilbc and format_ilbc (these do not contain any
  legally suspect code so they can be included in the tarball but it's
  pointless building them).
- Update chan_mobile patch to fix API breakages.
- Add a patch to chan_usbradio to fix API breakages.

* Thu Mar 27 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.9.beta6
- Add Postgresql schemas from contrib as documentation to the Postgresql subpackage.

* Tue Mar 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.8.beta6
- Update patches.
- Add patch to compile against external libedit rather than using the
  in-tree version.
- Add -Werror-implicit-function-declaration to optflags.
- Get rid of hashtest and hashtest2 binaries that link to unfortified
  versions of *printf functions.  They are compiled with -O0 which
  somehow pulls in the wrong versions.  These programs aren't
  necessary to the operation of the package anyway.

* Wed Mar 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.6.beta6
- Update to 1.6.0-beta6 to fix some security issues.
-
- AST-2008-002 details two buffer overflows that were discovered in
- RTP codec payload type handling.
-  * http://downloads.digium.com/pub/security/AST-2008-002.pdf
-  * All users of SIP in Asterisk 1.4 and 1.6 are affected.
-
- AST-2008-003 details a vulnerability which allows an attacker to
- bypass SIP authentication and to make a call into the context
- specified in the general section of sip.conf.
-  * http://downloads.digium.com/pub/security/AST-2008-003.pdf
-  * All users of SIP in Asterisk 1.0, 1.2, 1.4, or 1.6 are affected.
-
- AST-2008-004 Logging messages displayed using the ast_verbose
- logging API call are not displayed as a character string, they are
- displayed as a format string.
-  * http://downloads.digium.com/pub/security/AST-2008-004.pdf
-
- AST-2008-005 details a problem in the way manager IDs are caculated.
-  * http://downloads.digium.com/pub/security/AST-2008-005.pdf

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-0.5.beta5
- add Requires for versioned perl (libperl.so)

* Wed Mar  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.4.beta5
- Update to 1.6.0-beta5
- Remove upstreamed patches.

* Mon Mar  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.3.beta4
- Package the directory used to store monitor recordings.

* Tue Feb 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.2.beta4
- Add patch from David Woodhouse that fixes building on PPC64.

* Tue Feb 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.1.beta4
- Update to 1.6.0 beta 4

* Wed Feb 13 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.18-1
- Update to 1.4.18.
- Use -march=i486 on i386 builds for atomic operations (GCC 4.3
  compatibility).
- Use "logger reload" instead of "logger rotate" in logrotate file
  (#432197).
- Don't explicitly specify a group in in the init script to prevent
  Zaptel breakage (#426629).
- Split app_ices out to a separate package so that the ices package
  can be required.
- pbx_kdeconsole has been dropped, don't specifically exclude it from
  the build anymore.
- Update app_conference patch.
- Drop upstreamed libcap patch.

* Wed Jan  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.17-1
- Update to 1.4.17 to fix AST-2008-001.

* Fri Dec 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.2-1
- Update to 1.4.16.2

* Sat Dec 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.1-2
- Bump release and rebuild to fix broken dep on uw-imap.

* Wed Dec 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.1-1
- Update to the real 1.4.16.1.

* Wed Dec 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-2
- Add patch to bring source up to version 1.4.16.1 which will be
  released shortly to fix some crasher bugs introduced by 1.4.16.

* Tue Dec 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-1
- Update to 1.4.16 to fix security bug.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-7
- Really, really fix the build problems on devel.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-6
- Tweaks to get to build on x86_64

* Wed Dec 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-5
- Exclude PPC64

* Wed Dec 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-4
- Don't build apidocs by default since there's a problem building on x86_64.

* Tue Dec 11 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-3
- Really get rid of zero length map files.

* Mon Dec 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-2
- Get rid of zero length map files.
- Shorten descriptions of voicemail subpackages

* Fri Nov 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-1
- Update to 1.4.15

* Tue Nov 20 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-2
- Fix license and other rpmlint warnings.

* Mon Nov 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-1
- Update to 1.4.14

* Fri Nov 16 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-7
- Add chan_mobile

* Tue Nov 13 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-6
- Don't build cdr_sqlite because sqlite2 has been orphaned.
- Rebase local patches to latest upstream SVN
- Update app_conference patch to latest from upstream SVN
- Apply post-1.4.13 patches from upstream SVN

* Wed Oct 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-1
- Update to 1.4.13

* Tue Oct  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.12.1-1
- Update to 1.4.12.1

* Wed Aug 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.11-1
- Update to 1.4.11

* Fri Aug 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.10.1-1
- Update to 1.4.10.1.

* Tue Aug  7 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.10-1
- Update to 1.4.10 (security update).

* Tue Aug  7 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-7
- Add a patch that allows alternate extensions to be defined in users.conf

* Mon Aug  6 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-6
- Update app_conference patch. Enter/leave sounds are now possible.

* Fri Jul 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-5
- Update patches so we don't need to run auto* tools, because autoconf
  2.60 is required and FC-6 and RHEL5 only have autoconf 2.59.

* Thu Jul 26 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-4
- Don't build app_mp3

* Wed Jul 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-3
- Add app_conference

* Wed Jul 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-2
- Use plain useradd/groupadd rather than the fedora-usermgmt
- Clean up requirements
- Clean up build requirements by moving them to package sections

* Tue Jul 24 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-1
- Update to 1.4.9

* Tue Jul 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.8-1
- Update to 1.4.8
- Drop ixjuser patch.

* Tue Jul 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.7.1-1
- Update to 1.4.7.1

* Mon Jul  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.7-1
- Update to 1.4.7
- RxFAX/TxFAX applications

* Sun Jul  1 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-4
- It's "sbin", not "bin" silly.

* Sat Jun 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-3
- Add patch that lets us change TOS bits even when running non-root

* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-2
- voicemail needs to require /usr/bin/sox and /usr/bin/sendmail

* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-1
- Update to 1.4.6
- Remove upstreamed patch.

* Thu Jun 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-10
- Build the IMAP and ODBC storage options of voicemail and split
  voicemail out into subpackages.
- Apply patch so that the system UW IMAP libray can be linked against.
- Patch modules.conf.sample so that alternal voicemail modules don't
  get loaded simultaneously.
- Link against system GSM library rather than internal copy.
- Patch the Makefile so that it doesn't add redundant/wrong compiler
  options.
- Force building with the standard RPM optimization flags.
- Install the Asterisk MIB in a location that net-snmp can find it.
- Only package docs in the main package that are relevant and that
  haven't been packaged by a subpackage.
- Other minor cleanups.

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-9
- Move sounds

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-8
- Update some more ownership/permissions

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-7
- Fix some permissions.

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-6
- Update init script patch
- Move pid file to subdir of /var/run

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-5
- Update init script patch to run as non-root

* Sun Jun 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-4
- Build modules that depend on FreeTDS.
- Don't build voicemail with ODBC storage.

* Sun Jun 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-3
- Have the build output the commands executing, rather than covering them up.

* Fri Jun 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-1
- Update to 1.4.5
- Remove upstreamed patch.

* Wed May  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.4-2
- Add a patch to fix CVE-2007-2488/ASA-2007-013

* Fri Apr 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.4-1
- Update to 1.4.4

* Wed Mar 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.2-1
- Update to 1.4.2

* Tue Mar  6 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.1-2
- Package the IAXy firmware
- Minor clean-ups in files

* Mon Mar  5 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.1-1
- Update to 1.4.1
- Don't build/package codec_zap (zaptel 1.4.0 doesn't support it)

* Fri Dec 15 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-6.beta4
- Update to 1.4.0-beta4
- Various cleanups.

* Fri Oct 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-5.beta3
- Don't package IAXy firmware because of license
- Don't build app_rpt
- Don't BR lm_sensors on PPC
- Better way to prevent download/installation of sound archives
- Redo tarball to eliminate non-free items

* Thu Oct 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-4.beta3
- Remove explicit dependency on glibc-kernheaders.
- Build jabber modules on PPC

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-3.beta3
- *Really* update to beta3
- chan_jingle has been taken out of 1.4
- Move misplaced binaries to where they should be

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-2.beta3
- Remove requirement on asterisk-sounds-core until licensing can be
  figured out.

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-1.beta3
- Update to 1.4.0-beta3

* Sun Oct 15 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-0.beta2
- Update to 1.4.0-beta2

* Tue Jul 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.10-1
- Update to 1.2.10.

* Wed Jun  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.9.1
- Update to 1.2.9.1

* Fri Jun  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.8
- Update to 1.2.8
- Add misdn.conf to list of configs.
- Drop chan_bluetooth patch for now...

* Tue May  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-6
- Zaptel subpackage shouldn't obsolete the sqlite subpackage.
- Remove mISDN until build issues can be figured out.

* Mon Apr 24 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-5
- Build mISDN channel drivers, modelled after spec file from David Woodhouse

* Thu Apr 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-4
- Update chan_bluetooth patch with some additional information as to
  it's source and comment out more in the configuration file.

* Thu Apr 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-3
- Add chan_bluetooth

* Wed Apr 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-2
- Split off more stuff into subpackages.

* Wed Apr 12 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7-1
- Update to 1.2.7

* Mon Apr 10 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-3
- Fix detection of libpri on 64 bit arches (taken from Matthias Saou's rpmforge package)
- Change sqlite subpackage name to sqlite2 (there are sqlite3 modules in development).

* Thu Apr  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-2
- Don't build GTK 1.X console since GTK 1.X is being moved out of core...

* Mon Mar 27 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-1
- Update to 1.2.6

* Mon Mar  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.5-1
- Update to 1.2.5.
- Removed upstreamed MOH patch.
- Add full urls to the app_(r|t)xfax.c sources.
- Update spandsp patch.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-4
- Actually apply the patch.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-3
- Add patch to keep Asterisk from crashing when using MOH inside a MeetMe conference.

* Mon Feb  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-2
- BR sqlite2-devel

* Tue Jan 31 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-1
- Update to 1.2.4.

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-4
- Took some tricks from Asterisk packages by Roy-Magne Mo.
-   Enable gtk console module.
-   BR gtk+-devel.
-   Add logrotate script.
-   BR sqlite2-devel and new sqlite subpackage.
-   BR doxygen and graphviz for building duxygen documentation. (But don't build it yet.)

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-3
- Completely eliminate the "asterisk" user from the spec file.
- Move more config files to subpackages.
- Consolidate two patches that patch the init script.
- BR curl-devel
- BR alsa-lib-devel
- alsa, curl, oss subpackages

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-2
- Do not run as user "asterisk" as that prevents setting of IP TOS (which is bad for quality of service).
- Add patch for setting TOS separately for SIP and RTP packets.

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-1
- First version for Fedora Extras.

