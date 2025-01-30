%global username    saslauth

%global _plugindir2 %{_libdir}/sasl2
%global bootstrap_cyrus_sasl 0
%global bdb_migration %[!(0%{?rhel} >= 10)]
%global gdbm_db_file /etc/sasl2/sasldb2

Summary: The Cyrus SASL library
Name: cyrus-sasl
Version: 2.1.28
Release: %autorelease
License: BSD-Attribution-HPND-disclaimer
URL: https://www.cyrusimap.org/sasl/

# Source0 originally comes from https://www.cyrusimap.org/releases/;
# make-no-dlcompatorsrp-tarball.sh removes the "dlcompat" subdirectory and builds a
# new tarball.
Source0: cyrus-sasl-%{version}-nodlcompatorsrp.tar.gz
Source3: saslauth.sysusers
Source5: saslauthd.service
Source7: sasl-mechlist.c
Source9: saslauthd.sysconfig
Source10: make-no-dlcompatorsrp-tarball.sh
# From upstream git, required for reconfigure after applying patches to configure.ac
# https://raw.githubusercontent.com/cyrusimap/cyrus-sasl/master/autogen.sh
Source11: autogen.sh


Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Patch11: cyrus-sasl-2.1.25-no_rpath.patch
Patch15: cyrus-sasl-2.1.20-saslauthd.conf-path.patch
Patch23: cyrus-sasl-2.1.23-man.patch
Patch24: cyrus-sasl-2.1.21-sizes.patch
# The 64 bit *INT8 type is not used anywhere and other types match
Patch49: cyrus-sasl-2.1.26-md5global.patch

Patch101: cyrus-sasl-2.1.27-Add-basic-test-infrastructure.patch
Patch102: cyrus-sasl-2.1.27-Add-Channel-Binding-support-for-GSSAPI-GSS-SPNEGO.patch
#https://github.com/simo5/cyrus-sasl/commit/ebd2387f06c84c7f9aac3167ec041bb01e5c6e48
Patch106: cyrus-sasl-2.1.27-nostrncpy.patch
# Upstream PR: https://github.com/cyrusimap/cyrus-sasl/pull/635
Patch107: cyrus-sasl-2.1.27-more-tests.patch
Patch108: cyrus-sasl-2.1.27-Add-support-for-setting-max-ssf-0-to-GSS-SPNEGO.patch
#Migration tool should be removed from Fedora 36
Patch109: cyrus-sasl-2.1.27-Migration-from-BerkeleyDB.patch
Patch500: cyrus-sasl-2.1.27-coverity.patch
Patch501: cyrus-sasl-2.1.27-cumulative-digestmd5.patch
Patch502: cyrus-sasl-2.1.27-cumulative-ossl3.patch
Patch503: cyrus-sasl-2.1.28-SAST.patch

Patch599: cyrus-sasl-2.1.28-fedora-c99.patch
Patch600: cyrus-sasl-2.1.28-gcc15.patch

BuildRequires: autoconf, automake, libtool, gdbm-devel, groff
BuildRequires: krb5-devel >= 1.2.2, openssl-devel, pam-devel, pkgconfig
BuildRequires: mariadb-connector-c-devel, libpq-devel, zlib-devel
%if ! %{bootstrap_cyrus_sasl}
BuildRequires: openldap-devel
%endif
%if %{bdb_migration}
#build reqs for migration from BerkeleyDB
BuildRequires: libdb-devel-static
%endif
#build reqs for make check
BuildRequires: python3 nss_wrapper socket_wrapper krb5-server
BuildRequires: make
Requires(pre): /usr/sbin/useradd /usr/sbin/groupadd
Requires(postun): /usr/sbin/userdel /usr/sbin/groupdel
Requires: /sbin/nologin
Provides: user(%username)
Provides: group(%username)

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/saslauthd
%endif

%description
The %{name} package contains the Cyrus implementation of SASL.
SASL is the Simple Authentication and Security Layer, a method for
adding authentication support to connection-based protocols.

%package lib
Summary: Shared libraries needed by applications which use Cyrus SASL

%description lib
The %{name}-lib package contains shared libraries which are needed by
applications which use the Cyrus SASL library.

%package devel
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Summary: Files needed for developing applications with Cyrus SASL

%description devel
The %{name}-devel package contains files needed for developing and
compiling applications which use the Cyrus SASL library.

%package gssapi
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: GSSAPI authentication support for Cyrus SASL

%description gssapi
The %{name}-gssapi package contains the Cyrus SASL plugins which
support GSSAPI authentication. GSSAPI is commonly used for Kerberos
authentication.

%package plain
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: PLAIN and LOGIN authentication support for Cyrus SASL

%description plain
The %{name}-plain package contains the Cyrus SASL plugins which support
PLAIN and LOGIN authentication schemes.

%package md5
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: CRAM-MD5 and DIGEST-MD5 authentication support for Cyrus SASL

%description md5
The %{name}-md5 package contains the Cyrus SASL plugins which support
CRAM-MD5 and DIGEST-MD5 authentication schemes.

# This would more appropriately be named cyrus-sasl-auxprop-sql.
%package sql
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: SQL auxprop support for Cyrus SASL

%description sql
The %{name}-sql package contains the Cyrus SASL plugin which supports
using a RDBMS for storing shared secrets.

%if ! %{bootstrap_cyrus_sasl}
# This was *almost* named cyrus-sasl-auxprop-ldapdb, but that's a lot of typing.
%package ldap
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: LDAP auxprop support for Cyrus SASL

%description ldap
The %{name}-ldap package contains the Cyrus SASL plugin which supports using
a directory server, accessed using LDAP, for storing shared secrets.
%endif

%package scram
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: SCRAM auxprop support for Cyrus SASL

%description scram
The %{name}-scram package contains the Cyrus SASL plugin which supports
the SCRAM authentication scheme.

%package gs2
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: GS2 support for Cyrus SASL

%description gs2
The %{name}-gs2 package contains the Cyrus SASL plugin which supports
the GS2 authentication scheme.

###


%prep
%setup -q -n cyrus-sasl-%{version}
%patch -P11 -p1 -b .no_rpath
%patch -P15 -p1 -b .path
%patch -P23 -p1 -b .man
%patch -P24 -p1 -b .sizes
%patch -P49 -p1 -b .md5global.h
%patch -P101 -p1 -b .tests
%patch -P102 -p1 -b .gssapi_cbs
%patch -P106 -p1 -b .nostrncpy
%patch -P107 -p1 -b .moretests
%patch -P108 -p1 -b .maxssf0
%if %{bdb_migration}
%patch -P109 -p1 -b .frombdb
%endif
%patch -P500 -p1 -b .coverity
%patch -P501 -p1 -b .digestmd5
%patch -P502 -p1 -b .ossl3
%patch -P503 -p1 -b .sast
%patch -P599 -p1 -b .c99
%patch -P600 -p1 -b .gcc15

%build
# reconfigure
cp %{SOURCE11} ./
rm configure aclocal.m4 config/ltmain.sh Makefile.in
export NOCONFIGURE=yes
sh autogen.sh

%set_build_flags
# Find Kerberos.
krb5_prefix=`krb5-config --prefix`
if test x$krb5_prefix = x%{_prefix} ; then
        krb5_prefix=
else
        CPPFLAGS="-I${krb5_prefix}/include $CPPFLAGS"; export CPPFLAGS
        LDFLAGS="-L${krb5_prefix}/%{_lib} $LDFLAGS"; export LDFLAGS
fi

# Find OpenSSL.
LIBS="-lcrypt"; export LIBS
if pkg-config openssl ; then
        CPPFLAGS="`pkg-config --cflags-only-I openssl` $CPPFLAGS"; export CPPFLAGS
        LDFLAGS="`pkg-config --libs-only-L openssl` $LDFLAGS"; export LDFLAGS
fi

# Find the MySQL libraries used needed by the SQL auxprop plugin.
INC_DIR="`mysql_config --include`"
if test x"$INC_DIR" != "x-I%{_includedir}"; then
        CPPFLAGS="$INC_DIR $CPPFLAGS"; export CPPFLAGS
fi
LIB_DIR="`mysql_config --libs | sed -e 's,-[^L][^ ]*,,g' -e 's,^ *,,' -e 's, *$,,' -e 's,  *, ,g'`"
if test x"$LIB_DIR" != "x-L%{_libdir}"; then
        LDFLAGS="$LIB_DIR $LDFLAGS"; export LDFLAGS
fi

# Find the PostgreSQL libraries used needed by the SQL auxprop plugin.
INC_DIR="-I`pg_config --includedir`"
if test x"$INC_DIR" != "x-I%{_includedir}"; then
        CPPFLAGS="$INC_DIR $CPPFLAGS"; export CPPFLAGS
fi
LIB_DIR="-L`pg_config --libdir`"
if test x"$LIB_DIR" != "x-L%{_libdir}"; then
        LDFLAGS="$LIB_DIR $LDFLAGS"; export LDFLAGS
fi

# run "make check" against the built library rather than the one in buildroot
LDFLAGS="-Wl,--enable-new-dtags $LDFLAGS"; export LDFLAGS

echo "$CFLAGS"
echo "$CPPFLAGS"
echo "$LDFLAGS"

%configure \
        --enable-shared --disable-static \
        --disable-java \
        --with-plugindir=%{_plugindir2} \
        --with-configdir=%{_plugindir2}:%{_sysconfdir}/sasl2 \
        --disable-krb4 \
        --enable-gssapi${krb5_prefix:+=${krb5_prefix}} \
        --with-gss_impl=mit \
        --with-rc4 \
        --with-dblib=gdbm \
        --with-dbpath=%{gdbm_db_file} \
        --with-saslauthd=/run/saslauthd --without-pwcheck \
%if ! %{bootstrap_cyrus_sasl}
        --with-ldap \
%endif
        --with-devrandom=/dev/urandom \
        --enable-anon \
        --enable-cram \
        --enable-digest \
        --disable-ntlm \
        --enable-plain \
        --enable-login \
        --enable-alwaystrue \
        --enable-httpform \
        --disable-otp \
%if ! %{bootstrap_cyrus_sasl}
        --enable-ldapdb \
%endif
        --enable-sql --with-mysql=yes --with-pgsql=yes \
        --without-sqlite \
        --enable-auth-sasldb \
        "$@"
make sasldir=%{_plugindir2}
make -C saslauthd testsaslauthd
make -C sample

# Build a small program to list the available mechanisms, because I need it.
pushd lib
../libtool --mode=link %{__cc} -o sasl2-shared-mechlist -I../include $CFLAGS %{SOURCE7} $LDFLAGS ./libsasl2.la


%install
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT sasldir=%{_plugindir2}
make install DESTDIR=$RPM_BUILD_ROOT sasldir=%{_plugindir2} -C plugins

install -m755 -d $RPM_BUILD_ROOT%{_bindir}
./libtool --mode=install \
install -m755 sample/client $RPM_BUILD_ROOT%{_bindir}/sasl2-sample-client
./libtool --mode=install \
install -m755 sample/server $RPM_BUILD_ROOT%{_bindir}/sasl2-sample-server
%if %{bdb_migration} && "%{_sbindir}" != "%{_bindir}"
mv $RPM_BUILD_ROOT%{_sbindir}/cyrusbdb2current $RPM_BUILD_ROOT%{_bindir}/cyrusbdb2current
%endif
./libtool --mode=install \
install -m755 saslauthd/testsaslauthd $RPM_BUILD_ROOT%{_sbindir}/testsaslauthd

# Install the saslauthd mdoc page in the expected location.  Sure, it's not
# really a man page, but groff seems to be able to cope with it.
install -m755 -d $RPM_BUILD_ROOT%{_mandir}/man8/
install -m644 -p saslauthd/saslauthd.mdoc $RPM_BUILD_ROOT%{_mandir}/man8/saslauthd.8
install -m644 -p saslauthd/testsaslauthd.8 $RPM_BUILD_ROOT%{_mandir}/man8/testsaslauthd.8

# Install the systemd unit file for saslauthd and the config file.
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir} $RPM_BUILD_ROOT/etc/sysconfig
install -m644 -p %{SOURCE5} $RPM_BUILD_ROOT/%{_unitdir}/saslauthd.service
install -m644 -p %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/saslauthd

# Install the config dirs if they're not already there.
install -m755 -d $RPM_BUILD_ROOT/%{_sysconfdir}/sasl2
install -m755 -d $RPM_BUILD_ROOT/%{_plugindir2}

# Provide an easy way to query the list of available mechanisms.
./libtool --mode=install \
install -m755 lib/sasl2-shared-mechlist $RPM_BUILD_ROOT/%{_sbindir}/

# Sysusers file
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/cyrus-sasl.conf

# Remove unpackaged files from the buildroot.
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/libotp.*
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_mandir}/cat8/saslauthd.8

%check
make check %{?_smp_mflags}

%pre
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post saslauthd.service

%preun
%systemd_preun saslauthd.service

%postun
%systemd_postun_with_restart saslauthd.service

%ldconfig_scriptlets lib

%files
%doc saslauthd/LDAP_SASLAUTHD
%{_mandir}/man8/*
%{_sbindir}/pluginviewer
%{_sbindir}/saslauthd
%{_sbindir}/testsaslauthd
%config(noreplace) /etc/sysconfig/saslauthd
%{_unitdir}/saslauthd.service
%ghost %attr(755,root,root) /run/saslauthd
%{_sysusersdir}/cyrus-sasl.conf

%files lib
%license COPYING
%doc AUTHORS doc/html/*.html
%{_libdir}/libsasl*.so.*
%dir %{_sysconfdir}/sasl2
%dir %{_plugindir2}/
%{_plugindir2}/*anonymous*.so*
%{_plugindir2}/*sasldb*.so*
%{_sbindir}/saslpasswd2
%{_sbindir}/sasldblistusers2
%if %{bdb_migration}
%{_bindir}/cyrusbdb2current
%endif

%files plain
%{_plugindir2}/*plain*.so*
%{_plugindir2}/*login*.so*

%if ! %{bootstrap_cyrus_sasl}
%files ldap
%{_plugindir2}/*ldapdb*.so*
%endif

%files md5
%{_plugindir2}/*crammd5*.so*
%{_plugindir2}/*digestmd5*.so*

%files sql
%{_plugindir2}/*sql*.so*

%files gssapi
%{_plugindir2}/*gssapi*.so*

%files scram
%{_plugindir2}/libscram.so*

%files gs2
%{_plugindir2}/libgs2.so*

%files devel
%{_bindir}/sasl2-sample-client
%{_bindir}/sasl2-sample-server
%{_includedir}/*
%{_libdir}/libsasl*.*so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%{_sbindir}/sasl2-shared-mechlist

%changelog
%autochangelog
